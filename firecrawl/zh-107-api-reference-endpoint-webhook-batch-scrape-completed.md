---
title: 批量抓取完成 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-batch-scrape-completed
source: sitemap
fetched_at: 2026-03-23T07:09:05.331972-03:00
rendered_js: false
word_count: 23
summary: This document outlines the request header and body structure for webhook notifications, specifically detailing HMAC-SHA256 signature verification and payload fields.
tags:
    - webhook
    - hmac-signature
    - api-security
    - request-headers
    - webhook-payload
category: reference
---

#### 请求头

原始请求体的 HMAC-SHA256 签名，格式为 `sha256=<hex>`。当你在[账户设置](https://www.firecrawl.dev/app/settings?tab=advanced)中配置了 HMAC 密钥时，该字段会出现。有关验证详情，请参阅 [Webhook 安全](https://docs.firecrawl.dev/webhooks/security)。

示例:

`"sha256=abc123def456789..."`

#### 请求体

Allowed value: `"batch_scrape.completed"`

空数组。请通过 `GET /batch/scrape/{id}` 获取结果。

你在 webhook 配置中提供的自定义元数据对象。每次投递时都会原样返回。

#### 响应