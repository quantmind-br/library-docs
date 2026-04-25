---
title: Embedding
url: https://lmstudio.ai/docs/python/embedding
source: sitemap
fetched_at: 2026-04-07T21:31:20.896437305-03:00
rendered_js: false
word_count: 78
summary: This document explains that embeddings are vector representations capturing semantic meaning, which serves as a foundational component for tasks like RAG and similarity searches, detailing how to obtain an embedding model and subsequently generate the required vectors.
tags:
    - embeddings
    - vector-representation
    - rag
    - semantic-meaning
    - nomic-embed-text-v1.5
category: guide
---

Generate embeddings for input text. Embeddings are vector representations of text that capture semantic meaning. Embeddings are a building block for RAG (Retrieval-Augmented Generation) and other similarity-based tasks.

### Prerequisite: Get an Embedding Model[](#prerequisite-get-an-embedding-model)

If you don't yet have an embedding model, you can download a model like `nomic-ai/nomic-embed-text-v1.5` using the following command:

```

lms get nomic-ai/nomic-embed-text-v1.5
```

## Create Embeddings[](#create-embeddings "Link to 'Create Embeddings'")

To convert a string to a vector representation, pass it to the `embed` method on the corresponding embedding model handle.