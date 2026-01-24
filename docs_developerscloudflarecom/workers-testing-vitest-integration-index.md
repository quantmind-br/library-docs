---
title: Vitest integration · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/testing/vitest-integration/index.md
source: llms
fetched_at: 2026-01-24T15:29:41.865651145-03:00
rendered_js: false
word_count: 110
summary: This document introduces the Workers Vitest integration for testing Cloudflare Workers and Pages Functions, explaining how it allows tests to run directly within the Workers runtime.
tags:
    - cloudflare-workers
    - vitest
    - unit-testing
    - integration-testing
    - miniflare
    - javascript-testing
category: guide
---

For most users, Cloudflare recommends using the Workers Vitest integration for testing Workers and [Pages Functions](https://developers.cloudflare.com/pages/functions/) projects. [Vitest](https://vitest.dev/) is a popular JavaScript testing framework featuring a very fast watch mode, Jest compatibility, and out-of-the-box support for TypeScript. In this integration, Cloudflare provides a custom pool that allows your Vitest tests to run *inside* the Workers runtime.

The Workers Vitest integration:

* Supports both **unit tests** and **integration tests**.
* Provides direct access to Workers runtime APIs and bindings.
* Implements isolated per-test storage.
* Runs tests fully-locally using [Miniflare](https://miniflare.dev/).
* Leverages Vitest's hot-module reloading for near instant reruns.
* Provides a declarative interface for mocking outbound requests.
* Supports projects with multiple Workers.

[Write your first test](https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/)