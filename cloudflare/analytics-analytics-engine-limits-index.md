---
title: Workers Analytics Engine — Limits · Cloudflare Analytics docs
url: https://developers.cloudflare.com/analytics/analytics-engine/limits/index.md
source: llms
fetched_at: 2026-01-24T15:35:15.555858209-03:00
rendered_js: false
word_count: 134
summary: This document outlines the technical limits and data retention policies for Workers Analytics Engine, including data point constraints and storage duration.
tags:
    - workers-analytics-engine
    - limits
    - data-retention
    - cloudflare-workers
    - quotas
category: reference
---

The following limits apply to Workers Analytics Engine:

* Analytics Engine will accept up to twenty blobs, twenty doubles, and one index per call to `writeDataPoint`.
* The total size of all blobs in a request must not exceed **16 KB**. The 16 KB size limit for the blobs field applies to **each individual data point**, regardless of how many are included in a single request using writeDataPoints().
* Each index must not be more than 96 bytes.
* You can write a maximum of 250 data points per Worker invocation (client HTTP request). Each call to `writeDataPoint` counts towards this limit.

## Data retention

Data written to Workers Analytics Engine is stored for three months.

Interested in longer retention periods? Join the `#analytics-engine` channel in the [Cloudflare Developers Discord](https://discord.cloudflare.com/) and tell us more about what you are building.