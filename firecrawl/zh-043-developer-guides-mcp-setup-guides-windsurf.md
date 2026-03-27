---
title: 在 Windsurf 中使用 MCP 实现网页搜索与抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/mcp-setup-guides/windsurf
source: sitemap
fetched_at: 2026-03-23T07:33:58.559283-03:00
rendered_js: false
word_count: 50
summary: This document provides instructions on how to integrate the Firecrawl MCP server into the Windsurf IDE to enable automated web crawling and search capabilities.
tags:
    - web-scraping
    - windsurf
    - mcp-server
    - firecrawl
    - ide-integration
    - ai-agents
category: configuration
---

使用 Firecrawl MCP 为 Windsurf 添加网页抓取与搜索功能。

## [​](#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B) 快速开始

### [​](#1-%E8%8E%B7%E5%8F%96%E4%BD%A0%E7%9A%84-api-%E5%AF%86%E9%92%A5) 1. 获取你的 API 密钥

在 [firecrawl.dev/app](https://firecrawl.dev/app) 注册并复制你的 API 密钥。

### [​](#2-%E6%B7%BB%E5%8A%A0%E5%88%B0-windsurf) 2. 添加到 Windsurf

将以下内容添加到你的 `./codeium/windsurf/model_config.json`：

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

将 `YOUR_API_KEY` 替换为你的实际 Firecrawl API 密钥。

### [​](#3-%E9%87%8D%E5%90%AF-windsurf) 3. 重启 Windsurf

完成！Windsurf 现在可以搜索并爬取网站数据了。

## [​](#%E5%BF%AB%E9%80%9F%E6%BC%94%E7%A4%BA) 快速演示

在 Windsurf 中试试以下内容： **搜索：**

```
搜索最新的 Tailwind CSS 功能
```

**爬取：**

```
抓取 firecrawl.dev 并说明其作用
```

**获取文档：**

```
查找并抓取 Supabase 身份验证文档
```

Windsurf 的 AI 代理将自动调用 Firecrawl 工具。