---
title: 抓取已启动 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-crawl-started
source: sitemap
fetched_at: 2026-03-23T07:08:28.167926-03:00
rendered_js: false
word_count: 30
summary: This document describes the structure and fields of webhook notifications, including security signature verification, event types, and request payload identifiers.
tags:
    - webhook-configuration
    - hmac-signature
    - event-payload
    - api-security
    - data-delivery
category: reference
---

#### 请求头

原始请求体的 HMAC-SHA256 签名，格式为 `sha256=<hex>`。当你在[账户设置](https://www.firecrawl.dev/app/settings?tab=advanced)中配置了 HMAC 密钥时，该字段会出现。有关验证详情，请参阅 [Webhook 安全](https://docs.firecrawl.dev/webhooks/security)。

示例:

`"sha256=abc123def456789..."`

#### 请求体

事件类型。

Allowed value: `"crawl.started"`

爬取任务 ID，与 `POST /crawl` 返回的 `id` 一致。

此次 Webhook 投递的唯一标识符。可用于去重——重试时会发送相同的值。

你在 webhook 配置中提供的自定义元数据对象。每次投递时都会原样返回。

#### 响应