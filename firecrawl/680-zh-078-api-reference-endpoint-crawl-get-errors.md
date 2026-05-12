---
title: 获取抓取错误 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:09:47.720632-03:00
rendered_js: false
word_count: 30
summary: This document provides the API specification for retrieving error logs and identifying robots.txt blocked URLs for a specific crawl job.
tags:
    - api-endpoint
    - web-scraping
    - error-logs
    - robots-txt
    - firecrawl-api
    - crawl-status
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/crawl/{id}/errors \
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
  --url https://api.firecrawl.dev/v2/crawl/{id}/errors \
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

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 以获取自动化入门说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

尝试抓取但被 robots.txt 阻止的 URL 列表