# E班：無料の既存保存先（ATOが乗り換えを求める相手）調査

確認日：2026-10-02（日本時間）
調査担当：競合調査（E班）

## 調査環境に関する重要な注記（必ず読むこと）

- 本環境のネットワーク方針により、**WebFetch は試したすべてのホストで EGRESS_BLOCKED（403相当）** となりました。公式ヘルプ・公式サイト・App Store/Play Store・主要ニュースサイトのいずれも本文を取得できていません。
- そのため本報告の事実は、**すべて WebSearch の結果要約（検索エンジンが返した公式ページ等の抜粋）で確認したもの**です。各項目に「検索結果要約で確認（ページ本文は未取得）」と明記します。「ページ取得で確認」できた項目は **ゼロ** です。
- WebSearch の予算（セッション合計200回）も途中で上限に達し、後半で予定していた補足検索（TikTokの動画お気に入り公式ページ、Pinterestの通知仕様、Xブックマーク検索、写真アプリのテキスト検索、Keepメモの共有入口、各サービスのレビュー等）は実行できませんでした。該当項目は「未確認」としています。
- いずれのサービスも **実機未試用** です。
- 取得失敗URL（ネットワーク制限）は末尾の一覧にまとめました。

---

## 1. iOS 写真アプリのスクリーンショット ＋ Visual Intelligence（画面内容） ＋ Live Text（テキスト認識）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：写真アプリのスクリーンショット保存、Visual Intelligence（ビジュアルインテリジェンス、画面内容に対する機能）、Live Text（テキスト認識表示）
- 運営者：Apple Inc.（米国）
- 提供状況：継続。Visual Intelligence の画面内容対応は iOS 26 で提供開始と報じられ、Apple公式ユーザガイドにも iOS 26 版ページ（`/guide/iphone/use-visual-intelligence-iph12eb1545e/26/ios/26`）が存在（検索結果要約で確認）。なお検索結果要約には、現行ガイドが「iOS 27 以降の Apple Intelligence」を前提とする記述もあり（2026-09 に iOS 27 がリリース済みとみられる。Apple Newsroom "Major updates for Apple's software platforms are now available" 2026/09 がヒット。本文未取得）。

### 2. 対象ユーザー・対応OS
- iOS（iPhone）。Apple Intelligence 対応機種：iPhone 15 Pro / 15 Pro Max、iPhone 16 以降（Apple Support 121115 の検索結果要約で確認）。
- 要件：iOS 18.1 以降、空き容量 7GB 以上、デバイス言語と Siri 言語を同一の対応言語にする（同上）。
- Live Text／スクリーンショット保存自体は Apple Intelligence 非対応機種でも利用可（Live Text は iOS 15 以降の機能として公式ガイドにページあり。対応機種の詳細は未確認）。

### 3. 日本語UI
- Apple Intelligence の対応言語に日本語が含まれる（iOS 18.4 以降。Apple Support 121115 および Apple Newsroom 2025/03 の検索結果要約で確認）。
- Live Text の対応言語に日本語が含まれる（apple.com の Feature Availability ページの検索結果要約で確認）。
- 画面内容に対する Visual Intelligence が日本語で利用可能かは **未確認**（Feature Availability の該当項目を取得できず。推測：Apple Intelligence 対応言語に準じて日本語で使えると思われるが未確認）。

### 4. 共有入口
- スクリーンショット：サイドボタン＋音量上ボタンで撮影 → 画面下に Visual Intelligence のツールが表示（Apple Support ガイド "Learn about what's on your iPhone screen with Visual Intelligence" の検索結果要約で確認）。
- iOS共有シート／URL／ファイル／テキストの「保存」という概念はなし（写真アプリにスクショが保存されるのみ）。
- ブラウザ拡張・メール転送：非該当。

### 5. URL対応 / 画像対応
- URL：スクショ上のWebサイトを「タップして該当サイトへ移動」できる（検索結果要約で確認）。URL自体を保存する仕組みはなし。
- 画像：スクショは写真アプリに画像として保存される（標準機能）。

### 6. OCR
- Live Text：写真内のテキストをコピー・共有・翻訳・Webサイトを開く・電話をかける・調べる（Look Up）が可能（Apple Support 120004 およびユーザガイドの検索結果要約で確認）。
- 写真アプリで「写真内の文字」を検索語として検索できるか：**未確認**（該当ガイド "Search for photos and videos on iPhone" はヒットしたが本文未取得。学習知識では Live Text の文字が写真検索の対象になるが、現行ページで確認できず）。

### 7. 自動分類・AIタグ付け・要約
- Visual Intelligence（画面内容）：「Summarize（要約）」「Read Aloud（読み上げ）」ボタンあり（検索結果要約で確認）。
- 「Ask（ChatGPTに質問）」は外部AI（OpenAI ChatGPT）を利用（検索結果要約で確認）。
- スクショの自動分類・タグ付け：未確認（写真アプリの自動アルバム「スクリーンショット」は存在するが、内容に基づく自動整理は確認できず）。
- 無料。

