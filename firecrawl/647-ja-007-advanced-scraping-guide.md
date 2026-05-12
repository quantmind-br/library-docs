---
title: 高度なスクレイピングガイド | Firecrawl
url: https://docs.firecrawl.dev/ja/advanced-scraping-guide
source: sitemap
fetched_at: 2026-03-23T07:27:54.407367-03:00
rendered_js: false
word_count: 440
summary: This document provides a comprehensive technical reference for Firecrawl's scraping endpoints, covering configuration options for formats, content filtering, PDF parsing, caching, and browser automation actions.
tags:
    - firecrawl
    - web-scraping
    - api-reference
    - data-extraction
    - browser-automation
    - pdf-parsing
category: reference
---

Firecrawl の scrape、crawl、map、agent 各エンドポイントで利用できるすべてのオプションのリファレンスです。

## 基本的なスクレイピング

単一のページをスクレイピングしてクリーンなMarkdownコンテンツを取得するには、`/scrape` エンドポイントを使用します。

## PDFのスクレイピング

FirecrawlはPDFに対応しています。PDFを確実に解析したい場合は、`parsers` オプション（例: `parsers: ["pdf"]`）を使用してください。`mode` オプションで解析戦略を制御できます。

- **`auto`** (デフォルト) — まず高速なテキストベース抽出を試み、必要に応じてOCRにフォールバックします。
- **`fast`** — テキストベースの解析のみ（埋め込みテキスト）。最も高速ですが、スキャンされたページや画像の多いページはスキップされます。
- **`ocr`** — すべてのページで強制的にOCR解析を行います。スキャンされたドキュメントや、`auto` がページを誤判定する場合に使用してください。

`{ type: "pdf" }` と `"pdf"` は、どちらもデフォルトで `mode: "auto"` になります。

```
"parsers": [{ "type": "pdf", "mode": "fast", "maxPages": 50 }]
```

## スクレイピングのオプション

`/scrape` エンドポイントを使用する際は、以下のオプションでリクエストをカスタマイズできます。

### フォーマット (`formats`)

`formats` 配列は、スクレイパーが返す出力フォーマットを制御します。デフォルト: `["markdown"]`。 **文字列フォーマット**: 名前をそのまま渡します (例: `"markdown"`)。

FormatDescription`markdown`ページコンテンツをクリーンな Markdown に変換したもの。`html`不要な要素を削除して処理した HTML。`rawHtml`サーバーから返されたオリジナルの HTML をそのまま返すもの。`links`ページ上で見つかったすべてのリンク。`images`ページ上で見つかったすべての画像。`summary`ページコンテンツの LLM 生成サマリー。`branding`ブランドアイデンティティ (色、フォント、タイポグラフィ、余白、UI コンポーネント) を抽出。

**オブジェクトフォーマット**: `type` と追加オプションを含むオブジェクトを渡します。

FormatOptionsDescription`json``prompt?: string`, `schema?: object`LLM を使って構造化データを抽出します。JSON スキーマおよび/または自然言語のプロンプトを指定します (最大 10,000 文字)。`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`スクリーンショットを取得します。リクエストごとに最大 1 枚。ビューポートの最大解像度は 7680×4320。スクリーンショット URL は 24 時間後に期限切れになります。`changeTracking``modes?: ("json" | "git-diff")[]`, `tag?: string`, `schema?: object`, `prompt?: string`スクレイプ結果間の変更を追跡します。`formats` 配列に `"markdown"` も含まれている必要があります。`attributes``selectors: [{ selector: string, attribute: string }]`CSS セレクタにマッチする要素から特定の HTML 属性を抽出します。

### コンテンツフィルタリング

これらのパラメータは、ページのどの部分を出力に含めるかを制御します。`onlyMainContent` は最初に実行されてナビゲーションやフッターなどの共通レイアウト部分を除去し、その後に `includeTags` と `excludeTags` によって結果がさらに絞り込まれます。`onlyMainContent: false` を設定すると、タグフィルタリングの起点としてページ全体の HTML が使用されます。

