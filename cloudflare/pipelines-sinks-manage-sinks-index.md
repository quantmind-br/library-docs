---
title: Manage sinks · Cloudflare Pipelines Docs
url: https://developers.cloudflare.com/pipelines/sinks/manage-sinks/index.md
source: llms
fetched_at: 2026-01-24T15:19:23.664644512-03:00
rendered_js: false
word_count: 236
summary: This document provides instructions for managing data sinks in Cloudflare Pipelines, covering how to create, view, and delete them via the dashboard or Wrangler CLI.
tags:
    - cloudflare-pipelines
    - data-sinks
    - wrangler-cli
    - data-storage
    - pipeline-configuration
category: guide
---

Learn how to:

* Create and configure sinks for data storage
* View sink configuration
* Delete sinks when no longer needed

## Create a sink

Sinks are made available to pipelines as SQL tables using the sink name (e.g., `INSERT INTO my_sink SELECT * FROM my_stream`).

### Dashboard

1. In the Cloudflare dashboard, go to the **Pipelines** page.

   [Go to **Pipelines**](https://dash.cloudflare.com/?to=/:account/pipelines/overview)

2. Select **Create Pipeline** to launch the pipeline creation wizard.

3. Complete the wizard to create your sink along with the associated stream and pipeline.

### Wrangler CLI

To create a sink, run the [`pipelines sinks create`](https://developers.cloudflare.com/workers/wrangler/commands/#pipelines-sinks-create) command:

```bash
npx wrangler pipelines sinks create <SINK_NAME> \
  --type r2 \
  --bucket my-bucket \
```

For sink-specific configuration options, refer to [Available sinks](https://developers.cloudflare.com/pipelines/sinks/available-sinks/).

Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the [`pipelines setup`](https://developers.cloudflare.com/workers/wrangler/commands/#pipelines-setup) command:

```bash
npx wrangler pipelines setup
```

## View sink configuration

### Dashboard

1. In the Cloudflare dashboard, go to **Pipelines** > **Sinks**.

2. Select a sink to view its configuration.

### Wrangler CLI

To view a specific sink, run the [`pipelines sinks get`](https://developers.cloudflare.com/workers/wrangler/commands/#pipelines-sinks-get) command:

```bash
npx wrangler pipelines sinks get <SINK_ID>
```

To list all sinks in your account, run the [`pipelines sinks list`](https://developers.cloudflare.com/workers/wrangler/commands/#pipelines-sinks-list) command:

```bash
npx wrangler pipelines sinks list
```

## Delete a sink

### Dashboard

1. In the Cloudflare dashboard, go to **Pipelines** > **Sinks**.

2. Select the sink you want to delete.

3. In the **Settings** tab, navigate to **General**, and select **Delete**.

### Wrangler CLI

To delete a sink, run the [`pipelines sinks delete`](https://developers.cloudflare.com/workers/wrangler/commands/#pipelines-sinks-delete) command:

```bash
npx wrangler pipelines sinks delete <SINK_ID>
```

Warning

Deleting a sink stops all data writes to that destination.

## Limitations

Sinks cannot be modified after creation. To change sink configuration, you must delete and recreate the sink.