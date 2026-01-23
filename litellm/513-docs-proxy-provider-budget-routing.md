---
title: Budget Routing | liteLLM
url: https://docs.litellm.ai/docs/proxy/provider_budget_routing
source: sitemap
fetched_at: 2026-01-21T19:53:17.311521537-03:00
rendered_js: false
word_count: 458
summary: This document explains how to configure and manage usage budgets in LiteLLM across providers, specific models, and metadata tags. It details the setup process for spend tracking, routing logic, and multi-instance synchronization using Redis.
tags:
    - litellm
    - budget-management
    - cost-control
    - proxy-configuration
    - redis
    - usage-limits
category: configuration
---

LiteLLM Supports setting the following budgets:

- Provider budget - $100/day for OpenAI, $100/day for Azure.
- Model budget - $100/day for gpt-4 [https://api-base-1](https://api-base-1), $100/day for gpt-4o [https://api-base-2](https://api-base-2)
- Tag budget - $10/day for tag=`product:chat-bot`, $100/day for tag=`product:chat-bot-2`

## Provider Budgets[​](#provider-budgets "Direct link to Provider Budgets")

Use this to set budgets for LLM Providers - example $100/day for OpenAI, $100/day for Azure.

### Quick Start[​](#quick-start "Direct link to Quick Start")

Set provider budgets in your `proxy_config.yaml` file

#### Proxy Config setup[​](#proxy-config-setup "Direct link to Proxy Config setup")

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

router_settings:
provider_budget_config:
openai:
budget_limit:0.000000000001# float of $ value budget for time period
time_period: 1d # can be 1d, 2d, 30d, 1mo, 2mo
azure:
budget_limit:100
time_period: 1d
anthropic:
budget_limit:100
time_period: 10d
vertex_ai:
budget_limit:100
time_period: 12d
gemini:
budget_limit:100
time_period: 12d

# OPTIONAL: Set Redis Host, Port, and Password if using multiple instance of LiteLLM
redis_host: os.environ/REDIS_HOST
redis_port: os.environ/REDIS_PORT
redis_password: os.environ/REDIS_PASSWORD

general_settings:
master_key: sk-1234
```

#### Make a test request[​](#make-a-test-request "Direct link to Make a test request")

We expect the first request to succeed, and the second request to fail since we cross the budget for `openai`

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/user_keys#request-format)

- Successful Call
- Unsuccessful call

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "hi my name is test request"}
    ]
  }'
```

#### How provider budget routing works[​](#how-provider-budget-routing-works "Direct link to How provider budget routing works")

1. **Budget Tracking**:
   
   - Uses Redis to track spend for each provider
   - Tracks spend over specified time periods (e.g., "1d", "30d")
   - Automatically resets spend after time period expires
2. **Routing Logic**:
   
   - Routes requests to providers under their budget limits
   - Skips providers that have exceeded their budget
   - If all providers exceed budget, raises an error
3. **Supported Time Periods**:
   
   - Seconds: "Xs" (e.g., "30s")
   - Minutes: "Xm" (e.g., "10m")
   - Hours: "Xh" (e.g., "24h")
   - Days: "Xd" (e.g., "1d", "30d")
   - Months: "Xmo" (e.g., "1mo", "2mo")
4. **Requirements**:
   
   - Redis required for tracking spend across instances
   - Provider names must be litellm provider names. See [Supported Providers](https://docs.litellm.ai/docs/providers)

### Monitoring Provider Remaining Budget[​](#monitoring-provider-remaining-budget "Direct link to Monitoring Provider Remaining Budget")

#### Get Budget, Spend Details[​](#get-budget-spend-details "Direct link to Get Budget, Spend Details")

Use this endpoint to check current budget, spend and budget reset time for a provider

Example Request

```
curl -X GET http://localhost:4000/provider/budgets \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234"
```

Example Response

```
{
"providers":{
"openai":{
"budget_limit":1e-12,
"time_period":"1d",
"spend":0.0,
"budget_reset_at":null
},
"azure":{
"budget_limit":100.0,
"time_period":"1d",
"spend":0.0,
"budget_reset_at":null
},
"anthropic":{
"budget_limit":100.0,
"time_period":"10d",
"spend":0.0,
"budget_reset_at":null
},
"vertex_ai":{
"budget_limit":100.0,
"time_period":"12d",
"spend":0.0,
"budget_reset_at":null
}
}
}
```

#### Prometheus Metric[​](#prometheus-metric "Direct link to Prometheus Metric")

LiteLLM will emit the following metric on Prometheus to track the remaining budget for each provider

This metric indicates the remaining budget for a provider in dollars (USD)

```
litellm_provider_remaining_budget_metric{api_provider="openai"} 10
```

## Model Budgets[​](#model-budgets "Direct link to Model Budgets")

Use this to set budgets for models - example $10/day for openai/gpt-4o, $100/day for openai/gpt-4o-mini

### Quick Start[​](#quick-start-1 "Direct link to Quick Start")

Set model budgets in your `proxy_config.yaml` file

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY
max_budget:0.000000000001# (USD)
budget_duration: 1d # (Duration. can be 1s, 1m, 1h, 1d, 1mo)
-model_name: gpt-4o-mini
litellm_params:
model: openai/gpt-4o-mini
api_key: os.environ/OPENAI_API_KEY
max_budget:100# (USD)
budget_duration: 30d # (Duration. can be 1s, 1m, 1h, 1d, 1mo)


```

#### Make a test request[​](#make-a-test-request-1 "Direct link to Make a test request")

We expect the first request to succeed, and the second request to fail since we cross the budget for `openai/gpt-4o`

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/user_keys#request-format)

- Successful Call
- Unsuccessful call

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "hi my name is test request"}
    ]
  }'
```

## ✨ Tag Budgets[​](#-tag-budgets "Direct link to ✨ Tag Budgets")

Use this to set budgets for tags - example $10/day for tag=`product:chat-bot`, $100/day for tag=`product:chat-bot-2`

### Quick Start[​](#quick-start-2 "Direct link to Quick Start")

Set tag budgets by setting `tag_budget_config` in your `proxy_config.yaml` file

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY

litellm_settings:
tag_budget_config:
product:chat-bot:# (Tag)
max_budget:0.000000000001# (USD)
budget_duration: 1d # (Duration)
product:chat-bot-2:# (Tag)
max_budget:100# (USD)
budget_duration: 1d # (Duration)
```

#### Make a test request[​](#make-a-test-request-2 "Direct link to Make a test request")

We expect the first request to succeed, and the second request to fail since we cross the budget for `openai/gpt-4o`

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/user_keys#request-format)

- Successful Call
- Unsuccessful call

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "hi my name is test request"}
    ],
    "metadata": {"tags": ["product:chat-bot"]}
  }'
```

## Multi-instance setup[​](#multi-instance-setup "Direct link to Multi-instance setup")

If you are using a multi-instance setup, you will need to set the Redis host, port, and password in the `proxy_config.yaml` file. Redis is used to sync the spend across LiteLLM instances.

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

router_settings:
provider_budget_config:
openai:
budget_limit:0.000000000001# float of $ value budget for time period
time_period: 1d # can be 1d, 2d, 30d, 1mo, 2mo

# 👇 Add this: Set Redis Host, Port, and Password if using multiple instance of LiteLLM
redis_host: os.environ/REDIS_HOST
redis_port: os.environ/REDIS_PORT
redis_password: os.environ/REDIS_PASSWORD

general_settings:
master_key: sk-1234
```

## Spec for provider\_budget\_config[​](#spec-for-provider_budget_config "Direct link to Spec for provider_budget_config")

The `provider_budget_config` is a dictionary where:

- **Key**: Provider name (string) - Must be a valid [LiteLLM provider name](https://docs.litellm.ai/docs/providers)
- **Value**: Budget configuration object with the following parameters:
  
  - `budget_limit`: Float value representing the budget in USD
  - `time_period`: Duration string in one of the following formats:
    
    - Seconds: `"Xs"` (e.g., "30s")
    - Minutes: `"Xm"` (e.g., "10m")
    - Hours: `"Xh"` (e.g., "24h")
    - Days: `"Xd"` (e.g., "1d", "30d")
    - Months: `"Xmo"` (e.g., "1mo", "2mo")

Example structure:

```
provider_budget_config:
openai:
budget_limit:100.0# $100 USD
time_period:"1d"# 1 day period
azure:
budget_limit:500.0# $500 USD
time_period:"30d"# 30 day period
anthropic:
budget_limit:200.0# $200 USD
time_period:"1mo"# 1 month period
gemini:
budget_limit:50.0# $50 USD
time_period:"24h"# 24 hour period
```