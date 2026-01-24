---
title: Hot-link protection
url: https://developers.cloudflare.com/workers/examples/hot-link-protection/index.md
source: llms
fetched_at: 2026-01-24T15:26:04.718775822-03:00
rendered_js: false
word_count: 67
summary: This document explains how to implement hot-link protection using Cloudflare Workers to prevent unauthorized websites from linking to your content, specifically images, by inspecting the Referer header.
tags:
    - cloudflare-workers
    - hot-link-protection
    - security
    - http-headers
    - referer-header
    - image-protection
    - traffic-management
category: tutorial
---

---
title: Hot-link protection · Cloudflare Workers docs
description: Block other websites from linking to your content. This is useful
  for protecting images.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Security,Headers,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/hot-link-protection/
  md: https://developers.cloudflare.com/workers/examples/hot-link-protection/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/hot-link-protection)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const HOMEPAGE_URL = "https://tutorial.cloudflareworkers.com/";
      const PROTECTED_TYPE = "image/";


      // Fetch the original request
      const response = await fetch(request);


      // If it's an image, engage hotlink protection based on the
      // Referer header.
      const referer = request.headers.get("Referer");
      const contentType = response.headers.get("Content-Type") || "";


      if (referer && contentType.startsWith(PROTECTED_TYPE)) {
        // If the hostnames don't match, it's a hotlink
        if (new URL(referer).hostname !== new URL(request.url).hostname) {
          // Redirect the user to your website
          return Response.redirect(HOMEPAGE_URL, 302);
        }
      }


      // Everything is fine, return the response normally.
      return response;
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const HOMEPAGE_URL = "https://tutorial.cloudflareworkers.com/";
      const PROTECTED_TYPE = "image/";


      // Fetch the original request
      const response = await fetch(request);


      // If it's an image, engage hotlink protection based on the
      // Referer header.
      const referer = request.headers.get("Referer");
      const contentType = response.headers.get("Content-Type") || "";


      if (referer && contentType.startsWith(PROTECTED_TYPE)) {
        // If the hostnames don't match, it's a hotlink
        if (new URL(referer).hostname !== new URL(request.url).hostname) {
          // Redirect the user to your website
          return Response.redirect(HOMEPAGE_URL, 302);
        }
      }


      // Everything is fine, return the response normally.
      return response;
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch
  from urllib.parse import urlparse


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          homepage_url = "https://tutorial.cloudflareworkers.com/"
          protected_type = "image/"


          # Fetch the original request
          response = await fetch(request)


          # If it's an image, engage hotlink protection based on the referer header
          referer = request.headers["Referer"]
          content_type = response.headers["Content-Type"] or ""


          if referer and content_type.startswith(protected_type):
              # If the hostnames don't match, it's a hotlink
              if urlparse(referer).hostname != urlparse(request.url).hostname:
                  # Redirect the user to your website
                  return Response.redirect(homepage_url, 302)


          # Everything is fine, return the response normally
          return response
  ```

* Hono

  ```ts
  import { Hono } from 'hono';


  const app = new Hono();


  // Middleware for hot-link protection
  app.use('*', async (c, next) => {
    const HOMEPAGE_URL = "https://tutorial.cloudflareworkers.com/";
    const PROTECTED_TYPE = "image/";


    // Continue to the next handler to get the response
    await next();


    // If we have a response, check for hotlinking
    if (c.res) {
      // If it's an image, engage hotlink protection based on the Referer header
      const referer = c.req.header("Referer");
      const contentType = c.res.headers.get("Content-Type") || "";


      if (referer && contentType.startsWith(PROTECTED_TYPE)) {
        // If the hostnames don't match, it's a hotlink
        if (new URL(referer).hostname !== new URL(c.req.url).hostname) {
          // Redirect the user to your website
          c.res = c.redirect(HOMEPAGE_URL, 302);
        }
      }
    }
  });


  // Default route handler that passes through the request to the origin
  app.all('*', async (c) => {
    // Fetch the original request
    return fetch(c.req.raw);
  });


  export default app;
  ```