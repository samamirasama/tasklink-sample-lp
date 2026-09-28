---
name: sedori-research
description: 電脳せどりの商品リサーチを実行する。引数にカテゴリ・仕入れ先・セール名・ASINのいずれかを渡す。sedori-researcher が候補を抽出して candidates.csv に追記し、director がコンプライアンスと資金のゲート判定を行う。「/sedori-research 家電アクセサリ」「/sedori-research ヨドバシのセール」のように使う。
---

# /sedori-research

引数: `$ARGUMENTS`（カテゴリ / 仕入れ先 / セール名 / ASIN / 商品URL）

## 手順

1. `sedori-ops/config/business.yaml` を読み、`last_updated`、`tools.keepa.enabled`、`research.categories_excluded` を確認する。引数が除外カテゴリに該当する場合はその旨を伝えて終了する。
2. `sedori-researcher` エージェントに以下を渡して実行する。
   - 対象: `$ARGUMENTS`
   - モード: Keepa有効なら「Keepaモード」、無効なら「目視確認モード」（事業主に必要な数値の入力を依頼する）
   - 出力: `sedori-ops/data/candidates.csv` への追記、`python3 sedori-ops/scripts/candidate_screen.py --write` の実行、`sedori-ops/templates/research_report.md` 形式のレポート
3. researcher の結果を `sedori-director` に渡し、各候補について `sedori-ops/docs/01_compliance.md` B1〜B8 と資金ゲートを判定させる。判定結果（approved_for_purchase / hold / rejected と基準番号）を `candidates.csv` の `decision` に反映する。
4. 事業主に報告する。形式は「結論 → 前提・基準日 → 主要な数字 → 要点 → リスク → 代替案 → 事業主に実行してほしいこと」。

## 禁止

- 数値の捏造。取得できないものは「未取得」と書く。
- ログインを伴う自動取得や規約で禁じられたスクレイピングの実行・提案。
- 承認済み候補について「発注した」と記録すること（発注は事業主の行為）。
