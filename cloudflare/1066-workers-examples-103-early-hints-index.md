---
title: 103 Early Hints
url: https://developers.cloudflare.com/workers/examples/103-early-hints/index.md
source: llms
fetched_at: 2026-01-24T15:25:34.194291551-03:00
rendered_js: false
word_count: 325
summary: This document explains how to implement and enable 103 Early Hints in Cloudflare Workers to improve page load performance by preloading static assets through HTTP Link headers.
tags:
    - cloudflare-workers
    - 103-early-hints
    - http-headers
    - performance-optimization
    - asset-preloading
    - web-performance
category: tutorial
---

---
title: 103 Early Hints · Cloudflare Workers docs
description: Allow a client to request static assets while waiting for the HTML response.
lastUpdated: 2025-09-17T11:26:09.000Z
chatbotDeprioritize: false
tags: Middleware,Headers,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/103-early-hints/
  md: https://developers.cloudflare.com/workers/examples/103-early-hints/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/103-early-hints)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

`103` Early Hints is an HTTP status code designed to speed up content delivery. When enabled, Cloudflare can cache the `Link` headers marked with preload and/or preconnect from HTML pages and serve them in a `103` Early Hints response before reaching the origin server. Browsers can use these hints to fetch linked assets while waiting for the origin’s final response, dramatically improving page load speeds.

To ensure Early Hints are enabled on your zone:

1. In the Cloudflare dashboard, go to the **Speed settings** page.

   [Go to **Settings**](https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization)

2. Go to **Content Optimization**.

3. Enable the **Early Hints** toggle to on.

You can return `Link` headers from a Worker running on your zone to speed up your page load times.

* JavaScript

  ```js
  const CSS = "body { color: red; }";
  const HTML = `
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>Early Hints test</title>
      <link rel="stylesheet" href="/test.css">
  </head>
  <body>
      <h1>Early Hints test page</h1>
  </body>
  </html>
  `;


  export default {
    async fetch(req) {
      // If request is for test.css, serve the raw CSS
      if (/test\.css$/.test(req.url)) {
        return new Response(CSS, {
          headers: {
            "content-type": "text/css",
          },
        });
      } else {
        // Serve raw HTML using Early Hints for the CSS file
        return new Response(HTML, {
          headers: {
            "content-type": "text/html",
            link: "</test.css>; rel=preload; as=style",
          },
        });
      }
    },
  };
  ```

* TypeScript

  ```js
  const CSS = "body { color: red; }";
  const HTML = `
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>Early Hints test</title>
      <link rel="stylesheet" href="/test.css">
  </head>
  <body>
      <h1>Early Hints test page</h1>
  </body>
  </html>
  `;


  export default {
    async fetch(req): Promise<Response> {
      // If request is for test.css, serve the raw CSS
      if (/test\.css$/.test(req.url)) {
        return new Response(CSS, {
          headers: {
            "content-type": "text/css",
          },
        });
      } else {
        // Serve raw HTML using Early Hints for the CSS file
        return new Response(HTML, {
          headers: {
            "content-type": "text/html",
            link: "</test.css>; rel=preload; as=style",
          },
        });
      }
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  import re
  from workers import Response, WorkerEntrypoint


  CSS = "body { color: red; }"
  HTML = """
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>Early Hints test</title>
      <link rel="stylesheet" href="/test.css">
  </head>
  <body>
      <h1>Early Hints test page</h1>
  </body>
  </html>
  """


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          if re.search("test.css", request.url):
              headers = {"content-type": "text/css"}
              return Response(CSS, headers=headers)
          else:
              headers = {"content-type": "text/html","link": "</test.css>; rel=preload; as=style"}
          return Response(HTML, headers=headers)
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  const CSS = "body { color: red; }";
  const HTML = `
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>Early Hints test</title>
      <link rel="stylesheet" href="/test.css">
  </head>
  <body>
      <h1>Early Hints test page</h1>
  </body>
  </html>
  `;


  // Serve CSS file
  app.get("/test.css", (c) => {
    return c.body(CSS, {
      headers: {
        "content-type": "text/css",
      },
    });
  });


  // Serve HTML with early hints
  app.get("*", (c) => {
    return c.html(HTML, {
      headers: {
        link: "</test.css>; rel=preload; as=style",
      },
    });
  });


  export default app;
  ```