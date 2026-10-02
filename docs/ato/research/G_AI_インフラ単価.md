# G. 変動費試算のための現行単価調査（ATO：URL・画像のAI分類・要約 iPhoneアプリ）

- 確認日：2026-10-02
- 通貨：特記なき限り USD。JPY換算は第7項の暫定レートによる試算値。
- 確認方法の凡例
  - **[ページ取得で確認]** … 公式ページ（または公式ドキュメントのソースリポジトリ／公式Price List API）の本文を取得して確認
  - **[検索結果要約で確認（ページ本文は未取得）]** … WebSearch の結果要約のみ。公式ページ本文は取得できていない
  - **[取得失敗（ネットワーク制限）]** … 本環境のエグレス制限で 403。再試行せず
  - **未確認** … 上記いずれでも確認できず。計算には使用しない
- 補足：本セッションは WebSearch の上限（200回）に到達したため、未調査項目は「未確認（検索上限のため未調査）」と記載。

---

## 1. Anthropic Claude API（[ページ取得で確認]）

出典（取得済み）：
- https://platform.claude.com/docs/en/about-claude/pricing（docs.claude.com からの302リダイレクト先。確認日 2026-10-02）
- https://claude.com/pricing（anthropic.com/pricing からの301リダイレクト先。確認日 2026-10-02）
- https://platform.claude.com/docs/en/build-with-claude/vision（画像トークンの計算式。確認日 2026-10-02）

### 1-1. 現行モデルと料金（USD / 100万トークン）

| モデル | 入力 | 出力 | 5分キャッシュ書込 | 1時間キャッシュ書込 | キャッシュ読取 | Batch 入力 | Batch 出力 |
|---|---|---|---|---|---|---|---|
| Claude Fable 5.1 | $10 | $50 | $12.50 | $20 | $0.25 | $5 | $25 |
| Claude Fable 5 | $10 | $50 | $12.50 | $20 | $1 | $5 | $25 |
| Claude Opus 5.5 | $4 | $20 | $5 | $8 | $0.20 | $2 | $10 |
| Claude Opus 5 / 4.8 / 4.7 / 4.6 / 4.5 | $5 | $25 | $6.25 | $10 | $0.50 | $2.50 | $12.50 |
| Claude Sonnet 5.5 | $2 | $10 | $2.50 | $4 | $0.20 | $1 | $5 |
| Claude Sonnet 5 | $2 | $10 | $2.50 | $4 | $0.20 | $1 | $5 |
| Claude Sonnet 4.6 / 4.5 | $3 | $15 | $3.75 | $6 | $0.30 | $1.50 | $7.50 |
| **Claude Haiku 4.5（最安）** | **$1** | **$5** | $1.25 | $2 | $0.10 | $0.50 | $2.50 |
| Claude Haiku 3.5（retired） | $0.80 | $4 | $1 | $1.60 | $0.08 | $0.40 | $2 |

- **最安の現行モデル：Claude Haiku 4.5（$1 / $5）**。Haiku 3.5 は retired（Bedrock/Google Cloud のみ残存）のため採用しない。
- **中位モデル：Claude Sonnet 5.5（$2 / $10）**（claude.com/pricing の現行ラインナップは Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 4.5 の4つ）。
- 注意：Claude 4.7 以降のモデルは新トークナイザで「同じテキストで約30%多いトークン」になる（pricing ページ記載）。Haiku 4.5 は旧トークナイザ、Sonnet 5.5 は新トークナイザ側。試算で同じ「2,000トークン」を前提にすると Sonnet 側はやや過小評価になり得る。

### 1-2. 割引率
- **Batch API：入力・出力とも 50% 割引**（上表の Batch 列）。
- **プロンプトキャッシュ**：5分キャッシュ書込 = 入力単価の 1.25倍、1時間キャッシュ書込 = 2倍、**キャッシュ読取（ヒット）= 入力単価の 0.1倍（90%引き）**。例外：Fable 5.1 は 0.025倍、Opus 5.5 は 0.05倍。Batch 割引とキャッシュ割引は併用可能（乗算で重なる）。
- 長文コンテキスト（1Mトークン）は追加料金なし（4.6以降）。`inference_geo: "us"` 指定時は 1.1倍。

