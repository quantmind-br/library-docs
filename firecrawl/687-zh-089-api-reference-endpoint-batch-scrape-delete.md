---
title: 取消批量抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:09:55.978932-03:00
rendered_js: false
word_count: 31
summary: This document provides the API endpoint and authentication requirements for cancelling a batch scraping job using the Firecrawl service.
tags:
    - api-endpoint
    - batch-scraping
    - http-delete
    - bearer-authentication
    - job-cancellation
category: api
---

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}

curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

示例:

`"Batch scrape job successfully cancelled."`