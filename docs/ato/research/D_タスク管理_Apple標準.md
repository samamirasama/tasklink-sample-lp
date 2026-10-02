# D班：タスク管理系競合＋無料標準手段の調査（Things 3 / Todoist / TickTick / Microsoft To Do / Apple リマインダー / Apple メモ＋Safari）

確認日：2026-10-02（日本時間）
調査担当：D班（ATO 競合調査）

## 本調査の前提・制約（必読）
- **取得失敗（ネットワーク制限）**：本環境の egress プロキシにより、以下の公式URLへの WebFetch / curl は全て `EGRESS_BLOCKED`（CONNECT 403）で拒否され、ページ本文を取得できなかった（再試行せず）。
  - https://culturedcode.com/things/ 、https://culturedcode.com/things/support/articles/2803573/
  - https://todoist.com/pricing
  - https://ticktick.com/about/premium
  - https://support.apple.com/guide/iphone/add-items-to-the-reading-list-iph1bb2b4c7/ios 、https://support.apple.com/guide/iphone/set-reminders-iph3b1fd5b1/ios
  - https://apps.apple.com/jp/app/things-3/id904237743 、https://apps.apple.com/us/app/things-3/id904237743 、https://apps.apple.com/jp/app/todoist-to-do-list-planner/id572688855 、https://apps.apple.com/jp/app/ticktick-todo-task-list-plan/id626144601
  - https://support.microsoft.com/en-us/todo/my-day-and-suggestions 、https://techcommunity.microsoft.com/blog/to-doblog/discover-all-our-latest-features-on-ios-%E2%80%93-siri-shortcuts-share-extension-and-mor/1082376
  - 対象ドメイン（culturedcode.com、todoist.com、ticktick.com / help.ticktick.com、support.microsoft.com、techcommunity.microsoft.com、support.apple.com、apps.apple.com）は全て拒否対象のため、本調査で「ページ取得で確認」できた公式ページは **ゼロ**。
- したがって本レポートの「事実」は全て **「検索結果要約で確認（ページ本文は未取得）」** である。WebSearch の結果に含まれる公式ページ（および一部第三者ページ）の要約スニペットに基づく。各項目の出典URLは「要約が参照していたページ」であり、本文を直接閲覧したものではない。
- 調査途中でセッション全体の WebSearch 回数上限（200回）に達したため、以降の追加検索は不可。未確認項目のうち追加調査できなかったものは「未確認（検索上限のため未調査）」に相当する（各項目の「未確認」はこれを含む）。
- 実機（iPhone）での試用は一切行っていない。
- 価格は「公式ページ（公式ヘルプ／公式 pricing／App Store 掲載ページ）の検索結果要約」で確認できたもののみ記録し、第三者サイトのみの数値は「未確認」とし参考値として分けて記す。
- 「非対応」は公式に明記が確認できた場合のみ。それ以外は「未確認」。推測には「推測：」を付す。

---

## 1. Things 3（Cultured Code）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Things 3
- 運営者：Cultured Code GmbH & Co. KG（US App Store 掲載の開発者名、検索結果要約）
- 国：推測：ドイツ（GmbH & Co. KG はドイツの法人形態。所在地は現行ページで未確認）
- 提供状況：継続（2024年に Apple Vision Pro 版を追加、公式ブログ・サポート記事が現行で検索に出る）

### 2. 対象ユーザー・対応OS
- 対象：個人向けのタスク管理（GTD 志向）
- 対応：Mac、iPad、iPhone（Apple Watch 版同梱）、Apple Vision Pro（公式「Getting Things」ページ：各プラットフォームを別売）
- Android / Windows / Web：公式ページ本文で「非対応」の明記は直接確認できず（第三者記事は「Android・Windows・Web 版なし、Cultured Code は Apple プラットフォームのみ開発と表明」と記載）→ 事実上非対応だが、公式明記は未確認
- ブラウザ拡張：未確認（記載なし）

### 3. 日本語UI
- 日本語あり（US App Store 掲載の対応言語に Japanese が含まれる、検索結果要約）。リリースノートで「3.23.1 で日本語ローカライズの軽微な問題を修正」の記載あり（検索結果要約）

### 4. 共有入口
- iOS 共有シート：対応。公式サポート記事「Adding To-Dos From Other Apps」に「Share Sheet で他アプリのリンクやテキストから to-do を作成」「共有シートの Edit → Things を追加」と記載
- URL：対応（上記）
- テキスト：対応（共有シート、コピー＆ペースト、ドラッグ＆ドロップ）
- 画像・スクショ：未確認（公式記事スニペットは「links and text」のみ言及。学習知識では Things はファイル・画像添付非対応だが、現行ページで確認できず）
- メール転送：対応「Mail to Things」（Things Cloud の専用アドレスにメールを送ると to-do 化、2017年12月公式ブログ）
- その他：URL スキーム（things:///add、JSON 形式の一括追加）、Apple ショートカット アクション
- 保存時の必須入力：未確認（推測：タイトルは共有元のタイトルで自動補完され、リスト／日付は任意）

### 5. URL対応 / 画像対応
- URL：対応（to-do のメモ欄にリンクとして保存される旨、公式記事）
- 画像単体保存：未確認（上記の通り）

### 6. OCR
- 未確認（公式ページに記載を確認できず）

### 7. 自動分類・AIタグ付け・要約
- 未確認（公式ページに AI 機能の記載を確認できず。レビュー側で「AI 統合がない」との不満あり → 推測：提供なし）

### 8. 検索
- 未確認（学習知識ではアプリ内クイック検索でタイトル・メモを検索できるが、現行ページで確認できず）

