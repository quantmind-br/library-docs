---
title: Reserved capacity - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/reservations
source: sitemap
fetched_at: 2026-04-27T20:13:21.957894995-03:00
rendered_js: false
word_count: 143
summary: This document explains the benefits and mechanics of purchasing reserved capacity for enterprise accounts on Fireworks AI, detailing how consumption works, billing processes, and how to manage or acquire these commitments.
tags:
    - reserved-capacity
    - enterprise-accounts
    - gpu-hours
    - billing-process
    - usage-management
    - purchasing
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Enterprise accounts can purchase reserved capacity (typically 1-year commitments). Reservations provide:

- Guaranteed capacity
- Higher quotas
- Lower GPU-hour prices
- Pre-GA access to newer regions and newest hardware

## Usage and Billing

Consume a reservation by creating a deployment meeting the reservation parameters. Example: a reservation for 12 H100 GPUs with two deployments using 8 H100 GPUs each—both deployments running means 12 H100s count toward reservation, and the excess 4 H100s are billed at on-demand rates.

Follow [[070-guides-ondemand-deployments|deploying models on-demand]] to create a deployment.

> [!warning]
> When a reservation approaches its end time, renew or scale down deployments to avoid billing at on-demand rates.

Reservations are invoiced separately from on-demand usage (frequency determined by contract).

## Purchasing or Renewing

Contact your Fireworks account manager to purchase, increase, or renew reservations. Prospective customers: reach out to [sales team](https://fireworks.ai/company/contact-us).

## Viewing Reservations

```bash
firectl reservation list
```