ParameterTypeDefaultDescription`onlyMainContent``boolean``true`メインコンテンツのみを返します。ページ全体を対象にするには `false` を設定します。`includeTags``array`—含める HTML タグ、クラス、または ID（例: `["h1", "p", ".main-content"]`）。`excludeTags``array`—除外する HTML タグ、クラス、または ID（例: `["#ad", "#footer"]`）。

### タイミングとキャッシュ

ParameterTypeDefaultDescription`waitFor``integer` (ms)`0`スマート待機に加えて、スクレイピング前に追加で待機する時間。必要な場合にのみ使用してください。`maxAge``integer` (ms)`172800000`この値より新しい場合はキャッシュされたバージョンを返す (デフォルトは2日) 。常に最新を取得するには `0` を指定。`timeout``integer` (ms)`30000`リクエストを中断するまでの最大時間 (デフォルトは30秒) 。最小値は1000 (1秒) 。

### PDF 解析

ParameterTypeDefaultDescription`parsers``array``["pdf"]`PDF の処理方法を制御します。`[]` で解析をスキップしてbase64 を返す（1 クレジット固定）。

```
{ "type": "pdf", "mode": "fast" | "auto" | "ocr", "maxPages": 10 }
```

PropertyTypeDefaultDescription`type``"pdf"`*(required)*パーサーの種類。`mode``"fast" | "auto" | "ocr"``"auto"``fast`: テキストベースの抽出のみを実行。`auto`: fast で処理し、必要に応じて OCR をフォールバックとして使用。`ocr`: OCR のみを強制的に使用。`maxPages``integer`—解析するページ数の上限を設定。

### アクション

スクレイピング前にブラウザ アクションを実行できます。これは、動的コンテンツ、ナビゲーション、ユーザー制限付きページに対して有用です。1 リクエストあたり指定できるアクションは最大 50 個で、すべての `wait` アクションおよび `waitFor` の合計待機時間は 60 秒以内である必要があります。

ActionParametersDescription`wait``milliseconds?: number`, `selector?: string`固定時間待機 **または** 要素が表示されるまで待機します（どちらか一方のみ指定してください）。`selector` を使用する場合、タイムアウトは 30 秒です。`click``selector: string`, `all?: boolean`CSS セレクタにマッチする要素をクリックします。`all: true` を指定すると、すべてのマッチ対象をクリックします。`write``text: string`現在フォーカスされているフィールドにテキストを入力します。事前に `click` アクションで要素にフォーカスする必要があります。`press``key: string`キーボードキーを押下します（例: `"Enter"`、`"Tab"`、`"Escape"`）。`scroll``direction?: "up" | "down"`, `selector?: string`ページ全体または特定の要素をスクロールします。`direction` のデフォルトは `"down"` です。`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`スクリーンショットを取得します。最大ビューポート解像度は 7680×4320 です。`scrape`*(none)*アクションシーケンスのこの時点で、現在のページ HTML を取得します。`executeJavascript``script: string`ページ内で JavaScript コードを実行します。`{ type, value }` を返します。`pdf``format?: string`, `landscape?: boolean`, `scale?: number`PDF を生成します。サポートされるフォーマット: `"A0"`〜`"A6"`、`"Letter"`、`"Legal"`、`"Tabloid"`、`"Ledger"`。デフォルトは `"Letter"` です。

#### アクション実行時の注意点

- **Write** を使う前に、対象要素へフォーカスするための `click` が必要です。
- **Scroll** は、ページ全体ではなく特定の要素をスクロールするために、任意の `selector` を指定できます。
- **Wait** は、`milliseconds`（固定の待機時間）または `selector`（指定要素が表示されるまで待機）のいずれかを受け取ります。
- アクションは **逐次的に** 実行されます。各ステップは、次のステップが開始する前に完了します。
- アクションは **PDF では利用できません**。URL が PDF に解決される場合、そのリクエストは失敗します。