### 1-3. 画像入力の料金の考え方（公式計算式）
- 画像は 28×28 px のパッチ単位で「ビジュアルトークン」として課金：**トークン数 = ⌈幅/28⌉ × ⌈高さ/28⌉**。
- 上限：Claude 4.7 以降（高解像度ティア）は長辺 2576 px / 最大 4784 トークン、それ以外（標準ティア、Haiku 4.5 を含む）は長辺 1568 px / 最大 1568 トークン。超過分は縮小される。
- 公式ページの例：1000×1000 px = 1,296 トークン、1092×1092 px = 1,521 トークン、1920×1080 px = 標準ティア 1,560 / 高解像度 2,691 トークン。Haiku 4.5（$1/MTok）で 1000×1000 画像は約 $1.30 / 1,000枚。
- **1024×1024 px の場合：⌈1024/28⌉ = 37 → 37 × 37 = 1,369 トークン**（標準・高解像度どちらのティアでも縮小されない）。
- 費用 = 画像トークン × 当該モデルの入力単価。画像自体に別建ての固定料金はない。

---

## 2. OpenAI API

- 公式ページ：https://openai.com/api/pricing/ 、https://platform.openai.com/docs/pricing 、https://developers.openai.com/api/docs/pricing 、https://developers.openai.com/api/docs/guides/images-vision → いずれも **[取得失敗（ネットワーク制限）]**
- 第三者集計（openrouter.ai、morphllm.com）も **[取得失敗（ネットワーク制限）]**

**[検索結果要約で確認（ページ本文は未取得）]**（確認日 2026-10-02）
- GPT-5 nano：入力 $0.05 / 出力 $0.40（100万トークン）、コンテキスト 400K
- GPT-5 mini：入力 $0.25 / 出力 $2.00（100万トークン）、コンテキスト 400K
- 検索結果のタイトルには GPT-5.4 / 5.5 / 5.6 など新世代の存在が示唆されるが、単価は **未確認（検索上限のため未調査）**。
- 画像入力の料金計算（パッチ数・モデル別乗数）：**未確認（公式ページ取得失敗・検索上限）**。
- 中位モデルの単価：**未確認**。
- 出典（要約元）：https://openrouter.ai/openai/gpt-5-nano 、https://openrouter.ai/openai/gpt-5-mini 、https://pricepertoken.com/pricing-page/model/openai-gpt-5-nano 、https://www.morphllm.com/openai-api-pricing（いずれも本文未取得）

→ 本試算の第8項では OpenAI は計算に使わない。

---

## 3. Google Gemini API

- Gemini API（AI Studio）公式 https://ai.google.dev/gemini-api/docs/pricing → **[取得失敗（ネットワーク制限）]**
- Vertex AI 公式 https://cloud.google.com/vertex-ai/generative-ai/pricing → **[ページ取得で確認]**（curl で本文取得、確認日 2026-10-02。USD、Global エンドポイント、Standard 価格。Non-global は 10% 増し）

| モデル（Vertex AI） | 入力（text/image/video） | 出力 | 備考 |
|---|---|---|---|
| **Gemini 3.1 Flash-Lite（最安）** | **$0.25** | **$1.50** | Flex/Batch：$0.125 / $0.75、Priority：$0.45 / $2.70、キャッシュ入力 $0.025 |
| Gemini 3.5 Flash-Lite | $0.30 | $2.50 | Flex/Batch：$0.15 / $1.25 |
| Gemini 2.5 Flash | $0.30 | $2.50 | Batch：$0.15 / $1.25 |
| Gemini 3.6 / 3.7 / 3.8 Flash | $0.75（導入価格、2026-12-31まで） | $3.75（同） | 2027-01-01 以降は $1.50 / $7.50 |
| Gemini 3.5 Flash | $1.50 | $9.00 | Flex/Batch：$0.75 / $4.50 |
| Gemini 3 Flash Preview | $0.50 | （出力は抽出範囲外） | |

