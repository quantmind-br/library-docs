---
title: Alter headers
url: https://developers.cloudflare.com/workers/examples/alter-headers/index.md
source: llms
fetched_at: 2026-01-24T15:25:39.859147521-03:00
rendered_js: false
word_count: 86
summary: This document provides practical examples for adding, modifying, and deleting HTTP headers in requests and responses using Cloudflare Workers across multiple programming languages.
tags:
    - cloudflare-workers
    - http-headers
    - javascript
    - typescript
    - python
    - hono-framework
    - middleware
category: tutorial
---

---
title: Alter headers · Cloudflare Workers docs
description: Example of how to add, change, or delete headers sent in a request
  or returned in a response.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Headers,Middleware,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/alter-headers/
  md: https://developers.cloudflare.com/workers/examples/alter-headers/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/alter-headers)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const response = await fetch("https://example.com");


      // Clone the response so that it's no longer immutable
      const newResponse = new Response(response.body, response);


      // Add a custom header with a value
      newResponse.headers.append(
        "x-workers-hello",
        "Hello from Cloudflare Workers",
      );


      // Delete headers
      newResponse.headers.delete("x-header-to-delete");
      newResponse.headers.delete("x-header2-to-delete");


      // Adjust the value for an existing header
      newResponse.headers.set("x-header-to-change", "NewValue");


      return newResponse;
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const response = await fetch(request);


      // Clone the response so that it's no longer immutable
      const newResponse = new Response(response.body, response);


      // Add a custom header with a value
      newResponse.headers.append(
        "x-workers-hello",
        "Hello from Cloudflare Workers",
      );


      // Delete headers
      newResponse.headers.delete("x-header-to-delete");
      newResponse.headers.delete("x-header2-to-delete");


      // Adjust the value for an existing header
      newResponse.headers.set("x-header-to-change", "NewValue");


      return newResponse;
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import Response, fetch, WorkerEntrypoint


  class Default(WorkerEntrypoint):
    async def fetch(self, request):
        response = await fetch("https://example.com")


        # Grab the response headers so they can be modified
        new_headers = response.headers


        # Add a custom header with a value
        new_headers["x-workers-hello"] = "Hello from Cloudflare Workers"


        # Delete headers
        if "x-header-to-delete" in new_headers:
            del new_headers["x-header-to-delete"]
        if "x-header2-to-delete" in new_headers:
            del new_headers["x-header2-to-delete"]


        # Adjust the value for an existing header
        new_headers["x-header-to-change"] = "NewValue"


        return Response(response.body, headers=new_headers)
  ```

* Hono

  ```ts
  import { Hono } from 'hono';


  const app = new Hono();


  app.use('*', async (c, next) => {
    // Process the request with the next middleware/handler
    await next();


    // After the response is generated, we can modify its headers


    // Add a custom header with a value
    c.res.headers.append(
      "x-workers-hello",
      "Hello from Cloudflare Workers with Hono"
    );


    // Delete headers
    c.res.headers.delete("x-header-to-delete");
    c.res.headers.delete("x-header2-to-delete");


    // Adjust the value for an existing header
    c.res.headers.set("x-header-to-change", "NewValue");
  });


  app.get('*', async (c) => {
    // Fetch content from example.com
    const response = await fetch("https://example.com");


    // Return the response body with original headers
    // (our middleware will modify the headers before sending)
    return new Response(response.body, {
      headers: response.headers
    });
  });


  export default app;
  ```

You can also use the [`custom-headers-example` template](https://github.com/kristianfreeman/custom-headers-example) to deploy this code to your custom domain.