### 8. 検索
- Visual Intelligence の「Search」：画面上の類似アイテムをWeb検索（検索結果要約で確認）。
- 写真アプリ内のスクショ内文字検索：未確認（上記6参照）。

### 9. 再提示（リマインダー・スヌーズ・期限）
- 「Add to Calendar（カレンダーに追加）」：スクショ内のイベント情報からカレンダーイベントを作成（Apple Support ガイドの検索結果要約で確認）。
- リマインダー作成：公式ガイドの検索結果要約には記載なし。9to5Mac（2026-03-05）は「リマインダーは Visual Intelligence のエコシステムに含まれていない」と報道（本文未取得、検索結果要約のみ）。→ **公式ページで「非対応」と明記されたことは確認できていないため「未確認（報道では非対応）」**。
- スヌーズ・ランダム再提示・期限：未確認（検索結果に記載なし）。

### 10. 週次まとめ・ダイジェスト
- 未確認（検索結果に記載なし。写真アプリの「メモリー」は別概念）。

### 11. 完了・保留・不要の扱い
- 写真アプリの削除／最近削除した項目（標準）。スクショ単位の「完了」ステータスはなし（推測：標準の写真管理に準じる）。

### 12. 無料枠
- OS標準機能、無料。iCloud写真の容量はiCloudプランに依存（詳細未確認）。

### 13. 価格
- 無料（OS付属）。確認日 2026-10-02。確認元：Apple Support ガイド（検索結果要約）。

### 14. アカウント要否
- Apple Intelligence 利用に Apple Account のサインインが必要かは未確認。写真アプリ・Live Text はサインアップ不要（標準機能）。iCloud写真同期は任意。

### 15. 外部AI利用
- 「Ask」は ChatGPT（OpenAI）へ送信（検索結果要約で確認）。送信条件・ポリシー詳細は未確認。
- Apple Intelligence 自体は端末内処理と Private Cloud Compute を使うとされるが、現行ページで未確認。

### 16. データ削除・書き出し
- 写真アプリから画像として書き出し・削除可能（標準機能）。Visual Intelligence が生成した情報の保存・書き出しは未確認。

### 17. レビューの不満
- 未取得（App Store レビューは取得失敗）。参考：Fernandina Observer「Apple's Visual Intelligence is clever. But it can't remember.」（https://www.fernandinaobserver.org/stories/apples-visual-intelligence-is-clever-but-it-cant-remember,99018 ）という記事タイトルがヒット（本文未取得、投稿日不明）。タイトルから「記憶（保持・再提示）がない」という論点がうかがえるが、内容は未確認。

### 18. 出典URL一覧（確認日 2026-10-02、いずれも検索結果要約のみ）
- https://support.apple.com/guide/iphone/learn-iphone-screen-visual-intelligence-emvqp5vyxukx/ios
- https://support.apple.com/guide/iphone/use-visual-intelligence-iph12eb1545e/26/ios/26
- https://support.apple.com/en-us/121115 （How to get Apple Intelligence）
- https://www.apple.com/newsroom/2025/03/apple-intelligence-features-expand-to-new-languages-and-regions-today/
- https://support.apple.com/en-us/120004 （写真内テキストのコピー・翻訳）
- https://support.apple.com/guide/iphone/live-text-interact-content-a-photo-video-iph37fdd714b/ios
- https://www.apple.com/ios/feature-availability/
- https://9to5mac.com/2026/03/05/ios-26-gives-apples-calendar-app-a-convenient-new-advantage/
- https://9to5mac.com/2026/01/11/ios-26-new-screenshot-apple-intelligence-favorite-feature/

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。

---

## 2. Google「Pixel Screenshots」（Android / Pixel）

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Pixel Screenshots（Play Store パッケージ名 com.google.android.apps.pixel.agent）
- 運営者：Google LLC（米国）
- 提供状況：継続（Pixel 9 で2024年に提供開始、以後の Pixel Drop で機能追加。検索結果要約で確認）。

### 2. 対象ユーザー・対応OS
- Android（Pixel 専用）。対応機種：Pixel 9 / 9 Pro / 9 Pro XL / 9 Pro Fold、Pixel 10 / 10 Pro / 10 Pro XL / 10 Pro Fold（Google 公式ヘルプ 15312581 の検索結果要約で確認）。別の検索結果要約では Pixel 11 シリーズも列挙されていたが、同一ページの版違いとみられ、どちらが現行かは未確認。
- iOS・Web・Mac・Windows：非該当（Pixel 専用アプリ）。

### 3. 日本語UI
- 対応言語：英語・ドイツ語・日本語（公式ヘルプの検索結果要約で確認）。
- 提供国：オーストラリア、カナダ、ドイツ、インド、アイルランド、日本、マレーシア、シンガポール、英国、米国（公式ヘルプ en-uk 版の検索結果要約で確認。別要約では国数が少なく、版の差とみられる）。日本は含まれる。

