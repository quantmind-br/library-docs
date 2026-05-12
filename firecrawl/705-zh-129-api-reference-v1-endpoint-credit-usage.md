---
title: 额度使用 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:08:18.959268-03:00
rendered_js: false
word_count: 0
summary: This document displays a JSON response structure providing a snapshot of current account credit usage and billing cycle information.
tags:
    - api-response
    - account-billing
    - credit-usage
    - json-schema
    - billing-cycle
category: api
---

```
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