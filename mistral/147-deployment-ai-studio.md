---
title: Mistral Docs
url: https://docs.mistral.ai/deployment/ai-studio
source: crawler
fetched_at: 2026-01-29T07:33:12.745488942-03:00
rendered_js: false
word_count: 270
summary: This document introduces Mistral AI Studio and outlines the various ways users can access and deploy Mistral models, including through API endpoints, third-party cloud providers, and self-deployment options.
tags:
    - mistral-ai
    - ai-studio
    - cloud-deployment
    - api-access
    - self-deployment
    - large-language-models
category: concept
---

## AI Studio

**Mistral AI Studio** is a platform where you can access and manage models, usage, APIs, organizations, workspaces, and a variety of other features.  
We offer flexible access to our models through a range of options, services, and customizable solutions-including playgrounds, fine-tuning, and more-to meet your specific needs.

[![](https://docs.mistral.ai/img/aistudio.png)](https://console.mistral.ai/home)

Mistral AI currently provides three general types of access to Large Language Models and other services:

- **AI Studio** previously "La Plateforme": We provide API endpoints through [AI Studio](https://console.mistral.ai/) providing pay-as-you-go access to our latest models, manage Workspaces and Usage, as well as diverse other features.
- **Third Party Cloud**: You can access Mistral AI models via your preferred [cloud platforms](https://docs.mistral.ai/deployment/cloud).
- **Self-Deployment**: You can self-deploy our open-weights models on your own on-premise infrastructure. Multiple open-weights models are available under the [Apache 2.0](https://github.com/apache/.github/blob/main/LICENSE) License, you can find them on [Hugging Face](https://huggingface.co/mistralai).
  
  - **Self-Deploy with Enterprise Support**: You can also self-deploy our models, both open and frontier, with enterprise support. Reach out to us [here](https://mistral.ai/contact) if you’re interested!

You will need to activate payments on your account to enable your API keys in the [AI Studio](https://console.mistral.ai/). Check out the [Quickstart](https://docs.mistral.ai/getting-started/quickstart) guide to get started with your first Mistral API request.

Explore diverse capabilities of our models:

For a comprehensive list of options to deploy and consume Mistral AI models on the cloud, head on to the [**cloud deployment section**](https://docs.mistral.ai/deployment/cloud).

Raw model weights can be used in several ways:

- For self-deployment, on cloud or on premise, using either [TensorRT-LLM](https://docs.mistral.ai/deployment/self-deployment/trt) or [vLLM](https://docs.mistral.ai/deployment/self-deployment/vllm), head on to [**Deployment**](https://docs.mistral.ai/deployment/self-deployment/skypilot)
- For research, head-on to our [reference implementation repository](https://github.com/mistralai/mistral-src),
- For local deployment on consumer grade hardware, check out the [llama.cpp](https://github.com/ggerganov/llama.cpp) project or [Ollama](https://ollama.ai/).