### 4. 共有入口
- スクリーンショット撮影時に自動で取り込み（アプリ設定で保存・AI機能のオン／オフ可。検索結果要約で確認）。
- 共有メニューからの追加、URL・テキスト・ファイル単体の保存：未確認。

### 5. URL対応 / 画像対応
- 画像（スクショ）が主対象。撮影元のアプリ／Webサイトなどのメタデータも処理（Google Store 記事の検索結果要約で確認）。
- URL単体の保存：未確認。

### 6. OCR
- Gemini Nano（マルチモーダル）がスクショ内の情報を自動処理し、AIタイトルと要約を生成（検索結果要約で確認）。

### 7. 自動分類・AIタグ付け・要約
- AI生成のタイトル・要約、内容に基づく「おすすめのアクション」（リマインダー設定、Google カレンダー追加など）。コレクションへの追加を自動提案する「suggestions」機能あり。
- 端末内 AI（Gemini Nano）で処理、クラウド不使用、オフライン動作（Google Store 記事および blog.google の検索結果要約で確認）。
- 無料。

### 8. 検索
- AI機能オン時、保存した全スクショを自然言語で横断検索し、アクションチップで操作可能（公式ヘルプの検索結果要約で確認）。

### 9. 再提示
- スクショごとにリマインダー設定（スクショをタップ→スケジュール選択／ベルアイコン）で通知を受け取れる（公式ヘルプの検索結果要約で確認）。
- スヌーズ・ランダム再提示・期限：未確認。

### 10. 週次まとめ・ダイジェスト
- 未確認（検索結果に記載なし）。

### 11. 完了・保留・不要の扱い
- 削除可（詳細未確認）。設定に「Delete all AI summaries and metadata（すべてのAI要約とメタデータを削除）」あり（検索結果要約で確認）。

### 12. 無料枠
- 無料（Pixel 同梱アプリ。件数上限は未確認）。

### 13. 価格
- 無料（Play Store 掲載、対応 Pixel 限定）。確認日 2026-10-02。確認元：Play Store 掲載ページ（取得失敗、検索結果要約のみ）。

### 14. アカウント要否
- Google アカウント（Pixel 自体に必要）。アプリ単体のサインアップは未確認。

### 15. 外部AI利用
- 端末内 Gemini Nano で処理し、許可なくアプリや Google と共有されない旨の記述あり（Google Store 記事の検索結果要約で確認）。
- NotebookLM へスクショを書き出すアクションあり（blog.google の検索結果要約で確認。これは利用者操作による外部送信）。

### 16. データ削除・書き出し
- AI要約・メタデータの一括削除あり（上記）。スクショ自体は Google フォト等への保存と別管理かは未確認。書き出し形式：未確認（NotebookLM 連携のみ確認）。

### 17. レビューの不満
- 未取得（Play Store ページ取得失敗、追加検索は予算切れ）。

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約のみ）
- https://support.google.com/pixelphone/answer/15312581?hl=en
- https://support.google.com/pixelphone/answer/15312581?hl=en-uk
- https://store.google.com/intl/en/ideas/articles/pixel-screenshots/
- https://blog.google/products/pixel/google-pixel-screenshots-tips/
- https://play.google.com/store/apps/details?id=com.google.android.apps.pixel.agent&hl=en_US

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。

---

## 3. LINE Keep / Keepメモ

### 1. 名称 / 運営者 / 国 / 提供状況
- LINE Keep：**終了**。2024-08-28 に新規保存・追加・編集を停止、2024-08-29〜2025-08-28 は閲覧・ダウンロードのみ、2025-08-29 に完全終了しデータ削除（LINE お知らせ documentId=100000302 および ITmedia 2024-05-10 記事の検索結果要約で確認）。
- Keepメモ：**継続**（2020年7月開始の自分専用トークルーム。LINE ヘルプおよび上記お知らせの検索結果要約で確認）。
- 運営者：LINEヤフー株式会社（日本）。

### 2. 対象ユーザー・対応OS
- iOS、Android、PC（Windows／Mac 版 LINE にも Keepメモのヘルプあり。検索結果要約で確認）。

### 3. 日本語UI
- 日本語（LINE ヘルプが日本語で提供。検索結果要約で確認）。

### 4. 共有入口
- iOS共有シート：未確認（LINE の共有拡張から Keepメモ を宛先に選べるかは現行ページで確認できず）。
- URL・画像・ファイル・テキスト：トークルームとして送信できるものは保存可能とみられる（推測）。

### 5. URL対応 / 画像対応
- トークとして送信する形で URL・画像を残せる（推測：トークルーム仕様に準じる。公式ページ本文未取得）。

### 6. OCR
- 未確認（LINE のトーク内 OCR 機能の有無を確認できず）。

### 7. 自動分類・AIタグ付け・要約
- 未確認。

### 8. 検索
- 未確認（トーク検索に準じる可能性があるが確認できず）。

