---
title: Infinity | liteLLM
url: https://docs.litellm.ai/docs/providers/infinity
source: sitemap
fetched_at: 2026-01-21T19:49:27.276989192-03:00
rendered_js: false
word_count: 168
summary: This document explains how to integrate and use the Infinity text-embedding and reranking API through the LiteLLM Python SDK and Proxy server.
tags:
    - infinity
    - litellm
    - embeddings
    - reranking
    - python-sdk
    - api-integration
    - rest-api
category: guide
---

PropertyDetailsDescriptionInfinity is a high-throughput, low-latency REST API for serving text-embeddings, reranking models and clipProvider Route on LiteLLM`infinity/`Supported Operations`/rerank`, `/embeddings`Link to Provider Doc[Infinity ↗](https://github.com/michaelfeil/infinity)

## **Usage - LiteLLM Python SDK**[​](#usage---litellm-python-sdk "Direct link to usage---litellm-python-sdk")

```
from litellm import rerank, embedding
import os

os.environ["INFINITY_API_BASE"]="http://localhost:8080"

response = rerank(
    model="infinity/rerank",
    query="What is the capital of France?",
    documents=["Paris","London","Berlin","Madrid"],
)
```

## **Usage - LiteLLM Proxy**[​](#usage---litellm-proxy "Direct link to usage---litellm-proxy")

LiteLLM provides an cohere api compatible `/rerank` endpoint for Rerank calls.

**Setup**

Add this to your litellm proxy config.yaml

```
model_list:
-model_name: custom-infinity-rerank
litellm_params:
model: infinity/rerank
api_base: https://localhost:8080
api_key: os.environ/INFINITY_API_KEY
```

Start litellm

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

## Test request:[​](#test-request "Direct link to Test request:")

### Rerank[​](#rerank "Direct link to Rerank")

```
curl http://0.0.0.0:4000/rerank \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "custom-infinity-rerank",
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

#### Supported Cohere Rerank API Params[​](#supported-cohere-rerank-api-params "Direct link to Supported Cohere Rerank API Params")

ParamTypeDescription`query``str`The query to rerank the documents against`documents``list[str]`The documents to rerank`top_n``int`The number of documents to return`return_documents``bool`Whether to return the documents in the response

### Usage - Return Documents[​](#usage---return-documents "Direct link to Usage - Return Documents")

- SDK
- PROXY

```
response = rerank(
    model="infinity/rerank",
    query="What is the capital of France?",
    documents=["Paris","London","Berlin","Madrid"],
    return_documents=True,
)
```

## Pass Provider-specific Params[​](#pass-provider-specific-params "Direct link to Pass Provider-specific Params")

Any unmapped params will be passed to the provider as-is.

- SDK
- PROXY

```
from litellm import rerank
import os

os.environ["INFINITY_API_BASE"]="http://localhost:8080"

response = rerank(
    model="infinity/rerank",
    query="What is the capital of France?",
    documents=["Paris","London","Berlin","Madrid"],
    raw_scores=True,# 👈 PROVIDER-SPECIFIC PARAM
)
```

## Embeddings[​](#embeddings "Direct link to Embeddings")

LiteLLM provides an OpenAI api compatible `/embeddings` endpoint for embedding calls.

**Setup**

Add this to your litellm proxy config.yaml

```
model_list:
-model_name: custom-infinity-embedding
litellm_params:
model: infinity/provider/custom-embedding-v1
api_base: http://localhost:8080
api_key: os.environ/INFINITY_API_KEY
```

### Test request:[​](#test-request-1 "Direct link to Test request:")

```
curl http://0.0.0.0:4000/embeddings \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "custom-infinity-embedding",
    "input": ["hello"]
  }'
```

#### Supported Embedding API Params[​](#supported-embedding-api-params "Direct link to Supported Embedding API Params")

ParamTypeDescription`model``str`The embedding model to use`input``list[str]`The text inputs to generate embeddings for`encoding_format``str`The format to return embeddings in (e.g. "float", "base64")`modality``str`The type of input (e.g. "text", "image", "audio")

### Usage - Basic Examples[​](#usage---basic-examples "Direct link to Usage - Basic Examples")

- SDK
- PROXY

```
from litellm import embedding
import os

os.environ["INFINITY_API_BASE"]="http://localhost:8080"

response = embedding(
    model="infinity/bge-small",
input=["good morning from litellm"]
)

print(response.data[0]['embedding'])
```

### Usage - OpenAI Client[​](#usage---openai-client "Direct link to Usage - OpenAI Client")

- SDK
- PROXY

```
from openai import OpenAI

client = OpenAI(
  api_key="<LITELLM_MASTER_KEY>",
  base_url="<LITELLM_URL>"
)

response = client.embeddings.create(
  model="bge-small",
input=["The food was delicious and the waiter..."],
  encoding_format="float"
)

print(response.data[0].embedding)
```