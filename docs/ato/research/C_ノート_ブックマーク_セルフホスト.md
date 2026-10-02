# C班 競合調査：Cubox / Karakeep / はてなブックマーク / Notion / Bear / Google Keep

確認日：2026-10-02（日本時間）
確認方法（全サービス共通）：実機未試用。公式ページ閲覧・検索結果要約のみ。

## 本調査の制約（必読）
- この環境のネットワーク方針により、以下の公式ホストは WebFetch が EGRESS_BLOCKED（取得失敗）となった。これらは「取得失敗（ネットワーク制限）」として各サービスの出典一覧に残した。
  cubox.cc / test.cubox.cc / help.cubox.cc / karakeep.app / docs.karakeep.app / b.hatena.ne.jp / hatena.zendesk.com / bookmark.hatenastaff.com / labo.hatenastaff.com / www.notion.com / bear.app / blog.bear.app / support.google.com / workspaceupdates.googleblog.com / apps.apple.com / play.google.com / chromewebstore.google.com / discussions.apple.com / ja.wikipedia.org / en.wikipedia.org / 9to5google.com / alternativeto.net / app-liv.jp ほか
- ページ本文を取得できたのは GitHub（github.com, raw.githubusercontent.com）のみ。
- セッションの WebSearch 上限（200回）に途中で到達したため、後半の項目は「未確認（検索上限のため未調査）」とした。
- App Store の価格・レビューはページ取得不可。検索結果要約で確認できたものだけ記録し、他は「未確認」。
- 表記ルール：
  - 「ページ取得で確認」＝WebFetchで本文を取得して確認
  - 「検索結果要約で確認（ページ本文は未取得）」＝WebSearchの結果要約のみで確認。要約元が公式ページの場合はURLを併記
  - 「推測：」＝出典なしの推測

---

## 1. Cubox

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Cubox（App Store 表記「Cubox: AI Read-It-Later App」「Cubox: AI Reader & Highlight」）
- 運営者：検索結果要約で確認（ページ本文は未取得）：Suzhou Guaiqi Information Technology Co., Ltd.（中国・蘇州、2020年創業）。Google Play の開発者表記は「Zenbox Inc.」（検索結果要約。出典 Tracxn / Google Play 検索要約）
- 国：中国
- 提供状況：継続（2025年11月付のレビュー、2026年の価格記事が存在）

### 2. 対象ユーザー・対応OS
- iPhone（iOS 14.0以降）、iPad、Mac、Apple Vision（App Store US 掲載の検索結果要約）
- Android（Google Play 掲載 `pro.cubox.androidapp` の検索結果で確認、本文未取得）
- Chrome 拡張（Chrome Web Store 掲載の検索結果で確認、本文未取得）
- Web：未確認（公式サイト取得失敗）
- 対象ユーザー：一般の「あとで読む」利用者・知識管理層（公式タグライン「Save Once. Know Forever.」検索結果要約）

### 3. 日本語UI
- 未確認。App Store US 掲載の対応言語は「English, Simplified Chinese」（検索結果要約）。日本語の記載は見当たらなかった。
- 推測：日本語UIは未提供。

### 4. 共有入口
- 公式説明に「WeChat、ウェブサイト、アプリなどから収集」とある（検索結果要約）。
- iOS共有シート：未確認（公式ページ取得失敗。推測：read-it-later アプリとして共有拡張を備えるが現行ページで未確認）
- メール転送：レビューに「email drop」の言及あり（検索結果要約、App Store US レビュー）
- ブラウザ拡張：Chrome 拡張あり（検索結果）

### 5. URL対応 / 画像対応
- URL：対応（read-it-later アプリの中核機能、検索結果要約）
- 画像単体保存：未確認。レビューに「multiple file type support」の言及（検索結果要約）。

### 6. OCR
- 未確認

### 7. 自動分類・AIタグ付け・要約
- AI Insight（記事要約）、Ask AI（記事内容への質問）あり（App Store 検索結果要約）
- 有料：「Pro+AI」プラン（USD 69/年）に AI 機能が含まれる（検索結果要約、saasworthy / spotsaas。cubox.cc/pricing 本文は取得失敗）
- 端末内か外部AIか：未確認

### 8. 検索
- 未確認

### 9. 再提示（リマインダー等）
- 未確認（検索結果要約にリマインダー・ランダム再提示の言及なし）

### 10. 週次まとめ・ダイジェスト
- 未確認

### 11. 完了・保留・不要の扱い
- 未確認

### 12. 無料枠
- 無料利用あり、Pro で「expanded storage and full AI capabilities」（検索結果要約）。件数上限：未確認（学習知識では無料は保存件数上限ありだが現行ページで確認できず）

### 13. 価格
- Pro：USD 39/年。Pro+AI：USD 69/年（検索結果要約、確認日 2026-10-02、出典 https://www.saasworthy.com/product/cubox-cc , https://www.spotsaas.com/product/cubox ）
- 公式ブログに「Pro+AI Now 30% Off at $48」の記事タイトルあり（https://cubox.cc/blog/first-ever-discount-pro-ai-now-30-off-at-48/ 、本文取得失敗。時期不明）
- 月額：未確認。日本 App Store JPY：未確認（取得失敗）

