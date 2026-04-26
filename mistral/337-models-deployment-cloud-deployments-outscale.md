---
title: Outscale | Mistral Docs
url: https://docs.mistral.ai/models/deployment/cloud-deployments/outscale
source: sitemap
fetched_at: 2026-04-26T04:09:04.791788543-03:00
rendered_js: false
word_count: 191
summary: This document describes the process of deploying and querying Mistral AI models managed on the Outscale cloud platform.
tags:
    - mistral-ai
    - outscale
    - cloud-deployment
    - model-hosting
    - rest-api
    - infrastructure
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral AI models are available on the Outscale platform as managed deployments. Through the Outscale marketplace, you can subscribe to a Mistral service that will, on your behalf, provision a virtual machine and a GPU then deploy the model on it.

## Available Models

- Mistral Small (24.09)
- Codestral (24.05)
- Ministral 8B (24.10)

For more details, visit the [models](https://docs.mistral.ai/models/overview) page.

## Deployment

Follow the steps described in the [Outscale documentation](https://docs.outscale.com/en/userguide/Subscribing-To-a-Mistral-Service-and-Deploying-it.html) to deploy a service with the model of your choice. Deployed models expose a REST API that you can query using Mistral's SDK or plain HTTP calls. To run the examples below, you will need to set the following environment variables:

- `OUTSCALE_SERVER_URL`: The URL of the VM hosting your Mistral model.
- `OUTSCALE_MODEL_NAME`: The name of the model to query (e.g., `small-2409`, `codestral-2405`).

## FIM Support

Codestral can be queried using an additional completion mode called fill-in-the-middle (FIM). For more information, see the [code generation section](https://docs.mistral.ai/mistral-vibe/using-fim-api).

## Resources

For more information and examples, you can check:
- The [Outscale documentation](https://docs.outscale.com/en/userguide/Subscribing-To-a-Mistral-Service-and-Deploying-it.html) explaining how to subscribe to a Mistral service and deploy it.