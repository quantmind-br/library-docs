---
title: 抽取 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/extract
source: sitemap
fetched_at: 2026-03-23T07:20:43.818287-03:00
rendered_js: false
word_count: 197
summary: 该文档介绍了如何使用 Firecrawl 的 /extract 端点从网页或 URL 列表中提取结构化数据，包括配置 schema、使用提示词、启用网页搜索以及管理异步提取作业。
tags:
    - firecrawl
    - data-extraction
    - api-endpoint
    - web-scraping
    - structured-data
    - llm-integration
category: api
---

`/extract` 端点可简化从任意数量的 URL 或整个域名收集结构化数据的流程。你只需提供一个 URL 列表 (可选使用通配符，如 `example.com/*`) ，以及用于描述所需信息的提示或 schema。Firecrawl 将负责爬取、解析与汇总，不论数据集大小。

你可以从一个或多个 URL 中提取结构化数据，也可以使用通配符：

- **单个页面**  
  示例：`https://firecrawl.dev/some-page`
- **多个页面 / 整个域名**  
  示例：`https://firecrawl.dev/*`

当你使用 `/*` 时，Firecrawl 会自动爬取并解析该域名下它能发现的所有 URL，然后提取所需数据。该功能目前为实验性功能；如果你遇到问题，请发送邮件至 [help@firecrawl.com](mailto:help@firecrawl.com)。

### 示例用法

**关键参数：**

- **urls**：一个或多个 URL 的数组。支持通配符 (`/*`) 以进行更广泛的爬取。
- **prompt** (可选，若无 schema 则必填) ：用自然语言描述所需数据，或说明数据应如何结构化。
- **schema** (可选，若无 prompt 则必填) ：当已知 JSON 结构时使用的更严格定义。
- **enableWebSearch** (可选) ：设为 `true` 时，提取可跟随链接跳出指定域名。

更多详情见 [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/extract)。

### 响应 (SDK)

```
{
  "success": true,
  "data": {
    "company_mission": "Firecrawl 是从网页提取数据的最简便方式。开发者通过一次 API 调用即可将 URL 稳定转换为适用于 LLM 的 Markdown 或结构化数据。",
    "supports_sso": false,
    "is_open_source": true,
    "is_in_yc": true
  }
}
```

## Job status and completion

当你提交一次提取作业 (通过 API 或入门方法) ，会收到一个 Job ID。你可以用该 ID：

- 获取作业状态：向 /extract/ 端点发送请求，查看作业是否仍在运行或已完成。
- 等待结果：如果你使用默认的 `extract` 方法 (Python/Node) ，SDK 会等待并返回最终结果。
- 先启动再轮询：如果你使用启动方法—`start_extract` (Python) 或 `startExtract` (Node) ，SDK 会立即返回一个 Job ID。使用 `get_extract_status` (Python) 或 `getExtractStatus` (Node) 检查进度。

Below are code examples for checking an extraction job’s status using Python, Node.js, and cURL:

### 可能的状态

- **completed**: 提取已成功完成。
- **processing**: Firecrawl 仍在处理你的请求。
- **failed**: 发生错误，数据未完整提取。
- **cancelled**: 该任务已被用户取消。

#### 处理中示例

```
{
  "success": true,
  "data": [],
  "status": "processing",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

#### 完成示例

```
{
  "success": true,
  "data": {
      "company_mission": "Firecrawl 是从网页提取数据的最简便方式。开发者只需一次 API 调用，便可将 URL 可靠地转换为适用于 LLM 的 Markdown 或结构化数据。",
      "supports_sso": false,
      "is_open_source": true,
      "is_in_yc": true
    },
  "status": "已完成",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

如果你不想定义严格的结构，只需提供一个 `prompt`。底层模型会自动为你选择结构，这在进行探索性或更灵活的请求时很有用。

```
{
  "success": true,
  "data": {
    "company_mission": "将网站转化为可直接用于 LLM 的数据。用从任意网站抓取的干净数据驱动你的 AI 应用。"
  }
}
```

## 通过网页搜索提升结果

在请求中将 `enableWebSearch = true` 启用后，抓取范围会扩展到所提供的 URL 集合之外，从而获取来自相关链接页面的支撑性或关联信息。 下面是一个示例：它提取有关行车记录仪的信息，并使用相关页面的数据来充实结果：

### 含网页搜索的示例响应

```
{
  "success": true,
  "data": {
    "dash_cams": [
      {
        "name": "Nextbase 622GW",
        "price": "$399.99",
        "features": [
          "4K 视频录制",
          "图像防抖",
          "内置 Alexa",
          "集成 What3Words"
        ],
        /* 以下信息结合了其他网站的内容，例如 
        https://www.techradar.com/best/best-dash-cam，系通过 
        enableWebSearch 参数获取 */
        "pros": [
          "卓越的视频画质",
          "出色的夜视表现",
          "内置 GPS"
        ],
        "cons": ["价格偏高", "应用可能较不稳定"]
      }
    ],
  }

```

该响应包含从相关页面收集的补充上下文，从而提供更全面、更准确的信息。

`/extract` 端点现已支持在不提供特定 URL 的情况下，基于提示提取结构化数据。适用于研究场景或在确切 URL 不确定时使用。目前处于 Alpha 阶段。

## 已知限制 (Beta)

1. **大规模站点覆盖**  
   目前尚不支持在单个请求中完整覆盖超大型网站 (例如“Amazon 上的所有产品”) 。
2. **复杂逻辑查询**  
   类似“查找 2025 年的所有帖子”的请求可能无法稳定返回全部预期数据。更高级的查询能力正在开发中。
3. **偶发不一致**  
   不同运行的结果可能有所差异，尤其是在非常大型或动态的网站上。通常能捕获核心信息，但可能存在一定差异。
4. **Beta 状态**  
   由于 `/extract` 仍处于 Beta，功能和性能将持续演进。欢迎提交问题与反馈，帮助我们改进。

## 使用 FIRE-1

FIRE-1 是一款 AI 代理，可增强 Firecrawl 的抓取能力。它能够控制浏览器 actions，并在复杂的网站结构中导航，从而实现超越传统抓取方式的全面数据提取。 对于需要在多个页面之间导航或与页面元素交互的复杂抽取任务，你可以通过 `/extract` 端点使用 FIRE-1 代理。 **示例 (cURL) ：**

```
curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "提取该论坛帖中的所有用户评论。",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

> FIRE-1 已上线，目前处于预览可用状态。

## 计费与使用方式跟踪

我们已简化计费：现在 Extract 与其他所有端点一样采用额度计费。每个额度相当于 15 个 token。 你可以通过[dashboard](https://www.firecrawl.dev/app/extract)监控 Extract 的使用方式。 有反馈或需要帮助？请发送邮件至 [help@firecrawl.com](mailto:help@firecrawl.com)。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化入门说明。