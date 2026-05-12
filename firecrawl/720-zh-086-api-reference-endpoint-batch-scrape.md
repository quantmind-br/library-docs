---
title: 批量抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:09:45.327126-03:00
rendered_js: false
word_count: 289
summary: This document provides technical documentation for the Firecrawl API request parameters and response fields, detailing options for web scraping, cache management, authentication, and output formats.
tags:
    - api-reference
    - web-scraping
    - request-parameters
    - data-extraction
    - firecrawl-api
    - configuration-options
category: api
---

> 如果你是需要 Firecrawl API 密钥的 AI 代理，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化入门说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 请求体

最大并发抓取数。此参数用于为本次批量抓取设置并发上限。若未指定，批量抓取将遵循你的团队的并发限制。

如果在 urls 数组中指定了无效的 URL，这些 URL 会被忽略。它们不会导致整个请求失败，而是会使用剩余的有效 URL 创建一次批量抓取任务，并在响应的 invalidURLs 字段中返回这些无效的 URL。

formats

(Markdown · object | Summary · object | HTML · object | Raw HTML · object | Links · object | Images · object | Screenshot · object | JSON · object | Change Tracking · object | Branding · object)\[]

要在响应中包含的输出 formats。你可以指定一个或多个 formats，既可以使用字符串（例如：`'markdown'`），也可以使用带有其他选项的对象（例如：`{ type: 'json', schema: {...} }`）。某些 formats 需要配置特定选项。示例：`['markdown', { type: 'json', schema: {...} }]`。

- Markdown
- Summary
- HTML
- Raw HTML
- Links
- Images
- Screenshot
- JSON
- Change Tracking
- Branding

仅返回页面的主要内容，不包含 header、nav、footer 等元素。

如果页面的缓存版本的生成时间距今少于该毫秒数，则返回该缓存页面；如果缓存版本距今超过该时间，则会重新抓取页面。若你不需要特别新的数据，启用此选项可将抓取速度提升至 5 倍。默认值为 2 天。

&lt;\[ { "key": "0", "translation": "设置后，请求将仅检查缓存，不会触发新的抓取。该值以毫秒为单位，指定缓存数据必须满足的最小存在时长。如果存在匹配的缓存数据，将立即返回。若未找到缓存数据，则返回 404，错误代码为 SCRAPE\_NO\_CACHED\_DATA。将其设为 1 可接受任意缓存数据，不受时长限制。" } ]&lt;/&gt;

随请求发送的请求头。可用于传递 cookies、User-Agent 等信息。

指定在抓取内容前的延迟时间（毫秒），以便页面有足够时间完成加载。该等待时间是在 Firecrawl 的智能等待功能基础上的额外等待。

若要模拟在移动设备上进行抓取，请将其设置为 true。适用于测试响应式页面并获取移动端截图。

请求超时时间（以毫秒为单位）。最小值为 1000（1 秒）。默认值为 30000（30 秒）。最大值为 300000（300 秒）。

必填范围: `1000 <= x <= 300000`

用于控制在抓取过程中如何处理文件。包含 "pdf" 时（默认），会提取 PDF 内容并转换为 Markdown 格式，计费基于页数（每页 1 点数）。当传入空数组时，会以 base64 编码返回整个 PDF 文件，并对整份 PDF 按单一费率收取 1 点数。

actions

(Wait by Duration · object | Wait for Element · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

在抓取页面内容之前需要执行的页面 actions

- Wait by Duration
- Wait for Element
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

请求的地理位置设置。指定后，如果有可用的代理，将使用合适的代理，并模拟相应的语言和时区设置。如果未指定，则默认为“US”。

从 markdown 输出中移除所有 base 64 图像，以避免输出内容过长。这不会影响 html 或 rawHtml formats。图像的 alt 文本会保留在输出中，但 URL 会替换为占位符。

指定要使用的代理类型。

- basic：用于抓取几乎没有或只有基础反爬策略的网站的代理。速度快，通常可用。
- enhanced：用于抓取具有高级反爬策略的网站的增强型代理。速度较慢，但在某些站点上更可靠。每个请求最多消耗 5 点积分。
- auto：当 basic 代理抓取失败时，Firecrawl 会自动重试并切换为 enhanced 代理。如果使用 enhanced 重试成功，该次抓取将收取 5 点积分；如果使用 basic 一次就成功，则只按常规定价计费。

可用选项:

`basic`,

`enhanced`,

`auto`

如果为 true，该页面会存储到 Firecrawl 的索引和缓存中。如果你的抓取操作可能涉及数据保护方面的顾虑，将其设置为 false 会很有用。使用某些与敏感抓取相关的参数（例如 actions、headers）时，会被强制将此参数设为 false。

#### 响应

如果 ignoreInvalidURLs 为 true，则该字段是一个数组，包含请求中指定的所有无效 URL。若没有无效 URL，则该数组为空。如果 ignoreInvalidURLs 为 false，则该字段为 undefined。