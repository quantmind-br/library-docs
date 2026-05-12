---
title: Embeddings & Reranking - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/querying-embeddings-models
source: sitemap
fetched_at: 2026-04-27T20:18:22.353445445-03:00
rendered_js: false
word_count: 254
summary: This document serves as a guide detailing how to use Fireworks AI's hosted embedding and reranking models for tasks like RAG and semantic search, providing API examples for both the /embeddings and /rerank endpoints. It also explains advanced usage patterns such as specifying dimensions and parallel batch processing.
tags:
    - fireworks-ai
    - embedding-models
    - reranking
    - semantic-search
    - api-guide
    - qwen3
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Embeddings & Reranking

Fireworks hosts embedding and reranking models for RAG and semantic search. The API is OpenAI-compatible — see OpenAI's [embeddings guide](https://platform.openai.com/docs/guides/embeddings) and [embeddings API reference](https://platform.openai.com/docs/api-reference/embeddings).

## Generating Embeddings

Embeddings models take text input and output a vector of floating-point numbers for similarity comparisons and search.

```python
import requests

url = "https://api.fireworks.ai/inference/v1/embeddings"

payload = {
    "input": "The quick brown fox jumped over the lazy dog",
    "model": "fireworks/qwen3-embedding-8b",
}

headers = {
    "Authorization": "Bearer <FIREWORKS_API_KEY>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

Use the `dimensions` parameter for variable-length embeddings (e.g., `dimensions: 128`). The API is identical for BERT-based and LLM-based embeddings.

### Available Embedding Models

| Model | Description |
|-------|-------------|
| `fireworks/qwen3-embedding-8b` | SOTA Qwen3 Embeddings — available on serverless |
| `fireworks/qwen3-embedding-4b` | Smaller variant |
| `fireworks/qwen3-embedding-0p6b` | Smallest variant |

## Reranking Documents

Reranking models reorder a list of documents by relevance to a query.

### Available Reranker Models

| Model | Description |
|-------|-------------|
| `fireworks/qwen3-reranker-8b` | SOTA Qwen3 Reranker — available on serverless |
| `fireworks/qwen3-reranker-4b` | Smaller variant |
| `fireworks/qwen3-reranker-0p6b` | Smallest variant |

### Using the `/rerank` Endpoint

```python
import requests

url = "https://api.fireworks.ai/inference/v1/rerank"

payload = {
    "model": "fireworks/qwen3-reranker-8b",
    "query": "What is the capital of France?",
    "documents": [
        "Paris is the capital and largest city of France, home to the Eiffel Tower and the Louvre Museum.",
        "France is a country in Western Europe known for its wine, cuisine, and rich history.",
        "The weather in Europe varies significantly between northern and southern regions.",
        "Python is a popular programming language used for web development and data science."
    ],
    "top_n": 3,
    "return_documents": True
}

headers = {
    "Authorization": "Bearer <FIREWORKS_API_KEY>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

### Using the `/embeddings` Endpoint with `return_logits`

Format prompts as query-document pairs using the Qwen3 Reranker format, then extract the "yes" token probability as the relevance score:

```python
import requests

url = "https://api.fireworks.ai/inference/v1/embeddings"

query = "What is the capital of France?"
documents = [
    "Paris is the capital and largest city of France...",
    "France is a country in Western Europe...",
    "The weather in Europe varies...",
    "Python is a popular programming language..."
]

# Format prompts as query-document pairs using the Qwen3 Reranker format
instruction = "Given a web search query, retrieve relevant passages that answer the query"
prompts = [
    f"<Instruct>: {instruction}\n<Query>: {query}\n<Document>: {doc}"
    for doc in documents
]

# Token IDs for "no" and "yes" in Qwen3 reranker models
token_false_id = 2753   # "no"
token_true_id = 9454    # "yes"

payload = {
    "model": "fireworks/qwen3-reranker-8b",
    "input": prompts,
    "return_logits": [token_false_id, token_true_id],
    "normalize": True  # Applies softmax to the selected logits
}

headers = {
    "Authorization": "Bearer <FIREWORKS_API_KEY>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers).json()

# Extract relevance scores (probability of "yes" token)
results = []
for i, item in enumerate(response["data"]):
    probs = item["embedding"]  # [no_prob, yes_prob]
    relevance_score = probs[1]
    results.append({
        "index": i,
        "relevance_score": relevance_score,
        "document": documents[i]
    })

results.sort(key=lambda x: x["relevance_score"], reverse=True)

for result in results:
    print(f"Score: {result['relevance_score']:.4f} - {result['document'][:80]}...")
```

### Parallel Batch Processing

For large document sets, improve throughput with parallel requests:

```python
import asyncio
import aiohttp

url = "https://api.fireworks.ai/inference/v1/embeddings"

query = "What is the capital of France?"
documents = [...]  # Your list of documents

instruction = "Given a web search query, retrieve relevant passages that answer the query"
prompts = [
    f"<Instruct>: {instruction}\n<Query>: {query}\n<Document>: {doc}"
    for doc in documents
]

token_false_id = 2753
token_true_id = 9454

headers = {
    "Authorization": "Bearer <FIREWORKS_API_KEY>",
    "Content-Type": "application/json"
}

async def rerank_batch(session, batch_prompts):
    payload = {
        "model": "fireworks/qwen3-reranker-8b",
        "input": batch_prompts,
        "return_logits": [token_false_id, token_true_id],
        "normalize": True
    }
    async with session.post(url, json=payload, headers=headers) as response:
        return await response.json()

async def rerank_parallel(prompts, batch_size=100):
    batches = [prompts[i:i+batch_size] for i in range(0, len(prompts), batch_size)]

    async with aiohttp.ClientSession() as session:
        tasks = [rerank_batch(session, batch) for batch in batches]
        results = await asyncio.gather(*tasks)

    all_scores = []
    for result in results:
        for item in result["data"]:
            all_scores.append(item["embedding"][1])  # "yes" probability

    return all_scores

scores = asyncio.run(rerank_parallel(prompts))
```

> [!note] With `normalize=True`, softmax is applied to the selected logits, returning probabilities that sum to 1. The "yes" probability directly represents the relevance score.

## Deploying Embeddings and Reranking Models

While Qwen3 Embedding 8b and Qwen3 Reranker 8b are available on serverless, you can also deploy them via [[070-guides-ondemand-deployments|on-demand deployments]] for dedicated GPU access.

#fireworks-ai #embedding-models #reranking #semantic-search #api-guide #qwen3
