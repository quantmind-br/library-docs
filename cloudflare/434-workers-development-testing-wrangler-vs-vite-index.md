---
title: Choosing between Wrangler & Vite · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/development-testing/wrangler-vs-vite/index.md
source: llms
fetched_at: 2026-01-24T15:25:24.147310185-03:00
rendered_js: false
word_count: 224
summary: This document provides criteria and comparison points to help developers choose between using Wrangler or the Cloudflare Vite plugin based on their project's architectural focus and development needs.
tags:
    - cloudflare-workers
    - wrangler
    - vite-plugin
    - developer-tools
    - frontend-frameworks
    - serverless-functions
category: guide
---

# When to use Wrangler vs Vite

Deciding between Wrangler and the Cloudflare Vite plugin depends on your project's focus and development workflow. Here are some quick guidelines to help you choose:

## When to use Wrangler

* **Backend & Workers-focused:** If you're primarily building APIs, serverless functions, or background tasks, use Wrangler.

* **Remote development:** If your project needs the ability to run your worker remotely on Cloudflare's network, use Wrangler's `--remote` flag.

* **Simple frontends:** If you have minimal frontend requirements and don’t need hot reloading or advanced bundling, Wrangler may be sufficient.

## When to use the Cloudflare Vite Plugin

Use the [Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) for:

* **Frontend-centric development:** If you already use Vite with modern frontend frameworks like React, Vue, Svelte, or Solid, the Vite plugin integrates into your development workflow.

* **React Router v7:** If you are using [React Router v7](https://reactrouter.com/) (the successor to Remix), it is officially supported by the Vite plugin as a full-stack SSR framework.

* **Rapid iteration (HMR):** If you need near-instant updates in the browser, the Vite plugin provides [Hot Module Replacement (HMR)](https://vite.dev/guide/features.html#hot-module-replacement) during local development.

* **Advanced optimizations:** If you require more advanced optimizations (code splitting, efficient bundling, CSS handling, build time transformations, etc.), Vite is a strong fit.

* **Greater flexibility:** Due to Vite's advanced configuration options and large ecosystem of plugins, there is more flexibility to customize your development experience and build output.