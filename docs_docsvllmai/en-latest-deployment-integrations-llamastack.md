---
title: Llama Stack - vLLM
url: https://docs.vllm.ai/en/latest/deployment/integrations/llamastack/
source: sitemap
fetched_at: 2026-05-07T21:12:04.810788801-03:00
rendered_js: false
word_count: 71
summary: This document provides instructions for integrating vLLM with Llama Stack, covering both remote OpenAI-compatible API setups and embedded vLLM provider configurations.
tags:
    - vllm
    - llama-stack
    - inference
    - deployment
    - integration
    - model-serving
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/integrations/llamastack.md "Edit this page")

vLLM is also available via [Llama Stack](https://github.com/llamastack/llama-stack).

To install Llama Stack, run

```
pipinstallllama-stack-q
```

## Inference using OpenAI-Compatible API[¶](#inference-using-openai-compatible-api "Permanent link")

Then start the Llama Stack server and configure it to point to your vLLM server with the following settings:

```
inference:
-provider_id:vllm0
provider_type:remote::vllm
config:
url:http://127.0.0.1:8000
```

Please refer to [this guide](https://llama-stack.readthedocs.io/en/latest/providers/inference/remote_vllm.html) for more details on this remote vLLM provider.

## Inference using Embedded vLLM[¶](#inference-using-embedded-vllm "Permanent link")

An [inline provider](https://github.com/llamastack/llama-stack/tree/main/llama_stack/providers/inline/inference) is also available. This is a sample of configuration using that method:

```
inference:
-provider_type:vllm
config:
model:Llama3.1-8B-Instruct
tensor_parallel_size:4
```