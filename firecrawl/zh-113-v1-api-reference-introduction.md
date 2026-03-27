---
title: 简介 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/v1/api-reference/introduction
source: sitemap
fetched_at: 2026-03-23T07:36:51.163236-03:00
rendered_js: false
word_count: 47
summary: This document provides the foundational technical specifications for the Firecrawl API, including base URL configuration, authentication procedures, status code handling, and rate limit policies.
tags:
    - api-documentation
    - authentication
    - rate-limiting
    - http-status-codes
    - developer-guide
category: reference
---

## [​](#%E5%8A%9F%E8%83%BD) 功能

## [​](#%E4%BB%A3%E7%90%86%E7%89%B9%E6%80%A7) 代理特性

## [​](#%E5%9F%BA%E7%A1%80-url) 基础 URL

所有请求使用以下基础 URL：

```
https://api.firecrawl.dev
```

## [​](#%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81) 身份验证

进行身份验证时，需要在请求中包含 Authorization 头。其值应为 `Bearer fc-123456789`，其中 `fc-123456789` 是你的 API 密钥。

```
Authorization：Bearer fc-123456789
```

​

## [​](#%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81) 响应代码

Firecrawl 使用常规 HTTP 状态码来表示请求结果。 通常，2xx 表示成功，4xx 表示与用户相关的错误，5xx 表示基础设施问题。

StatusDescription200请求成功。400请检查参数是否正确。401未提供 API key。402需要付款。404找不到请求的资源。429超出速率限制。5xx表示 Firecrawl 的服务器错误。

请参阅“错误代码”部分，了解所有可能的 API 错误的详细说明。

## [​](#%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6) 速率限制

Firecrawl API 设有速率限制，以确保服务的稳定性和可靠性。该限制适用于所有端点，按特定时间窗口内的请求次数计量。 当你超出速率限制时，将会收到 429 状态码。