---
title: クレジット使用状況 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:12:31.890214-03:00
rendered_js: false
word_count: 0
summary: This document represents a JSON response structure for a billing credit status check, providing information on remaining credits and the current billing cycle timeline.
tags:
    - api-response
    - billing-data
    - account-credits
    - usage-tracking
    - json-schema
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