---
title: Configuration · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/configuration/index.md
source: llms
fetched_at: 2026-01-24T14:00:15.784124508-03:00
rendered_js: false
word_count: 345
summary: This document provides a comprehensive list of configuration settings for AI Search instances, detailing which parameters are editable after creation and their specific roles in indexing, retrieval, and generation.
tags:
    - ai-search
    - configuration
    - indexing
    - retrieval
    - query-rewriting
    - embedding-models
    - chunking
category: configuration
---

You can customize how your AI Search instance indexes your data, and retrieves and generates responses for queries. Some settings can be updated after the instance is created, while others are fixed at creation time.

The table below lists all available configuration options:

| Configuration | Editable after creation | Description |
| - | - | - |
| [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) | no | The source where your knowledge base is stored |
| [Path filtering](https://developers.cloudflare.com/ai-search/configuration/path-filtering/) | yes | Include or exclude specific paths from indexing |
| [Chunk size](https://developers.cloudflare.com/ai-search/configuration/chunking/) | yes | Number of tokens per chunk |
| [Chunk overlap](https://developers.cloudflare.com/ai-search/configuration/chunking/) | yes | Number of overlapping tokens between chunks |
| [Embedding model](https://developers.cloudflare.com/ai-search/configuration/models/) | no | Model used to generate vector embeddings |
| [Query rewrite](https://developers.cloudflare.com/ai-search/configuration/query-rewriting/) | yes | Enable or disable query rewriting before retrieval |
| [Query rewrite model](https://developers.cloudflare.com/ai-search/configuration/models/) | yes | Model used for query rewriting |
| [Query rewrite system prompt](https://developers.cloudflare.com/ai-search/configuration/system-prompt/) | yes | Custom system prompt to guide query rewriting behavior |
| [Match threshold](https://developers.cloudflare.com/ai-search/configuration/retrieval-configuration/) | yes | Minimum similarity score required for a vector match |
| [Maximum number of results](https://developers.cloudflare.com/ai-search/configuration/retrieval-configuration/) | yes | Maximum number of vector matches returned (`top_k`) |
| [Reranking](https://developers.cloudflare.com/ai-search/configuration/reranking/) | yes | Rerank to reorder retrieved results by semantic relevance using a reranking model after initial retrieval |
| [Generation model](https://developers.cloudflare.com/ai-search/configuration/models/) | yes | Model used to generate the final response |
| [Generation system prompt](https://developers.cloudflare.com/ai-search/configuration/system-prompt/) | yes | Custom system prompt to guide response generation |
| [Similarity caching](https://developers.cloudflare.com/ai-search/configuration/cache/) | yes | Enable or disable caching of responses for similar (not just exact) prompts |
| [Similarity caching threshold](https://developers.cloudflare.com/ai-search/configuration/cache/) | yes | Controls how similar a new prompt must be to a previous one to reuse its cached response |
| [AI Gateway](https://developers.cloudflare.com/ai-gateway) | yes | AI Gateway for monitoring and controlling model usage |
| AI Search name | no | Name of your AI Search instance |
| [Service API token](https://developers.cloudflare.com/ai-search/configuration/service-api-token/) | yes | API token that grants AI Search permission to configure resources on your account |