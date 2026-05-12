---
title: Webhook 事件类型 | Firecrawl
url: https://docs.firecrawl.dev/zh/webhooks/events
source: sitemap
fetched_at: 2026-03-23T07:28:02.289093-03:00
rendered_js: false
word_count: 72
summary: This document provides a comprehensive technical reference for webhook events, detailing the payload structure and specific event triggers for crawling, batch scraping, data extraction, and agent-based tasks.
tags:
    - webhooks
    - api-reference
    - event-driven
    - data-scraping
    - automation
category: reference
---

## 快速参考

事件触发条件`crawl.started`爬取任务开始处理`crawl.page`在爬取过程中抓取某个页面时`crawl.completed`爬取任务结束，且所有页面均已处理完成`batch_scrape.started`批量抓取作业开始处理`batch_scrape.page`在批量抓取过程中抓取某个 URL 时`batch_scrape.completed`批次中的所有 URL 均已处理完成`extract.started`提取任务开始处理`extract.completed`提取成功完成`extract.failed`提取失败`agent.started`代理任务开始处理`agent.action`代理执行某个工具（抓取、搜索等）`agent.completed`代理成功完成`agent.failed`代理遇到错误`agent.cancelled`代理任务被用户取消

## 负载结构

所有 webhook 事件均采用以下结构：

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

字段类型描述`success`boolean操作是否成功`type`string事件类型（例如 `crawl.page`）`id`string任务 ID`data`array与事件相关的数据（见下方示例）`metadata`object来自你在 webhook 配置中的自定义元数据`error`string错误信息（当 `success` 为 `false` 时）

## 爬取事件

### `crawl.started`

在爬取任务开始处理时发送。

```
{
  "success": true,
  "type": "crawl.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

在爬取过程中，每抓取到一个页面就会发送此事件。`data` 数组包含页面内容和元数据。

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# 页面内容……",
      "metadata": {
        "title": "页面标题",
        "description": "页面说明",
        "url": "https://example.com/page",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com/page",
        "proxyUsed": "basic",
        "cacheState": "命中",
        "cachedAt": "2025-09-03T21:11:25.636Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `crawl.completed`

在爬取任务结束且所有页面都已处理时发送。

```
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## 批量抓取事件

### `batch_scrape.started`

在批量抓取任务开始处理时发送。

```
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `batch_scrape.page`

针对批处理中每个被抓取的 URL 发送。`data` 数组包含页面内容和元数据。

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "页面描述",
        "url": "https://example.com",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com",
        "proxyUsed": "basic",
        "cacheState": "miss",
        "cachedAt": "2025-09-03T23:30:53.434Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `batch_scrape.completed`

在批次中的所有 URL 均处理完成后发送。

```
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

当提取任务开始处理时发送。

```
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

在提取操作成功完成后发送。`data` 数组包含提取的数据和用量信息。

```
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "示例网站", "category": "科技" },
      "extractId": "550e8400-e29b-41d4-a716-446655440000",
      "llmUsage": 0.0020118,
      "totalUrlsScraped": 1,
      "sources": {
        "siteName": ["https://example.com"],
        "category": ["https://example.com"]
      }
    }
  ],
  "metadata": {}
}
```

当提取失败时发送。`error` 字段中包含失败原因。

```
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "提取数据失败：超时已超出",
  "metadata": {}
}
```

## Agent 事件

### `agent.started`

当 Agent 任务开始执行时发送。

```
{
  "success": true,
  "type": "agent.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `agent.action`

在每次调用工具（scrape、search 等）后发送。

```
{
  "success": true,
  "type": "agent.action",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 5,
      "action": "mcp__tools__scrape",
      "input": {
        "url": "https://example.com"
      }
    }
  ],
  "metadata": {}
}
```

### `agent.completed`

当 agent 成功完成时会发送该事件。`data` 数组包含提取的数据以及消耗的总额度（credits）。

```
{
  "success": true,
  "type": "agent.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 15,
      "data": {
        "company": "示例公司",
        "industry": "技术",
        "founded": 2020
      }
    }
  ],
  "metadata": {}
}
```

### `agent.failed`

当 agent 遇到错误时会发送该事件。`error` 字段包含失败原因。

```
{
  "success": false,
  "type": "agent.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 8
    }
  ],
  "error": "Max credits exceeded",
  "metadata": {}
}
```

### `agent.cancelled`

当用户取消代理作业时发送。

```
{
  "success": false,
  "type": "agent.cancelled",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 3
    }
  ],
  "metadata": {}
}
```

## 事件过滤

默认情况下，你会接收到所有事件。若只想订阅特定事件，请在 webhook 配置中通过指定 `events` 数组：

```
{
  "url": "https://your-app.com/webhook",
  "events": ["completed", "failed"]
}
```

如果你只关心任务是否完成，而不需要逐页级更新时，这会很有用。