- 画像入力：上記「入力」単価にトークン換算で課金。ページ注記「**1024×1024 の画像は 1,290 トークン**（画像トークン数は解像度により変動）」。
- 無料枠：Vertex AI の料金ページには無料枠の記載なし（従量課金）。Gemini API（AI Studio）側の無料枠は **[検索結果要約で確認（ページ本文は未取得）]**：「Flash / Flash-Lite 系に無料ティアあり（トークン課金なし、レート制限で制御。要約では『1日1,500リクエストまで』『クレジットカード不要』）」。具体的な現行の RPM/RPD 条件は **未確認**。
- 要約元：https://www.morphllm.com/gemini-api-pricing 、https://tokenmix.ai/blog/gemini-api-pricing 、https://creditforstartups.com/pricing/gemini-api-pricing（本文未取得）

---

## 4. オブジェクトストレージ

### 4-1. Cloudflare R2（[ページ取得で確認]）
- 出典：公式ドキュメントのソース（cloudflare/cloudflare-docs リポジトリ production ブランチ）https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/r2/pricing.mdx（公開ページ https://developers.cloudflare.com/r2/pricing/ は [取得失敗（ネットワーク制限）]）。確認日 2026-10-02。
- Standard storage：**$0.015 / GB-month**、Class A（書込系）$4.50 / 100万リクエスト、Class B（読取系）$0.36 / 100万リクエスト
- Infrequent Access：$0.01 / GB-month、Class A $9.00 / 100万、Class B $0.90 / 100万、データ取出 $0.01 / GB、最低保存 30日
- **エグレス（インターネットへの転送）：全ストレージクラスで無料**。条件：R2 から直接（Workers API、S3 API、r2.dev ドメイン、カスタムドメイン経由）のエグレスは転送課金なし。
- **無料枠（毎月、Standard のみ）：10 GB-month、Class A 100万リクエスト、Class B 1,000万リクエスト**。削除系操作は無料。
- 請求単位は切り上げ（1.1 GB-month → 2 GB-month 課金）。

### 4-2. AWS S3 東京リージョン ap-northeast-1（[ページ取得で確認：公式 Price List API]）
- 出典：https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/ap-northeast-1/index.csv（Publication Date 2026-09-28、Version 20260928230416）。公開ページ https://aws.amazon.com/s3/pricing/ は [取得失敗（ネットワーク制限）]。
- S3 Standard 保存：**$0.025 / GB-月（最初の 50 TB）**、$0.024（次の 450 TB）、$0.023（500 TB 超）
- リクエスト：PUT/COPY/POST/LIST **$0.0047 / 1,000 リクエスト**、GET その他 **$0.0037 / 10,000 リクエスト**
- インターネットへのデータ転送（DTO）：S3 の Price List には AWS 内向け（$0.0）と MRAP 分しか含まれず、インターネット向け段階料金は **未確認（Price List 上は別オファー "AWSDataTransfer"）**。参考として **[検索結果要約で確認（ページ本文は未取得）]**：月 100 GB まで無料、以降 10 TB まで $0.09 / GB（要約元：https://www.cloudzero.com/blog/s3-pricing/ ほか）。

### 4-3. Supabase Storage
- 公式 https://supabase.com/pricing → **[取得失敗（ネットワーク制限）]**。GitHub リポジトリ経由も本セッションでは取得不可。
- **[検索結果要約で確認（ページ本文は未取得）]**：Free $0（Storage 1 GB、Egress 5 GB/月、DB 500 MB、MAU 50,000、2 プロジェクト）。Pro $25/月（Storage 100 GB、Egress 250 GB/月、DB 8 GB、MAU 100,000、7日分バックアップ）。超過：Storage **$0.021 / GB-月**、Egress **$0.09 / GB**。
- 要約元：https://makerkit.dev/blog/saas/supabase-pricing 、https://www.srvrlss.io/provider/supabase/ 、https://costbench.com/software/database-as-service/supabase/（本文未取得）

