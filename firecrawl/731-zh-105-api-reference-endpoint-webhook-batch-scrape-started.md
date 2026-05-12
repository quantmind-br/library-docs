---
title: 批量抓取已启动 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-batch-scrape-started
source: sitemap
fetched_at: 2026-03-23T07:08:44.548049-03:00
rendered_js: false
word_count: 26
summary: This document describes the structure of webhook request headers and bodies for batch scraping tasks, including authentication via HMAC-SHA256 signatures and payload metadata.
tags:
    - webhook
    - hmac-sha256
    - batch-scraping
    - api-security
    - request-headers
category: reference
---

#### 请求头

原始请求体的 HMAC-SHA256 签名，格式为 `sha256=<hex>`。当你在[账户设置](https://www.firecrawl.dev/app/settings?tab=advanced)中配置了 HMAC 密钥时，该字段会出现。有关验证详情，请参阅 [Webhook 安全](https://docs.firecrawl.dev/webhooks/security)。

示例:

`"sha256=abc123def456789..."`

#### 请求体

Allowed value: `"batch_scrape.started"`

批量抓取任务 ID，与 `POST /batch/scrape` 返回的 `id` 一致。

你在 webhook 配置中提供的自定义元数据对象。每次投递时都会原样返回。

#### 响应