### 14. アカウント要否
- 未確認（推測：クラウド同期型のためサインアップ必須）

### 15. 外部AI利用の有無と送信先
- プライバシーポリシー（https://help.cubox.cc/legal/privacy 、最終更新 2024-11-28、本文取得失敗）の検索結果要約：第三者への個人情報提供・販売を行わない、URL を SHA-256 でハッシュ化して処理、閲覧履歴は保存しない。
- AI 処理の送信先（OpenAI 等）：未確認

### 16. データ削除・書き出し
- 未確認

### 17. レビューの不満（App Store US、検索結果要約。投稿日は一部のみ判明）
- 登録メールが中国語で届く／UIに英語と中国語が混在して使いにくい（日付不明）
- データが中国側サーバーに同期されるという懸念（過去レビュー、日付不明）
- 2025年11月：iOS でファイル添付が動作せず、サポート対応もなかった
- 同期不具合（サポート対応で解決した旨）
- 出典：https://apps.apple.com/us/app/cubox-ai-read-it-later-app/id1113361350?see-all=reviews&platform=iphone （取得失敗、検索結果要約のみ）

### 18. 出典URL一覧（確認日 2026-10-02）
- https://cubox.cc/ 取得失敗（ネットワーク制限）
- https://cubox.cc/pricing/ 取得失敗（ネットワーク制限）
- https://help.cubox.cc/legal/privacy 取得失敗（ネットワーク制限）
- https://apps.apple.com/us/app/cubox-ai-read-it-later-app/id1113361350 取得失敗（ネットワーク制限）・検索結果要約で確認
- https://play.google.com/store/apps/details?id=pro.cubox.androidapp 取得失敗（ネットワーク制限）
- https://www.saasworthy.com/product/cubox-cc 検索結果要約で確認
- https://www.spotsaas.com/product/cubox 検索結果要約で確認
- https://tracxn.com/d/companies/cubox/... 取得失敗（ネットワーク制限）・検索結果要約で確認

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は全て取得失敗、実機未試用）

---

## 2. Karakeep（旧 Hoarder）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Karakeep（旧称 Hoarder）
- 運営者：GitHub の karakeep-app オーガニゼーションによるオープンソース（AGPL-3.0）。GitHub Sponsors / Buy Me a Coffee で支援を受ける（ページ取得で確認：https://github.com/karakeep-app/karakeep ）。法人・所在国：未確認
- 提供状況：継続（取得時点で GitHub スター 29.4k、コミット 2,260）

### 2. 対象ユーザー・対応OS
- 対象：セルフホスト前提（README「self-hosting first」）。マネージドクラウド cloud.karakeep.app あり（ページ取得で確認）
- iOS アプリ、Android アプリ、Chrome 拡張、Firefox アドオン、コミュニティ製 Safari 拡張（macOS/iOS）（ページ取得で確認：docs quick-sharing.md）
- Web（セルフホストのWeb UI）

### 3. 日本語UI
- 未確認（検索上限のため未調査）

### 4. 共有入口
- iOS/Android ネイティブアプリでクイック保存（ページ取得で確認：quick-sharing.md）。共有シートで扱える種類の明記はドキュメントになし
- ブラウザ拡張（Chrome / Firefox / Safari）
- RSS フィード自動取り込み、REST API（ページ取得で確認：README）
- メール転送：未確認

### 5. URL対応 / 画像対応
- ブックマーク種別は Links / Text / Media（画像・PDF）。「Images or PDFs you want to save for later. Karakeep automatically extracts content」（ページ取得で確認：bookmarking.md）
- 画像単体保存：対応

### 6. OCR
- 対応（Tesseract）。環境変数 `OCR_LANGS`（既定 `eng`、カンマ区切りで言語追加）、`OCR_CONFIDENCE_THRESHOLD`（既定 50）（ページ取得で確認：environment-variables.md）。日本語OCRは `jpn` 追加で可能と思われるが未確認（推測）

### 7. 自動分類・AIタグ付け・要約
- 「LLM-based automatic tagging and summarization」（README、ページ取得）
- 環境変数（ページ取得で確認）：
  - `OPENAI_API_KEY` または `OLLAMA_BASE_URL` の設定で自動タグ付けが有効
  - `INFERENCE_ENABLE_AUTO_TAGGING` 既定 true、`INFERENCE_ENABLE_AUTO_SUMMARIZATION` 既定 false
  - `INFERENCE_TEXT_MODEL`（取得時のドキュメント既定表記「gpt-6-luna」。検索結果要約では「gpt-4.1-mini」とあり、版差の可能性。要再確認）、`INFERENCE_IMAGE_MODEL` 既定 gpt-4o-mini
  - `INFERENCE_LANG` 既定 english（タグ生成言語）、`INFERENCE_CONTEXT_LENGTH` 既定 2048
