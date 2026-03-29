---
title: Pipelines · Cloudflare Pipelines Docs
url: https://developers.cloudflare.com/pipelines/pipelines/index.md
source: llms
fetched_at: 2026-01-24T15:19:15.030411693-03:00
rendered_js: false
word_count: 73
summary: This document explains how Pipelines use SQL transformations to connect data streams and sinks for real-time processing, validation, and enrichment.
tags:
    - cloudflare-pipelines
    - sql-transformations
    - data-ingestion
    - stream-processing
    - data-transformation
category: concept
---

Pipelines connect [streams](https://developers.cloudflare.com/pipelines/streams/) and [sinks](https://developers.cloudflare.com/pipelines/sinks/) via SQL transformations, which can modify events before writing them to storage. This enables you to shift left, pushing validation, schematization, and processing to your ingestion layer to make your queries easy, fast, and correct.

Pipelines enable you to filter, transform, enrich, and restructure events in real-time as data flows from streams to sinks.

## Learn more

[Manage pipelines ](https://developers.cloudflare.com/pipelines/pipelines/manage-pipelines/)Create, configure, and manage SQL transformations between streams and sinks.