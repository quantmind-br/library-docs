---
title: 高级抓取指南 | Firecrawl
url: https://docs.firecrawl.dev/zh/advanced-scraping-guide
source: sitemap
fetched_at: 2026-03-23T07:27:42.283358-03:00
rendered_js: false
word_count: 483
summary: This document provides a comprehensive reference for the Firecrawl scrape endpoint, detailing configuration options for output formats, content filtering, PDF parsing, and browser automation actions.
tags:
    - firecrawl
    - web-scraping
    - api-reference
    - pdf-parsing
    - browser-automation
    - data-extraction
category: reference
---

涵盖 Firecrawl 的 scrape、crawl、map 和 agent 各端点下所有选项的参考说明。

## 基础抓取

要抓取单个页面并获取干净的 Markdown 内容，请使用 `/scrape` 端点。

## 抓取 PDF

Firecrawl 支持 PDF。需要确保解析 PDF 时，请使用 `parsers` 选项（例如 `parsers: ["pdf"]`）。你可以通过 `mode` 选项来控制解析策略：

- **`auto`** （默认）— 先尝试基于文本的快速提取，如有需要再回退到 OCR。
- **`fast`** — 仅进行基于文本（嵌入文本）的解析。速度最快，但会跳过扫描件或图片较多的页面。
- **`ocr`** — 对每一页强制使用 OCR 解析。适用于扫描文档，或在 `auto` 误判页面类型时使用。

`{ type: "pdf" }` 和 `"pdf"` 都默认使用 `mode: "auto"`。

```
"parsers": [{ "type": "pdf", "mode": "fast", "maxPages": 50 }]
```

## 抓取选项

使用 `/scrape` 端点时，你可以通过以下选项定制请求。

### formats (`formats`)

`formats` 数组控制 scraper 返回哪些输出类型。默认值：`["markdown"]`。 **字符串 formats**：直接传入名称 (例如 `"markdown"`) 。

FormatDescription`markdown`页面内容转换为干净的 Markdown。`html`处理后的 HTML，已移除不必要的元素。`rawHtml`服务器返回的原始 HTML，保持原样。`links`页面上发现的所有链接。`images`页面上发现的所有图片。`summary`使用 LLM 生成的页面内容摘要。`branding`提取品牌风格特征 (颜色、字体、排版、间距、UI 组件) 。

**对象 formats**：传入包含 `type` 和其他选项的对象。

FormatOptionsDescription`json``prompt?: string`, `schema?: object`使用 LLM 抽取结构化数据。提供 JSON schema 和/或自然语言提示词 (最多 10,000 字符) 。`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`捕获截图。每个请求最多一个。viewport 最大分辨率为 7680×4320。截图 URL 会在 24 小时后过期。`changeTracking``modes?: ("json" | "git-diff")[]`, `tag?: string`, `schema?: object`, `prompt?: string`跟踪不同抓取结果之间的变化。需要在 formats 数组中同时包含 `"markdown"`。`attributes``selectors: [{ selector: string, attribute: string }]`从匹配 CSS 选择器的元素中提取指定的 HTML 属性。

### 内容过滤

这些参数用于控制页面的哪些部分会出现在输出中。`onlyMainContent` 会优先执行，用于去掉页面框架内容（导航、页脚等），然后 `includeTags` 和 `excludeTags` 会在此基础上进一步收窄结果范围。若将 `onlyMainContent: false`，则会使用整页 HTML 作为后续标签过滤的起点。

参数类型默认值描述`onlyMainContent``boolean``true`仅返回主体内容。设为 `false` 则返回整页内容。`includeTags``array`—要包含的 HTML 标签、类或 ID（例如 `["h1", "p", ".main-content"]`）。`excludeTags``array`—要排除的 HTML 标签、类或 ID（例如 `["#ad", "#footer"]`）。

### 时间与缓存

参数类型默认值描述`waitFor``integer` (ms)`0`在抓取前额外等待的时间，会叠加在智能等待的基础上。请谨慎使用。`maxAge``integer` (ms)`172800000`如果缓存的存在时间小于该值，则返回缓存结果 (默认 2 天) 。设为 `0` 则始终获取最新内容。`timeout``integer` (ms)`30000`在中止请求前允许的最长请求耗时 (默认 30 秒) 。最小值为 1000 (1 秒) 。

### PDF 解析

参数类型默认值描述`parsers``array``["pdf"]`控制 PDF 处理。使用 `[]` 跳过解析并返回 base64（固定费用 1 积分）。

```
{ "type": "pdf", "mode": "fast" | "auto" | "ocr", "maxPages": 10 }
```