### 9. 再提示
- 期限設定：対応（When による日付指定、Deadline）
- リマインダー：対応（時刻通知。公式「Scheduling To-Dos」記事が検索に出る）
- Today / This Evening / Upcoming / Anytime / Someday の分類（公式記事「An In-Depth Look at Today, Upcoming, Anytime, and Someday」）
- Someday：「まだ明確でないが将来実行可能になりうるもの」の置き場（公式）
- スヌーズ：未確認
- ランダム再提示（resurfacing）：未確認（記載なし）

### 10. 週次まとめ・ダイジェスト
- 「Weekly Review」は公式 Shortcuts Gallery のショートカット（Things とカレンダーを画面分割で表示）として提供（検索結果要約）。アプリ内蔵のレビュー機能ではない
- メール／通知ダイジェスト：未確認

### 11. 完了・保留・不要の扱い
- 完了／キャンセルした to-do・プロジェクトは「Logbook」に移動（アーカイブ相当、公式）
- 保留：Someday
- 削除：未確認（学習知識ではゴミ箱あり）

### 12. 無料枠
- 買い切りのため無料プランなし。Mac は体験版あり（公式「Trying the App」記事）。iPhone 版の無料体験：未確認

### 13. 価格
- 買い切り（サブスクなし、公式「App Store Pricing」）。プラットフォームごとに別購入。Things Cloud 同期は無料
- USD（公式 pricing ページの検索結果要約で確認）：Mac USD 49.99、Apple Vision Pro USD 29.99。iPhone / iPad の USD は公式 pricing ページ要約には含まれず
- USD（US App Store 掲載ページの検索結果要約で確認）：iPhone USD 9.99（Apple Watch 版含む）
- iPad USD：未確認（第三者サイトの参考値 USD 19.99 のみ、公式要約では確認できず）
- JPY（日本 App Store 掲載ページの検索結果要約で確認）：iPhone 版 ¥1,500。iPad / Mac の JPY：未確認
- 確認日 2026-10-02 / 確認元 https://culturedcode.com/things/pricing/ 、https://apps.apple.com/jp/app/things-3/id904237743 、https://apps.apple.com/us/app/things-3/id904237743（いずれも検索結果要約、ページ本文は未取得）

### 14. アカウント要否
- Things Cloud アカウント（メールアドレス）は同期用。推測：同期しない単機利用はアカウント不要。iCloud 同期ではなく独自 Things Cloud

### 15. 外部AI利用
- 記載なし → 未確認（AI 機能自体の記載が確認できない）
- プライバシー：Things Cloud は通信 TLS、保存時 AES-256 暗号化（公式プライバシーポリシー スニペット）

### 16. データ削除・書き出し
- エクスポート：GDPR に基づき SQLite データベースファイルとして取得可、PDF 印刷、Mac では AppleScript（公式「Exporting Your Data」）
- アカウント削除：アプリ設定から Things Cloud アカウント削除可。削除は取り消し不可で、各端末内のデータは残る（公式「Deleting Your Account & Data」）

### 17. レビューの不満（2〜4件）
- Android / Windows / Web 版がなく、Apple 以外の端末と併用できない（第三者レビュー集：https://organized3.com/things-3-alternative 、https://donebear.com/blog/things-3-for-windows 、日付不明）
- 自然言語入力（タスク全体）がない、AI 統合がない（第三者レビュー要約：https://www.producthunt.com/products/things-3/reviews 、https://mwm.ai/apps/things-3/904237743 、日付不明）
- プラットフォームごとの別購入で合計額がかさむ（https://organized3.com/blog/things-3-price-breakdown 、日付不明）
- ※App Store レビュー本文は取得できず（apps.apple.com 遮断）

### 18. 出典URL一覧（確認日 2026-10-02、いずれも検索結果要約で確認・ページ本文は未取得）
- https://culturedcode.com/things/
- https://culturedcode.com/things/pricing/
- https://culturedcode.com/things/support/articles/2803552/ （Getting Things）
- https://culturedcode.com/things/support/articles/2803569/ （Adding To-Dos From Other Apps）
- https://culturedcode.com/things/support/articles/4001304/ （Today, Upcoming, Anytime, Someday）
- https://culturedcode.com/things/blog/2017/12/mail-to-things/
- https://culturedcode.com/things/help/url-scheme/
- https://culturedcode.com/things/support/articles/2982272/ （Exporting Your Data）
- https://culturedcode.com/things/support/articles/2803591/ （Deleting Your Account & Data）
- https://culturedcode.com/privacy/
- https://apps.apple.com/jp/app/things-3/id904237743
- https://apps.apple.com/us/app/things-3/id904237743

### 19. 確認方法
- 検索結果要約で確認（ページ本文は未取得）。公式ページへの WebFetch は取得失敗（ネットワーク制限）。実機未試用。追加検索は WebSearch 回数上限により不可

---

## 2. Todoist（Doist）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Todoist
- 運営者：Doist Inc.（デラウェア州登記、登記住所 251 Little Falls Drive, Wilmington, DE 19808、公式利用規約／プライバシーのスニペット）
- 国：米国（登記上）
- 提供状況：継続（2026 Changelog が公式ヘルプに存在、2025年12月に料金改定）

### 2. 対象ユーザー・対応OS
- 対象：個人〜チーム（Beginner / Pro / Business）
- 対応OS：iOS、Android、Web、Mac、Windows（公式ヘルプが各プラットフォーム向けに存在）。ブラウザ拡張：未確認（学習知識では Chrome/Firefox/Safari/Edge 拡張ありだが現行ページで確認できず。「Task Assist extension」という名称の機能は公式ヘルプに存在）

