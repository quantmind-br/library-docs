---
title: "\U0001F4BE D1 · Cloudflare Workers docs"
url: https://developers.cloudflare.com/workers/testing/miniflare/storage/d1/index.md
source: llms
fetched_at: 2026-01-24T15:32:01.577895024-03:00
rendered_js: false
word_count: 41
summary: This document explains how to configure D1 databases in Miniflare and provides instructions for programmatically interacting with D1 storage for testing purposes.
tags:
    - miniflare
    - d1-databases
    - cloudflare-workers
    - local-development
    - unit-testing
    - database-bindings
category: guide
---

* [D1 Reference](https://developers.cloudflare.com/d1/)

## Databases

Specify D1 Databases to add to your environment as follows:

```js
const mf = new Miniflare({
  d1Databases:{
    DB:"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
});
```

## Working with D1 Databases

For testing, it can be useful to put/get data from D1 storage bound to a Worker. You can do this with the `getD1Database` method:

```js
const db = await mf.getD1Database("DB");
const stmt = await db.prepare("<Query>");
const returnValue = await stmt.run();


return Response.json(returnValue.results);
```