---
title: Billing · Cloudflare D1 docs
url: https://developers.cloudflare.com/d1/observability/billing/index.md
source: llms
fetched_at: 2026-01-24T15:11:57.850229011-03:00
rendered_js: false
word_count: 149
summary: This document explains how to monitor Cloudflare D1 billing metrics, such as rows read and written, through the dashboard and GraphQL API while detailing how to set up usage-based notifications.
tags:
    - cloudflare-d1
    - billing-metrics
    - usage-analytics
    - graphql-api
    - monitoring
    - database-management
category: guide
---

D1 exposes analytics to track billing metrics (rows read, rows written, and total storage) across all databases in your account.

The metrics displayed in the [Cloudflare dashboard](https://dash.cloudflare.com/) are sourced from Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). You can access the metrics [programmatically](https://developers.cloudflare.com/d1/observability/metrics-analytics/#query-via-the-graphql-api) via GraphQL or HTTP client.

## View metrics in the dashboard

Total account billable usage analytics for D1 are available in the Cloudflare dashboard. To view current and past metrics for an account:

1. In the Cloudflare dashboard, go to the **Billing** page.

   [Go to **Billing**](https://dash.cloudflare.com/?to=/:account/billing)

2. Go to **Billable Usage**.

From here you can view charts of your account's D1 usage on a daily or month-to-date timeframe.

Note that billable usage history is stored for a maximum of 30 days.

## Billing Notifications

Usage-based billing notifications are available within the [Cloudflare dashboard](https://dash.cloudflare.com) for users looking to monitor their total account usage.

Notifications on the following metrics are available:

* Rows Read
* Rows Written