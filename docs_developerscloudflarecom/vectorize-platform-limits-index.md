---
title: Limits · Cloudflare Vectorize docs
url: https://developers.cloudflare.com/vectorize/platform/limits/index.md
source: llms
fetched_at: 2026-01-24T15:24:34.037312626-03:00
rendered_js: false
word_count: 338
summary: This document provides the operational limits and technical specifications for Cloudflare Vectorize, including constraints on indexes, vectors, and metadata.
tags:
    - cloudflare-vectorize
    - service-limits
    - vector-database
    - index-configuration
    - quota-management
category: reference
---

The following limits apply to accounts, indexes and vectors (as specified):

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form](https://forms.gle/nyamy2SM9zwWTXKE6). If the limit can be increased, Cloudflare will contact you with next steps.

| Feature | Current Limit |
| - | - |
| Indexes per account | 50,000 (Workers Paid) / 100 (Free) |
| Maximum dimensions per vector | 1536 dimensions, 32 bits precision |
| Precision per vector dimension | 32 bits (float32) |
| Maximum vector ID length | 64 bytes |
| Metadata per vector | 10KiB |
| Maximum returned results (`topK`) with values or metadata | 20 |
| Maximum returned results (`topK`) without values and metadata | 100 |
| Maximum upsert batch size (per batch) | 1000 (Workers) / 5000 (HTTP API) |
| Maximum vectors in a list-vectors page | 1000 |
| Maximum index name length | 64 bytes |
| Maximum vectors per index | 10,000,000 |
| Maximum namespaces per index | 50,000 (Workers Paid) / 1000 (Free) |
| Maximum namespace name length | 64 bytes |
| Maximum vectors upload size | 100 MB |
| Maximum metadata indexes per Vectorize index | 10 |
| Maximum indexed data per metadata index per vector | 64 bytes |

## Limits V1 (deprecated)

The following limits apply to accounts, indexes and vectors (as specified):

| Feature | Current Limit |
| - | - |
| Indexes per account | 100 indexes |
| Maximum dimensions per vector | 1536 dimensions |
| Maximum vector ID length | 64 bytes |
| Metadata per vector | 10KiB |
| Maximum returned results (`topK`) | 20 |
| Maximum upsert batch size (per batch) | 1000 (Workers) / 5000 (HTTP API) |
| Maximum index name length | 63 bytes |
| Maximum vectors per index | 200,000 |
| Maximum namespaces per index | 1000 namespaces |
| Maximum namespace name length | 63 bytes |