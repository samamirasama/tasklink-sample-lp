# ATO（共有シート→永続保存→本体アプリで解析・再提示）技術実現性調査

- 確認日: 2026-10-02
- 調査方法と制約:
  - developer.apple.com はページ取得（WebFetch / 公式ドキュメントJSON）で確認できた。以下「ページ取得で確認」と表記。
  - support.apple.com、www.apple.com（Newsroom）はネットワーク制限（EGRESS_BLOCKED, 403）で取得失敗。該当項目は「取得失敗（ネットワーク制限）」または「検索結果要約で確認（ページ本文は未取得）」と表記。
  - セッションの WebSearch 回数上限に達したため、途中から検索は実施不可。未調査項目は「未確認（検索上限のため未調査）」と表記。
  - 学習知識由来の数値は「未確認（学習知識では〜）」と明記。

---

## 1. Share Extension（共有拡張）

### 1-1. 受け取れるデータ種別と NSExtensionActivationRule
- 公式リファレンス `NSExtensionActivationRule`（iOS 8.0+）: 「Share または Action 拡張がサポートするセマンティックなデータ型」。子キーとして以下が存在する（ページ取得で確認）。
  - Web Content: `NSExtensionActivationSupportsWebURLWithMaxCount`（「拡張がサポートするHTTP URLの最大数」）、`NSExtensionActivationSupportsWebPageWithMaxCount`
  - Files: `NSExtensionActivationSupportsFileWithMaxCount`（「あらゆる種類のファイルの最大数」）、`NSExtensionActivationSupportsImageWithMaxCount`（「画像ファイルの最大数」）、`NSExtensionActivationSupportsMovieWithMaxCount`
  - Text: `NSExtensionActivationSupportsText`（「テキストをサポートするか」のBool）
  - Attachments: `NSExtensionActivationSupportsAttachmentsWithMinCount` / `MaxCount`
  - Configuration: `NSExtensionActivationUsesStrictMatching`, `NSExtensionActivationDictionaryVersion`
- 結論: URL・画像・テキスト・ファイルはいずれも宣言可能。ATOでは WebURL（例: MaxCount 1）、Image（複数可）、Text、File を併記し、必要に応じて `NSPredicate` 文字列（`SUBQUERY(...)` 形式）で細かく制御する（Predicate形式の詳細は公式ガイドの Info.plist Key Reference 参照、本調査では本文未取得）。
- 出典: https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/nsextensionactivationrule （ページ取得で確認、2026-10-02）

### 1-2. 実行時間・メモリ制約（公式記述）
- App Extension Programming Guide（アーカイブ、ページ取得で確認）:
  - 「Memory limits for running app extensions are significantly lower than the memory limits imposed on a foreground app. On both platforms, the system may aggressively terminate extensions because users want to return to their main goal in the host app.」
  - 「Design your app extension to launch quickly, aiming for well under one second. An extension that launches too slowly is terminated by the system.」
  - 「Your app extension doesn't own the main run loop ... if your extension blocks the main run loop, it can create a bad user experience」
- 具体的なメモリ上限値（MB）は公式ドキュメントに記載なし（確認できず）。
  - Apple Developer Forums（thread/115259、ページ取得で確認）では Action 拡張のクラッシュログに `EXC_RESOURCE RESOURCE_TYPE_MEMORY (limit=120 MB)` が出る事例が報告され、Apple スタッフは「アプリと拡張はメモリ使用量についてサンドボックス化されることが多い」と回答しているが、「120MB」という数値そのものを公式仕様として明言はしていない。
  - 検索結果要約（ページ本文未取得）では Share 拡張の上限として 120MB がコミュニティで広く報告されている（Igor Kulman ブログ、element-ios issue 等）。シミュレータでは上限が無効。
  - 結論: 「未確認（学習知識および開発者コミュニティでは Share/Action 拡張は約120MB、実機依存）」。
- 実行時間の数値制限（秒）は公式記述なし。拡張は `completeRequest(returningItems:)` 呼び出しで終了するため、長時間処理は不可とみなすべき。
- 出典: https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionCreation.html （ページ取得で確認、2026-10-02）／ https://developer.apple.com/forums/thread/115259 （ページ取得で確認、2026-10-02）

