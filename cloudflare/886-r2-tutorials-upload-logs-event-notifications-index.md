---
title: Log and store upload events in R2 with event notifications
url: https://developers.cloudflare.com/r2/tutorials/upload-logs-event-notifications/index.md
source: llms
fetched_at: 2026-01-24T15:21:52.203513412-03:00
rendered_js: false
word_count: 500
summary: This document provides a step-by-step guide on configuring Cloudflare R2 event notifications and Cloudflare Queues to capture and store upload logs in a separate R2 bucket.
tags:
    - cloudflare-r2
    - event-notifications
    - cloudflare-queues
    - cloudflare-workers
    - typescript
    - logging
category: tutorial
---

---
title: Log and store upload events in R2 with event notifications · Cloudflare R2 docs
description: This example provides a step-by-step guide on using event
  notifications to capture and store R2 upload logs in a separate bucket.
lastUpdated: 2025-10-13T13:40:40.000Z
chatbotDeprioritize: false
tags: TypeScript
source_url:
  html: https://developers.cloudflare.com/r2/tutorials/upload-logs-event-notifications/
  md: https://developers.cloudflare.com/r2/tutorials/upload-logs-event-notifications/index.md
---

This example provides a step-by-step guide on using [event notifications](https://developers.cloudflare.com/r2/buckets/event-notifications/) to capture and store R2 upload logs in a separate bucket.

![Push-Based R2 Event Notifications](https://developers.cloudflare.com/_astro/pushed-based-event-notification.NdMYExDK_1ERAd2.svg)

## Prerequisites

To continue, you will need:

* A subscription to [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/#workers), required for using queues.

## 1. Install Wrangler

To begin, refer to [Install/Update Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/#install-wrangler) to install Wrangler, the Cloudflare Developer Platform CLI.

## 2. Create R2 buckets

You will need to create two R2 buckets:

* `example-upload-bucket`: When new objects are uploaded to this bucket, your [consumer Worker](https://developers.cloudflare.com/queues/get-started/#4-create-your-consumer-worker) will write logs.
* `example-log-sink-bucket`: Upload logs from `example-upload-bucket` will be written to this bucket.

To create the buckets, run the following Wrangler commands:

```sh
npx wrangler r2 bucket create example-upload-bucket
npx wrangler r2 bucket create example-log-sink-bucket
```

## 3. Create a queue

Note

You will need a [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) to create and use [Queues](https://developers.cloudflare.com/queues/) and Cloudflare Workers to consume event notifications.

Event notifications capture changes to data in `example-upload-bucket`. You will need to create a new queue to receive notifications:

```sh
npx wrangler queues create example-event-notification-queue
```

## 4. Create a Worker

Before you enable event notifications for `example-upload-bucket`, you need to create a [consumer Worker](https://developers.cloudflare.com/queues/reference/how-queues-works/#create-a-consumer-worker) to receive the notifications.

Create a new Worker with C3 (`create-cloudflare` CLI). [C3](https://developers.cloudflare.com/pages/get-started/c3/) is a command-line tool designed to help you set up and deploy new applications, including Workers, to Cloudflare.

* npm

  ```sh
  npm create cloudflare@latest -- consumer-worker
  ```

* yarn

  ```sh
  yarn create cloudflare consumer-worker
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest consumer-worker
  ```

For setup, select the following options:

* For *What would you like to start with?*, choose `Hello World example`.
* For *Which template would you like to use?*, choose `Worker only`.
* For *Which language do you want to use?*, choose `TypeScript`.
* For *Do you want to use git for version control?*, choose `Yes`.
* For *Do you want to deploy your application?*, choose `No` (we will be making some changes before deploying).

Then, move into your newly created directory:

```sh
cd consumer-worker
```

## 5. Configure your Worker

In your Worker project's \[[Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/)]\(/workers/wrangler/configuration/), add a [queue consumer](https://developers.cloudflare.com/workers/wrangler/configuration/#queues) and [R2 bucket binding](https://developers.cloudflare.com/workers/wrangler/configuration/#r2-buckets). The queues consumer bindings will register your Worker as a consumer of your future event notifications and the R2 bucket bindings will allow your Worker to access your R2 bucket.

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "event-notification-writer",
    "main": "src/index.ts",
    "compatibility_date": "2024-03-29",
    "compatibility_flags": [
      "nodejs_compat"
    ],
    "queues": {
      "consumers": [
        {
          "queue": "example-event-notification-queue",
          "max_batch_size": 100,
          "max_batch_timeout": 5
        }
      ]
    },
    "r2_buckets": [
      {
        "binding": "LOG_SINK",
        "bucket_name": "example-log-sink-bucket"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  name = "event-notification-writer"
  main = "src/index.ts"
  compatibility_date = "2024-03-29"
  compatibility_flags = ["nodejs_compat"]


  [[queues.consumers]]
  queue = "example-event-notification-queue"
  max_batch_size = 100
  max_batch_timeout = 5


  [[r2_buckets]]
  binding = "LOG_SINK"
  bucket_name = "example-log-sink-bucket"
  ```

## 6. Write event notification messages to R2

Add a [`queue` handler](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer) to `src/index.ts` to handle writing batches of notifications to our log sink bucket (you do not need a [fetch handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/)):

```ts
export interface Env {
  LOG_SINK: R2Bucket;
}


export default {
  async queue(batch, env): Promise<void> {
    const batchId = new Date().toISOString().replace(/[:.]/g, "-");
    const fileName = `upload-logs-${batchId}.json`;


    // Serialize the entire batch of messages to JSON
    const fileContent = new TextEncoder().encode(
      JSON.stringify(batch.messages),
    );


    // Write the batch of messages to R2
    await env.LOG_SINK.put(fileName, fileContent, {
      httpMetadata: {
        contentType: "application/json",
      },
    });
  },
} satisfies ExportedHandler<Env>;
```

## 7. Deploy your Worker

To deploy your consumer Worker, run the [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) command:

```sh
npx wrangler deploy
```

## 8. Enable event notifications

Now that you have your consumer Worker ready to handle incoming event notification messages, you need to enable event notifications with the [`wrangler r2 bucket notification create` command](https://developers.cloudflare.com/workers/wrangler/commands/#r2-bucket-notification-create) for `example-upload-bucket`:

```sh
npx wrangler r2 bucket notification create example-upload-bucket --event-type object-create --queue example-event-notification-queue
```

## 9. Test

Now you can test the full end-to-end flow by uploading an object to `example-upload-bucket` in the Cloudflare dashboard. After you have uploaded an object, logs will appear in `example-log-sink-bucket` in a few seconds.