---
title: Cursor での MCP のウェブ検索とスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/mcp-setup-guides/cursor
source: sitemap
fetched_at: 2026-03-23T07:32:16.955605-03:00
rendered_js: false
word_count: 77
summary: This document provides instructions on how to integrate the Firecrawl MCP server into the Cursor IDE to enable web scraping and search capabilities directly within the chat interface.
tags:
    - firecrawl
    - cursor-ide
    - mcp
    - web-scraping
    - ai-assistant
    - developer-tools
    - configuration
category: configuration
---

Firecrawl の MCP を使って、Cursor にウェブスクレイピングと検索機能を追加します。

## かんたんセットアップ

### 1. APIキーを取得

[firecrawl.dev/app](https://firecrawl.dev/app) にサインアップして、APIキーをコピーします。

### 2. Cursor に追加

設定（`Cmd+,`）を開き、「MCP」を検索して、以下を追加します：

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

`your_api_key_here` を実際の Firecrawl API キーに置き換えてください。

### 3. Cursor を再起動する

完了です！これで Cursor から Web を検索してスクレイピングできるようになりました。

## クイックデモ

Cursor Chat（`Cmd+K`）で試してみてください： **検索：**

```
TypeScript ベストプラクティス 2025 を検索
```

**スクレイピング：**

```
firecrawl.devをスクレイピングして、その機能を教えて
```

**ドキュメントを取得:**

```
React hooksのドキュメントをスクレイピングし、useEffectについて説明してください
```

Cursor は Firecrawl のツールを自動で使用します。

## Windows でのトラブルシューティング

Windows で `spawn npx ENOENT` または “No server info found” エラーが表示される場合、Cursor が PATH 内の `npx` を見つけられていません。次のいずれかの方法を試してください: **オプション A: `npx.cmd` のフルパスを使う** コマンド プロンプトで `where npx` を実行してフルパスを取得し、そのパスで設定を更新します:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

`command` のパスを、`where npx` の出力結果に置き換えてください。 **オプション B: リモートホストされた URL を使用する（Node.js は不要）**

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/YOUR-API-KEY/v2/mcp"
    }
  }
}
```

`YOUR-API-KEY` を Firecrawl の API キーに置き換えてください。