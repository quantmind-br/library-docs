---
title: Wrangler's unstable_startWorker() · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/testing/unstable_startworker/index.md
source: llms
fetched_at: 2026-01-24T15:26:57.010468207-03:00
rendered_js: false
word_count: 99
summary: This document explains how to use Wrangler's experimental unstable_startWorker API to programmatically control the dev server for testing Cloudflare Workers outside of Vitest.
tags:
    - cloudflare-workers
    - wrangler
    - testing
    - integration-testing
    - unstable-api
category: guide
---

Note

For most users, Cloudflare recommends using the Workers Vitest integration. If you have been using `unstable_dev()`, refer to the [Migrate from `unstable_dev()` guide](https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-from-unstable-dev/).

Warning

`unstable_startWorker()` is an experimental API subject to breaking changes.

If you do not want to use Vitest, consider using [Wrangler's `unstable_startWorker()` API](https://developers.cloudflare.com/workers/wrangler/api/#unstable_startworker). This API exposes the internals of Wrangler's dev server, and allows you to customise how it runs. Compared to using [Miniflare directly for testing](https://developers.cloudflare.com/workers/testing/miniflare/writing-tests/), you can pass in a Wrangler configuration file, and it will automatically load the configuration for you.

This example uses `node:test`, but should apply to any testing framework:

```ts
import assert from "node:assert";
import test, { after, before, describe } from "node:test";
import { unstable_startWorker } from "wrangler";


describe("worker", () => {
  let worker;


  before(async () => {
    worker = await unstable_startWorker({ config: "wrangler.json" });
  });


  test("hello world", async () => {
    assert.strictEqual(
      await (await worker.fetch("http://example.com")).text(),
      "Hello world",
    );
  });


  after(async () => {
    await worker.dispose();
  });
});
```