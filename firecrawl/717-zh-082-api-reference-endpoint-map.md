---
title: Map（映射） - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:09:24.084952-03:00
rendered_js: false
word_count: 53
summary: This document describes the authentication requirements and configuration parameters for performing search and sitemap-based URL discovery via the Firecrawl API.
tags:
    - firecrawl-api
    - authentication
    - sitemap-configuration
    - api-request-parameters
    - url-discovery
category: api
---

> 您是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 请求体

指定搜索查询，以按相关性对结果排序。示例：使用“blog”将返回在 URL 中包含单词“blog”的网址，并按相关性排序。

用于映射（mapping）时的 sitemap 模式。若设置为 `skip`，则不会使用 sitemap 来发现 URL。若设置为 `only`，则只会返回出现在 sitemap 中的 URL。默认值为 `include`，此时会同时使用 sitemap 和其他方式来发现 URL。

跳过站点地图缓存以获取最新的 URL。站点地图数据最多会被缓存 7 天；如果你刚更新了站点地图，请使用该参数。

返回的最大链接数量

必填范围: `x <= 100000`

请求的地域设置。指定后，如果有可用代理，将使用相应代理，并模拟对应的语言和时区设置。若未指定，则默认为“US”。

#### 响应