### 3. 日本語UI
- 対応（公式ヘルプに日本語版 https://www.todoist.com/ja/help/... が存在）

### 4. 共有入口
- iOS 共有シート：対応。公式ヘルプ「Add files and links to Todoist from your mobile devices」：写真やファイルを開き共有シートで Todoist を選択 → タスク名を入力し、必要なら期限・プロジェクトを指定して保存
- URL：対応（リンク共有、同ヘルプ）
- 画像・スクショ：対応（写真の共有、同ヘルプ）。Quick Add は1タスクにつき添付1件。追加分はコメントで
- ファイル：対応（33種類のファイル形式、無料 5MB / Pro・Business 100MB まで）
- メール転送：対応（Email Assist：転送メールをタスク化、Pro/Business）。学習知識ではプロジェクト宛メール転送もあるが現行ページで未確認
- 保存時の必須入力：タスク名（ヘルプ「Enter a name for the task」）。期限・プロジェクトは任意

### 5. URL対応 / 画像対応
- URL：対応
- 画像単体保存：対応（タスクへの添付として）

### 6. OCR
- 未確認。関連：公式ヘルプ「Capture tasks from text, images, and documents」（画像からタスク抽出する AI 機能）があるが、画像内文字の検索ではない

### 7. 自動分類・AIタグ付け・要約
- 「Todoist Assist」：Ramble（音声→タスク）、Task Assist（タスク／サブタスク提案）、Email Assist（転送メール→タスク）、Filter Assist（全ユーザー）
- 無料枠：Ramble は Beginner 月10回、Pro 無制限。Todoist Assist・Email Assist は Pro/Business のみ（公式ヘルプ スニペット）
- 外部AI：複数の LLM プロバイダーを利用、Todoist のインフラ経由で処理（詳細は 15 参照）

### 8. 検索
- 未確認（現行ページで検索範囲を確認できず）

### 9. 再提示
- リマインダー：Beginner は「日時付きタスクの自動リマインダー」のみ（上限 700 件）。カスタム／時刻指定／位置情報／繰り返しリマインダーは Pro（公式「Usage limits」「Get started with Todoist Pro」スニペット）
- 期限設定：対応（due date / deadline）
- スヌーズ：未確認
- ランダム再提示：未確認（記載なし）

### 10. 週次まとめ・ダイジェスト
- 未確認（学習知識では週次の生産性メールや Karma があるが現行ページで確認できず）

### 11. 完了・保留・不要の扱い
- 完了：対応。アクティビティ履歴は Beginner 1週間（公式 Usage limits）
- アーカイブ：プロジェクトのアーカイブ（Google Sheets エクスポートが「完了タスクを含められる」ことから完了タスクは保持）
- 削除：対応（アカウント削除含む）

### 12. 無料枠（Beginner）
- アクティブな個人プロジェクト 5、フィルター 3、自動リマインダー 700、カスタムリマインダー不可、アクティビティ履歴 1週間、ファイル 5MB/件、Ramble 月10回（公式ヘルプ スニペット）

### 13. 価格
- Pro（USD、公式 pricing スニペット）：月額 USD 7、年額 USD 60（月換算 USD 5 ＝ 60÷12）
- Pro（JPY、公式日本語ヘルプ「Todoist プロ プラン：料金改定」スニペット、2025-12-10 適用）：月額 ¥1,118、年額 ¥10,080（月換算 ¥840 ＝ 10,080÷12）。App Store 経由の購読も同額との記載。改定前は月額 ¥588／年額 ¥5,856
  - 注意：別の検索結果要約では同改定を「¥894/月、¥8,064/年」と要約しており数値が食い違う。税込／税抜や表示条件の差の可能性があるため、要再確認
- Business（JPY）：月額 ¥1,600/人、年額 ¥14,400/人（月換算 ¥1,200）
- 確認日 2026-10-02 / 確認元 https://www.todoist.com/pricing 、https://www.todoist.com/ja/help/articles/todoist-pro-plan-pricing-update-bxBvHZuJZ （いずれも検索結果要約で確認、ページ本文は未取得）

### 14. アカウント要否
- 必要（メール等でサインアップ、クラウド同期）。iCloud 同期ではない

### 15. 外部AI利用の有無と送信先
- あり。公式「Todoist security, privacy, and compliance」「Introduction to Todoist Assist」スニペット：「厳選した複数の LLM プロバイダー」を利用、「データを OpenAI に直接送らず Todoist のインフラ経由で処理」「プロバイダーはモデル学習に使わないことを明示的に約束」「Todoist 自身も汎用 AI の学習に利用しない」
- 具体的なプロバイダー名：未確認

### 16. データ削除・書き出し
- エクスポート：プロジェクト単位の CSV（全プラン。アクティブタスク、ラベル、日付、優先度、コメントを含む）。Google Sheets へのエクスポート拡張（完了タスクを含められるが、デッドライン・コメント・添付・リマインダーは除外）
- アカウント削除：Web の設定 → Delete account（永久・不可逆、全データ削除）

