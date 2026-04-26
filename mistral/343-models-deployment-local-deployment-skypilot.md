---
title: SkyPilot | Mistral Docs
url: https://docs.mistral.ai/models/deployment/local-deployment/skypilot
source: sitemap
fetched_at: 2026-04-26T04:09:17.424399569-03:00
rendered_js: false
word_count: 185
summary: This document provides instructions for deploying LLM inference servers to cloud environments using the SkyPilot framework and pre-built Docker containers.
tags:
    - skypilot
    - llm-deployment
    - cloud-infrastructure
    - gpu-instances
    - inference-server
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[SkyPilot](https://skypilot.readthedocs.io/en/latest/) is a framework for running LLMs, AI, and batch jobs on any cloud, offering maximum cost savings, highest GPU availability, and managed execution. We provide an example SkyPilot config that deploys our models.

## Setup

After [installing SkyPilot](https://skypilot.readthedocs.io/en/latest/getting-started/installation.html), you need to create a configuration file that tells SkyPilot how and where to deploy your inference server, using our pre-built Docker container:

```yaml
```

Once these environment variables are set, you can use `sky launch` to launch the inference server with the appropriate model name, for example with `mistral-7b`:

```bash
```

## Security

> [!warning] When deployed this way, the model will be accessible to the whole world. You **must** secure it, either by exposing it exclusively on your private network (change the `--host` Docker option for that), by adding a load-balancer with an authentication mechanism in front of it, or by configuring your instance networking properly.

## Retrieving IP Address

To easily retrieve the IP address of the deployed `mistral-7b` cluster, you can use:

```bash
```

You can then use `curl` to send a completion request:

```bash
```

> [!note] Many cloud providers require you to explicitly request access to powerful GPU instances. Read [SkyPilot's guide](https://skypilot.readthedocs.io/en/latest/cloud-setup/quota.html) on how to do this.