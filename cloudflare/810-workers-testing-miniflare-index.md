---
title: Miniflare · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/testing/miniflare/index.md
source: llms
fetched_at: 2026-01-24T15:29:38.025133206-03:00
rendered_js: false
word_count: 179
summary: This document introduces Miniflare, a TypeScript-based simulator used for local development and testing of Cloudflare Workers in a sandbox environment.
tags:
    - miniflare
    - cloudflare-workers
    - local-development
    - testing
    - worker-simulator
    - typescript
category: concept
---

Warning

This documentation describes the Miniflare API, which is only relevant for advanced use cases. Instead, most users should use [Wrangler](https://developers.cloudflare.com/workers/wrangler) to build, run & deploy their Workers locally

**Miniflare** is a simulator for developing and testing [**Cloudflare Workers**](https://workers.cloudflare.com/). It's written in TypeScript, and runs your code in a sandbox implementing Workers' runtime APIs.

* 🎉 **Fun:** develop Workers easily with detailed logging, file watching and pretty error pages supporting source maps.
* 🔋 **Full-featured:** supports most Workers features, including KV, Durable Objects, WebSockets, modules and more.
* ⚡ **Fully-local:** test and develop Workers without an Internet connection. Reload code on change quickly.

[Get Started](https://developers.cloudflare.com/workers/testing/miniflare/get-started)

[GitHub](https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare)

[NPM](https://npmjs.com/package/miniflare)

***

These docs primarily cover Miniflare specific things. For more information on runtime APIs, refer to the [Cloudflare Workers docs](https://developers.cloudflare.com/workers).

If you find something that doesn't behave as it does in the production Workers environment (and this difference isn't documented), or something's wrong in these docs, please [open a GitHub issue](https://github.com/cloudflare/workers-sdk/issues/new/choose).

* [Get Started](https://developers.cloudflare.com/workers/testing/miniflare/get-started/)
* [Writing tests ](https://developers.cloudflare.com/workers/testing/miniflare/writing-tests/): Write integration tests against Workers using Miniflare.
* [Core](https://developers.cloudflare.com/workers/testing/miniflare/core/)
* [Developing](https://developers.cloudflare.com/workers/testing/miniflare/developing/)
* [Migrations ](https://developers.cloudflare.com/workers/testing/miniflare/migrations/): Review migration guides for specific versions of Miniflare.
* [Storage](https://developers.cloudflare.com/workers/testing/miniflare/storage/)