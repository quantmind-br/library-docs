---
title: Write to Analytics Engine · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/examples/analytics-engine/index.md
source: llms
fetched_at: 2026-01-24T15:25:39.991048939-03:00
rendered_js: false
word_count: 174
summary: This document explains how to set up and use Workers Analytics Engine to collect, store, and query custom time-series metrics from Cloudflare Workers.
tags:
    - cloudflare-workers
    - analytics-engine
    - time-series
    - telemetry
    - data-analysis
    - sql-api
category: guide
---

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) provides time-series analytics at scale. Use it to track custom metrics, build usage-based billing, or understand service health on a per-customer basis.

Unlike logs, Analytics Engine is designed for aggregated queries over high-cardinality data. Writes are non-blocking and do not impact request latency.

## Configure the binding

Add an Analytics Engine dataset binding to your Wrangler configuration file. The dataset is created automatically when you first write to it.

* wrangler.jsonc

  ```jsonc
  {
    "analytics_engine_datasets": [
      {
        "binding": "ANALYTICS",
        "dataset": "my_dataset",
      },
    ],
  }
  ```

* wrangler.toml

  ```toml
  [[analytics_engine_datasets]]
  binding = "ANALYTICS"
  dataset = "my_dataset"
  ```

## Write data points

* JavaScript

  ```js
  export default {
    async fetch(request, env) {
      const url = new URL(request.url);


      // Write a page view event
      env.ANALYTICS.writeDataPoint({
        blobs: [
          url.pathname,
          request.headers.get("cf-connecting-country") ?? "unknown",
        ],
        doubles: [1], // Count
        indexes: [url.hostname], // Sampling key
      });


      // Write a response timing event
      const start = Date.now();
      const response = await fetch(request);
      const duration = Date.now() - start;


      env.ANALYTICS.writeDataPoint({
        blobs: [url.pathname, response.status.toString()],
        doubles: [duration],
        indexes: [url.hostname],
      });


      // Writes are non-blocking - no need to await or use waitUntil()
      return response;
    },
  };
  ```

* TypeScript

  ```ts
  interface Env {
    ANALYTICS: AnalyticsEngineDataset;
  }


  export default {
    async fetch(request: Request, env: Env): Promise<Response> {
      const url = new URL(request.url);


      // Write a page view event
      env.ANALYTICS.writeDataPoint({
        blobs: [
          url.pathname,
          request.headers.get("cf-connecting-country") ?? "unknown",
        ],
        doubles: [1], // Count
        indexes: [url.hostname], // Sampling key
      });


      // Write a response timing event
      const start = Date.now();
      const response = await fetch(request);
      const duration = Date.now() - start;


      env.ANALYTICS.writeDataPoint({
        blobs: [url.pathname, response.status.toString()],
        doubles: [duration],
        indexes: [url.hostname],
      });


      // Writes are non-blocking - no need to await or use waitUntil()
      return response;
    },
  };
  ```

## Data point structure

Each data point consists of:

* **blobs** (strings) - Dimensions for grouping and filtering. Use for paths, regions, status codes, or customer IDs.
* **doubles** (numbers) - Numeric values to record, such as counts, durations, or sizes.
* **indexes** (strings) - A single string used as the [sampling key](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/#sampling). Group related events under the same index.

## Query your data

Query your data using the [SQL API](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/):

```bash
curl "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/analytics_engine/sql" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --data "SELECT blob1 AS path, SUM(_sample_interval) AS views FROM my_dataset WHERE timestamp > NOW() - INTERVAL '1' HOUR GROUP BY path ORDER BY views DESC LIMIT 10"
```

## Related resources

* [Analytics Engine documentation](https://developers.cloudflare.com/analytics/analytics-engine/) - Full reference for Workers Analytics Engine.
* [SQL API reference](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/) - Query syntax and available functions.
* [Grafana integration](https://developers.cloudflare.com/analytics/analytics-engine/grafana/) - Visualize Analytics Engine data in Grafana.