### 1-3. 本体アプリとのデータ共有（App Groups / 共有コンテナ）
- 「Configuring app groups」（ページ取得で確認）: 「You can also use an app group to share data between an app extension or App Clip and its host app.」共有手段として (a) `UserDefaults(suiteName:)`、(b) `FileManager.containerURL(forSecurityApplicationGroupIdentifier:)` で共有コンテナのパス取得、(c) バックグラウンド URLSession の `sharedContainerIdentifier` を列挙。App Group は Keychain Access Group としても利用可能。各開発者アカウントで最大 1,000 の App Group を登録可能。
- App Extension Programming Guide（ページ取得で確認）: 「the running app extension and containing app have no direct access to each other's containers」「To avoid data corruption, you must synchronize data accesses. Use Core Data, SQLite, or Posix locks」
- 結論: ATOは App Group 共有コンテナに、受け取った URL/画像/テキストをファイル＋メタデータ（SQLite/Core Data/SwiftData もしくは JSON）として即保存し、拡張は保存だけして終了する設計が公式に沿う。
- 出典: https://developer.apple.com/documentation/xcode/configuring-app-groups （ページ取得で確認、2026-10-02）／ https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html （ページ取得で確認、2026-10-02）

### 1-4. 拡張から本体アプリを起動できるか
- `NSExtensionContext.open(_:completionHandler:)` 公式リファレンス（ページ取得で確認）: 「Each extension point determines whether to support this method ... In iOS, the Today and iMessage app extension points support this method. An iMessage app extension can use this method only to open its parent app」。Share 拡張は対象外。
- Apple Developer Forums thread/773342（ページ取得で確認）: Apple Frameworks Engineer の回答「There's no supported way for you to launch your app directly from App Extensions, except Today and Widgets (which requires OpenURLIntent and is available to processes that can use App Intents)」。レスポンダチェーンをたどる等の裏技は非サポートで審査リスクあり。
- 結論: Share 拡張から本体アプリを直接起動する公式手段はない。ATOは「拡張は保存のみ→ユーザーが後で本体を開く」か、ローカル通知（UNUserNotificationCenter は拡張からも使用可。ただし未確認：通知権限は本体で取得済みであること）で誘導する設計にする。
- 出典: https://developer.apple.com/documentation/foundation/nsextensioncontext/open(_:completionhandler:) （ページ取得で確認、2026-10-02）／ https://developer.apple.com/forums/thread/773342 （ページ取得で確認、2026-10-02）

---

## 2. 拡張終了後に本体アプリが処理を続ける手段

### 2-1. BGTaskScheduler（BGAppRefreshTask / BGProcessingTask）
- 「Choosing Background Strategies for Your App」（ページ取得で確認）:
  - 「Schedule these types of background tasks using BGProcessingTaskRequest, and the system decides the best time to launch your background task.」
  - BGAppRefreshTask: 「The system decides the best time to launch your background task, and provides your app up to 30 seconds of background runtime.」
- `BGProcessingTask` リファレンス（ページ取得で確認）: 「Although processing tasks can run for minutes, the system can interrupt the process.」「Processing tasks run only when the device is idle. The system terminates any background processing tasks running when the user starts using the device.」
- 「Starting and Terminating Tasks During Development」（ページ取得で確認）: 「The delay between the time you schedule a background task and when the system launches your app to run the task can be many hours.」
- 結論: 即時・確実な実行は公式に保証されない（「システムが最適な時刻を決める」「数時間遅れうる」「端末アイドル時のみ」）。ATOでの「共有直後の自動解析」には使えず、あくまで「次回起動までに余力があれば先行処理」の位置づけ。
- 出典: https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app ／ https://developer.apple.com/documentation/backgroundtasks/bgprocessingtask ／ https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtask ／ https://developer.apple.com/documentation/backgroundtasks/starting-and-terminating-tasks-during-development （すべてページ取得で確認、2026-10-02）

### 2-2. URLSession バックグラウンド転送
- `URLSessionConfiguration.background(withIdentifier:)`（ページ取得で確認）: 「In iOS, this configuration makes it possible for transfers to continue even when the app itself is suspended or terminated.」「If the user terminates the app from the multitasking screen, the system cancels all of the session's background transfers.」
- `isDiscretionary`（ページ取得で確認）: 「For transfers started while your app is in the background, the system always starts transfers at its discretion」
- `sharedContainerIdentifier`（ページ取得で確認）: 「To create a URL session for use by an app extension, set this property to a valid identifier for a container shared between the app extension and its containing app.」「If you try to create a URL session from your app extension but fail to set this property to a valid value, the URL session is invalidated upon creation.」
- App Extension Programming Guide: 「only one process can use a background session at a time, you need to create a different background session for the containing app and each of its app extensions.」
- 結論: 拡張から外部API（例: 解析サーバ）へアップロードを投げる手段としては成立する。ただし「転送」専用で、端末内解析の継続には使えない。
- 出典: https://developer.apple.com/documentation/foundation/urlsessionconfiguration/background(withidentifier:) ／ .../isdiscretionary ／ .../sharedcontaineridentifier （ページ取得で確認、2026-10-02）／ ExtensibilityPG/ExtensionScenarios.html（同上）

