---
title: Zero Data Retention - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/security_compliance/data_handling
source: sitemap
fetched_at: 2026-04-27T20:18:14.833280821-03:00
rendered_js: false
word_count: 243
summary: This document explains Fireworks' default zero data retention policy, detailing how prompt and generation data are handled by default, when metadata is logged, and how users can opt into logging for advanced features.
tags:
    - data-retention
    - zero-logging
    - api-storage
    - prompt-caching
    - conversation-data
    - fireworks
category: concept
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks has Zero Data Retention by default. Specifically, this means:

- Fireworks does **not** log or store prompt or generation data for any open models, without explicit user opt-in.
  - Prompt and generation data exist only in volatile memory for the duration of the request. If [[072-guides-prompt-caching|prompt caching]] is active (`#data-privacy`), some prompt data (and associated KV caches) can be stored in volatile memory for several minutes. In either case, prompt and generation data are not logged into any persistent storage.
- Fireworks logs metadata (e.g., number of tokens in a request) as required to deliver the service.
- Users can explicitly opt-in to log prompt and generation data for certain advanced features (e.g., FireOptimizer).

## Response API data retention

For the Response API specifically, Fireworks retains conversation data with the following policy when the API request has `store=True` (the default):

| Setting | Behavior |
|---|---|
| **What is stored** | User prompts, model responses, and tools called by the model |
| **Opt-out** | Set `store=False` in API requests to prevent any conversation data from being retained |
| **Retention period** | All stored conversation data is automatically deleted after 30 days |
| **Immediate deletion** | Use the DELETE API endpoint with the `response_id` to permanently remove a record |

> [!note]
> This retention policy is designed to be consistent with the OpenAI API while providing users control over their data storage preferences.

#data-retention #zero-logging #api-storage #prompt-caching #conversation-data #fireworks