#### 高度なアクション例

**スクリーンショットを撮影する:**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": "#load-more" },
      { "type": "wait", "milliseconds": 1000 },
      { "type": "screenshot", "fullPage": true, "quality": 80 }
    ]
  }'
```

**複数の要素をクリックする:**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": ".expand-button", "all": true },
      { "type": "wait", "milliseconds": 500 }
    ],
    "formats": ["markdown"]
  }'
```

**PDF を生成する:**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "pdf", "format": "A4", "landscape": false }
    ]
  }'
```

### フルスクレイプの例

次のリクエストでは、複数のスクレイプオプションを組み合わせています。

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats": [
        "markdown",
        "links",
        "html",
        "rawHtml",
        { "type": "screenshot", "fullPage": true, "quality": 80 }
      ],
      "includeTags": ["h1", "p", "a", ".main-content"],
      "excludeTags": ["#ad", "#footer"],
      "onlyMainContent": false,
      "waitFor": 1000,
      "timeout": 15000,
      "parsers": ["pdf"]
    }'
```

このリクエストは、Markdown、HTML、raw HTML、リンク、およびページ全体のスクリーンショットを返します。コンテンツの対象を `<h1>`、`<p>`、`<a>`、`.main-content` に絞り、`#ad` と `#footer` を除外し、スクレイピング前に1秒待機し、タイムアウトを15秒に設定し、PDF解析を有効にします。 詳細は [Scrape API reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape) を参照してください。

`formats` 内で JSON フォーマットオブジェクトを使用して、一度の処理で構造化データを抽出します。

## Agent endpoint

自律的に複数ページにまたがるデータを抽出するには、`/v2/agent` エンドポイントを使用します。エージェントは非同期で動作します。まずジョブを開始し、その後、結果が返ってくるまでポーリングします。

### エージェントオプション

ParameterTypeDefaultDescription`prompt``string`*(required)*抽出するデータを自然言語で記述した指示 (最大 10,000 文字) 。`urls``array`—エージェントの処理対象を限定する URL。`schema``object`—抽出データの構造を定義する JSON スキーマ。`maxCredits``number``2500`エージェントが消費できる最大クレジット数。ダッシュボードでは最大 2,500 まで対応しています。より高い上限を設定する場合は、API 経由で設定してください (2,500 を超える値は常に有料リクエストとして課金されます) 。`strictConstrainToURLs``boolean``false``true` の場合、エージェントは指定された URL のみを巡回します。`model``string``"spark-1-mini"`使用する AI モデル。`"spark-1-mini"` (デフォルト、60% 低コスト) または `"spark-1-pro"` (高精度) 。

### エージェントのステータスを確認する

進捗状況を確認するには、`GET /v2/agent/{jobId}` をポーリングします。レスポンスの `status` フィールドは `"processing"`、`"completed"`、または `"failed"` のいずれかになります。

```
curl -X GET https://api.firecrawl.dev/v2/agent/YOUR-JOB-ID \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

Python および Node 用の SDK には、ジョブを開始し、完了するまで自動的にポーリングするための便利なメソッド `firecrawl.agent()` も用意されています。

## 複数ページのクロール

複数のページをクロールするには、`/v2/crawl` エンドポイントを使用します。クロールは非同期で実行され、ジョブIDが返されます。`limit` パラメータを使用して、クロールするページ数を制御します。省略した場合、最大 10,000 ページまでクロールされます。

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
```

### レスポンス

```
{ "id": "1234-5678-9101" }
```

### クロールジョブを確認する

ジョブIDを使用してクロールのステータスを確認し、その結果を取得します。

```
curl -X GET https://api.firecrawl.dev/v2/crawl/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

コンテンツサイズが 10MB を超える場合、またはクロールジョブがまだ実行中の場合、レスポンスには `next` パラメータ（次の結果ページを指す URL）が含まれることがあります。

### クロール用プロンプトとパラメータのプレビュー

自然言語の `prompt` を指定すると、Firecrawl がクロール設定を自動で推定します。まずはプレビューしてください：

```
curl -X POST https://api.firecrawl.dev/v2/crawl/params-preview \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "prompt": "ドキュメントとブログを抽出する"
  }'
