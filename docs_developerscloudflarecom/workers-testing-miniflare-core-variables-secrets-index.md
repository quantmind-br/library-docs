---
title: "\U0001F511 Variables and Secrets · Cloudflare Workers docs"
url: https://developers.cloudflare.com/workers/testing/miniflare/core/variables-secrets/index.md
source: llms
fetched_at: 2026-01-24T15:31:49.825603062-03:00
rendered_js: false
word_count: 59
summary: This document explains how to configure variable, secret, and blob bindings in Miniflare and how they are injected as globals.
tags:
    - miniflare
    - cloudflare-workers
    - bindings
    - configuration
    - environment-variables
category: configuration
---

## Bindings

Variables and secrets are bound as follows:

```js
const mf = new Miniflare({
  bindings: {
    KEY1: "value1",
    KEY2: "value2",
  },
});
```

## Text and Data Blobs

Text and data blobs can be loaded from files. File contents will be read and bound as `string`s and `ArrayBuffer`s respectively.

```js
const mf = new Miniflare({
  textBlobBindings: { TEXT: "text.txt" },
  dataBlobBindings: { DATA: "data.bin" },
});
```

## Globals

Injecting arbitrary globals is not supported by [workerd](https://github.com/cloudflare/workerd). If you're using a service Worker, bindings will be injected as globals, but these must be JSON-serializable.