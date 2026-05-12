---
title: 历史积分使用情况 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:08:15.29248-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a JSON response containing credit allocation periods associated with a specific API key.
tags:
    - json-schema
    - api-response
    - credit-allocation
    - billing-data
category: api
---

```
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