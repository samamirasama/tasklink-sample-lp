"""利益・ROI計算（1SKU）。

business.yaml の手数料率・送料・返品率・ポイント方針を使って、
docs/02_research_criteria.md の式で粗利・粗利率・ROI を計算します。

使い方:
    python3 sedori-ops/scripts/profit_calc.py --cost 2980 --price 4980 \
        --category "家電＆カメラ" --size standard_1 --days 30 --qty 3 --shipping 0 --points 0

    # JSON 出力（candidate_screen.py などから利用）
    python3 sedori-ops/scripts/profit_calc.py --cost 2980 --price 4980 --json

期待出力（例。手数料表が未記入なら FBA配送代行は 0 で計算し、警告を出します）:
    売上                4,980
    販売手数料 (8.4%)    -418
    ...
    粗利                 ○○○   粗利率 ○○%   ROI ○○%
    判定: OK / NG（理由）
"""
from __future__ import annotations

import argparse
import json
import sys

from sedori_config import load_config, load_fba_fees, referral_rate


def calc(
    cfg: dict,
    cost: float,
    price: float,
    category: str | None = None,
    size_tier: str | None = None,
    days: float | None = None,
    qty: int = 1,
    shipping: float = 0.0,
    points: float = 0.0,
    platform: str = "amazon",
    fba_fee_override: float | None = None,
) -> dict:
    """1個あたりの損益内訳を返す。金額は円、率は小数。"""
    warnings: list[str] = []
    t = cfg["targets"]
    ship = cfg["shipping"]
    src = cfg["sourcing"]
    days = float(days if days is not None else t["sell_through_days_max"])

    # 販売手数料
    if platform == "amazon":
        rate, rate_src = referral_rate(cfg, category)
        if rate_src == "default":
            warnings.append("販売手数料はカテゴリ未登録のため default 率を使用")
        if not cfg["selling_platforms"]["amazon"].get("fee_rates_verified_on"):
            warnings.append("fee_rates_verified_on が未記入（手数料率は未確認値）")
    else:
        rate = float(cfg["selling_platforms"][platform]["fee_rate"])
    referral_fee = price * rate

    # FBA配送代行
    fba_fee = 0.0
    if platform == "amazon" and cfg["selling_platforms"]["amazon"].get("fulfillment") == "FBA":
        if fba_fee_override is not None:
            fba_fee = float(fba_fee_override)
        else:
            fees = load_fba_fees(cfg)
            row = fees.get(size_tier or "")
            if row and row["fee_jpy"] > 0:
                fba_fee = float(row["fee_jpy"])
                if not row["verified_on"]:
                    warnings.append(f"FBA手数料 {size_tier} は verified_on が未記入")
            else:
                warnings.append(f"FBA手数料 {size_tier or '(未指定)'} が未設定のため 0 で計算。実費を fba_fees に記入すること")
        storage = float(cfg["selling_platforms"]["amazon"]["monthly_storage_fee_per_unit_jpy"]) * days / 30.0
        inbound = float(ship["inbound_to_fba_per_unit_jpy"]) + float(ship["packaging_per_unit_jpy"])
    else:
        storage = 0.0
        inbound = float(ship["packaging_per_unit_jpy"])  # 自己発送の送料は price に含めない前提。必要なら --shipping-out を追加
    return_reserve = price * float(ship["return_rate_assumed"])

    unit_cost = cost + (shipping / qty if qty else shipping)
    point_credit = 0.0
    if src.get("include_points_in_profit") and points:
        point_credit = points * float(src.get("points_haircut", 1.0))
    effective_cost = unit_cost - point_credit

    gross = price - referral_fee - fba_fee - storage - inbound - return_reserve - effective_cost
    margin = gross / price if price else 0.0
    roi = gross / effective_cost if effective_cost else 0.0

    fails = []
    if margin < float(t["gross_margin_min"]):
        fails.append(f"粗利率 {margin:.1%} < {float(t['gross_margin_min']):.0%}")
    if roi < float(t["roi_min"]):
        fails.append(f"ROI {roi:.1%} < {float(t['roi_min']):.0%}")
    if gross < float(t["profit_per_unit_min_jpy"]):
        fails.append(f"粗利 {gross:,.0f}円 < {float(t['profit_per_unit_min_jpy']):,.0f}円")

    return {
        "price": price,
        "referral_rate": rate,
        "referral_fee": referral_fee,
        "fba_fee": fba_fee,
        "storage_fee": storage,
        "inbound_and_packaging": inbound,
        "return_reserve": return_reserve,
        "unit_cost": unit_cost,
        "point_credit": point_credit,
        "gross_profit": gross,
        "gross_margin": margin,
        "roi": roi,
        "ok": not fails,
        "fails": fails,
        "warnings": warnings,
        "floor_price": floor_price(cfg, effective_cost, rate, fba_fee, storage, inbound),
    }


