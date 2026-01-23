---
title: Cohere SDK | liteLLM
url: https://docs.litellm.ai/docs/pass_through/cohere
source: sitemap
fetched_at: 2026-01-21T19:46:51.419257782-03:00
rendered_js: false
word_count: 173
summary: This document explains how to use LiteLLM Proxy as a pass-through for Cohere's native API endpoints to enable features like logging and cost tracking without changing request formats. It provides setup instructions and cURL examples for chat, rerank, and embedding endpoints.
tags:
    - litellm
    - cohere
    - pass-through-endpoints
    - api-proxy
    - rerank-api
    - cost-tracking
    - llm-ops
category: guide
---

Pass-through endpoints for Cohere - call provider-specific endpoint, in native format (no translation).

FeatureSupportedNotesCost Tracking✅Supported for `/v1/chat`, and `/v2/chat`Logging✅works across all integrationsEnd-user Tracking❌[Tell us if you need this](https://github.com/BerriAI/litellm/issues/new)Streaming✅

Just replace `https://api.cohere.com` with `LITELLM_PROXY_BASE_URL/cohere` 🚀

#### **Example Usage**[​](#example-usage "Direct link to example-usage")

```
curl --request POST \
  --url http://0.0.0.0:4000/cohere/v1/chat \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-anything" \
  --data '{
    "chat_history": [
      {"role": "USER", "message": "Who discovered gravity?"},
      {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
    ],
    "message": "What year was he born?",
    "connectors": [{"id": "web-search"}]
  }'
```

Supports **ALL** Cohere Endpoints (including streaming).

[**See All Cohere Endpoints**](https://docs.cohere.com/reference/chat)

## Quick Start[​](#quick-start "Direct link to Quick Start")

Let's call the Cohere [`/rerank` endpoint](https://docs.cohere.com/reference/rerank)

1. Add Cohere API Key to your environment

<!--THE END-->

2. Start LiteLLM Proxy

```
litellm

# RUNNING on http://0.0.0.0:4000
```

3. Test it!

Let's call the Cohere /rerank endpoint

```
curl --request POST \
  --url http://0.0.0.0:4000/cohere/v1/rerank \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-anything" \
  --data '{
    "model": "rerank-english-v3.0",
    "query": "What is the capital of the United States?",
    "top_n": 3,
    "documents": ["Carson City is the capital city of the American state of Nevada.",
                  "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                  "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                  "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
                  "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."]
  }'
```

## Examples[​](#examples "Direct link to Examples")

Anything after `http://0.0.0.0:4000/cohere` is treated as a provider-specific route, and handled accordingly.

Key Changes:

**Original Endpoint****Replace With**`https://api.cohere.com``http://0.0.0.0:4000/cohere` (LITELLM\_PROXY\_BASE\_URL="[http://0.0.0.0:4000](http://0.0.0.0:4000)")`bearer $CO_API_KEY``bearer anything` (use `bearer LITELLM_VIRTUAL_KEY` if Virtual Keys are setup on proxy)

### **Example 1: Rerank endpoint**[​](#example-1-rerank-endpoint "Direct link to example-1-rerank-endpoint")

#### LiteLLM Proxy Call[​](#litellm-proxy-call "Direct link to LiteLLM Proxy Call")

```
curl --request POST \
  --url http://0.0.0.0:4000/cohere/v1/rerank \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-anything" \
  --data '{
    "model": "rerank-english-v3.0",
    "query": "What is the capital of the United States?",
    "top_n": 3,
    "documents": ["Carson City is the capital city of the American state of Nevada.",
                  "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                  "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                  "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
                  "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."]
  }'
```

#### Direct Cohere API Call[​](#direct-cohere-api-call "Direct link to Direct Cohere API Call")

```
curl --request POST \
  --url https://api.cohere.com/v1/rerank \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY" \
  --data '{
    "model": "rerank-english-v3.0",
    "query": "What is the capital of the United States?",
    "top_n": 3,
    "documents": ["Carson City is the capital city of the American state of Nevada.",
                  "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                  "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                  "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
                  "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."]
  }'
```

### **Example 2: Chat API**[​](#example-2-chat-api "Direct link to example-2-chat-api")

#### LiteLLM Proxy Call[​](#litellm-proxy-call-1 "Direct link to LiteLLM Proxy Call")

```
curl --request POST \
  --url http://0.0.0.0:4000/cohere/v1/chat \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-anything" \
  --data '{
    "chat_history": [
      {"role": "USER", "message": "Who discovered gravity?"},
      {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
    ],
    "message": "What year was he born?",
    "connectors": [{"id": "web-search"}]
  }'
```

#### Direct Cohere API Call[​](#direct-cohere-api-call-1 "Direct link to Direct Cohere API Call")

```
curl --request POST \
  --url https://api.cohere.com/v1/chat \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY" \
  --data '{
    "chat_history": [
      {"role": "USER", "message": "Who discovered gravity?"},
      {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
    ],
    "message": "What year was he born?",
    "connectors": [{"id": "web-search"}]
  }'
```

### **Example 3: Embedding**[​](#example-3-embedding "Direct link to example-3-embedding")

```
curl --request POST \
  --url https://api.cohere.com/v1/embed \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-anything" \
  --data '{
    "model": "embed-english-v3.0",
    "texts": ["hello", "goodbye"],
    "input_type": "classification"
  }'
```

#### Direct Cohere API Call[​](#direct-cohere-api-call-2 "Direct link to Direct Cohere API Call")

```
curl --request POST \
  --url https://api.cohere.com/v1/embed \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY" \
  --data '{
    "model": "embed-english-v3.0",
    "texts": ["hello", "goodbye"],
    "input_type": "classification"
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
  --url http://0.0.0.0:4000/cohere/v1/rerank \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer sk-1234ewknldferwedojwojw" \
  --data '{
    "model": "rerank-english-v3.0",
    "query": "What is the capital of the United States?",
    "top_n": 3,
    "documents": ["Carson City is the capital city of the American state of Nevada.",
                  "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                  "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                  "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
                  "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."]
  }'
```