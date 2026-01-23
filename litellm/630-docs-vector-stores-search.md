---
title: /vector_stores/search - Search Vector Store | liteLLM
url: https://docs.litellm.ai/docs/vector_stores/search
source: sitemap
fetched_at: 2026-01-21T19:55:55.229309523-03:00
rendered_js: false
word_count: 177
summary: This document explains how to perform vector store searches using the LiteLLM Python SDK and Proxy Server to support retrieval-augmented generation (RAG) across multiple providers.
tags:
    - litellm
    - vector-store
    - rag
    - search-api
    - python-sdk
    - proxy-server
    - llm-integration
category: api
---

Search a vector store for relevant chunks based on a query and file attributes filter. This is useful for retrieval-augmented generation (RAG) use cases.

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Tracked per search operationLogging✅Works across all integrationsEnd-user Tracking✅Support LLM Providers**OpenAI, Azure OpenAI, Bedrock, Vertex RAG Engine, Azure AI, Milvus, Gemini**Full vector stores API support across providers

## Usage[​](#usage "Direct link to Usage")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

- Basic Usage
- Advanced Configuration
- Multiple Queries
- OpenAI Provider
- Azure AI Provider
- Milvus Provider
- Gemini Provider

#### Non-streaming example[​](#non-streaming-example "Direct link to Non-streaming example")

Search Vector Store - Basic

```
import litellm

response =await litellm.vector_stores.asearch(
    vector_store_id="vs_abc123",
    query="What is the capital of France?"
)
print(response)
```

#### Synchronous example[​](#synchronous-example "Direct link to Synchronous example")

Search Vector Store - Sync

```
import litellm

response = litellm.vector_stores.search(
    vector_store_id="vs_abc123",
    query="What is the capital of France?"
)
print(response)
```

### LiteLLM Proxy Server[​](#litellm-proxy-server "Direct link to LiteLLM Proxy Server")

- Setup & Usage
- curl

<!--THE END-->

1. Setup config.yaml

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY

general_settings:
# Vector store settings can be added here if needed
```

2. Start proxy

```
litellm --config /path/to/config.yaml
```

3. Test it with OpenAI SDK!

OpenAI SDK via LiteLLM Proxy

```
from openai import OpenAI

# Point OpenAI SDK to LiteLLM proxy
client = OpenAI(
    base_url="http://0.0.0.0:4000",
    api_key="sk-1234",# Your LiteLLM API key
)

search_results = client.beta.vector_stores.search(
    vector_store_id="vs_abc123",
    query="What is the capital of France?",
    max_num_results=5
)
print(search_results)
```

## Setting Up Vector Stores[​](#setting-up-vector-stores "Direct link to Setting Up Vector Stores")

To use vector store search, configure your vector stores in the `vector_store_registry`. See the [Vector Store Configuration Guide](https://docs.litellm.ai/docs/completion/knowledgebase) for:

- Provider-specific configuration (Bedrock, OpenAI, Azure, Vertex AI, PG Vector)
- Python SDK and Proxy setup examples
- Authentication and credential management

## Using Vector Stores with Chat Completions[​](#using-vector-stores-with-chat-completions "Direct link to Using Vector Stores with Chat Completions")

Pass `vector_store_ids` in chat completion requests to automatically retrieve relevant context. See [Using Vector Stores with Chat Completions](https://docs.litellm.ai/docs/completion/knowledgebase#2-make-a-request-with-vector_store_ids-parameter) for implementation details.