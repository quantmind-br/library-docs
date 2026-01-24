---
title: Custom Domain with Images
url: https://developers.cloudflare.com/workers/examples/images-workers/index.md
source: llms
fetched_at: 2026-01-24T15:26:07.182863076-03:00
rendered_js: false
word_count: 240
summary: This document explains how to serve images from a custom domain using Cloudflare Workers or a URL prefix to proxy requests to the Cloudflare Images delivery service.
tags:
    - cloudflare-workers
    - cloudflare-images
    - custom-domain
    - image-delivery
    - serverless
    - proxy
category: tutorial
---

---
title: Custom Domain with Images · Cloudflare Workers docs
description: Set up custom domain for Images using a Worker or serve images
  using a prefix path and Cloudflare registered domain.
lastUpdated: 2025-09-09T12:12:09.000Z
chatbotDeprioritize: false
tags: JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/images-workers/
  md: https://developers.cloudflare.com/workers/examples/images-workers/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/images-workers)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

To serve images from a custom domain:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

   [Go to **Workers & Pages**](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

2. Select **Create application** > **Workers** > **Create Worker** and create your Worker.

3. In your Worker, select **Quick edit** and paste the following code.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      // You can find this in the dashboard, it should look something like this: ZWd9g1K7eljCn_KDTu_MWA
      const accountHash = "";


      const { pathname } = new URL(request.url);


      // A request to something like cdn.example.com/83eb7b2-5392-4565-b69e-aff66acddd00/public
      // will fetch "https://imagedelivery.net/<accountHash>/83eb7b2-5392-4565-b69e-aff66acddd00/public"


      return fetch(`https://imagedelivery.net/${accountHash}${pathname}`);
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      // You can find this in the dashboard, it should look something like this: ZWd9g1K7eljCn_KDTu_MWA
      const accountHash = "";


      const { pathname } = new URL(request.url);


      // A request to something like cdn.example.com/83eb7b2-5392-4565-b69e-aff66acddd00/public
      // will fetch "https://imagedelivery.net/<accountHash>/83eb7b2-5392-4565-b69e-aff66acddd00/public"


      return fetch(`https://imagedelivery.net/${accountHash}${pathname}`);
    },
  } satisfies ExportedHandler;
  ```

* Hono

  ```ts
  import { Hono } from 'hono';


  interface Env {
    // You can store your account hash as a binding variable
    ACCOUNT_HASH?: string;
  }


  const app = new Hono<{ Bindings: Env }>();


  app.get('*', async (c) => {
    // You can find this in the dashboard, it should look something like this: ZWd9g1K7eljCn_KDTu_MWA
    // Either get it from environment or hardcode it here
    const accountHash = c.env.ACCOUNT_HASH || "";


    const url = new URL(c.req.url);


    // A request to something like cdn.example.com/83eb7b2-5392-4565-b69e-aff66acddd00/public
    // will fetch "https://imagedelivery.net/<accountHash>/83eb7b2-5392-4565-b69e-aff66acddd00/public"


    return fetch(`https://imagedelivery.net/${accountHash}${url.pathname}`);
  });


  export default app;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint
  from js import URL, fetch


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          # You can find this in the dashboard, it should look something like this: ZWd9g1K7eljCn_KDTu_MWA
          account_hash = ""
          url = URL.new(request.url)


          # A request to something like cdn.example.com/83eb7b2-5392-4565-b69e-aff66acddd00/public
          # will fetch "https://imagedelivery.net/<accountHash>/83eb7b2-5392-4565-b69e-aff66acddd00/public"
          return fetch(f'https://imagedelivery.net/{account_hash}{url.pathname}')
  ```

Another way you can serve images from a custom domain is by using the `cdn-cgi/imagedelivery` prefix path which is used as path to trigger `cdn-cgi` image proxy.

Below is an example showing the hostname as a Cloudflare proxied domain under the same account as the Image, followed with the prefix path and the image `<ACCOUNT_HASH>`, `<IMAGE_ID>` and `<VARIANT_NAME>` which can be found in the **Images** on the Cloudflare dashboard.

```js
https://example.com/cdn-cgi/imagedelivery/<ACCOUNT_HASH>/<IMAGE_ID>/<VARIANT_NAME>
```