属性类型默认值描述`type``"pdf"`*(必填)*解析器类型。`mode``"fast" | "auto" | "ocr"``"auto"``fast`：仅进行基于文本的抽取。`auto`：快速模式，必要时回退到 OCR。`ocr`：强制使用 OCR。`maxPages``integer`—解析的最大页数上限。

### actions

在抓取前执行浏览器 actions。这对于处理动态内容、页面导航或需要用户交互才能访问的页面非常有用。每个请求最多可包含 50 个 actions，并且所有 `wait` actions 与 `waitFor` 的总等待时间不得超过 60 秒。

ActionParametersDescription`wait``milliseconds?: number`, `selector?: string`等待固定时长 **或** 等待某个元素可见（两者择一传入，不要同时使用）。使用 `selector` 时，超时时间为 30 秒。`click``selector: string`, `all?: boolean`点击匹配该 CSS 选择器的元素。设置 `all: true` 将点击所有匹配元素。`write``text: string`向当前获得焦点的输入字段键入文本。你必须先通过 `click` action 使元素获得焦点。`press``key: string`模拟按下某个键盘按键（例如 `"Enter"`、`"Tab"`、`"Escape"`）。`scroll``direction?: "up" | "down"`, `selector?: string`滚动整个页面或某个特定元素。方向默认为 `"down"`。`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`截取页面截图。最大视口分辨率为 7680×4320。`scrape`*(none)*在 action 序列执行到此步骤时，捕获当前页面 HTML。`executeJavascript``script: string`在页面中运行 JavaScript 代码。返回 `{ type, value }`。`pdf``format?: string`, `landscape?: boolean`, `scale?: number`生成 PDF。支持的格式包括 `"A0"` 到 `"A6"`、`"Letter"`、`"Legal"`、`"Tabloid"`、`"Ledger"`。默认值为 `"Letter"`。

#### actions 执行说明

- 在使用 **Write** 前，需要先执行一次 `click` 以聚焦目标元素。
- **Scroll** 可以接受一个可选的 `selector`，用于滚动特定元素而不是整个页面。
- **Wait** 接受 `milliseconds`（固定延迟）或 `selector`（等待元素可见）两种参数中的一种。
- actions 按**顺序**执行：每一步都会在下一步开始前完成。
- actions **不支持 PDF**。如果 URL 解析为 PDF 文档，请求将会失败。

#### 高级操作示例

**执行截图操作：**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": "#load-more" },
      { "type": "wait", "milliseconds": 1000 },
      { "type": "screenshot", "fullPage": true, "quality": 80 }
    ]
  }'
```

**点击多个元素：**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": ".expand-button", "all": true },
      { "type": "wait", "milliseconds": 500 }
    ],
    "formats": ["markdown"]
  }'
```

**生成 PDF 文件：**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "pdf", "format": "A4", "landscape": false }
    ]
  }'
```

### 完整抓取示例

以下请求组合了多个抓取选项：

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats": [
        "markdown",
        "links",
        "html",
        "rawHtml",
        { "type": "screenshot", "fullPage": true, "quality": 80 }
      ],
      "includeTags": ["h1", "p", "a", ".main-content"],
      "excludeTags": ["#ad", "#footer"],
      "onlyMainContent": false,
      "waitFor": 1000,
      "timeout": 15000,
      "parsers": ["pdf"]
    }'
```

该请求会返回 Markdown、HTML、原始 HTML、链接以及整页截图。它将内容范围限定为 `<h1>`、`<p>`、`<a>` 和 `.main-content`，同时排除 `#ad` 和 `#footer`，在开始抓取前等待 1 秒，将超时时间设置为 15 秒，并启用 PDF 解析。 有关详细信息，请参阅完整的 [Scrape API 参考文档](https://docs.firecrawl.dev/api-reference/endpoint/scrape)。

在 `formats` 中使用 JSON 格式对象，一次性提取结构化数据：

## Agent endpoint

使用 `/v2/agent` 端点进行自动化的多页面数据提取。Agent 以异步方式运行：你先创建一个任务，然后通过轮询获取结果。

### Agent 选项

参数类型默认值描述`prompt``string`*(required)*自然语言说明，用于描述要提取哪些数据 (最多 10,000 个字符) 。`urls``array`—将 Agent 的访问限制在这些 URL。`schema``object`—用于组织提取数据结构的 JSON 模式 (schema) 。`maxCredits``number``2500`Agent 可消耗的最大额度。Dashboard 最多支持 2,500；如需更高上限，请通过 API 设置 (高于 2,500 的值始终按付费请求计费) 。`strictConstrainToURLs``boolean``false`为 `true` 时，Agent 只会访问提供的这些 URL。`model``string``"spark-1-mini"`要使用的 AI 模型。`"spark-1-mini"` (默认，成本降低 60%) 或 `"spark-1-pro"` (更高准确率) 。

### 检查 agent 状态

轮询 `GET /v2/agent/{jobId}` 以检查进度。响应中的 `status` 字段将为 `"processing"`、`"completed"` 或 `"failed"`。

```
curl -X GET https://api.firecrawl.dev/v2/agent/YOUR-JOB-ID \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

Python 和 Node SDK 还提供了一个便捷方法（`firecrawl.agent()`），用于启动任务并自动轮询，直到任务完成。

## 爬取多个页面

要爬取多个页面，请使用 `/v2/crawl` 端点。该爬取任务以异步方式运行，并返回一个任务 ID。使用 `limit` 参数控制爬取的页面数量。若省略该参数，爬取任务最多会处理 10,000 个页面。

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
```

### 返回结果

```
{ "id": "1234-5678-9101" }
```

### 检查抓取任务

使用任务 ID 查看抓取任务的状态并获取其结果。

```
curl -X GET https://api.firecrawl.dev/v2/crawl/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

如果内容大小超过 10MB，或者抓取任务仍在运行，响应中可能会包含一个 `next` 参数，即用于获取下一页结果的 URL。

### 爬取提示与参数预览

你可以提供自然语言的 `prompt`，让 Firecrawl 自动推导爬取设置。请先预览结果：

```
curl -X POST https://api.firecrawl.dev/v2/crawl/params-preview \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "prompt": "提取文档与博客"
  }'
