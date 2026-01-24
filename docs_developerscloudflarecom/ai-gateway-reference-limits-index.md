---
title: Limits · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/reference/limits/index.md
source: llms
fetched_at: 2026-01-24T15:07:44.890561202-03:00
rendered_js: false
word_count: 281
summary: This document outlines the technical limits and quotas for Cloudflare AI Gateway features, including caching, log storage, and gateway configurations across free and paid plans.
tags:
    - ai-gateway
    - cloudflare
    - limits
    - quotas
    - logging
    - caching
    - rate-limits
category: reference
---

The following limits apply to gateway configurations, logs, and related features in Cloudflare's platform.

| Feature | Limit |
| - | - |
| [Cacheable request size](https://developers.cloudflare.com/ai-gateway/features/caching/) | 25 MB per request |
| [Cache TTL](https://developers.cloudflare.com/ai-gateway/features/caching/#cache-ttl-cf-aig-cache-ttl) | 1 month |
| [Custom metadata](https://developers.cloudflare.com/ai-gateway/observability/custom-metadata/) | 5 entries per request |
| [Datasets](https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/) | 10 per gateway |
| Gateways free plan | 10 per account |
| Gateways paid plan | 20 per account |
| Gateway name length | 64 characters |
| Log storage rate limit | 500 logs per second per gateway |
| Logs stored [paid plan](https://developers.cloudflare.com/ai-gateway/reference/pricing/) | 10 million per gateway 1 |
| Logs stored [free plan](https://developers.cloudflare.com/ai-gateway/reference/pricing/) | 100,000 per account 2 |
| [Log size stored](https://developers.cloudflare.com/ai-gateway/observability/logging/) | 10 MB per log 3 |
| [Logpush jobs](https://developers.cloudflare.com/ai-gateway/observability/logging/logpush/) | 4 per account |
| [Logpush size limit](https://developers.cloudflare.com/ai-gateway/observability/logging/logpush/) | 1MB per log |

1 If you have reached 10 million logs stored per gateway, new logs will stop being saved. To continue saving logs, you must delete older logs in that gateway to free up space or create a new gateway. Refer to [Auto Log Cleanup](https://developers.cloudflare.com/ai-gateway/observability/logging/#auto-log-cleanup) for more details on how to automatically delete logs.

2 If you have reached 100,000 logs stored per account, across all gateways, new logs will stop being saved. To continue saving logs, you must delete older logs. Refer to [Auto Log Cleanup](https://developers.cloudflare.com/ai-gateway/observability/logging/#auto-log-cleanup) for more details on how to automatically delete logs.

3 Logs larger than 10 MB will not be stored.

Need a higher limit?

To request an increase to a limit, complete the [Limit Increase Request Form](https://forms.gle/cuXu1QnQCrSNkkaS8). If the limit can be increased, Cloudflare will contact you with next steps.