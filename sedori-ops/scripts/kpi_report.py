"""KPI集計（docs/05_kpi.md の定義）。

sales.csv / inventory.csv / contacts.csv から、期間内の売上・粗利・粗利率・ROI・返品率・
滞留在庫比率・一次返信SLA遵守率を集計して表示します。

使い方:
    python3 sedori-ops/scripts/kpi_report.py --period month            # 今月（JST）
    python3 sedori-ops/scripts/kpi_report.py --period week             # 直近7日
    python3 sedori-ops/scripts/kpi_report.py --from 2026-09-01 --to 2026-09-30
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from datetime import date, datetime, timedelta, timezone

from sedori_config import OPS_ROOT, load_config

JST = timezone(timedelta(hours=9))
DATA = os.path.join(OPS_ROOT, "data")


def _read(name: str) -> list[dict]:
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _d(v: str | None) -> date | None:
    if not v:
        return None
    try:
        return datetime.fromisoformat(v.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return date.fromisoformat(v[:10])
        except ValueError:
            return None


def _f(v, default=0.0) -> float:
    try:
        return float(v) if v not in (None, "") else default
    except ValueError:
        return default


def _hours_between(a: str | None, b: str | None) -> float | None:
    try:
        ta = datetime.fromisoformat(a)  # type: ignore[arg-type]
        tb = datetime.fromisoformat(b)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return (tb - ta).total_seconds() / 3600


def period_range(period: str | None, d_from: str | None, d_to: str | None) -> tuple[date, date]:
    today = datetime.now(JST).date()
    if d_from or d_to:
        return (date.fromisoformat(d_from) if d_from else date(2000, 1, 1), date.fromisoformat(d_to) if d_to else today)
    if period == "week":
        return today - timedelta(days=6), today
    return today.replace(day=1), today


def report(cfg: dict, start: date, end: date) -> dict:
    t = cfg["targets"]
    sales = [r for r in _read("sales.csv") if (d := _d(r.get("sold_at"))) and start <= d <= end]
    sold = [r for r in sales if r.get("returned", "0") != "1"]
    returned = [r for r in sales if r.get("returned", "0") == "1"]

    revenue = sum(_f(r["sale_price"]) * _f(r.get("qty"), 1) for r in sold)
    cogs = sum(_f(r["unit_cost"]) * _f(r.get("qty"), 1) for r in sold)
    fees = sum((_f(r.get("referral_fee")) + _f(r.get("fba_fee")) + _f(r.get("other_fee")) + _f(r.get("shipping_cost"))) for r in sold)
    refund_loss = sum(_f(r.get("refund_amount")) for r in returned)
    gross = revenue - cogs - fees - refund_loss
    units = sum(_f(r.get("qty"), 1) for r in sold)

    inv = [r for r in _read("inventory.csv") if r.get("status") in ("in_stock", "stranded")]
    inv_value = sum(_f(r["unit_cost"]) * _f(r.get("qty_available")) for r in inv)
    stale_value = sum(
        _f(r["unit_cost"]) * _f(r.get("qty_available")) for r in inv if _f(r.get("days_in_stock")) > float(t["sell_through_days_max"])
    )
    days = max((end - start).days + 1, 1)
    turnover_days = (inv_value / (cogs / days)) if cogs > 0 else None

    contacts = [r for r in _read("contacts.csv") if (d := _d(r.get("received_at"))) and start <= d <= end]
    sla = float(cfg["communication"]["response_sla_hours"])
    answered = [r for r in contacts if r.get("reply_sent_at")]
    within = [r for r in answered if (h := _hours_between(r.get("received_at"), r.get("reply_sent_at"))) is not None and h <= sla]

    return {
        "period": f"{start} 〜 {end}",
        "売上": revenue,
        "粗利": gross,
        "粗利率": (gross / revenue) if revenue else None,
        "ROI": (gross / cogs) if cogs else None,
        "販売数": units,
        "返品率": (len(returned) / len(sales)) if sales else None,
        "在庫金額": inv_value,
        "滞留在庫比率": (stale_value / inv_value) if inv_value else None,
        "在庫回転日数": turnover_days,
        "受信数": len(contacts),
        "一次返信SLA遵守率": (len(within) / len(contacts)) if contacts else None,
        "targets": {
            "売上": float(t["monthly_revenue_jpy"]),
            "粗利": float(t["monthly_gross_profit_jpy"]),
            "粗利率": float(t["gross_margin_min"]),
            "ROI": float(t["roi_min"]),
            "在庫回転日数": float(t["sell_through_days_max"]),
        },
    }


def _fmt(v, kind: str) -> str:
    if v is None:
        return "—"
    if kind == "pct":
        return f"{v:.1%}"
    if kind == "days":
        return f"{v:.0f}日"
    if kind == "int":
        return f"{v:,.0f}"
    return f"{v:,.0f}円"


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--period", choices=["week", "month"], default="month")
    p.add_argument("--from", dest="d_from")
    p.add_argument("--to", dest="d_to")
    a = p.parse_args(argv)
    cfg = load_config()
    start, end = period_range(a.period, a.d_from, a.d_to)
    r = report(cfg, start, end)
    tg = r["targets"]
    rows = [
        ("売上", _fmt(r["売上"], "yen"), _fmt(tg["売上"], "yen") if a.period == "month" else "—"),
        ("粗利", _fmt(r["粗利"], "yen"), _fmt(tg["粗利"], "yen") if a.period == "month" else "—"),
        ("粗利率", _fmt(r["粗利率"], "pct"), f"≥ {tg['粗利率']:.0%}"),
        ("ROI", _fmt(r["ROI"], "pct"), f"≥ {tg['ROI']:.0%}"),
        ("販売数", _fmt(r["販売数"], "int"), "—"),
        ("返品率", _fmt(r["返品率"], "pct"), "≤ 3%"),
        ("在庫金額", _fmt(r["在庫金額"], "yen"), "—"),
        ("滞留在庫比率", _fmt(r["滞留在庫比率"], "pct"), "≤ 20%"),
        ("在庫回転日数", _fmt(r["在庫回転日数"], "days"), f"≤ {tg['在庫回転日数']:.0f}日"),
        ("受信数", _fmt(r["受信数"], "int"), "—"),
        ("一次返信SLA遵守率", _fmt(r["一次返信SLA遵守率"], "pct"), "≥ 95%"),
    ]
    print(f"KPIレポート {r['period']}")
    print(f"{'指標':<14}{'実績':>14}{'目標':>14}")
    for k, v, g in rows:
        print(f"{k:<14}{v:>14}{g:>14}")
    if not r["販売数"]:
        print("※ 期間内の売上データがありません（sales.csv）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