### 2-3. BGContinuedProcessingTask（iOS 26）— 存在を公式資料で確認
- `BGContinuedProcessingTask` リファレンス（ページ取得で確認）: iOS 26.0 / iPadOS 26.0 / Mac Catalyst 26.0。「A task that starts in the foreground and can continue running in the background as needed.」「The system displays the progress of this task in a Live Activity and a person can cancel it」「The system can terminate a continuous background task abruptly depending on run-time conditions」
- `BGContinuedProcessingTaskRequest`（ページ取得で確認）: 「The app submits this request from the foreground. Submission needs to occur as a result of a person's action, such as tapping a button.」
- 「Performing long-running tasks on iOS and iPadOS」（ページ取得で確認）: バックグラウンドでも GPU（対応機種、`com.apple.developer.background-tasks.continued-processing.gpu` 相当の Background GPU Access capability 必須）、ネットワーク、Core Image / Vision / Accelerate 等の CPU 集約処理が可能。「The system cancels any running tasks if a person closes the app in the app switcher」。
- WWDC25 Session 227「Finish tasks in the background」（ページ取得で確認）: 「Continue processing tasks always start with an explicit action that someone performs in your app, like a button tap or gesture.」「Avoid automatic workloads like maintenance, backups, or photo syncing.」
- Forums thread/804919（ページ取得で確認）: Apple DTS Engineer「We can't guarantee any specific time, but there isn't any artificial throttle on timing and, theoretically, a task could run for an hour+ under the right circumstances.」
- 重要な含意: BGContinuedProcessingTask は本体アプリのフォアグラウンドでユーザー操作により開始する必要があるため、Share 拡張からは開始できない（拡張は別プロセス）。ATOでは「本体を開いて『解析開始』を押す→バックグラウンドに回っても継続」という用途に適する。
- 出典: https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask ／ https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest ／ https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados ／ https://developer.apple.com/videos/play/wwdc2025/227/ ／ https://developer.apple.com/forums/thread/804919 （すべてページ取得で確認、2026-10-02）

---

## 3. 共有シートで受け取る URL の実態（Instagram / X / YouTube / TikTok / Safari）
- 公式資料: 各サードパーティアプリが共有シートに何を載せるかを定めた Apple 公式資料は存在しない（アプリ側の `UIActivityViewController` / `NSItemProvider` 実装次第）。
- 一次情報（ページ取得で確認）: Apple Developer Forums thread/702127 — Safari からの共有では `public.url` が主で、`public.plain-text` にフォールバックするコードが一般的。`loadItem` の戻りが `URL` ではなく `Data`（UTF-8のURL文字列）で来る場合があり、両方に対応する必要がある。Apple スタッフ回答なし。
- 検索結果要約（ページ本文未取得）: Safari の画像共有を受けるには `public.url` の宣言が必要で、その結果通常のWebページ共有時にも拡張が表示される（thread/719804）。
- 以下は本調査で一次情報を確認できず「推測（学習知識・一般的な開発者報告）」:
  - Instagram: 投稿/リールの共有は `public.url`（instagram.com のリンク）のみ。画像バイナリは渡らない。ログイン必須ページのため OGP 取得が制限されることが多い。
  - X: `public.url`（x.com / twitter.com のステータスURL）＋ `public.plain-text`（ツイート本文を含むことがある）。
  - YouTube: `public.url`（youtu.be 短縮URL）＋タイトルの `public.plain-text` が付くことがある。
  - TikTok: `public.url`（vm.tiktok.com 等の短縮URL）または `public.plain-text` に URL 文字列が入るケースの報告がある（型が揃わない）。
  - Safari: `public.url`（ページURL）＋ ページタイトルは `NSExtensionItem.attributedContentText` や `public.plain-text` に入る場合がある。「Webページ（WebPage）」型を使うと JavaScript プリプロセッサで DOM 情報を取得可能。
  - 結論: 「未確認（検索上限のため未調査）」。実機で各アプリの `registeredTypeIdentifiers` をログ出力して確定する必要がある（末尾リスト参照）。
