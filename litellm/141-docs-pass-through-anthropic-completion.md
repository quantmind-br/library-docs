---
title: Anthropic Passthrough | liteLLM
url: https://docs.litellm.ai/docs/pass_through/anthropic_completion
source: sitemap
fetched_at: 2026-01-21T19:46:44.756141585-03:00
rendered_js: false
word_count: 229
summary: Explains how to use LiteLLM Proxy as a pass-through for native Anthropic API endpoints to enable features like cost tracking, logging, and virtual key management without format translation.
tags:
    - litellm-proxy
    - anthropic
    - api-passthrough
    - cost-tracking
    - streaming
    - batch-processing
    - virtual-keys
category: guide
---

Pass-through endpoints for Anthropic - call provider-specific endpoint, in native format (no translation).

FeatureSupportedNotesCost Tracking✅supports all models on `/messages`, `/v1/messages/batches` endpointLogging✅works across all integrationsEnd-user Tracking✅disable prometheus tracking via `litellm.disable_end_user_cost_tracking_prometheus_only`Streaming✅

Just replace `https://api.anthropic.com` with `LITELLM_PROXY_BASE_URL/anthropic`

#### **Example Usage**[​](#example-usage "Direct link to example-usage")

- curl
- Anthropic Python SDK

```
curl --request POST \
  --url http://0.0.0.0:4000/anthropic/v1/messages \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-anything" \
  --data '{
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }'
```

Supports **ALL** Anthropic Endpoints (including streaming).

[**See All Anthropic Endpoints**](https://docs.anthropic.com/en/api/messages)

## Quick Start[​](#quick-start "Direct link to Quick Start")

Let's call the Anthropic [`/messages` endpoint](https://docs.anthropic.com/en/api/messages)

1. Add Anthropic API Key to your environment

```
export ANTHROPIC_API_KEY=""
```

2. Start LiteLLM Proxy

```
litellm

# RUNNING on http://0.0.0.0:4000
```

3. Test it!

Let's call the Anthropic /messages endpoint

```
curl http://0.0.0.0:4000/anthropic/v1/messages \
     --header "x-api-key: $LITELLM_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
    '{
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }'
```

## Examples[​](#examples "Direct link to Examples")

Anything after `http://0.0.0.0:4000/anthropic` is treated as a provider-specific route, and handled accordingly.

Key Changes:

**Original Endpoint****Replace With**`https://api.anthropic.com``http://0.0.0.0:4000/anthropic` (LITELLM\_PROXY\_BASE\_URL="[http://0.0.0.0:4000](http://0.0.0.0:4000)")`bearer $ANTHROPIC_API_KEY``bearer anything` (use `bearer LITELLM_VIRTUAL_KEY` if Virtual Keys are setup on proxy)

### **Example 1: Messages endpoint**[​](#example-1-messages-endpoint "Direct link to example-1-messages-endpoint")

#### LiteLLM Proxy Call[​](#litellm-proxy-call "Direct link to LiteLLM Proxy Call")

```
curl --request POST \
  --url http://0.0.0.0:4000/anthropic/v1/messages \
  --header "x-api-key: $LITELLM_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
  --data '{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ]
  }'
```

#### Direct Anthropic API Call[​](#direct-anthropic-api-call "Direct link to Direct Anthropic API Call")

```
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
    '{
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }'
```

### **Example 2: Token Counting API**[​](#example-2-token-counting-api "Direct link to example-2-token-counting-api")

#### LiteLLM Proxy Call[​](#litellm-proxy-call-1 "Direct link to LiteLLM Proxy Call")

```
curl --request POST \
    --url http://0.0.0.0:4000/anthropic/v1/messages/count_tokens \
    --header "x-api-key: $LITELLM_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: token-counting-2024-11-01" \
    --header "content-type: application/json" \
    --data \
    '{
        "model": "claude-3-5-sonnet-20241022",
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }'
```

#### Direct Anthropic API Call[​](#direct-anthropic-api-call-1 "Direct link to Direct Anthropic API Call")

```
curl https://api.anthropic.com/v1/messages/count_tokens \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "anthropic-beta: token-counting-2024-11-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-3-5-sonnet-20241022",
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ]
}'
```

### **Example 3: Batch Messages**[​](#example-3-batch-messages "Direct link to example-3-batch-messages")

#### LiteLLM Proxy Call[​](#litellm-proxy-call-2 "Direct link to LiteLLM Proxy Call")

```
curl --request POST \
    --url http://0.0.0.0:4000/anthropic/v1/messages/batches \
    --header "x-api-key: $LITELLM_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: message-batches-2024-09-24" \
    --header "content-type: application/json" \
    --data \
'{
    "requests": [
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": "Hello, world"}
                ]
            }
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": "Hi again, friend"}
                ]
            }
        }
    ]
}'
```

#### Direct Anthropic API Call[​](#direct-anthropic-api-call-2 "Direct link to Direct Anthropic API Call")

```
curl https://api.anthropic.com/v1/messages/batches \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "anthropic-beta: message-batches-2024-09-24" \
     --header "content-type: application/json" \
     --data \
'{
    "requests": [
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": "Hello, world"}
                ]
            }
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": "Hi again, friend"}
                ]
            }
        }
    ]
}'
```

Configuration Required for Batch Cost Tracking

For batch passthrough cost tracking to work properly, you need to define the Anthropic model in your `proxy_config.yaml`:

```
model_list:
-model_name: claude-sonnet-4-5-20250929# or any alias
litellm_params:
model: anthropic/claude-sonnet-4-5-20250929
api_key: os.environ/ANTHROPIC_API_KEY
```

This ensures the polling mechanism can correctly identify the provider and retrieve batch status for cost calculation.

## Advanced[​](#advanced "Direct link to Advanced")

Pre-requisites

- [Setup proxy with DB](https://docs.litellm.ai/docs/proxy/virtual_keys#setup)

Use this, to avoid giving developers the raw Anthropic API key, but still letting them use Anthropic endpoints.

### Use with Virtual Keys[​](#use-with-virtual-keys "Direct link to Use with Virtual Keys")

1. Setup environment

```
export DATABASE_URL=""
export LITELLM_MASTER_KEY=""
export COHERE_API_KEY=""
```

```
litellm

# RUNNING on http://0.0.0.0:4000
```

2. Generate virtual key

```
curl -X POST 'http://0.0.0.0:4000/key/generate' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{}'
```

Expected Response

```
{
    ...
    "key": "sk-1234ewknldferwedojwojw"
}
```

3. Test it!

```
curl --request POST \
  --url http://0.0.0.0:4000/anthropic/v1/messages \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-1234ewknldferwedojwojw" \
  --data '{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ]
  }'
```

### Send `litellm_metadata` (tags, end-user cost tracking)[​](#send-litellm_metadata-tags-end-user-cost-tracking "Direct link to send-litellm_metadata-tags-end-user-cost-tracking")

- curl
- Anthropic Python SDK

```
curl --request POST \
  --url http://0.0.0.0:4000/anthropic/v1/messages \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-anything" \
  --data '{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ],
    "litellm_metadata": {
        "tags": ["test-tag-1", "test-tag-2"], 
        "user": "test-user" # track end-user/customer cost
    }
  }'
```