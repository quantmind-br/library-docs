---
title: 历史 Token 使用情况 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:09:03.396361-03:00
rendered_js: false
word_count: 52
summary: Provides an endpoint to retrieve historical token usage data for authenticated teams, including a breakdown by API key and billing period.
tags:
    - api-reference
    - token-usage
    - billing
    - historical-data
    - firecrawl-api
category: api
---

GET

/

team

/

token-usage

/

historical

获取已认证团队的历史 token 用量（仅限 Extract）

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/token-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalTokens": 1000
    }
  ]
}
```

按月返回历史 Token 使用情况。该端点也可选择按 API 密钥分解使用量。

我们已简化计费，将 Extract 与其他端点统一改为使用 credit。每个 credit 折合 15 个 token。报告的 token 使用量现在包含所有端点的使用。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化引导说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 查询参数

#### 响应