- 対応プロバイダ（ページ取得で確認：different-ai-providers.md）：OpenAI、Ollama（ローカル）、Gemini、OpenRouter、Perplexity、Azure、Cloudflare（OpenAI互換エンドポイント経由）
- 費用：ソフト自体は無料だが、外部APIを使う場合のAPI料金は利用者負担（推測）。Ollama なら端末/自サーバ内で完結

### 8. 検索
- 全文検索＋セマンティック検索（Meilisearch）、検索クエリ言語あり（ページ取得で確認：README、docs一覧）

### 9. 再提示
- 現行機能としては未確認（ドキュメントに記載なし）
- Feature request「"Remind me of this" feature」Issue #705（2024-11-29 起票、Open、ラベル Feature request / pri/medium / status/approved、担当 xuatz）：特定日またはランダム間隔で保存物の通知を受けたいという要望（ページ取得で確認：https://github.com/karakeep-app/karakeep/issues/705 ）
- 「random / resurface」で Issue 検索：該当なし（ページ取得で確認）

### 10. 週次まとめ・ダイジェスト
- 未確認（ドキュメントに記載なし）

### 11. 完了・保留・不要の扱い
- アーカイブ：「Archive hides a bookmark from the homepage without deleting it.」（ページ取得で確認：bookmarking.md）
- お気に入り（Star）あり。削除あり
- 既読ステータス：未確認

### 12. 無料枠
- セルフホスト：無料・無制限（AGPL-3.0）
- Karakeep Cloud（パブリックベータ）：無料枠 10 ブックマーク・20MB（検索結果要約、出典 marqly.com。公式 cloud.karakeep.app は未取得）

### 13. 価格
- Karakeep Cloud Pro：USD 4/月（年払いで約17%割引、年額の正確な数値は非公開との記載）。50,000ブックマーク、50GB、AIタグ付け、全文検索（検索結果要約、確認日 2026-10-02、出典 https://www.marqly.com/compare/linkwarden-vs-karakeep ほか。公式価格ページは未取得）
- 日本 App Store：アプリ自体は無料と思われるが未確認

### 14. アカウント要否
- 自サーバのアカウント作成が必要。`DISABLE_SIGNUPS`（既定 false）で新規登録を止められる（ページ取得で確認）

### 15. 外部AI利用の有無と送信先
- 管理者が設定したプロバイダへ送信（OpenAI 等のクラウド、または Ollama でローカル完結）。ドキュメントには送信先に関するプライバシー説明の明示はなし（ページ取得で確認：different-ai-providers.md）

### 16. データ削除・書き出し
- インポート：Netscape HTML（Chrome/Firefox）、Pocket CSV、Omnivore JSON、CLI（1行1URL）。「Titles, tags and addition date will be preserved」（ページ取得で確認：import.md）
- エクスポート：未確認（検索上限のため未調査）。セルフホストのためDBは自己管理

### 17. レビューの不満（公式コミュニティ）
- GitHub Discussion #1833（2025-08-11〜12）：外部 Ollama で要約・自動タグ付けが即失敗。原因はディスク/メモリ不足（40GB→86GB、4GB→16GB に増強で解消）。「セルフホストAIのエラーログを詳しくしてほしい」との要望（ページ取得で確認：https://github.com/karakeep-app/karakeep/discussions/1833 ）
- Issue #705（2024-11-29）：リマインダー機能がない（上記）
- その他：未確認（検索上限のため未調査）

### 18. 出典URL一覧（確認日 2026-10-02）
- https://github.com/karakeep-app/karakeep ページ取得で確認
- https://raw.githubusercontent.com/karakeep-app/karakeep/main/docs/docs/03-configuration/01-environment-variables.md ページ取得で確認
- https://raw.githubusercontent.com/karakeep-app/karakeep/main/docs/docs/03-configuration/02-different-ai-providers.md ページ取得で確認
- https://raw.githubusercontent.com/karakeep-app/karakeep/main/docs/docs/04-using-karakeep/bookmarking.md ページ取得で確認
- https://raw.githubusercontent.com/karakeep-app/karakeep/main/docs/docs/04-using-karakeep/quick-sharing.md ページ取得で確認
- https://raw.githubusercontent.com/karakeep-app/karakeep/main/docs/docs/04-using-karakeep/import.md ページ取得で確認
- https://github.com/karakeep-app/karakeep/issues/705 ページ取得で確認
- https://github.com/karakeep-app/karakeep/discussions/1833 ページ取得で確認
- https://karakeep.app/ 取得失敗（ネットワーク制限）
- https://docs.karakeep.app/configuration/different-ai-providers/ 取得失敗（ネットワーク制限）
- https://www.marqly.com/compare/linkwarden-vs-karakeep 検索結果要約で確認（Cloud価格）

### 19. 確認方法
- GitHub 上のドキュメント本文を取得して確認。公式サイト・クラウド価格ページは未取得。実機未試用。

---