- 出典: https://developer.apple.com/forums/thread/702127 （ページ取得で確認、2026-10-02）／ https://developer.apple.com/forums/thread/719804 （検索結果要約で確認、ページ本文は未取得、2026-10-02）

---

## 4. LinkPresentation（LPMetadataProvider）
- 公式リファレンス（ページ取得で確認）: iOS 13.0+。「Use LPMetadataProvider to fetch metadata for a URL, including its title, icon, and image or video links. All properties on the resulting LPLinkMetadata instance are optional.」「If your user doesn't have a network connection, the fetch can fail. If the server doesn't respond or is too slow, the fetch can time out.」
  - `timeout`: 既定 30 秒。超過時は `LPError.metadataFetchTimedOut`。
  - `shouldFetchSubresources`: 既定 true（icon/image/video をダウンロード）。false にするとメイン資源のメタデータのみ。
  - `startFetchingMetadata(for:completionHandler:)`: インスタンスごとに1回のみ。「The completion handler executes on a background queue.」「When the completion handler returns, it deletes any file URLs returned in the resulting LPLinkMetadata.」（画像は即座に自前でコピー/保持する必要がある）
  - macOS では `com.apple.security.network.client` エンタイトルメントが必要（iOS 拡張では不要）。
- ログイン必須ページでの制約: 公式に明記はない。LPMetadataProvider は内部で WebKit を用いて取得するため、認証 Cookie を持たない匿名アクセス相当になり、ログイン壁のあるページ（Instagram 等）はタイトルやOGPが取れない/ログインページのメタデータになる可能性が高い（推測、公式記述なし）。
- 拡張内で使えるか: 公式に禁止記述なし。Forums thread/765628（ページ取得で確認）では、通常アプリでも WebKit 関連エンタイトルメント不足のログやプロセス終了エラーが出る事象が Apple に FB15430726 として報告され「調査中」。検索結果要約では LinkPresentation をメインスレッド外から使うとクラッシュした報告がある。拡張内では WebKit プロセス起動＋メモリ上限（1-2）の影響が懸念されるため、ATOでは「拡張内では URL と最低限のテキストだけ保存し、メタデータ取得は本体アプリ側で行う」設計が安全。
- 出典: https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider （および /timeout, /shouldfetchsubresources, /startfetchingmetadata(for:completionhandler:)）（ページ取得で確認、2026-10-02）／ https://developer.apple.com/forums/thread/765628 （ページ取得で確認、2026-10-02）

---

## 5. 端末内 OCR（Vision: RecognizeTextRequest / VNRecognizeTextRequest）
- Vision フレームワーク概要（ページ取得で確認）: 「Recognizing text in 26 languages across everyday objects, documents, and photos」。「Starting in iOS 18.0, the Vision framework provides a new Swift-only API」（`RecognizeTextRequest`。旧 `VNRecognizeTextRequest` はレガシーAPIとして併存）。
- `RecognizeTextRequest`（ページ取得で確認）: iOS 18.0+。「To specify or limit the languages to find in the request, set recognitionLanguages」。設定項目: `automaticallyDetectsLanguage`, `usesLanguageCorrection`, `supportedRecognitionLanguages`, `customWords`, `recognitionLevel`（.fast / .accurate）。`supportedRecognitionLanguages` は「The identifiers of the languages that the request supports」で、実行時に実機で問い合わせる形。
- 日本語対応: 公式ページに言語一覧の明記なし（「26言語」とのみ）。日本語の明示的な記載は本調査で確認できず。「未確認（学習知識では iOS 16 以降 `ja-JP` が VNRecognizeTextRequest の対応言語に含まれ、検索結果要約でも『iOS 16 から日本語OCRが可能』と報告）」。Forums thread/692193（2021年）は Apple スタッフ回答なし。
- オフライン動作: Vision は端末内で推論する設計（プロトコル `DownloadableAssetsRequest` が存在する要求種別のみ追加アセットのダウンロードが必要）。RecognizeTextRequest がダウンロード必須か否かは公式ページで明記されていない → 「未確認（学習知識では OCR モデルは OS 同梱でオフライン動作）」。
- 補足: Vision には Foundation Models 連携用の `OCRTool` / `BarcodeReaderTool` が追加されている（ページ取得で確認）。LLM のツール呼び出しで OCR を組み込める。
- 出典: https://developer.apple.com/documentation/vision ／ https://developer.apple.com/documentation/vision/recognizetextrequest ／ .../supportedrecognitionlanguages ／ .../recognitionlanguages （ページ取得で確認、2026-10-02）／ https://developer.apple.com/forums/thread/692193 （ページ取得で確認、2026-10-02）

