---
title: 在 Claude Code 中使用 MCP 进行网页搜索和抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/mcp-setup-guides/claude-code
source: sitemap
fetched_at: 2026-03-23T07:29:10.274041-03:00
rendered_js: false
word_count: 49
summary: This document provides instructions on how to integrate the Firecrawl MCP server with Claude Code to enable web searching and scraping capabilities.
tags:
    - claude-code
    - firecrawl
    - mcp-server
    - web-scraping
    - search-integration
    - ai-tools
category: tutorial
---

使用 Firecrawl MCP 为 Claude Code 添加网页抓取和搜索能力。

## 快速开始

### 1. 获取你的 API 密钥

在 [firecrawl.dev/app](https://firecrawl.dev/app) 注册并复制你的 API 密钥。

### 2. 添加 Firecrawl MCP 服务器

**选项 A：远程托管 URL (推荐)**

```
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp
```

**选项 B：本地 (npx)**

```
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

将 `your-api-key` 替换为你的实际 Firecrawl API 密钥。 完成！现在你可以在 Claude Code 中搜索并抓取网页了。

## 快速演示

在 Claude Code 中试试这些： **搜索网页：**

```
Search for the latest Next.js 15 features
```

**抓取网页：**

```
Scrape firecrawl.dev and tell me what it does
```

**查看文档：**

```
Find and scrape the Stripe API docs for payment intents
```

Claude 会自动使用 Firecrawl 的搜索和抓取工具来获取相关信息。