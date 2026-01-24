---
title: DevTools · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/observability/dev-tools/index.md
source: llms
fetched_at: 2026-01-24T15:29:17.200683939-03:00
rendered_js: false
word_count: 157
summary: This document explains how to access and use Chrome DevTools for debugging, profiling, and monitoring Cloudflare Workers during local development or within the dashboard environment.
tags:
    - cloudflare-workers
    - chrome-devtools
    - wrangler
    - debugging
    - local-development
    - performance-profiling
    - vite
category: guide
---

## Using DevTools

When running your Worker locally using the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) (`wrangler dev`) or using [Vite](https://vite.dev/) with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), you automatically have access to [Cloudflare's implementation](https://github.com/cloudflare/workers-sdk/tree/main/packages/chrome-devtools-patches) of [Chrome DevTools](https://developer.chrome.com/docs/devtools/overview).

You can use Chrome DevTools to:

* View logs directly in the Chrome console
* [Debug code by setting breakpoints](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/)
* [Profile CPU usage](https://developers.cloudflare.com/workers/observability/dev-tools/cpu-usage/)
* [Observe memory usage and debug memory leaks in your code that can cause out-of-memory (OOM) errors](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/)

## Opening DevTools

### Wrangler

* Run your Worker locally, by running `wrangler dev`
* Press the `D` key from your terminal to open DevTools in a browser tab

### Vite

* Run your Worker locally by running `vite`
* In a new Chrome tab, open the debug URL that shows in your console (for example, `http://localhost:5173/__debug`)

### Dashboard editor & playground

Both the [Cloudflare dashboard](https://dash.cloudflare.com/) and the [Worker's Playground](https://workers.cloudflare.com/playground) include DevTools in the UI.

## Related resources

* [Local development](https://developers.cloudflare.com/workers/development-testing/) - Develop your Workers and connected resources locally via Wrangler and workerd, for a fast, accurate feedback loop.