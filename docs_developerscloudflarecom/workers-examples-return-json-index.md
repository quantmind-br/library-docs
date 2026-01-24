---
title: Return JSON
url: https://developers.cloudflare.com/workers/examples/return-json/index.md
source: llms
fetched_at: 2026-01-24T15:26:21.075617609-03:00
rendered_js: false
word_count: 71
summary: This document provides code examples for returning JSON responses from Cloudflare Workers using multiple programming languages and frameworks to build APIs and middleware.
tags:
    - cloudflare-workers
    - json
    - api-development
    - javascript
    - typescript
    - python
    - rust
    - hono
category: tutorial
---

---
title: Return JSON · Cloudflare Workers docs
description: Return JSON directly from a Worker script, useful for building APIs
  and middleware.
lastUpdated: 2025-08-20T18:47:44.000Z
chatbotDeprioritize: false
tags: JSON,JavaScript,TypeScript,Python,Rust
source_url:
  html: https://developers.cloudflare.com/workers/examples/return-json/
  md: https://developers.cloudflare.com/workers/examples/return-json/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/return-json)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const data = {
        hello: "world",
      };


      return Response.json(data);
    },
  };
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwB2AMwBOAKziAbDOmjJALhYs2wDnC40+AkROlyFkgLAAoAMLoqEAKY3sAESgBnGOhdRo1pSXV4CYhIqOGBbBgAiKBpbAA8AOgArFwjSVCgwe1DwqJiE5IjzKxt7CGwAFToYW184GBgwPgIoa2REuAA3OBdeBFgIAGpgdFxwW3NzOPckElxbVDhwCBIAbzMSEm66Kl4-WwheAAsACgRbAEcQWxcIAEpV9Y2SXmsb2cCSBgenp8PbMDA6F8EQA7pgwLgIgAaR4bAC+RDMsJIZwgIAQVBIACVru4qC5bEkXNZjppboj4TCEeZVMx1JptDx+EIxFJZPJxIoitY7A5nG4PF4WlRfP5NKQQmFImFCJpUn4MlkpREyICyIVLDzShUqjVNvVGrxmq1ktYJmYVhFgHBogB9YajTIRJS5Ob5FJwmm0+mBRm6FkGdnGZjmIA)

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const data = {
        hello: "world",
      };


      return Response.json(data);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response
  import json


  class Default(WorkerEntrypoint):
      def fetch(self, request):
          data = json.dumps({"hello": "world"})
          headers = {"content-type": "application/json"}
          return Response(data, headers=headers)
  ```

* Rust

  ```rs
  use serde::{Deserialize, Serialize};
  use worker::*;


  #[derive(Deserialize, Serialize, Debug)]
  struct Json {
      hello: String,
  }


  #[event(fetch)]
  async fn fetch(_req: Request, _env: Env, _ctx: Context) -> Result<Response> {
      let data = Json {
          hello: String::from("world"),
      };
      Response::from_json(&data)
  }
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.get("*", (c) => {
    const data = {
      hello: "world",
    };


    return c.json(data);
  });


  export default app;
  ```