---
title: llm-d - vLLM
url: https://docs.vllm.ai/en/latest/deployment/integrations/llm-d/
source: sitemap
fetched_at: 2026-05-07T21:12:06.1960099-03:00
rendered_js: false
word_count: 65
summary: This document describes how to deploy vLLM using the llm-d Kubernetes-native inference stack for distributed model serving at scale.
tags:
    - vllm
    - kubernetes
    - llm-d
    - model-serving
    - distributed-inference
    - deployment
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/integrations/llm-d.md "Edit this page")

vLLM can be deployed with [llm-d](https://github.com/llm-d/llm-d), a Kubernetes-native distributed inference serving stack providing well-lit paths for anyone to serve large generative AI models at scale. It helps achieve the fastest "time to state-of-the-art (SOTA) performance" for key OSS models across most hardware accelerators and infrastructure providers.

You can use vLLM with llm-d directly by following [this guide](https://llm-d.ai/docs/guide) or via [KServe's LLMInferenceService](https://kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-overview).