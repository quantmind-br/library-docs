---
title: /rag/ingest | liteLLM
url: https://docs.litellm.ai/docs/rag_ingest
source: sitemap
fetched_at: 2026-01-21T19:54:07.195221763-03:00
rendered_js: false
word_count: 328
summary: This document details the LiteLLM RAG ingestion pipeline, providing API specifications and configuration options for uploading, chunking, and embedding documents across vector store providers like OpenAI, AWS Bedrock, and Vertex AI.
tags:
    - rag-ingestion
    - vector-stores
    - openai
    - aws-bedrock
    - vertex-ai
    - embeddings
    - api-reference
category: api
---

All-in-one document ingestion pipeline: **Upload → Chunk → Embed → Vector Store**

FeatureSupportedLoggingYesSupported Providers`openai`, `bedrock`, `vertex_ai`, `gemini`

tip

After ingesting documents, use [/rag/query](https://docs.litellm.ai/docs/rag_query) to search and generate responses with your ingested content.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### OpenAI[​](#openai "Direct link to OpenAI")

Ingest to OpenAI vector store

```
curl -X POST "http://localhost:4000/v1/rag/ingest" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d "{
        \"file\": {
            \"filename\": \"document.txt\",
            \"content\": \"$(base64 -i document.txt)\",
            \"content_type\": \"text/plain\"
        },
        \"ingest_options\": {
            \"vector_store\": {
                \"custom_llm_provider\": \"openai\"
            }
        }
    }"
```

### Bedrock[​](#bedrock "Direct link to Bedrock")

Ingest to Bedrock Knowledge Base

```
curl -X POST "http://localhost:4000/v1/rag/ingest" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d "{
        \"file\": {
            \"filename\": \"document.txt\",
            \"content\": \"$(base64 -i document.txt)\",
            \"content_type\": \"text/plain\"
        },
        \"ingest_options\": {
            \"vector_store\": {
                \"custom_llm_provider\": \"bedrock\"
            }
        }
    }"
```

### Vertex AI RAG Engine[​](#vertex-ai-rag-engine "Direct link to Vertex AI RAG Engine")

Ingest to Vertex AI RAG Corpus

```
curl -X POST "http://localhost:4000/v1/rag/ingest" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d "{
        \"file\": {
            \"filename\": \"document.txt\",
            \"content\": \"$(base64 -i document.txt)\",
            \"content_type\": \"text/plain\"
        },
        \"ingest_options\": {
            \"vector_store\": {
                \"custom_llm_provider\": \"vertex_ai\",
                \"vector_store_id\": \"your-corpus-id\",
                \"gcs_bucket\": \"your-gcs-bucket\"
            }
        }
    }"
```

## Response[​](#response "Direct link to Response")

```
{
"id":"ingest_abc123",
"status":"completed",
"vector_store_id":"vs_xyz789",
"file_id":"file_123"
}
```

## Query with RAG[​](#query-with-rag "Direct link to Query with RAG")

After ingestion, use the [/rag/query](https://docs.litellm.ai/docs/rag_query) endpoint to search and generate LLM responses:

RAG Query

```
curl -X POST "http://localhost:4000/v1/rag/query" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "What is the main topic?"}],
        "retrieval_config": {
            "vector_store_id": "vs_xyz789",
            "custom_llm_provider": "openai",
            "top_k": 5
        }
    }'
```

This will:

1. Search the vector store for relevant context
2. Prepend the context to your messages
3. Generate an LLM response

### Direct Vector Store Search[​](#direct-vector-store-search "Direct link to Direct Vector Store Search")

Alternatively, search the vector store directly with `/vector_stores/{vector_store_id}/search`:

Search the vector store

```
curl -X POST "http://localhost:4000/v1/vector_stores/vs_xyz789/search" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "query": "What is the main topic?",
        "max_num_results": 5
    }'
```

## End-to-End Example[​](#end-to-end-example "Direct link to End-to-End Example")

### OpenAI[​](#openai-1 "Direct link to OpenAI")

#### 1. Ingest Document[​](#1-ingest-document "Direct link to 1. Ingest Document")

Step 1: Ingest

```
curl -X POST "http://localhost:4000/v1/rag/ingest" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d "{
        \"file\": {
            \"filename\": \"test_document.txt\",
            \"content\": \"$(base64 -i test_document.txt)\",
            \"content_type\": \"text/plain\"
        },
        \"ingest_options\": {
            \"name\": \"test-basic-ingest\",
            \"vector_store\": {
                \"custom_llm_provider\": \"openai\"
            }
        }
    }"
```

Response:

```
{
"id":"ingest_d834f544-fc5e-4751-902d-fb0bcc183b85",
"status":"completed",
"vector_store_id":"vs_692658d337c4819183f2ad8488d12fc9",
"file_id":"file-M2pJJiWH56cfUP4Fe7rJay"
}
```

#### 2. Query[​](#2-query "Direct link to 2. Query")

Step 2: Query

```
curl -X POST "http://localhost:4000/v1/vector_stores/vs_692658d337c4819183f2ad8488d12fc9/search" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "query": "What is LiteLLM?",
        "custom_llm_provider": "openai"
    }'
```

Response:

```
{
"object":"vector_store.search_results.page",
"search_query":["What is LiteLLM?"],
"data":[
{
"file_id":"file-M2pJJiWH56cfUP4Fe7rJay",
"filename":"test_document.txt",
"score":0.4004629778869299,
"attributes":{},
"content":[
{
"type":"text",
"text":"Test document abc123 for RAG ingestion.\nThis is a sample document to test the RAG ingest API.\nLiteLLM provides a unified interface for vector stores."
}
]
}
],
"has_more":false,
"next_page":null
}
```

## Request Parameters[​](#request-parameters "Direct link to Request Parameters")

### Top-Level[​](#top-level "Direct link to Top-Level")

ParameterTypeRequiredDescription`file`objectOne of file/file\_url/file\_id requiredBase64-encoded file`file.filename`stringYesFilename with extension`file.content`stringYesBase64-encoded content`file.content_type`stringYesMIME type (e.g., `text/plain`)`file_url`stringOne of file/file\_url/file\_id requiredURL to fetch file from`file_id`stringOne of file/file\_url/file\_id requiredExisting file ID`ingest_options`objectYesPipeline configuration

### ingest\_options[​](#ingest_options "Direct link to ingest_options")

ParameterTypeRequiredDescription`vector_store`objectYesVector store configuration`name`stringNoPipeline name for logging

### vector\_store (OpenAI)[​](#vector_store-openai "Direct link to vector_store (OpenAI)")

ParameterTypeDefaultDescription`custom_llm_provider`string-`"openai"``vector_store_id`stringauto-createExisting vector store ID

### vector\_store (Bedrock)[​](#vector_store-bedrock "Direct link to vector_store (Bedrock)")

ParameterTypeDefaultDescription`custom_llm_provider`string-`"bedrock"``vector_store_id`stringauto-createExisting Knowledge Base ID`wait_for_ingestion`boolean`false`Wait for indexing to complete`ingestion_timeout`integer`300`Timeout in seconds (if waiting)`s3_bucket`stringauto-createS3 bucket for documents`s3_prefix`string`"data/"`S3 key prefix`embedding_model`string`amazon.titan-embed-text-v2:0`Bedrock embedding model`aws_region_name`string`us-west-2`AWS region

Bedrock Auto-Creation

When `vector_store_id` is omitted, LiteLLM automatically creates:

- S3 bucket for document storage
- OpenSearch Serverless collection
- IAM role with required permissions
- Bedrock Knowledge Base
- Data Source

### vector\_store (Vertex AI)[​](#vector_store-vertex-ai "Direct link to vector_store (Vertex AI)")

ParameterTypeDefaultDescription`custom_llm_provider`string-`"vertex_ai"``vector_store_id`string**required**RAG corpus ID`gcs_bucket`string**required**GCS bucket for file uploads`vertex_project`stringenv `VERTEXAI_PROJECT`GCP project ID`vertex_location`string`us-central1`GCP region`vertex_credentials`stringADCPath to credentials JSON`wait_for_import`boolean`true`Wait for import to complete`import_timeout`integer`600`Timeout in seconds (if waiting)

Vertex AI Prerequisites

1. Create a RAG corpus in Vertex AI console or via API
2. Create a GCS bucket for file uploads
3. Authenticate via `gcloud auth application-default login`
4. Install: `pip install 'google-cloud-aiplatform>=1.60.0'`

## Input Examples[​](#input-examples "Direct link to Input Examples")

### File (Base64)[​](#file-base64 "Direct link to File (Base64)")

Request body

```
{
"file":{
"filename":"document.txt",
"content":"<base64-encoded-content>",
"content_type":"text/plain"
},
"ingest_options":{
"vector_store":{"custom_llm_provider":"openai"}
}
}
```

### File URL[​](#file-url "Direct link to File URL")

Ingest from URL

```
curl -X POST "http://localhost:4000/v1/rag/ingest" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "file_url": "https://example.com/document.pdf",
        "ingest_options": {"vector_store": {"custom_llm_provider": "openai"}}
    }'
```

## Chunking Strategy[​](#chunking-strategy "Direct link to Chunking Strategy")

Control how documents are split into chunks before embedding. Specify `chunking_strategy` in `ingest_options`.

ParameterTypeDefaultDescription`chunk_size`integer`1000`Maximum size of each chunk`chunk_overlap`integer`200`Overlap between consecutive chunks

### Vertex AI RAG Engine[​](#vertex-ai-rag-engine-1 "Direct link to Vertex AI RAG Engine")

Vertex AI RAG Engine supports custom chunking via the `chunking_strategy` parameter. Chunks are processed server-side during import.

Vertex AI with custom chunking

```
curl -X POST "http://localhost:4000/v1/rag/ingest" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d "{
        \"file\": {
            \"filename\": \"document.txt\",
            \"content\": \"$(base64 -i document.txt)\",
            \"content_type\": \"text/plain\"
        },
        \"ingest_options\": {
            \"chunking_strategy\": {
                \"chunk_size\": 500,
                \"chunk_overlap\": 100
            },
            \"vector_store\": {
                \"custom_llm_provider\": \"vertex_ai\",
                \"vector_store_id\": \"your-corpus-id\",
                \"gcs_bucket\": \"your-gcs-bucket\"
            }
        }
    }"
```