### 17. レビューの不満（2〜4件）
- リマインダーや繰り返しタスクの設定が分かりにくい（日本 App Store レビューの要約：https://apps.apple.com/jp/app/todoist-todo-%E3%83%AA%E3%82%B9%E3%83%88-%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%80%E3%83%BC/id572688855?see-all=reviews 、投稿日不明）
- ラベルなど基本機能が有料のみ（同上）
- UI の学習コストが高く、コマンド的な入力が必要な場面がある（note 記事 https://note.com/tsukasa_yamato/n/n2ba59e364427 、日付不明）
- 2025年12月の値上げ（月額 ¥588→¥1,118 相当）に関する言及（https://penchi.jp/archives/13381.html は旧改定の記事。現行改定の不満は定量的に未確認）

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約経由）
- https://www.todoist.com/pricing
- https://www.todoist.com/help/articles/usage-limits-in-todoist-e5rcSY
- https://www.todoist.com/help/articles/add-files-and-links-to-todoist-from-your-mobile-devices-zez9K3cj
- https://www.todoist.com/help/todoist/todoist-and-ai/capture-tasks-from-text-images-and-documents-cAflh0WKe
- https://www.todoist.com/help/todoist/todoist-and-ai/introduction-to-todoist-assist-KgPP22q5O
- https://www.todoist.com/help/articles/todoist-security-privacy-and-compliance-mqmhua06
- https://www.todoist.com/privacy
- https://www.todoist.com/ja/help/articles/todoist-pro-plan-pricing-update-bxBvHZuJZ
- https://www.todoist.com/help/account-and-billing/security/import-or-export-a-project-as-a-csv-file-in-todoist-YC8YvN
- https://www.todoist.com/help/articles/delete-your-todoist-account-luq3xH
- https://apps.apple.com/jp/app/todoist-todo-%E3%83%AA%E3%82%B9%E3%83%88-%E3%82%BF%E3%82%B9%E3%82%AF%E7%AE%A1%E7%90%86/id572688855

### 19. 確認方法
- 検索結果要約で確認（ページ本文は未取得）。公式ページへの WebFetch は取得失敗（ネットワーク制限）。実機未試用。追加検索は WebSearch 回数上限により不可

---

## 3. TickTick（Appest）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：TickTick
- 運営者：Appest Limited（開発）、運営は杭州随笔记网络技术有限公司（Hangzhou Suibiji Network Technology）との記載（百度百科 スニペット）。2024年2月設立の TickTick Limited（香港）という法人情報もあり（第三者）
- 国：中国（杭州）／香港。公式ページでの所在地明記は未確認
- 提供状況：継続（2026年の価格・機能情報が複数、AI 機能・MCP のヘルプ記事あり）

### 2. 対象ユーザー・対応OS
- 対象：個人〜小規模チーム（コラボ機能あり）
- 対応OS：iOS、Android、Web、Mac、Windows（日本 App Store に Mac 版掲載 id966085870 あり、Web 版あり）。ブラウザ拡張：未確認（学習知識では Chrome/Firefox 拡張ありだが現行ページで確認できず）

### 3. 日本語UI
- 対応（公式「Translations」ページに Japanese を含む約26言語、ボランティア翻訳。公式 TickTick Japan ブログ https://blog.jp.ticktick.com/ あり）

### 4. 共有入口
- iOS 共有シート：**未確認**。公式ヘルプ（Add Tasks、Siri & URL Scheme、Shortcuts、Widgets）の検索結果に共有シートの記述を見つけられず。第三者記事（The Sweet Setup）に「iOS の Share Sheet からタスクにメタデータを追加できる」との記述あり。学習知識では「TickTick」共有拡張が存在するが現行公式ページで確認できず
- URL スキーム：対応（ticktick://v1/add 等、x-callback 対応、公式）
- Siri / ショートカット / ウィジェット：対応（公式）
- メール転送：未確認（学習知識ではメール→タスクあり。Spark 連携の公式記事はあり）
- 画像・スクショ：添付としてアップロード可。無料は 1日1件、Premium は 1日99件（公式ブログ「Premium 101」スニペット）
- 保存時の必須入力：未確認

### 5. URL対応 / 画像対応
- URL：タスク内容としてテキスト保存は可（推測：URL スキーム・共有）。公式明記は未確認
- 画像単体保存：添付として可（上限は上記）

### 6. OCR
- 未確認

### 7. 自動分類・AIタグ付け・要約
- 公式ヘルプ「AI Features」：AI Assistant（自然言語でタスク管理）、AI Voice Add（音声→タスク）、録音の文字起こし＋要約
- 無料／有料の区分：未確認
- 外部AI：「第三者 AI サービスプロバイダーを利用し、処理は機能提供に限定、データはモデル学習に使わない」（公式ヘルプ スニペット）。プロバイダー名は未確認

### 8. 検索
- 検索コマンドは URL スキームに存在（公式）。全文／添付内の検索範囲：未確認

### 9. 再提示
- リマインダー：無料でもタスクリマインダー対応（公式 upgrade ページ「Task Reminders」が Free に含まれる）。メールリマインダーは Premium
- 期限設定：対応。繰り返し：対応（推測、公式スニペットでは直接確認できず）
- スヌーズ：未確認
- ランダム再提示：未確認

### 10. 週次まとめ・ダイジェスト
- 未確認（学習知識では統計の週次サマリーがあるが現行ページで確認できず）

### 11. 完了・保留・不要の扱い
- 完了：対応。「Won't Do（やらない）」ステータス：未確認（学習知識にはあるが現行ページで確認できず）。リストのアーカイブ：未確認

### 12. 無料枠
- 9 リスト、1リストあたり 99 タスク、リスト＆カンバン表示、自然言語入力、タスクリマインダー、クロスプラットフォーム同期、添付 1日1件（公式 upgrade ページ／ブログ スニペット）
- Premium：299 リスト、1リスト 999 タスク、複数カレンダービュー、所要時間、メールリマインダー、テーマ、添付 1日99件

