---
title: Add-on Credits | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/plans-and-billing/add-on-credits
source: sitemap
fetched_at: 2026-04-29T15:05:47.922838834-03:00
rendered_js: false
word_count: 560
summary: This document explains how Warp's Add-on credits system functions, including purchasing options, auto-reload settings, team usage policies, and spend management.
tags:
    - billing-management
    - ai-usage
    - subscription-credits
    - team-administration
    - account-settings
    - spending-limits
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Add-on credits let you continue using premium AI models after reaching monthly plan quotas, at lower rates with more spending control.

> [!warning]
> Legacy plans (Pro, Turbo, Lightspeed) do not support Add-on Credits. Upgrade to Build plan or see [Overages (Legacy)](https://docs.warp.dev/support-and-community/plans-and-billing/overages-legacy) for additional options.

Manage and purchase Add-on credits in **Settings > Billing and usage**.

## How Add-on credits work

Add-on credits extend AI usage beyond your monthly quota. Once plan credits are used, Warp automatically draws from available Add-on credits.

If **Auto reload** is enabled, new credits are added automatically based on your configured monthly limit and purchase amount.

Add-on credits are available for Build, Business, and Enterprise plans. They **roll over across billing cycles** and remain valid for **12 months from purchase**.

## Purchasing Add-on credits

### 1. Buy on-demand

Purchase additional credits anytime in **Settings > Billing and usage**. Buying larger denominations upfront provides larger discounts.

| Credits | Price | Discount |
|---------|-------|----------|
| 400 | $10 | 0% |
| 1,000 | $20 | 20% |
| 3,000 | $50 | 33% |
| 6,500 | $100 | 40% |

### 2. Enable auto-reload

Auto reload purchases more credits when your balance reaches **100 credits**, ensuring uninterrupted AI access.

By default, **Auto reload is disabled for new subscribers**. When enabled, it starts with a **$200 monthly spend limit**, adjustable anytime.

> [!info]
> Opt in when subscribing at [app.warp.dev/upgrade](https://app.warp.dev/upgrade) or change anytime in **Settings > Billing and usage**.

## Configuring a monthly spend limit

Sets the maximum spent on Add-on credits per calendar month.

- Default limit is $200, adjustable in **Settings > Billing and usage**.
- If a purchase would exceed your limit, it **won't process** — raise the limit or choose a smaller amount.
- Once reached, no additional purchases occur until the next calendar month or you update the limit.

> [!note]
> Monthly spend limit resets at the start of each calendar month, separate from your billing cycle.

## Billing and credit usage

When your balance renews:

1. Warp first consumes your included monthly plan credits.
2. After those are used, Warp draws from available Add-on Credits.
3. If Add-on Credits run out and Auto reload is enabled, Warp purchases more up to your monthly limit.

Track remaining credits and spending in the credits transparency footer and **Settings > Billing and usage**.

### Teams using Add-on Credits

For Build or Business teams, **Add-on Credits are shared across all members**. Team admins manage:

- Enabling or disabling Auto reload
- Adjusting monthly spend limits
- Choosing Add-on credit increments
- Viewing usage and spending breakdowns

Each user has their own monthly credit limit, but usage beyond that quota draws from shared team credits.

**Example:** If your plan includes 1,500 credits per team member:
- User A reaches their 1,500 limit → further usage draws from shared Add-on Credits
- User B has only used 200 credits → their quota is unaffected

## Plan changes and cancellations

- Purchased Add-on Credits remain valid for **12 months after purchase** with an active subscription.
- Moving to Free plan loses access to Add-on Credits. Cannot purchase more until resubscribed.
- All unused Add-on Credits remain valid as long as you have an active subscription.

## Related

- [[290-support-and-community-plans-and-billing-bring-your-own-api-key]] - Route requests through your own API keys
- [[281-enterprise-support-and-resources-billing]] - Enterprise billing and spending controls