---

## 6. Apple Intelligence「Foundation Models framework」（iOS 26）
- 公式フレームワークページ（ページ取得で確認）: iOS 26.0 / iPadOS 26.0 / macOS 26.0 / visionOS 26.0（watchOS は 27.0）。「The Foundation Models framework provides access to any large language model, like the on-device and Private Cloud Compute models designed for Apple Intelligence.」「On-device models excel at ... summarization, entity extraction, text and image understanding, refinement, dialog for games, generating creative content」。
  - `@Generable` による構造化出力（Guided generation）、`Tool` によるツール呼び出し、画像を含むマルチモーダル添付（`Attachment`, `ImageAttachmentContent`）、Dynamic Profile。
  - 「To use Apple Foundation Models, people need a device that supports Apple Intelligence.」
- `SystemLanguageModel`（ページ取得で確認）: 「the on-device text foundation model that powers Apple Intelligence」。可用性は `.availability` で確認し、`UnavailableReason` は `appleIntelligenceNotEnabled` / `deviceNotEligible` / `modelNotReady` の3種。`contextSize`, `supportedLanguages`, `supportsLocale(_:)`, `tokenCount(for:)` を提供。`useCase: .contentTagging` で分類・タグ付け専用アダプタ。
- コンテキスト長（ページ取得で確認、「Managing the context window」）: 「Apple's on-device foundation model has a context window of 4096 tokens per session」「For multibyte languages such as Chinese, Japanese, Korean, and Vietnamese a token typically represents one character.」超過時は `exceededContextWindowSize` エラー。長文は分割要約が推奨。
- タグ付け・分類（ページ取得で確認、「Categorizing and organizing data with content tags」）: 「A content tagging model produces a list of categorizing tags based on the input text」。topics / actions / objects / emotions を抽出。用途例「Help people organize their content for tasks such as email autolabeling」。
- 日本語対応（ページ取得で確認、「Supporting languages and locales」）: 「The on-device system language model is multilingual, which means the same model understands and generates text in any language that Apple Intelligence supports.」具体的な言語一覧は support.apple.com の Apple Intelligence ページを参照する構成だが、同ページは取得失敗（ネットワーク制限）。検索結果要約（Apple Newsroom 2025-09、ページ本文未取得）では Apple Intelligence の対応言語に日本語が含まれる。→「日本語対応: 検索結果要約で確認（学習知識でも iOS 18.4 以降日本語対応）」。注意: ガードレール（安全フィルタ）は対応言語のみに適用。
- 対応機種: 公式ページは support.apple.com にリンクするのみで本調査では取得失敗。「未確認（学習知識では iPhone 15 Pro / 15 Pro Max および iPhone 16 シリーズ以降、M1 以降の iPad / Mac）」。
- 無料か: 端末内モデル（SystemLanguageModel）について課金の記述はなく、API 利用料の概念はない（WWDC25 Session 286 でも費用への言及なし）。developer.apple.com/apple-intelligence/（ページ取得で確認）には「If you're enrolled in the App Store Small Business Program and your app has fewer than 2 million total first-time App Store downloads, you can access the next generation of Apple Foundation Models running on Private Cloud Compute at no cloud API cost.」とあり、サーバ側 PCC モデル（`PrivateCloudComputeLanguageModel`、iOS 27.0+、管理エンタイトルメント要申請）は条件付き無料。→「端末内モデル: 無料（課金記述なし）、PCC: 条件付き無料（iOS 27 以降）」。
- モデル規模: WWDC25 Session 286（ページ取得で確認）「a large language model with 3 billion parameters, each quantized to 2 bits」「optimized for use cases like summarization, extraction, classification」。
- 出典: https://developer.apple.com/documentation/foundationmodels ／ .../systemlanguagemodel ／ .../managing-the-context-window ／ .../supporting-languages-and-locales-with-foundation-models ／ .../categorizing-and-organizing-data-with-content-tags ／ .../privatecloudcomputelanguagemodel ／ https://developer.apple.com/apple-intelligence/ ／ https://developer.apple.com/videos/play/wwdc2025/286/ （すべてページ取得で確認、2026-10-02）／ https://support.apple.com/en-us/121115 （取得失敗（ネットワーク制限））

