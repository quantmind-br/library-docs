---
title: Usage limits | Mistral Docs
url: https://docs.mistral.ai/admin/user-management-finops/usage-limits
source: sitemap
fetched_at: 2026-04-26T04:01:08.685918714-03:00
rendered_js: false
word_count: 162
summary: This document explains how to manage costs and usage by configuring spending caps and monitoring rate limits for workspaces.
tags:
    - cost-management
    - spending-limits
    - usage-tracking
    - rate-limits
    - workspace-administration
    - billing-controls
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Usage Limits

Set spending caps and usage thresholds to control costs across your Organization's Workspaces.

## Spending Limits

Set a monthly spending cap per Workspace to prevent unexpected charges. When a Workspace reaches its limit, API requests are rejected until the next billing period or until you increase the limit.

**To configure:**

1. Open [Admin Workspace settings](https://admin.mistral.ai).
2. Set the **monthly spending limit**.
3. Save your changes.

## Rate Limits

Rate limits are applied at the Workspace level and vary by [usage tier](https://docs.mistral.ai/admin/user-management-finops/tier):

| Limit | Description |
|-------|-------------|
| **Requests per second (RPS)** | Maximum concurrent API requests |
| **Tokens per minute** | Throughput limit for token processing |
| **Tokens per month** | Overall consumption cap |

View current rate limits at [Admin Limits](https://admin.mistral.ai/plateforme/limits).

## Tracking Usage

Track API consumption, token usage, and costs per Workspace from the Admin Panel:

1. From the Workspace settings, click the **Usage** tab.
2. View:
   - Overview of your spending
   - Detailed breakdown by API and services
   - Input and output token costs per model

Use this data alongside spending limits to govern costs across teams and projects.

#cost-management #spending-limits #usage-tracking #rate-limits
