---
title: 获取爬取错误 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:08:11.236577-03:00
rendered_js: false
word_count: 27
summary: This document provides the API reference for retrieving error logs and URLs blocked by robots.txt during a crawl operation.
tags:
    - api-reference
    - crawl-errors
    - robots-txt
    - web-scraping
    - authentication
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
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

curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
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

> 注意：现已提供此 API 的全新 [v2 版本](https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-get-errors)，具备更强大的功能和更好的性能。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

在抓取时尝试访问但被 robots.txt 阻止的 URL 列表