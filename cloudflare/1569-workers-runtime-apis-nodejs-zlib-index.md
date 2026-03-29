---
title: zlib · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/zlib/index.md
source: llms
fetched_at: 2026-01-24T15:30:42.865681493-03:00
rendered_js: false
word_count: 68
summary: This document explains how to enable and use the Node.js zlib module for Gzip, Deflate, and Brotli compression within Cloudflare Workers using compatibility flags.
tags:
    - cloudflare-workers
    - nodejs-compat
    - zlib
    - compression
    - wrangler-configuration
    - nodejs-apis
category: api
---

Note

To enable built-in Node.js APIs and polyfills, add the nodejs\_compat compatibility flag to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). This also enables nodejs\_compat\_v2 as long as your compatibility date is 2024-09-23 or later. [Learn more about the Node.js compatibility flag and v2](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The node:zlib module provides compression functionality implemented using Gzip, Deflate/Inflate, and Brotli. To access it:

```js
import zlib from "node:zlib";
```

The full `node:zlib` API is documented in the [Node.js documentation for `node:zlib`](https://nodejs.org/api/zlib.html).