---
title: Cerebrium | Mistral Docs
url: https://docs.mistral.ai/models/deployment/local-deployment/cerebrium
source: sitemap
fetched_at: 2026-04-26T04:09:13.676667782-03:00
rendered_js: false
word_count: 291
summary: This document provides a walkthrough for deploying AI applications on the Cerebrium serverless infrastructure, covering project initialization, hardware configuration, and API deployment.
tags:
    - serverless-ai
    - gpu-infrastructure
    - model-deployment
    - python-sdk
    - cloud-computing
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[Cerebrium](https://www.cerebrium.ai/) is a serverless AI infrastructure platform that makes it easier for companies to build and deploy AI based applications. They offer Serverless GPU's with low cold start times with over 12 varieties of GPU chips that auto scale and you only pay for the compute you use.

## Installation

First, we install Cerebrium and login to get authenticated:

```bash
```

## Project Setup

Create your first project:

```bash
```

## Configuration

Set up your environment and hardware in the **cerebrium.toml** file. Here we are using an Ampere A10 GPU. You can read more [here](https://docs.cerebrium.ai/cerebrium/environments/custom-images).

## Writing Code

Running code in Cerebrium is like writing normal python with no special syntax. In your **main.py** specify the following:

```python
```

## Authentication

We need to add our Hugging Face token to our [Cerebrium Secrets](https://docs.cerebrium.ai/cerebrium/environments/using-secrets) since using the Mistral model requires authentication. Please make sure the Huggingface token you added, has **WRITE** permissions.

On first deploy, it will download the model and store it on disk therefore for subsequent calls it will load the model from disk.

Add the following to your main.py:

```python
```

## Deployment

Every function in Cerebrium is callable through an API endpoint. Code at the top most layer (ie: not in a function) is instantiated only when the container is spun up the first time so for subsequent calls, it will simply run the code defined in the function you call.

Our final main.py should look like this:

```python
```

You will see your application deploy, install pip packages and download the model. Once completed it will output a CURL request you can use to call your endpoint. Just remember to end the url with the function you would like to call - in this case /run.

You should then get a message looking like this: