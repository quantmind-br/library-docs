---
title: LlamaIndex - vLLM
url: https://docs.vllm.ai/en/latest/serving/integrations/llamaindex/
source: sitemap
fetched_at: 2026-05-07T21:15:18.228180651-03:00
rendered_js: false
word_count: 37
summary: This document provides instructions on how to integrate and run vLLM models within the LlamaIndex framework for inference.
tags:
    - vllm
    - llamaindex
    - llm-inference
    - gpu-optimization
    - model-serving
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/serving/integrations/llamaindex.md "Edit this page")

vLLM is also available via [LlamaIndex](https://github.com/run-llama/llama_index) .

To install LlamaIndex, run

```
pipinstallllama-index-llms-vllm-q
```

To run inference on a single or multiple GPUs, use `Vllm` class from `llamaindex`.

```
fromllama_index.llms.vllmimport Vllm

llm = Vllm(
    model="microsoft/Orca-2-7b",
    tensor_parallel_size=4,
    max_new_tokens=100,
    vllm_kwargs={"gpu_memory_utilization": 0.5},
)
```

Please refer to this [Tutorial](https://docs.llamaindex.ai/en/latest/examples/llm/vllm/) for more details.