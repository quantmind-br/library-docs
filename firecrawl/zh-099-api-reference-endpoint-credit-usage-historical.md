---
title: 历史积分用量 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:09:33.941745-03:00
rendered_js: false
word_count: 36
summary: This document describes the API endpoint for retrieving historical credit usage data on a monthly basis, with the option to filter by specific API keys.
tags:
    - api-reference
    - credit-usage
    - historical-data
    - billing-metrics
    - authentication
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/credit-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalCredits": 1000
    }
  ]
}
```

GET

/

team

/

credit-usage

/

historical

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/credit-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalCredits": 1000
    }
  ]
}
```

按月返回历史积分用量。该端点还可选按 API key 分解用量。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化引导说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 查询参数

#### 响应