def floor_price(cfg: dict, effective_cost: float, rate: float, fba_fee: float, storage: float, inbound: float) -> float:
    """粗利率が gross_margin_min ちょうどになる販売価格（下限価格）。"""
    m = float(cfg["targets"]["gross_margin_min"])
    r = float(cfg["shipping"]["return_rate_assumed"])
    denom = 1.0 - rate - r - m
    if denom <= 0:
        return float("inf")
    return (fba_fee + storage + inbound + effective_cost) / denom


def _fmt(result: dict) -> str:
    lines = [
        f"売上                    {result['price']:>10,.0f}",
        f"販売手数料 ({result['referral_rate']:.1%})   {-result['referral_fee']:>10,.0f}",
        f"FBA配送代行             {-result['fba_fee']:>10,.0f}",
        f"保管料                  {-result['storage_fee']:>10,.0f}",
        f"入庫送料・梱包          {-result['inbound_and_packaging']:>10,.0f}",
        f"返品引当                {-result['return_reserve']:>10,.0f}",
        f"仕入れ原価              {-result['unit_cost']:>10,.0f}",
    ]
    if result["point_credit"]:
        lines.append(f"ポイント控除            {result['point_credit']:>10,.0f}")
    lines += [
        "-" * 36,
        f"粗利                    {result['gross_profit']:>10,.0f}   粗利率 {result['gross_margin']:.1%}   ROI {result['roi']:.1%}",
        f"下限価格（粗利率下限）  {result['floor_price']:>10,.0f}",
        "判定: " + ("OK" if result["ok"] else "NG（" + " / ".join(result["fails"]) + "）"),
    ]
    for w in result["warnings"]:
        lines.append(f"⚠ {w}")
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(description="1SKUの利益・ROI計算")
    p.add_argument("--cost", type=float, required=True, help="仕入れ単価（税込）")
    p.add_argument("--price", type=float, required=True, help="想定販売価格")
    p.add_argument("--category", default=None, help="Amazonカテゴリ（business.yaml のキーと一致させる）")
    p.add_argument("--size", default=None, help="FBAサイズ区分（fba_fees の size_tier）")
    p.add_argument("--days", type=float, default=None, help="想定回転日数（既定: sell_through_days_max）")
    p.add_argument("--qty", type=int, default=1, help="仕入れ数量（送料の按分用）")
    p.add_argument("--shipping", type=float, default=0.0, help="仕入れ送料合計")
    p.add_argument("--points", type=float, default=0.0, help="1個あたりポイント還元")
    p.add_argument("--platform", default="amazon", choices=["amazon", "yahoo_auction", "mercari_shops"])
    p.add_argument("--fba-fee", type=float, default=None, help="FBA配送代行手数料を直接指定")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)

    cfg = load_config()
    r = calc(cfg, a.cost, a.price, a.category, a.size, a.days, a.qty, a.shipping, a.points, a.platform, a.fba_fee)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(_fmt(r))
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
