---
title: One post tagged with "key management" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/key-management
source: sitemap
fetched_at: 2026-01-21T19:41:44.786889605-03:00
rendered_js: false
word_count: 59
summary: This document provides instructions on defining usage tiers with rate limits and highlights updates regarding logging fixes, fine-tuning observability, and customizable guardrail parameters.
tags:
    - rate-limiting
    - budget-management
    - api-logging
    - guardrails
    - observability
    - litellm-updates
category: configuration
---

Define tiers with rate limits. Assign them to keys.

Use this to control access and budgets across a lot of keys.

```
curl -L -X POST 'http://0.0.0.0:4000/budget/new' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "budget_id": "high-usage-tier",
    "model_max_budget": {
        "gpt-4o": {"rpm_limit": 1000000}
    }
}'
```

LiteLLM was double logging litellm\_request span. This is now fixed.

Logs for finetuning requests are now available on all logging providers (e.g. Datadog).

You can now set custom parameters (like success threshold) for your guardrails in each request.