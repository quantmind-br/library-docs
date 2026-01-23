---
title: /vector_stores - Create Vector Store | liteLLM
url: https://docs.litellm.ai/docs/vector_stores/create
source: sitemap
fetched_at: 2026-01-21T19:55:54.943458005-03:00
rendered_js: false
word_count: 32
summary: This document explains how to create vector stores for document chunk storage and retrieval in RAG systems, following the OpenAI API format and utilizing tools like litellm for testing.
tags:
    - vector-stores
    - rag
    - openai-api
    - litellm
    - document-retrieval
    - chunking-strategy
category: api
---

Create a vector store which can be used to store and search document chunks for retrieval-augmented generation (RAG) use cases.

The request body follows OpenAI's vector stores API format.

```
{
"name":"My Document Store",
"file_ids":["file-abc123","file-def456"],
"expires_after":{
"anchor":"last_active_at",
"days":7
},
"chunking_strategy":{
"type":"static",
"static":{
"max_chunk_size_tokens":800,
"chunk_overlap_tokens":400
}
},
"metadata":{
"project":"rag-system",
"environment":"production"
}
}
```

```
{
"id":"vs_abc123",
"object":"vector_store",
"created_at":1699061776,
"name":"My Document Store",
"bytes":139920,
"file_counts":{
"in_progress":0,
"completed":2,
"failed":0,
"cancelled":0,
"total":2
},
"status":"completed",
"expires_after":{
"anchor":"last_active_at",
"days":7
},
"expires_at":null,
"last_active_at":1699061776,
"metadata":{
"project":"rag-system",
"environment":"production"
}
}
```

Mock Response Example

```
import litellm

# Mock response for testing
mock_response ={
"id":"vs_mock123",
"object":"vector_store",
"created_at":1699061776,
"name":"Mock Vector Store",
"bytes":0,
"file_counts":{
"in_progress":0,
"completed":0,
"failed":0,
"cancelled":0,
"total":0
},
"status":"completed"
}

response =await litellm.vector_stores.acreate(
    name="Test Store",
    mock_response=mock_response
)
print(response)
```