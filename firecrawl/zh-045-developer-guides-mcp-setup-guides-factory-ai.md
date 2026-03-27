---
title: 在 Factory AI 中使用 MCP 进行网页搜索与爬取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/mcp-setup-guides/factory-ai
source: sitemap
fetched_at: 2026-03-23T07:33:55.169046-03:00
rendered_js: false
word_count: 64
summary: This document provides instructions on how to integrate the Firecrawl MCP server into Factory AI to enable web scraping and search capabilities.
tags:
    - factory-ai
    - firecrawl
    - mcp-server
    - web-scraping
    - api-integration
    - automation
category: guide
---

使用 Firecrawl MCP 为 Factory AI 接入网页爬取与搜索功能。

## 快速开始

### 1. 获取你的 API 密钥

在 [firecrawl.dev/app](https://firecrawl.dev/app) 注册并复制你的 API 密钥。

### 2. 安装 Factory AI CLI

如果尚未安装，请先安装 [Factory AI CLI](https://docs.factory.ai/cli/getting-started/quickstart)： **macOS/Linux：**

```
curl -fsSL https://app.factory.ai/cli | sh
```

**Windows：**

```
iwr https://app.factory.ai/cli/install.ps1 -useb | iex
```

### 3. 添加 Firecrawl MCP Server

在 Factory droid CLI 中，通过 `/mcp add` 命令添加 Firecrawl：

```
/mcp add firecrawl "npx -y firecrawl-mcp" -e FIRECRAWL_API_KEY=your-api-key-here
```

将 `your-api-key-here` 替换成你自己的 Firecrawl API 密钥。

### 4. 完成！

现在可以在 Factory AI 会话中使用 Firecrawl 工具了！

## 快速演示

在 Factory AI 中试试以下操作： **搜索全网：**

**抓取页面：**

```
抓取 firecrawl.dev 并告诉我它是做什么的
```

**查看文档：**

```
查找并抓取 Stripe API 文档中的 Payment Intents 部分
```

Factory 将自动借助 Firecrawl 的搜索与抓取工具获取信息。