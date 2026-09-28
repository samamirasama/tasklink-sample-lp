# 週次ルーチン

1. **リサーチ枠**（researcher）: 2〜3セッション。カテゴリをローテーションし、`candidates.csv` に追記。
2. **滞留在庫レビュー**（trader）: `days_in_stock` が `sell_through_days_max` の70%を超えたSKUを列挙し、値下げ／返送／他販路の3案。
3. **KPI速報**（trader）: `python3 sedori-ops/scripts/kpi_report.py --period week`。
4. **規約・手数料の変更確認**（director）: セラーセントラルのお知らせ、メルカリShops・ヤフオク!のお知らせを事業主が確認し、変更があれば `00_facts_and_sources.md` と `business.yaml` を更新。
5. **資金配分**（director）: 現金残高、入金予定、発注予定を並べ、`reserve_ratio` を守れているか確認。
6. **文面の改善**（copywriter / communicator）: 今週の問い合わせで多かった質問を出品文面に反映。
