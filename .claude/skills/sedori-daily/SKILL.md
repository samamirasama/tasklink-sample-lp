---
name: sedori-daily
description: 電脳せどりの日次ルーチンを実行する。未返信の問い合わせ、承認待ち候補、価格チェック、入荷・納品状況、売上転記を各役割に振り分け、最後に「今日やること／準備済み／要判断」の日次ブリーフを出す。引数に week / month を渡すと週次・月次ルーチンを実行する。
---

# /sedori-daily

引数: `$ARGUMENTS`（空なら日次。`week` で週次、`month` で月次）

## 手順

1. 実行するルーチンを決める: 空 → `sedori-ops/routines/daily.md`、`week` → `weekly.md`、`month` → `monthly.md`。
2. `sedori-director` エージェントに該当ルーチンを渡し、各項目を担当役割（communicator / trader / researcher / copywriter）に Agent で委任させる。
   - 未返信: `contacts.csv` の `reply_sent_at` 空欄かつ SLA（`communication.response_sla_hours`）に迫るもの
   - 承認待ち: `candidates.csv` の `decision=pending`
   - 価格: `inventory.csv` の `in_stock` SKU（現在価格は事業主が入力）
   - 入荷・納品: `purchases.csv` の `ordered`、`inventory.csv` の `qty_inbound`
   - 売上転記: 事業主から受け取ったレポートを `sales.csv` に
   - 週次・月次では `python3 sedori-ops/scripts/kpi_report.py --period week|month` も実行
3. 日次ブリーフを3ブロックで出す。
   - **今日やること（事業主）**: 発注・送信・価格反映・納品など、人が実行する行為
   - **準備済み**: エージェントが作成した文面・記録・試算
   - **要判断**: エスカレーション事項、資金・規約に関わる判断、基準変更の提案
4. `docs/00_facts_and_sources.md` に「未確認」の項目が残っている場合、週次ではその再確認を事業主に促す。
