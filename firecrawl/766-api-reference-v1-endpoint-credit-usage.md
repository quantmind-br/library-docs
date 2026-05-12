---
title: Credit Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:18:29.516464-03:00
rendered_js: false
word_count: 46
summary: This document describes the API endpoint for retrieving the current credit usage, plan limits, and billing cycle information for an authenticated team.
tags:
    - api-endpoint
    - credit-usage
    - billing-information
    - bearer-authentication
    - firecrawl-api
category: api
---

Get remaining credits for the authenticated team

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_credits": 1000,
    "plan_credits": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

Get remaining credits for the authenticated team

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_credits": 1000,
    "plan_credits": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/credit-usage) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Response