---
title: バッチスクレープ - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:13:50.848192-03:00
rendered_js: false
word_count: 279
summary: This document provides a technical reference for configuring batch scraping requests using the Firecrawl API, detailing parameters for output formats, caching, proxy settings, and execution actions.
tags:
    - firecrawl-api
    - web-scraping
    - batch-processing
    - api-reference
    - data-extraction
    - proxy-settings
category: reference
---

複数のURLをスクレイピングし、必要に応じてLLMを用いて情報を抽出する

> Firecrawl API key が必要な AI エージェントの場合は、自動オンボーディング手順について [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

同時に実行されるスクレイプの最大数。このパラメータで、このバッチスクレイプに対する同時実行数の上限を設定できます。指定しない場合、このバッチスクレイプはチームで設定された同時実行数の上限に従います。

urls 配列に無効な URL が含まれている場合、それらは無視されます。無効な URL が原因でリクエスト全体が失敗するのではなく、残りの有効な URL を使ってバッチスクレイプが作成され、無効な URL はレスポンスの invalidURLs フィールドで返されます。

formats

(Markdown · object | Summary · object | HTML · object | Raw HTML · object | Links · object | Images · object | Screenshot · object | JSON · object | Change Tracking · object | Branding · object)\[]

レスポンスに含める出力フォーマットを指定します。1つ以上のフォーマットを、文字列（例: `'markdown'`）または追加オプションを含むオブジェクト（例: `{ type: 'json', schema: {...} }`）として指定できます。一部のフォーマットでは、特定のオプションの設定が必須です。例: `['markdown', { type: 'json', schema: {...} }]`。

- Markdown
- Summary
- HTML
- Raw HTML
- Links
- Images
- Screenshot
- JSON
- Change Tracking
- Branding

ヘッダーやナビゲーション、フッターなどを除外し、ページのメインコンテンツのみを返します。

ページのキャッシュが、この値（ミリ秒）で指定した有効期間より新しい場合は、そのキャッシュ版を返します。キャッシュがこの値より古い場合は、新たにページのスクレイピングを行います。極めて最新のデータが不要であれば、これを有効にすることでスクレイピングを最大500%高速化できます。デフォルトは2日です。

設定すると、このリクエストはキャッシュのみを確認し、新しいスクレイプは実行されません。値はミリ秒単位で、キャッシュデータに必要な最小経過時間を指定します。一致するキャッシュデータが存在する場合は、即座に返されます。キャッシュデータが見つからない場合は、エラーコード SCRAPE\_NO\_CACHED\_DATA を含む 404 が返されます。経過時間に関係なく、任意のキャッシュデータを許可するには 1 に設定します。

リクエストに含めるヘッダー。Cookie や User-Agent などを送信するために使用できます。

コンテンツを取得する前に待機する時間をミリ秒単位で指定します。ページが十分に読み込まれるまでの時間を確保するための遅延です。この待機時間は、Firecrawl のスマート待機機能に加えて発生します。

モバイル端末からのスクレイピングをエミュレートしたい場合は、true に設定します。レスポンシブページのテストやモバイル向けスクリーンショットの取得に便利です。

リクエストを送信する際に TLS 証明書の検証を行わないようにします。

リクエストのタイムアウト時間をミリ秒単位で指定します。最小値は 1000（1 秒）です。デフォルト値は 30000（30 秒）です。最大値は 300000（300 秒）です。

必須範囲: `1000 <= x <= 300000`

スクレイピング時のファイルの処理方法を制御します。"pdf" が含まれている場合（デフォルト）、PDF の内容が抽出されて markdown 形式に変換され、課金はページ数に基づきます（1ページあたり1クレジット）。空の配列を渡した場合、PDF ファイルは base64 エンコード形式で返され、PDF 全体で一律1クレジットが請求されます。

actions

(Wait by Duration · object | Wait for Element · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

コンテンツを取得する前にページに対して実行するアクション

- Wait by Duration
- Wait for Element
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

リクエストのロケーション設定です。指定すると、利用可能な場合は適切なプロキシが使用され、対応する言語およびタイムゾーン設定がエミュレートされます。指定されていない場合は、デフォルトで「US」が使用されます。

markdown 出力からすべての Base64 画像を削除します。長くなりすぎる可能性があるためです。これは html または rawHtml フォーマットには影響しません。画像の代替テキストは出力に残りますが、URL はプレースホルダーに置き換えられます。

広告およびCookie同意ポップアップのブロックを有効化します。

使用するプロキシの種類を指定します。

- basic: ボット対策がない、または基本的なボット対策のみを行っているサイト向けのプロキシです。高速で、多くのケースではこれで十分です。
- enhanced: 高度なボット対策を行っているサイト向けの強化プロキシです。basic よりは遅くなりますが、一部のサイトではより高い成功率が期待できます。1 リクエストあたり最大 5 クレジット消費します。
- auto: basic プロキシでのスクレイピングに失敗した場合、Firecrawl が自動的に enhanced プロキシで再試行します。enhanced での再試行が成功した場合、そのスクレイプには 5 クレジットが課金されます。最初の basic で成功した場合は、通常のコストのみが課金されます。

利用可能なオプション:

`basic`,

`enhanced`,

`auto`

true の場合、そのページは Firecrawl のインデックスおよびキャッシュに保存されます。スクレイピング活動でデータ保護上の懸念が生じる可能性がある場合は、これを false に設定すると有用です。機密性の高いスクレイピングに関連する一部のパラメータ（例: actions、headers）を使用すると、このパラメータは強制的に false になります。

true の場合、このバッチスクレイプではゼロデータ保持が有効になり、データは一切保持されません。この機能を有効にするには、[help@firecrawl.dev](mailto:help@firecrawl.dev) までご連絡ください。

#### レスポンス

ignoreInvalidURLs が true の場合、このフィールドは、リクエスト内で指定された無効な URL を含む配列になります。無効な URL がなかった場合、この配列は空になります。ignoreInvalidURLs が false の場合、このフィールドは undefined になります。