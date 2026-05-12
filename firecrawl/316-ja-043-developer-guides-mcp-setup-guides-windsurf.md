---
title: Windsurf での MCP Web 検索とスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/mcp-setup-guides/windsurf
source: sitemap
fetched_at: 2026-03-23T07:35:06.48268-03:00
rendered_js: false
word_count: 34
summary: This document provides instructions on integrating the Firecrawl MCP server into the Windsurf environment to enable automated web scraping and search capabilities.
tags:
    - windsurf
    - firecrawl
    - mcp-server
    - web-scraping
    - ai-development
    - configuration
category: configuration
---

Firecrawl MCP を使って、Windsurf に Web スクレイピングと検索機能を追加します。

## かんたんセットアップ

### 1. APIキーを取得する

[firecrawl.dev/app](https://firecrawl.dev/app) に登録し、APIキーをコピーします。

### 2. Windsurf に追加

次を `./codeium/windsurf/model_config.json` に追加してください:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

`YOUR_API_KEY` を実際の Firecrawl API キーに置き換えてください。

### 3. Windsurf を再起動する

完了です！これで Windsurf で Web の検索とスクレイピングができるようになりました。

## クイックデモ

Windsurf で試してみてください： **検索：**

**スクレイピング：**

```
firecrawl.dev をスクレイピングして、その機能を説明する
```

**ドキュメントを取得:**

```
Supabase認証ドキュメントを検索してスクレイピング
```

WindsurfのAIエージェントは、Firecrawlのツールを自動で利用します。