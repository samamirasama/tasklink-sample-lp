# 月次ルーチン

1. **月次締め**（trader）: `python3 sedori-ops/scripts/kpi_report.py --period month`。売上・粗利・粗利率・ROI・回転・返品率を `05_kpi.md` の目標と比較。
2. **基準の見直し**（director）: 粗利率・回転が2か月連続未達なら `business.yaml: targets / research` を見直す。
3. **カテゴリ配分**（researcher）: カテゴリ別の粗利と歩留まり（approved/調査数）から、来月の注力カテゴリを1〜2つ提案。
4. **請求書の棚卸し**（trader）: `purchases.csv` の `invoice_path` が全行埋まっているか。欠けていれば仕入れ先に再発行依頼（communicator）。
5. **税務**（事業主）: 会計ソフトへ売上・仕入れ・経費を反映。
6. **リスク点検**（director）: アカウント健全性、真贋調査・規制通知の有無、在庫金額の集中（1SKUが在庫総額の30%超なら分散を提案）。
