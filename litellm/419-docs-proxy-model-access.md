---
title: Restrict Model Access | liteLLM
url: https://docs.litellm.ai/docs/proxy/model_access
source: sitemap
fetched_at: 2026-01-21T19:52:56.8286848-03:00
rendered_js: false
word_count: 296
summary: This document explains how to manage access to specific models using virtual keys and team IDs, while also describing how to discover model metadata and fallbacks via the API.
tags:
    - access-control
    - litellm-proxy
    - model-restriction
    - api-keys
    - team-management
    - fallback-models
category: guide
---

## **Restrict models by Virtual Key**[​](#restrict-models-by-virtual-key "Direct link to restrict-models-by-virtual-key")

Set allowed models for a key using the `models` param

```
curl 'http://0.0.0.0:4000/key/generate' \
--header 'Authorization: Bearer <your-master-key>' \
--header 'Content-Type: application/json' \
--data-raw '{"models": ["gpt-3.5-turbo", "gpt-4"]}'
```

info

This key can only make requests to `models` that are `gpt-3.5-turbo` or `gpt-4`

Verify this is set correctly by

- Allowed Access
- Disallowed Access

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

### [API Reference](https://litellm-api.up.railway.app/#/key%20management/generate_key_fn_key_generate_post)[​](#api-reference "Direct link to api-reference")

## **Restrict models by `team_id`**[​](#restrict-models-by-team_id "Direct link to restrict-models-by-team_id")

`litellm-dev` can only access `azure-gpt-3.5`

**1. Create a team via `/team/new`**

```
curl --location 'http://localhost:4000/team/new' \
--header 'Authorization: Bearer <your-master-key>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "team_alias": "litellm-dev",
  "models": ["azure-gpt-3.5"]
}' 

# returns {...,"team_id": "my-unique-id"}
```

**2. Create a key for team**

```
curl --location 'http://localhost:4000/key/generate' \
--header 'Authorization: Bearer sk-1234' \
--header 'Content-Type: application/json' \
--data-raw '{"team_id": "my-unique-id"}'
```

**3. Test it**

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer sk-qo992IjKOC2CHKZGRoJIGA' \
    --data '{
        "model": "BEDROCK_GROUP",
        "messages": [
            {
                "role": "user",
                "content": "hi"
            }
        ]
    }'
```

```
{"error":{"message":"Invalid model for team litellm-dev: BEDROCK_GROUP.  Valid models for team are: ['azure-gpt-3.5']\n\n\nTraceback (most recent call last):\n  File \"/Users/ishaanjaffer/Github/litellm/litellm/proxy/proxy_server.py\", line 2298, in chat_completion\n    _is_valid_team_configs(\n  File \"/Users/ishaanjaffer/Github/litellm/litellm/proxy/utils.py\", line 1296, in _is_valid_team_configs\n    raise Exception(\nException: Invalid model for team litellm-dev: BEDROCK_GROUP.  Valid models for team are: ['azure-gpt-3.5']\n\n","type":"None","param":"None","code":500}}%            
```

### [API Reference](https://litellm-api.up.railway.app/#/team%20management/new_team_team_new_post)[​](#api-reference-1 "Direct link to api-reference-1")

## **View Available Fallback Models**[​](#view-available-fallback-models "Direct link to view-available-fallback-models")

Use the `/v1/models` endpoint to discover available fallback models for a given model. This helps you understand which backup models are available when your primary model is unavailable or restricted.

Extension Point

The `include_metadata` parameter serves as an extension point for exposing additional model metadata in the future. While currently focused on fallback models, this approach will be expanded to include other model metadata such as pricing information, capabilities, rate limits, and more.

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

Get all available models:

```
curl -X GET 'http://localhost:4000/v1/models' \
  -H 'Authorization: Bearer <your-api-key>'
```

### Get Fallback Models with Metadata[​](#get-fallback-models-with-metadata "Direct link to Get Fallback Models with Metadata")

Include metadata to see fallback model information:

```
curl -X GET 'http://localhost:4000/v1/models?include_metadata=true' \
  -H 'Authorization: Bearer <your-api-key>'
```

### Get Specific Fallback Types[​](#get-specific-fallback-types "Direct link to Get Specific Fallback Types")

You can specify the type of fallbacks you want to see:

- General Fallbacks
- Context Window Fallbacks
- Content Policy Fallbacks

```
curl -X GET 'http://localhost:4000/v1/models?include_metadata=true&fallback_type=general' \
  -H 'Authorization: Bearer <your-api-key>'
```

General fallbacks are alternative models that can handle the same types of requests.

### Example Response[​](#example-response "Direct link to Example Response")

When `include_metadata=true` is specified, the response includes fallback information:

```
{
"data":[
{
"id":"gpt-4",
"object":"model",
"created":1677610602,
"owned_by":"openai",
"fallbacks":{
"general":["gpt-3.5-turbo","claude-3-sonnet"],
"context_window":["gpt-4-turbo","claude-3-opus"],
"content_policy":["claude-3-haiku"]
}
}
]
}
```

### Use Cases[​](#use-cases "Direct link to Use Cases")

- **High Availability**: Identify backup models to ensure service continuity
- **Cost Optimization**: Find cheaper alternatives when primary models are expensive
- **Content Filtering**: Discover models with different content policies
- **Context Length**: Find models that can handle larger inputs
- **Load Balancing**: Distribute requests across multiple compatible models

### API Parameters[​](#api-parameters "Direct link to API Parameters")

ParameterTypeDescription`include_metadata`booleanInclude additional model metadata including fallbacks`fallback_type`stringFilter fallbacks by type: `general`, `context_window`, or `content_policy`

## Advanced: Model Access Groups[​](#advanced-model-access-groups "Direct link to Advanced: Model Access Groups")

For advanced use cases, use [Model Access Groups](https://docs.litellm.ai/docs/proxy/model_access_groups) to dynamically group multiple models and manage access without restarting the proxy.

## [Role Based Access Control (RBAC)](https://docs.litellm.ai/docs/proxy/jwt_auth_arch)[​](#role-based-access-control-rbac "Direct link to role-based-access-control-rbac")