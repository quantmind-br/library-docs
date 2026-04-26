---
title: Rate limits and usage tiers | Mistral Docs
url: https://docs.mistral.ai/admin/user-management-finops/tier
source: sitemap
fetched_at: 2026-04-26T04:01:06.629385564-03:00
rendered_js: false
word_count: 233
summary: This document outlines the rate limiting policy for the Mistral API, explaining the different types of limits enforced and how usage tiers are determined by billing plans.
tags:
    - rate-limits
    - api-usage
    - billing-tiers
    - mistral-api
    - service-limits
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Rate Limits and Usage Tiers

When you use the Mistral API, your requests are subject to rate limits to ensure fair usage and prevent abuse.

Rate limits are set at the **Organization level**, applying across all Workspaces.

Visit [Admin Limits](https://admin.mistral.ai/plateforme/limits) to see current rate limits and usage tier.

## Limit Types

| Limit | Description |
|-------|-------------|
| **Requests per second (RPS)** | Maximum concurrent API requests |
| **Tokens per minute** | Throughput limit for token processing (input + output) |
| **Tokens per month** | Overall consumption cap |

## Usage Tiers

### Experiment Plan (Free)

The free tier is for **evaluation and prototyping only**. Limited rate limits. Upgrade to **Scale** plan to increase limits.

### Scale Plan (Pay-as-you-go)

Gives access to Tier 1 and above. Upgrade in [Admin Subscriptions](https://admin.mistral.ai/organization/billing).

Tier upgrades happen **automatically** based on your cumulative billed amount (total sum of all invoices, not monthly).

## Requesting Higher Limits

To request limits beyond Tier 4:

1. First **reach Tier 4** and **meet the required billing threshold** (>$2,000 / €2,000)
2. Contact [support](https://help.mistral.ai) with:
   - Target requests per second
   - Specific model you plan to use
   - Estimate of tokens required per minute and per month

#rate-limits #api-usage #billing-tiers #mistral-api
