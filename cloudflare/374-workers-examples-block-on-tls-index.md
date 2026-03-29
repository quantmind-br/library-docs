---
title: Block on TLS
url: https://developers.cloudflare.com/workers/examples/block-on-tls/index.md
source: llms
fetched_at: 2026-01-24T15:25:43.984801702-03:00
rendered_js: false
word_count: 93
summary: Demonstrates how to use Cloudflare Workers to inspect the TLS version of incoming requests and block connections that do not meet security requirements.
tags:
    - cloudflare-workers
    - tls
    - security
    - middleware
    - javascript
    - typescript
    - python
    - request-handling
category: tutorial
---

---
title: Block on TLS · Cloudflare Workers docs
description: Inspects the incoming request's TLS version and blocks if under TLSv1.2.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Security,Middleware,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/block-on-tls/
  md: https://developers.cloudflare.com/workers/examples/block-on-tls/index.md
---

* JavaScript

  ```js
  export default {
    async fetch(request) {
      try {
        const tlsVersion = request.cf.tlsVersion;
        // Allow only TLS versions 1.2 and 1.3
        if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
          return new Response("Please use TLS version 1.2 or higher.", {
            status: 403,
          });
        }
        return fetch(request);
      } catch (err) {
        console.error(
          "request.cf does not exist in the previewer, only in production",
        );
        return new Response(`Error in workers script ${err.message}`, {
          status: 500,
        });
      }
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      try {
        const tlsVersion = request.cf.tlsVersion;
        // Allow only TLS versions 1.2 and 1.3
        if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
          return new Response("Please use TLS version 1.2 or higher.", {
            status: 403,
          });
        }
        return fetch(request);
      } catch (err) {
        console.error(
          "request.cf does not exist in the previewer, only in production",
        );
        return new Response(`Error in workers script ${err.message}`, {
          status: 500,
        });
      }
    },
  } satisfies ExportedHandler;
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  // Middleware to check TLS version
  app.use("*", async (c, next) => {
    // Access the raw request to get the cf object with TLS info
    const request = c.req.raw;
    const tlsVersion = request.cf?.tlsVersion;


    // Allow only TLS versions 1.2 and 1.3
    if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
      return c.text("Please use TLS version 1.2 or higher.", 403);
    }


    await next();


  });


  app.onError((err, c) => {
      console.error(
        "request.cf does not exist in the previewer, only in production",
      );
      return c.text(`Error in workers script: ${err.message}`, 500);
  });


  app.get("/", async (c) => {
    return c.text(`TLS Version: ${c.req.raw.cf.tlsVersion}`);
  });


  export default app;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          tls_version = request.cf.tlsVersion
          if tls_version not in ("TLSv1.2", "TLSv1.3"):
              return Response("Please use TLS version 1.2 or higher.", status=403)
          return fetch(request)
  ```