### 13. 価格
- USD：Premium 年額 USD 49.99（公式 upgrade ページ https://ticktick.com/about/upgrade の検索結果要約で確認。「月あたり USD 4.17 未満」の表現あり）。第三者サイトは 2026-07-23 時点で USD 35.99/年（期間限定割引）とも記載 → 割引価格は未確認。月額 USD：未確認
- JPY：未確認（公式ページ要約で確認できず）。参考値（第三者サイトのみ、未確認扱い）：日本 App Store 月額 ¥600・年額 ¥5,000、公式 Web 月額 ¥300・年額 ¥2,900（2026年5月時点、https://app-tatsujin.com/ticktick-free-vs-premium-comparison/ ）
- 確認日 2026-10-02 / 確認元 https://ticktick.com/about/upgrade （検索結果要約、ページ本文は未取得）

### 14. アカウント要否
- 必要（クラウド同期型）。iCloud 同期ではない

### 15. 外部AI利用の有無と送信先
- あり（第三者 AI プロバイダー利用、学習不使用の明記）。送信先の具体名：未確認
- 一般データ：保存時暗号化、アカウント削除後 90 日間バックアップに保持（公式プライバシーポリシー スニペット）

### 16. データ削除・書き出し
- Web 版 設定 → Account → Backup & Import でバックアップ生成・インポート可（公式「Data Backup and Import」）。形式：未確認（学習知識では CSV）
- アカウント削除：対応（削除後 90 日でバックアップから消去）

### 17. レビューの不満（2〜4件）
- カレンダー完全同期やカスタムスマートリストなど主要機能がサブスク限定（https://efficient.app/apps/ticktick 、https://habitbox.app/blog/ticktick-review 、2026）
- カレンダー同期（CalDAV/iCloud）が 15分〜1時間遅れる（同上）
- UI が雑然として古く感じる（https://efficient.app/apps/ticktick 、2026）
- 韓国語テキストを日付と誤認識する（Capterra レビュー要約 https://www.capterra.com/p/170641/TickTick/reviews/ 、日付不明）
- ※App Store レビュー本文は取得できず

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約経由）
- https://ticktick.com/about/upgrade
- https://ticktick.com/language_support?language=en_us
- https://help.ticktick.com/articles/7055782422935240704 （Add Tasks）
- https://help.ticktick.com/articles/7055781515422072832 （Siri & URL Scheme）
- https://help.ticktick.com/articles/7444685542580551680 （AI Features）
- https://help.ticktick.com/articles/7055781405648748544 （Data Backup and Import）
- https://ticktick.com/privacy?language=en_us
- https://blog.ticktick.com/2020/10/30/ticktick-premium-101/
- https://apps.apple.com/jp/app/ticktick-todo%E3%83%AA%E3%82%B9%E3%83%88%E3%81%A8%E3%82%BF%E3%82%B9%E3%82%AF%E7%AE%A1%E7%90%86%E3%81%A8%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%80%E3%83%BC/id626144601

### 19. 確認方法
- 検索結果要約で確認（ページ本文は未取得）。公式ページへの WebFetch は取得失敗（ネットワーク制限）。実機未試用。追加検索は WebSearch 回数上限により不可

---

## 4. Microsoft To Do

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Microsoft To Do
- 運営者：Microsoft Corporation（米国）
- 提供状況：継続（公式サポートページ・ストア掲載が現行。Outlook との統合が進行中。2026年8月に全クライアントで同期障害が報告されたとの第三者記述あり）

### 2. 対象ユーザー・対応OS
- 対象：個人（Microsoft アカウント）および Microsoft 365 利用者
- 対応OS：iOS、Android、Web（to-do.office.com）、Windows、Mac（Microsoft Store 掲載・公式ヘルプ）。ブラウザ拡張：未確認

### 3. 日本語UI
- 対応（公式サポートが日本語 https://support.microsoft.com/ja-jp/todo/... で提供、「今日の予定」「提案」の日本語表記を確認）

### 4. 共有入口
- iOS 共有シート：対応（Microsoft Tech Community 公式ブログ「Siri shortcuts, share extension」：共有ボタン → To Do を選択 → 保存先リストを選ぶ）
- URL / テキスト：対応（推測：共有拡張の対象。公式スニペットは種別を明記せず）
- 画像・スクショ・ファイル：未確認（学習知識ではタスクへのファイル添付可だが、共有シートから直接可能かは現行ページで確認できず）
- メール転送：未確認（Outlook のフラグ付きメールがタスク化される機能は学習知識にあるが現行ページで未確認）
- 保存時の必須入力：リストの選択（公式ブログ）。タイトルは共有内容から自動（推測）

### 5. URL対応 / 画像対応
- URL：対応（推測、上記）
- 画像単体保存：未確認

### 6. OCR
- 未確認

### 7. 自動分類・AIタグ付け・要約
- 未確認（公式ヘルプで Copilot 等の AI 機能の記載を確認できず）
- 関連：「提案」は AI 的な再提示機能（9・10 参照）

### 8. 検索
- 未確認

### 9. 再提示
- 「今日の予定（My Day）」：毎日空のリストから開始し、その日集中するタスクを選ぶ。未完了のタスクは翌日の「提案」に出る（公式 ja-jp ヘルプ スニペット）
- 「提案（Suggestions）」：電球アイコンから表示。今日・明日期限、期限超過、前日 My Day に入れて未完了のタスクなどを最大 7 件表示。設定で「期限が今日のタスクを自動で My Day に追加」も可能（公式ヘルプ スニペット）
- リマインダー・期限・繰り返し：対応（Siri ショートカット設定で「リマインダー・期限・メモを自動追加」と公式ブログ）
- スヌーズ：未確認
- ランダム再提示：未確認

### 10. 週次まとめ・ダイジェスト
- 未確認

