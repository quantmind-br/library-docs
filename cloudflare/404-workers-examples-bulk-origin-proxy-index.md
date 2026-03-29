---
title: Bulk origin override
url: https://developers.cloudflare.com/workers/examples/bulk-origin-proxy/index.md
source: llms
fetched_at: 2026-01-24T15:25:44.788512596-03:00
rendered_js: false
word_count: 37
summary: This document provides implementation examples for using Cloudflare Workers to proxy incoming requests from multiple domain hostnames to different third-party origin URLs.
tags:
    - cloudflare-workers
    - origin-override
    - proxy
    - hostname-redirection
    - fetch-api
    - middleware
category: tutorial
---

---
title: Bulk origin override · Cloudflare Workers docs
description: Resolve requests to your domain to a set of proxy third-party origin URLs.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Middleware,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/bulk-origin-proxy/
  md: https://developers.cloudflare.com/workers/examples/bulk-origin-proxy/index.md
---

* JavaScript

  ```js
  export default {
    async fetch(request) {
      /**
       * An object with different URLs to fetch
       * @param {Object} ORIGINS
       */
      const ORIGINS = {
        "starwarsapi.yourdomain.com": "swapi.dev",
        "google.yourdomain.com": "www.google.com",
      };


      const url = new URL(request.url);


      // Check if incoming hostname is a key in the ORIGINS object
      if (url.hostname in ORIGINS) {
        const target = ORIGINS[url.hostname];
        url.hostname = target;
        // If it is, proxy request to that third party origin
        return fetch(url.toString(), request);
      }
      // Otherwise, process request as normal
      return fetch(request);
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      /**
       * An object with different URLs to fetch
       * @param {Object} ORIGINS
       */
      const ORIGINS = {
        "starwarsapi.yourdomain.com": "swapi.dev",
        "google.yourdomain.com": "www.google.com",
      };


      const url = new URL(request.url);


      // Check if incoming hostname is a key in the ORIGINS object
      if (url.hostname in ORIGINS) {
        const target = ORIGINS[url.hostname];
        url.hostname = target;
        // If it is, proxy request to that third party origin
        return fetch(url.toString(), request);
      }
      // Otherwise, process request as normal
      return fetch(request);
    },
  } satisfies ExportedHandler;
  ```

* Hono

  ```ts
  import { Hono } from "hono";
  import { proxy } from "hono/proxy";


  // An object with different URLs to fetch
  const ORIGINS: Record<string, string> = {
    "starwarsapi.yourdomain.com": "swapi.dev",
    "google.yourdomain.com": "www.google.com",
  };


  const app = new Hono();


  app.all("*", async (c) => {
    const url = new URL(c.req.url);


    // Check if incoming hostname is a key in the ORIGINS object
    if (url.hostname in ORIGINS) {
      const target = ORIGINS[url.hostname];
      url.hostname = target;


      // If it is, proxy request to that third party origin
      return proxy(url, c.req.raw);
    }


    // Otherwise, process request as normal
    return proxy(c.req.raw);
  });


  export default app;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint
  from js import fetch, URL


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          # A dict with different URLs to fetch
          ORIGINS = {
            "starwarsapi.yourdomain.com": "swapi.dev",
            "google.yourdomain.com": "www.google.com",
          }


          url = URL.new(request.url)


          # Check if incoming hostname is a key in the ORIGINS object
          if url.hostname in ORIGINS:
              url.hostname = ORIGINS[url.hostname]
              # If it is, proxy request to that third party origin
              return fetch(url.toString(), request)


          # Otherwise, process request as normal
          return fetch(request)
  ```