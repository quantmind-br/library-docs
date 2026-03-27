---
title: 搜索 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/search
source: sitemap
fetched_at: 2026-03-23T07:20:27.590062-03:00
rendered_js: false
word_count: 318
summary: This document describes the Firecrawl Search API, which enables users to perform web, news, and image searches with support for content scraping, category filtering, and advanced query parameters.
tags:
    - web-scraping
    - search-api
    - data-extraction
    - ai-integration
    - api-documentation
category: api
---

Firecrawl 的搜索 API 允许你进行网页搜索，并可选在一次操作中抓取搜索结果。

- 选择特定输出 formats (markdown、HTML、links、screenshots)
- 使用可自定义参数 (如 location) 进行网页搜索
- 可选以多种 formats 从搜索结果中提取内容
- 控制结果数量并设置超时

详情参见 [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search)。

### /search 端点

用于执行网页搜索，并可选择从结果中获取内容。

### 安装

### 基本用法

### 响应

SDK 将直接返回数据对象；cURL 将返回完整的有效负载。

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

## 搜索结果类型

除了常规网页结果外，Search 还可通过 `sources` 参数支持以下专用结果类型：

- `web`：标准网页结果 (默认)
- `news`：新闻结果
- `images`：图片搜索结果

你可以在一次调用中请求多个 source (例如 `sources: ["web", "news"]`) 。此时，`limit` 参数会**按每种 source 类型分别生效**——因此，当 `limit: 5` 且 `sources: ["web", "news"]` 时，会分别返回最多 5 条 web 结果和最多 5 条 news 结果 (合计最多 10 条) 。如果你需要为不同的 source 设置不同的参数 (例如不同的 `limit` 值或不同的 `scrapeOptions`) ，请分别发起独立的调用。

## 搜索类别

使用 `categories` 参数按特定类别过滤搜索结果：

- `github`：在 GitHub 的仓库、代码、Issue 和文档中搜索
- `research`：搜索学术与科研网站 (arXiv、Nature、IEEE、PubMed 等)
- `pdf`：搜索 PDF 文档

### GitHub 分类搜索

在 GitHub 仓库中进行定向搜索：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "Python 网页抓取",
    "categories": ["github"],
    "limit": 10
  }'
```

### 研究类别搜索

搜索学术与科研类网站：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "机器学习 transformer",
    "categories": ["研究"],
    "limit": 10
  }'
```

### 混合类别搜索

在一次搜索中合并多个类别：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "神经网络",
    "categories": ["github", "research"],
    "limit": 15
  }'
```

### 分类响应格式

每条搜索结果都包含一个 `category` 字段，用于标示其来源：

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "神经网络实现",
        "description": "基于 PyTorch 的神经网络实现",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "神经网络架构的最新进展",
        "description": "探讨神经网络改进的研究论文"
        "category": "research"
      }
    ]
  }
}
```

示例：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### 按尺寸筛选的高清图片搜索

使用 images 源的搜索运算符查找高分辨率图片：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sunset imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "mountain wallpaper larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**常见高清分辨率：**

- `imagesize:1920x1080` - 全高清 (1080p)
- `imagesize:2560x1440` - QHD (1440p)
- `imagesize:3840x2160` - 4K UHD
- `larger:1920x1080` - 高清及以上
- `larger:2560x1440` - QHD 及以上

## 搜索并抓取内容

在一次操作中完成搜索并从结果中提取内容。

通过 `scrapeOptions` 参数，该搜索端点支持 /scrape 端点中的所有选项。

### 包含爬取内容的响应

