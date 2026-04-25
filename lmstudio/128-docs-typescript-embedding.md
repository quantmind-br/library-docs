---
title: Embedding
url: https://lmstudio.ai/docs/typescript/embedding
source: sitemap
fetched_at: 2026-04-07T21:28:59.387497091-03:00
rendered_js: false
word_count: 78
summary: This document explains the concept of text embeddings, which are vector representations capturing semantic meaning, and outlines the necessary steps to acquire an embedding model and generate embeddings using a provided method.
tags:
    - embeddings
    - text-representation
    - rag
    - vectorization
    - nlp
    - embedding-model
category: concept
---

Generate embeddings for input text. Embeddings are vector representations of text that capture semantic meaning. Embeddings are a building block for RAG (Retrieval-Augmented Generation) and other similarity-based tasks.

### Prerequisite: Get an Embedding Model[](#prerequisite-get-an-embedding-model)

If you don't yet have an embedding model, you can download a model like `nomic-ai/nomic-embed-text-v1.5` using the following command:

```

lms get nomic-ai/nomic-embed-text-v1.5
```

## Create Embeddings[](#create-embeddings "Link to 'Create Embeddings'")

To convert a string to a vector representation, pass it to the `embed` method on the corresponding embedding model handle.