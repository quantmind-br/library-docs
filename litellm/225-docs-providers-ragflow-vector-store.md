---
title: RAGFlow Vector Stores | liteLLM
url: https://docs.litellm.ai/docs/providers/ragflow_vector_store
source: sitemap
fetched_at: 2026-01-21T19:50:14.631479672-03:00
rendered_js: false
word_count: 401
summary: This document explains how to integrate and manage RAGFlow datasets using LiteLLM, covering configuration, dataset creation, and specific chunking parameters for knowledge base management.
tags:
    - litellm
    - ragflow
    - vector-store
    - dataset-management
    - rag-applications
    - knowledge-base
    - chunking-methods
category: guide
---

Litellm support creation and management of datasets for document processing and knowledge base management in Ragflow.

PropertyDetailsDescriptionRAGFlow datasets enable document processing, chunking, and knowledge base management for RAG applications.Provider Route on LiteLLM`ragflow` in the litellm vector\_store\_registryProvider Doc[RAGFlow API Documentation ↗](https://ragflow.io/docs)Supported OperationsDataset Management (Create, List, Update, Delete)Search/Retrieval❌ Not supported (management only)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Example using LiteLLM Python SDK

```
import os
import litellm

# Set RAGFlow credentials
os.environ["RAGFLOW_API_KEY"]="your-ragflow-api-key"
os.environ["RAGFLOW_API_BASE"]="http://localhost:9380"# Optional, defaults to localhost:9380

# Create a RAGFlow dataset
response = litellm.vector_stores.create(
    name="my-dataset",
    custom_llm_provider="ragflow",
    metadata={
"description":"My knowledge base dataset",
"embedding_model":"BAAI/bge-large-zh-v1.5@BAAI",
"chunk_method":"naive"
}
)

print(f"Created dataset ID: {response.id}")
print(f"Dataset name: {response.name}")
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

#### 1. Configure your vector\_store\_registry[​](#1-configure-your-vector_store_registry "Direct link to 1. Configure your vector_store_registry")

- config.yaml
- LiteLLM UI

```
model_list:
-model_name: gpt-4o-mini
litellm_params:
model: gpt-4o-mini
api_key: os.environ/OPENAI_API_KEY

vector_store_registry:
-vector_store_name:"ragflow-knowledge-base"
litellm_params:
vector_store_id:"your-dataset-id"
custom_llm_provider:"ragflow"
api_key: os.environ/RAGFLOW_API_KEY
api_base: os.environ/RAGFLOW_API_BASE  # Optional
vector_store_description:"RAGFlow dataset for knowledge base"
vector_store_metadata:
source:"Company documentation"
```

#### 2. Create a dataset via Proxy[​](#2-create-a-dataset-via-proxy "Direct link to 2. Create a dataset via Proxy")

- Curl
- OpenAI Python SDK

```
curl http://localhost:4000/v1/vector_stores \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "name": "my-ragflow-dataset",
    "custom_llm_provider": "ragflow",
    "metadata": {
      "description": "Test dataset",
      "chunk_method": "naive"
    }
  }'
```

## Configuration[​](#configuration "Direct link to Configuration")

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

RAGFlow vector stores support configuration via environment variables:

- `RAGFLOW_API_KEY` - Your RAGFlow API key (required)
- `RAGFLOW_API_BASE` - RAGFlow API base URL (optional, defaults to `http://localhost:9380`)

### Parameters[​](#parameters "Direct link to Parameters")

You can also pass these via `litellm_params`:

- `api_key` - RAGFlow API key (overrides `RAGFLOW_API_KEY` env var)
- `api_base` - RAGFlow API base URL (overrides `RAGFLOW_API_BASE` env var)

## Dataset Creation Options[​](#dataset-creation-options "Direct link to Dataset Creation Options")

### Basic Dataset Creation[​](#basic-dataset-creation "Direct link to Basic Dataset Creation")

```
response = litellm.vector_stores.create(
    name="basic-dataset",
    custom_llm_provider="ragflow"
)
```

### Dataset with Chunk Method[​](#dataset-with-chunk-method "Direct link to Dataset with Chunk Method")

RAGFlow supports various chunk methods for different document types:

