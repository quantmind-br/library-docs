---
title: Using timingSafeEqual
url: https://developers.cloudflare.com/workers/examples/protect-against-timing-attacks/index.md
source: llms
fetched_at: 2026-01-24T15:26:16.192782348-03:00
rendered_js: false
word_count: 206
summary: This document explains how to use the timingSafeEqual function in Cloudflare Workers to prevent timing side-channel attacks when comparing sensitive data.
tags:
    - cloudflare-workers
    - security
    - web-crypto
    - timing-attacks
    - cryptography
    - authentication
category: guide
---

---
title: Using timingSafeEqual · Cloudflare Workers docs
description: Protect against timing attacks by safely comparing values using
  `timingSafeEqual`.
lastUpdated: 2025-09-01T10:19:51.000Z
chatbotDeprioritize: false
tags: Security,Web Crypto,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/protect-against-timing-attacks/
  md: https://developers.cloudflare.com/workers/examples/protect-against-timing-attacks/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/protect-against-timing-attacks)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

The [`crypto.subtle.timingSafeEqual`](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/#timingsafeequal) function compares two values using a constant-time algorithm. The time taken is independent of the contents of the values.

When strings are compared using the equality operator (`==` or `===`), the comparison will end at the first mismatched character. By using `timingSafeEqual`, an attacker would not be able to use timing to find where at which point in the two strings there is a difference.

The `timingSafeEqual` function takes two `ArrayBuffer` or `TypedArray` values to compare. These buffers must be of equal length, otherwise an exception is thrown. Note that this function is not constant time with respect to the length of the parameters and also does not guarantee constant time for the surrounding code. Handling of secrets should be taken with care to not introduce timing side channels.

In order to compare two strings, you must use the [`TextEncoder`](https://developers.cloudflare.com/workers/runtime-apis/encoding/#textencoder) API.

* TypeScript

  ```ts
  interface Environment {
    MY_SECRET_VALUE?: string;
  }


  export default {
    async fetch(req: Request, env: Environment) {
      if (!env.MY_SECRET_VALUE) {
        return new Response("Missing secret binding", { status: 500 });
      }


      const authToken = req.headers.get("Authorization") || "";


      if (authToken.length !== env.MY_SECRET_VALUE.length) {
        return new Response("Unauthorized", { status: 401 });
      }


      const encoder = new TextEncoder();


      const a = encoder.encode(authToken);
      const b = encoder.encode(env.MY_SECRET_VALUE);


      if (a.byteLength !== b.byteLength) {
        return new Response("Unauthorized", { status: 401 });
      }


      if (!crypto.subtle.timingSafeEqual(a, b)) {
        return new Response("Unauthorized", { status: 401 });
      }


      return new Response("Welcome!");
    },
  };
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response
  from js import TextEncoder, crypto


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          auth_token = request.headers["Authorization"] or ""
          secret = self.env.MY_SECRET_VALUE


          if secret is None:
              return Response("Missing secret binding", status=500)


          if len(auth_token) != len(secret):
              return Response("Unauthorized", status=401)


          encoder = TextEncoder.new()
          a = encoder.encode(auth_token)
          b = encoder.encode(secret)


          if a.byteLength != b.byteLength:
              return Response("Unauthorized", status=401)


          if not crypto.subtle.timingSafeEqual(a, b):
              return Response("Unauthorized", status=401)


          return Response("Welcome!")
  ```

* Hono

  ```ts
  import { Hono } from 'hono';


  interface Environment {
    Bindings: {
      MY_SECRET_VALUE?: string;
    }
  }


  const app = new Hono<Environment>();


  // Middleware to handle authentication with timing-safe comparison
  app.use('*', async (c, next) => {
    const secret = c.env.MY_SECRET_VALUE;


    if (!secret) {
      return c.text("Missing secret binding", 500);
    }


    const authToken = c.req.header("Authorization") || "";


    // Early length check to avoid unnecessary processing
    if (authToken.length !== secret.length) {
      return c.text("Unauthorized", 401);
    }


    const encoder = new TextEncoder();


    const a = encoder.encode(authToken);
    const b = encoder.encode(secret);


    if (a.byteLength !== b.byteLength) {
      return c.text("Unauthorized", 401);
    }


    // Perform timing-safe comparison
    if (!crypto.subtle.timingSafeEqual(a, b)) {
      return c.text("Unauthorized", 401);
    }


    // If we got here, the auth token is valid
    await next();
  });


  // Protected route
  app.get('*', (c) => {
    return c.text("Welcome!");
  });


  export default app;
  ```