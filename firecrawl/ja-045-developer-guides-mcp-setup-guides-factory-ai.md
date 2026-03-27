---
title: Factory AI での MCP Web検索とスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/mcp-setup-guides/factory-ai
source: sitemap
fetched_at: 2026-03-23T07:35:18.721202-03:00
rendered_js: false
word_count: 52
summary: This document provides instructions on how to integrate the Firecrawl MCP server with Factory AI to enable web scraping and search capabilities.
tags:
    - firecrawl
    - factory-ai
    - mcp-server
    - web-scraping
    - api-integration
    - automation
category: guide
---

Firecrawl の MCP を使って、Factory AI にウェブスクレイピングと検索機能を追加します。

## クイックセットアップ

### 1. APIキーを取得する

[firecrawl.dev/app](https://firecrawl.dev/app) に登録し、APIキーをコピーします。

### 2. Factory AI CLI をインストールする

まだインストールしていない場合は、[Factory AI CLI](https://docs.factory.ai/cli/getting-started/quickstart) をインストールしてください： **macOS/Linux:**

```
curl -fsSL https://app.factory.ai/cli | sh
```

**Windows（ウィンドウズ）:**

```
iwr https://app.factory.ai/cli/install.ps1 -useb | iex
```

### 3. Firecrawl MCP Server を追加

Factory droid CLI で `/mcp add` コマンドを実行して、Firecrawl を追加します：

```
/mcp add firecrawl "npx -y firecrawl-mcp" -e FIRECRAWL_API_KEY=your-api-key-here
```

`your-api-key-here` をご自身の Firecrawl API キーに置き換えてください。

### 4. 完了！

これで Firecrawl ツールが Factory AI のセッション内で利用できるようになりました！

## クイックデモ

Factory AI で試してみましょう: **ウェブ検索:**

**ページをスクレイピングする:**

```
firecrawl.devをスクレイピングして、その機能を教えて
```

**ドキュメントを入手:**

```
Stripe API ドキュメントから payment intents を検索してスクレイピングする
```

Factoryは情報を取得するためにFirecrawlの検索・スクレイプツールを自動的に使用します。