---
title: Cron Container · Cloudflare Containers docs
url: https://developers.cloudflare.com/containers/examples/cron/index.md
source: llms
fetched_at: 2026-01-24T15:11:15.827002292-03:00
rendered_js: false
word_count: 48
summary: This document explains how to use Workers Cron Triggers to launch and manage containers on a predefined schedule. It covers configuring the Wrangler file and implementing the scheduled handler in a Worker script.
tags:
    - cloudflare-workers
    - cron-triggers
    - containers
    - durable-objects
    - automation
    - scheduling
category: guide
---

To launch a container on a schedule, you can use a Workers [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/).

For a full example, see the [Cron Container Template](https://github.com/mikenomitch/cron-container/tree/main).

Use a cron expression in your Wrangler config to specify the schedule:

* wrangler.jsonc

  ```jsonc
  {
    "name": "cron-container",
    "main": "src/index.ts",
    "triggers": {
      "crons": [
        "*/2 * * * *" // Run every 2 minutes
      ]
    },
    "containers": [
      {
        "class_name": "CronContainer",
        "image": "./Dockerfile"
      }
    ],
    "durable_objects": {
      "bindings": [
        {
          "class_name": "CronContainer",
          "name": "CRON_CONTAINER"
        }
      ]
    },
    "migrations": [
      {
        "new_sqlite_classes": ["CronContainer"],
        "tag": "v1"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  name = "cron-container"
  main = "src/index.ts"


  [triggers]
  crons = [ "*/2 * * * *" ]


  [[containers]]
  class_name = "CronContainer"
  image = "./Dockerfile"


  [[durable_objects.bindings]]
  class_name = "CronContainer"
  name = "CRON_CONTAINER"


  [[migrations]]
  new_sqlite_classes = [ "CronContainer" ]
  tag = "v1"
  ```

Then in your Worker, call your Container from the "scheduled" handler:

```ts
import { Container, getContainer } from '@cloudflare/containers';


export class CronContainer extends Container {
  sleepAfter = '10s';


  override onStart() {
    console.log('Starting container');
  }


  override onStop() {
    console.log('Container stopped');
  }
}


export default {
  async fetch(): Promise<Response> {
    return new Response("This Worker runs a cron job to execute a container on a schedule.");
  },


  async scheduled(_controller: any, env: { CRON_CONTAINER: DurableObjectNamespace<CronContainer> }) {
    let container = getContainer(env.CRON_CONTAINER);
    await container.start({
      envVars: {
        MESSAGE: "Start Time: " + new Date().toISOString(),
      }
    })
  },
};
```