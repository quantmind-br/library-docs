---
title: スクレイプ - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/scrape
source: sitemap
fetched_at: 2026-03-23T07:12:09.917819-03:00
rendered_js: false
word_count: 162
summary: This document describes the request parameters and configuration options for an API endpoint designed to scrape web content and optionally extract information using LLMs.
tags:
    - web-scraping
    - api-documentation
    - data-extraction
    - proxy-configuration
    - content-format
category: api
---

1つのURLをスクレイピングし、必要に応じてLLMを使って情報を抽出する

> 注記: 機能とパフォーマンスが向上した本 API の新しい [v2 バージョン](https://docs.firecrawl.dev/ja/api-reference/endpoint/scrape) が利用可能です。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

ヘッダー、ナビゲーション、フッターなどを除き、ページのメインコンテンツのみを返します。

ページのキャッシュが、このミリ秒数以内に生成されたものであれば、そのキャッシュされたバージョンを返します。キャッシュされたページがこの値より古い場合は、ページをスクレイピングします。極めて最新のデータが不要な場合、これを有効にすることでスクレイピングを最大 500% 高速化できます。デフォルトは 0 で、この場合キャッシュは無効になります。

リクエストに付与して送信するヘッダー。Cookie や User-Agent などを送るために使用できます。

コンテンツを取得する前に待機する時間（ディレイ）をミリ秒単位で指定します。これにより、ページが十分に読み込まれるまでの時間を確保できます。

モバイル端末からのスクレイピングを模擬したい場合は true に設定してください。レスポンシブページのテストやモバイル画面のスクリーンショット取得に便利です。

リクエスト時に TLS 証明書の検証をスキップする

スクレイピング中のPDFファイルの処理方法を制御します。true の場合、PDFのコンテンツを抽出してMarkdown形式に変換し、課金はページ数に基づきます（1ページあたり1クレジット）。false の場合、PDFファイルはbase64エンコードされたデータとして返され、合計1クレジットの定額課金となります。

actions

(Wait · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

ページからコンテンツを取得する前に実行するアクション

- Wait
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

リクエストに対するロケーション設定です。指定されている場合、利用可能であれば適切なプロキシを使用し、対応する言語およびタイムゾーン設定を再現します。指定されていない場合は、デフォルトで 'US' が使用されます。

出力から、非常に長くなりがちな Base64 画像をすべて削除します。画像の alt テキストは出力内に残りますが、URL はプレースホルダーに置き換えられます。

広告とクッキーポップアップのブロックを有効にします。

使用するプロキシの種類を指定します。

- basic: ボット対策がない、または基本的なボット対策のみが導入されているサイト向けのプロキシです。高速で、ほとんどの場合はこれで十分です。
- enhanced: 高度なボット対策が導入されているサイト向けの強化プロキシです。速度は遅くなりますが、特定のサイトではより信頼性があります。1 リクエストあたり最大 5 クレジット消費します。
- auto: basic プロキシでのスクレイピングが失敗した場合に、Firecrawl が自動的に enhanced プロキシで再試行します。enhanced での再試行が成功した場合、そのスクレイピングには 5 クレジットが請求されます。最初の basic での試行が成功した場合は、通常どおりのコストのみが請求されます。

プロキシを指定しない場合、Firecrawl はデフォルトで basic を使用します。

利用可能なオプション:

`basic`,

`enhanced`,

`auto`

true の場合、そのページは Firecrawl のインデックスおよびキャッシュに保存されます。スクレイピング内容がデータ保護上の懸念を伴う可能性がある場合は、これを false に設定するのが有効です。機密性の高いスクレイピングに関連する一部のパラメータ（アクションやヘッダーなど）を使用すると、このパラメータは強制的に false に設定されます。

出力に含めるフォーマット。

利用可能なオプション:

`markdown`,

`html`,

`rawHtml`,

`links`,

`screenshot`,

`screenshot@fullPage`,

`json`,

`changeTracking`

変更追跡用のオプション（ベータ版）。changeTracking がフォーマットに含まれている場合にのみ有効です。変更追跡を使用する際は、markdown フォーマットも指定する必要があります。

true の場合、このスクレイプではデータを一切保持しないゼロデータ保持モードが有効になります。この機能を有効にするには、[help@firecrawl.dev](mailto:help@firecrawl.dev) までご連絡ください。

#### レスポンス