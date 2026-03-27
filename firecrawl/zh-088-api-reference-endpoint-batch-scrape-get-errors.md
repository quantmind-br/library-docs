---
title: 获取批量抓取错误信息 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:09:36.766498-03:00
rendered_js: false
word_count: 39
summary: This document provides the API reference for retrieving error logs and blocked robots.txt URLs associated with a specific batch scraping task.
tags:
    - api-reference
    - firecrawl
    - batch-scraping
    - error-handling
    - robots-txt
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id}/errors \
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
  --url https://api.firecrawl.dev/v2/batch/scrape/{id}/errors \
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

> 如果你是需要 Firecrawl API 密钥的 AI 代理，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

尝试抓取但被 robots.txt 阻止的 URL 列表