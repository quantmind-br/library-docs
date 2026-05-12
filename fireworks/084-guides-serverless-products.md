---
title: Serverless Priority and Turbo - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/serverless-products
source: sitemap
fetched_at: 2026-04-27T20:15:10.187525852-03:00
rendered_js: false
word_count: 163
summary: 'This document explains the two available workload tiers offered by Fireworks.ai: Priority tier for enhanced reliability during peak times and Turbo mode for achieving faster response speeds, both at a higher cost.'
tags:
    - workload-tiers
    - priority-tier
    - turbo-mode
    - reliability
    - speed
    - api-configuration
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks offers a Priority tier for workloads requiring higher reliability, and a Turbo mode for workloads requiring higher speeds.

## Priority tier

Priority tier is for workloads requiring higher reliability during peak traffic, at a higher price. Priority is prioritized above Standard traffic and is less likely to be rate limited.

> [!info]
> Priority tier uses OpenAI-compatible chat completions. The Anthropic `messages` API does not support `service_tier`.

To use priority tier, set `service_tier` to `"priority"`:

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k2p5",
    "service_tier": "priority",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Priority tier is available on select models. Models and pricing are listed on the [Pricing](https://fireworks.ai/pricing#text) page.

## Turbo mode

Turbo mode is a high-speed configuration for interactive applications requiring fast response speeds, at a higher price. It is not a different model — quality remains the same. Turbo mode is available for select models.

| Model | `model` id |
|---|---|
| Kimi K2.6 Turbo | `accounts/fireworks/routers/kimi-k2p6-turbo` |

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k2p6-turbo",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Pricing is listed on the [Pricing](https://fireworks.ai/pricing#text) page.

## See also

- [[009-getting-started-quickstart|Serverless quickstart]]
- [[075-guides-querying-text-models|Text models]]
- [[089-tools-sdks-anthropic-compatibility|Anthropic compatibility]]
