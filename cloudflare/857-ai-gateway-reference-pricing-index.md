---
title: Pricing · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/reference/pricing/index.md
source: llms
fetched_at: 2026-01-24T15:07:46.400654905-03:00
rendered_js: false
word_count: 248
summary: This document outlines the pricing structure and plan-specific features for Cloudflare's AI Gateway, including core feature availability, logging limits, and Logpush costs.
tags:
    - ai-gateway
    - pricing
    - billing
    - logging
    - logpush
    - cloudflare-workers
category: reference
---

AI Gateway is available to use on all plans.

AI Gateway's core features available today are offered for free, and all it takes is a Cloudflare account and one line of code to [get started](https://developers.cloudflare.com/ai-gateway/get-started/). Core features include: dashboard analytics, caching, and rate limiting.

We will continue to build and expand AI Gateway. Some new features may be additional core features that will be free while others may be part of a premium plan. We will announce these as they become available.

You can monitor your usage in the AI Gateway dashboard.

## Persistent logs

Persistent logs are available on all plans, with a free allocation for both free and paid plans. Charges for additional logs beyond those limits are based on the number of logs stored per month.

### Free allocation and overage pricing

| Plan | Free logs stored | Overage pricing |
| - | - | - |
| Workers Free | 100,000 logs total | N/A - Upgrade to Workers Paid |
| Workers Paid | 1,000,000 logs total | N/A |

Allocations are based on the total logs stored across all gateways. For guidance on managing or deleting logs, please see our [documentation](https://developers.cloudflare.com/ai-gateway/observability/logging).

## Logpush

Logpush is only available on the Workers Paid plan.

| | Paid plan |
| - | - |
| Requests | 10 million / month, +$0.05/million |

## Fine print

Prices subject to change. If you are an Enterprise customer, reach out to your account team to confirm pricing details.