### 11. 完了・保留・不要の扱い
- 完了：対応（完了済みタスクの表示切替）。アーカイブ：未確認。削除：対応

### 12. 無料枠
- 無料（Microsoft アカウントで利用）。有料プランなし（Microsoft 365 契約と連動する機能はあるが To Do 自体に課金なし）。件数上限：未確認

### 13. 価格
- 無料（確認日 2026-10-02、確認元 https://www.microsoft.com/ja-jp/microsoft-365/microsoft-to-do-list-app 、検索結果要約）

### 14. アカウント要否
- Microsoft アカウント必須（推測：サインインなしでは使用不可。公式明記は未確認）

### 15. 外部AI利用の有無と送信先
- 未確認（To Do 固有の AI 機能・外部送信の記載を確認できず）

### 16. データ削除・書き出し
- アプリ内エクスポート機能：なしとの回答（Microsoft Q&A「There is no way to export data from Microsoft To Do for Office 365 users」）。個人アカウントは Outlook.com 設定 → 全般 → エクスポートで取得可能との回答（Q&A、Microsoft 公式ヘルプでの明記は未確認）
- 印刷：Windows アプリ／Web で「リストを印刷」（第三者記事）
- アカウント削除：Microsoft アカウント閉鎖（30/60 日の再開猶予後にデータ削除、公式ヘルプ）

### 17. レビューの不満（2〜4件）
- デスクトップとモバイル間の同期遅延、2026年8月の全クライアント同期障害（Microsoft Q&A / Tech Community 経由の要約。URL：https://techcommunity.microsoft.com/category/microsoftto-do/discussions/to-do 、日付 2026年8月とされる）
- iOS/iPadOS のウィジェット対応要望（US App Store レビュー要約 https://apps.apple.com/us/app/microsoft-to-do/id1212616790 、日付不明）
- 共同作業・高度機能の不足（Software Advice レビュー https://www.softwareadvice.com/project-management/microsoft-to-do-profile/reviews/ 、日付不明）
- データのエクスポート手段がない（Microsoft Q&A https://learn.microsoft.com/en-us/answers/questions/4739090/ 、日付不明）

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約経由）
- https://support.microsoft.com/en-us/todo/my-day-and-suggestions
- https://support.microsoft.com/ja-jp/todo/plan-and-connect-with-microsoft-to-do
- https://support.microsoft.com/ja-jp/todo/welcome-to-microsoft-to-do
- https://techcommunity.microsoft.com/blog/to-doblog/discover-all-our-latest-features-on-ios-%E2%80%93-siri-shortcuts-share-extension-and-mor/1082376
- https://www.microsoft.com/ja-jp/microsoft-365/microsoft-to-do-list-app
- https://apps.apple.com/us/app/microsoft-to-do/id1212616790
- https://learn.microsoft.com/en-us/answers/questions/4739090/there-is-no-way-to-export-data-from-microsoft-to-d
- https://support.microsoft.com/en-us/account-billing/how-to-close-your-microsoft-account-c1b2d13f-4de6-6e1b-4a31-d9d668849979

### 19. 確認方法
- 検索結果要約で確認（ページ本文は未取得）。公式ページへの WebFetch は取得失敗（ネットワーク制限）。実機未試用。追加検索は WebSearch 回数上限により不可

---

## 5. Apple リマインダー（iOS 標準）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：リマインダー（Reminders）
- 運営者：Apple Inc.（米国）
- 提供状況：継続（iOS 標準アプリ。iPhone ユーザガイド現行版に記載）

### 2. 対象ユーザー・対応OS
- 対象：全 iPhone ユーザー
- 対応：iOS、iPadOS、macOS、watchOS、iCloud.com（Web）。Android / Windows：ネイティブアプリなし（iCloud.com 経由のみ、推測）。ブラウザ拡張：なし（推測）

### 3. 日本語UI
- 対応（iOS 日本語環境で日本語。Apple サポートに日本語ガイドあり）

### 4. 共有入口
- iOS 共有シート：対応。「他のアプリに戻るためのリンクを追加：対象アプリの共有ボタン → リマインダー アイコン」（公式「Add details in Reminders on iPhone」スニペット）
- URL：対応（Safari の Web ページ、マップの場所など）
- 画像・スクショ：リマインダー内で「写真」ボタンから撮影／ライブラリから選択／書類スキャンで添付可（公式）。共有シートから画像を直接リマインダーへ：未確認
- テキスト：共有シート経由（推測）
- メール転送：なし（推測）。Siri 提案：メール・メッセージ本文からリマインダー候補を提示（公式「Siri Suggestions」スマートリスト）
- 保存時の必須入力：未確認（推測：タイトルは共有元から自動）

### 5. URL対応 / 画像対応
- URL：対応
- 画像単体保存：対応（添付として）

### 6. OCR
- 未確認（iOS のテキスト認識表示（Live Text）は写真・カメラ・Safari 等で機能するが、リマインダー内の添付画像を文字検索できるかは公式に確認できず）

### 7. 自動分類・AIタグ付け・要約
- Apple Intelligence（対応機種・地域）：他アプリのテキストから「提案されたリマインダー」（Safari のレシピの材料、メールのアクションアイテムなど）、リスト内の関連リマインダーを自動でセクション分類（公式「Use Apple Intelligence in Reminders」スニペット）
- 無料。端末内処理または Private Cloud Compute（15 参照）

### 8. 検索
- 未確認（学習知識ではタイトル・メモの検索可だが現行ページで確認できず）

