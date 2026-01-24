---
title: Adding CORS headers
url: https://developers.cloudflare.com/pages/functions/examples/cors-headers/index.md
source: llms
fetched_at: 2026-01-24T15:18:47.1375343-03:00
rendered_js: false
word_count: 38
summary: This document provides code examples for implementing Cross-Origin Resource Sharing (CORS) headers within Cloudflare Pages Functions to handle preflight requests and cross-origin access.
tags:
    - cloudflare-pages
    - cors
    - http-headers
    - functions
    - typescript
category: guide
---

---
title: Adding CORS headers · Cloudflare Pages docs
description: A Pages Functions for appending CORS headers.
lastUpdated: 2025-09-15T21:45:20.000Z
chatbotDeprioritize: false
tags: Headers
source_url:
  html: https://developers.cloudflare.com/pages/functions/examples/cors-headers/
  md: https://developers.cloudflare.com/pages/functions/examples/cors-headers/index.md
---

This example is a snippet from our Cloudflare Pages Template repo.

```ts
// Respond to OPTIONS method
export const onRequestOptions: PagesFunction = async () => {
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
      "Access-Control-Allow-Methods": "GET, OPTIONS",
      "Access-Control-Max-Age": "86400",
    },
  });
};


// Set CORS to all /api responses
export const onRequest: PagesFunction = async (context) => {
  const response = await context.next();
  response.headers.set("Access-Control-Allow-Origin", "*");
  response.headers.set("Access-Control-Max-Age", "86400");
  return response;
};
```