### 9. 再提示
- 未確認（リマインダー・スヌーズ機能の記載なし）。

### 10. 週次まとめ
- 未確認（記載なし）。

### 11. 完了・保留・不要の扱い
- メッセージの削除（推測：トークルームの操作に準じる）。

### 12. 無料枠・制限
- Keepメモを含むトークルームで送受信した画像・動画・ファイルのサーバー保存期間は「一定期間のみ」で、期間終了後は表示・ダウンロード・送受信不可。保存期間の詳細は案内されない（LINE ヘルプの検索結果要約で確認）。
- 旧 Keep の「最大1GB、50MB超のファイルは30日」は終了した Keep の制限（検索結果要約で確認）。Keepメモには適用されない（Keepメモの容量上限は未確認）。

### 13. 価格
- 無料。確認日 2026-10-02。確認元：LINE ヘルプ（検索結果要約）。

### 14. アカウント要否
- LINE アカウント必須。

### 15. 外部AI利用
- 未確認。

### 16. データ削除・書き出し
- 旧 Keep はバックアップ（ダウンロード）案内あり（お知らせの検索結果要約で確認）。Keepメモの書き出し形式は未確認。

### 17. レビューの不満
- 未取得。

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約のみ）
- https://notice.line.me/line/ios/document/notice?documentId=100000302&lang=ja （Keepの終了・バックアップのお知らせ）
- https://help.line.me/line/smartphone/pc?lang=ja&contentId=20017696 （Keepメモの基本的な使い方）
- https://help.line.me/line/desktop/pc?lang=ja&contentId=20017696 （Windows/Mac Keepメモ）
- https://help.line.me/line/ios/sp?lang=ja&contentId=20018617 （保存期間に関するヘルプ）
- https://www.itmedia.co.jp/news/articles/2405/10/news156.html

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。

---

## 4. Instagram「保存済み」「コレクション」

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：保存済み（Saved）、コレクション（Collections）、共同コレクション（Collaborative collections）
- 運営者：Meta Platforms, Inc.（米国）
- 提供状況：継続。

### 2. 対象ユーザー・対応OS
- iOS、Android、Web。共同コレクションは「パソコンでは利用不可」（help.instagram.com 3129045784070725 の検索結果要約で確認）。

### 3. 日本語UI
- 未確認（日本語ヘルプの存在は検索で直接確認せず。推測：提供あり）。

### 4. 共有入口
- Instagram 内の投稿・リールの保存アイコンのみ。iOS共有シートから外部コンテンツを保存する仕組みはなし（推測：公式ヘルプに該当記述なし）。

### 5. URL対応 / 画像対応
- Instagram 投稿のみ。外部URL・画像単体は非該当。

### 6. OCR
- 未確認（記載なし）。

### 7. 自動分類・AIタグ付け・要約
- 未確認（記載なし）。コレクションは手動作成（保存アイコン長押しで既存コレクション選択または新規作成。公式ヘルプの検索結果要約で確認）。

### 8. 検索
- 未確認（保存済み内の検索の有無を確認できず）。

### 9. 再提示
- 未確認（リマインダー・通知の記載なし）。保存は投稿者に通知されない、保存済みは自分だけが閲覧可（公式ヘルプの検索結果要約で確認）。

### 10. 週次まとめ
- 未確認（記載なし）。

### 11. 完了・保留・不要の扱い
- コレクションの名前変更・投稿の追加／削除・コレクション削除（help 1524436600950937 の検索結果要約で確認）。

### 12. 無料枠
- 無料。件数上限：未確認。

### 13. 価格
- 無料。確認日 2026-10-02。確認元：Instagram ヘルプセンター（検索結果要約）。

### 14. アカウント要否
- Instagram アカウント必須。

### 15. 外部AI利用
- 未確認。

### 16. データ削除・書き出し
- アカウントセンター →「情報をエクスポート（Export your information）」で、保存済み投稿（saved_posts.json）と保存コレクション（saved_collections.json）が、投稿へのリンク・アカウント・保存日時の参照情報として含まれる。画像・動画・キャプション本体は含まれない（第三者解説 Stashr／AllMySaves の検索結果要約で確認。**公式ヘルプ本文は未取得**）。

### 17. レビューの不満
- note「保存した投稿、どこ行ったか分からなくなってた。Instagramのコレクションで仕分けた」（https://note.com/genial_rose6801/n/nb78396bfac2c 、投稿日未確認）：保存しっぱなしで見失う体験談（検索結果要約で確認）。
- 知る見る！図鑑「インスタの保存済投稿などの整理テク」（https://brains.hatenablog.com/entry/2025/05/16/000020 、2025-05-16）：「とりあえず保存して見返そうと思ったまま忘れ、ひとつの場所に積み上がる」問題を前提に整理法を解説（検索結果要約で確認）。
- App Store レビュー：取得失敗。

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約のみ）
- https://help.instagram.com/1744643532522513 （Save posts you see on Instagram）
- https://help.instagram.com/1524436600950937 （コレクションの編集・削除）
- https://help.instagram.com/3129045784070725 （共同コレクション）
- https://help.instagram.com/1240131202713621 （Who can see my saved posts?）
- https://stashr.me/blog/export-instagram-data
- https://allmysaves.com/learn/export-your-saved-posts-from-instagram

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。

