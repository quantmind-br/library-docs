---
title: Text Embeddings | Mistral Docs
url: https://docs.mistral.ai/capabilities/embeddings/text_embeddings
source: crawler
fetched_at: 2026-01-29T07:34:11.31438175-03:00
rendered_js: false
word_count: 250
summary: A guide to using Mistral AI's text embedding models, covering how to transform text into numerical vectors for applications like semantic search, clustering, and RAG.
tags:
    - Mistral AI
    - embeddings
    - NLP
    - API
    - vector search
category: guide
---

Embeddings are at the core of multiple enterprise use cases, such as **retrieval systems**, **clustering**, **code analytics**, **classification**, and a variety of search applications. Embedding content, allows you to perform semantic search and diverse NLP tasks for your applications.

[Open in Colab ↗](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/embeddings/embeddings.ipynb)

### How to Generate Embeddings

To generate text embeddings using Mistral AI's embeddings API, we can make a request to the API endpoint and specify the embedding model `mistral-embed`, along with providing a list of input texts. The API will then return the corresponding embeddings as numerical vectors, which can be used for further analysis or processing in NLP applications.

The output is an embedding object with the embeddings and the token usage information.

Let's take a look at the length of the first embedding:

It returns 1024, which means that our embedding dimension is 1024. The `mistral-embed` model generates embedding vectors of dimension 1024 for each text string, regardless of the text length. It's worth nothing that while higher dimensional embeddings can better capture text information and improve the performance of NLP tasks, they may require more computational resources for hosting and inference, and may result in increased latency and memory usage for storing and processing these embeddings. This trade-off between performance and computational resources should be considered when designing NLP systems that rely on text embeddings.

Below you will find some examples of how to use the Mistral Embeddings API and different use cases.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.