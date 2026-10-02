# MVP仕様書（検証用試作品）

- 作成日：2026年10月2日（木）
- 位置づけ：`01_結論と評価.md` 4.4 の「入れる（P0／P1）」を、実装担当が着手できる粒度に落としたもの。**需要検証前の試作品の仕様**であり、公開版の仕様ではない。ヒアリング・代替A・実機検証（`06`）の結果で変更する。
- 対象OS：iOS 26 以降（現行は iOS 27、2026-09-15公開）。端末内LLM（P2）はiOS 27・Apple Intelligence対応機種のみ。
- 守る条件（引継ぎ資料7章）：保存と分析を分ける／共有拡張で長時間処理をしない／ログイン必須ページはURLのまま使える／自動分類の誤りを修正できる／通知は任意／外部AI送信は同意制／APIキーをアプリに置かない／ローカル保存で開始（同期・アカウントは見送り）。

## 1. 作らないもの（明示）
- アカウント、クラウド同期、サーバー。AI分類（外部・端末内とも、P2として条件付き）。時間別の再提示。スクショ自動取り込み。期限の自動設定。通知の既定オン。

## 2. 画面と遷移

| 画面 | 目的 | 主な要素 | 遷移 |
|---|---|---|---|
| S0 共有拡張 | 受け取って保存して閉じる | 「保存しました」表示（1秒以内に自動で閉じる）。入力欄なし | 閉じる→共有元に戻る |
| S1 受信箱 | 未処理の一覧 | 新しい順。各行：サムネイル／タイトル（未取得は「タイトル未取得」）／共有元／保存日。分類フィルタ（行く・買う・やる・未分類）。検索欄 | 行→S2。右上→S3、S4 |
| S2 詳細 | 判断する | 元URLを開く／元画像を見る、メモ、分類の変更、完了・保留・不要、取り消し（直後のスナックバー） | 判断後→S1へ戻る |
| S3 今週の見返し | 少数ずつ判断する | 候補を1件ずつカード表示（上限は設定、既定5件）。各カードに「開く」「完了」「保留」「不要」。残り件数表示。「今日はここまで」 | 終了→S1 |
| S4 設定 | 任意の通知・書き出し・削除 | 週次通知（既定オフ、曜日・時刻）、見返し件数、画像の縮小保存（既定オン）、書き出し（JSON）、読み込み、全削除（2段階確認） | — |
| S5 保留・完了・不要の一覧 | 見返す | タブで切替。各行から「受信箱に戻す」 | — |

**S3の候補の選び方（既定）**：未処理のうち、保留中でないもの（`snoozed_until` が過去または空）を、`last_presented_at` が古い順→`created_at` が古い順に取り出す。提示したら `last_presented_at` を更新し、同じ週に同じ件を2回出さない。

**「不要」の扱い**：削除ではなく `status=dismissed` に変え、S5で30日間は戻せる。30日後の自動削除は設定で選択（既定は自動削除しない。保存上限の検討は試用後）。

## 3. データモデル（引継ぎ資料8章のたたき台を確定）

| 項目 | 型 | 内容・制約 |
|---|---|---|
| id | UUID | 一意 |
| created_at / updated_at | Date | 保存時刻・更新時刻 |
| source_type | enum | url / image / text / file |
| original_url | String? | 共有で受け取ったURL。正規化は行わず原文を残す。短縮URLの展開は本体で任意（取得失敗時は原文のまま） |
| source_app_hint | String? | 共有元の推定（URLのホスト等から。取得できなければ空。推測で埋めない） |
| shared_text | String? | 共有時に付随したテキスト |
| local_asset_ref | String? | 画像・ファイルの保存先ファイル名（共有コンテナ） |
| title | String? | 取得したタイトル。未取得は nil（UIで「タイトル未取得」） |
| title_source | enum? | fetched / user / shared_text |
| user_note | String? | メモ |
| extracted_text | String? | OCR結果（P2）。検索対象 |
| action_type | enum | go / buy / do / none（既定 none） |
| classification_origin | enum | user / none（AI分類導入時に ai を追加） |
| status | enum | inbox / snoozed / done / dismissed |
| resolved_at | Date? | done／dismissed にした時刻 |
| snoozed_until | Date? | 保留の期限。nil の保留は「無期限保留」とし、S3には出さず S5 から戻す |
| last_presented_at | Date? | S3で最後に提示した時刻 |
| presented_count | Int | 提示回数（圧迫感の分析用） |
| processing_status | enum | pending / fetched / failed / skipped |
| error_code | String? | 取得失敗の種別（timeout / login_required_suspected / network / unsupported） |
| metadata_source / metadata_fetched_at | String? / Date? | 取得元（linkpresentation）と時刻 |
| estimated_minutes / deadline 系 | — | **MVPでは持たない**（引継ぎ資料の項目は将来用に予約） |