---

## 5. X（旧Twitter）ブックマーク

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：ブックマーク（Bookmarks）、ブックマークフォルダ（Bookmark Folders）
- 運営者：X Corp.（米国）
- 提供状況：継続。

### 2. 対象ユーザー・対応OS
- iOS、Android、Web（公式ヘルプの手順にモバイル・Web双方あり。検索結果要約で確認）。

### 3. 日本語UI
- 未確認（日本語ヘルプの直接確認は予算切れで未実施。推測：提供あり）。

### 4. 共有入口
- X 内の投稿のブックマークアイコンのみ。外部コンテンツの保存は非該当。

### 5. URL対応 / 画像対応
- X の投稿のみ。

### 6. OCR
- 未確認（記載なし）。

### 7. 自動分類・AIタグ付け・要約
- 未確認（記載なし）。

### 8. 検索
- ブックマーク内検索の有無：未確認（検索予算切れ）。

### 9. 再提示
- 未確認（リマインダー・通知の記載なし）。ブックマークは常に非公開（公式ヘルプの検索結果要約で確認）。

### 10. 週次まとめ
- 未確認（記載なし）。

### 11. 完了・保留・不要の扱い
- ブックマーク解除、フォルダからの削除（フォルダから外してもアカウントからは消えない。公式ヘルプの検索結果要約で確認）。

### 12. 無料枠
- 無料アカウント：ブックマーク保存可、「All Bookmarks」の単一ビュー。フォルダ作成は有料（help.x.com About Bookmarks／About X Premium の検索結果要約、および第三者解説 contextbolt で確認）。
- Premium：「無制限のブックマークとブックマークフォルダ」（公式ヘルプの検索結果要約で確認）。無料アカウントのブックマーク件数上限は未確認。
- フォルダは最安ティア Basic に含まれる（help.x.com/en/using-x/x-premium を引用する第三者解説の検索結果要約で確認。公式本文は未取得）。

### 13. 価格（確認日 2026-10-02）
- 日本（JPY、Web購入、第三者比較記事 2026年版の検索結果要約。**公式ページ本文は未取得**）：
  - Basic：月額 368円／年額 3,916円
  - Premium：月額 980円／年額 10,280円
  - Premium+：月額 6,080円／年額 60,040円
  - iPhone アプリ内購入では Premium が月額 1,380円（Web の 980円より高い。アプリストア手数料差との解説）
- 米国（USD、第三者解説 contextbolt の検索結果要約）：Basic 月額 USD 3 から／年額 USD 32。
- 確認元：https://pro-marketing.jp/sns-marketing/x-premium-plan-comparison/ 、https://web-k-creation.com/information/information/1667/ 、https://contextbolt.com/blog/x-bookmark-folders/ （いずれも検索結果要約のみ。公式 help.x.com は取得失敗）。
- 注意：価格は購入経路（Web／iOS／Android）と時期で変動するため、公式の料金ページで再確認が必要。

### 14. アカウント要否
- X アカウント必須。

### 15. 外部AI利用
- 未確認（Grok 連携は Premium 特典として言及されるが、ブックマークとの関係は未確認）。

### 16. データ削除・書き出し
- 未確認（X のデータアーカイブにブックマークが含まれるかは確認できず）。

### 17. レビューの不満
- xantenna.net「Xのブックマーク整理術｜貯まる一方で見返せない人のための管理方法」（https://xantenna.net/blog/x-bookmark-organization 、投稿日未確認）：保存はワンタップだが探すときは時系列スクロールのみ、整理機能が限定的、X 以外で見つけたものと保存場所が分断される、と指摘（検索結果要約で確認。※ツール提供側のブログの可能性あり）。
- Bulkmark Blog「Why Your Twitter/X Bookmarks Pile Up」（https://bulkmark.io/blog/why-twitter-bookmarks-pile-up 、投稿日未確認）：「未読コンテンツの墓場」になる、と記述（検索結果要約で確認。※競合ツールのブログ）。

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約のみ）
- https://help.x.com/en/using-x/bookmarks
- https://help.x.com/en/using-x/x-premium
- https://help.x.com/en/using-x/x-premium-how-to
- https://contextbolt.com/blog/x-bookmark-folders/
- https://pro-marketing.jp/sns-marketing/x-premium-plan-comparison/
- https://web-k-creation.com/information/information/1667/

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。

---

## 6. YouTube「後で見る」

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：後で見る（Watch Later）
- 運営者：Google LLC（米国）
- 提供状況：継続。

### 2. 対象ユーザー・対応OS
- iOS、Android、Web（公式ヘルプにプラットフォーム別ページあり。検索結果要約で確認）。

