---
title: What is RAG
url: https://developers.cloudflare.com/ai-search/concepts/what-is-rag/index.md
source: llms
fetched_at: 2026-01-24T14:00:12.136365408-03:00
rendered_js: false
word_count: 376
summary: This document defines Retrieval-Augmented Generation (RAG) and explains how it integrates external data sources with large language models to provide accurate, grounded responses. It outlines the three-step pipeline of indexing, retrieval, and generation while highlighting the benefits of reducing model hallucinations without requiring fine-tuning.
tags:
    - retrieval-augmented-generation
    - rag
    - large-language-models
    - vector-database
    - artificial-intelligence
    - information-retrieval
    - llm-accuracy
category: concept
---

---
title: What is RAG · Cloudflare AI Search docs
description: Retrieval-Augmented Generation (RAG) is a way to use your own data
  with a large language model (LLM). Instead of relying only on what the model
  was trained on, RAG searches for relevant information from your data source
  and uses it to help answer questions.
lastUpdated: 2025-09-24T17:03:07.000Z
chatbotDeprioritize: false
tags: LLM
source_url:
  html: https://developers.cloudflare.com/ai-search/concepts/what-is-rag/
  md: https://developers.cloudflare.com/ai-search/concepts/what-is-rag/index.md
---

Retrieval-Augmented Generation (RAG) is a way to use your own data with a large language model (LLM). Instead of relying only on what the model was trained on, RAG searches for relevant information from your data source and uses it to help answer questions.

## How RAG works

Here’s a simplified overview of the RAG pipeline:

1. **Indexing:** Your content (e.g. docs, wikis, product information) is split into smaller chunks and converted into vectors using an embedding model. These vectors are stored in a vector database.
2. **Retrieval:** When a user asks a question, it’s also embedded into a vector and used to find the most relevant chunks from the vector database.
3. **Generation:** The retrieved content and the user’s original question are combined into a single prompt. An LLM uses that prompt to generate a response.

The resulting response should be accurate, relevant, and based on your own data.

![What is RAG](https://developers.cloudflare.com/_astro/RAG.Br2ehjiz_2lPBPi.webp)

How does AI Search work

To learn more details about how AI Search uses RAG under the hood, reference [How AI Search works](https://developers.cloudflare.com/ai-search/concepts/how-ai-search-works/).

## Why use RAG?

RAG lets you bring your own data into LLM generation without retraining or fine-tuning a model. It improves both accuracy and trust by retrieving relevant content at query time and using that as the basis for a response.

Benefits of using RAG:

* **Accurate and current answers:** Responses are based on your latest content, not outdated training data.
* **Control over information sources:** You define the knowledge base so answers come from content you trust.
* **Fewer hallucinations:** Responses are grounded in real, retrieved data, reducing made-up or misleading answers.
* **No model training required:** You can get high-quality results without building or fine-tuning your own LLM which can be time consuming and costly.

RAG is ideal for building AI-powered apps like:

* AI assistants for internal knowledge
* Support chatbots connected to your latest content
* Enterprise search across documentation and files