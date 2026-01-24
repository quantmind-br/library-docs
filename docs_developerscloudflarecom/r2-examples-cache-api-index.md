---
title: Use the Cache API · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/examples/cache-api/index.md
source: llms
fetched_at: 2026-01-24T15:21:17.80477983-03:00
rendered_js: false
word_count: 63
summary: This document explains how to use the Cloudflare Workers Cache API to cache objects retrieved from R2 storage for improved performance.
tags:
    - cloudflare-workers
    - cache-api
    - r2-storage
    - performance-optimization
    - object-storage
category: guide
---

Use the [Cache API](https://developers.cloudflare.com/workers/runtime-apis/cache/) to store R2 objects in Cloudflare's cache.

Note

You will need to [connect a custom domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) or [route](https://developers.cloudflare.com/workers/configuration/routing/routes/) to your Worker in order to use the Cache API. Cache API operations in the Cloudflare Workers dashboard editor, Playground previews, and any `*.workers.dev` deployments will have no impact.

```js
export default {
  async fetch(request, env, context) {
    try {
      const url = new URL(request.url);


      // Construct the cache key from the cache URL
      const cacheKey = new Request(url.toString(), request);
      const cache = caches.default;


      // Check whether the value is already available in the cache
      // if not, you will need to fetch it from R2, and store it in the cache
      // for future access
      let response = await cache.match(cacheKey);


      if (response) {
        console.log(`Cache hit for: ${request.url}.`);
        return response;
      }


      console.log(
        `Response for request url: ${request.url} not present in cache. Fetching and caching request.`
      );


      // If not in cache, get it from R2
      const objectKey = url.pathname.slice(1);
      const object = await env.MY_BUCKET.get(objectKey);
      if (object === null) {
        return new Response('Object Not Found', { status: 404 });
      }


      // Set the appropriate object headers
      const headers = new Headers();
      object.writeHttpMetadata(headers);
      headers.set('etag', object.httpEtag);


      // Cache API respects Cache-Control headers. Setting s-max-age to 10
      // will limit the response to be in cache for 10 seconds max
      // Any changes made to the response here will be reflected in the cached value
      headers.append('Cache-Control', 's-maxage=10');


      response = new Response(object.body, {
        headers,
      });


      // Store the fetched response as cacheKey
      // Use waitUntil so you can return the response without blocking on
      // writing to cache
      context.waitUntil(cache.put(cacheKey, response.clone()));


      return response;
    } catch (e) {
      return new Response('Error thrown ' + e.message);
    }
  },
};
```