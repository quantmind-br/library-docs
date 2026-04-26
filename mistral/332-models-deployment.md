---
title: Deployment | Mistral Docs
url: https://docs.mistral.ai/models/deployment
source: sitemap
fetched_at: 2026-04-26T04:08:54.973690831-03:00
rendered_js: false
word_count: 88
summary: This document provides an overview of available deployment options for Mistral models, including managed cloud provider integrations and local self-hosting strategies.
tags:
    - mistral-models
    - cloud-deployment
    - local-hosting
    - infrastructure-setup
    - model-deployment
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Run Mistral models through managed cloud services or Mistral Compute. Open-weight models (Apache 2.0) can be deployed on compatible hardware. Commercial models are available through cloud provider integrations or Mistral Compute.

## Deployment Options

| Option | Description |
|--------|-------------|
| [Cloud Deployments](https://docs.mistral.ai/models/deployment/cloud-deployments) | Access Mistral models through Azure AI, Amazon Bedrock, Google Cloud Vertex AI, Snowflake Cortex, IBM watsonx, and Outscale |
| [Local Deployment](https://docs.mistral.ai/models/deployment/local-deployment) | Run open-weight models on your own infrastructure using vLLM, TensorRT-LLM, TGI, SkyPilot, Cerebrium, or Cloudflare Workers AI. Supports configurations from single-GPU setups (RTX 4090) to multi-node clusters (4+ H100s for larger models) |