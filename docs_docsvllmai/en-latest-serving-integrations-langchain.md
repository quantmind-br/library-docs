---
title: LangChain - vLLM
url: https://docs.vllm.ai/en/latest/serving/integrations/langchain/
source: sitemap
fetched_at: 2026-05-07T21:15:16.968546751-03:00
rendered_js: false
word_count: 38
summary: This document provides instructions for integrating and utilizing vLLM within the LangChain framework to perform model inference.
tags:
    - vllm
    - langchain
    - llm-inference
    - gpu-acceleration
    - python-integration
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/serving/integrations/langchain.md "Edit this page")

vLLM is also available via [LangChain](https://github.com/langchain-ai/langchain) .

To install LangChain, run

```
pipinstalllangchainlangchain_community-q
```

To run inference on a single or multiple GPUs, use `VLLM` class from `langchain`.

Code

```
fromlangchain_community.llmsimport VLLM

llm = VLLM(
    model="Qwen/Qwen3-4B",
    trust_remote_code=True,  # mandatory for hf models
    max_new_tokens=128,
    top_k=10,
    top_p=0.95,
    temperature=0.8,
    # for distributed inference
    # tensor_parallel_size=...,
)

print(llm("What is the capital of France ?"))
```

Please refer to this [Tutorial](https://python.langchain.com/docs/integrations/llms/vllm) for more details.