---
name: sedori-listing
description: 承認済みの仕入れ候補または在庫SKUについて、販売先別の出品文面を作成し、禁止表現チェックと下限価格の登録まで行う。「/sedori-listing C-20260928-001」「/sedori-listing SKU名」のように使う。
---

# /sedori-listing

引数: `$ARGUMENTS`（candidate_id または sku。複数可）

## 手順

1. `sedori-ops/data/candidates.csv` / `inventory.csv` から対象行を特定する。`decision` が `approved_for_purchase` でない候補は、その旨を伝えて director の判定を先に促す。
2. `sedori-copywriter` エージェントに対象を渡し、`business.yaml` で有効な販売先ごとに文面を作成させる（テンプレ: `sedori-ops/templates/listing_*.md`、規約: `docs/03_writing_guidelines.md`）。禁止表現チェック結果と事実の根拠URLを必ず添えさせる。
3. `sedori-trader` エージェントに `python3 sedori-ops/scripts/profit_calc.py` で下限価格（floor_price）を計算させ、`inventory.csv` に行を作成または更新させる（`status=inbound`）。
4. `sedori-director` が文面のC項チェック（`docs/01_compliance.md` C1〜C6）を確認する。
5. 事業主に、販売先別の文面・下限価格・出品時の設定メモ・未確定項目を渡す。出品の確定操作は事業主が行う。
