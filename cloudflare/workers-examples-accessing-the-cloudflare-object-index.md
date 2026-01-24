---
title: Accessing the Cloudflare Object
url: https://developers.cloudflare.com/workers/examples/accessing-the-cloudflare-object/index.md
source: llms
fetched_at: 2026-01-24T15:25:35.200117667-03:00
rendered_js: false
word_count: 114
summary: This document demonstrates how to access the `cf` object within Cloudflare Workers to retrieve custom metadata and properties associated with incoming requests.
tags:
    - cloudflare-workers
    - request-handling
    - cf-object
    - edge-computing
    - javascript
    - python
category: tutorial
---

---
title: Accessing the Cloudflare Object · Cloudflare Workers docs
description: Access custom Cloudflare properties and control how Cloudflare
  features are applied to every request.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/accessing-the-cloudflare-object/
  md: https://developers.cloudflare.com/workers/examples/accessing-the-cloudflare-object/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/accessing-the-cloudflare-object)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(req) {
      const data =
        req.cf !== undefined
          ? req.cf
          : { error: "The `cf` object is not available inside the preview." };


      return new Response(JSON.stringify(data, null, 2), {
        headers: {
          "content-type": "application/json;charset=UTF-8",
        },
      });
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(req): Promise<Response> {
      const data =
        req.cf !== undefined
          ? req.cf
          : { error: "The `cf` object is not available inside the preview." };


      return new Response(JSON.stringify(data, null, 2), {
        headers: {
          "content-type": "application/json;charset=UTF-8",
        },
      });
    },
  } satisfies ExportedHandler;
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.get("*", async (c) => {
    // Access the raw request to get the cf object
    const req = c.req.raw;


    // Check if the cf object is available
    const data =
      req.cf !== undefined
        ? req.cf
        : { error: "The `cf` object is not available inside the preview." };


    // Return the data formatted with 2-space indentation
    return c.json(data);
  });


  export default app;
  ```

* Python

  ```py
  import json
  from workers import Response, WorkerEntrypoint
  from js import JSON


  class Default(WorkerEntrypoint):
    async def fetch(self, request):
      error = json.dumps({ "error": "The `cf` object is not available inside the preview." })
      data = request.cf if request.cf is not None else error
      headers = {"content-type":"application/json"}
      return Response(JSON.stringify(data, None, 2), headers=headers)
  ```