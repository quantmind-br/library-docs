---
title: Change Tracking | Firecrawl
url: https://docs.firecrawl.dev/zh/features/change-tracking
source: sitemap
fetched_at: 2026-03-23T07:21:01.339506-03:00
rendered_js: false
word_count: 327
summary: This document explains how to use the change tracking feature in Firecrawl to monitor and compare web page content over time by detecting additions, removals, and modifications.
tags:
    - change-tracking
    - web-scraping
    - data-monitoring
    - git-diff
    - automation
    - api-integration
    - structured-data
category: guide
---

![变更追踪](https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f) Change tracking 会将页面的当前内容与上次抓取时的内容进行比较。将 `changeTracking` 添加到你的 `formats` 数组中，以检测页面是新增、未变化还是已修改，并 (可选) 获取结构化的差异信息，了解具体发生了哪些变更。

- 适用于 `/scrape`、`/crawl` 和 `/batch/scrape`
- 提供两种 diff 模式：用于行级变更的 `git-diff`，以及用于字段级比较的 `json`
- 作用范围限定在你的团队内，也可以按你传入的 tag 进一步限定

## 工作原理

每次启用 `changeTracking` 的抓取都会存储一个快照，并将其与该 URL 上一次抓取生成的快照进行比较。快照会被持久化存储且不会过期，因此无论两次抓取之间间隔多长时间，对比结果都能保持准确。

ScrapeResultFirst time`changeStatus: "new"` (不存在之前的版本)Content unchanged`changeStatus: "same"`Content modified`changeStatus: "changed"` (有可用的 diff 数据)Page removed`changeStatus: "removed"`

响应会在 `changeTracking` 对象中包含以下字段：

FieldTypeDescription`previousScrapeAt``string | null`上一次抓取的时间戳 (首次抓取时为 `null`)`changeStatus``string``"new"`、`"same"`、`"changed"` 或 `"removed"``visibility``string``"visible"` (可通过链接/站点地图发现) 或 `"hidden"` (URL 仍然可用但不再被链接)`diff``object | undefined`行级 diff (仅在 `git-diff` 模式且状态为 `"changed"` 时存在)`json``object | undefined`字段级比较 (仅在 `json` 模式且状态为 `"changed"` 时存在)

## 基本用法

在 `formats` 数组中同时包含 `markdown` 和 `changeTracking`。`markdown` 格式是必需的，因为变更跟踪会根据页面的 markdown 内容来比较差异。

### 响应

在首次抓取时，`changeStatus` 为 `"new"`，并且 `previousScrapeAt` 为 `null`：

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $9/mo\nPro: $29/mo...",
    "changeTracking": {
      "previousScrapeAt": null,
      "changeStatus": "new",
      "visibility": "visible"
    }
  }
}
```

在后续抓取中，`changeStatus` 表示内容是否发生了变化：

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $12/mo\nPro: $39/mo...",
    "changeTracking": {
      "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible"
    }
  }
}
```

## Git-diff 模式

`git-diff` 模式会以类似 `git diff` 的格式返回逐行的变更。向 `formats` 数组中传入一个包含 `modes: ["git-diff"]` 的对象：

### 响应

`diff` 对象同时包含纯文本 diff 和 JSON 结构化表示：

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "diff": {
      "text": "@@ -1,3 +1,3 @@\n # Pricing\n-Starter: $9/mo\n-Pro: $29/mo\n+Starter: $12/mo\n+Pro: $39/mo",
      "json": {
        "files": [{
          "chunks": [{
            "content": "@@ -1,3 +1,3 @@",
            "changes": [
              { "type": "normal", "content": "# Pricing" },
              { "type": "del", "ln": 2, "content": "Starter: $9/mo" },
              { "type": "del", "ln": 3, "content": "Pro: $29/mo" },
              { "type": "add", "ln": 2, "content": "Starter: $12/mo" },
              { "type": "add", "ln": 3, "content": "Pro: $39/mo" }
            ]
          }]
        }]
      }
    }
  }
}
```

结构化的 `diff.json` 对象包含：

- `files`：变更文件的数组 (网页通常只有一个文件)
- `chunks`：文件内的变更片段
- `changes`：逐行变更记录，包含 `type` (`"add"`、`"del"` 或 `"normal"`) 、行号 (`ln`) 以及 `content`

## JSON 模式

`json` 模式会基于你定义的 schema，同时从页面的当前版本和先前版本中提取指定字段。这样可以在不解析完整差异 (diff) 的情况下，跟踪价格、库存水平或元数据等结构化数据的变化。 在请求中传入 `modes: ["json"]`，并通过 `schema` 定义要提取的字段：

### 响应

schema 中的每个字段都会返回 `previous` 和 `current` 两个值：

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-05T08:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "json": {
      "price": {
        "previous": "$19.99",
        "current": "$24.99"
      },
      "availability": {
        "previous": "有货",
        "current": "有货"
      }
    }
  }
}
```

你也可以传入一个可选的 `prompt`，配合 schema 一起引导 LLM 进行抽取。

默认情况下，变更追踪会与你团队对同一 URL 最近一次的抓取结果进行比较。通过标签，你可以为同一 URL 维护**相互独立的追踪历史**，这在你以不同监控频率或在不同上下文下监控同一页面时非常有用。

