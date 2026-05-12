---
title: Agent 执行失败 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-agent-failed
source: sitemap
fetched_at: 2026-03-23T07:09:14.681368-03:00
rendered_js: false
word_count: 0
summary: This document describes the structure and fields of a JSON error response returned when an agent execution fails due to credit exhaustion.
tags:
    - api-response
    - error-handling
    - webhook-payload
    - credit-limit
    - json-schema
category: api
---

```
{
  "success": false,
  "type": "agent.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "d4e5f6a7-0004-0000-0000-000000000000",
  "data": [
    {
      "creditsUsed": 8
    }
  ],
  "error": "Max credits exceeded",
  "metadata": {}
}
```