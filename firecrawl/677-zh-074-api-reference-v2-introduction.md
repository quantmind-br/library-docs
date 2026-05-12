---
title: 简介 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v2-introduction
source: sitemap
fetched_at: 2026-03-23T07:31:53.781983-03:00
rendered_js: false
word_count: 54
summary: This document provides the foundational technical information for interacting with the Firecrawl API, including base URL, authentication procedures, HTTP status codes, and rate limiting policies.
tags:
    - web-scraping
    - api-documentation
    - authentication
    - rate-limiting
    - http-status-codes
category: reference
---

Firecrawl API 为你提供以编程方式访问 Web 数据的能力。所有端点共享同一个基础 URL、认证机制和响应格式，详见本页。

## 功能

## Agent 功能

## 基础 URL

所有请求都使用以下基础 URL：

```
https://api.firecrawl.dev
```

## 身份验证

每个请求必须在 `Authorization` 请求头中包含 API 密钥：

```
Authorization: Bearer fc-YOUR-API-KEY
```

在所有 API 调用中都要包含这个请求头。你可以在 [Firecrawl 控制台](https://www.firecrawl.dev/app/api-keys) 中找到你的 API 密钥。

## 响应代码

Firecrawl 使用标准的 HTTP 状态码来指示请求的结果。`2xx` 范围内的代码表示成功，`4xx` 代码表示客户端错误，`5xx` 代码表示服务器错误。

StatusDescription`200`请求成功。`400`请求参数无效。`401`缺少 API key 或 API key 无效。`402`需要付费。`404`未找到请求的资源。`429`超出速率限制。`5xx`Firecrawl 端的服务器错误。

当发生 `5xx` 错误时，响应体中会包含一个特定的错误码，帮助你诊断问题。

## 速率限制

Firecrawl API 会对所有端点实施速率限制，以确保服务稳定。速率限制是基于特定时间窗口内的请求数量设定的。 当你超过速率限制时，API 会返回 `429` 状态码。请在短暂延迟后再重试该请求。