```
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - 终极网页抓取 API",
      "description": "Firecrawl 是强大的网页抓取 API，可将任意网站转化为干净且结构化的数据，供 AI 与分析使用。",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\n终极网页抓取 API\n\n## 将任意网站转化为干净且结构化的数据\n\nFirecrawl 让从网站提取数据变得简单高效，适用于 AI 应用、市场研究、内容聚合等场景……",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - 终极网页抓取 API",
        "description": "Firecrawl 是强大的网页抓取 API，可将任意网站转化为干净且结构化的数据，供 AI 与分析使用。"
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## 高级搜索选项

Firecrawl 的搜索 API 支持通过多种参数自定义搜索：

### 位置定制

### 基于时间的搜索

使用 `tbs` 参数按时间过滤结果。注意，`tbs` 仅适用于 `web` 源结果，不会过滤 `news` 或 `images` 结果。如果你需要按时间过滤的新闻结果，建议使用 `web` 源并配合 `site:` 运算符限定到特定新闻域名。

常用 `tbs` 值：

- `qdr:h` - 过去 1 小时
- `qdr:d` - 过去 24 小时
- `qdr:w` - 过去 1 周
- `qdr:m` - 过去 1 个月
- `qdr:y` - 过去 1 年
- `sbd:1` - 按日期排序 (最新优先)

若需更精确的时间过滤，可使用自定义日期范围格式指定确切的区间：

你可以将 `sbd:1` 与时间过滤条件组合使用，在时间范围内按日期排序返回结果。例如，`sbd:1,qdr:w` 会返回过去一周内的结果，并按最新优先排序；`sbd:1,cdr:1,cd_min:12/1/2024,cd_max:12/31/2024` 会返回 2024 年 12 月内的结果，并按日期排序。

### 自定义超时

为搜索操作设置自定义超时时间：

## 零数据保留 (ZDR)

对于有严格数据处理要求的团队，Firecrawl 可通过 `enterprise` 参数为 `/search` 端点提供零数据保留 (ZDR) 选项。ZDR 搜索功能适用于 Enterprise 计划——访问 [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) 即可开始使用。

### 端到端 ZDR

使用端到端 ZDR 时，Firecrawl 及我们的上游搜索服务提供商均实行零数据保留。整个流程中的任何环节都不会存储查询或结果数据。

- **成本：** 每 10 个结果 10 额度
- **参数：** `enterprise: ["zdr"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["zdr"]
  }'
```

### 匿名化 ZDR

使用匿名化 ZDR 时，Firecrawl 会在我们这一侧实施完全的零数据保留。我们的搜索提供商可能会缓存查询，但这些查询已被完全匿名化——不附带任何可识别信息。

- **成本：** 每 10 个结果 2 个额度
- **参数：** `enterprise: ["anon"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["anon"]
  }'
```

### 结合使用 Search ZDR 和 Scrape ZDR

如果你使用的是带内容抓取 (`scrapeOptions`) 的 search，则 `enterprise` 参数适用于搜索部分，而 `scrapeOptions` 中的 `zeroDataRetention` 则适用于抓取部分。要让这两部分都实现完整的 ZDR，请同时设置这两个参数：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 5,
    "enterprise": ["zdr"],
    "scrapeOptions": {
      "formats": ["markdown"],
      "zeroDataRetention": true
    }
  }'
```

## 成本影响

每次搜索的费用为每 10 条搜索结果消耗 2 个积分。如果启用了抓取选项，每个搜索结果会按标准抓取费用计费：

- **Basic scrape**：每个网页 1 个积分
- **PDF parsing**：每个 PDF 页面 1 个积分
- **Enhanced proxy mode**：每个网页额外 4 个积分
- **JSON mode**：每个网页额外 4 个积分

为控制成本，可以：

- 如果不需要 PDF 解析，将其设置为 `parsers: []`
- 在可能的情况下使用 `proxy: "basic"` 而不是 `"enhanced"`，或者将其设置为 `"auto"`
- 使用 `limit` 参数限制搜索结果数量

## 高级抓取选项

有关抓取选项的更多详细信息，请参阅 [Scrape 功能文档](https://docs.firecrawl.dev/features/scrape)。除 FIRE-1 Agent 和 Change-Tracking 功能外，其余均受此搜索端点支持。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。