- Naive (General)
- Book
- Q&A
- Paper

```
response = litellm.vector_stores.create(
    name="general-dataset",
    custom_llm_provider="ragflow",
    metadata={
"chunk_method":"naive",
"parser_config":{
"chunk_token_num":512,
"delimiter":"\n",
"html4excel":False,
"layout_recognize":"DeepDOC"
}
}
)
```

### Dataset with Ingestion Pipeline[​](#dataset-with-ingestion-pipeline "Direct link to Dataset with Ingestion Pipeline")

Instead of using a chunk method, you can use an ingestion pipeline:

```
response = litellm.vector_stores.create(
    name="pipeline-dataset",
    custom_llm_provider="ragflow",
    metadata={
"parse_type":2,# Number of parsers in your pipeline
"pipeline_id":"d0bebe30ae2211f0970942010a8e0005"# 32-character hex ID
}
)
```

**Note**: `chunk_method` and `pipeline_id` are mutually exclusive. Use one or the other.

### Advanced Parser Configuration[​](#advanced-parser-configuration "Direct link to Advanced Parser Configuration")

```
response = litellm.vector_stores.create(
    name="advanced-dataset",
    custom_llm_provider="ragflow",
    metadata={
"chunk_method":"naive",
"description":"Advanced dataset with custom parser config",
"embedding_model":"BAAI/bge-large-zh-v1.5@BAAI",
"permission":"me",# or "team"
"parser_config":{
"chunk_token_num":1024,
"delimiter":"\n!?;。；！？",
"html4excel":True,
"layout_recognize":"DeepDOC",
"auto_keywords":5,
"auto_questions":3,
"task_page_size":12,
"raptor":{
"use_raptor":True
},
"graphrag":{
"use_graphrag":False
}
}
}
)
```

## Supported Chunk Methods[​](#supported-chunk-methods "Direct link to Supported Chunk Methods")

RAGFlow supports the following chunk methods:

- `naive` - General purpose (default)
- `book` - For book documents
- `email` - For email documents
- `laws` - For legal documents
- `manual` - Manual chunking
- `one` - Single chunk
- `paper` - For academic papers
- `picture` - For image documents
- `presentation` - For presentation documents
- `qa` - Q&A format
- `table` - For table documents
- `tag` - Tag-based chunking

## RAGFlow-Specific Parameters[​](#ragflow-specific-parameters "Direct link to RAGFlow-Specific Parameters")

All RAGFlow-specific parameters should be passed via the `metadata` field:

ParameterTypeDescription`avatar`stringBase64 encoding of the avatar (max 65535 chars)`description`stringBrief description of the dataset (max 65535 chars)`embedding_model`stringEmbedding model name (e.g., "BAAI/bge-large-zh-v1.5@BAAI")`permission`stringAccess permission: "me" (default) or "team"`chunk_method`stringChunking method (see supported methods above)`parser_config`objectParser configuration (varies by chunk\_method)`parse_type`intNumber of parsers in pipeline (required with pipeline\_id)`pipeline_id`string32-character hex pipeline ID (required with parse\_type)

## Error Handling[​](#error-handling "Direct link to Error Handling")

RAGFlow returns error responses in the following format:

```
{
"code":101,
"message":"Dataset name 'my-dataset' already exists"
}
```

LiteLLM automatically maps these to appropriate exceptions:

- `code != 0` → Raises exception with the error message
- Missing required fields → Raises `ValueError`
- Mutually exclusive parameters → Raises `ValueError`

## Limitations[​](#limitations "Direct link to Limitations")

- **Search/Retrieval**: RAGFlow vector stores support dataset management only. Search operations are not supported and will raise `NotImplementedError`.
- **List/Update/Delete**: These operations are not yet implemented through the standard vector store API. Use RAGFlow's native API endpoints directly.

## Further Reading[​](#further-reading "Direct link to Further Reading")

Vector Stores:

- [Vector Store Creation](https://docs.litellm.ai/docs/vector_stores/create)
- [Using Vector Stores with Completions](https://docs.litellm.ai/docs/completion/knowledgebase)
- [Vector Store Registry](https://docs.litellm.ai/docs/completion/knowledgebase#vectorstoreregistry)