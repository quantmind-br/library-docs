---
title: Limits · Cloudflare Workers KV docs
url: https://developers.cloudflare.com/kv/platform/limits/index.md
source: llms
fetched_at: 2026-01-24T15:16:34.885148661-03:00
rendered_js: false
word_count: 262
summary: This document outlines the usage limits, storage capacities, and operational constraints for Cloudflare Workers KV across Free and Paid plans.
tags:
    - cloudflare-workers-kv
    - usage-limits
    - quotas
    - storage-specifications
    - pricing-plans
category: reference
---

| Feature | Free | Paid |
| - | - | - |
| Reads | 100,000 reads per day | Unlimited |
| Writes to different keys | 1,000 writes per day | Unlimited |
| Writes to same key | 1 per second | 1 per second |
| Operations/Worker invocation [1](#user-content-fn-1) | 1000 | 1000 |
| Namespaces | 1000 | 1000 |
| Storage/account | 1 GB | Unlimited |
| Storage/namespace | 1 GB | Unlimited |
| Keys/namespace | Unlimited | Unlimited |
| Key size | 512 bytes | 512 bytes |
| Key metadata | 1024 bytes | 1024 bytes |
| Value size | 25 MiB | 25 MiB |
| Minimum [`cacheTtl`](https://developers.cloudflare.com/kv/api/read-key-value-pairs/#cachettl-parameter) [2](#user-content-fn-2) | 60 seconds | 60 seconds |

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form](https://forms.gle/ukpeZVLWLnKeixDu7). If the limit can be increased, Cloudflare will contact you with next steps.

Free versus Paid plan pricing

Refer to [KV pricing](https://developers.cloudflare.com/kv/platform/pricing/) to review the specific KV operations you are allowed under each plan with their pricing.

Workers KV REST API limits

Using the REST API to access Cloudflare Workers KV is subject to the [rate limits that apply to all operations of the Cloudflare REST API](https://developers.cloudflare.com/fundamentals/api/reference/limits).

## Footnotes

1. Within a single invocation, a Worker can make up to 1,000 operations to external services (for example, 500 Workers KV reads and 500 R2 reads). A bulk request to Workers KV counts for 1 request to an external service. [↩](#user-content-fnref-1)

2. The maximum value is [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER). [↩](#user-content-fnref-2)