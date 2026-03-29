---
title: "\U0001FAA3 R2 · Cloudflare Workers docs"
url: https://developers.cloudflare.com/workers/testing/miniflare/storage/r2/index.md
source: llms
fetched_at: 2026-01-24T15:32:09.090447677-03:00
rendered_js: false
word_count: 86
summary: This document explains how to configure Cloudflare R2 buckets in Miniflare and interact with them using the getR2Bucket method for external manipulation during testing.
tags:
    - miniflare
    - cloudflare-r2
    - testing
    - r2-buckets
    - local-development
category: reference
---

* [R2 Reference](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)

## Buckets

Specify R2 Buckets to add to your environment as follows:

```js
const mf = new Miniflare({
  r2Buckets: ["BUCKET1", "BUCKET2"],
});
```

## Manipulating Outside Workers

For testing, it can be useful to put/get data from R2 storage outside a worker. You can do this with the `getR2Bucket` method:

```js
import { Miniflare } from "miniflare";


const mf = new Miniflare({
  modules: true,
  script: `
  export default {
    async fetch(request, env, ctx) {
      const object = await env.BUCKET.get("count");
      const value = parseInt(await object.text()) + 1;
      await env.BUCKET.put("count", value.toString());
      return new Response(value.toString());
    }
  }
  `,
  r2Buckets: ["BUCKET"],
});


const bucket = await mf.getR2Bucket("BUCKET");
await bucket.put("count", "1");


const res = await mf.dispatchFetch("http://localhost:8787/");
console.log(await res.text()); // 2
console.log(await (await bucket.get("count")).text()); // 2
```