### 3. 日本語UI
- 日本語ヘルプあり（検索結果に日本語版ヘルプ URL がヒット。本文未取得）。

### 4. 共有入口
- YouTube 内の動画・ショートの「保存」→「後で見る」、サムネイルの「後で見る」ボタン（公式ヘルプ 56101 の検索結果要約で確認）。外部コンテンツは非該当。

### 5. URL対応 / 画像対応
- YouTube 動画のみ。

### 6. OCR
- 非該当。

### 7. 自動分類・AIタグ付け・要約
- 未確認（記載なし）。

### 8. 検索
- 未確認（再生リスト内検索の有無を確認できず）。

### 9. 再提示
- 未確認（リマインダー・通知の記載なし）。

### 10. 週次まとめ
- 未確認（記載なし）。

### 11. 完了・保留・不要の扱い
- 「後で見る」から削除（公式ヘルプの検索結果要約で確認）。視聴済み動画の一括削除：第三者記事に言及あり（公式未確認）。

### 12. 無料枠・上限
- 再生リストに表示できる動画は最大 5,000 本（公式ヘルプ「再生リストの作成と管理」57792 の検索結果要約で確認）。「後で見る」もこの上限に達すると追加できなくなる旨は第三者記事（wiz.ooo、X 投稿）で言及（公式ヘルプに「後で見る」固有の上限明記があるかは未確認）。

### 13. 価格
- 無料。確認日 2026-10-02。確認元：YouTube ヘルプ（検索結果要約）。

### 14. アカウント要否
- Google アカウント必須。

### 15. 外部AI利用
- 未確認。

### 16. データ削除・書き出し
- 未確認（Google データエクスポートに再生リストが含まれるかは現行ページで未確認）。

### 17. レビューの不満
- X 投稿（@kmitc26、投稿日未確認）「YouTube『後で見る』が上限5000本で追加できなくなった。収集癖あるから一括削除は抵抗あるし、1つずつ整理は面倒」（https://x.com/kmitc26/status/2024364003846455658 、検索結果要約で確認）。
- wiz.ooo「『後で見る』に追加した動画がなくなった？追加できるのは5000本まで」（https://wiz.ooo/life/10459 、投稿日未確認）。

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約のみ）
- https://support.google.com/youtube/answer/56101 （後で見るに動画を追加・削除）
- https://support.google.com/youtube/answer/57792 （再生リストの作成と管理）
- https://support.google.com/youtube/answer/9209643 （You タブ）
- https://wiz.ooo/life/10459
- https://x.com/kmitc26/status/2024364003846455658

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。

---

## 7. TikTok「お気に入り（セーブ）」

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：お気に入り（Favorites）／セーブ、コレクション
- 運営者：TikTok Pte. Ltd.／ByteDance（シンガポール・中国系。日本法人あり）
- 提供状況：継続。

### 2. 対象ユーザー・対応OS
- iOS、Android（Web 版での利用可否は未確認）。

### 3. 日本語UI
- 日本語ヘルプあり（support.tiktok.com/ja/ のページがヒット。本文未取得）。

### 4. 共有入口
- TikTok 内の投稿のブックマーク（セーブ）アイコン。映画・TV番組・書籍のリンクからも「お気に入りに追加」可（公式ヘルプ "your-favorite-movies-and-tv-shows" "your-favorite-books" の検索結果要約で確認）。外部コンテンツは非該当。

### 5. URL対応 / 画像対応
- TikTok 投稿のみ。

### 6. OCR
- 非該当・未確認。

### 7. 自動分類・AIタグ付け・要約
- 未確認。

### 8. 検索
- 未確認。

### 9. 再提示
- 未確認（リマインダー・通知の記載なし）。

### 10. 週次まとめ
- 未確認。

### 11. 完了・保留・不要の扱い
- セーブ解除・コレクションからの移動（第三者解説の検索結果要約で確認。公式ページは未取得）。

### 12. 無料枠・制限
- 無料。コレクション作成：セーブボタン長押し→「新規」→名前を付けて保存（第三者解説 stasht.app／MakeUseOf の検索結果要約で確認。**動画お気に入り・コレクションに関する公式ヘルプ本文は未取得**）。件数上限：未確認。

### 13. 価格
- 無料。確認日 2026-10-02。確認元：TikTok サポート（検索結果要約）。

### 14. アカウント要否
- TikTok アカウント必須。

### 15. 外部AI利用
- 未確認。

### 16. データ削除・書き出し
- 未確認（TikTok の「データをダウンロード」にお気に入りが含まれるかは現行ページで確認できず）。

### 17. レビューの不満
- 未取得。

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約のみ）
- https://support.tiktok.com/en/using-tiktok/exploring-videos/your-favorite-movies-and-tv-shows
- https://support.tiktok.com/en/using-tiktok/exploring-videos/your-favorite-books?lang=en
- https://support.tiktok.com/ja/using-tiktok/exploring-videos/your-favorite-movies-and-tv-shows
- https://www.makeuseof.com/how-to-find-and-manage-tiktok-favorites/
- https://stasht.app/blog/how-to-organize-saved-tiktoks

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。動画のお気に入り／コレクションの公式ヘルプ URL は特定できなかった（推測した URL は取得失敗）。