### 4-4. Firebase Storage（Cloud Storage for Firebase）
- 公式 https://firebase.google.com/pricing → **[取得失敗（ネットワーク制限）]**
- **[検索結果要約で確認（ページ本文は未取得）]**：2026-02-03 以降、Cloud Storage for Firebase は Blaze（課金アカウント連携）が必須。Blaze の無償枠（us-central1 / us-west1 / us-east1 の *.firebasestorage.app バケット）：5 GB-月、転送 100 GB/月、Class A 5,000、Class B 50,000。超過：$0.026 / GB 保存、$0.12 / GB ダウンロード、アップロード $0.05 / 1万回、ダウンロード $0.004 / 1万回。
- 裏付け（[ページ取得で確認] https://cloud.google.com/storage/pricing、curl 取得）：Cloud Storage の Always Free = Standard storage 5 GB-months、Class A 5,000、Class B 50,000、転送 100 GB（US-WEST1 / US-CENTRAL1 / US-EAST1 のみ）。インターネット向け転送（Asia・Australia 除く宛先）$0.12 / GiB（0–10 TiB）。us-central1 Standard storage は $0.000027397 / GiB-時（≒ $0.020 / GiB-月）。東京（asia-northeast1）の保存単価はページがJS描画のため **未確認**。

---

## 5. サーバーレス / 軽量バックエンド

### 5-1. Cloudflare Workers（[ページ取得で確認]）
- 出典：https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/workers/platform/pricing.mdx および .../workers/platform/limits.mdx（公開ページ https://developers.cloudflare.com/workers/platform/pricing/ は [取得失敗（ネットワーク制限）]）。確認日 2026-10-02。
- **Free：100,000 リクエスト/日（UTC 0時リセット）、CPU 時間 10 ms/呼び出し**、Workers KV・Pages Functions・Hyperdrive の限定利用を含む。静的アセットへのリクエストは無料・無制限。
- **Paid（Standard）：最低 $5 USD/月/アカウント**。月 1,000万リクエスト込み（超過 $0.30 / 100万）、CPU 時間 3,000万 CPU-ms/月込み（超過 $0.02 / 100万 CPU-ms）、CPU 上限 5 分/リクエスト（既定 30 秒）。Durable Objects も含む。

### 5-2. Supabase
- 公式 → **[取得失敗（ネットワーク制限）]**。**[検索結果要約で確認（ページ本文は未取得）]**：Free $0 / Pro $25/月（内訳は 4-3 参照）。Pro 以上では Compute アドオン等が別途（未確認）。

### 5-3. Firebase（Spark / Blaze）
- 公式 → **[取得失敗（ネットワーク制限）]**。**[検索結果要約で確認（ページ本文は未取得）]**：Spark = 無料プラン（Firestore 1 GB、読取 50K/日、書込 20K/日、削除 20K/日 等）、Blaze = 従量課金（無償枠超過分のみ課金）。
- 裏付け（[ページ取得で確認] https://cloud.google.com/firestore/pricing、curl 取得）：Firestore 無料枠 = 保存 1 GiB、読取 50,000/日、書込 20,000/日、削除 20,000/日、送信転送 10 GiB/月（1プロジェクト1DBまで）。

---

## 6. Apple（[ページ取得で確認]）

- App Store 手数料：**標準 30%**。**Small Business Program：15%**（有料アプリ・App 内課金）。
  - 条件：前暦年の全アプリ合計 proceeds（Apple 手数料・税等控除後の売上、USD 換算）が **100万 USD 以下**、かつ当年も 100万 USD を超えないこと。Account Holder であること、最新の Paid Apps 契約への同意、関連デベロッパアカウントの開示が必要。当年中に 100万 USD を超えた以降の売上は 30%。翌年以降に下回れば再申請可。
  - 出典：https://developer.apple.com/app-store/small-business-program/（確認日 2026-10-02）
