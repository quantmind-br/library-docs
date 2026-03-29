---
title: Bulk redirects
url: https://developers.cloudflare.com/workers/examples/bulk-redirects/index.md
source: llms
fetched_at: 2026-01-24T15:25:44.469997403-03:00
rendered_js: false
word_count: 95
summary: This document provides code examples for implementing bulk URL redirects in Cloudflare Workers using a mapping object to route incoming request paths to specified destinations.
tags:
    - cloudflare-workers
    - redirects
    - url-mapping
    - javascript
    - typescript
    - python
    - serverless-functions
category: tutorial
---

---
title: Bulk redirects · Cloudflare Workers docs
description: Redirect requests to certain URLs based on a mapped object to the
  request's URL.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Middleware,Redirects,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/bulk-redirects/
  md: https://developers.cloudflare.com/workers/examples/bulk-redirects/index.md
---

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const externalHostname = "examples.cloudflareworkers.com";


      const redirectMap = new Map([
        ["/bulk1", "https://" + externalHostname + "/redirect2"],
        ["/bulk2", "https://" + externalHostname + "/redirect3"],
        ["/bulk3", "https://" + externalHostname + "/redirect4"],
        ["/bulk4", "https://google.com"],
      ]);


      const requestURL = new URL(request.url);
      const path = requestURL.pathname;
      const location = redirectMap.get(path);


      if (location) {
        return Response.redirect(location, 301);
      }
      // If request not in map, return the original request
      return fetch(request);
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const externalHostname = "examples.cloudflareworkers.com";


      const redirectMap = new Map([
        ["/bulk1", "https://" + externalHostname + "/redirect2"],
        ["/bulk2", "https://" + externalHostname + "/redirect3"],
        ["/bulk3", "https://" + externalHostname + "/redirect4"],
        ["/bulk4", "https://google.com"],
      ]);


      const requestURL = new URL(request.url);
      const path = requestURL.pathname;
      const location = redirectMap.get(path);


      if (location) {
        return Response.redirect(location, 301);
      }
      // If request not in map, return the original request
      return fetch(request);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch
  from urllib.parse import urlparse


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          external_hostname = "examples.cloudflareworkers.com"


          redirect_map = {
            "/bulk1": "https://" + external_hostname + "/redirect2",
            "/bulk2": "https://" + external_hostname + "/redirect3",
            "/bulk3": "https://" + external_hostname + "/redirect4",
            "/bulk4": "https://google.com",
            }


          url = urlparse(request.url)
          location = redirect_map.get(url.path, None)


          if location:
              return Response.redirect(location, 301)


          # If request not in map, return the original request
          return fetch(request)
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  // Configure your redirects
  const externalHostname = "examples.cloudflareworkers.com";


  const redirectMap = new Map([
    ["/bulk1", `https://${externalHostname}/redirect2`],
    ["/bulk2", `https://${externalHostname}/redirect3`],
    ["/bulk3", `https://${externalHostname}/redirect4`],
    ["/bulk4", "https://google.com"],
  ]);


  // Middleware to handle redirects
  app.use("*", async (c, next) => {
    const path = c.req.path;
    const location = redirectMap.get(path);


    if (location) {
      // If path is in our redirect map, perform the redirect
      return c.redirect(location, 301);
    }


    // Otherwise, continue to the next handler
    await next();
  });


  // Default handler for requests that don't match any redirects
  app.all("*", async (c) => {
    // Pass through to origin
    return fetch(c.req.raw);
  });


  export default app;
  ```