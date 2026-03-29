---
title: SkyPilot | Mistral Docs
url: https://docs.mistral.ai/deployment/self-deployment/skypilot
source: crawler
fetched_at: 2026-01-29T07:34:15.829294632-03:00
rendered_js: false
word_count: 185
summary: A guide on deploying Mistral models using SkyPilot, an open-source framework for running machine learning workloads on multiple cloud providers.
tags:
    - Mistral AI
    - SkyPilot
    - deployment
    - cloud infrastructure
    - LLM
category: guide
---

## Deploy with SkyPilot

[SkyPilot](https://skypilot.readthedocs.io/en/latest/) is a framework for running LLMs, AI, and batch jobs on any cloud, offering maximum cost savings, highest GPU availability, and managed execution. We provide an example SkyPilot config that deploys our models.

After [installing SkyPilot](https://skypilot.readthedocs.io/en/latest/getting-started/installation.html), you need to create a configuration file that tells SkyPilot how and where to deploy your inference server, using our pre-built Docker container:

Once these environment variables are set, you can use `sky launch` to launch the inference server with the appropriate model name, for example with `mistral-7b`:

When deployed this way, the model will be accessible to the whole world. You **must** secure it, either by exposing it exclusively on your private network (change the `--host` Docker option for that), by adding a load-balancer with an authentication mechanism in front of it, or by configuring your instance networking properly.

To easily retrieve the IP address of the deployed `mistral-7b` cluster, you can use:

You can then use `curl` to send a completion request:

Many cloud providers require you to explicitly request access to powerful GPU instances. Read [SkyPilot's guide](https://skypilot.readthedocs.io/en/latest/cloud-setup/quota.html) on how to do this.