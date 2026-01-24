---
title: Version metadata binding · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/index.md
source: llms
fetched_at: 2026-01-24T15:30:09.824251924-03:00
rendered_js: false
word_count: 102
summary: This document explains how to configure and use the version metadata binding to access Worker version details like ID, tag, and timestamp within the runtime.
tags:
    - cloudflare-workers
    - version-metadata
    - wrangler-config
    - bindings
    - runtime-api
category: reference
---

The version metadata binding can be used to access metadata associated with a [version](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/#versions) from inside the Workers runtime.

Worker version ID, version tag and timestamp of when the version was created are available through the version metadata binding. They can be used in events sent to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) or to any third-party analytics/metrics service in order to aggregate by Worker version.

To use the version metadata binding, update your Worker's Wrangler file:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "version_metadata": {
      "binding": "CF_VERSION_METADATA"
    }
  }
  ```

* wrangler.toml

  ```toml
  [version_metadata]
  binding = "CF_VERSION_METADATA"
  ```

### Interface

An example of how to access the version ID and version tag from within a Worker to send events to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/):

* JavaScript

  ```js
  export default {
    async fetch(request, env, ctx) {
      const { id: versionId, tag: versionTag, timestamp: versionTimestamp } = env.CF_VERSION_METADATA;
      env.WAE.writeDataPoint({
        indexes: [versionId],
        blobs: [versionTag, versionTimestamp],
        //...
      });
      //...
    },
  };
  ```

* TypeScript

  ```ts
  interface Environment {
    CF_VERSION_METADATA: WorkerVersionMetadata;
    WAE: AnalyticsEngineDataset;
  }


  export default {
    async fetch(request, env, ctx) {
      const { id: versionId, tag: versionTag } = env.CF_VERSION_METADATA;
      env.WAE.writeDataPoint({
        indexes: [versionId],
        blobs: [versionTag],
        //...
      });
      //...
    },
  } satisfies ExportedHandler<Env>;
  ```