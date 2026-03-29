---
title: /vector_stores/\{vector_store_id\}/files | liteLLM
url: https://docs.litellm.ai/docs/vector_store_files
source: sitemap
fetched_at: 2026-01-21T19:55:53.678184345-03:00
rendered_js: false
word_count: 167
summary: This document outlines the API endpoints and client methods for managing vector store files, detailing operations such as creating, listing, retrieving, and deleting files through the LiteLLM proxy and OpenAI.
tags:
    - vector-stores
    - litellm-proxy
    - openai-api
    - file-management
    - rag-systems
    - api-endpoints
category: api
---

Vector store files represent the individual files that live inside a vector store.

FeatureSupportedLogging✅ (full request/response logging)Supported Providers`openai`

## Supported operations[​](#supported-operations "Direct link to Supported operations")

OperationDescriptionOpenAI Python ClientLiteLLM ProxyCreate vector store fileAttach a file to a vector store with optional chunking overrides✅✅List vector store filesPaginated listing with filters✅✅Retrieve vector store fileFetch metadata for a single file✅✅Delete vector store fileRemove a file from a store (file object persists)✅✅Retrieve vector store file contentStream processed chunks❌✅Update vector store file attributesPatch custom attributes❌✅

note

Vector store support currently works **only with OpenAI vector stores and OpenAI-uploaded file IDs**.

## Create vector store file[​](#create-vector-store-file "Direct link to Create vector store file")

`POST http://localhost:4000/v1/vector_stores/&#123;vector_store_id&#125;/files`

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000",# LiteLLM proxy or OpenAI base
    api_key="sk-1234"
)

vector_store_file = client.vector_stores.files.create(
    vector_store_id="vs_69172088a18c8191ab3e2621aa87d1ee",
    file_id="file-NDbEDJTfqVh7S4Ugi3CGYw",
    chunking_strategy={
"type":"static",
"static":{
"max_chunk_size_tokens":800,
"chunk_overlap_tokens":400,
},
},
)

print(vector_store_file)
```

## List vector store files[​](#list-vector-store-files "Direct link to List vector store files")

`GET http://localhost:4000/v1/vector_stores/&#123;vector_store_id&#125;/files`

Parameters:

- `vector_store_id` (path, required)
- `after` / `before` (query, optional) – pagination cursors
- `filter` (query, optional) – `in_progress`, `completed`, `failed`, `cancelled`
- `limit` (query, optional, default `20`, range `1-100`)
- `order` (query, optional, default `desc`)

```
vector_store_files = client.vector_stores.files.list(
    vector_store_id="vs_abc123"
)
print(vector_store_files)
```

## Retrieve vector store file[​](#retrieve-vector-store-file "Direct link to Retrieve vector store file")

`GET http://localhost:4000/v1/vector_stores/&#123;vector_store_id&#125;/files/&#123;file_id&#125;`

```
vector_store_file = client.vector_stores.files.retrieve(
    vector_store_id="vs_abc123",
    file_id="file-abc123"
)
print(vector_store_file)
```

## Delete vector store file[​](#delete-vector-store-file "Direct link to Delete vector store file")

`DELETE http://localhost:4000/v1/vector_stores/&#123;vector_store_id&#125;/files/&#123;file_id&#125;`

```
deleted_vector_store_file = client.vector_stores.files.delete(
    vector_store_id="vs_abc123",
    file_id="file-abc123"
)
print(deleted_vector_store_file)
```

## Proxy-only endpoints[​](#proxy-only-endpoints "Direct link to Proxy-only endpoints")

When you need raw content chunks or attribute updates, call the LiteLLM Proxy directly.

### Retrieve file content[​](#retrieve-file-content "Direct link to Retrieve file content")

```
curl -X GET "http://localhost:4000/v1/vector_stores/\{vector_store_id\}/files/\{file_id\}/content" \
  -H "Authorization: Bearer sk-1234"
```

### Update file attributes[​](#update-file-attributes "Direct link to Update file attributes")

```
curl -X POST "http://localhost:4000/v1/vector_stores/\{vector_store_id\}/files/\{file_id\}" \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
        "attributes": {
          "category": "support-faq",
          "language": "en"
        }
      }'
```