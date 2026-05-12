---
title: 抓取 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/scrape
source: sitemap
fetched_at: 2026-03-23T07:20:23.218108-03:00
rendered_js: false
word_count: 341
summary: Firecrawl 是一个将网站内容转换为 LLM 友好格式的抓取平台，支持 Markdown 输出、结构化数据提取、品牌视觉分析及网页交互操作。
tags:
    - web-scraping
    - llm-data-extraction
    - markdown-conversion
    - api-integration
    - structured-data
    - data-processing
category: reference
---

Firecrawl 将网页转换为 Markdown，非常适合 LLM 应用。

- 处理复杂环节：代理、缓存、速率限制、被 JS 阻止的内容
- 支持动态内容：动态网站、JS 渲染站点、PDF、图片
- 输出干净的 Markdown、结构化数据、截图或 HTML

详情请参阅 [Scrape Endpoint API 参考](https://docs.firecrawl.dev/api-reference/endpoint/scrape)。

### /scrape 端点

用于抓取指定 URL 并获取其内容。

### 安装

### 使用方式

有关参数的更多信息，请参阅 [API 参考](https://docs.firecrawl.dev/api-reference/endpoint/scrape)。

### 响应

各 SDK 会直接返回数据对象。cURL 将按下方所示原样返回载荷。

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

## 抓取 formats

现在你可以选择输出所需的 formats。你可以指定多个输出 formats。支持的 formats 包括：

- Markdown (`markdown`)
- 摘要 (`summary`)
- HTML (`html`) - 页面 HTML 的清洗版本
- 原始 HTML (`rawHtml`) - 按页面返回的不经修改的 HTML
- 截图 (`screenshot`，可选项包括 `fullPage`、`quality`、`viewport`) — 截图 URL 会在 24 小时后过期
- 链接 (`links`)
- JSON (`json`) - 结构化输出
- 图片 (`images`) - 提取页面中的所有图片 URL
- 品牌 (`branding`) - 提取品牌标识与设计系统

输出键将与你选择的 format 对应。

### /scrape (使用 JSON) 端点

用于从抓取的页面中提取结构化数据。

输出：

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI 赋能的网页抓取与数据抽取",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI 赋能的网页抓取与数据抽取",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI 赋能的网页抓取与数据抽取",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

现在，你只需向端点传入一个 `prompt`，即可在不提供 schema 的情况下进行提取。LLM 会自行决定数据结构。

输出：

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI 驱动的网页抓取与数据抽取",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI 驱动的网页抓取与数据抽取",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI 驱动的网页抓取与数据抽取",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### JSON 格式选项

使用 `json` 格式时，在 `formats` 中传入一个对象，包含以下参数：

- `schema`：用于结构化输出的 JSON Schema。
- `prompt`：可选提示；在提供 schema 时或仅需轻量指引时用于辅助抽取。

## 提取品牌识别度

### /scrape (品牌信息) 端点

branding 格式会从网页中提取完整的品牌识别信息，包括颜色、字体、排版、间距、UI 组件等。它适用于设计系统分析、品牌监测，或构建需要理解网站视觉风格的工具。

### 响应

品牌配置会返回一个完整的 `BrandingProfile` 对象，其结构如下：

```
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### 品牌档案结构

`branding` 对象包含以下属性：

- `colorScheme`: 检测到的配色方案 (`"light"` 或 `"dark"`)
- `logo`: 主徽标的 URL
- `colors`: 包含品牌颜色的对象：
  
  - `primary`、`secondary`、`accent`: 主要品牌色
  - `background`、`textPrimary`、`textSecondary`: 界面颜色
  - `link`、`success`、`warning`、`error`: 语义颜色
- `fonts`: 页面中使用的字体系列数组
- `typography`: 详细的排版信息：
  
  - `fontFamilies`: 正文、标题与代码字体系列
  - `fontSizes`: 标题与正文的尺寸定义
  - `fontWeights`: 字重定义 (细体、常规、中等、粗体)
  - `lineHeights`: 不同文本类型的行高值
- `spacing`: 间距与布局信息：
  
  - `baseUnit`: 基础间距单位 (像素)
  - `borderRadius`: 默认圆角
  - `padding`、`margins`: 间距值
- `components`: UI 组件样式：
  
  - `buttonPrimary`、`buttonSecondary`: 按钮样式
  - `input`: 输入框样式
- `icons`: 图标样式信息
- `images`: 品牌图像 (logo、favicon、og:image)
- `animations`: 动画与过渡设置
- `layout`: 布局配置 (栅格、页眉/页脚高度)
- `personality`: 品牌个性特征 (语气、调性、目标受众)

### 与其他 formats 结合使用

你可以将 branding 格式与其他 formats 组合，以获取更全面的页面数据：

## 使用 actions 与页面交互

Firecrawl 允许你在抓取页面内容之前对网页执行各种 actions。这对于与动态内容交互、在页面之间导航，或访问需要用户操作的内容特别有用。 下面是一个示例，演示如何使用 actions 访问 google.com，搜索 Firecrawl，点击第一个结果，并截取页面截图。 在执行其他 actions 之前或之后，几乎都应使用 `wait` action，为页面加载预留足够时间。

### 示例

### 输出

有关 actions 参数的更多信息，请参见 [API 参考](https://docs.firecrawl.dev/api-reference/endpoint/scrape)。

## 位置与语言

指定国家/地区和首选语言，以根据你的目标位置和语言偏好获取相关内容。

### 工作原理

当你指定位置设置时，Firecrawl 会在可用时使用合适的代理，并仿真相应的语言和时区设置。默认情况下，若未指定位置，位置将设为“US”。

### 用法

要使用位置和语言设置，请在请求体中包含 `location` 对象，并提供以下属性：

- `country`：ISO 3166-1 alpha-2 国家/地区代码 (例如“US”“AU”“DE”“JP”) 。默认值为“US”。
- `languages`：按优先级排序的首选语言和区域设置数组。默认使用所设位置对应的语言。

有关受支持位置的更多详情，请参阅[代理文档](https://docs.firecrawl.dev/zh/features/proxies)。

## 缓存与 maxAge (缓存)

为加快请求速度，当有较新的副本可用时，Firecrawl 默认会直接从缓存返回结果。

- **默认新鲜度窗口**：`maxAge = 172800000` 毫秒 (2 天) 。如果缓存页面仍在该窗口内，将立即返回；否则会重新抓取页面并写入缓存。
- **性能**：在数据对时效性要求不高时，抓取速度可提升至最多 5 倍。
- **始终获取最新**：将 `maxAge` 设为 `0`。注意，这会完全绕过缓存，因此每次请求都会走完整的抓取流水线，这意味着请求完成所需时间更长，也更有可能失败。如果对每个请求的实时性不是绝对关键，建议使用非零的 `maxAge`。
- **避免存储**：如果不希望 Firecrawl 为本次请求缓存/存储结果，将 `storeInCache` 设为 `false`。
- **仅查缓存**：设置 `minAge` 可仅执行缓存查询，而不会触发新的抓取。该值以毫秒为单位，指定缓存数据必须满足的最小缓存时长。如果未找到缓存数据，将返回带有错误代码 `SCRAPE_NO_CACHED_DATA` 的 `404`。将 `minAge` 设为 `1` 可接受任意缓存数据，无论其缓存时长是多少。
- **变更跟踪**：包含 `changeTracking` 的请求会绕过缓存，因此会忽略 `maxAge`。

示例 (强制获取最新内容) ：

示例 (使用 10 分钟缓存窗口) ：

## 批量抓取多个 URL

你现在可以同时批量抓取多个 URL。它以起始 URL 和可选参数作为输入。params 参数允许你为批量抓取任务指定其他选项，例如输出 formats。

### 工作原理

它与 `/crawl` 端点的运行方式非常相似。它会提交一个批量抓取作业，并返回一个作业 ID，用于检查该批量抓取的状态。 SDK 提供两种方式：同步与异步。同步方式会直接返回批量抓取作业的结果，异步方式则会返回一个作业 ID，供您用于查询批量抓取的状态。

### 使用方法

### Response

如果你使用 SDK 的同步方法，将直接返回批量抓取任务的结果；否则会返回一个作业 ID，你可以用它来查询批量抓取的状态。

#### 同步执行

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Firecrawl 文档首页！[浅色标志](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "使用 Groq Llama 3 构建“网站对话”功能 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "了解如何使用 Firecrawl、Groq Llama 3 和 LangChain 构建“与你的网站对话”的机器人。",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### 异步

你可以使用作业 ID 调用 `/batch/scrape/{id}` 端点来查看批量抓取的状态。该端点应在作业仍在运行期间或刚完成后使用，**因为批量抓取作业会在 24 小时后过期**。

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## 增强模式

对于复杂网站，Firecrawl 提供了增强模式，在提高成功率的同时保护隐私。 了解更多关于[增强模式](https://docs.firecrawl.dev/zh/features/enhanced-mode)的信息。

## 零数据保留 (ZDR)

Firecrawl 支持零数据保留 (ZDR) ，适用于有严格数据处理要求的团队。启用后，Firecrawl 不会在请求生命周期结束后保留任何页面内容或提取的数据。 要启用 ZDR，请在请求中设置 `zeroDataRetention: true`：

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "url": "https://example.com",
    "formats": ["markdown"],
    "zeroDataRetention": true
  }'
```

ZDR 仅适用于 Enterprise 计划，且需要为你的团队启用。访问 [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) 以开始使用。 ZDR 会在基础抓取成本之上，**为每个页面额外增加 1 个 credit**。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化引导说明。