---
title: 批量抓取 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:20:49.884387-03:00
rendered_js: false
word_count: 144
summary: 该文档介绍了如何使用 Firecrawl 的批量抓取功能，通过并发处理多个 URL 并支持同步与异步模式来实现高效的数据提取与 webhook 通知。
tags:
    - firecrawl
    - web-scraping
    - batch-processing
    - api-reference
    - webhooks
    - data-extraction
    - concurrency
category: api
---

批量抓取让你能够在单个任务中抓取多个 URL。传入一个 URL 列表和可选参数后，Firecrawl 会并发处理这些 URL，并一次性返回所有结果。

- 类似 `/crawl`，但适用于明确指定的一组 URL
- 支持同步和异步模式
- 支持所有抓取选项，包括结构化提取
- 可为每个任务配置并发数

## 工作方式

你可以通过两种方式运行批量抓取：

模式SDK 方法 (JS / Python)行为同步`batchScrape` / `batch_scrape`启动批量任务并等待其完成，返回所有结果异步`startBatchScrape` / `start_batch_scrape`启动批量任务并返回作业 ID，用于轮询或 Webhook

## 基本用法

### 响应

调用 `batchScrape` / `batch_scrape` 会在批处理完成后返回完整结果。

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

调用 `startBatchScrape` / `start_batch_scrape` 会返回一个作业 ID。你可以通过 `getBatchScrapeStatus` / `get_batch_scrape_status`、API 端点 `/batch/scrape/{id}`，或 webhooks 来跟踪进度。作业结果在完成后会通过 API 保留 24 小时。在此之后，你仍然可以在[活动日志](https://www.firecrawl.dev/app/logs)中查看批量抓取历史和结果。

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## 并发

默认情况下，批量抓取作业会使用你团队的全部浏览器并发上限 (参见 [Rate Limits](https://docs.firecrawl.dev/zh/rate-limits)) 。你可以通过 `maxConcurrency` 参数为每个作业降低并发数。 例如，`maxConcurrency: 50` 会将该作业限制为最多 50 个同时抓取。对于大批量作业，如果将这个值设得过低，会显著减慢处理速度，因此只有在你需要为其他并发作业预留容量时才应降低它。

你可以使用批量抓取，从该批次中的每个页面提取结构化数据。当你希望对一组 URL 应用相同的 schema 时，这会非常有用。

### 响应

`batchScrape` / `batch_scrape` 返回完整结果：

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
      "json": {
        "title": "使用 Groq Llama 3 打造“网站聊天”功能 | Firecrawl",
        "description": "了解如何结合使用 Firecrawl、Groq Llama 3 和 Langchain，构建一个可与您网站对话的聊天机器人。"
      }
    },
    ...
  ]
}
```

`startBatchScrape` / `start_batch_scrape` 返回任务 ID：

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Webhook

你可以配置 Webhook，在批次中的每个 URL 被抓取时接收实时通知。这样你可以立即处理结果，而无需等待整个批次完成。

```
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### 事件类型

事件描述`batch_scrape.started`批量抓取任务已开始`batch_scrape.page`单个 URL 已成功抓取`batch_scrape.completed`所有 URL 均已处理完毕`batch_scrape.failed`批量抓取任务遇到错误

### 载荷

每次 webhook 投递都包含一个 JSON 请求体，结构如下：

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "batch-job-id",
  "data": [...],
  "metadata": {},
  "error": null
}
```

### 验证 webhook 签名

来自 Firecrawl 的每个 webhook 请求都会包含一个 `X-Firecrawl-Signature` 请求头，其中包含一个 HMAC-SHA256 签名。始终验证该签名，以确保 webhook 是真实的且未被篡改。

1. 在你账号设置中的 [Advanced 选项卡](https://www.firecrawl.dev/app/settings?tab=advanced) 获取你的 webhook secret
2. 从 `X-Firecrawl-Signature` 请求头中提取签名
3. 使用你的 secret 对原始请求体计算 HMAC-SHA256
4. 使用时间安全 (timing-safe) 的比较函数将其与签名请求头的值进行比较

如需查看 JavaScript 和 Python 的完整实现示例，请参阅 [Webhook 安全文档](https://docs.firecrawl.dev/zh/webhooks/security)。 如需查看更全面的 webhook 文档，包括详细的事件负载、高级配置和故障排查，请参阅 [Webhooks 文档](https://docs.firecrawl.dev/zh/webhooks/overview)。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化入门说明。