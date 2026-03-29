---
title: Recipes and examples · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/testing/vitest-integration/recipes/index.md
source: llms
fetched_at: 2026-01-24T15:29:44.534524173-03:00
rendered_js: false
word_count: 152
summary: This document provides a collection of example recipes for performing unit and integration testing on Cloudflare Workers and Pages using the Vitest pool package.
tags:
    - cloudflare-workers
    - vitest
    - unit-testing
    - integration-testing
    - testing-recipes
    - vitest-pool-workers
category: guide
---

Recipes are examples that help demonstrate how to write unit tests and integration tests for Workers projects using the [`@cloudflare/vitest-pool-workers`](https://www.npmjs.com/package/@cloudflare/vitest-pool-workers) package.

* [Basic unit and integration tests for Workers using `SELF`](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/basics-unit-integration-self)
* [Basic unit and integration tests for Pages Functions using `SELF`](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/pages-functions-unit-integration-self)
* [Basic integration tests using an auxiliary Worker](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/basics-integration-auxiliary)
* [Basic integration test for Workers with static assets](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/workers-assets)
* [Isolated tests using KV, R2 and the Cache API](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/kv-r2-caches)
* [Isolated tests using D1 with migrations](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/d1)
* [Isolated tests using Durable Objects with direct access](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/durable-objects)
* [Isolated tests using Workflows](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/workflows)
* [Tests using Queue producers and consumers](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/queues)
* [Tests using Hyperdrive with a Vitest managed TCP server](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/hyperdrive)
* [Tests using declarative/imperative outbound request mocks](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/request-mocking)
* [Tests using multiple auxiliary Workers and request mocks](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/multiple-workers)
* [Tests importing WebAssembly modules](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/web-assembly)
* [Tests using JSRPC with entrypoints and Durable Objects](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/rpc)
* [Tests using `ctx.exports` to access Worker exports](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/context-exports)
* [Integration test with static assets and Puppeteer](https://github.com/GregBrimble/puppeteer-vitest-workers-assets)
* [Resolving modules with Vite Dependency Pre-Bundling](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/module-resolution)
* [Mocking Workers AI and Vectorize bindings in unit tests](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-pool-workers-examples/ai-vectorize)