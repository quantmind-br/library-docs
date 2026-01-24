---
title: Watermarks · Cloudflare Images docs
url: https://developers.cloudflare.com/images/examples/watermark-from-kv/index.md
source: llms
fetched_at: 2026-01-24T15:15:15.586044057-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for applying a watermark to an image using Cloudflare Workers, R2 storage, KV namespaces, and the Images transformation API with integrated caching.
tags:
    - cloudflare-workers
    - r2-storage
    - kv-namespace
    - images-api
    - image-processing
    - caching
category: tutorial
---

```ts
interface Env {
    BUCKET: R2Bucket,
    NAMESPACE: KVNamespace,
    IMAGES: ImagesBinding,
}
export default {
    async fetch(request, env, ctx): Promise<Response> {
        const watermarkKey = "my-watermark";
        const sourceKey = "my-source-image";


        const cache = await caches.open("transformed-images");
        const cacheKey = new URL(sourceKey + "/" + watermarkKey, request.url);
        const cacheResponse = await cache.match(cacheKey);


        if (cacheResponse) {
            return cacheResponse;
        }


        let watermark = await env.NAMESPACE.get(watermarkKey, "stream");
        let source = await env.BUCKET.get(sourceKey);


        if (!watermark || !source) {
            return new Response("Not found", { status: 404 });
        }


        const result = await env.IMAGES.input(source.body)
            .draw(watermark)
            .output({ format: "image/jpeg" });


        const response = result.response();


        ctx.waitUntil(cache.put(cacheKey, response.clone()));


        return result.response();
  },
} satisfies ExportedHandler<Env>;
```