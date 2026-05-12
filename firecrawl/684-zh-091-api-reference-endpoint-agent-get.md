---
title: 获取 Agent 状态 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/agent-get
source: sitemap
fetched_at: 2026-03-23T07:09:51.702358-03:00
rendered_js: false
word_count: 41
summary: This document provides the API reference for checking the status and retrieving data from a Firecrawl agent job.
tags:
    - api-reference
    - firecrawl-api
    - agent-job
    - data-extraction
    - bearer-authentication
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "status": "processing",
  "data": {},
  "model": "spark-1-pro",
  "error": "<string>",
  "expiresAt": "2023-11-07T05:31:56Z",
  "creditsUsed": 123
}

curl --request GET \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "status": "processing",
  "data": {},
  "model": "spark-1-pro",
  "error": "<string>",
  "expiresAt": "2023-11-07T05:31:56Z",
  "creditsUsed": 123
}
```

> 如果你是需要 Firecrawl API 密钥的 AI 代理，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化入门说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应

可用选项:

`processing`,

`completed`,

`failed`

提取的数据（仅在状态为 completed 时可用）

model

enum&lt;string&gt;

默认值:spark-1-pro

本次 Agent 运行所使用的模型预设

可用选项:

`spark-1-pro`,

`spark-1-mini`