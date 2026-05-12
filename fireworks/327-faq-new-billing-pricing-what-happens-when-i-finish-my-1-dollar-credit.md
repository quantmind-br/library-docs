---
title: How do credits work?
url: https://docs.fireworks.ai/faq-new/billing-pricing/what-happens-when-i-finish-my-1-dollar-credit
source: sitemap
fetched_at: 2026-04-27T20:13:15.580735202-03:00
rendered_js: false
word_count: 263
summary: Postpaid billing system where prepaid credits are applied first, then usage charges accrue and are billed monthly. Account suspension rules differ based on whether a payment method is on file.
tags:
    - billing
    - credits
    - account-management
    - postpaid
category: faq
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## How credits are applied

Fireworks uses a **postpaid billing** system:

- **Prepaid credits are used first** for all usage
- Once credits are exhausted, **usage charges accrue** at your rate plan pricing
- **Charges are billed at month-end**
- Prepaid credits are **instantly applied** to any outstanding balance

> [!example]
> If you had a `$750` outstanding bill and added `$500` in credits, your bill reduces to `$250`. The remaining credit is `$0` — credits are consumed by existing charges first.

## Missing credits after purchase?

1. Visit your **billing dashboard**
2. Check the **"Credits"** section and **current outstanding balance**
3. Credits are always applied to existing balances before being available for new usage

## Why did I receive an invoice after depositing credits?

You receive an invoice for usage **exceeding your pre-purchased credits** (automatically, regardless of subscription status).

> [!example]
> Deposited `$20` in credits but incurred `$83` in usage → billed `$63` at month-end.

## What happens when my $1 credit runs out?

| Account state | Behavior |
|---|---|
| **No payment method** | Account suspended. Provisional rate limit of **10 RPM**. Add payment method to restore service. |
| **Payment method on file** | Service continues. Billed at month-end up to your configured spend limit (default $50/month for new accounts). |

**To access full rate limits (up to 6,000 RPM)** → add a payment method in [billing settings](https://fireworks.ai/billing).

## Receipts for purchased credits

Receipts are sent via **Stripe** upon purchase. Check your email for a Stripe receipt (not from Fireworks). If missing, contact `community_billing@fireworks.ai`.

#billing #credits #account-management #postpaid