- Apple Developer Program 年会費：**99 USD/年**（Enterprise Program は 299 USD/年）。
  - 出典：https://developer.apple.com/programs/ 、https://developer.apple.com/jp/programs/ 、https://developer.apple.com/jp/help/account/membership/program-enrollment/（確認日 2026-10-02）。日本語ヘルプの記載：「年間登録料は99米ドル…（または現地通貨の同等額）。価格は地域によって異なる場合があり、登録手続きの際は現地通貨で表示されます。」
  - **JPY 額は公式ページに記載なし → 未確認**。参考 **[検索結果要約で確認（ページ本文は未取得）]**：2026年の実払い例として ¥12,980（税込）という記事あり（要約元：https://www.tekural.com/blog/apple-developer-program-cost 、https://zenn.dev/ytz_ichi/articles/4d13d1b734fbba。本文未取得）。試算では 99 USD × 第7項レートを併記する。

---

## 7. 為替の目安（USD/JPY）

- 日本銀行 https://www.boj.or.jp/statistics/market/forex/fxdaily/index.htm 、tradingeconomics.com、Google Finance、Yahoo Finance、Wise、x-rates、三菱UFJリサーチ&コンサルティング、みずほ、三井住友、frankfurter.app、open.er-api.com → すべて **[取得失敗（ネットワーク制限）]**
- **[検索結果要約で確認（ページ本文は未取得）]**：2026-09-30 の USD/JPY は 157.39（要約元：https://tradingeconomics.com/japan/currency）。10/2 の予測値として 158.37（要約元：https://30rates.com/usd-to-jpy-forecast-converter-dollar-to-yen 等の予測サイト、断定不可）。
- **試算用暫定レート：1 USD = 157 JPY**（断定せず、上記要約値を丸めた参考値。実際の計算時に最新レートへ差し替えること）。

---

## 8. 参考試算：URL保存 1 件あたりの AI 処理費用（Anthropic、[ページ取得で確認] 済みの単価のみ使用）

前提
- 最安モデル：Claude Haiku 4.5（入力 $1 / 出力 $5 per 1M tokens）
- 中位モデル：Claude Sonnet 5.5（入力 $2 / 出力 $10 per 1M tokens）
- 計算式：費用(USD) = 入力トークン × 入力単価 / 1,000,000 + 出力トークン × 出力単価 / 1,000,000
- 画像 1 枚（1024×1024）= ⌈1024/28⌉² = 37² = **1,369 トークン**（第1-3項）
- キャッシュ・Batch は未適用（適用時の値は下段に併記）。システムプロンプト等の固定分は含めていない（実装時は数百トークン追加されるので、必要ならキャッシュ対象にする）。
- JPY 換算：1 USD = 157 JPY（第7項の暫定レート）

### 8-1. ケースA：本文テキスト 2,000 トークン入力 + 出力 200 トークン（分類・要約）

| モデル | 計算 | 1件あたり USD | 1件あたり JPY（157円換算） |
|---|---|---|---|
| Haiku 4.5 | 2,000×1/1e6 + 200×5/1e6 = 0.002 + 0.001 | **$0.0030** | 約 0.47 円 |
| Sonnet 5.5 | 2,000×2/1e6 + 200×10/1e6 = 0.004 + 0.002 | **$0.0060** | 約 0.94 円 |

### 8-2. ケースB：画像 1 枚（1024×1024 ≒ 1,369 トークン）+ 出力 200 トークン（OCR補助・分類）

| モデル | 計算 | 1件あたり USD | 1件あたり JPY（157円換算） |
|---|---|---|---|
| Haiku 4.5 | 1,369×1/1e6 + 200×5/1e6 = 0.001369 + 0.001 | **$0.002369** | 約 0.37 円 |
| Sonnet 5.5 | 1,369×2/1e6 + 200×10/1e6 = 0.002738 + 0.002 | **$0.004738** | 約 0.74 円 |

### 8-3. 利用者 1 人あたり月額（件数 × 1件あたり費用）

| 月間件数 | ケース | Haiku 4.5 USD | Haiku 4.5 JPY | Sonnet 5.5 USD | Sonnet 5.5 JPY |
|---|---|---|---|---|---|
| 100 件 | A（テキスト） | $0.30 | 約 47 円 | $0.60 | 約 94 円 |
| 100 件 | B（画像） | $0.237 | 約 37 円 | $0.474 | 約 74 円 |
| 300 件 | A（テキスト） | $0.90 | 約 141 円 | $1.80 | 約 283 円 |
| 300 件 | B（画像） | $0.711 | 約 112 円 | $1.421 | 約 223 円 |
| 1,000 件 | A（テキスト） | $3.00 | 約 471 円 | $6.00 | 約 942 円 |
| 1,000 件 | B（画像） | $2.369 | 約 372 円 | $4.738 | 約 744 円 |

