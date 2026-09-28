# データスキーマ（`data/*.csv`）

文字コード UTF-8、区切りカンマ、1行目ヘッダー。日付は `YYYY-MM-DD`、日時は `YYYY-MM-DDTHH:MM+09:00`。金額は税込円・整数。

## ID体系

- candidate_id: `C-YYYYMMDD-NNN`
- purchase_id: `P-YYYYMMDD-NNN`
- sku: 事業主が決める（例 `BRAND-MODEL-COLOR`）
- sale_id: プラットフォームの注文番号
- contact_id: `M-YYYYMMDD-NNN`

## candidates.csv（リサーチ候補）

| 列 | 内容 |
|---|---|
| candidate_id | ID |
| researched_at | 調査日時 |
| platform | 販売先（amazon / yahoo_auction / mercari_shops） |
| asin_or_url | ASIN または商品URL |
| title | 商品名 |
| category | Amazonカテゴリ |
| condition | new / used |
| source_name | 仕入れ先 |
| source_url | 仕入れ先URL |
| source_price | 仕入れ単価（税込） |
| source_shipping | 仕入れ送料（合計） |
| source_qty_limit | 購入数量制限（不明なら空） |
| points_jpy | ポイント還元（1個あたり） |
| sell_price | 想定販売価格 |
| price_90d_median | 直近90日中央値（未取得なら空） |
| rank | 売れ筋ランキング |
| rank_category | ランキングのカテゴリ |
| fba_sellers | FBA出品者数 |
| est_monthly_sales | 月間推定販売数（未取得なら空） |
| size_tier | FBAサイズ区分 |
| gross_profit | 1個あたり粗利（計算値） |
| gross_margin | 粗利率 |
| roi | ROI |
| score | スコア（0-100） |
| compliance_flags | B1〜B8 のNG項目（セミコロン区切り、なければ空） |
| decision | pending / approved_for_purchase / hold / rejected |
| status | researched / purchased / listed / sold_out / dropped |
| notes | 備考（データ取得元・精度） |

## purchases.csv（仕入れ）

purchase_id, candidate_id, ordered_at, source_name, order_number, sku, qty, unit_price, shipping, points_jpy, total_cost, invoice_path, delivered_at, status(ordered/delivered/cancelled/partial), notes

## inventory.csv（在庫）

sku, asin, fnsku, title, platform, condition, qty_inbound, qty_available, unit_cost, listed_price, floor_price, listed_at, days_in_stock, status(inbound/in_stock/stranded/removed), notes

## sales.csv（販売）

sale_id, sold_at, platform, sku, qty, sale_price, referral_fee, fba_fee, other_fee, shipping_cost, unit_cost, gross_profit, returned(0/1), return_reason, refund_amount, notes

## contacts.csv（連絡記録）

contact_id, received_at, platform, counterparty(buyer/seller/supplier/platform), order_or_sku, category(shipping/condition/return/cancel/inquiry/claim/negotiation/other), summary, reply_sent_at, escalated(0/1), resolved(0/1), notes
