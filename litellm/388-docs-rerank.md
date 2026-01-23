---
title: /rerank | liteLLM
url: https://docs.litellm.ai/docs/rerank
source: sitemap
fetched_at: 2026-01-21T19:54:11.71056617-03:00
rendered_js: false
word_count: 94
summary: This document provides instructions for implementing document reranking across multiple providers using LiteLLM's Python SDK and API proxy. It covers setup, asynchronous usage, and configuration for features like load balancing and cost tracking.
tags:
    - litellm
    - rerank
    - python-sdk
    - api-proxy
    - search-optimization
category: guide
---

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Works with all supported modelsLogging✅Works across all integrationsEnd-user Tracking✅Fallbacks✅Works between supported modelsLoadbalancing✅Works between supported modelsGuardrails✅Applies to input query only (not documents)Supported ProvidersCohere, Together AI, Azure AI, DeepInfra, Nvidia NIM, Infinity, Fireworks AI, Voyage AI

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start[​](#quick-start "Direct link to Quick Start")

```
from litellm import rerank
import os

os.environ["COHERE_API_KEY"]="sk-.."

query ="What is the capital of the United States?"
documents =[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
]

response = rerank(
    model="cohere/rerank-english-v3.0",
    query=query,
    documents=documents,
    top_n=3,
)
print(response)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import arerank
import os, asyncio

os.environ["COHERE_API_KEY"]="sk-.."

asyncdeftest_async_rerank():
    query ="What is the capital of the United States?"
    documents =[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
]

    response =await arerank(
        model="cohere/rerank-english-v3.0",
        query=query,
        documents=documents,
        top_n=3,
)
print(response)

asyncio.run(test_async_rerank())
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides an cohere api compatible `/rerank` endpoint for Rerank calls.

**Setup**

Add this to your litellm proxy config.yaml

```
model_list:
-model_name: Salesforce/Llama-Rank-V1
litellm_params:
model: together_ai/Salesforce/Llama-Rank-V1
api_key: os.environ/TOGETHERAI_API_KEY
-model_name: rerank-english-v3.0
litellm_params:
model: cohere/rerank-english-v3.0
api_key: os.environ/COHERE_API_KEY
```

Start litellm

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

Test request

```
curl http://0.0.0.0:4000/rerank \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "rerank-english-v3.0",
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

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

#### ⚡️See all supported models and providers at [models.litellm.ai](https://models.litellm.ai/)[​](#%EF%B8%8Fsee-all-supported-models-and-providers-at-modelslitellmai "Direct link to ️see-all-supported-models-and-providers-at-modelslitellmai")

ProviderLink to UsageCohere (v1 + v2 clients)[Usage](#quick-start)Together AI[Usage](https://docs.litellm.ai/docs/providers/togetherai)Azure AI[Usage](https://docs.litellm.ai/docs/providers/azure_ai#rerank-endpoint)Jina AI[Usage](https://docs.litellm.ai/docs/providers/jina_ai)AWS Bedrock[Usage](https://docs.litellm.ai/docs/providers/bedrock#rerank-api)HuggingFace[Usage](https://docs.litellm.ai/docs/providers/huggingface_rerank)Infinity[Usage](https://docs.litellm.ai/docs/providers/infinity)vLLM[Usage](https://docs.litellm.ai/docs/providers/vllm#rerank-endpoint)DeepInfra[Usage](https://docs.litellm.ai/docs/providers/deepinfra#rerank-endpoint)Vertex AI[Usage](https://docs.litellm.ai/docs/providers/vertex#rerank-api)Fireworks AI[Usage](https://docs.litellm.ai/docs/providers/fireworks_ai#rerank-endpoint)Voyage AI[Usage](https://docs.litellm.ai/docs/providers/voyage#rerank)