### 9. 再提示
- 日時通知：対応。場所通知：対応（到着時／出発時、Bluetooth 接続の車に乗ったとき）（公式）
- 期限：対応。繰り返し：対応（推測、公式スニペットでは直接確認できず）
- スマートリスト「今日」（当日・期限超過）「日時設定済み」「フラグ付き」「完了」（公式「Use Smart Lists」）
- スヌーズ：未確認（レビューに「スヌーズオプションが欲しい」との要望あり）
- ランダム再提示：未確認

### 10. 週次まとめ・ダイジェスト
- 未確認（記載なし）

### 11. 完了・保留・不要の扱い
- 完了：丸をタップ。「完了済みを表示」で確認、完了スマートリストあり（公式）
- 保留：なし（推測。フラグ・日付変更で代替）
- 削除：対応

### 12. 無料枠
- 無料・件数上限なし（推測：iCloud 容量の範囲内）

### 13. 価格
- 無料（iOS 同梱）。確認日 2026-10-02 / 確認元 https://support.apple.com/guide/iphone/add-details-iphec7a1de82/ios （検索結果要約）

### 14. アカウント要否
- Apple Account / iCloud で同期。推測：iCloud をオフにしても端末内で利用可能

### 15. 外部AI利用の有無と送信先
- Apple Intelligence は可能な限り端末内処理、複雑な要求は Private Cloud Compute（Apple シリコン サーバー）で処理し、データは保存されず Apple もアクセス不可（公式「Apple Intelligence and privacy on iPhone」スニペット）。第三者 AI への送信：リマインダー機能に関しては記載なし（未確認。ChatGPT 連携は Siri/作文ツールの別機能）

### 16. データ削除・書き出し
- エクスポート：未確認（公式ガイドで確認できず。学習知識では標準のエクスポート機能なし）
- 削除：リマインダー／リスト単位で削除可。iCloud からの削除：未確認

### 17. レビューの不満（2〜4件）
- 通知が届かない／表示されてすぐ消える（Apple Community https://discussions.apple.com/thread/254601701 「Reminders App is suddenly unreliable」、日付不明）
- iCloud 同期の問題（Mac 側で CPU 100%、同期できない）（https://discussions.apple.com/thread/250852651 、日付不明）
- 将来日時のリマインダーが勝手に当日にリセットされる（US App Store レビュー要約 https://kimola.com/reports/unlock-insights-apple-reminders-app-feedback-analysis-app-store-us-141966 、日付不明）
- サブリスト・スヌーズ・メモとの連携が欲しい（同上）

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約経由）
- https://support.apple.com/guide/iphone/add-details-iphec7a1de82/ios
- https://support.apple.com/guide/iphone/create-reminders-iph88463e18/ios
- https://support.apple.com/guide/iphone/use-smart-lists-iphe882772ed/ios
- https://support.apple.com/en-us/102484
- https://support.apple.com/guide/iphone/apple-intelligence-and-privacy-iphe3f499e0e/ios
- https://support.apple.com/en-in/guide/iphone/iphcb580b580/ios （Use Apple Intelligence in Reminders）

### 19. 確認方法
- 検索結果要約で確認（ページ本文は未取得）。support.apple.com への WebFetch は取得失敗（ネットワーク制限）。実機未試用。追加検索は WebSearch 回数上限により不可

---

## 6. Apple メモ ＋ Safari リーディングリスト ＋ Safari タブグループ（iOS 標準）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：メモ（Notes）、Safari リーディングリスト、Safari タブグループ
- 運営者：Apple Inc.（米国）
- 提供状況：継続（いずれも iPhone ユーザガイド現行版に記載）

### 2. 対象ユーザー・対応OS
- 対象：全 iPhone ユーザー
- 対応：iOS、iPadOS、macOS、iCloud.com（メモ）。Safari リーディングリスト／タブグループは iCloud 経由で Apple デバイス間同期（Windows 版 iCloud でのブックマーク同期は未確認）

### 3. 日本語UI
- 対応（iOS 標準。Apple サポートに日本語ガイドあり）

### 4. 共有入口
- メモ：共有シート → 「メモ」または「クイックメモに追加」で他アプリの内容を追加（公式「Use Notes」スニペット）。マップの場所、Safari の Web ページ、ファイルの PDF、スクリーンショットを添付として追加可（公式「Add photos, video, and more to notes」）
- リーディングリスト：Safari の共有 → 「リーディングリストに追加」。リンク長押しで開かずに追加も可（公式「Save webpages to read later」）
- タブグループ：タブを長押し → 「タブを移動」→ 新規タブグループ（公式「Organize your tabs with Tab Groups」）。共有シートからの保存ではない
- 保存時の必須入力：メモは不要（推測）。リーディングリストは不要（ワンタップ）

### 5. URL対応 / 画像対応
- メモ：URL 対応（リンク添付）、画像対応（写真・スクショ・スキャン）
- リーディングリスト：URL のみ。画像：非対応（Web ページ専用機能であり、公式ガイドに画像保存の記載なし → 推測ベース）
- タブグループ：URL（タブ）のみ

### 6. OCR
- メモ：対応。「検索はメモ内の画像の内容を認識（例：bike で自転車の画像）」「スキャン書類や画像内の特定のテキスト（領収書など）を検索可」（公式「Search through your notes on iPhone」スニペット）。「添付ファイルを含める」で PDF 等も検索対象
- リーディングリスト／タブグループ：なし（推測）

### 7. 自動分類・AIタグ付け・要約
- メモ：Apple Intelligence の作文ツール（要約・校正）が利用可能（学習知識。現行ガイドのスニペットでは直接確認できず → 未確認）。自動タグ付け：未確認
- リーディングリスト／タブグループ：なし（推測）

