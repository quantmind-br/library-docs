---
title: 获取提取状态 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:09:22.219916-03:00
rendered_js: false
word_count: 34
summary: This document provides the API specification for retrieving the status and results of a Firecrawl extraction task using a specific ID.
tags:
    - api-endpoint
    - data-extraction
    - firecrawl
    - authentication
    - task-status
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z",
  "tokensUsed": 123
}

curl --request GET \
  --url https://api.firecrawl.dev/v2/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z",
  "tokensUsed": 123
}
```

> 如果你是需要 Firecrawl API 密钥的 AI 代理，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化接入说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

当前提取任务的状态

可用选项:

`completed`,

`processing`,

`failed`,

`cancelled`

提取任务使用的 token 数量。仅在任务完成后可查看。