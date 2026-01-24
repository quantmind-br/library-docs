---
title: Queues - Publish Directly via HTTP · Cloudflare Queues docs
url: https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/index.md
source: llms
fetched_at: 2026-01-24T15:20:18.459306761-03:00
rendered_js: false
word_count: 149
summary: This document explains how to publish messages to a Cloudflare Queue using the HTTP API, enabling message ingestion from any programming language or HTTP client.
tags:
    - cloudflare-queues
    - http-api
    - message-publishing
    - api-authentication
    - cloud-messaging
category: guide
---

The following example shows you how to publish messages to a Queue from any HTTP client, using a Cloudflare API token to authenticate.

This allows you to write to a Queue from any service or programming language that supports HTTP, including Go, Rust, Python or even a Bash script.

## Prerequisites

* A [queue created](https://developers.cloudflare.com/queues/get-started/#3-create-a-queue) via the [Cloudflare dashboard](https://dash.cloudflare.com) or the [wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/).
* A Cloudflare API token with the `Queues Edit` permission.

### 1. Send a test message

To make sure you successfully authenticate and write a message to your queue, use `curl` on the command line:

```sh
# Make sure to replace the placeholder with your shared secret
curl -XPOST -H "Authorization: Bearer <paste-your-api-token-here>" "https://api.cloudflare.com/client/v4/accounts/<paste-your-account-id-here>/queues/<paste-your-queue-id-here>/messages" --data '{ "body": { "greeting": "hello" } }'
```

```sh
{"success":true}
```

This will issue a HTTP POST request, and if successful, return a HTTP 200 with a `success: true` response body.

* If you receive a HTTP 403, this is because your API token is invalid or does not have the `Queues Edit` permission.

For full documentation about the HTTP Push API, refer to the [Cloudflare API documentation](https://developers.cloudflare.com/api/resources/queues/subresources/messages/).