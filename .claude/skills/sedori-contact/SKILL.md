---
name: sedori-contact
description: 購入者・仕入れ先・プラットフォームからの受信内容に対する返信文面を作成し、エスカレーション判定と contacts.csv への記録を行う。「/sedori-contact 購入者から『まだ届かない』と連絡」「/sedori-contact Amazonから真贋調査の通知」のように使う。
---

# /sedori-contact

引数: `$ARGUMENTS`（受信内容の要約または本文。注文番号・SKUがあれば含める）

## 手順

1. `sedori-communicator` エージェントに受信内容を渡し、分類 → 事実の照合（`sales.csv` / `inventory.csv` / `purchases.csv`）→ 文面作成 → エスカレーション判定 → `contacts.csv` 追記を行わせる。
2. エスカレーション該当（返金・交換の確定、真贋・知財の指摘、2往復目以降のクレーム、仕入れ先との交渉）の場合は、`sedori-director` に経緯と選択肢を整理させ、事業主の判断事項として提示する。プラットフォームからの規制通知なら `templates/messages/platform_poa.md` の骨子で改善計画書の下書きも作る。
3. 事業主に「送信用文面」「根拠にした事実」「未確認事項」「エスカレーション要否」を渡す。送信は事業主が行い、送信後に `reply_sent_at` を記録する。
4. 同種の問い合わせが繰り返されている場合は、出品文面への反映を `/sedori-listing` で提案する。
