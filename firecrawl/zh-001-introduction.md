---
title: 快速上手 | Firecrawl
url: https://docs.firecrawl.dev/zh/introduction
source: sitemap
fetched_at: 2026-03-23T07:30:12.737336-03:00
rendered_js: false
word_count: 109
summary: This document provides an introduction to Firecrawl, an API service designed to convert websites into clean, LLM-ready data formats through scraping, searching, and agent-based browsing.
tags:
    - web-scraping
    - llm-data
    - data-extraction
    - ai-agents
    - browser-automation
    - api-documentation
    - markdown-conversion
category: guide
---

## 抓取你的第一个网站

只需一次 API 调用，就能将任意网站转换为干净、适配 LLM 的数据。

### 将 Firecrawl 与 AI 智能体配合使用 (推荐)

Firecrawl 技能是让智能体发现并使用 Firecrawl 的最快方式。否则，你的智能体不会知道可以使用 Firecrawl。

```
npx -y firecrawl-cli@latest init --all --browser
```

也可以使用 [MCP Server](https://docs.firecrawl.dev/zh/mcp-server) 将 Firecrawl 直接连接到 Claude、Cursor、Windsurf、VS Code 等其他 AI 工具。

### 发出你的第一个请求

复制下方的代码，将 `fc-YOUR-API-KEY` 替换为你的 API 密钥，然后运行：

示例响应

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

### 为什么选择 Firecrawl？

- **适用于 LLM 的输出**：获取干净的 markdown、结构化 JSON、截图等多种格式
- **处理好繁琐细节**：代理、反机器人/反爬机制、JavaScript 渲染和动态内容
- **可靠**：为生产环境打造，高可用且结果稳定一致
- **快速**：数秒内返回结果，并针对高吞吐场景进行了优化
- **浏览器沙箱**：为智能体提供全托管浏览器环境，零配置，可按任意规模扩展
- **MCP Server**：通过 [Model Context Protocol](https://docs.firecrawl.dev/zh/mcp-server) 将 Firecrawl 连接到任意 AI 工具

* * *

## 抓取

抓取任意 URL，并以 markdown、HTML 或其他 formats 形式获取其内容。所有选项请参阅 [Scrape 功能文档](https://docs.firecrawl.dev/zh/features/scrape)。

响应

各 SDK 将直接返回数据对象。cURL 将按下方所示原样返回有效载荷。

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I 开始了！[查看我们第 2 天的发布 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 获享 2 个月免费...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "首页 - Firecrawl",
      "description": "Firecrawl 可抓取并将任何网站转换为干净的 Markdown。",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "将任意网站转换为可直接用于 LLM 的数据。",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## 搜索

Firecrawl 的搜索 API 支持你进行网页搜索，并可在一次操作中可选地抓取搜索结果。

- 选择特定输出格式 (Markdown、HTML、链接、截图)
- 选择特定来源 (网页、新闻、图片)
- 通过可自定义参数 (如位置等) 进行网页搜索

详见[Search Endpoint API Reference](https://docs.firecrawl.dev/zh/api-reference/endpoint/search)。

响应

SDK 会直接返回数据对象。cURL 会返回完整的 payload。

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - 面向 AI 的 Web 数据 API",
        "description": "用于 AI 的网页爬取、抓取与搜索 API。为规模而建。Firecrawl 将整个互联网送达 AI 代理与开发者。",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl：将整站转换为可供 LLM 使用的内容 - GitHub",
        "description": "Firecrawl 是一项 API 服务，接收一个 URL，对其进行爬取，并将其转换为干净的 Markdown 或结构化数据。",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "快速上手 | Firecrawl",
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
        "title": "Y Combinator 创业公司 Firecrawl 准备出资 100 万美元雇用三名 AI 代理作为员工",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "目前它在 YC 的招聘板发布了三则"仅限 AI 代理"的新职位，并为此预留了总计 100 万美元的预算。",
        "date": "3 个月前",
        "position": 1
      },
      ...
    ]
  }
}
```

## 智能体

Firecrawl 的智能体是一个自动化的网页数据采集工具。你只需描述你需要的数据，它就会在整个网络中进行搜索、导航，并从中提取这些数据。请查看 [Agent 功能文档](https://docs.firecrawl.dev/zh/features/agent) 以了解所有选项。

示例响应

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

## 浏览器

Firecrawl 浏览器沙箱为您的智能体提供安全的浏览器环境，以便与 Web 交互。可填写表单、点击按钮、进行身份验证等。无需本地配置或安装 Chromium。完整文档请参阅 [Browser 功能文档](https://docs.firecrawl.dev/zh/features/browser)。

示例响应

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

## 资源