---

## 7. App Store 審査ガイドライン（プライバシー関連）
- 5.1.1(i) プライバシーポリシー（ページ取得で確認）: App Store Connect とアプリ内にポリシーへのリンク必須。収集データ・方法・用途、第三者（analytics, 広告ネットワーク, サードパーティSDK, 親会社・子会社等）が同等の保護をすること、データ保持/削除方針と同意撤回・削除要求の方法を明記。
- 5.1.1(ii) 同意（ページ取得で確認）: 「Apps that collect user or usage data must secure user consent for the collection, even if such data is considered to be anonymous」「Paid functionality must not be dependent on or require a user to grant access to this data」「provide the customer with an easily accessible and understandable way to withdraw consent」。
- 5.1.1(iii) データ最小化（ページ取得で確認）: 「Where possible, use the out-of-process picker or a share sheet rather than requesting full access to protected resources like Photos or Contacts.」→ ATOの「共有シート経由で受け取る」設計はこの条項に適合的。
- 5.1.1(v) アカウント（ページ取得で確認）: 「If your app doesn't include significant account-based features, let people use it without a login. If your app supports account creation, you must also offer account deletion within the app.」
  - 「Offering account deletion in your app」（ページ取得で確認）: 2022-06-30 以降必須。「only offering to temporarily deactivate or disable an account is insufficient」「This includes user-generated content」「Apps not operating in highly regulated industries should not require people to make a phone call, send an email, or go through other support flows.」「All users should be allowed to delete their accounts, regardless of where they're located.」
  - 含意: ATOがアカウント不要（端末内＋iCloud 同期のみ）なら削除機能要件は発生しない。独自アカウントを作るなら即時削除フローが必須。
- 5.1.2(i) データの使用と共有（ページ取得で確認、原文）: 「Unless otherwise permitted by law, you may not use, transmit, or share someone's personal data without first obtaining their permission. You must provide access to information about how and where the data will be used. You must clearly disclose where personal data will be shared with third parties, including with third-party AI, and obtain explicit permission before doing so.」
  - 含意: ATOが OpenAI/Anthropic 等の外部 AI にユーザーの共有コンテンツ（URL、画像、OCR テキスト）を送る場合、送信先が「サードパーティAI」であることの明示開示＋事前の明示同意が必須。端末内 Foundation Models / Vision のみなら該当しない。
- プライバシーマニフェスト（ページ取得で確認）: `PrivacyInfo.xcprivacy` に「収集するデータ種別」と「Required Reasons API の使用理由」を記載。指定リストのサードパーティSDKは署名付きマニフェスト必須。
- App Privacy（「栄養ラベル」）（ページ取得で確認）: 「You need to identify all of the data you or your third-party partners collect」。「Collect」は「transmitting data off the device in a way that allows you and/or your third-party partners to access it for a period longer than what is necessary to service the transmitted request in real time」。外部AIに送るデータはこれに該当する可能性が高い（リアルタイム処理のみで保持しない場合は要検討）。
- 出典: https://developer.apple.com/app-store/review/guidelines/ ／ https://developer.apple.com/support/offering-account-deletion-in-your-app/ ／ https://developer.apple.com/documentation/bundleresources/privacy-manifest-files ／ https://developer.apple.com/app-store/app-privacy-details/ （すべてページ取得で確認、2026-10-02）

---

