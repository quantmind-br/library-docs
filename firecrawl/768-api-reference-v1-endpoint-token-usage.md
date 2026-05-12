---
title: Token Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/token-usage
source: sitemap
fetched_at: 2026-03-23T07:18:17.89789-03:00
rendered_js: false
word_count: 50
summary: This document provides the API specification for retrieving the current token usage and billing cycle information for an authenticated team.
tags:
    - api-endpoint
    - token-usage
    - authentication
    - billing-data
    - firecrawl-api
category: api
---

Get remaining tokens for the authenticated team (Extract only)

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

Get remaining tokens for the authenticated team (Extract only)

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

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/token-usage) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Response