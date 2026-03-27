---
title: Token Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/token-usage
source: sitemap
fetched_at: 2026-03-23T07:08:01.486638-03:00
rendered_js: false
word_count: 28
summary: This document provides the API endpoint and usage instructions for retrieving the remaining Extract token balance for an authenticated team.
tags:
    - api-reference
    - token-usage
    - account-management
    - extract-api
    - billing-information
category: api
---

获取当前已认证团队的剩余 Token（仅限 Extract）

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_tokens": 1000,
    "plan_tokens": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

获取当前已认证团队的剩余 Token（仅限 Extract）

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_tokens": 1000,
    "plan_tokens": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

> 注意：此 API 的 [v2 新版本](https://docs.firecrawl.dev/zh/api-reference/endpoint/token-usage) 现已上线，提供更强大的功能和更优的性能。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 响应