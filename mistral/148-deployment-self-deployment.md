---
title: Self-deployment | Mistral Docs
url: https://docs.mistral.ai/deployment/self-deployment
source: crawler
fetched_at: 2026-01-29T07:33:13.969192675-03:00
rendered_js: false
word_count: 52
summary: This document outlines the recommended inference engines and infrastructure management tools for self-deploying Mistral AI models on private infrastructure.
tags:
    - self-deployment
    - mistral-ai
    - inference-engines
    - vllm
    - infrastructure-management
category: guide
---

Mistral AI models can be **self-deployed on your own infrastructure** through various inference engines. We recommend using [vLLM](https://vllm.readthedocs.io/), a highly-optimized Python-only serving framework which can expose an OpenAI-compatible API.

Other inference engine alternatives include [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) and [TGI](https://huggingface.co/docs/text-generation-inference/index).

You can also leverage specific tools to facilitate infrastructure management, such as [SkyPilot](https://skypilot.readthedocs.io) or [Cerebrium](https://www.cerebrium.ai).