---
title: エージェント完了 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-agent-completed
source: sitemap
fetched_at: 2026-03-23T07:13:11.473637-03:00
rendered_js: false
word_count: 0
summary: This document provides an example of a JSON webhook response payload generated after the successful completion of an agent task.
tags:
    - webhook-response
    - api-payload
    - agent-automation
    - json-schema
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