## 3. はてなブックマーク

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：はてなブックマーク
- 運営者：株式会社はてな（日本）
- 提供状況：継続。有料オプション「はてなブックマークプラス」は 2017-04-05 に提供終了（検索結果要約、出典 https://bookmark.hatenastaff.com/entry/2017/02/17/150000 、https://internet.watch.impress.co.jp/docs/news/1044929.html 、本文未取得）

### 2. 対象ユーザー・対応OS
- Web、iOS アプリ、Android アプリ（公式ヘルプの検索結果要約）
- Chrome 拡張（Chrome Web Store 掲載、検索結果）
- Apple シリコン Mac で iOS アプリを「はてラボ」として提供（2022-03-23 開発者ブログのタイトルで確認、本文未取得）
- 対象：日本語圏の一般ユーザー（ソーシャルブックマーク）

### 3. 日本語UI
- 日本語（日本のサービス。公式ヘルプが日本語で提供されていることを検索結果で確認）

### 4. 共有入口
- iOS共有シート：「ブラウザアプリやその他のアプリで気になるページを発見した場合、アプリの共有ボタンから、簡単にはてなブックマークに登録できます。この機能を使用するためには、アプリ内でログインを済ませておく必要があります」（検索結果要約、出典 https://b.hatena.ne.jp/help/entry/app_extension 、本文取得失敗）
- 「あとで読む」も iPhone の共有ボタン下部から直接付与できるケースあり（検索結果要約、出典 https://b.hatena.ne.jp/help/entry/read_later_app ）
- ブラウザ拡張：公式ブログ「『ブラウザ拡張』が1位！『まだ誰もブックマークしていないページ』のブックマーク方法ランキング」（2022-04-14、タイトルのみ確認）
- URLからの手動ブックマーク（Zendesk ヘルプ記事タイトルで確認）
- メール転送・画像・ファイル：未確認

### 5. URL対応 / 画像対応
- URL：対応（サービスの中核）
- 画像単体保存：未確認（推測：URLベースのブックマークのため画像単体の保存は想定されていない）

### 6. OCR
- 未確認（推測：なし）

### 7. 自動分類・AIタグ付け・要約
- 未確認（検索上限のため未調査）

### 8. 検索
- 自分のブックマークの検索機能あり（Zendesk ヘルプ記事「より進んだ使い方（検索機能、あとで読む、URLからブックマーク、お気に入り）」タイトルで確認、本文取得失敗）。全文検索かどうか：未確認

### 9. 再提示
- 「あとで読む」リマインダー通知：iOS アプリ「左上のプロフィールアイコン > あとで読む > リマインダーを受け取る」で設定（検索結果要約、出典 https://b.hatena.ne.jp/help/entry/read_later_app ）。通知タイミング・頻度の詳細：未確認
- スヌーズ・ランダム再提示・期限設定：未確認

### 10. 週次まとめ・ダイジェスト
- 未確認

### 11. 完了・保留・不要の扱い
- 「あとで読む」は「あとで読む」「後で読む」タグ付けまたはアイコンで管理（検索結果要約）。読了後の扱い（タグ外し・既読）：未確認
- ブックマーク削除：あり（推測）

### 12. 無料枠
- 基本無料（有料プラン「はてなブックマークプラス」は 2017-04-05 終了）
- 注意：検索結果に出た「Pro 月額550円・広告非表示」は「はてなブログPro」の情報であり、はてなブックマークの有料プランではない（無関係のため採用しない）

### 13. 価格
- 無料（JPY 0）。現行の有料プラン：未確認（2017年以降の新設有料プランは検索結果で確認できず）。確認日 2026-10-02

### 14. アカウント要否
- はてなIDでのログインが必要（共有拡張の利用にもログイン必須、検索結果要約）

### 15. 外部AI利用の有無と送信先
- 未確認（検索上限のため未調査）

### 16. データ削除・書き出し
- エクスポート：設定画面「データ管理」から「ブックマーク形式、Atomフィード形式、RSS1.0形式」でダウンロード可能（検索結果要約、出典 https://b.hatena.ne.jp/help/entry/port 、本文取得失敗）。Atom 形式でのエクスポートを扱うサードパーティツールあり（ページ取得で確認：https://github.com/tkancf/hatebu-to-omnivore ）
- アカウント削除：未確認

### 17. レビューの不満（App Store 日本、検索結果要約。投稿日不明）
- 右下メニューボタンが使いづらく、カテゴリ階層が深い
- バックグラウンドで動き続けることによる著しいバッテリー消費
- UI変更でカテゴリ選択の手間が増え、ブックマークコメントを閉じるボタンが小さくなった
- iOS アップデートのたびに Share Extension が使えなくなる
- 出典：https://apps.apple.com/jp/app/%E3%81%AF%E3%81%A6%E3%81%AA%E3%83%96%E3%83%83%E3%82%AF%E3%83%9E%E3%83%BC%E3%82%AF/id354976659 （取得失敗、検索結果要約のみ）

