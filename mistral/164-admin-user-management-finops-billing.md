---
title: Billing | Mistral Docs
url: https://docs.mistral.ai/admin/user-management-finops/billing
source: sitemap
fetched_at: 2026-04-26T04:01:03.293618806-03:00
rendered_js: false
word_count: 181
summary: This document outlines how to manage billing information, payment methods, and invoices for an organization, as well as how billing is structured for subscriptions and API usage.
tags:
    - billing-management
    - invoice-tracking
    - payment-methods
    - organization-settings
    - api-usage-billing
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Billing

View and manage payment methods, invoices, and billing information for your Organization.

Requires the **Admin** or **Billing** role.

## Setting Up Billing

1. Open [Admin Subscriptions Billing](https://admin.mistral.ai/organization/billing).
2. Add a payment method (credit card or Google Pay).
3. Enter billing details: individual or company name, address, and VAT number if applicable.

> [!info]
> You need billing set up to activate API keys beyond the free tier and subscribe to Pro, Team, or Enterprise plans.

## Invoices

View and download invoices from the billing section. Invoices include:
- Subscription charges
- API usage charges (pay-as-you-go)
- Seat allocations

## Billing Structure

| Type | Description |
|------|-------------|
| **Le Chat subscriptions** (Pro, Team, Enterprise) | Billed at start of each billing period (monthly or annual). Fixed-price plans. |
| **API usage** (Scale plan) | Pay-as-you-go based on tokens processed. No upfront cost. |
| **Plan upgrades** | Payment due immediately for the new plan. |

Billing is managed at the Organization level. All Workspace API usage within your Organization is consolidated into a single bill. Use [usage limits](https://docs.mistral.ai/admin/user-management-finops/usage-limits) to set spending caps per Workspace.

#billing-management #invoice-tracking #payment-methods #api-usage-billing
