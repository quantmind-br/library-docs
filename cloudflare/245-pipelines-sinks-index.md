---
title: Sinks · Cloudflare Pipelines Docs
url: https://developers.cloudflare.com/pipelines/sinks/index.md
source: llms
fetched_at: 2026-01-24T15:19:22.543821017-03:00
rendered_js: false
word_count: 88
summary: This document explains the role and functionality of sinks in Cloudflare Pipelines, including supported destinations like R2 and Apache Iceberg with exactly-once delivery guarantees.
tags:
    - cloudflare-pipelines
    - sinks
    - r2-storage
    - apache-iceberg
    - data-ingestion
    - exactly-once-delivery
category: concept
---

Sinks define destinations for your data in Cloudflare Pipelines. They support writing to [R2 Data Catalog](https://developers.cloudflare.com/r2/data-catalog/) as Apache Iceberg tables or to [R2](https://developers.cloudflare.com/r2/) as raw JSON or Parquet files.

Sinks provide exactly-once delivery guarantees, ensuring events are never duplicated or dropped. They can be configured to write files frequently for low-latency ingestion or to write larger, less frequent files for better query performance.

## Learn more

[Manage sinks ](https://developers.cloudflare.com/pipelines/sinks/manage-sinks/)Create, configure, and delete sinks using Wrangler or the API.

[Available sinks ](https://developers.cloudflare.com/pipelines/sinks/available-sinks/)Learn about supported sink destinations and their configuration options.