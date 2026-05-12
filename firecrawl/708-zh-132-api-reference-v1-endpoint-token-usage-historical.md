---
title: 历史 Token 使用情况 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:08:08.697744-03:00
rendered_js: false
word_count: 27
summary: This document describes an API endpoint for retrieving historical token usage for authenticated teams, with an option to break down statistics by API key.
tags:
    - api-documentation
    - token-usage
    - billing-metrics
    - analytics-endpoint
    - team-authentication
category: api
---

获取已认证团队的历史 Token 用量（仅限 Extract）

按月返回历史 Token 使用情况。该端点还可选按 API key 对使用情况进行细分。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 查询参数

#### 响应