---

## 8. Pinterest

### 1. 名称 / 運営者 / 国 / 提供状況
- 名称：Pinterest（ピン、ボード、シークレットボード、Save Extension）
- 運営者：Pinterest, Inc.（米国）
- 提供状況：継続。

### 2. 対象ユーザー・対応OS
- iOS（App Store：iOS 16.0 以降）、Android、Web、ブラウザ拡張（Pinterest 保存ボタン）。検索結果要約で確認。

### 3. 日本語UI
- App Store 日本掲載ページに日本語対応の記載（検索結果要約で確認）。日本語ヘルプの有無は未確認（推測：あり）。

### 4. 共有入口
- iOS共有シート：Web ページで共有アイコン → Pinterest アイコン、または一覧の「Save to Pinterest」をタップ → 保存する画像を1枚以上選択 → 必要なら編集アイコンで事前選択されたボードを変更 → 保存（公式ヘルプ "Add the Pinterest Save Extension" の検索結果要約で確認）。
- ブラウザ拡張：Pinterest ブラウザボタン（公式ヘルプあり）。
- 「写真から Pin を作成」（Create a Pin from an image or video）ヘルプあり（本文未取得）。
- テキスト・ファイル・メール転送：未確認。

### 5. URL対応 / 画像対応
- Web ページ上の画像を Pin として保存（URL はリンク先として付随）。端末内の写真からの Pin 作成ヘルプあり（本文未取得）。

### 6. OCR
- 未確認（記載なし）。

### 7. 自動分類・AIタグ付け・要約
- 未確認。ボードは手動作成（公式ヘルプ "Create a board"）。ホームフィードはボードや行動に基づく推薦（検索結果要約で確認）。

### 8. 検索
- Pinterest 全体検索はあり。自分の保存 Pin 内に限定した検索の有無：未確認。

### 9. 再提示
- 自分が保存した Pin の再提示（リマインダー等）：未確認。
- 通知設定（プッシュ／メール／アプリ内）を種類ごとにオン／オフ可（公式ヘルプ "Edit notification settings" の検索結果要約で確認）。
- 推測：ボードに基づく「おすすめ」通知は、新しい Pin の推薦であり、保存済み Pin を再提示するものではないと思われる（公式本文未取得のため未確認）。

### 10. 週次まとめ
- 未確認（メール通知カテゴリの内訳を確認できず）。

### 11. 完了・保留・不要の扱い
- Pin の削除、ボードの整理・アーカイブ（"Manage your boards" ヘルプあり、本文未取得）。

### 12. 無料枠
- 無料（件数上限：未確認）。

### 13. 価格
- 無料。App Store（日本）：無料、評価 4.8（約536万件）、サイズ 241.5MB（検索結果要約で確認、確認日 2026-10-02、確認元 https://apps.apple.com/jp/app/pinterest/id429047995 ）。

### 14. アカウント要否
- Pinterest アカウント必須。

### 15. 外部AI利用
- 未確認（「GenAI interests」設定が推薦の調整項目として存在。検索結果要約で確認）。

### 16. データ削除・書き出し
- 設定 →「プライバシーとデータ」→「データをリクエスト」で個人データのダウンロードを申請でき、最大48時間以内に SendSafely 経由のメールでリンクが届く（公式ヘルプ "Download your Pinterest data" の検索結果要約で確認）。形式の詳細：未確認。

### 17. レビューの不満
- 未取得（App Store レビューは取得失敗）。

### 18. 出典URL一覧（確認日 2026-10-02、検索結果要約のみ）
- https://help.pinterest.com/en/article/save-pins-with-the-pinterest-browser-button
- https://help.pinterest.com/en/article/add-pins-from-the-web
- https://help.pinterest.com/en/article/create-a-board
- https://help.pinterest.com/en/article/secret-boards
- https://help.pinterest.com/en/article/edit-notification-settings
- https://help.pinterest.com/en/article/tune-your-home-feed
- https://help.pinterest.com/en/article/download-your-pinterest-data
- https://apps.apple.com/jp/app/pinterest/id429047995

### 19. 確認方法
- 検索結果要約のみ（公式ページ本文は未取得、実機未試用）。

---

## 無料手段に共通する「保存したものを忘れる・見返さない」不満の例

需要規模や全ユーザーの意見とは断定しない。いずれも検索結果要約で確認（本文未取得）。ツール事業者のブログは利害関係がある点に注意。

1. **Instagram**：note「保存した投稿、どこ行ったか分からなくなってた。Instagramのコレクションで仕分けた」
   - URL：https://note.com/genial_rose6801/n/nb78396bfac2c （投稿日未確認）
   - 要旨：とりあえず保存ボタンを押し、あとで見返そうと思ったまま忘れ、保存が一箇所に積み上がる体験談。
