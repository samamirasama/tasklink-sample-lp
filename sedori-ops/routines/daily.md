# 日次ルーチン（`/sedori-daily` で実行）

所要目安 15〜30分。director が進行し、各役割に振る。

1. **未返信チェック**（communicator）
   - `contacts.csv` で `reply_sent_at` が空、かつ受信から `response_sla_hours` に迫るものを列挙。
   - 返信文面を作成し、事業主が送信。
2. **承認待ち候補**（director）
   - `candidates.csv` の `decision=pending` を列挙し、コンプライアンス・資金ゲートを判定。
3. **価格チェック**（trader）
   - `inventory.csv` の `status=in_stock` について、現在のカート価格を事業主が確認して入力。`floor_price` 割れの競合があれば「追随しない／損切り／保持」の期待値を提示。
4. **入荷・納品状況**（trader）
   - `purchases.csv` の `status=ordered` で予定日超過のものを列挙。
   - `inventory.csv` の `qty_inbound` が残っているものを列挙。
5. **売上転記**（trader）
   - 前日の売上を `sales.csv` に転記（事業主がレポートを渡す）。
6. **日次ブリーフ**（director）
   - 「今日やること（人）」「エージェントが準備済みのもの」「要判断事項」の3ブロックで出力。
