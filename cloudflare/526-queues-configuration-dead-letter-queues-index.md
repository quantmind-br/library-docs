---
title: Dead Letter Queues · Cloudflare Queues docs
url: https://developers.cloudflare.com/queues/configuration/dead-letter-queues/index.md
source: llms
fetched_at: 2026-01-24T15:20:04.638967394-03:00
rendered_js: false
word_count: 173
summary: This document explains the functionality and configuration of Dead Letter Queues (DLQ) within Cloudflare Queues to manage messages that fail delivery after multiple retries.
tags:
    - cloudflare-queues
    - dead-letter-queue
    - message-delivery
    - configuration
    - error-handling
    - wrangler
category: concept
---

A Dead Letter Queue (DLQ) is a common concept in a messaging system, and represents where messages are sent when a delivery failure occurs with a consumer after `max_retries` is reached. A Dead Letter Queue is like any other queue, and can be produced to and consumed from independently.

With Cloudflare Queues, a Dead Letter Queue is defined within your [consumer configuration](https://developers.cloudflare.com/queues/configuration/configure-queues/). Messages are delivered to the DLQ when they reach the configured retry limit for the consumer. Without a DLQ configured, messages that reach the retry limit are deleted permanently.

For example, the following consumer configuration would send messages to our DLQ named `"my-other-queue"` after retrying delivery (by default, 3 times):

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "queues": {
      "consumers": [
        {
          "queue": "my-queue",
          "dead_letter_queue": "my-other-queue"
        }
      ]
    }
  }
  ```

* wrangler.toml

  ```toml
  [[queues.consumers]]
    queue = "my-queue"
    dead_letter_queue = "my-other-queue"
  ```

You can also configure a DLQ when creating a consumer from the command-line using `wrangler`:

```sh
wrangler queues consumer add $QUEUE_NAME $SCRIPT_NAME --dead-letter-queue=$NAME_OF_OTHER_QUEUE
```

To process messages placed on your DLQ, you need to [configure a consumer](https://developers.cloudflare.com/queues/configuration/configure-queues/) for that queue as you would with any other queue.

Messages delivered to a DLQ without an active consumer will persist for four (4) days before being deleted from the queue.