2. **Instagram**：知る見る！図鑑「【これで完璧】インスタの保存済投稿などの整理テクをわかりやすく解説！」
   - URL：https://brains.hatenablog.com/entry/2025/05/16/000020 （2025-05-16）
   - 要旨：「あとで見返そうと思ったままずっと忘れてしまい、保存した投稿がどんどん積み上がる」問題を前提に整理法を解説。
3. **X ブックマーク**：xantenna.net「Xのブックマーク整理術｜貯まる一方で見返せない人のための管理方法」
   - URL：https://xantenna.net/blog/x-bookmark-organization （投稿日未確認）
   - 要旨：保存はワンタップなのに探す時は時系列スクロールのみ、整理機能が限定的、他サービスで見つけたものと保存場所が分断される。
4. **X ブックマーク／Read-later 全般**：Bulkmark Blog「Why Your Twitter/X Bookmarks Pile Up (And What to Actually Do About It)」
   - URL：https://bulkmark.io/blog/why-twitter-bookmarks-pile-up （投稿日未確認、競合ツール事業者）
   - 要旨：ブックマークは「未読コンテンツの墓場」になる。保存は報酬だが読む作業が伴わない、と主張。Pocket 等の研究で保存物に戻る率が平均5％未満とも記述（一次資料は未確認）。
5. **YouTube 後で見る**：X 投稿（@kmitc26）
   - URL：https://x.com/kmitc26/status/2024364003846455658 （投稿日未確認）
   - 要旨：「後で見る」が上限5,000本で追加できなくなった。収集癖があり一括削除に抵抗、一つずつ整理は面倒。
6. （補足・行動の裏付け）narumi.blog.jp「スマホの『スクショ』こそ最高のブックマークだったりする」
   - URL：https://narumi.blog.jp/archives/74685389.html （投稿日未確認）
   - 要旨：SNS で見かけた気になる情報をスクショで溜めて後で見返す、という保存行動の記述（不満ではなく、ATO が想定する「スクショ＝保存」行動の例）。
7. （補足）Fernandina Observer「Apple's Visual Intelligence is clever. But it can't remember.」
   - URL：https://www.fernandinaobserver.org/stories/apples-visual-intelligence-is-clever-but-it-cant-remember,99018 （投稿日未確認、タイトルのみ確認・本文未取得）

---

## 取得失敗URL一覧（ネットワーク制限 EGRESS_BLOCKED、確認日 2026-10-02）

- https://support.apple.com/guide/iphone/use-visual-intelligence-iph2ebdb6ae7/ios
- https://www.apple.com/jp/ios/ios-26/
- https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/
- https://support.google.com/pixelphone/answer/15312581?hl=en
- https://store.google.com/intl/en/ideas/articles/pixel-screenshots/
- https://blog.google/products/pixel/google-pixel-screenshots-tips/
- https://play.google.com/store/apps/details?id=com.google.android.apps.pixel.agent&hl=en_US
- https://notice.line.me/line/ios/document/notice?documentId=100000302&lang=ja
- https://www.itmedia.co.jp/news/articles/2405/10/news156.html
- https://chiilabo.com/2024-05/line-keep-discontinue/
- https://help.instagram.com/3129045784070725
- https://about.instagram.com/blog/announcements/introducing-new-ways-to-organize-your-saved-posts
- https://help.x.com/en/using-x/bookmarks
- https://help.x.com/en/using-x/x-premium
- https://contextbolt.com/blog/x-bookmark-folders/
- https://support.google.com/youtube/answer/9059342?hl=ja
- https://support.tiktok.com/en/using-tiktok/exploring-videos/favorites （URL 自体の存在も未確認）
- https://help.pinterest.com/en/article/add-pins-from-the-web
- https://newsroom.pinterest.com/en/post/new-pinterest-shortcuts-for-ios-11
- https://9to5mac.com/2026/01/11/ios-26-new-screenshot-apple-intelligence-favorite-feature/
- https://www.androidpolice.com/google-pixel-screenshots-guide/
- https://help.line.me/line/smartphone/pc?lang=ja&contentId=20017696
- https://note.com/genial_rose6801/n/nb78396bfac2c
- https://xantenna.net/blog/x-bookmark-organization
- https://wiz.ooo/life/10459

## 未実施の補足検索（WebSearch 予算上限により実行不可）

- TikTok 動画のお気に入り／コレクションの公式ヘルプ本文
- Pinterest の通知内容（保存済み Pin の再提示の有無）
- X ブックマーク内検索の有無、公式料金ページ（JPY）
- YouTube 日本語ヘルプでの「後で見る」上限明記
- iOS 写真アプリでのスクショ内文字検索（Live Text による写真検索）の現行公式記述
- Visual Intelligence（画面内容）の日本語対応の公式明記
- Keepメモ の iOS 共有シートからの保存可否
- 各サービスの App Store／Play Store／公式コミュニティでのレビュー不満