計算例（1,000件・A・Sonnet 5.5）：$0.0060 × 1,000 = $6.00 → 6.00 × 157 = 942 円。

### 8-4. 割引適用時の目安（公式割引率による）
- Batch API（50% 引き、非同期処理が許容できる場合）：上表の **半額**。例：1,000件・A は Haiku $1.50 / Sonnet $3.00。
- プロンプトキャッシュ：固定のシステムプロンプト部分のみ 0.1倍（Haiku 4.5・Sonnet 4.6 以前）／ 0.2倍相当（Sonnet 5.5 は $0.20/MTok = 0.1倍）になる。本試算の 2,000 トークンは毎回異なる本文と仮定しているためキャッシュ効果は見込んでいない。
- 注意：Sonnet 5.5 など 4.7 以降のモデルは同じ本文で約 30% 多くトークン化されるため、実測では Sonnet 側の入力が 2,000 → 約 2,600 トークン相当になり得る（その場合 A は $0.0072/件）。

### 8-5. 参考：他社最安モデルでの同条件（確認レベルに注意）
- Gemini 3.1 Flash-Lite（Vertex AI、[ページ取得で確認]、$0.25 / $1.50）：ケースA = 2,000×0.25/1e6 + 200×1.5/1e6 = $0.0005 + $0.0003 = **$0.0008/件**（1,000件で $0.80）。ケースB（1024×1024 = 1,290 トークン、ページ注記）= 1,290×0.25/1e6 + 200×1.5/1e6 = $0.0003225 + $0.0003 = **$0.00062/件**。Flex/Batch なら半額。
- OpenAI GPT-5 nano / mini：単価が **[検索結果要約のみ]** のため本試算では計算対象外（要約値 nano $0.05/$0.40 を仮に当てはめると A = $0.00018/件 だが未確認）。

---

## 9. 取得失敗 URL 一覧（ネットワーク制限、再試行せず）
- https://openai.com/api/pricing/ 、https://platform.openai.com/docs/pricing 、https://developers.openai.com/api/docs/pricing 、https://developers.openai.com/api/docs/models/gpt-5-nano 、https://developers.openai.com/api/docs/guides/images-vision
- https://ai.google.dev/gemini-api/docs/pricing 、https://docs.cloud.google.com/...（image-understanding）
- https://developers.cloudflare.com/r2/pricing/ 、https://developers.cloudflare.com/workers/platform/pricing/ 、https://www.cloudflare.com/...（代替：GitHub の公式ドキュメントソースで取得済み）
- https://supabase.com/pricing
- https://firebase.google.com/pricing
- https://aws.amazon.com/s3/pricing/（代替：公式 Price List API で取得済み）
- https://www.boj.or.jp/statistics/market/forex/fxdaily/index.htm 、https://tradingeconomics.com/japan/currency 、Google Finance / Yahoo Finance / Wise / x-rates / 国内銀行レートページ / api.frankfurter.app / open.er-api.com
- https://openrouter.ai/openai/gpt-5-nano 、https://openrouter.ai/openai/gpt-5-mini 、https://www.morphllm.com/openai-api-pricing 、https://www.tekural.com/blog/apple-developer-program-cost

## 10. 未確認項目まとめ（計算に未使用）
- OpenAI 全モデルの公式単価・画像トークン計算（検索要約のみ）
- Gemini API（AI Studio）無料枠の現行条件（検索要約のみ）
- AWS S3 東京のインターネット向け転送単価（検索要約のみ）
- Supabase / Firebase の公式単価（検索要約のみ。GCS / Firestore の公式ページで一部裏付け）
- Apple Developer Program の JPY 年会費（公式は「現地通貨で登録時に表示」）
- USD/JPY の当日レート（検索要約の 157.39（9/30）を丸めた 157 を暫定使用）
