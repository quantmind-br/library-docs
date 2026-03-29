---
title: /rag/query | liteLLM
url: https://docs.litellm.ai/docs/rag_query
source: sitemap
fetched_at: 2026-01-21T19:54:07.247989548-03:00
rendered_js: false
word_count: 209
summary: This document provides technical specifications and implementation examples for the RAG Query endpoint, which integrates vector store searching, reranking, and LLM generation. It details request parameters, streaming options, and multi-provider support for building retrieval-augmented generation workflows.
tags:
    - rag
    - vector-store
    - reranking
    - llm-api
    - semantic-search
    - retrieval-augmented-generation
category: api
---

RAG Query endpoint: **Search Vector Store → (Rerank) → LLM Completion**

FeatureSupportedLoggingYesStreamingYesRerankingYes (optional)Supported Providers`openai`, `bedrock`, `vertex_ai`

## Quick Start[​](#quick-start "Direct link to Quick Start")

RAG Query with OpenAI

```
curl -X POST "http://localhost:4000/v1/rag/query" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "What is LiteLLM?"}],
        "retrieval_config": {
            "vector_store_id": "vs_abc123",
            "custom_llm_provider": "openai",
            "top_k": 5
        }
    }'
```

## How It Works[​](#how-it-works "Direct link to How It Works")

The RAG query endpoint performs the following steps:

1. **Extract Query**: Extracts the query text from the last user message
2. **Search Vector Store**: Searches the specified vector store for relevant context
3. **Rerank (Optional)**: Reranks the search results using a reranking model
4. **Generate Response**: Calls the LLM with the retrieved context prepended to the messages

## Response[​](#response "Direct link to Response")

The response follows the standard OpenAI chat completion format, with additional search metadata:

```
{
"id":"chatcmpl-abc123",
"object":"chat.completion",
"created":1703123456,
"model":"gpt-4o-mini",
"choices":[
{
"index":0,
"message":{
"role":"assistant",
"content":"LiteLLM is a unified interface for 100+ LLMs..."
},
"finish_reason":"stop"
}
],
"usage":{
"prompt_tokens":150,
"completion_tokens":50,
"total_tokens":200
},
"_hidden_params":{
"search_results":{...},
"rerank_results":{...}
}
}
```

## With Reranking[​](#with-reranking "Direct link to With Reranking")

Add a `rerank` configuration to improve result quality:

RAG Query with Reranking

```
curl -X POST "http://localhost:4000/v1/rag/query" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "What is LiteLLM?"}],
        "retrieval_config": {
            "vector_store_id": "vs_abc123",
            "custom_llm_provider": "openai",
            "top_k": 10
        },
        "rerank": {
            "enabled": true,
            "model": "cohere/rerank-english-v3.0",
            "top_n": 3
        }
    }'
```

## Streaming[​](#streaming "Direct link to Streaming")

Enable streaming for real-time responses:

RAG Query with Streaming

```
curl -X POST "http://localhost:4000/v1/rag/query" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "What is LiteLLM?"}],
        "retrieval_config": {
            "vector_store_id": "vs_abc123",
            "custom_llm_provider": "openai"
        },
        "stream": true
    }'
```

## Request Parameters[​](#request-parameters "Direct link to Request Parameters")

### Top-Level[​](#top-level "Direct link to Top-Level")

ParameterTypeRequiredDescription`model`stringYesThe LLM model to use for generation`messages`arrayYesArray of chat messages (OpenAI format)`retrieval_config`objectYesVector store search configuration`rerank`objectNoReranking configuration`stream`booleanNoEnable streaming (default: `false`)

### retrieval\_config[​](#retrieval_config "Direct link to retrieval_config")

ParameterTypeDefaultDescription`vector_store_id`string**required**ID of the vector store to search`custom_llm_provider`string`"openai"`Vector store provider`top_k`integer`10`Number of results to retrieve

### rerank[​](#rerank "Direct link to rerank")

ParameterTypeDefaultDescription`enabled`boolean`false`Enable reranking`model`string-Reranking model (e.g., `cohere/rerank-english-v3.0`)`top_n`integer`5`Number of results after reranking

## End-to-End Example[​](#end-to-end-example "Direct link to End-to-End Example")

### 1. Ingest a Document[​](#1-ingest-a-document "Direct link to 1. Ingest a Document")

First, ingest a document using the [/rag/ingest](https://docs.litellm.ai/docs/rag_ingest) endpoint:

Step 1: Ingest

```
curl -X POST "http://localhost:4000/v1/rag/ingest" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d "{
        \"file\": {
            \"filename\": \"company_docs.txt\",
            \"content\": \"$(base64 -i company_docs.txt)\",
            \"content_type\": \"text/plain\"
        },
        \"ingest_options\": {
            \"vector_store\": {
                \"custom_llm_provider\": \"openai\"
            }
        }
    }"
```

Response:

```
{
"id":"ingest_abc123",
"status":"completed",
"vector_store_id":"vs_xyz789",
"file_id":"file-123"
}
```

### 2. Query with RAG[​](#2-query-with-rag "Direct link to 2. Query with RAG")

Now query the ingested documents:

Step 2: Query

```
curl -X POST "http://localhost:4000/v1/rag/query" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": "What products does the company offer?"}
        ],
        "retrieval_config": {
            "vector_store_id": "vs_xyz789",
            "custom_llm_provider": "openai",
            "top_k": 5
        }
    }'
```

Response:

```
{
"id":"chatcmpl-abc123",
"object":"chat.completion",
"model":"gpt-4o-mini",
"choices":[
{
"index":0,
"message":{
"role":"assistant",
"content":"Based on the company documents, the company offers..."
},
"finish_reason":"stop"
}
]
}
```

## Provider Examples[​](#provider-examples "Direct link to Provider Examples")

### Bedrock[​](#bedrock "Direct link to Bedrock")

RAG Query with Bedrock

```
curl -X POST "http://localhost:4000/v1/rag/query" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
        "messages": [{"role": "user", "content": "What is LiteLLM?"}],
        "retrieval_config": {
            "vector_store_id": "KNOWLEDGE_BASE_ID",
            "custom_llm_provider": "bedrock",
            "top_k": 5
        }
    }'
```

### Vertex AI[​](#vertex-ai "Direct link to Vertex AI")

RAG Query with Vertex AI

```
curl -X POST "http://localhost:4000/v1/rag/query" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "vertex_ai/gemini-1.5-pro",
        "messages": [{"role": "user", "content": "What is LiteLLM?"}],
        "retrieval_config": {
            "vector_store_id": "your-corpus-id",
            "custom_llm_provider": "vertex_ai",
            "top_k": 5
        }
    }'
```

## Python SDK[​](#python-sdk "Direct link to Python SDK")

Using litellm.aquery()

```
import litellm

response =await litellm.aquery(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"What is LiteLLM?"}],
    retrieval_config={
"vector_store_id":"vs_abc123",
"custom_llm_provider":"openai",
"top_k":5,
},
    rerank={
"enabled":True,
"model":"cohere/rerank-english-v3.0",
"top_n":3,
},
)

print(response.choices[0].message.content)
```