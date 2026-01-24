---
title: Bindings
url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/index.md
source: llms
fetched_at: 2026-01-24T15:09:55.175001728-03:00
rendered_js: false
word_count: 388
summary: This document explains how to configure and attach resource bindings like KV namespaces and R2 buckets to User Workers within the Cloudflare for Platforms ecosystem.
tags:
    - cloudflare-workers
    - workers-for-platforms
    - resource-bindings
    - kv-namespace
    - r2-buckets
    - serverless-configuration
category: guide
---

---
title: Bindings · Cloudflare for Platforms docs
description: When you deploy User Workers through Workers for Platforms, you can
  attach bindings to give them access to resources like KV namespaces, D1
  databases, R2 buckets, and more. This enables your end customers to build more
  powerful applications without you having to build the infrastructure
  components yourself.
lastUpdated: 2025-12-29T17:29:32.000Z
chatbotDeprioritize: false
tags: Bindings
source_url:
  html: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/
  md: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/index.md
---

When you deploy User Workers through Workers for Platforms, you can attach [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) to give them access to resources like [KV namespaces](https://developers.cloudflare.com/kv/), [D1 databases](https://developers.cloudflare.com/d1/), [R2 buckets](https://developers.cloudflare.com/r2/), and more. This enables your end customers to build more powerful applications without you having to build the infrastructure components yourself.

With bindings, each of your users can have their own:

* [KV namespace](https://developers.cloudflare.com/kv/) that they can use to store and retrieve data
* [R2 bucket](https://developers.cloudflare.com/r2/) that they can use to store files and assets
* [Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) dataset that they can use to collect observability data
* [Durable Objects](https://developers.cloudflare.com/durable-objects/) class that they can use for stateful coordination

#### Resource isolation

Each User Worker can only access the bindings that are explicitly attached to it. For complete isolation, you can create and attach a unique resource (like a D1 database or KV namespace) to every User Worker.

![Resource Isolation Model](https://developers.cloudflare.com/_astro/programmable-platforms-5.B2yd7IjV_Z1gqk3t.svg)

## Adding a KV Namespace to a User Worker

This example walks through how to create a [KV namespace](https://developers.cloudflare.com/kv/) and attach it to a User Worker. The same process can be used to attach to other [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/).

### 1. Create a KV namespace

Create a KV namespace using the [Cloudflare API](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/bulk_update/).

### 2. Attach the KV namespace to the User Worker

Use the [Upload User Worker API](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/) to attach the KV namespace binding to the Worker. You can do this when you're first uploading the Worker script or when updating an existing Worker.

Note

When using the API to upload scripts, bindings must be specified in the `metadata` object of your multipart upload request. You cannot upload the `wrangler.toml` file as a module to configure the bindings. For more details about multipart uploads, see [Multipart upload metadata](https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/).

##### Example API request

```bash
curl -X PUT \
  "https://api.cloudflare.com/client/v4/accounts/<account-id>/workers/dispatch/namespaces/<your-namespace>/scripts/<script-name>" \
  -H "Content-Type: multipart/form-data" \
  -H "Authorization: Bearer <api-token>" \
  -F 'metadata={
    "main_module": "worker.js",
    "bindings": [
      {
        "type": "kv_namespace",
        "name": "USER_KV",
        "namespace_id": "<your-namespace-id>"
      }
    ]
  }' \
  -F 'worker.js=@/path/to/worker.js'
```

Now, the User Worker has can access the `USER_KV` binding through the `env` argument using `env.USER_DATA.get()`, `env.USER_DATA.put()`, and other KV methods.

Note: If you plan to add new bindings to the Worker, use the `keep_bindings` parameter to ensure existing bindings are preserved while adding new ones.

```bash
curl -X PUT \
  "https://api.cloudflare.com/client/v4/accounts/<account-id>/workers/dispatch/namespaces/<your-namespace>/scripts/<script-name>" \
  -H "Content-Type: multipart/form-data" \
  -H "Authorization: Bearer <api-token>" \
  -F 'metadata={
    "bindings": [
      {
        "type": "r2_bucket",
        "name": "STORAGE",
        "bucket_name": "<your-bucket-name>"
      }
    ],
    "keep_bindings": ["kv_namespace"]
  }'
```