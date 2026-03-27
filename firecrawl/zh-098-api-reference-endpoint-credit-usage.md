---
title: 积分使用情况 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:09:24.271066-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON schema representing a user's current subscription usage, including remaining credits and billing cycle timestamps.
tags:
    - api-response
    - usage-statistics
    - billing-data
    - subscription-management
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