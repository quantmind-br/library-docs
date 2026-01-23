---
title: VLLM | liteLLM
url: https://docs.litellm.ai/docs/pass_through/vllm
source: sitemap
fetched_at: 2026-01-21T19:47:02.23882353-03:00
rendered_js: false
word_count: 164
summary: This document explains how to configure and use LiteLLM Proxy as a pass-through for native VLLM endpoints to enable logging and access control while maintaining provider-specific API formats.
tags:
    - litellm-proxy
    - vllm
    - pass-through
    - api-gateway
    - logging
    - virtual-keys
category: guide
---

Pass-through endpoints for VLLM - call provider-specific endpoint, in native format (no translation).

FeatureSupportedNotesCost Tracking❌Not supportedLogging✅works across all integrationsEnd-user Tracking❌[Tell us if you need this](https://github.com/BerriAI/litellm/issues/new)Streaming✅

Just replace `https://my-vllm-server.com` with `LITELLM_PROXY_BASE_URL/vllm` 🚀

#### **Example Usage**[​](#example-usage "Direct link to example-usage")

```
curl -L -X GET 'http://0.0.0.0:4000/vllm/metrics' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
```

Supports **ALL** VLLM Endpoints (including streaming).

## Quick Start[​](#quick-start "Direct link to Quick Start")

Let's call the VLLM [`/score` endpoint](https://vllm.readthedocs.io/en/latest/api_reference/api_reference.html)

1. Add a VLLM hosted model to your LiteLLM Proxy

info

Works with LiteLLM v1.72.0+.

```
model_list:
-model_name:"my-vllm-model"
litellm_params:
model: hosted_vllm/vllm-1.72
api_base: https://my-vllm-server.com
```

2. Start LiteLLM Proxy

```
litellm

# RUNNING on http://0.0.0.0:4000
```

3. Test it!

Let's call the VLLM `/score` endpoint

```
curl -X 'POST' \
  'http://0.0.0.0:4000/vllm/score' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "my-vllm-model",
  "encoding_format": "float",
  "text_1": "What is the capital of France?",
  "text_2": "The capital of France is Paris."
}'
```

## Examples[​](#examples "Direct link to Examples")

Anything after `http://0.0.0.0:4000/vllm` is treated as a provider-specific route, and handled accordingly.

Key Changes:

**Original Endpoint****Replace With**`https://my-vllm-server.com``http://0.0.0.0:4000/vllm` (LITELLM\_PROXY\_BASE\_URL="[http://0.0.0.0:4000](http://0.0.0.0:4000)")`bearer $VLLM_API_KEY``bearer anything` (use `bearer LITELLM_VIRTUAL_KEY` if Virtual Keys are setup on proxy)

### **Example 1: Metrics endpoint**[​](#example-1-metrics-endpoint "Direct link to example-1-metrics-endpoint")

#### LiteLLM Proxy Call[​](#litellm-proxy-call "Direct link to LiteLLM Proxy Call")

```
curl -L -X GET 'http://0.0.0.0:4000/vllm/metrics' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer $LITELLM_VIRTUAL_KEY' \
```

#### Direct VLLM API Call[​](#direct-vllm-api-call "Direct link to Direct VLLM API Call")

```
curl -L -X GET 'https://my-vllm-server.com/metrics' \
-H 'Content-Type: application/json' \
```

### **Example 2: Chat API**[​](#example-2-chat-api "Direct link to example-2-chat-api")

#### LiteLLM Proxy Call[​](#litellm-proxy-call-1 "Direct link to LiteLLM Proxy Call")

```
curl -L -X POST 'http://0.0.0.0:4000/vllm/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer $LITELLM_VIRTUAL_KEY' \
-d '{
    "messages": [
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?"
        }
    ],
    "max_tokens": 2048,
    "temperature": 0.8,
    "top_p": 0.1,
    "model": "qwen2.5-7b-instruct",
}'
```

#### Direct VLLM API Call[​](#direct-vllm-api-call-1 "Direct link to Direct VLLM API Call")

```
curl -L -X POST 'https://my-vllm-server.com/chat/completions' \
-H 'Content-Type: application/json' \
-d '{
    "messages": [
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?"
        }
    ],
    "max_tokens": 2048,
    "temperature": 0.8,
    "top_p": 0.1,
    "model": "qwen2.5-7b-instruct",
}'
```

## Advanced - Use with Virtual Keys[​](#advanced---use-with-virtual-keys "Direct link to Advanced - Use with Virtual Keys")

Pre-requisites

- [Setup proxy with DB](https://docs.litellm.ai/docs/proxy/virtual_keys#setup)

Use this, to avoid giving developers the raw Cohere API key, but still letting them use Cohere endpoints.

### Usage[​](#usage "Direct link to Usage")

1. Setup environment

```
export DATABASE_URL=""
export LITELLM_MASTER_KEY=""
export HOSTED_VLLM_API_BASE=""
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
curl -L -X POST 'http://0.0.0.0:4000/vllm/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234ewknldferwedojwojw' \
  --data '{
    "messages": [
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?"
        }
    ],
    "max_tokens": 2048,
    "temperature": 0.8,
    "top_p": 0.1,
    "model": "qwen2.5-7b-instruct",
}'
```