---
title: 取消批量抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:08:45.155931-03:00
rendered_js: false
word_count: 28
summary: This document provides the API specification for cancelling a batch scraping job using a DELETE request with Bearer token authentication.
tags:
    - api-reference
    - batch-scraping
    - http-delete
    - authorization
    - firecrawl-api
category: api
---

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}

curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> 注意：新的 [v2 版本 API](https://docs.firecrawl.dev/zh/api-reference/endpoint/batch-scrape-delete) 现已推出，具备改进的功能和性能。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

示例:

`"Batch scrape job successfully cancelled."`