---
title: Create a simple search engine · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/index.md
source: llms
fetched_at: 2026-01-24T15:06:44.574124789-03:00
rendered_js: false
word_count: 63
summary: This document demonstrates how to implement a fast search engine using the Cloudflare AI Search search method and Workers Binding.
tags:
    - cloudflare-workers
    - ai-search
    - search-method
    - workers-binding
    - javascript
    - typescript
category: tutorial
---

By using the `search` method, you can implement a simple but fast search engine. This example uses [Workers Binding](https://developers.cloudflare.com/ai-search/usage/workers-binding/), but can be easily adapted to use the [REST API](https://developers.cloudflare.com/ai-search/usage/rest-api/) instead.

To replicate this example remember to:

* Disable `rewrite_query`, as you want to match the original user query
* Configure your AI Search to have small chunk sizes, usually 256 tokens is enough

- JavaScript

  ```js
  export default {
    async fetch(request, env) {
      const url = new URL(request.url);
      const userQuery =
        url.searchParams.get("query") ??
        "How do I train a llama to deliver coffee?";
      const searchResult = await env.AI.autorag("my-rag").search({
        query: userQuery,
        rewrite_query: false,
      });


      return Response.json({
        files: searchResult.data.map((obj) => obj.filename),
      });
    },
  };
  ```

- TypeScript

  ```ts
  export interface Env {
    AI: Ai;
  }


  export default {
    async fetch(request, env): Promise<Response> {
      const url = new URL(request.url);
      const userQuery =
        url.searchParams.get("query") ??
        "How do I train a llama to deliver coffee?";
      const searchResult = await env.AI.autorag("my-rag").search({
        query: userQuery,
        rewrite_query: false,
      });


      return Response.json({
        files: searchResult.data.map((obj) => obj.filename),
      });
    },
  } satisfies ExportedHandler<Env>;
  ```