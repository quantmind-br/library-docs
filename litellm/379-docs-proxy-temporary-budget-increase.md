---
title: ✨ Temporary Budget Increase | liteLLM
url: https://docs.litellm.ai/docs/proxy/temporary_budget_increase
source: sitemap
fetched_at: 2026-01-21T19:53:48.852311902-03:00
rendered_js: false
word_count: 46
summary: This document provides instructions on how to create a LiteLLM Virtual Key and apply a temporary budget increase with an expiration date.
tags:
    - litellm
    - virtual-key
    - budget-management
    - api-configuration
    - cost-control
    - key-management
category: guide
---

Set temporary budget increase for a LiteLLM Virtual Key. Use this if you get asked to increase the budget for a key temporarily.

HierarchySupportedLiteLLM Virtual Key✅User❌Team❌Organization❌

1. Create a LiteLLM Virtual Key with budget

```
curl -L -X POST 'http://localhost:4000/key/generate' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer LITELLM_MASTER_KEY' \
-d '{
    "max_budget": 0.0000001
}'
```

Expected response:

```
{
"key":"sk-your-new-key"
}
```

2. Update key with temporary budget increase

```
curl -L -X POST 'http://localhost:4000/key/update' \
-H 'Authorization: Bearer LITELLM_MASTER_KEY' \
-H 'Content-Type: application/json' \
-d '{
    "key": "sk-your-new-key",
    "temp_budget_increase": 100, 
    "temp_budget_expiry": "2025-01-15"
}'
```

3. Test it!

```
curl -L -X POST 'http://localhost:4000/chat/completions' \
-H 'Authorization: Bearer sk-your-new-key' \
-H 'Content-Type: application/json' \
-d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello, world!"}]
}'
```

Expected Response Header:

```
x-litellm-key-max-budget: 100.0000001
```