```

### 爬虫选项

当使用 `/v2/crawl` 端点时，你可以使用以下选项自定义爬取行为。

#### 路径过滤

参数类型默认值说明`includePaths``array`—要包含的 URL 的正则表达式模式（默认仅匹配路径名）。`excludePaths``array`—要排除的 URL 的正则表达式模式（默认仅匹配路径名）。`regexOnFullURL``boolean``false`在完整 URL 上进行模式匹配，而不仅仅是路径名。

#### 爬取范围

参数类型默认值描述`maxDiscoveryDepth``integer`—用于发现新 URL 的最大链接深度。`limit``integer``10000`最大爬取页面数。`crawlEntireDomain``boolean``false`通过遍历同级和父级页面来覆盖整个域名。`allowExternalLinks``boolean``false`跟踪指向外部域名的链接。`allowSubdomains``boolean``false`跟踪主域名下的子域名。`delay``number` (s)—两次爬取之间的延迟时间（秒）。

#### Sitemap 和去重

ParameterTypeDefaultDescription`sitemap``string``"include"``"include"`：使用 sitemap + 链接发现。`"skip"`：忽略 sitemap。`"only"`：仅抓取 sitemap 中的 URL。`deduplicateSimilarURLs``boolean``true`将 URL 变体（`www.`、`https`、结尾斜杠、`index.html`）视为同一 URL 进行规范化去重。`ignoreQueryParameters``boolean``false`在去重前移除查询字符串（例如将 `/page?a=1` 和 `/page?a=2` 视为同一个 URL）。

#### 爬取任务的抓取选项

参数类型默认值描述`scrapeOptions``object``{ formats: ["markdown"] }`每个页面的抓取配置。支持上述所有[抓取选项](#scrape-options)。

### 抓取示例

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-你的-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "includePaths": ["^/blog/.*$", "^/docs/.*$"],
      "excludePaths": ["^/admin/.*$", "^/private/.*$"],
      "maxDiscoveryDepth": 2,
      "limit": 1000
    }'
```

## 网站链接映射

`/v2/map` 端点用于识别与给定网站相关的 URL。

```
curl -X POST https://api.firecrawl.dev/v2/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

### Map 参数选项

参数类型默认值说明`search``string`—通过文本匹配来过滤链接。`limit``integer``100`返回的最大链接数量。`sitemap``string``"include"``"include"`、`"skip"` 或 `"only"`。`includeSubdomains``boolean``true`是否包含该网站的子域名。

相关 API 参考：[/map 端点文档](https://docs.firecrawl.dev/api-reference/endpoint/map)

### 允许 Firecrawl 抓取你的网站

- **User Agent（用户代理）**：请在防火墙或安全规则中允许 `FirecrawlAgent`。
- **IP addresses（IP 地址）**：Firecrawl 不使用固定的对外 IP 地址集合。

### 允许你的应用调用 Firecrawl API

如果你的防火墙阻止应用向外部服务发出出站请求，你需要将 Firecrawl 的 API 服务器 IP 地址加入白名单，这样你的应用才能访问 Firecrawl API（`api.firecrawl.dev`）：

- **IP Address**: `35.245.250.27`

将此 IP 添加到防火墙的出站允许列表中，这样你的后端就可以向 Firecrawl 发送抓取（scrape）、爬取（crawl）、映射（map）以及智能体（agent）请求。