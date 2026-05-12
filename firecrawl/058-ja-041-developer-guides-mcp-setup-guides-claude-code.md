---
title: Claude Code での MCP によるウェブ検索とスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/mcp-setup-guides/claude-code
source: sitemap
fetched_at: 2026-03-23T07:29:19.74862-03:00
rendered_js: false
word_count: 41
summary: This document provides instructions on how to integrate Firecrawl's MCP server with Claude Code to enable web searching and scraping capabilities.
tags:
    - firecrawl
    - claude-code
    - mcp-server
    - web-scraping
    - api-integration
category: guide
---

Firecrawl の MCP を使って、Claude Code にウェブ検索とスクレイピング機能を追加します。

## クイックセットアップ

### 1. APIキーを取得する

[firecrawl.dev/app](https://firecrawl.dev/app) にサインアップし、APIキーをコピーします。

### 2. Firecrawl MCP サーバーの追加

**オプション A: リモートでホストされた URL (推奨)**

```
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp
```

**オプション B: ローカル (npx)**

```
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

`your-api-key` を実際の Firecrawl API キーに置き換えてください。 完了です！これで Claude Code からウェブを検索・スクレイピングできます。

## クイックデモ

Claude Codeで以下を試してください: **ウェブを検索する:**

```
Search for the latest Next.js 15 features
```

**ページをスクレイピングする:**

```
Scrape firecrawl.dev and tell me what it does
```

**ドキュメントを取得:**

```
Find and scrape the Stripe API docs for payment intents
```

Claude は、情報を取得するために Firecrawl の検索ツールとスクレイピングツールを自動的に使用します。