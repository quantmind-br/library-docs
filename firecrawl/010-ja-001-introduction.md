---
title: クイックスタート | Firecrawl
url: https://docs.firecrawl.dev/ja/introduction
source: sitemap
fetched_at: 2026-03-23T07:30:25.867027-03:00
rendered_js: false
word_count: 102
summary: This document provides an overview of the Firecrawl API, explaining how to perform web scraping, search, agent-driven data extraction, and browser automation to convert website content into LLM-ready formats.
tags:
    - web-scraping
    - ai-agents
    - data-extraction
    - markdown-conversion
    - browser-automation
    - api-integration
category: guide
---

## 最初のウェブサイトをスクレイピングする

任意のウェブサイトを、1 回の API コールでクリーンな LLM 向けデータに変換できます。

### AIエージェントでFirecrawlを使う (推奨)

Firecrawlスキルは、エージェントがFirecrawlを見つけて利用できるようにする最速の方法です。これがない場合、エージェントはFirecrawlが利用可能であることを認識できません。

```
npx -y firecrawl-cli@latest init --all --browser
```

または [MCP Server](https://docs.firecrawl.dev/ja/mcp-server) を使用して、Firecrawl を Claude、Cursor、Windsurf、VS Code などの AI ツールに直接接続することもできます。

### 最初のリクエストを送信する

以下のコードをコピーし、`fc-YOUR-API-KEY` を自分の API キーに置き換えて実行してください:

レスポンス例

```
{
  "success": true,
  "data": {
    "markdown": "# Example Domain\n\nThis domain is for use in illustrative examples...",
    "metadata": {
      "title": "Example Domain",
      "sourceURL": "https://example.com"
    }
  }
}
```

* * *

### なぜ Firecrawl なのか？

- **LLM 向けの出力**: クリーンな Markdown、構造化 JSON、スクリーンショットなどを生成
- **面倒な処理もまとめて対応**: プロキシ、ボット対策、JavaScript レンダリング、動的コンテンツまでカバー
- **高い信頼性**: プロダクション向けに構築されており、高い稼働率と一貫した結果を提供
- **高速**: 秒単位で結果を返し、高スループット向けに最適化
- **ブラウザサンドボックス**: エージェント向けの完全マネージドなブラウザ環境で、設定不要・任意の規模にスケール可能
- **MCP Server**: [Model Context Protocol](https://docs.firecrawl.dev/ja/mcp-server) 経由で、任意の AI ツールに Firecrawl を接続

* * *

## スクレイピング

任意のURLをスクレイプして、そのコンテンツをMarkdown、HTML、その他さまざまなフォーマットで取得できます。すべてのオプションについては [Scrape 機能ドキュメント](https://docs.firecrawl.dev/ja/features/scrape) を参照してください。

レスポンス

SDKはデータオブジェクトを直接返します。cURLは以下のとおり、ペイロードをそのまま返します。

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I が開幕！[2日目のリリースを見る 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 2か月無料をゲット...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "ホーム - Firecrawl",
      "description": "Firecrawl は、あらゆるウェブサイトをクリーンな Markdown にクロールして変換します。",
      "language": "en",
      "keywords": "Firecrawl,Markdown,データ,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "あらゆるウェブサイトを LLM で使えるデータに変換。",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl"
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## Search

Firecrawl の検索APIを使うと、ウェブ検索と、必要に応じた検索結果のスクレイピングを1回の操作で実行できます。

- 出力フォーマット (markdown、HTML、links、screenshots) を選択
- 取得元のソース (web、news、images) を選択
- カスタマイズ可能なパラメータ (location など) でウェブを検索

詳細は [Search Endpoint API Reference](https://docs.firecrawl.dev/ja/api-reference/endpoint/search) を参照してください。

レスポンス

SDK は `data` オブジェクトをそのまま返します。cURL では完全なペイロードが返されます。

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - AI向けWebデータAPI",
        "description": "AI向けのウェブクローリング、スクレイピング、検索API。大規模運用に対応。Firecrawlはインターネット全体をAIエージェントやビルダーに提供します。",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

## Agent

Firecrawl の Agent は、自律的なウェブデータ収集ツールです。必要なデータを自然文で指示するだけで、ウェブ上を検索・移動し、任意のサイトからデータを抽出します。利用可能なオプションの詳細は [Agent 機能ドキュメント](https://docs.firecrawl.dev/ja/features/agent) を参照してください。

レスポンス例

```
{
  "success": true,
  "data": {
    "result": "Notion offers the following pricing plans:\n\n1. **Free** - $0/month - For individuals...\n2. **Plus** - $10/seat/month - For small teams...\n3. **Business** - $18/seat/month - For companies...\n4. **Enterprise** - Custom pricing - For large organizations...",
    "sources": [
      "https://www.notion.so/pricing"
    ]
  }
}
```

## Browser

Firecrawl ブラウザサンドボックスは、エージェントがウェブと安全にやり取りできるブラウザ環境を提供します。フォームへの入力、ボタンのクリック、認証などを実行できます。ローカルでのセットアップや Chromium のインストールは不要です。完全なドキュメントについては、[Browser の機能ドキュメント](https://docs.firecrawl.dev/ja/features/browser)を参照してください。

レスポンス例

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-...",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-...?interactive=true"
}
```

* * *

## リソース