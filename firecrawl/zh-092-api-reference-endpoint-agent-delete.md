---
title: 取消 Agent - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/agent-delete
source: sitemap
fetched_at: 2026-03-23T07:09:54.245865-03:00
rendered_js: false
word_count: 60
summary: This document provides the API specification for cancelling a pending or running agent task using the Firecrawl platform.
tags:
    - api-endpoint
    - agent-task
    - task-cancellation
    - rest-api
    - firecrawl-api
category: api
---

取消智能体任务

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'

{
  "success": true
}
```

DELETE

/

agent

/

{jobId}

取消智能体任务

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'

{
  "success": true
}
```

> 如果你是需要 Firecrawl API 密钥的 AI 代理，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化接入说明。

#### 授权

[​](#authorization-authorization)

Authorization

string

header

必填

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

[​](#parameter-job-id)

jobId

string&lt;uuid&gt;

必填

Agent 任务的 ID

#### 响应

200 - application/json

代理任务已成功取消

[​](#response-success)

success

boolean

[建议编辑](https://github.com/firecrawl/firecrawl-docs/edit/main/zh/api-reference/endpoint/agent-delete.mdx)[提出问题](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path%3A%20%2Fzh%2Fapi-reference%2Fendpoint%2Fagent-delete)

[获取 Agent 状态  
\
上一页](https://docs.firecrawl.dev/zh/api-reference/endpoint/agent-get)

[Extract  
\
下一页](https://docs.firecrawl.dev/zh/api-reference/endpoint/extract)