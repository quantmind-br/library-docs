---
title: Fetch HTML
url: https://developers.cloudflare.com/workers/examples/fetch-html/index.md
source: llms
fetched_at: 2026-01-24T15:25:59.016104518-03:00
rendered_js: false
word_count: 109
summary: This document demonstrates how to fetch HTML content from a remote server and serve it using Cloudflare Workers across different programming languages.
tags:
    - cloudflare-workers
    - fetch-api
    - http-requests
    - serverless
    - javascript
    - typescript
    - python
category: tutorial
---

---
title: Fetch HTML · Cloudflare Workers docs
description: Send a request to a remote server, read HTML from the response, and
  serve that HTML.
lastUpdated: 2025-08-20T18:47:44.000Z
chatbotDeprioritize: false
tags: JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/fetch-html/
  md: https://developers.cloudflare.com/workers/examples/fetch-html/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/fetch-html)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      /**
       * Replace `remote` with the host you wish to send requests to
       */
      const remote = "https://example.com";


      return await fetch(remote, request);
    },
  };
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwAOACzCAjADYAzAE4A7DOEBWAFwsWbYBzhcafASPHT5S1QFgAUAGF0VCAFMH2ACJQAzjHQeo0e2ok2ngExCRUcMCODABEUDSOAB4AdABWHjGkqFBgzpHRcQkp6THWdg7OENgAKnQwjoFwMDBgfARQ9sipcABucB68CLAQANTA6LjgjtbWSd5IJLiOqHDgECQA3lYkJP10VLxBjhC8ABYAFAiOAI4gjh4QAJSb2zskyABUH69vHyQASo4WnBeI4SAADK7jJzgkgAdz8pxIEFOYNOPnWdEo8M8SIg6BIHmcuBIV1u9wgHmR6B+Ow+yFpvHsD1JjmhYIYJBipwgEBgHjUyGQSUiLUcySZwEyVlpVwgIAQVF2cLgfiOJwuUPQTgANKzyQ9HkRXgBfHVWE1EayaZjaXT6Hj8IRiSSyRTKFRlexOFzuLw+PwdKiBYK6UgRKKxKKEXSZII5PKRmJkMDoMilWzeyo1OoNXbNVq8dqddL2GZWDYxYCqqgAfXGk1yMTUhSWxQyJutNrtoQdhmdJjd5hUzGsQA)

* TypeScript

  ```ts
  export default {
    async fetch(request: Request): Promise<Response> {
      /**
       * Replace `remote` with the host you wish to send requests to
       */
      const remote = "https://example.com";


      return await fetch(remote, request);
    },
  };
  ```

* Python

  ```py
  from workers import WorkerEntrypoint
  from js import fetch


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          # Replace `remote` with the host you wish to send requests to
          remote = "https://example.com"
          return await fetch(remote, request)
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.all("*", async (c) => {
    /**
     * Replace `remote` with the host you wish to send requests to
     */
    const remote = "https://example.com";


    // Forward the request to the remote server
    return await fetch(remote, c.req.raw);
  });


  export default app;
  ```