### 8. 検索
- メモ：全文（タイプ・手書き）＋画像内＋添付ファイル（公式）
- リーディングリスト：未確認（第三者レビューに「保存物を探すのが難しい」との不満）
- タブグループ：Safari のタブ検索（未確認）

### 9. 再提示
- メモ：リマインダーなし（公式ガイドに記載なし → 未確認。推測：なし。リマインダーアプリとの連携で代替）
- リーディングリスト：未読／既読の管理のみ（長押しで「既読にする」「削除」など、公式）。通知やリマインダーなし（推測）
- タブグループ：なし（推測）
- ランダム再提示：いずれもなし（推測）

### 10. 週次まとめ・ダイジェスト
- なし（推測、公式記載なし）

### 11. 完了・保留・不要の扱い
- メモ：ピン留め、フォルダ、削除（「最近削除した項目」保持期間は未確認）
- リーディングリスト：既読／未読、削除。「未読」表示で絞り込み（Mac 版公式ガイドに「未読」の記載。iPhone 版は第三者記述）
- タブグループ：タブを閉じる／グループ削除

### 12. 無料枠
- 無料（iCloud 容量の範囲内。iCloud 無料 5GB、学習知識）

### 13. 価格
- 無料（iOS 同梱）。確認日 2026-10-02 / 確認元 https://support.apple.com/guide/iphone/search-notes-iphb8628c6b8/ios 、https://support.apple.com/guide/iphone/save-pages-to-a-reading-list-iph1a4721132/ios （検索結果要約）

### 14. アカウント要否
- iCloud で同期。推測：端末内のみでも使用可（「iPhone 内」メモ）。リーディングリストのオフライン保存は「設定 → アプリ → Safari → 自動的にオフライン保存」（公式）

### 15. 外部AI利用の有無と送信先
- Apple Intelligence：端末内処理または Private Cloud Compute（Apple リマインダーの項と同じ公式ページ）。メモ固有の第三者 AI 送信：記載なし（未確認）

### 16. データ削除・書き出し
- メモ：未確認（学習知識では PDF 書き出し・共有は可、一括エクスポートは Mac 経由）。iCloud.com で添付の表示・ダウンロード可（公式 iCloud ガイド）
- リーディングリスト：エクスポート機能なし（推測。公式記載なし）
- 削除：項目単位で可

### 17. レビューの不満（2〜4件）
- リーディングリストに保存したものが読まれず積み上がる、タグ・フォルダがない（https://keep.md/blog/native-browser-reading-lists 、https://pawelgrzybek.com/apple-please-fix-the-safari-reading-list/ 、日付不明）
- 未読と既読の区別がしづらい（「すべて」「未読」の切替が目立たない）（同上）
- リーディングリストが保存されない／同期しない（Apple Community https://discussions.apple.com/thread/254598683 、日付不明）
- 半年後に目的の保存物を探すのが困難（https://www.theodorehq.com/muse/blog/posts/safari-reading-list-alternative 、日付不明）

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約経由）
- https://support.apple.com/guide/iphone/search-notes-iphb8628c6b8/ios
- https://support.apple.com/guide/iphone/add-attachments-iph23f4d9aa9/ios
- https://support.apple.com/en-us/118442 （Use Notes on your iPhone）
- https://support.apple.com/guide/iphone/save-pages-to-a-reading-list-iph1a4721132/ios
- https://support.apple.com/guide/iphone/organize-your-tabs-with-tab-groups-iph3028ebf68/ios
- https://support.apple.com/guide/safari/keep-a-reading-list-sfri35905/mac （Mac 版、未読表示の参考）
- https://support.apple.com/guide/iphone/apple-intelligence-and-privacy-iphe3f499e0e/ios

### 19. 確認方法
- 検索結果要約で確認（ページ本文は未取得）。support.apple.com への WebFetch は取得失敗（ネットワーク制限）。実機未試用。追加検索は WebSearch 回数上限により不可

---

## ATO 観点の所見（推測を含む）
- 共有シート保存：Things・Todoist・MS To Do・Apple リマインダー・Apple メモは公式に共有シート対応を確認。TickTick は公式ページで直接確認できず（未確認）。Todoist は保存時に「タスク名の入力」が必要（必須入力あり）。Apple メモ・リーディングリストは入力なしで保存できる
- 画像・スクショ：Todoist・Apple リマインダー・Apple メモは画像添付を公式確認。TickTick は無料 1日1件の上限。Things は未確認（推測：非対応）。MS To Do は未確認
- 再提示：各タスク管理アプリは「日時／場所リマインダー」型。「提案」型は MS To Do（My Day 提案、未完了を翌日提案）と Apple リマインダー（Siri 提案・Apple Intelligence）。**ランダム再提示（resurfacing）や「忘れた頃に出す」機能はいずれも公式に確認できなかった**（推測：ATO の差別化余地）
- 完了・アーカイブ：Things は Logbook、Todoist は完了＋プロジェクトアーカイブ、Apple リマインダーは「完了済み」、リーディングリストは「既読」。「不要（やらない）」の明示ステータスは公式に確認できず（TickTick の Won't Do は未確認）
- OCR：Apple メモのみ公式に画像内テキスト検索を確認。タスク管理 4 サービスは未確認
- 外部 AI：Todoist（複数 LLM、Todoist インフラ経由、学習不使用）、TickTick（第三者 AI、学習不使用）が明記。Apple は端末内／Private Cloud Compute。Things・MS To Do は記載なし
- エクスポート：Things（SQLite）、Todoist（CSV）、TickTick（バックアップ）、MS To Do（アプリ内なし、Outlook.com 経由）、Apple リマインダー／リーディングリスト（未確認・推測なし）