保存先：App Group共有コンテナ内のSQLite（SwiftData または GRDB）。画像は同コンテナの `images/`。拡張と本体の同時アクセスはSQLiteのロックに任せ、拡張は書き込みのみ。

## 4. 共有拡張の仕様（S0）
1. 受け取り型：`public.url`（最大1）、`public.image`（最大5）、`public.plain-text`、`public.file-url`（最大1）。
2. 処理：型ごとに値を取り出し、画像は**デコードせずData のまま**書き出す。レコードを `processing_status=pending` で保存。所要が1秒を超えても保存を優先し、UIは「保存中」のまま待つ。
3. 禁止：通信、メタデータ取得、OCR、LLM、本体アプリの起動。
4. 失敗時：保存できなかった理由を `error_code` に記録し「保存できませんでした」を表示して閉じる（内容は失わないよう、生データを `failed/` に退避）。
5. 通知：本体で通知権限が許可済みの場合のみ「保存しました。開いて確認」を即時ローカル通知（設定でオフ可。既定オフ。試用で要否を測る）。

## 5. 本体での取得（P1）
- 起動時とS1の引き下げ更新で、`pending` を新しい順に処理。1件ずつ `LPMetadataProvider`（タイムアウト10秒、サブリソース取得はサムネイルのみ）。
- 失敗は `failed` にして理由を残し、再試行は手動（S2「再取得」）と次回起動時の1回のみ。無限再試行しない。
- Instagram／X／TikTok など、タイトルがログインページ相当（例：「Instagram」「ログイン」のみ）の場合は `login_required_suspected` とし、タイトルは採用せず `shared_text` の先頭を代替表示にする。
- 外部サーバーは使わない（SSRF対策の対象なし）。将来サーバー取得を入れる場合は `01` 5.2 の対策を必須にする。

## 6. 通知（P1、任意）
- 週次通知のみ。既定オフ。曜日・時刻を指定。文面は件数のみ（「見返し候補が5件あります」）。内容を含めない。
- 通知の許可率・無効化を計測する（7章）。

## 7. 計測イベント（本文・画像・URLは記録しない）

| イベント | 属性 | 用途 |
|---|---|---|
| capture_attempt | source_type, host(ドメインのみ), type_identifiers数 | 保存成功率の分母 |
| capture_success / capture_fail | elapsed_ms, error_code | 分子、失敗原因 |
| fetch_result | status, error_code, elapsed_ms | 取得成功率 |
| item_open | from(S1/S2/S3), age_days | 再利用率 |
| item_resolve | status(done/dismissed/snoozed), from, age_days, presented_count | 実行率・整理率 |
| review_start / review_end | shown, resolved, duration_s | 週次レビューの使われ方 |
| notif_permission | granted(bool) / notif_disabled | 通知負担 |
| app_open | — | 7日後利用 |
| export / delete_all | — | 書き出し・削除の利用 |

保存先はローカルのJSONL。試用者が面談時に書き出して渡す（自動送信しない）。集計は `kit/compute_metrics.py`。

## 8. 同意・表示文言（試作品）
- 初回起動：「このアプリは、共有した内容を端末内にだけ保存します。サーバーに送信しません。削除・書き出しはいつでも設定からできます。」
- 外部AIを将来入れる場合（MVPでは出さない）：送信する項目（タイトル・共有テキスト・画像のどれか）、送信先の事業者名、目的、保存条件を項目ごとに表示し、同意しなくても保存と見返しは使えることを明記する。審査ガイドライン5.1.2(i)に対応。

## 9. 受け入れ条件（試作品の完成の定義）
1. `06` 試験Aの10共有元すべてで保存が成功し、1秒以内に拡張が閉じる（画像5枚は2秒以内）。
2. 機内モードで保存・一覧・見返し・完了/保留/不要が動く。
3. 書き出し→削除→読み込みで全件・画像が復元する。
4. 通知オフのまま、週次レビューがアプリ内で完結する。
5. 計測イベントに本文・画像・完全URLが含まれない。
