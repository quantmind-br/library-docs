---
title: エージェントをキャンセルする - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/agent-delete
source: sitemap
fetched_at: 2026-03-23T07:13:56.435274-03:00
rendered_js: false
word_count: 52
summary: This document provides the API endpoint specification for canceling an active agent job within the Firecrawl platform using a unique job identifier.
tags:
    - firecrawl-api
    - agent-job
    - delete-request
    - api-reference
    - job-management
category: api
---

エージェントジョブをキャンセルする

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

エージェントジョブをキャンセルする

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'

{
  "success": true
}
```

> Firecrawl APIキーが必要なAIエージェントの方は、自動オンボーディング手順については [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

[​](#authorization-authorization)

Authorization

string

header

必須

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

[​](#parameter-job-id)

jobId

string&lt;uuid&gt;

必須

エージェントジョブのID

#### レスポンス

200 - application/json

エージェントジョブが正常にキャンセルされました

[​](#response-success)

success

boolean

[編集を提案](https://github.com/firecrawl/firecrawl-docs/edit/main/ja/api-reference/endpoint/agent-delete.mdx)[問題を報告](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path%3A%20%2Fja%2Fapi-reference%2Fendpoint%2Fagent-delete)

[エージェントのステータスを取得  
\
前へ](https://docs.firecrawl.dev/ja/api-reference/endpoint/agent-get)

[Extract  
\
次へ](https://docs.firecrawl.dev/ja/api-reference/endpoint/extract)