---
title: "\U0001F4E6 KV · Cloudflare Workers docs"
url: https://developers.cloudflare.com/workers/testing/miniflare/storage/kv/index.md
source: llms
fetched_at: 2026-01-24T15:32:07.467775998-03:00
rendered_js: false
word_count: 101
summary: This document explains how to configure and interact with KV namespaces in the Miniflare environment, including programmatic access for testing outside of workers.
tags:
    - miniflare
    - cloudflare-workers
    - kv-namespaces
    - local-testing
    - key-value-storage
category: reference
---

* [KV Reference](https://developers.cloudflare.com/kv/api/)

## Namespaces

Specify KV namespaces to add to your environment as follows:

```js
const mf = new Miniflare({
  kvNamespaces: ["TEST_NAMESPACE1", "TEST_NAMESPACE2"],
});
```

You can now access KV namespaces in your workers:

```js
export default {
  async fetch(request, env) {
    return new Response(await env.TEST_NAMESPACE1.get("key"));
  },
};
```

Miniflare supports all KV operations and data types.

## Manipulating Outside Workers

For testing, it can be useful to put/get data from KV outside a worker. You can do this with the `getKVNamespace` method:

```js
import { Miniflare } from "miniflare";


const mf = new Miniflare({
  modules: true,
  script: `
  export default {
    async fetch(request, env, ctx) {
      const value = parseInt(await env.TEST_NAMESPACE.get("count")) + 1;
      await env.TEST_NAMESPACE.put("count", value.toString());
      return new Response(value.toString());
    },
  }
  `,
  kvNamespaces: ["TEST_NAMESPACE"],
});


const ns = await mf.getKVNamespace("TEST_NAMESPACE");
await ns.put("count", "1");


const res = await mf.dispatchFetch("http://localhost:8787/");
console.log(await res.text()); // 2
console.log(await ns.get("count")); // 2
```