## 8. App Store 手数料
- 標準（ページ取得で確認、「Apple Developer Program – What's included」）: 「The commission on the sale of digital goods and services through the App Store is 30% (15% if you're enrolled in the App Store Small Business Program, Video Partner Program, Mini Apps Partner Program, or News Partner Program) and 15% for qualifying subscriptions.」脚注: 「Different commission rates and fees may apply for certain apps distributed in Brazil, the European Union, Japan, the Netherlands, Russia, and South Korea.」
- Small Business Program（ページ取得で確認）: 「Existing developers who made up to 1 million USD in proceeds in the prior calendar year for all their apps, as well as developers new to the App Store, can qualify」「If a participating developer surpasses the 1 million USD threshold in the current calendar year, the standard commission rate will apply to future sales」。関連アカウント（50%超の持分関係）合算。日本語版ページでは「EUで代替規約を採用しているデベロッパと、最初の1年が経過したサブスクリプションに対して、Appleはさらに手数料を10%に引き下げます」。
- サブスクリプション2年目（ページ取得で確認、「Auto-renewable subscriptions」）: 「After a subscriber accumulates one year of paid service, your net revenue increases to 85%」「Free trials and renewal extensions are excluded from days of paid service」「If the subscription is renewed within 60 days, the days of paid service resume」。SBP 参加者は初年度から 85%。
- 日本（スマホソフトウェア競争促進法 / Mobile Software Competition Act, MSCA）— 公式発表あり（ページ取得で確認）:
  - Apple Developer News（2025-12-17）「Changes to iOS in Japan」: iOS 26.2 から、代替アプリマーケットプレイス配信・運営、In-App Purchase 以外での決済処理（代替決済／リンクアウト）が可能。「By March 17, 2026, all current members of the Apple Developer Program will need to agree to the latest update to the Apple Developer Program License Agreement」。
  - 「App distribution in Japan」サポートページ（ページ取得で確認）の料率:
    - App Store 手数料（コミッション）: 21%（デジタル商品・サービスの販売。アプリ内での代替決済利用を含む）／ 10%（Small Business Program・Mini Apps Partner Program・Video Partner Program 参加者の取引、および初年度経過後の自動更新サブスクリプション）
    - Apple 決済処理手数料: 5%（Apple In-App Purchase で処理する場合に別途）→ IAP 利用時の合計は 21%+5%=26%（SBP は 10%+5%=15%）
    - ストアサービス手数料（アプリ外オファー／リンクアウト）: 15%（SBP・初年度経過後サブスクは 10%）。「Only sales made within 7 days of the link tap are subject to this commission.」
    - Core Technology Commission: 5%（代替マーケットプレイス経由配信アプリの有料アプリ・デジタル商品売上に対して）
    - 施行: MSCA は 2025-12-18 全面施行（検索結果要約）、Apple の対応は iOS 26.2（2025-12-17 発表）。
  - 注意: 「何もしなければ従来の 30%/15% が続くのか」は取得したページには明記なし（未確認）。
- 出典: https://developer.apple.com/programs/whats-included/ ／ https://developer.apple.com/jp/programs/whats-included/ ／ https://developer.apple.com/app-store/small-business-program/ ／ https://developer.apple.com/jp/app-store/small-business-program/ ／ https://developer.apple.com/app-store/subscriptions/ ／ https://developer.apple.com/news/?id=074b3wzz ／ https://developer.apple.com/support/app-distribution-in-japan/ （すべてページ取得で確認、2026-10-02）／ https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/ （取得失敗（ネットワーク制限）、検索結果要約のみ）

---

## 9. Apple Developer Program 年会費
- USD: 「The Apple Developer Program is 99 USD per membership year. Prices may vary by region and are listed in local currency during the enrollment process.」（ページ取得で確認）。非営利・教育機関・政府機関は免除申請可。
- JPY: 日本語ページも「年間99米ドルです。価格は地域によって異なる場合があり、登録手続きの際は現地通貨で表示されます」とのみ記載（ページ取得で確認）。円建て額は公式ページに未掲載 →「未確認（学習知識では 14,800 円/年前後。登録画面で要確認）」。
- 出典: https://developer.apple.com/programs/enroll/ ／ https://developer.apple.com/jp/programs/enroll/ （ページ取得で確認、2026-10-02）

---

