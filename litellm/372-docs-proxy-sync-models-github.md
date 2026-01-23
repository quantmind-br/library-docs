---
title: Auto Sync New Models (Day-0 Launches) | liteLLM
url: https://docs.litellm.ai/docs/proxy/sync_models_github
source: sitemap
fetched_at: 2026-01-21T19:53:41.930603373-03:00
rendered_js: false
word_count: 142
summary: This document explains how to use LiteLLM's auto-sync feature to update model pricing and context window data dynamically without restarting the service.
tags:
    - litellm
    - model-pricing
    - auto-sync
    - dynamic-configuration
    - api-management
    - zero-downtime
category: guide
---

Automatically keep your model pricing and context window data up to date without restarting your service. **This allows you to add day-0 support for new models without restarting your service.**

## Overview[​](#overview "Direct link to Overview")

When providers like OpenAI or Anthropic release new models (e.g., GPT-5, Claude 4), you typically need to restart your LiteLLM service to get the latest pricing and context window data.

With auto-sync, LiteLLM automatically pulls the latest model data from GitHub's [`model_prices_and_context_window.json`](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json) without requiring a restart. This means:

- **Zero downtime** when new models are released
- **Always accurate pricing** for cost tracking and budgets
- **Automatic updates** - set it once and forget it

## Quick Start[​](#quick-start "Direct link to Quick Start")

**Manual sync:**

```
curl -X POST "https://your-proxy-url/reload/model_cost_map" \
  -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  -H "Content-Type: application/json"
```

**Automatic sync every 6 hours:**

```
curl -X POST "https://your-proxy-url/schedule/model_cost_map_reload?hours=6" \
  -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  -H "Content-Type: application/json"
```

## API Endpoints[​](#api-endpoints "Direct link to API Endpoints")

EndpointMethodDescription`/reload/model_cost_map`POSTManual sync`/schedule/model_cost_map_reload?hours={hours}`POSTSchedule periodic sync`/schedule/model_cost_map_reload`DELETECancel scheduled sync`/schedule/model_cost_map_reload/status`GETCheck sync status

**Authentication:** Requires admin role or master key

## Python Example[​](#python-example "Direct link to Python Example")

```
import requests

defsync_models(proxy_url, admin_token):
    response = requests.post(
f"{proxy_url}/reload/model_cost_map",
        headers={"Authorization":f"Bearer {admin_token}"}
)
return response.json()

# Usage
result = sync_models("https://your-proxy-url","your-admin-token")
print(result['message'])
```

## Configuration[​](#configuration "Direct link to Configuration")

**Custom model cost map URL:**

```
export LITELLM_MODEL_COST_MAP_URL="https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json"
```

**Use local model cost map:**

```
export LITELLM_LOCAL_MODEL_COST_MAP=True
```