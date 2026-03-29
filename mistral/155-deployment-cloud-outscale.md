---
title: Outscale | Mistral Docs
url: https://docs.mistral.ai/deployment/cloud/outscale
source: crawler
fetched_at: 2026-01-29T07:34:19.726050225-03:00
rendered_js: false
word_count: 191
summary: This document explains how to deploy and query Mistral AI models on the Outscale platform using managed deployments and REST APIs.
tags:
    - mistral-ai
    - outscale-cloud
    - model-deployment
    - rest-api
    - codestral
    - cloud-infrastructure
category: guide
---

Mistral AI models are available on the Outscale platform as managed deployments. Through the Outscale marketplace, you can subscribe to a Mistral service that will, on your behalf, provision a virtual machine and a GPU then deploy the model on it. As of today, the following models are available:

- Mistral Small (24.09)
- Codestral (24.05)
- Ministral 8B (24.10)

For more details, visit the [models](https://docs.mistral.ai/getting-started/models/models_overview) page.

The following sections outline the steps to query a Mistral model on the Outscale platform.

Follow the steps described in the [Outscale documentation](https://docs.outscale.com/en/userguide/Subscribing-To-a-Mistral-Service-and-Deploying-it.html) to deploy a service with the model of your choice. Deployed models expose a REST API that you can query using Mistral's SDK or plain HTTP calls. To run the examples below, you will need to set the following environment variables:

- `OUTSCALE_SERVER_URL`: The URL of the VM hosting your Mistral model.
- `OUTSCALE_MODEL_NAME`: The name of the model to query (e.g., `small-2409`, `codestral-2405`).

Codestral can be queried using an additional completion mode called fill-in-the-middle (FIM). For more information, see the [code generation section](https://docs.mistral.ai/capabilities/code_generation).

For more information and examples, you can check:

- The [Outscale documentation](https://docs.outscale.com/en/userguide/Subscribing-To-a-Mistral-Service-and-Deploying-it.html) explaining how to subscribe to a Mistral service and deploy it.