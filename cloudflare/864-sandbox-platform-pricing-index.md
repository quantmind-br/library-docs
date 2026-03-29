---
title: Pricing · Cloudflare Sandbox SDK docs
url: https://developers.cloudflare.com/sandbox/platform/pricing/index.md
source: llms
fetched_at: 2026-01-24T15:23:00.401524866-03:00
rendered_js: false
word_count: 69
summary: This document explains the pricing model for the Sandbox SDK, which is based on the Cloudflare Containers platform and additional usage of Workers and Durable Objects.
tags:
    - sandbox-sdk
    - pricing
    - billing
    - containers
    - cloudflare-workers
    - durable-objects
category: reference
---

Sandbox SDK pricing is determined by the underlying [Containers](https://developers.cloudflare.com/containers/) platform it's built on.

## Containers Pricing

Refer to [Containers pricing](https://developers.cloudflare.com/containers/pricing/) for complete details on:

* vCPU, memory, and disk usage rates
* Network egress pricing
* Instance types and their costs

## Related Pricing

When using Sandbox, you'll also be billed for:

* [Workers](https://developers.cloudflare.com/workers/platform/pricing/) - Handles incoming requests to your sandbox
* [Durable Objects](https://developers.cloudflare.com/durable-objects/platform/pricing/) - Powers each sandbox instance
* [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#pricing) - Optional observability (if enabled)