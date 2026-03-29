---
title: Release notes · Cloudflare Workers KV docs
url: https://developers.cloudflare.com/kv/platform/release-notes/index.md
source: llms
fetched_at: 2026-01-24T15:16:40.312805834-03:00
rendered_js: false
word_count: 164
summary: This document contains release notes for Cloudflare Workers KV, highlighting updates to bulk operation error reporting in the REST API and the introduction of a GraphQL-based analytics API.
tags:
    - workers-kv
    - cloudflare
    - release-notes
    - rest-api
    - graphql-api
    - analytics
    - error-handling
category: reference
---

[Subscribe to RSS](https://developers.cloudflare.com/kv/platform/release-notes/index.xml)

## 2024-11-14

**Workers KV REST API bulk operations provide granular errors**

The REST API endpoints for bulk operations ([write](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update/), [delete](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_delete/)) now return the keys of operations that failed during the bulk operation. The updated response bodies are documented in the [REST API documentation](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/list/) and contain the following information in the `result` field:

```
{
  "successful_key_count": number,
  "unsuccessful_keys": string[]
}
```

The unsuccessful keys are an array of keys that were not written successfully to all storage backends and therefore should be retried.

## 2024-08-08

**New KV Analytics API**

Workers KV now has a new [metrics dashboard](https://developers.cloudflare.com/kv/observability/metrics-analytics/#view-metrics-in-the-dashboard) and [analytics API](https://developers.cloudflare.com/kv/observability/metrics-analytics/#query-via-the-graphql-api) that leverages the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) used by many other Cloudflare products. The new analytics API provides per-account and per-namespace metrics for both operations and storage, including latency metrics for read and write operations to Workers KV.

The legacy Workers KV analytics REST API will be turned off as of January 31st, 2025. Developers using this API will receive a series of email notifications prior to the shutdown of the legacy API.