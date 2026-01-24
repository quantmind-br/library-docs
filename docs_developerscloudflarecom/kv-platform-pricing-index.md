---
title: Pricing · Cloudflare Workers KV docs
url: https://developers.cloudflare.com/kv/platform/pricing/index.md
source: llms
fetched_at: 2026-01-24T15:16:36.231454332-03:00
rendered_js: false
word_count: 270
summary: This document outlines the pricing structure and usage limits for Workers KV across Free and Paid plans, including details on billable operations and data storage.
tags:
    - workers-kv
    - pricing
    - billing
    - usage-limits
    - cloudflare-workers
category: reference
---

Workers KV is included in both the Free and Paid [Workers plans](https://developers.cloudflare.com/workers/platform/pricing/).

| | Free plan1 | Paid plan |
| - | - | - |
| Keys read | 100,000 / day | 10 million/month, + $0.50/million |
| Keys written | 1,000 / day | 1 million/month, + $5.00/million |
| Keys deleted | 1,000 / day | 1 million/month, + $5.00/million |
| List requests | 1,000 / day | 1 million/month, + $5.00/million |
| Stored data | 1 GB | 1 GB, + $0.50/ GB-month |

1 The Workers Free plan includes limited Workers KV usage. All limits reset daily at 00:00 UTC. If you exceed any one of these limits, further operations of that type will fail with an error.

Note

Workers KV pricing for read, write and delete operations is on a per-key basis. Bulk read operations are billed by the amount of keys read in a bulk read operation.

## Pricing FAQ

### When writing via KV's [REST API](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update/), how are writes charged?

Each key-value pair in the `PUT` request is counted as a single write, identical to how each call to `PUT` in the Workers API counts as a write. Writing 5,000 keys via the REST API incurs the same write costs as making 5,000 `PUT` calls in a Worker.

### Do queries I issue from the dashboard or wrangler (the CLI) count as billable usage?

Yes, any operations via the Cloudflare dashboard or wrangler, including updating (writing) keys, deleting keys, and listing the keys in a namespace count as billable KV usage.

### Does Workers KV charge for data transfer / egress?

No.