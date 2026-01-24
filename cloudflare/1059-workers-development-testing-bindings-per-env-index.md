---
title: Supported bindings per development mode · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/development-testing/bindings-per-env/index.md
source: llms
fetched_at: 2026-01-24T15:25:16.372218309-03:00
rendered_js: false
word_count: 386
summary: This document explains the differences between local and remote development environments for Cloudflare Workers, detailing binding support for simulations and remote connections.
tags:
    - cloudflare-workers
    - wrangler-dev
    - local-development
    - remote-development
    - resource-bindings
    - worker-simulation
category: reference
---

## Local development

**Local simulations**: During local development, your Worker code always executes locally and bindings connect to locally simulated resources [by default](https://developers.cloudflare.com/workers/development-testing/#remote-bindings). This is supported in [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/#dev) and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

**Remote binding connections:**: Allows you to connect to remote resources on a [per-binding basis](https://developers.cloudflare.com/workers/development-testing/#remote-bindings). This is supported in [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/#dev) and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

| Binding | Local simulations | Remote binding connections |
| - | - | - |
| **AI** | ❌ | ✅ |
| **Assets** | ✅ | ❌ |
| **Analytics Engine** | ✅ | ❌ |
| **Browser Rendering** | ✅ | ✅ |
| **D1** | ✅ | ✅ |
| **Durable Objects** | ✅ | ❌ [1](#user-content-fn-1) |
| **Containers** | ✅ | ❌ |
| **Email Bindings** | ✅ | ✅ |
| **Hyperdrive** | ✅ | ❌ |
| **Images** | ✅ | ✅ |
| **KV** | ✅ | ✅ |
| **mTLS** | ❌ | ✅ |
| **Queues** | ✅ | ✅ |
| **R2** | ✅ | ✅ |
| **Rate Limiting** | ✅ | ❌ |
| **Service Bindings (multiple Workers)** | ✅ | ✅ |
| **Vectorize** | ❌ | ✅ |
| **Workflows** | ✅ | ❌ |

## Remote development

During remote development, all of your Worker code is uploaded and executed on Cloudflare's infrastructure, and bindings always connect to remote resources. **We recommend using local development with remote binding connections instead** for faster iteration and debugging.

Supported only in [`wrangler dev --remote`](https://developers.cloudflare.com/workers/wrangler/commands/#dev) - there is **no Vite plugin equivalent**.

| Binding | Remote development |
| - | - |
| **AI** | ✅ |
| **Assets** | ✅ |
| **Analytics Engine** | ✅ |
| **Browser Rendering** | ✅ |
| **D1** | ✅ |
| **Durable Objects** | ✅ |
| **Containers** | ❌ |
| **Email Bindings** | ✅ |
| **Hyperdrive** | ✅ |
| **Images** | ✅ |
| **KV** | ✅ |
| **mTLS** | ✅ |
| **Queues** | ❌ |
| **R2** | ✅ |
| **Rate Limiting** | ✅ |
| **Service Bindings (multiple Workers)** | ✅ |
| **Vectorize** | ✅ |
| **Workflows** | ❌ |

## Footnotes

1. Refer to [Using remote resources with Durable Objects and Workflows](https://developers.cloudflare.com/workers/development-testing/#using-remote-resources-with-durable-objects-and-workflows) for recommended workarounds. [↩](#user-content-fnref-1)