---
title: Redirect
url: https://developers.cloudflare.com/workers/examples/redirect/index.md
source: llms
fetched_at: 2026-01-24T15:26:18.341092378-03:00
rendered_js: false
word_count: 148
summary: This document provides code examples and instructions for implementing URL redirects in Cloudflare Workers using multiple programming languages and frameworks.
tags:
    - cloudflare-workers
    - redirects
    - javascript
    - typescript
    - python
    - rust
    - hono
category: tutorial
---

---
title: Redirect · Cloudflare Workers docs
description: Redirect requests from one URL to another or from one set of URLs
  to another set.
lastUpdated: 2025-08-20T18:47:44.000Z
chatbotDeprioritize: false
tags: Middleware,Redirects,JavaScript,TypeScript,Python,Rust
source_url:
  html: https://developers.cloudflare.com/workers/examples/redirect/
  md: https://developers.cloudflare.com/workers/examples/redirect/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/redirect)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

## Redirect all requests to one URL

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const destinationURL = "https://example.com";
      const statusCode = 301;
      return Response.redirect(destinationURL, statusCode);
    },
  };
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwBmYQDYAnIKkBGGQHZhALhYs2wDnC40+AkeKmyFwgLAAoAMLoqEAKY3sAESgBnGOhdRo1pSXV4CYhIqOGBbBgAiKBpbAA8AOgArFwjSVCgwe1DwqJiE5IjzKxt7CGwAFToYW184GBgwPgIoa2REuAA3OBdeBFgIAGpgdFxwW3NzOPckElxbVDhwCBIAbzMSEm66Kl4-WwheAAsACgRbAEcQWxcIAEpV9Y2SXmsb2evoEO8qAFUAJQAMiQGCQIocIBAYC4lMhkHFQg1bPEXsBUo8Ni8qG8bgQQC4rHNgSRhIIZER0SQzhAQAgqCQ-td3FikWceGdeBBjnMbtFmtZ-gCADQkHHU-EjWy3ckbAC+grMMqI5lUzHUmm0PH4QlEkmkpOMRWsdgczjcHi8LSovn8mlIITCkTChE0qT8GSyDoiZDA6DIhUsRtKFSqNU29UavD5VDaLmsEzMKwiwDg0QA+sNRpkIkpcnN8ikZcqVWrAhrdNqDHq5IpmOYgA)

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const destinationURL = "https://example.com";
      const statusCode = 301;
      return Response.redirect(destinationURL, statusCode);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response


  class Default(WorkerEntrypoint):
      def fetch(self, request):
          destinationURL = "https://example.com"
          statusCode = 301
          return Response.redirect(destinationURL, statusCode)
  ```

* Rust

  ```rs
  use worker::*;


  #[event(fetch)]
  async fn fetch(_req: Request, _env: Env, _ctx: Context) -> Result<Response> {
      let destination_url = Url::parse("https://example.com")?;
      let status_code = 301;
      Response::redirect_with_status(destination_url, status_code)
  }
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.all("*", (c) => {
    const destinationURL = "https://example.com";
    const statusCode = 301;
    return c.redirect(destinationURL, statusCode);
  });


  export default app;
  ```

## Redirect requests from one domain to another

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const base = "https://example.com";
      const statusCode = 301;


      const url = new URL(request.url);
      const { pathname, search } = url;


      const destinationURL = `${base}${pathname}${search}`;
      console.log(destinationURL);


      return Response.redirect(destinationURL, statusCode);
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const base = "https://example.com";
      const statusCode = 301;


      const url = new URL(request.url);
      const { pathname, search } = url;


      const destinationURL = `${base}${pathname}${search}`;
      console.log(destinationURL);


      return Response.redirect(destinationURL, statusCode);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response
  from urllib.parse import urlparse


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          base = "https://example.com"
          statusCode = 301


          url = urlparse(request.url)


          destinationURL = f'{base}{url.path}{url.query}'
          print(destinationURL)


          return Response.redirect(destinationURL, statusCode)
  ```

* Rust

  ```rs
  use worker::*;


  #[event(fetch)]
  async fn fetch(req: Request, _env: Env, _ctx: Context) -> Result<Response> {
      let mut base = Url::parse("https://example.com")?;
      let status_code = 301;


      let url = req.url()?;


      base.set_path(url.path());
      base.set_query(url.query());


      console_log!("{:?}", base.to_string());


      Response::redirect_with_status(base, status_code)
  }
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.all("*", (c) => {
    const base = "https://example.com";
    const statusCode = 301;


    const { pathname, search } = new URL(c.req.url);


    const destinationURL = `${base}${pathname}${search}`;
    console.log(destinationURL);


    return c.redirect(destinationURL, statusCode);
  });


  export default app;
  ```