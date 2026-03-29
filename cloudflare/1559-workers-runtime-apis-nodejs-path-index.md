---
title: path · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/path/index.md
source: llms
fetched_at: 2026-01-24T15:30:34.915989573-03:00
rendered_js: false
word_count: 70
summary: This document explains how to enable and use the built-in Node.js path module in Cloudflare Workers using the nodejs_compat compatibility flag.
tags:
    - cloudflare-workers
    - nodejs-compatibility
    - path-module
    - wrangler-configuration
    - compatibility-flags
category: reference
---

Note

To enable built-in Node.js APIs and polyfills, add the nodejs\_compat compatibility flag to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). This also enables nodejs\_compat\_v2 as long as your compatibility date is 2024-09-23 or later. [Learn more about the Node.js compatibility flag and v2](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`node:path`](https://nodejs.org/api/path.html) module provides utilities for working with file and directory paths. The `node:path` module can be accessed using:

```js
import path from "node:path";
path.join("/foo", "bar", "baz/asdf", "quux", "..");
// Returns: '/foo/bar/baz/asdf'
```

Refer to the [Node.js documentation for `path`](https://nodejs.org/api/path.html) for more information.