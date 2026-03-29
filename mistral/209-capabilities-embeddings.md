---
title: Mistral Docs
url: https://docs.mistral.ai/capabilities/embeddings
source: crawler
fetched_at: 2026-01-29T07:33:08.656211743-03:00
rendered_js: false
word_count: 183
summary: This document introduces Mistral AI's Embeddings API, explaining how vector representations capture semantic meaning for applications like retrieval-augmented generation, clustering, and classification.
tags:
    - mistral-ai
    - embeddings
    - vector-space
    - natural-language-processing
    - semantic-search
    - retrieval-augmented-generation
    - text-embeddings
    - code-embeddings
category: concept
---

## Embeddings

**Embeddings** are **vector representations** of text that capture the **semantic meaning** of paragraphs through their position in a high-dimensional vector space. Mistral AI's Embeddings API offers cutting-edge, state-of-the-art embeddings for text and code, which can be used for many natural language processing (NLP) tasks.

![embedding_graph](https://docs.mistral.ai/img/embedding_graph.png)![embedding_graph](https://docs.mistral.ai/img/embedding_graph_dark.png)

Among the vast array of use cases for embeddings are **retrieval systems** powering **retrieval-augmented generation**, **clustering** of unorganized data, **classification** of vast amounts of documents, **semantic code search** to explore databases and repositories, **code analytics**, **duplicate detection**, and various kinds of search when dealing with multiple sources of raw text or code.

We provide two state-of-the-art embeddings:

- [Text Embeddings](https://docs.mistral.ai/capabilities/embeddings/text_embeddings): For embedding a wide variety of text, a general-purpose, efficient embedding model.
- [Code Embeddings](https://docs.mistral.ai/capabilities/embeddings/code_embeddings): Specially designed for code, perfect for embedding code databases, repositories, and powering coding assistants with state-of-the-art retrieval.

We will cover the fundamentals of the embeddings API, including how to measure the distance between text embeddings, and explore two main use cases: clustering and classification.

For a quick example and introduction on how to leverage embeddings for RAG (Retrieval-Augmented Generation), check out our [RAG Quickstart](https://docs.mistral.ai/capabilities/embeddings/rag_quickstart).