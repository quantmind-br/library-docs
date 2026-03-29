---
title: Asynchronous Batch API · Cloudflare Workers AI docs
url: https://developers.cloudflare.com/workers-ai/features/batch-api/index.md
source: llms
fetched_at: 2026-01-24T15:33:14.129995189-03:00
rendered_js: false
word_count: 245
summary: This document explains how to use Cloudflare's Asynchronous Batch API to process large collections of AI inference requests efficiently through queuing and delayed responses.
tags:
    - batch-api
    - asynchronous-processing
    - cloudflare-workers-ai
    - inference
    - rest-api
    - worker-bindings
category: guide
---

Asynchronous batch processing lets you send a collection (batch) of inference requests in a single call. Instead of expecting immediate responses for every request, the system queues them for processing and returns the results later.

Batch processing is useful for large workloads such as summarization or embeddings when there is no human interaction. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if Cloudflare does not have enough capacity at a given time.

When you send a batch request, the API immediately acknowledges receipt with a status like `queued` and provides a unique `request_id`. This ID is later used to poll for the final responses once the processing is complete.

You can use the Batch API by either creating and deploying a Cloudflare Worker that leverages the [Batch API with the AI binding](https://developers.cloudflare.com/workers-ai/features/batch-api/workers-binding/), using the [REST API](https://developers.cloudflare.com/workers-ai/features/batch-api/rest-api/) directly or by starting from a [template](https://github.com/craigsdennis/batch-please-workers-ai).

Note

Ensure that the total payload is under 10 MB.

## Demo application

If you want to get started quickly, click the button below:

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/craigsdennis/batch-please-workers-ai)

This will create a repository in your GitHub account and deploy a ready-to-use Worker that demonstrates how to use Cloudflare's Asynchronous Batch API. The template includes preconfigured AI bindings, and examples for sending and retrieving batch requests with and without external references. Once deployed, you can visit the live Worker and start experimenting with the Batch API immediately.

## Supported Models

Refer to our [model catalog](https://developers.cloudflare.com/workers-ai/models/?capabilities=Batch) for supported models.