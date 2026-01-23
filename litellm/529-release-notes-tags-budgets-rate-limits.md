---
title: One post tagged with "budgets/rate limits" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/budgets-rate-limits
source: sitemap
fetched_at: 2026-01-21T19:41:22.810540428-03:00
rendered_js: false
word_count: 59
summary: This document outlines how to configure usage budget tiers for rate limiting and details updates regarding logging improvements and custom guardrail parameters.
tags:
    - litellm
    - budget-management
    - rate-limiting
    - logging
    - guardrails
    - api-updates
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