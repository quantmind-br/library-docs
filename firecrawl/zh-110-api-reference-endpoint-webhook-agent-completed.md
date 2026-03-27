---
title: 智能体已完成 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-agent-completed
source: sitemap
fetched_at: 2026-03-23T07:09:00.668812-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON response structure representing the completion status of an agent process, including metadata, credit usage, and extracted business information.
tags:
    - api-response
    - agent-completion
    - webhook-payload
    - data-extraction
category: api
---

```
{
  "success": true,
  "type": "agent.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "d4e5f6a7-0003-0000-0000-000000000000",
  "data": [
    {
      "creditsUsed": 15,
      "data": {
        "company": "Example Corp",
        "industry": "Technology",
        "founded": 2020
      }
    }
  ],
  "metadata": {}
}
```