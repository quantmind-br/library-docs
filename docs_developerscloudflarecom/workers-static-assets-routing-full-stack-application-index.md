---
title: Full-stack application · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/static-assets/routing/full-stack-application/index.md
source: llms
fetched_at: 2026-01-24T15:31:09.106587456-03:00
rendered_js: false
word_count: 94
summary: This document defines full-stack applications on Cloudflare Workers and provides a list of supported web frameworks for server-side rendering and client-side hydration.
tags:
    - full-stack
    - cloudflare-workers
    - ssr
    - web-frameworks
    - server-side-rendering
    - hydration
category: concept
---

Full-stack applications are web applications which are span both the client and server. The build process of these applications will produce a HTML files, accompanying client-side resources (e.g. JavaScript bundles, CSS stylesheets, images, fonts, etc.) and a Worker script. Data is typically fetched the Worker script at request-time and the initial page response is usually server-side rendered (SSR). From there, the client is then hydrated and a SPA-like experience ensues.

The following full-stack frameworks are natively supported by Workers:

* [Astro](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/)
* [React Router (formerly Remix)](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/)
* [Next.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/)
* [RedwoodSDK](https://developers.cloudflare.com/workers/framework-guides/web-apps/redwoodsdk/)
* [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/)

- [Analog](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/)
- [Angular](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/angular/)
- [Nuxt](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/nuxt/)
- [Qwik](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/qwik/)
- [Solid](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/solid/)
- [Waku](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/waku/)