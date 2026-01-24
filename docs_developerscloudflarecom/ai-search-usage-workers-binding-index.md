---
title: Workers Binding
url: https://developers.cloudflare.com/ai-search/usage/workers-binding/index.md
source: llms
fetched_at: 2026-01-24T14:00:53.519684098-03:00
rendered_js: false
word_count: 654
summary: This document explains how to configure and use Cloudflare AI Search bindings within the Workers platform, detailing specific API methods for searching and generating context-aware responses.
tags:
    - cloudflare-workers
    - ai-search
    - bindings
    - wrangler-configuration
    - api-reference
    - serverless
category: reference
---

---
title: Workers Binding · Cloudflare AI Search docs
description: Cloudflare’s serverless platform allows you to run code at the edge
  to build full-stack applications with Workers. A binding enables your Worker
  or Pages Function to interact with resources on the Cloudflare Developer
  Platform.
lastUpdated: 2025-10-28T15:46:27.000Z
chatbotDeprioritize: false
tags: Bindings
source_url:
  html: https://developers.cloudflare.com/ai-search/usage/workers-binding/
  md: https://developers.cloudflare.com/ai-search/usage/workers-binding/index.md
---

Cloudflare’s serverless platform allows you to run code at the edge to build full-stack applications with [Workers](https://developers.cloudflare.com/workers/). A [binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/) enables your Worker or Pages Function to interact with resources on the Cloudflare Developer Platform.

To use your AI Search with Workers or Pages, create an AI binding either in the Cloudflare dashboard (refer to [AI bindings](https://developers.cloudflare.com/pages/functions/bindings/#workers-ai) for instructions), or you can update your [Wrangler file](https://developers.cloudflare.com/workers/wrangler/configuration/). To bind AI Search to your Worker, add the following to your Wrangler file:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "ai": {
      "binding": "AI"
    }
  }
  ```

* wrangler.toml

  ```toml
  [ai]
  binding = "AI" # i.e. available in your Worker on env.AI
  ```

AI Search is the new name for AutoRAG

API endpoints may still reference `autorag` for the time being. Functionality remains the same, and support for the new naming will be introduced gradually.

## `aiSearch()`

This method searches for relevant results from your data source and generates a response using your default model and the retrieved context, for an AI Search named `my-autorag`:

```js
const answer = await env.AI.autorag("my-autorag").aiSearch({
  query: "How do I train a llama to deliver coffee?",
  model: "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
  rewrite_query: true,
  max_num_results: 2,
  ranking_options: {
    score_threshold: 0.3
  },
  reranking: {
    enabled: true,
    model: "@cf/baai/bge-reranker-base"
  },
  stream: true,
});
```

### Parameters

`query` string required

The input query.

`model` string optional

The text-generation model that is used to generate the response for the query. For a list of valid options, check the AI Search Generation model Settings. Defaults to the generation model selected in the AI Search Settings.

`system_prompt` string optional

The system prompt for generating the answer.

`rewrite_query` boolean optional

Rewrites the original query into a search optimized query to improve retrieval accuracy. Defaults to `false`.

`max_num_results` number optional

The maximum number of results that can be returned from the Vectorize database. Defaults to `10`. Must be between `1` and `50`.

`ranking_options` object optional

Configurations for customizing result ranking. Defaults to `{}`.

* `score_threshold` number optional
  * The minimum match score required for a result to be considered a match. Defaults to `0`. Must be between `0` and `1`.

`reranking` object optional

Configurations for customizing reranking. Defaults to `{}`.

* `enabled` boolean optional

  * Enables or disables reranking, which reorders retrieved results based on semantic relevance using a reranking model. Defaults to `false`.

* `model` string optional

  * The reranking model to use when reranking is enabled.

`stream` boolean optional

Returns a stream of results as they are available. Defaults to `false`.

`filters` object optional

Narrow down search results based on metadata, like folder and date, so only relevant content is retrieved. For more details, refer to [Metadata filtering](https://developers.cloudflare.com/ai-search/configuration/metadata/).

### Response

This is the response structure without `stream` enabled.

```sh
{
    "object": "vector_store.search_results.page",
    "search_query": "How do I train a llama to deliver coffee?",
    "response": "To train a llama to deliver coffee:\n\n1. **Build trust** — Llamas appreciate patience (and decaf).\n2. **Know limits** — Max 3 cups per llama, per `llama-logistics.md`.\n3. **Use voice commands** — Start with \"Espresso Express!\"\n4.",
    "data": [
      {
        "file_id": "llama001",
        "filename": "llama/logistics/llama-logistics.md",
        "score": 0.45,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/logistics/",
        },
        "content": [
          {
            "id": "llama001",
            "type": "text",
            "text": "Llamas can carry 3 drinks max."
          }
        ]
      },
      {
        "file_id": "llama042",
        "filename": "llama/llama-commands.md",
        "score": 0.4,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/",
        },
        "content": [
          {
            "id": "llama042",
            "type": "text",
            "text": "Start with basic commands like 'Espresso Express!' Llamas love alliteration."
          }
        ]
      },
    ],
    "has_more": false,
    "next_page": null
}
```

## `search()`

This method searches for results from your corpus and returns the relevant results, for the AI Search instance named `my-autorag`:

```js
const answer = await env.AI.autorag("my-autorag").search({
  query: "How do I train a llama to deliver coffee?",
  rewrite_query: true,
  max_num_results: 2,
  ranking_options: {
    score_threshold: 0.3
  },
  reranking: {
    enabled: true,
    model: "@cf/baai/bge-reranker-base"
  }
});
```

### Parameters

`query` string required

The input query.

`rewrite_query` boolean optional

Rewrites the original query into a search optimized query to improve retrieval accuracy. Defaults to `false`.

`max_num_results` number optional

The maximum number of results that can be returned from the Vectorize database. Defaults to `10`. Must be between `1` and `50`.

`ranking_options` object optional

Configurations for customizing result ranking. Defaults to `{}`.

* `score_threshold` number optional
  * The minimum match score required for a result to be considered a match. Defaults to `0`. Must be between `0` and `1`.

`reranking` object optional

Configurations for customizing reranking. Defaults to `{}`.

* `enabled` boolean optional

  * Enables or disables reranking, which reorders retrieved results based on semantic relevance using a reranking model. Defaults to `false`.

* `model` string optional

  * The reranking model to use when reranking is enabled.

`filters` object optional

Narrow down search results based on metadata, like folder and date, so only relevant content is retrieved. For more details, refer to [Metadata filtering](https://developers.cloudflare.com/ai-search/configuration/metadata).

### Response

```sh
{
    "object": "vector_store.search_results.page",
    "search_query": "How do I train a llama to deliver coffee?",
    "data": [
      {
        "file_id": "llama001",
        "filename": "llama/logistics/llama-logistics.md",
        "score": 0.45,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/logistics/",
        },
        "content": [
          {
            "id": "llama001",
            "type": "text",
            "text": "Llamas can carry 3 drinks max."
          }
        ]
      },
      {
        "file_id": "llama042",
        "filename": "llama/llama-commands.md",
        "score": 0.4,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/",
        },
        "content": [
          {
            "id": "llama042",
            "type": "text",
            "text": "Start with basic commands like 'Espresso Express!' Llamas love alliteration."
          }
        ]
      },
    ],
    "has_more": false,
    "next_page": null
}
```

## Local development

Local development is supported by proxying requests to your deployed AI Search instance. When running in local mode, your application forwards queries to the configured remote AI Search instance and returns the generated responses as if they were served locally.