## 使用变更追踪进行 Crawl

在 crawl 操作中添加变更追踪，用于监控整个站点的变更情况。将 `changeTracking` formats 传入 `scrapeOptions` 中：

## 使用变更跟踪的批量抓取

使用 [batch scrape](https://docs.firecrawl.dev/zh/features/batch-scrape) 功能来监控一组特定的 URL：

## 调度变更跟踪

当你按固定计划定期进行抓取时，变更跟踪的效果最佳。你可以使用 cron 任务、云调度服务或工作流工具来实现自动化。

### Cron 任务

创建一个脚本，用于抓取指定 URL，并在检测到变更时发送通知：

```
#!/bin/bash
RESPONSE=$(curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://competitor.com/pricing",
    "formats": [
      "markdown",
      {
        "type": "changeTracking",
        "modes": ["json"],
        "schema": {
          "type": "object",
          "properties": {
            "starter_price": { "type": "string" },
            "pro_price": { "type": "string" }
          }
        }
      }
    ]
  }')

STATUS=$(echo "$RESPONSE" | jq -r '.data.changeTracking.changeStatus')

if [ "$STATUS" = "changed" ]; then
  echo "$RESPONSE" | jq '.data.changeTracking.json'
  # 通过电子邮件、Slack 等发送告警
fi
```

使用 `crontab -e` 将其加入定时任务：

```
0 */6 * * * /path/to/check-pricing.sh >> /var/log/price-monitor.log 2>&1
```

调度计划表达式每小时`0 * * * *`每 6 小时一次`0 */6 * * *`每天上午 9 点`0 9 * * *`每周一上午 8 点`0 8 * * 1`

### 云端和无服务器调度器

- **AWS**：通过 EventBridge 规则触发 Lambda 函数
- **GCP**：通过 Cloud Scheduler 触发 Cloud Function
- **Vercel / Netlify**：由 Cron 触发的无服务器函数
- **GitHub Actions**：使用 `schedule` 和 `cron` 触发的定时工作流

### 工作流自动化

像 **n8n**、**Zapier** 和 **Make** 这样的无代码平台可以按设定的计划调用 Firecrawl API，并将结果发送到 Slack、电子邮件或数据库。请参阅 [工作流自动化指南](https://docs.firecrawl.dev/zh/developer-guides/workflow-automation/n8n)。

## Webhooks

对于 crawl 和批量 scrape 等异步操作，可以使用 [webhooks](https://docs.firecrawl.dev/zh/webhooks/overview) 在结果就绪时接收变更追踪结果，而无需轮询。

`crawl.page` 事件的负载 (payload) 中会为每个页面包含一个 `changeTracking` 对象：

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [{
    "markdown": "# 价格\n\nStarter: $12/mo...",
    "metadata": {
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "statusCode": 200
    },
    "changeTracking": {
      "previousScrapeAt": "2025-06-05T12:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible",
      "diff": {
        "text": "@@ -2,1 +2,1 @@\n-Starter: $9/mo\n+Starter: $12/mo"
      }
    }
  }]
}
```

有关 webhook 配置 (请求头 (headers) 、元数据 (metadata) 、事件 (events) 、重试机制、签名验证等) 的详细信息，请参阅 [Webhooks 文档](https://docs.firecrawl.dev/zh/webhooks/overview)。

## 配置参考

传入 `changeTracking` 格式对象时可用的全部配置项如下：

ParameterTypeDefaultDescription`type``string`(required)必须为 `"changeTracking"``modes``string[]``[]`要启用的 diff 模式：`"git-diff"`、`"json"`，或两者同时启用`schema``object`(none)用于字段级比较的 JSON Schema (`json` 模式下必填)`prompt``string`(none)用于引导 LLM 提取的自定义提示词 (与 `json` 模式配合使用)`tag``string``null`独立的变更跟踪历史标识符

### 数据模型

## 重要细节

- **快照保留**：快照会被持久化存储且不会过期。即使在距离上一次抓取数月之后才再次抓取，依然会与之前的快照进行正确比较。
- **作用范围**：比较的作用范围限定在你的团队内。你首次抓取任意 URL 时都会返回 `"new"`，即便其他用户之前抓取过它。
- **URL 匹配**：之前的抓取记录会基于精确的源 URL、team ID、`markdown` 格式和 `tag` 进行匹配。请在多次抓取之间保持 URL 一致。
- **参数一致性**：在针对同一 URL 的多次抓取中使用不同的 `includeTags`、`excludeTags` 或 `onlyMainContent` 设置会导致比较结果不可靠。
- **比较算法**：该算法对空白字符和内容顺序的变化具有鲁棒性。为处理验证码/反爬虫随机化，iframe 源 URL 会被忽略。
- **缓存**：带有 `changeTracking` 的请求会绕过索引缓存。`maxAge` 参数会被忽略。
- **错误处理**：留意响应中的 `warning` 字段，并处理 `changeTracking` 对象可能缺失的情况 (如果查询上一轮抓取记录的数据库操作超时，就可能出现这种情况) 。

## 计费

模式费用基础变更追踪无额外费用 (使用标准抓取额度)`git-diff` 模式无额外费用`json` 模式每页 5 个额度

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化接入说明。