### 18. 出典URL一覧（確認日 2026-10-02）
- https://b.hatena.ne.jp/ 取得失敗（ネットワーク制限）
- https://b.hatena.ne.jp/help/entry/app_extension 取得失敗・検索結果要約で確認
- https://b.hatena.ne.jp/help/entry/read_later_app 取得失敗・検索結果要約で確認
- https://b.hatena.ne.jp/help/entry/read_later 検索結果で存在確認
- https://b.hatena.ne.jp/help/entry/port 取得失敗・検索結果要約で確認
- https://b.hatena.ne.jp/help/entry/touch_app 検索結果で存在確認
- https://hatena.zendesk.com/hc/ja/articles/900003697986 取得失敗（ネットワーク制限）
- https://bookmark.hatenastaff.com/entry/2017/02/17/150000 取得失敗・検索結果要約で確認
- https://bookmark.hatenastaff.com/entry/2022/04/14/160915 取得失敗・タイトルのみ確認
- https://labo.hatenastaff.com/entry/2022/03/23/153000 取得失敗・タイトルのみ確認
- https://internet.watch.impress.co.jp/docs/news/1044929.html 検索結果要約で確認
- https://github.com/tkancf/hatebu-to-omnivore ページ取得で確認

### 19. 確認方法
- 公式ヘルプは検索結果要約のみ（本文未取得）。実機未試用。

---

## 4. Notion（Web Clipper / iOSアプリ共有シート保存）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Notion（Notion Web Clipper、Notion iOS アプリ）
- 運営者：Notion Labs, Inc.（米国）※学習知識。現行ページで法人名は未確認（notion.com 取得失敗）
- 提供状況：継続

### 2. 対象ユーザー・対応OS
- Web Clipper：Chrome、Safari、Firefox、モバイル（公式ページタイトル「Notion Web Clipper for Chrome, Safari, Firefox, and mobile」検索結果で確認）
- iOS（iOS 13.0 以降で共有シート利用可、検索結果要約）、Android、Web、Mac、Windows（学習知識、現行ページで未確認）
- 対象：個人〜企業の汎用ワークスペース利用者

### 3. 日本語UI
- 日本語の公式料金ページが存在する旨を検索結果要約で確認（本文未取得）。推測：日本語UIあり

### 4. 共有入口
- iOS共有シート：Safari/Chrome で共有アイコン → 「その他」→ Notion をオン → 以後、共有シートに Notion が表示。タイトル付与・ワークスペースとページの選択 → 保存（検索結果要約、出典 https://www.notion.com/help/web-clipper 、本文取得失敗）
- 画像・ローカルファイル：写真を選択 → 共有 → Notion（同上）
- ブラウザ拡張：Chrome/Safari/Firefox の Web Clipper
- テキスト：未確認。メール転送：未確認

### 5. URL対応 / 画像対応
- URL：対応（ページとして保存、またはデータベースへ追加）
- 画像単体保存：対応（写真の共有で Notion に保存、検索結果要約）

### 6. OCR
- 未確認（検索上限のため未調査）

### 7. 自動分類・AIタグ付け・要約
- Notion AI：2025-05-13 にスタンドアロンの AI アドオン販売を終了し、Business プラン（USD 20/メンバー/月、年払い）に同梱。Free/Plus は回数制限付きトライアルのみ。2025-12-01 に既存アドオン契約者を Business へ自動移行（検索結果要約、サードパーティ記事：usecarly.com、costbench.com、aumiqx.com。公式ページ本文は未取得）
- 日本語記事では「Free/Plus は AI 20回まで」との記載（検索結果要約、サードパーティ）
- 自動タグ付け：未確認（学習知識ではデータベースの AI 自動入力プロパティがあるが現行ページで未確認）
- 端末内か外部AIか：外部（クラウド）。送信先モデル提供者：未確認

### 8. 検索
- 未確認（検索上限のため未調査。学習知識ではワークスペース全文検索あり）

### 9. 再提示
- リマインダー：ページ内の @remind、またはデータベースの Date プロパティで設定。「30分前」等の事前通知、時刻・タイムゾーン指定可。モバイルアプリにはリマインド時刻から5分以内にプッシュ通知。アプリを開いていない場合はプッシュ通知とメールの両方が送られる（検索結果要約、出典 https://www.notion.com/help/reminders 、本文取得失敗）
- スヌーズ・ランダム再提示：未確認（推測：なし。保存物に自動で期限を付ける仕組みはなく、ユーザーが日付プロパティを設定する必要がある）

### 10. 週次まとめ・ダイジェスト
- 未確認

### 11. 完了・保留・不要の扱い
- 未確認。推測：データベースのステータス／チェックボックスプロパティをユーザーが自作して運用する（組み込みの「既読」概念はない）

### 12. 無料枠
- Free プラン USD 0（検索結果要約）。ブロック数・ゲスト数・アップロード容量の制限：未確認（notion.com/pricing 取得失敗）

