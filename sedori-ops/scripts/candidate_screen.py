"""candidates.csv の一括スクリーニング。

各行について profit_calc で粗利・粗利率・ROI を計算し、docs/02_research_criteria.md の
スコアリング（100点満点）を付け、必須条件を満たさない行には notes に理由を追記します。
decision 列は自動では変えません（director / 事業主の判断領域）。

使い方:
    python3 sedori-ops/scripts/candidate_screen.py            # 結果を表示（書き込みなし）
    python3 sedori-ops/scripts/candidate_screen.py --write    # gross_profit/gross_margin/roi/score を CSV に書き戻す
    python3 sedori-ops/scripts/candidate_screen.py --file path/to/other.csv
"""
from __future__ import annotations

import argparse
import csv
import os
import statistics
import sys

from profit_calc import calc
from sedori_config import OPS_ROOT, load_config

DEFAULT_FILE = os.path.join(OPS_ROOT, "data", "candidates.csv")


def _num(v, default=None):
    try:
        return float(v) if v not in (None, "") else default
    except ValueError:
        return default


def _interp(x: float, points: list[tuple[float, float]]) -> float:
    """折れ線補間。points は (x, y) 昇順。範囲外は端の値。"""
    if x <= points[0][0]:
        return points[0][1]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return points[-1][1]


def score_row(cfg: dict, row: dict, r: dict) -> tuple[float, list[str]]:
    t, rs = cfg["targets"], cfg["research"]
    notes: list[str] = []
    roi_min = float(t["roi_min"])
    sales_min = float(rs["min_monthly_sales_estimate"])

    # 収益性 30
    s_profit = _interp(r["roi"] / roi_min if roi_min else 0, [(1, 15), (1.5, 22), (2, 30)]) if r["roi"] >= roi_min else 0

    # 回転 25（月販推定が無ければ上限12）
    est = _num(row.get("est_monthly_sales"))
    if est is None:
        s_turn = 12 if _num(row.get("rank")) is not None else 0
        notes.append("月販推定なし: 回転スコア上限12")
    else:
        s_turn = _interp(est / sales_min if sales_min else 0, [(1, 12), (2, 20), (3, 25)]) if est >= sales_min else 0

    # 競合 20
    fba = _num(row.get("fba_sellers"))
    if fba is None:
        s_comp, note = 0, "FBA出品者数なし"
        notes.append(note)
    elif fba <= 2:
        s_comp = 20
    elif fba <= 4:
        s_comp = 15
    elif fba <= 6:
        s_comp = 10
    elif fba <= float(rs["max_fba_sellers"]):
        s_comp = 5
    else:
        s_comp = 0

    # 価格安定性 15（90日中央値と現在価格の乖離で代用。履歴が無ければ 5）
    med = _num(row.get("price_90d_median"))
    price = _num(row.get("sell_price"), 0)
    if med and price:
        cv = abs(price - med) / med
        s_stab = 15 if cv <= 0.10 else 10 if cv <= 0.20 else 5 if cv <= 0.30 else 0
    else:
        s_stab = 5
        notes.append("90日中央値なし: 安定性スコア5")

    # リスク 10（compliance_flags が空なら10、あれば0）
    flags = (row.get("compliance_flags") or "").strip()
    s_risk = 0 if flags else 10

    total = s_profit + s_turn + s_comp + s_stab + s_risk
    return round(total, 1), notes


def hard_filters(cfg: dict, row: dict, r: dict) -> list[str]:
    rs = cfg["research"]
    fails = list(r["fails"])
    fba = _num(row.get("fba_sellers"))
    if fba is not None and fba > float(rs["max_fba_sellers"]):
        fails.append(f"FBA出品者 {int(fba)} > {rs['max_fba_sellers']}")
    if (row.get("compliance_flags") or "").strip():
        fails.append("compliance NG: " + row["compliance_flags"])
    if row.get("condition") == "used" and not cfg["business"].get("handles_used_goods"):
        fails.append("中古品は未解禁（古物商許可）")
    return fails


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--file", default=DEFAULT_FILE)
    p.add_argument("--write", action="store_true", help="計算結果を CSV に書き戻す")
    a = p.parse_args(argv)

    cfg = load_config()
    with open(a.file, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    summary = []
    for row in rows:
        cost = _num(row.get("source_price"))
        price = _num(row.get("sell_price"))
        med = _num(row.get("price_90d_median"))
        if cost is None or price is None:
            summary.append((row.get("candidate_id"), None, ["source_price / sell_price が未入力"]))
            continue
        use_price = min(price, med) if med else price  # 値崩れ対策: 中央値と現在価格の低い方
        qty_limit = int(_num(row.get("source_qty_limit"), 1) or 1)
        r = calc(
            cfg,
            cost,
            use_price,
            row.get("category") or None,
            row.get("size_tier") or None,
            None,
            max(qty_limit, 1),
            _num(row.get("source_shipping"), 0.0),
            _num(row.get("points_jpy"), 0.0),
            row.get("platform") or "amazon",
        )
        fails = hard_filters(cfg, row, r)
        score, notes = score_row(cfg, row, r)
        if fails:
            score = min(score, 49.0)  # 必須条件NGは推奨ライン(70)に届かないようにする
        row["gross_profit"] = f"{r['gross_profit']:.0f}"
        row["gross_margin"] = f"{r['gross_margin']:.3f}"
        row["roi"] = f"{r['roi']:.3f}"
        row["score"] = f"{score:.0f}"
        auto_note = "; ".join(notes + fails + r["warnings"])
        if auto_note:
            base = (row.get("notes") or "").split(" | auto:")[0]
            row["notes"] = f"{base} | auto: {auto_note}".strip(" |")
        summary.append((row.get("candidate_id"), score, fails))

    verdicts = []
    for cid, score, fails in summary:
        if score is None:
            verdicts.append(f"{cid}: 計算不可（{'; '.join(fails)}）")
        else:
            v = "推奨" if score >= 70 and not fails else ("不採用" if fails else "保留")
            verdicts.append(f"{cid}: score={score:.0f} {v}" + (f"（{'; '.join(fails)}）" if fails else ""))
    print("\n".join(verdicts) if verdicts else "候補がありません")

    if a.write:
        with open(a.file, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
        print(f"書き込み完了: {a.file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
