---
title: Map | Firecrawl
url: https://docs.firecrawl.dev/ja/features/map
source: sitemap
fetched_at: 2026-03-23T07:23:08.791904-03:00
rendered_js: false
word_count: 70
summary: This document explains how to use the Firecrawl /map endpoint to quickly retrieve and filter a list of URLs from a website, leveraging sitemaps and search engine data.
tags:
    - web-scraping
    - site-mapping
    - url-discovery
    - api-documentation
    - data-extraction
category: api
---

単一のURLからウェブサイト全体のマップを素早く取得する最も簡単な方法です。次の用途に非常に有用です:

- エンドユーザーに、どのリンクをスクレイプするか選んでもらう必要があるとき
- サイト上のリンクをすぐに把握したいとき
- 特定のトピックに関連するページだけをスクレイプしたいとき (`search` パラメータを使用)
- サイトの特定ページだけをスクレイプすればよいとき

## マッピング

### /map エンドポイント

URL をマッピングし、サイト内の URL を取得するために使用します。サイト上に存在するリンクの大部分を返します。 URL は主にウェブサイトのサイトマップから検出され、カバレッジを向上させるために SERP (検索エンジン) の結果および以前にクロールされたページによって補完されます。`sitemap` パラメータでサイトマップの動作を制御できます。

### インストール

### 使い方

### レスポンス

SDKはデータオブジェクトを直接返します。cURLは下記のとおり、ペイロードをそのまま返します。

```
{
  "success": true,
  "links": [
    {
      "url": "https://docs.firecrawl.dev/features/scrape",
      "title": "スクレイプ | Firecrawl",
      "description": "あらゆるURLをクリーンなデータに変換",
    },
    {
      "url": "https://www.firecrawl.dev/blog/5_easy_ways_to_access_glm_4_5",
      "title": "GLM-4.5にアクセスする簡単な5つの方法",
      "description": "GLM-4.5モデルにローカル、チャットアプリ、公式API、そしてLLMマーケットプレイスAPIを通じてシームレスに統合する方法を解説...",
    },
    {
      "url": "https://www.firecrawl.dev/playground",
      "title": "Playground - Firecrawl",
      "description": "APIレスポンスをプレビューし、API用コードスニペットを取得",
    },
    {
      "url": "https://www.firecrawl.dev/?testId=2a7e0542-077b-4eff-bec7-0130395570d6",
      "title": "Firecrawl - AI向けWebデータAPI",
      "description": "AI向けのウェブクロール・スクレイプ・検索API。大規模運用に対応。Firecrawlはインターネット全体をAIエージェントとビルダーに提供。クリーンで構造化されたデータを...",
    },
    {
      "url": "https://www.firecrawl.dev/?testId=af391f07-ca0e-40d3-8ff2-b1ecf2e3fcde",
      "title": "Firecrawl - AI向けWebデータAPI",
      "description": "AI向けのウェブクロール・スクレイプ・検索API。大規模運用に対応。Firecrawlはインターネット全体をAIエージェントとビルダーに提供。クリーンで構造化されたデータを..."
    },
    ...
  ]
}
```

#### 検索付きのマップ

`search` パラメータを使うと、サイト内の特定のURLを検索できます。

```
curl -X POST https://api.firecrawl.dev/v2/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "url": "https://firecrawl.dev",
    "search": "docs"
  }'
```

返答は、関連性の高い順に並べた番号付きリストで提供されます。

```
{
  "status": "success",
  "links": [
    {
      "url": "https://docs.firecrawl.dev",
      "title": "Firecrawl ドキュメント",
      "description": "Firecrawl ドキュメント",
    },
    {
      "url": "https://docs.firecrawl.dev/sdks/python",
      "title": "Firecrawl Python SDK",
      "description": "Firecrawl Python SDK ドキュメント"
    },
    ...
  ]
}
```

## 位置と言語

対象の地域と言語の優先度に基づいて関連コンテンツを取得するため、国と言語の優先設定を指定します。/scrape エンドポイントと同様です。

### 仕組み

ロケーション設定を指定すると、Firecrawl は (利用可能であれば) 適切なプロキシを使用し、対応する言語とタイムゾーン設定をエミュレートします。指定がない場合、ロケーションは既定で「US」になります。

### 使用方法

位置情報と言語設定を利用するには、リクエストボディに `location` オブジェクトを含め、次のプロパティを指定してください。

- `country`: ISO 3166-1 alpha-2 の国コード (例: ‘US’、‘AU’、‘DE’、‘JP’) 。デフォルトは ‘US’ です。
- `languages`: リクエストで優先する言語・ロケールの配列 (優先順) 。デフォルトは指定した国・地域の言語です。

対応している国・地域の詳細は、[プロキシのドキュメント](https://docs.firecrawl.dev/ja/features/proxies)を参照してください。

## 留意事項

このエンドポイントは速度を優先しているため、Web サイト上のリンクをすべて取得できない場合があります。主に Web サイトのサイトマップを使用し、キャッシュ済みのクロールデータや検索エンジンの結果で補完しています。より網羅的かつ最新の URL リストが必要な場合は、代わりに [/crawl](https://docs.firecrawl.dev/ja/features/crawl) エンドポイントを使用することをご検討ください。

> Firecrawl API キーが必要な AI エージェントですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) をご覧ください。