### 13. 価格（確認日 2026-10-02）
- USD：Free 0 / Plus 10/月 / Business 20/月 / Enterprise 個別（検索結果要約、サードパーティ記事。年払い・月払いの区別は記事により不統一のため要再確認）
- JPY（検索結果要約、サードパーティ日本語記事）：Business 年払い 約3,150円/メンバー/月、月払い 約3,800円（2026-08-03 時点の記事）
- 日本 App Store 内課金（検索結果要約、2026-09-10 時点の記事）：Plus 1,800円/月・18,000円/年、「Notion Plus & AI」4,000円/月・40,000円/年
- 出典：https://www.jicoo.com/magazine/blog/notion-pricing 、https://temp.co.jp/blog/price 、https://tool-hikaku.com/notion-ryokin-guide/ ほか（いずれも本文未取得）

### 14. アカウント要否
- アカウント必須（推測。クラウド型サービス）

### 15. 外部AI利用の有無と送信先
- 未確認（検索上限のため未調査）

### 16. データ削除・書き出し
- 未確認（検索上限のため未調査。学習知識では Markdown/CSV/HTML/PDF エクスポートがあるが現行ページで確認できず）

### 17. レビューの不満
- 未確認（検索上限のため未調査）

### 18. 出典URL一覧（確認日 2026-10-02）
- https://www.notion.com/help/web-clipper 取得失敗・検索結果要約で確認
- https://www.notion.com/en-US/web-clipper 検索結果でタイトル確認
- https://www.notion.com/help/reminders 取得失敗・検索結果要約で確認
- https://www.notion.com/pricing 取得失敗（ネットワーク制限）
- https://www.usecarly.com/blog/notion-ai-pricing-change/ 取得失敗・検索結果要約で確認
- https://costbench.com/software/ai-productivity/notion-ai/ 検索結果要約で確認
- https://www.jicoo.com/magazine/blog/notion-pricing 検索結果要約で確認
- https://apps.apple.com/us/app/notion-web-clipper/id1559269364 検索結果で存在確認（取得失敗）

### 19. 確認方法
- 公式ヘルプは検索結果要約のみ。価格はサードパーティ記事の検索結果要約。実機未試用。

---

## 5. Bear

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Bear（App Store 表記「Bear - Markdown Notes」）
- 運営者：Shiny Frog（学習知識ではイタリア。現行ページで未確認）
- 提供状況：継続（2025-09 Web Clipper 2.0、2026-04 公式ブログ記事の存在を検索結果で確認）

### 2. 対象ユーザー・対応OS
- iPhone、iPad、Mac（Bear Pro の説明で「iPhone・iPad への iCloud 同期」、検索結果要約）
- Android / Windows / Web：未確認（学習知識では Apple プラットフォーム限定だが現行ページで未確認）
- ブラウザ拡張：Bear Web Clipper（公式 FAQ「Bear Web Clipper」「How to Clip Web Pages」が存在。Web Clipper 2.0 で Safari on iPhone/iPad に対応、検索結果要約、出典 https://blog.bear.app/2025/09/introducing-bear-web-clipper-2-0-faster-private-and-more-reliable/ ）
- 対象：Markdown ノート利用者（個人）

### 3. 日本語UI
- 未確認（学習知識では日本語ローカライズありだが現行ページで確認できず）

### 4. 共有入口
- iOS共有拡張：「Bear for iOS comes with an App Extension that makes it easy to collect text, links, photos, and files from other apps.」共有アイコン → Bear アイコン（検索結果要約、出典 https://bear.app/faq/ios-app-extension/ 、本文取得失敗）
- Webページ全体の取り込み：拡張で「Web Page Content」を選び保存。設定「Web Content Options」で画像の取り込み可否、ソースリンク追記、付与タグを設定（同上）
- Safari（iPhone/iPad）のアドレスバーから1タップ保存（Web Clipper 2.0、検索結果要約）
- メール転送：未確認

### 5. URL対応 / 画像対応
- URL：対応（リンク保存・ページ本文クリップ）
- 画像単体保存：対応（共有拡張で photos を収集、検索結果要約）

### 6. OCR
- Bear Pro：画像と PDF 内のテキストを検索可能（「OCR search allows you to search for text in images and PDFs (Bear Pro required)」検索結果要約、出典 bear.app / blog.bear.app 2026-04 記事「Bear Beyond Text」、本文未取得）

### 7. 自動分類・AIタグ付け・要約
- 未確認（検索結果要約に AI 機能の言及なし。推測：AI タグ付け・要約は非搭載）

### 8. 検索
- 全文検索＋画像/PDF 内テキスト検索（Pro）（検索結果要約）

### 9. 再提示
- 未確認（検索結果要約にリマインダーの言及なし。学習知識ではリマインダー機能なし）

### 10. 週次まとめ・ダイジェスト
- 未確認（推測：なし）

### 11. 完了・保留・不要の扱い
- 未確認（学習知識ではアーカイブ・ゴミ箱があるが現行ページで確認できず）