```

### クローラーオプション

`/v2/crawl` エンドポイントでは、次のオプションでクロールの挙動をカスタマイズできます。

#### パスフィルタリング

ParameterTypeDefaultDescription`includePaths``array`—デフォルトでは URL のパス名のみに適用される、インクルード対象とする URL の正規表現パターン。`excludePaths``array`—デフォルトでは URL のパス名のみに適用される、除外対象とする URL の正規表現パターン。`regexOnFullURL``boolean``false`パス名ではなく、完全な URL に対してパターンをマッチさせます。

#### クロール範囲

ParameterTypeDefaultDescription`maxDiscoveryDepth``integer`—新しいURLを発見する際の最大リンク深度。`limit``integer``10000`クロールするページ数の上限。`crawlEntireDomain``boolean``false`同一階層や上位階層のページも探索してドメイン全体をカバーする。`allowExternalLinks``boolean``false`外部ドメインへのリンクもたどる。`allowSubdomains``boolean``false`メインドメインのサブドメインもたどる。`delay``number` (s)—スクレイピング間のディレイ。

#### サイトマップと重複排除

ParameterTypeDefaultDescription`sitemap``string``"include"``"include"`: サイトマップ + リンク発見を使用します。`"skip"`: サイトマップを無視します。`"only"`: サイトマップ上の URL のみをクロールします。`deduplicateSimilarURLs``boolean``true`URL のバリエーション（`www.`, `https`, 末尾のスラッシュ, `index.html`）を正規化し、同一の URL として扱います。`ignoreQueryParameters``boolean``false`重複排除の前にクエリ文字列を除去します（例: `/page?a=1` と `/page?a=2` は 1 つの URL と見なされます）。

#### クローリング時のスクレイプオプション

ParameterTypeDefaultDescription`scrapeOptions``object``{ formats: ["markdown"] }`ページ単位のスクレイプ設定。上記のすべての [scrape options](#scrape-options) が利用可能です。

### クロールの例

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "includePaths": ["^/blog/.*$", "^/docs/.*$"],
      "excludePaths": ["^/admin/.*$", "^/private/.*$"],
      "maxDiscoveryDepth": 2,
      "limit": 1000
    }'
```

## ウェブサイトリンクのマッピング

`/v2/map` エンドポイントは、指定したウェブサイトに関連する URL を特定します。

```
curl -X POST https://api.firecrawl.dev/v2/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

### マップオプション

ParameterTypeDefaultDescription`search``string`—指定したテキストに一致するリンクのみを対象にします。`limit``integer``100`返すリンクの最大数。`sitemap``string``"include"``"include"`、`"skip"`、`"only"` のいずれかを指定。`includeSubdomains``boolean``true`サブドメインを含めるかどうか。

該当するAPIリファレンスはこちら: [Map Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)

### 自分のウェブサイトのスクレイピングを Firecrawl に許可する

- **User Agent**: ファイアウォールやセキュリティルールで `FirecrawlAgent` を許可してください。
- **IP addresses**: Firecrawl は、外向き通信に固定の送信元 IP アドレスを使用していません。

### アプリケーションから Firecrawl API への呼び出しを許可する

ファイアウォールがアプリケーションから外部サービスへのアウトバウンドリクエストをブロックしている場合は、アプリケーションが Firecrawl API（`api.firecrawl.dev`）に到達できるよう、Firecrawl の API サーバーの IP アドレスをホワイトリストに追加する必要があります。

- **IP Address**: `35.245.250.27`

この IP をファイアウォールのアウトバウンド許可リストに追加し、バックエンドから Firecrawl へ scrape、crawl、map、および agent リクエストを送信できるようにしてください。