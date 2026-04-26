---
title: Embeddings | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/embeddings
source: sitemap
fetched_at: 2026-04-26T04:13:03.360874436-03:00
rendered_js: false
word_count: 183
summary: Vector representations of text and code for semantic analysis and NLP tasks including retrieval and classification.
tags:
    - embeddings
    - vector-space
    - semantic-search
    - natural-language-processing
    - retrieval-augmented-generation
    - data-clustering
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Embeddings

**Embeddings** are vector representations of text that capture semantic meaning through position in high-dimensional vector space.

![Embeddings](https://docs.mistral.ai/img/embedding_graph.png)![Embeddings dark](https://docs.mistral.ai/img/embedding_graph_dark.png)

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Retrieval systems** | Power RAG (retrieval-augmented generation) |
| **Clustering** | Group unorganized data |
| **Classification** | Categorize large document sets |
| **Semantic code search** | Explore code databases and repositories |
| **Duplicate detection** | Find similar text or code |
| **Search** | Semantic search across sources |

## Embedding Models

| Model | Description |
|-------|-------------|
| [Text Embeddings](https://docs.mistral.ai/studio-api/knowledge-rag/embeddings/text_embeddings) | General-purpose efficient text embedding model |
| [Code Embeddings](https://docs.mistral.ai/studio-api/knowledge-rag/embeddings/code_embeddings) | Optimized for code databases, repositories, and coding assistants |

## Basic Usage

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

response = client.embeddings(
    model="mistral-embed-latest",
    input="The quick brown fox jumps over the lazy dog"
)

embedding = response.data[0].embedding
```

## Measuring Distance

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Compare embeddings
text1_embedding = client.embeddings(model="mistral-embed", input="Hello world").data[0].embedding
text2_embedding = client.embeddings(model="mistral-embed", input="Hi there").data[0].embedding

similarity = cosine_similarity(text1_embedding, text2_embedding)
```

## RAG Quickstart

For a complete RAG implementation example, see the [RAG Quickstart](https://docs.mistral.ai/studio-api/knowledge-rag/embeddings/rag_quickstart).

#embeddings #vector-space #semantic-search #natural-language-processing #retrieval-augmented-generation #data-clustering
