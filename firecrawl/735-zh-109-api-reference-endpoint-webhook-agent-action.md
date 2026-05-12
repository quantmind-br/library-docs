---
title: 智能体操作 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-agent-action
source: sitemap
fetched_at: 2026-03-23T07:08:55.749723-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON representation of an agent action response, detailing the status, credits consumed, and operational data for a scraping task.
tags:
    - api-response
    - agent-action
    - web-scraping
    - json-schema
    - webhook-payload
category: api
---

```
{
  "success": true,
  "type": "agent.action",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "d4e5f6a7-0002-0000-0000-000000000000",
  "data": [
    {
      "creditsUsed": 5,
      "action": "scrape",
      "input": {
        "url": "https://example.com"
      }
    }
  ],
  "metadata": {}
}
```