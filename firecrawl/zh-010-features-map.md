---
title: Map | Firecrawl
url: https://docs.firecrawl.dev/zh/features/map
source: sitemap
fetched_at: 2026-03-23T07:20:38.069886-03:00
rendered_js: false
word_count: 81
summary: This document explains how to use the Firecrawl /map endpoint to generate a list of URLs from a website using sitemaps, search results, and cached data.
tags:
    - web-scraping
    - api-documentation
    - url-mapping
    - site-indexing
    - firecrawl-api
    - web-crawling
category: api
---

从单个 URL 快速生成整站链接地图的最简方式。这在以下场景特别有用：

- 需要让终端用户选择要抓取的链接时
- 需要快速了解网站包含哪些链接
- 需要抓取与特定主题相关的页面 (使用 `search` 参数)
- 只需抓取网站中的特定页面

## 映射

### /map 端点

用于映射一个 URL 并获取该网站的 URL。会返回站点上大部分的链接。 URL 主要从网站的 sitemap 中获取，并辅以 SERP (搜索引擎结果页) 结果和之前抓取的页面，以提升覆盖率。你可以使用 `sitemap` 参数来控制 sitemap 的行为。

### 安装

### 使用方法

### 响应

SDK 会直接返回数据对象。cURL 会按下方所示原样返回负载。

```
{
  "success": true,
  "links": [
    {
      "url": "https://docs.firecrawl.dev/features/scrape",
      "title": "Scrape | Firecrawl",
      "description": "将任意 URL 转换为干净的数据",
    },
    {
      "url": "https://www.firecrawl.dev/blog/5_easy_ways_to_access_glm_4_5",
      "title": "访问 GLM-4.5 的 5 种简单方式",
      "description": "了解如何在本地、通过聊天应用、通过官方 API，以及借助 LLM 市场 API 实现无缝集成地访问 GLM-4.5 模型……",
    },
    {
      "url": "https://www.firecrawl.dev/playground",
      "title": "Playground - Firecrawl",
      "description": "预览 API 响应并获取该 API 的代码片段",
    },
    {
      "url": "https://www.firecrawl.dev/?testId=2a7e0542-077b-4eff-bec7-0130395570d6",
      "title": "Firecrawl - 面向 AI 的 Web 数据 API",
      "description": "面向 AI 的网页爬取、抓取与搜索 API，面向规模而构建。Firecrawl 为 AI 代理与构建者提供全网数据：干净、结构化，并且……",
    },
    {
      "url": "https://www.firecrawl.dev/?testId=af391f07-ca0e-40d3-8ff2-b1ecf2e3fcde",
      "title": "Firecrawl - 面向 AI 的 Web 数据 API",
      "description": "面向 AI 的网页爬取、抓取与搜索 API，面向规模而构建。Firecrawl 为 AI 代理与构建者提供全网数据：干净、结构化，并且……"
    },
    ...
  ]
}
```

#### 带搜索参数的 Map

使用 `search` 参数的 Map 可在站内搜索特定的 URL。

```
curl -X POST https://api.firecrawl.dev/v2/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "url": "https://firecrawl.dev",
    "search": "docs"
  }'
```

响应将按相关性从高到低返回一个有序列表。

```
{
  "status": "success",
  "links": [
    {
      "url": "https://docs.firecrawl.dev",
      "title": "Firecrawl 文档",
      "description": "Firecrawl 文档"
    },
    {
      "url": "https://docs.firecrawl.dev/sdks/python",
      "title": "Firecrawl Python SDK",
      "description": "Firecrawl Python SDK 文档"
    },
    ...
  ]
}
```

## 位置与语言

指定国家和首选语言，根据你的目标位置与语言偏好获取更相关的内容，方式与 /scrape 端点相似。

### 工作原理

当你指定位置设置时，Firecrawl 会在可用时使用合适的代理，并模拟相应的语言和时区设置。默认情况下，若未指定，位置将设为“US”。

### 用法

要配置位置和语言，请在请求体中包含 `location` 对象，并设置以下属性：

- `country`：ISO 3166-1 alpha-2 国家代码 (如 ‘US’、‘AU’、‘DE’、‘JP’) 。默认值为 ‘US’。
- `languages`：按优先级排序的首选语言与区域设置数组。默认使用所设位置的语言。

有关支持的地区与位置的更多信息，请参见 [Proxies 文档](https://docs.firecrawl.dev/zh/features/proxies)。

## 注意事项

该端点优先考虑速度，因此可能无法捕获所有网站链接。它主要依赖网站的 sitemap，并结合缓存的爬取数据和搜索引擎结果。若需要更全面且最新的 URL 列表，请考虑改用 [/crawl](https://docs.firecrawl.dev/zh/features/crawl) 端点。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化接入说明。