---
title: Search（搜索） - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:08:51.254359-03:00
rendered_js: false
word_count: 182
summary: This document describes the Firecrawl search endpoint, which combines web search capabilities with scraping functionality to retrieve structured web content. It outlines various request parameters, including query operators, geolocation settings, content categorization, and time-based filtering.
tags:
    - api-reference
    - web-scraping
    - search-engine
    - data-extraction
    - firecrawl-api
    - query-operators
category: api
---

`search` 端点将网页搜索与 Firecrawl 的抓取能力相结合，为任意查询返回完整页面内容。 在请求中包含 `scrapeOptions`，并设置 `formats: [{"type": "markdown"}]`，即可为每条搜索结果获取完整的 markdown 内容；否则默认只返回结果（url、title、description）。你也可以使用其他 formats，例如 `{"type": "summary"}` 来获取精简内容。

## 支持的查询运算符

我们支持多种查询运算符，帮助你更高效地筛选搜索结果。

运算符功能示例`""`精确（非模糊）匹配一段文本`"Firecrawl"``-`排除特定关键词或对其他运算符取反`-bad`, `-site:firecrawl.dev``site:`仅返回来自指定网站的结果`site:firecrawl.dev``filetype:`仅返回具有特定文件扩展名的结果`filetype:pdf`, `-filetype:pdf``inurl:`仅返回在 URL 中包含某个词的结果`inurl:firecrawl``allinurl:`仅返回在 URL 中包含多个词的结果`allinurl:git firecrawl``intitle:`仅返回在页面标题中包含某个词的结果`intitle:Firecrawl``allintitle:`仅返回在页面标题中包含多个词的结果`allintitle:firecrawl playground``related:`仅返回与特定域相关的结果`related:firecrawl.dev``imagesize:`仅返回尺寸完全匹配的图片`imagesize:1920x1080``larger:`仅返回大于指定尺寸的图片`larger:1920x1080`

## location 参数

使用 `location` 参数获取按地理位置定向的搜索结果。格式：“string”。示例：“Germany”、“San Francisco,California,United States”。 查看[支持的位置完整列表](https://firecrawl.dev/search_locations.json)，了解所有可用的国家和语言。

## country 参数

使用 `country` 参数以 ISO 国家/地区代码指定搜索结果所属国家/地区。默认值：“US”。 示例：“US”、“DE”、“FR”、“JP”、“UK”、“CA”。

```
{
  "query": "餐厅",
  "country": "DE"
}
```

## `categories` 参数

使用 `categories` 参数按特定类别过滤搜索结果：

- **`github`** : 在 GitHub 仓库、代码、问题和文档中搜索
- **`research`** : 搜索学术和研究类网站（arXiv、Nature、IEEE、PubMed 等）
- **`pdf`** : 搜索 PDF

### 使用示例

```
{
  "query": "机器学习",
  "categories": ["github", "research"],
  "limit": 10
}
```

### 分类响应

每个结果都包含一个 `category` 字段，用于表示其来源：

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/ml-project",
        "title": "Machine Learning Project",
        "description": "Implementation of ML algorithms",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ML Research Paper",
        "description": "Latest advances in machine learning",
        "category": "research"
      }
    ]
  }
}
```

## 基于时间的搜索

使用 `tbs` 参数按时间范围过滤搜索结果，包括自定义日期区间。详细示例及支持的 formats 请参见 [Search Feature 文档](https://docs.firecrawl.dev/features/search#time-based-search)。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？如需自动化入门说明，请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 请求体

搜索查询语句

Maximum string length: `500`

返回结果的最大数量

必填范围: `1 <= x <= 100`

sources

(Web · object | Images · object | News · object)\[]

要搜索的数据源。将决定响应中可用的数组。默认为 \['web']。

- Web
- Images
- News

categories

(GitHub · object | Research · object | PDF · object)\[]

根据类别筛选结果。默认值为 \[]，表示结果不会按类别进行过滤。

- GitHub
- Research
- PDF

用于按时间过滤结果的搜索参数。支持预设时间范围（`qdr:h`、`qdr:d`、`qdr:w`、`qdr:m`、`qdr:y`）、自定义日期范围（`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`），以及按日期排序（`sbd:1`）。这些参数值可以组合使用，例如：`sbd:1,qdr:w`。

用于搜索结果的位置参数（例如 `San Francisco,California,United States`）。为获得最佳效果，请同时设置该参数和 `country` 参数。

用于按地域定向搜索结果的 ISO 国家代码（例如 `US`）。为获得最佳效果，请同时设置此参数和 `location` 参数。

从搜索结果中排除对其他 Firecrawl 端点无效的 URL。这样在将搜索结果数据输送到其他 Firecrawl API 端点时，有助于减少错误。

用于零数据保留（ZDR）的企业搜索选项。端到端 ZDR 使用 `["zdr"]`（10 额度 / 10 个结果），匿名化 ZDR 使用 `["anon"]`（2 额度 / 10 个结果）。必须为你的团队启用。

#### 响应

搜索结果。可用的数组取决于你在请求中指定的源。默认情况下会返回 `web` 数组。