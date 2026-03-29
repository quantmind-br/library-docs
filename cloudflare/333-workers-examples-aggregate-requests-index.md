---
title: Aggregate requests
url: https://developers.cloudflare.com/workers/examples/aggregate-requests/index.md
source: llms
fetched_at: 2026-01-24T15:25:39.502923669-03:00
rendered_js: false
word_count: 67
summary: This document demonstrates how to perform multiple concurrent network requests and aggregate their JSON responses into a single response using Cloudflare Workers.
tags:
    - cloudflare-workers
    - fetch-api
    - concurrent-requests
    - http-requests
    - serverless
    - json-aggregation
category: guide
---

---
title: Aggregate requests · Cloudflare Workers docs
description: Send two GET request to two urls and aggregates the responses into
  one response.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/aggregate-requests/
  md: https://developers.cloudflare.com/workers/examples/aggregate-requests/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/aggregate-requests)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      // someHost is set up to return JSON responses
      const someHost = "https://jsonplaceholder.typicode.com";
      const url1 = someHost + "/todos/1";
      const url2 = someHost + "/todos/2";


      const responses = await Promise.all([fetch(url1), fetch(url2)]);
      const results = await Promise.all(responses.map((r) => r.json()));


      const options = {
        headers: { "content-type": "application/json;charset=UTF-8" },
      };
      return new Response(JSON.stringify(results), options);
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request) {
      // someHost is set up to return JSON responses
      const someHost = "https://jsonplaceholder.typicode.com";
      const url1 = someHost + "/todos/1";
      const url2 = someHost + "/todos/2";


      const responses = await Promise.all([fetch(url1), fetch(url2)]);
      const results = await Promise.all(responses.map((r) => r.json()));


      const options = {
        headers: { "content-type": "application/json;charset=UTF-8" },
      };
      return new Response(JSON.stringify(results), options);
    },
  } satisfies ExportedHandler;
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.get("*", async (c) => {
    // someHost is set up to return JSON responses
    const someHost = "https://jsonplaceholder.typicode.com";
    const url1 = someHost + "/todos/1";
    const url2 = someHost + "/todos/2";


    // Fetch both URLs concurrently
    const responses = await Promise.all([fetch(url1), fetch(url2)]);


    // Parse JSON responses concurrently
    const results = await Promise.all(responses.map((r) => r.json()));


    // Return aggregated results
    return c.json(results);
  });


  export default app;
  ```

* Python

  ```py
  from workers import Response, fetch, WorkerEntrypoint
  import asyncio
  import json


  class Default(WorkerEntrypoint):
    async def fetch(self, request):
      # some_host is set up to return JSON responses
      some_host = "https://jsonplaceholder.typicode.com"
      url1 = some_host + "/todos/1"
      url2 = some_host + "/todos/2"


      responses = await asyncio.gather(fetch(url1), fetch(url2))
      results = await asyncio.gather(*(r.json() for r in responses))


      headers = {"content-type": "application/json;charset=UTF-8"}
      return Response.json(results, headers=headers)
  ```