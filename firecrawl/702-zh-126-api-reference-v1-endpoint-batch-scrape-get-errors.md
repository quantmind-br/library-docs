---
title: 获取批量抓取错误 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:08:46.798694-03:00
rendered_js: false
word_count: 38
summary: This document describes the API endpoint for retrieving error logs and blocked URLs associated with a specific batch scrape job.
tags:
    - api-reference
    - batch-scraping
    - error-logs
    - robots-txt
    - firecrawl-api
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

GET

/

batch

/

scrape

/

{id}

/

errors

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

> 注意：新的 [此 API 的 v2 版本](https://docs.firecrawl.dev/zh/api-reference/endpoint/batch-scrape-get-errors) 现已提供，具备改进的错误报告和调试功能。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

在抓取时尝试访问但被 robots.txt 阻止的 URL 列表