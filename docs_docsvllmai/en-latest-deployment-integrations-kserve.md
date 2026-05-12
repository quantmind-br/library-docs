---
title: KServe - vLLM
url: https://docs.vllm.ai/en/latest/deployment/integrations/kserve/
source: sitemap
fetched_at: 2026-05-07T21:12:00.821528518-03:00
rendered_js: false
word_count: 34
summary: This document outlines how to deploy vLLM on Kubernetes using the KServe platform for scalable model inference.
tags:
    - vllm
    - kserve
    - kubernetes
    - model-serving
    - distributed-inference
    - deployment-guide
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/integrations/kserve.md "Edit this page")

vLLM can be deployed with [KServe](https://github.com/kserve/kserve) on Kubernetes for highly scalable distributed model serving.

You can use vLLM with KServe's [Hugging Face serving runtime](https://kserve.github.io/website/docs/model-serving/generative-inference/overview) or via [`LLMInferenceService` that uses llm-d](https://kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-overview).