### 12. 無料枠
- 無料版：エディタ利用、エクスポート .txt / .md / .textbundle / .bearnote / .rtf（検索結果要約、出典 https://bear.app/faq/export-your-notes/ 、本文取得失敗）
- Pro：iCloud/CloudKit 同期、ノート暗号化とアプリロック、OCR 検索、追加テーマ・アイコン、HTML/DOCX/PDF/JPG/ePub エクスポート（検索結果要約）

### 13. 価格（確認日 2026-10-02）
- Bear Pro：USD 2.99/月、USD 29.99/年、7日間無料トライアル（検索結果要約、出典 https://bear.app/faq/features-and-price-of-bear-pro/ 、本文取得失敗）
- 日本 App Store JPY：未確認（取得失敗）

### 14. アカウント要否
- サインアップ不要、iCloud 同期（Pro）（検索結果要約で「iCloud/CloudKit 同期」を確認。アカウント不要は推測）

### 15. 外部AI利用の有無と送信先
- Web Clipper 2.0 は「on-device privacy」を謳う（検索結果要約、alternativeto ニュースタイトル）。外部 AI 利用：未確認（推測：なし）

### 16. データ削除・書き出し
- エクスポート形式は上記 12. のとおり（無料：txt/md/textbundle/bearnote/rtf、Pro：html/docx/pdf/jpg/epub）
- アカウント削除：アカウント概念なし（推測）

### 17. レビューの不満
- 未確認（検索上限のため未調査）

### 18. 出典URL一覧（確認日 2026-10-02）
- https://bear.app/ 取得失敗（ネットワーク制限）
- https://bear.app/faq/features-and-price-of-bear-pro/ 取得失敗・検索結果要約で確認
- https://bear.app/faq/ios-app-extension/ 取得失敗・検索結果要約で確認
- https://bear.app/faq/export-your-notes/ 取得失敗・検索結果要約で確認
- https://bear.app/faq/browser-extensions/ 、https://bear.app/faq/clip-web-pages/ 検索結果で存在確認
- https://blog.bear.app/2025/09/introducing-bear-web-clipper-2-0-faster-private-and-more-reliable/ 取得失敗・検索結果要約で確認
- https://blog.bear.app/2026/04/bear-beyond-text-working-with-images-pdfs-and-more/ 検索結果で存在確認
- https://apps.apple.com/jp/app/bear-markdown-notes/id1016366447 取得失敗（ネットワーク制限）

### 19. 確認方法
- 公式 FAQ・ブログは検索結果要約のみ。実機未試用。

---

## 6. Google Keep

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Google Keep
- 運営者：Google LLC（米国）
- 提供状況：継続。ただしリマインダー機能は Google Tasks へ移行（2024年4月発表、2025-10-13 から段階的提供開始、2026年1月中旬に広範展開。検索結果要約、出典 https://workspaceupdates.googleblog.com/2025/10/google-keep-reminders-now-saved-to-tasks.html 、https://9to5google.com/2026/01/15/google-keep-reminders-migration-tasks-wide/ 、いずれも本文取得失敗）

### 2. 対象ユーザー・対応OS
- iOS、Android、Web、Chrome 拡張（検索結果要約）
- Mac / Windows ネイティブ：未確認
- 対象：一般の Google アカウント利用者（無料）

### 3. 日本語UI
- 未確認（推測：Google 製品として日本語UIあり）

### 4. 共有入口
- iOS共有シート：「tap your sharing icon and from the Share via list select Google Keep」（検索結果要約）。一方、Apple Community に「ios share to Google Keep no longer an option」というスレッドあり（https://discussions.apple.com/thread/255290496 、取得失敗、日付不明）。現行 iOS で共有拡張が確実に動作するかは未確認
- Chrome 拡張：ページ・リンク・画像を Keep に保存（検索結果要約）
- 画像：カメラアプリ等から共有メニューで Keep に送信可能（まとめて送信可、検索結果要約・サードパーティ）
- メール転送：未確認

### 5. URL対応 / 画像対応
- URL：対応（リンクをメモとして保存。リンクプレビュー等の詳細は未確認）
- 画像単体保存：対応（画像メモ）

### 6. OCR
- 「Grab image text（画像のテキストを抽出）」：Web、Android、iOS で利用可。画像内の「⋮」メニューから実行、テキストがメモに挿入される。インターネット接続が必要（検索結果要約、サードパーティ記事 cisdem.com / techrepublic.com。公式ヘルプ本文は未取得）

### 7. 自動分類・AIタグ付け・要約
- 未確認（検索上限のため未調査）

### 8. 検索
- 未確認（検索上限のため未調査。学習知識では画像内テキストも検索対象だが現行ページで確認できず）

### 9. 再提示
- 時刻リマインダー：Keep から設定可（従来機能）。Tasks 移行後は新規リマインダーがタスクとして保存され、カレンダー・Tasks アプリで表示（検索結果要約）
- 場所リマインダー：移行後「You can no longer create or get location-based reminders」（検索結果要約、出典 https://support.google.com/tasks/answer/16540694 、本文取得失敗）
- 通知：移行後は Keep 自体はリマインダー通知を送らず、Google Calendar / Tasks アプリが担当（同上）
- スヌーズ・ランダム再提示：未確認

