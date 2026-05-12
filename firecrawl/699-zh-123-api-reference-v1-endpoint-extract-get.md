---
title: 获取提取状态 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:08:24.390121-03:00
rendered_js: false
word_count: 29
summary: This document provides the API endpoint reference for retrieving the status and results of a specific data extraction job using an authorization token.
tags:
    - api-reference
    - data-extraction
    - authentication
    - get-request
    - status-check
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}

curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

> 注意：此 API 的全新 [v2 版本](https://docs.firecrawl.dev/zh/api-reference/endpoint/extract-get) 现已推出，具备更强大的功能和更高的性能。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

提取作业的当前状态

可用选项:

`completed`,

`processing`,

`failed`,

`cancelled`