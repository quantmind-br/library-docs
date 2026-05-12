---
title: クレジット利用状況 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:13:21.380569-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON response structure representing the current credit usage and billing cycle information for a user account.
tags:
    - api-response
    - billing-details
    - credit-usage
    - account-management
    - json-schema
category: api
---

```
{
  "success": true,
  "data": {
    "remainingCredits": 1000,
    "planCredits": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```