### 10. 週次まとめ・ダイジェスト
- 未確認（推測：なし）

### 11. 完了・保留・不要の扱い
- アーカイブ：メモを開き右上の「アーカイブ」でアーカイブ欄へ移動（削除ではなく後から復元可）。削除はゴミ箱へ移動し 7 日間保持（検索結果要約、出典 https://support.google.com/keep/answer/6262765 、本文取得失敗）

### 12. 無料枠
- 無料（検索結果要約）。保存容量が Google アカウントの容量に含まれるか：未確認

### 13. 価格（確認日 2026-10-02）
- 無料（JPY 0 / USD 0）。有料プラン：なし（検索結果要約。Google One 等の容量課金との関係は未確認）

### 14. アカウント要否
- Google アカウント必須（推測。クラウド同期型）

### 15. 外部AI利用の有無と送信先
- OCR はクラウド処理（インターネット接続必須、サードパーティ記事）。Google 側の AI/データ利用記載：未確認（検索上限のため未調査）

### 16. データ削除・書き出し
- Google Takeout で Keep を選択してエクスポート。完了後にメールでリンクが届き、1週間で失効（検索結果要約、出典 howtogeek.com、本文取得失敗）。形式：未確認（学習知識では JSON + HTML）
- 移行前リマインダーのデータは Takeout で書き出し可（Workspace 向け記載、検索結果要約）
- アカウント削除：Google アカウント削除に準ずる（推測）

### 17. レビューの不満
- Apple Community：iOS の共有シートに Google Keep が表示されなくなった（https://discussions.apple.com/thread/255290496 、日付不明、取得失敗）
- リマインダー移行により Keep からの通知が来なくなる・場所リマインダーが使えなくなる（検索結果要約、公式ヘルプ記載に基づく仕様変更。ユーザー不満としての出典は未確認）
- その他：未確認（検索上限のため未調査）

### 18. 出典URL一覧（確認日 2026-10-02）
- https://keep.google.com/ 未取得
- https://support.google.com/keep/answer/6300456 取得失敗（ネットワーク制限）
- https://support.google.com/keep/answer/6262765 取得失敗・検索結果要約で確認
- https://support.google.com/tasks/answer/16540694 取得失敗・検索結果要約で確認
- https://workspaceupdates.googleblog.com/2025/10/google-keep-reminders-now-saved-to-tasks.html 取得失敗・検索結果要約で確認
- https://9to5google.com/2026/01/15/google-keep-reminders-migration-tasks-wide/ 取得失敗・検索結果要約で確認
- https://www.cisdem.com/resource/google-keep-ocr.html 検索結果要約で確認
- https://www.howtogeek.com/694042/how-to-export-your-google-keep-notes-and-attachments/ 取得失敗・検索結果要約で確認
- https://discussions.apple.com/thread/255290496 取得失敗（ネットワーク制限）
- https://chromewebstore.google.com/detail/google-keep-chrome-extens/lpcaedmchfhocbbapmcbpinfpgnhiddi 検索結果で存在確認

### 19. 確認方法
- 公式ヘルプは検索結果要約のみ。実機未試用。

---

## 横断メモ（ATO 企画向けの示唆。推測を含む）
- iOS共有シート保存：Notion、Bear、はてなブックマーク、Karakeep は公式に共有拡張の記載あり（検索結果要約／ドキュメント）。Google Keep は共有拡張の記載はあるが「共有シートから消えた」という利用者報告がある。Cubox は未確認。
- 画像・スクショ単体保存：Karakeep（Media）、Bear（photos）、Notion（写真共有）、Google Keep（画像メモ）は対応。はてなブックマークは URL 前提（推測で非対応）。Cubox は未確認。
- 再提示：いずれも「保存物を自動で再提示する」機能は確認できず。Notion と Google Keep（Tasks 経由）は手動リマインダー、はてなブックマークは「あとで読む」リマインダー通知設定あり（詳細未確認）、Karakeep はリマインダー要望 Issue #705 が Open（2024-11-29 起票、承認済み・未実装）。
- 完了・アーカイブ：Karakeep と Google Keep は「アーカイブ＝ホームから隠すが削除しない」概念を明示。Notion は自作プロパティ依存（推測）。
- 価格：Cubox Pro USD 39/年・Pro+AI USD 69/年、Karakeep Cloud Pro USD 4/月、Bear Pro USD 2.99/月・29.99/年、Notion Business USD 20/月（AI同梱）、はてなブックマーク・Google Keep は無料。JPY は Notion の日本 App Store 価格（Plus 1,800円/月、18,000円/年、Plus & AI 4,000円/月、40,000円/年、サードパーティ記事）のみ確認。
- 外部AI：Karakeep は管理者設定次第（Ollama でローカル可）。Cubox・Notion はクラウドAI（送信先の明記は未確認）。Bear は AI 非搭載と推測。Google Keep の OCR はクラウド処理。
