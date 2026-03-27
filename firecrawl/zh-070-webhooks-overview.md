---
title: Webhooks | Firecrawl
url: https://docs.firecrawl.dev/zh/webhooks/overview
source: sitemap
fetched_at: 2026-03-23T07:36:47.690613-03:00
rendered_js: false
word_count: 56
summary: This document explains how to configure and use webhooks in the Firecrawl API to receive real-time notifications for crawling and scraping operations.
tags:
    - webhook-configuration
    - api-integration
    - real-time-notifications
    - data-scraping
    - asynchronous-tasks
    - event-handling
category: configuration
---

Webhooks 让你能够随着操作进展实时接收通知，而无需主动轮询状态。

## 支持的操作

操作事件Crawl`started`, `page`, `completed`Batch Scrape`started`, `page`, `completed`Extract`started`, `completed`, `failed`Agent`started`, `action`, `completed`, `failed`, `cancelled`

## 配置

在你的请求中添加一个 `webhook` 对象：

```
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["started", "page", "completed", "failed"]
  }
}
```

字段类型必填描述`url`string是你的端点 URL（HTTPS）`headers`object否要附带的自定义请求头`metadata`object否包含在负载中的自定义数据`events`array否要接收的事件类型（默认：全部）

## 用法

### 通过 Webhook 爬取

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### 通过 Webhook 进行批量抓取

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

## 超时与重试

你的 endpoint 必须在 **10 秒** 内返回 `2xx` 状态码。 如果发送失败（超时、非 2xx 状态码或网络错误），Firecrawl 会自动重试：

重试次数失败后的延迟时间第 1 次1 分钟第 2 次5 分钟第 3 次15 分钟

在 3 次重试均失败后，该 webhook 会被标记为失败，不再进行后续尝试。