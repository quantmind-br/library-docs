---
title: Auth with headers
url: https://developers.cloudflare.com/workers/examples/auth-with-headers/index.md
source: llms
fetched_at: 2026-01-24T15:25:39.56411603-03:00
rendered_js: false
word_count: 86
summary: Explains how to implement basic request authentication in Cloudflare Workers by verifying a pre-shared key within a custom request header.
tags:
    - cloudflare-workers
    - authentication
    - request-headers
    - pre-shared-key
    - security
    - access-control
category: tutorial
---

---
title: Auth with headers · Cloudflare Workers docs
description: Allow or deny a request based on a known pre-shared key in a
  header. This is not meant to replace the WebCrypto API.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Authentication,Web Crypto,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/auth-with-headers/
  md: https://developers.cloudflare.com/workers/examples/auth-with-headers/index.md
---

Caution when using in production

The example code contains a generic header key and value of `X-Custom-PSK` and `mypresharedkey`. To best protect your resources, change the header key and value in the Workers editor before saving your code.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      /**
       * @param {string} PRESHARED_AUTH_HEADER_KEY Custom header to check for key
       * @param {string} PRESHARED_AUTH_HEADER_VALUE Hard coded key value
       */
      const PRESHARED_AUTH_HEADER_KEY = "X-Custom-PSK";
      const PRESHARED_AUTH_HEADER_VALUE = "mypresharedkey";
      const psk = request.headers.get(PRESHARED_AUTH_HEADER_KEY);


      if (psk === PRESHARED_AUTH_HEADER_VALUE) {
        // Correct preshared header key supplied. Fetch request from origin.
        return fetch(request);
      }


      // Incorrect key supplied. Reject the request.
      return new Response("Sorry, you have supplied an invalid key.", {
        status: 403,
      });
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      /**
       * @param {string} PRESHARED_AUTH_HEADER_KEY Custom header to check for key
       * @param {string} PRESHARED_AUTH_HEADER_VALUE Hard coded key value
       */
      const PRESHARED_AUTH_HEADER_KEY = "X-Custom-PSK";
      const PRESHARED_AUTH_HEADER_VALUE = "mypresharedkey";
      const psk = request.headers.get(PRESHARED_AUTH_HEADER_KEY);


      if (psk === PRESHARED_AUTH_HEADER_VALUE) {
        // Correct preshared header key supplied. Fetch request from origin.
        return fetch(request);
      }


      // Incorrect key supplied. Reject the request.
      return new Response("Sorry, you have supplied an invalid key.", {
        status: 403,
      });
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          PRESHARED_AUTH_HEADER_KEY = "X-Custom-PSK"
          PRESHARED_AUTH_HEADER_VALUE = "mypresharedkey"


          psk = request.headers[PRESHARED_AUTH_HEADER_KEY]


          if psk == PRESHARED_AUTH_HEADER_VALUE:
              # Correct preshared header key supplied. Fetch request from origin.
              return fetch(request)


          # Incorrect key supplied. Reject the request.
          return Response("Sorry, you have supplied an invalid key.", status=403)
  ```

* Hono

  ```ts
  import { Hono } from 'hono';


  const app = new Hono();


  // Add authentication middleware
  app.use('*', async (c, next) => {
    /**
     * Define authentication constants
     */
    const PRESHARED_AUTH_HEADER_KEY = "X-Custom-PSK";
    const PRESHARED_AUTH_HEADER_VALUE = "mypresharedkey";


    // Get the pre-shared key from the request header
    const psk = c.req.header(PRESHARED_AUTH_HEADER_KEY);


    if (psk === PRESHARED_AUTH_HEADER_VALUE) {
      // Correct preshared header key supplied. Continue to the next handler.
      await next();
    } else {
      // Incorrect key supplied. Reject the request.
      return c.text("Sorry, you have supplied an invalid key.", 403);
    }
  });


  // Handle all authenticated requests by passing through to origin
  app.all('*', async (c) => {
    return fetch(c.req.raw);
  });


  export default app;
  ```