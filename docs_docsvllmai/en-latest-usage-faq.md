---
title: Frequently Asked Questions - vLLM
url: https://docs.vllm.ai/en/latest/usage/faq/
source: sitemap
fetched_at: 2026-05-07T21:15:28.881264244-03:00
rendered_js: false
word_count: 299
summary: This document provides answers to common questions regarding vLLM, covering multi-model serving, embedding model recommendations, and factors affecting output determinism and numerical stability.
tags:
    - vllm
    - inference-stability
    - embedding-models
    - openai-api
    - numerical-accuracy
    - model-serving
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/usage/faq.md "Edit this page")

> Q: How can I serve multiple models on a single port using the OpenAI API?

A: Assuming that you're referring to using OpenAI compatible server to serve multiple models at once, that is not currently supported, you can run multiple instances of the server (each serving a different model) at the same time, and have another layer to route the incoming request to the correct server accordingly.

* * *

> Q: Which model to use for offline inference embedding?

A: You can try [e5-mistral-7b-instruct](https://huggingface.co/intfloat/e5-mistral-7b-instruct) and [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5); more are listed [here](https://docs.vllm.ai/en/latest/models/supported_models/).

By extracting hidden states, vLLM can automatically convert text generation models like [Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B), [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) into embedding models, but they are expected to be inferior to models that are specifically trained on embedding tasks.

* * *

> Q: Can the output of a prompt vary across runs in vLLM?

A: Yes, it can. vLLM does not guarantee stable log probabilities (logprobs) for the output tokens. Variations in logprobs may occur due to numerical instability in Torch operations or non-deterministic behavior in batched Torch operations when batching changes. For more details, see the [Numerical Accuracy section](https://pytorch.org/docs/stable/notes/numerical_accuracy.html#batched-computations-or-slice-computations).

In vLLM, the same requests might be batched differently due to factors such as other concurrent requests, changes in batch size, or batch expansion in speculative decoding. These batching variations, combined with numerical instability of Torch operations, can lead to slightly different logit/logprob values at each step. Such differences can accumulate, potentially resulting in different tokens being sampled. Once a different token is sampled, further divergence is likely.

## Mitigation Strategies[¶](#mitigation-strategies "Permanent link")

- For improved stability and reduced variance, use `float32`. Note that this will require more memory.
- If using `bfloat16`, switching to `float16` can also help.
- Using request seeds can aid in achieving more stable generation for temperature &gt; 0, but discrepancies due to precision differences may still occur.