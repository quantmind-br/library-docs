---
title: Protocols · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/reference/protocols/index.md
source: llms
fetched_at: 2026-01-24T15:26:53.517258683-03:00
rendered_js: false
word_count: 135
summary: This document lists the supported network protocols and communication interfaces for inbound and outbound traffic within Cloudflare Workers.
tags:
    - cloudflare-workers
    - protocols
    - networking
    - http
    - websockets
    - tcp-sockets
    - smtp
category: reference
---

Cloudflare Workers support the following protocols and interfaces:

| Protocol | Inbound | Outbound |
| - | - | - |
| **HTTP / HTTPS** | Handle incoming HTTP requests using the [`fetch()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/) | Make HTTP subrequests using the [`fetch()` API](https://developers.cloudflare.com/workers/runtime-apis/fetch/) |
| **Direct TCP sockets** | Support for handling inbound TCP connections is [coming soon](https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/) | Create outbound TCP connections using the [`connect()` API](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) |
| **WebSockets** | Accept incoming WebSocket connections using the [`WebSocket` API](https://developers.cloudflare.com/workers/runtime-apis/websockets/) | |
| **HTTP/3 (QUIC)** | Accept inbound requests over [HTTP/3](https://www.cloudflare.com/learning/performance/what-is-http3/) by enabling it on your [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) in **Speed** > **Settings** > **Protocol Optimization** area of the [Cloudflare dashboard](https://dash.cloudflare.com/). | |
| **SMTP** | Use [Email Workers](https://developers.cloudflare.com/email-routing/email-workers/) to process and forward email, without having to manage TCP connections to SMTP email servers | [Email Workers](https://developers.cloudflare.com/email-routing/email-workers/) |