## 10. iCloud 同期（CloudKit）のコスト
- 開発者負担（ページ取得で確認）: 日本語「What's included」ページ「Apple Developer Programのメンバーは、個々のアプリに対してそれぞれ最大1PBの無料ストレージを利用することができます。」CloudKit ページ「Store private data securely in your users' iCloud accounts for limitless scale as your user base grows, and get up to 1PB of storage for your app's public data.」→ 公開データベースは最大 1PB まで無料、追加課金の記述なし。
- ユーザーの iCloud 容量との関係: CloudKit 公式ページの「Store private data securely in your users' iCloud accounts」および `CKDatabase`「A private database that's accessible only to the user of the current device」「All access to the private and shared databases requires an iCloud account」から、プライベートDBのデータはユーザーの iCloud アカウント側に保存される。「プライベートDBがユーザーの iCloud ストレージ容量（5GB 無料枠等）に計上される」旨の明文は本調査で取得したページには見当たらず →「検索結果要約で確認（NSHipster, fatbobman 等の二次情報では『プライベートDBはユーザーの iCloud 容量を消費、公開DBはアプリ側の割当を消費』）」。
- 公開DBの細かな無料枠（10GB アセット / 100MB DB / 2GB 転送/月 から、アクティブユーザー数に応じて最大 1PB/10TB/200TB/日 まで拡張）は検索結果要約のみで、現行の developer.apple.com ページでは確認できなかった →「未確認（学習知識および二次情報）」。
- 実務上の含意: ATOの保存データ（URL・画像・OCR結果）は CloudKit プライベートDB（または NSPersistentCloudKitContainer / SwiftData+CloudKit）に置けば開発者側のサーバ費用はゼロで、容量はユーザーの iCloud 枠を消費する。ユーザーの iCloud が満杯だと同期が失敗する点は UI で扱う必要がある。
- 出典: https://developer.apple.com/jp/programs/whats-included/ ／ https://developer.apple.com/icloud/cloudkit/ ／ https://developer.apple.com/documentation/cloudkit/ckdatabase （ページ取得で確認、2026-10-02）

---

## 取得失敗（ネットワーク制限）／未調査の一覧
- https://support.apple.com/en-us/121115 （Apple Intelligence 対応機種・言語）— 取得失敗（EGRESS_BLOCKED）
- https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/ — 取得失敗（EGRESS_BLOCKED）
- Share 拡張の公式メモリ上限値（MB）— 公式記載なし
- Instagram / X / YouTube / TikTok の共有ペイロードの一次情報 — 検索上限のため未調査（推測のみ）
- Vision OCR の対応言語一覧（日本語の明記）— 公式ページに一覧なし
- CloudKit 公開DBの段階的無料枠の現行公式表 — 未確認
- Apple Developer Program の円建て年会費 — 公式ページに未掲載

---

## 実機で確かめないと分からない点
1. Share 拡張の実効メモリ上限（機種・OS別）と、画像複数枚を受けたときのクラッシュ閾値（`EXC_RESOURCE RESOURCE_TYPE_MEMORY` の limit 値）。
2. Instagram / X / YouTube / TikTok / Safari / 写真アプリから共有したときの `NSItemProvider.registeredTypeIdentifiers` の実際の組み合わせ（`public.url` / `public.plain-text` / `public.image` / `public.file-url` のどれが、どの順で来るか。URL が `URL` 型で来るか `Data` で来るか）。
3. 各アプリから渡る URL の形式（短縮URL か、トラッキングパラメータ付きか、Universal Link か）と、本体側で正規化・展開できるか。
4. ログイン必須ページ（Instagram、X の一部）に対する `LPMetadataProvider` の戻り値（タイトル・画像が取れるか、ログインページのメタデータになるか、エラーになるか）。
5. `LPMetadataProvider` を Share 拡張内で呼んだときの安定性（WebKit プロセス起動によるメモリ増、メインスレッド要件、タイムアウト30秒が拡張のライフサイクル内に収まるか）。
6. `RecognizeTextRequest.supportedRecognitionLanguages` に `ja` が含まれるか（対象 OS）、日本語縦書き・手書き・SNSスクショでの精度、機内モードでの動作。
7. Foundation Models: 対象端末での `SystemLanguageModel.default.availability` の結果、日本語プロンプト／日本語入力での `supportsLocale(.current)`、コンテキスト 4096 トークンで日本語（1文字≒1トークン）の記事本文がどれだけ入るか、`contentTagging` ユースケースの日本語タグ品質。
8. `BGContinuedProcessingTask` が実際に継続する時間（アイドル／充電中／低電力モード）と Live Activity の見え方、進捗更新頻度による早期終了の有無。
9. `BGProcessingTask` / `BGAppRefreshTask` の実行遅延（実環境で数時間〜翌日になるか）。
10. Share 拡張からのローカル通知（UNUserNotificationCenter）で本体アプリへ誘導できるか、通知権限の取得状態が拡張に反映されるか。
11. App Group 共有コンテナ上で SwiftData / Core Data を拡張と本体が同時に触る場合のロック・整合性（拡張終了直後に本体が開くケース）。
12. CloudKit プライベートDB利用時、ユーザーの iCloud 容量超過時の挙動（`CKError.quotaExceeded`）とユーザー向けメッセージ。
13. 日本ストアフロントで新手数料（21%+5% 等）が自動適用されるのか、従来 30%/15% のままなのか（App Store Connect の契約画面で要確認）。
