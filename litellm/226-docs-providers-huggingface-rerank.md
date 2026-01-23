---
title: HuggingFace Rerank | liteLLM
url: https://docs.litellm.ai/docs/providers/huggingface_rerank
source: sitemap
fetched_at: 2026-01-21T19:49:23.064906226-03:00
rendered_js: false
word_count: 116
summary: This document explains how to integrate and use HuggingFace reranking models via LiteLLM, including instructions for the Python SDK, async implementation, and proxy server configuration.
tags:
    - huggingface
    - rerank
    - litellm
    - python-sdk
    - api-proxy
    - semantic-search
category: guide
---

HuggingFace Rerank allows you to use reranking models hosted on Hugging Face infrastructure or your custom endpoints to reorder documents based on their relevance to a query.

PropertyDetailsDescriptionHuggingFace Rerank enables semantic reranking of documents using models hosted on Hugging Face infrastructure or custom endpoints.Provider Route on LiteLLM`huggingface/` in model nameProvider Doc[Hugging Face Hub ↗](https://huggingface.co/models?pipeline_tag=sentence-similarity)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Example using LiteLLM Python SDK

```
import litellm
import os

# Set your HuggingFace token
os.environ["HF_TOKEN"]="hf_xxxxxx"

# Basic rerank usage
response = litellm.rerank(
    model="huggingface/BAAI/bge-reranker-base",
    query="What is the capital of the United States?",
    documents=[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
],
    top_n=3,
)

print(response)
```

### Custom Endpoint Usage[​](#custom-endpoint-usage "Direct link to Custom Endpoint Usage")

Using custom HuggingFace endpoint

```
import litellm

response = litellm.rerank(
    model="huggingface/BAAI/bge-reranker-base",
    query="hello",
    documents=["hello","world"],
    top_n=2,
    api_base="https://my-custom-hf-endpoint.com",
    api_key="test_api_key",
)

print(response)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

Async rerank example

```
import litellm
import asyncio
import os

os.environ["HF_TOKEN"]="hf_xxxxxx"

asyncdefasync_rerank_example():
    response =await litellm.arerank(
        model="huggingface/BAAI/bge-reranker-base",
        query="What is the capital of the United States?",
        documents=[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
],
        top_n=3,
)
print(response)

asyncio.run(async_rerank_example())
```

## LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

### 1. Configure your model in config.yaml[​](#1-configure-your-model-in-configyaml "Direct link to 1. Configure your model in config.yaml")

- config.yaml

```
model_list:
-model_name: bge-reranker-base
litellm_params:
model: huggingface/BAAI/bge-reranker-base
api_key: os.environ/HF_TOKEN
-model_name: bge-reranker-large  
litellm_params:
model: huggingface/BAAI/bge-reranker-large
api_key: os.environ/HF_TOKEN
-model_name: custom-reranker
litellm_params:
model: huggingface/BAAI/bge-reranker-base
api_base: https://my-custom-hf-endpoint.com
api_key: your-custom-api-key
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
export HF_TOKEN="hf_xxxxxx"
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Make rerank requests[​](#3-make-rerank-requests "Direct link to 3. Make rerank requests")

- Curl
- Python SDK
- Using requests library

```
curl http://localhost:4000/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "bge-reranker-base",
    "query": "What is the capital of the United States?",
    "documents": [
        "Carson City is the capital city of the American state of Nevada.",
        "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
        "Washington, D.C. is the capital of the United States.",
        "Capital punishment has existed in the United States since before it was a country."
    ],
    "top_n": 3
  }'
```

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

### Authentication[​](#authentication "Direct link to Authentication")

#### Using HuggingFace Token (Serverless)[​](#using-huggingface-token-serverless "Direct link to Using HuggingFace Token (Serverless)")

```
import os
os.environ["HF_TOKEN"]="hf_xxxxxx"

# Or pass directly
litellm.rerank(
    model="huggingface/BAAI/bge-reranker-base",
    api_key="hf_xxxxxx",
# ... other params
)
```

#### Using Custom Endpoint[​](#using-custom-endpoint "Direct link to Using Custom Endpoint")

```
litellm.rerank(
    model="huggingface/BAAI/bge-reranker-base",
    api_base="https://your-custom-endpoint.com",
    api_key="your-custom-key",
# ... other params
)
```

## Response Format[​](#response-format "Direct link to Response Format")

The response follows the standard rerank API format:

```
{
"results":[
{
"index":3,
"relevance_score":0.999071
},
{
"index":4,
"relevance_score":0.7867867
},
{
"index":0,
"relevance_score":0.32713068
}
],
"id":"07734bd2-2473-4f07-94e1-0d9f0e6843cf",
"meta":{
"api_version":{
"version":"2",
"is_experimental":false
},
"billed_units":{
"search_units":1
}
}
}
```