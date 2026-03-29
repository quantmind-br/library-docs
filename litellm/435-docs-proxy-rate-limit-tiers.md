---
title: ✨ Budget / Rate Limit Tiers | liteLLM
url: https://docs.litellm.ai/docs/proxy/rate_limit_tiers
source: sitemap
fetched_at: 2026-01-21T19:53:25.54865934-03:00
rendered_js: false
word_count: 61
summary: This document provides instructions on defining tiers with rate limits and assigning these budgets to API keys for centralized access and resource control.
tags:
    - litellm
    - rate-limiting
    - budget-management
    - api-keys
    - enterprise-features
    - access-control
category: guide
---

Define tiers with rate limits. Assign them to keys.

Use this to control access and budgets across a lot of keys.

info

This is a LiteLLM Enterprise feature.

Get a 7 day free trial + get in touch [here](https://litellm.ai/#trial).

See pricing [here](https://litellm.ai/#pricing).

## 1. Create a budget[​](#1-create-a-budget "Direct link to 1. Create a budget")

```
curl -L -X POST 'http://0.0.0.0:4000/budget/new' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "budget_id": "my-test-tier",
    "rpm_limit": 0
}'
```

## 2. Assign budget to a key[​](#2-assign-budget-to-a-key "Direct link to 2. Assign budget to a key")

```
curl -L -X POST 'http://0.0.0.0:4000/key/generate' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "budget_id": "my-test-tier"
}'
```

Expected Response:

```
{
"key":"sk-...",
"budget_id":"my-test-tier",
"litellm_budget_table":{
"budget_id":"my-test-tier",
"rpm_limit":0
}
}
```

## 3. Check if budget is enforced on key[​](#3-check-if-budget-is-enforced-on-key "Direct link to 3. Check if budget is enforced on key")

```
curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-...' \ # 👈 KEY from step 2.
-d '{
    "model": "<REPLACE_WITH_MODEL_NAME_FROM_CONFIG.YAML>",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan"}
    ]
}'
```

## [API Reference](https://litellm-api.up.railway.app/#/budget%20management)[​](#api-reference "Direct link to api-reference")