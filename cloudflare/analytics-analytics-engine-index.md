---
title: Workers Analytics Engine · Cloudflare Analytics docs
url: https://developers.cloudflare.com/analytics/analytics-engine/index.md
source: llms
fetched_at: 2026-01-24T15:35:14.659943789-03:00
rendered_js: false
word_count: 75
summary: This document introduces Workers Analytics Engine, a service for capturing and querying high-cardinality telemetry data using Workers and SQL APIs.
tags:
    - workers-analytics-engine
    - cloudflare-workers
    - telemetry
    - data-analytics
    - sql-querying
category: concept
---

Workers Analytics Engine provides unlimited-cardinality analytics at scale, via [a built-in API](https://developers.cloudflare.com/analytics/analytics-engine/get-started/) to write data points from Workers, and a [SQL API](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/) to query that data.

You can use Workers Analytics Engine to:

* Expose custom analytics to your own customers
* Build usage-based billing systems
* Understand the health of your service on a per-customer or per-user basis
* Add instrumentation to frequently called code paths, without impacting performance or overwhelming external analytics systems with events

[Get started](https://developers.cloudflare.com/analytics/analytics-engine/get-started/)