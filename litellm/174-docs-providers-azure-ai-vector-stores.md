---
title: Azure AI Search - Vector Store (Unified API) | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_ai_vector_stores
source: sitemap
fetched_at: 2026-01-21T19:48:09.709316121-03:00
rendered_js: false
word_count: 298
summary: Explains how to perform vector searches on Azure AI Search using LiteLLM's unified API, covering configuration, search parameters, and integration with embedding models.
tags:
    - litellm
    - azure-ai-search
    - vector-store
    - python-sdk
    - semantic-search
    - embeddings
category: guide
---

Use this to **search** Azure AI Search Vector Stores, with LiteLLM's unified `/chat/completions` API.

## Quick Start[​](#quick-start "Direct link to Quick Start")

You need three things:

1. An Azure AI Search service
2. An embedding model (to convert your queries to vectors)
3. A search index with vector fields

## Usage[​](#usage "Direct link to Usage")

- SDK
- PROXY

### Basic Search[​](#basic-search "Direct link to Basic Search")

```
from litellm import vector_stores
import os

# Set your credentials
os.environ["AZURE_SEARCH_API_KEY"]="your-search-api-key"
os.environ["AZURE_AI_SEARCH_EMBEDDING_API_BASE"]="your-embedding-endpoint"
os.environ["AZURE_AI_SEARCH_EMBEDDING_API_KEY"]="your-embedding-api-key"

# Search the vector store
response = vector_stores.search(
    vector_store_id="my-vector-index",# Your Azure AI Search index name
    query="What is the capital of France?",
    custom_llm_provider="azure_ai",
    azure_search_service_name="your-search-service",
    litellm_embedding_model="azure/text-embedding-3-large",
    litellm_embedding_config={
"api_base": os.getenv("AZURE_AI_SEARCH_EMBEDDING_API_BASE"),
"api_key": os.getenv("AZURE_AI_SEARCH_EMBEDDING_API_KEY"),
},
    api_key=os.getenv("AZURE_SEARCH_API_KEY"),
)

print(response)
```

### Async Search[​](#async-search "Direct link to Async Search")

```
from litellm import vector_stores

response =await vector_stores.asearch(
    vector_store_id="my-vector-index",
    query="What is the capital of France?",
    custom_llm_provider="azure_ai",
    azure_search_service_name="your-search-service",
    litellm_embedding_model="azure/text-embedding-3-large",
    litellm_embedding_config={
"api_base": os.getenv("AZURE_AI_SEARCH_EMBEDDING_API_BASE"),
"api_key": os.getenv("AZURE_AI_SEARCH_EMBEDDING_API_KEY"),
},
    api_key=os.getenv("AZURE_SEARCH_API_KEY"),
)

print(response)
```

### Advanced Options[​](#advanced-options "Direct link to Advanced Options")

```
from litellm import vector_stores

response = vector_stores.search(
    vector_store_id="my-vector-index",
    query="What is the capital of France?",
    custom_llm_provider="azure_ai",
    azure_search_service_name="your-search-service",
    litellm_embedding_model="azure/text-embedding-3-large",
    litellm_embedding_config={
"api_base": os.getenv("AZURE_AI_SEARCH_EMBEDDING_API_BASE"),
"api_key": os.getenv("AZURE_AI_SEARCH_EMBEDDING_API_KEY"),
},
    api_key=os.getenv("AZURE_SEARCH_API_KEY"),
    top_k=10,# Number of results to return
    azure_search_vector_field="contentVector",# Custom vector field name
)

print(response)
```

## Required Parameters[​](#required-parameters "Direct link to Required Parameters")

ParameterTypeDescription`vector_store_id`stringYour Azure AI Search index name`custom_llm_provider`stringSet to `"azure_ai"``azure_search_service_name`stringName of your Azure AI Search service`litellm_embedding_model`stringModel to generate query embeddings (e.g., `"azure/text-embedding-3-large"`)`litellm_embedding_config`dictConfig for the embedding model (api\_base, api\_key, api\_version)`api_key`stringYour Azure AI Search API key

## Supported Features[​](#supported-features "Direct link to Supported Features")

FeatureStatusNotesLogging✅ SupportedFull logging support availableGuardrails❌ Not Yet SupportedGuardrails are not currently supported for vector storesCost Tracking✅ SupportedCost is $0 according to AzureUnified API✅ SupportedCall via OpenAI compatible `/v1/vector_stores/search` endpointPassthrough❌ Not yet supported

## Response Format[​](#response-format "Direct link to Response Format")

The response follows the standard LiteLLM vector store format:

```
{
"object":"vector_store.search_results.page",
"search_query":"What is the capital of France?",
"data":[
{
"score":0.95,
"content":[
{
"text":"Paris is the capital of France...",
"type":"text"
}
],
"file_id":"doc_123",
"filename":"Document doc_123",
"attributes":{
"document_id":"doc_123"
}
}
]
}
```

## How It Works[​](#how-it-works "Direct link to How It Works")

When you search:

1. LiteLLM converts your query to a vector using the embedding model you specified
2. It sends the vector to Azure AI Search
3. Azure AI Search finds the most similar documents in your index
4. Results come back with similarity scores

The embedding model can be any model supported by LiteLLM - Azure OpenAI, OpenAI, Bedrock, etc.

## Setting Up Your Azure AI Search Index[​](#setting-up-your-azure-ai-search-index "Direct link to Setting Up Your Azure AI Search Index")

Your index needs a vector field. Here's what that looks like:

```
{
"name":"my-vector-index",
"fields":[
{
"name":"id",
"type":"Edm.String",
"key":true
},
{
"name":"content",
"type":"Edm.String"
},
{
"name":"contentVector",
"type":"Collection(Edm.Single)",
"searchable":true,
"dimensions":1536,
"vectorSearchProfile":"myVectorProfile"
}
]
}
```

The vector dimensions must match your embedding model. For example:

- `text-embedding-3-large`: 1536 dimensions
- `text-embedding-3-small`: 1536 dimensions
- `text-embedding-ada-002`: 1536 dimensions

## Common Issues[​](#common-issues "Direct link to Common Issues")

**"Failed to generate embedding for query"**

Your embedding model config is wrong. Check:

- `litellm_embedding_config` has the right api\_base and api\_key
- The embedding model name is correct
- Your credentials work

**"Index not found"**

The `vector_store_id` doesn't match any index in your search service. Check:

- The index name is correct
- You're using the right search service name

**"Field 'contentVector' not found"**

Your index uses a different vector field name. Pass it via `azure_search_vector_field`.