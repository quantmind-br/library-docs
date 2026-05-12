---
title: Rerank documents - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/rerank-documents
source: sitemap
fetched_at: 2026-04-27T20:19:03.349534105-03:00
rendered_js: false
word_count: 225
summary: This document details how to use the Fireworks AI API endpoint for reranking documents via a POST request. It specifies the required parameters in the request body, such as query, documents list, model name, and top_n count.
tags:
    - api-endpoint
    - rerank
    - fireworks-ai
    - rest-api
    - inference
    - document-retrieval
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Rerank documents

Reranks documents based on relevance to a search query using a reranker model.

## Endpoint

```
POST /inference/v1/rerank
```

## Authorization

Bearer authentication header: `Bearer <token>`

## Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `query` | string | Yes | The search query to use for reranking. |
| `documents` | array[string] | Yes | List of documents to rerank. Minimum 1 document. |
| `model` | string | Yes | Reranker model name (e.g., `accounts/fireworks/models/qwen3-reranker-8b`). |
| `top_n` | integer | No | Number of most relevant documents to return. Defaults to all. Min: 1. |
| `return_documents` | boolean | No | Whether to return document text in response. Defaults to `true`. |
| `task` | string | No | Task description to guide reranking. |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `object` | string | Always `"list"`. |
| `model` | string | Name of the model used. |
| `data` | array | Reranked documents ordered by relevance score (highest first). |
| `usage` | object | Token usage information. |

### Data Object

| Field | Type | Description |
|-------|------|-------------|
| `index` | integer | Original document index. |
| `relevance_score` | number | Relevance score. |
| `document` | string | Document text (if `return_documents=true`). |

## Example

```bash
curl --request POST \
  --url https://api.fireworks.ai/inference/v1/rerank \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "query": "What is machine learning?",
  "documents": [
    "Machine learning is a subset of AI.",
    "The weather is sunny today."
  ],
  "model": "accounts/fireworks/models/qwen3-reranker-8b",
  "top_n": 2,
  "return_documents": true,
  "task": "Given a web search query, retrieve relevant passages that answer the query"
}
'
```

```json
{
  "object": "list",
  "model": "accounts/fireworks/models/qwen3-reranker-8b",
  "data": [
    {
      "index": 0,
      "relevance_score": 0.95,
      "document": "Machine learning is a subset of AI."
    },
    {
      "index": 1,
      "relevance_score": 0.12,
      "document": "The weather is sunny today."
    }
  ],
  "usage": {
    "prompt_tokens": 50,
    "total_tokens": 50
  }
}
```
