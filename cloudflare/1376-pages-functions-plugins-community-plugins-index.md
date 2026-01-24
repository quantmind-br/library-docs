---
title: Community Plugins · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/plugins/community-plugins/index.md
source: llms
fetched_at: 2026-01-24T15:18:51.040742017-03:00
rendered_js: false
word_count: 187
summary: This document lists community-maintained plugins for Cloudflare Pages, providing a directory of extensions for asset management, proxying, error logging, and framework integration.
tags:
    - cloudflare-pages
    - pages-plugins
    - community-contributions
    - middleware
    - developer-tools
category: reference
---

The following are some of the community-maintained Pages Plugins. If you have created a Pages Plugin and would like to share it with developers, create a PR to add it to this alphabeticallly-ordered list using the link in the footer.

* [pages-plugin-asset-negotiation](https://github.com/Cherry/pages-plugin-asset-negotiation)

  Given a folder of assets in multiple formats, this Plugin will automatically negotiate with a client to serve an optimized version of a requested asset.

* [proxyflare-for-pages](https://github.com/flaregun-net/proxyflare-for-pages)

  Move traffic around your Cloudflare Pages domain with ease. Proxyflare is a reverse-proxy that enables you to:

  * Port forward, redirect, and reroute HTTP and websocket traffic anywhere on the Internet.
  * Mount an entire website on a subpath (for example, `mysite.com/docs`) on your apex domain.
  * Serve static text (like `robots.txt` and other structured metadata) from any endpoint.

  Refer to [Proxyflare](https://proxyflare.works) for more information.

* [cloudflare-pages-plugin-rollbar](https://github.com/hckr-studio/cloudflare-pages-plugin-rollbar)

  The [Rollbar](https://rollbar.com/) Pages Plugin captures and logs all exceptions which occur below it in the execution chain of your [Pages Functions](https://developers.cloudflare.com/pages/functions/). Discover, predict, and resolve errors in real-time.

* [cloudflare-pages-plugin-trpc](https://github.com/toyamarinyon/cloudflare-pages-plugin-trpc)

  Allows developers to quickly create a tRPC server with a Cloudflare Pages Function.

* [pages-plugin-twind](https://github.com/helloimalastair/twind-plugin)

  Automatically injects Tailwind CSS styles into HTML pages after analyzing which classes are used.