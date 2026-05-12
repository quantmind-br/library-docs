---
title: Guides Quotas Usage Rate Limits
url: https://docs.fireworks.ai/guides/quotas_usage/rate-limits
source: sitemap
fetched_at: 2026-04-27T20:18:18.61642325-03:00
rendered_js: false
word_count: 406
summary: This document provides a comprehensive overview of user account quotas and limits, detailing spending tiers, how to manage custom budgets, and the specifics of serverless rate limits and on-demand GPU quotas.
tags:
    - quotas
    - limits
    - spending-tiers
    - rate-limiting
    - budget-control
    - api-usage
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## Spending tiers

Account tier determines the maximum budget you can set:

| Tier | Criteria | Max Monthly Budget |
|------|----------|-------------------|
| Tier 1 | Valid payment method | $50 |
| Tier 2 | Spend or add $50 in credits | $500 |
| Tier 3 | Spend or add $500 in credits | $5,000 |
| Tier 4 | Spend or add $5,000 in credits | $50,000 |
| Unlimited | [Contact us](https://fireworks.ai/company/contact-us) | Unlimited |

## Manage your quotas

### Budget control

Control monthly spending with flexible budget limits. Adjust anytime.

**View current spend limit:**
```bash
firectl quota get monthly-spend-usd
```

**Set a custom monthly budget:**
```bash
firectl quota update monthly-spend-usd --value <AMOUNT>
```

> [!example]
> To set a $200 monthly budget: `firectl quota update monthly-spend-usd --value 200`

### When you reach your budget

All API requests pause automatically across serverless inference, deployments, and fine-tuning. To resume, [add credits](https://fireworks.ai/billing) to increase your tier and set a higher budget.

### On-demand deployment quotas

On-demand deployments have GPU quotas instead of rate limits:

| GPU Type | Default Quota |
|----------|---------------|
| Nvidia A100 | 16 GPUs |
| Nvidia H100 | 16 GPUs |
| Nvidia H200 | 16 GPUs |
| Nvidia B200 | 16 GPUs |
| LoRAs (on-demand) | 100 |

## Serverless rate limits

### Default limits

All accounts with a payment method:

| Limit | Value |
|-------|-------|
| Requests per minute (RPM) | Up to 6,000 (dynamic ceiling) |
| Audio min per minute, Whisper-v3-large | 200 |
| Audio min per minute, Whisper-v3-turbo | 400 |
| Concurrent connections, streaming speech | 10 |
| LoRAs (on-demand) | 100 |

### How rate limiting works

Dynamic rate limits use soft limits that grow with sustained usage:

**Soft limits (starting point):**
- 1 request per second (RPS)
- 1,000 input tokens per second
- 200 output tokens per second

**Above soft limits:**
- Requests can exceed soft limits if there's available bandwidth
- Exceeding soft limits is **not guaranteed** to work
- When bandwidth is constrained, requests above soft limits may be rate limited

**Dynamic growth:**
- Soft limit grows with sustained usage
- Roughly doubles every hour with consistent usage

**Monitoring your limits:**
- `x-ratelimit-limit-requests`: Current minimum limit
- `x-ratelimit-remaining-requests`: Remaining capacity
- `x-ratelimit-over-limit: yes`: Request processed but near capacity

### Account recovery

If suspended due to failed payment:
1. Go to [Billing → Invoices](https://fireworks.ai/billing)
2. Pay outstanding invoices
3. Account reactivates automatically within an hour

#quotas #rate-limiting #budget-control
