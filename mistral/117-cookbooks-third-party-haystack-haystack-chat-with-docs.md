---
title: Using Mistral AI with Haystack - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-haystack-haystack_chat_with_docs
source: crawler
fetched_at: 2026-01-29T07:34:07.632944835-03:00
rendered_js: false
word_count: 233
---

In this cookbook, we will use Mistral embeddings and generative models in 2 [Haystack](https://github.com/deepset-ai/haystack) pipelines:

1. We will build an indexing pipeline that can create embeddings for the contents of URLs and indexes them into a vector database
2. We will build a retrieval-augmented chat pipeline to chat with the contents of the URLs

First, we install our dependencies

Next, we need to set the `MISTRAL_API_KEY` environment variable 👇

## Index URLs with Mistral Embeddings

Below, we are using `mistral-embed` in a full Haystack indexing pipeline. We create embeddings for the contents of the chosen URLs with `mistral-embed` and write them to an [`InMemoryDocumentStore`](https://docs.haystack.deepset.ai/v2.0/docs/inmemorydocumentstore) using the [`MistralDocumentEmbedder`](https://docs.haystack.deepset.ai/v2.0/docs/mistraldocumentembedder).

> 💡This document store is the simplest to get started with as it has no requirements to setup. Feel free to change this document store to any of the [vector databases available for Haystack 2.0](https://haystack.deepset.ai/integrations?type=Document%20Store) such as **Weaviate**, **Chroma**, **AstraDB** etc.

## Chat With the URLs with Mistral Generative Models

Now that we have indexed the contents and embeddings of various URLs, we can create a RAG pipeline that uses the [`MistralChatGenerator`](https://docs.haystack.deepset.ai/v2.0/docs/mistralchatgenerator) component with `mistral-small`. A few more things to know about this pipeline:

- We are using the [`MistralTextEmbdder`](https://docs.haystack.deepset.ai/v2.0/docs/mistraltextembedder) to embed our question and retrieve the most relevant 1 document
- We are enabling streaming responses by providing a `streaming_callback`
- `documents` is being provided to the chat template by the retriever, while we provide `query` to the pipeline when we run it.