---
title: 抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/scrape
source: sitemap
fetched_at: 2026-03-23T07:07:52.557142-03:00
rendered_js: false
word_count: 170
summary: This document provides the technical specifications and parameter configurations for the Firecrawl scrape API, detailing how to manage caching, authentication, proxy settings, and browser actions.
tags:
    - api-reference
    - web-scraping
    - data-extraction
    - proxy-settings
    - browser-automation
category: api
---

> 注意：全新的 [此 API 的 v2 版本](https://docs.firecrawl.dev/zh/api-reference/endpoint/scrape) 现已上线，提供更强大的功能和更高的性能。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 请求体

如果页面的缓存版本的生成时间距现在小于此值（毫秒），则返回该缓存版本；如果缓存版本早于此值，则会重新抓取页面。如果你不需要极其实时的数据，启用此选项可以将抓取速度最多提升 5 倍。默认值为 0，表示禁用缓存。

随请求发送的请求头。可用于携带 cookies、user-agent 等信息。

设置在获取内容前的延迟时间（毫秒），以便页面有足够时间加载完成。

若要模拟移动端抓取，请将其设置为 true。适用于测试响应式页面并获取移动端截图。

控制在爬取过程中如何处理 PDF 文件。为 true 时，会提取 PDF 内容并转换为 Markdown 格式，按页数计费（每页 1 个积分）。为 false 时，会返回以 base64 编码的 PDF 文件，统一按 1 个积分计费。

actions

(Wait · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

在抓取页面内容前需要执行的 actions

- Wait
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

请求的地理位置设置。指定后，如果可用，将使用合适的代理服务器，并模拟相应的语言和时区设置。如果未指定，默认值为“US”。

从输出中移除所有 Base64 图片，以避免内容过于冗长。图片的替代文本（alt 文本）会保留在输出中，但其 URL 会被占位符替换。

指定要使用的代理类型。

- basic：适用于抓取没有或仅有基础防爬机制网站的代理。速度快，通常足够好用。
- enhanced：适用于抓取具有高级防爬机制网站的增强型代理。速度较慢，但在某些网站上更可靠。每次请求最多消耗 5 个积分。
- auto：当使用 basic 代理抓取失败时，Firecrawl 会自动使用 enhanced 代理重试。如果使用 enhanced 重试成功，该次抓取将收取 5 个积分；如果首次使用 basic 即抓取成功，则只收取常规费用。

如果未指定代理类型，Firecrawl 将默认使用 basic。

可用选项:

`basic`,

`enhanced`,

`auto`

如果为 true，该页面将被存储到 Firecrawl 的索引和缓存中。若你的抓取活动可能涉及数据保护方面的问题，将其设置为 false 会更合适。使用某些与敏感抓取相关的参数（如 actions、headers）时，该参数会被强制设为 false。

输出中要包含的formats。

可用选项:

`markdown`,

`html`,

`rawHtml`,

`links`,

`screenshot`,

`screenshot@fullPage`,

`json`,

`changeTracking`

用于 changeTracking 的选项（Beta）。仅当在 formats 中包含 'changeTracking' 时才适用。使用 changeTracking 时，还必须同时指定 'markdown' 格式。

#### 响应