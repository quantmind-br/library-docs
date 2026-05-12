---
title: Offline Inference - vLLM
url: https://docs.vllm.ai/en/latest/serving/offline_inference/
source: sitemap
fetched_at: 2026-05-07T21:15:12.867924144-03:00
rendered_js: false
word_count: 190
summary: This document describes methods for performing offline inference using vLLM, covering both the direct use of the LLM class and the Ray Data integration for large-scale distributed workloads.
tags:
    - offline-inference
    - vllm
    - ray-data
    - large-language-models
    - model-serving
    - distributed-computing
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/serving/offline_inference.md "Edit this page")

Offline inference is possible in your own code using vLLM's [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM "            LLM") class.

For example, the following code downloads the [`facebook/opt-125m`](https://huggingface.co/facebook/opt-125m) model from HuggingFace and runs it in vLLM using the default configuration.

```
fromvllmimport LLM

# Initialize the vLLM engine.
llm = LLM(model="facebook/opt-125m")
```

After initializing the [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") instance, use the available APIs to perform model inference. The available APIs depend on the model type:

- [Generative models](https://docs.vllm.ai/en/latest/models/generative_models/) output logprobs which are sampled from to obtain the final output text.
- [Pooling models](https://docs.vllm.ai/en/latest/models/pooling_models/) output their hidden states directly.

## Ray Data LLM API[¶](#ray-data-llm-api "Permanent link")

Ray Data LLM is an alternative offline inference API that uses vLLM as the underlying engine. This API adds several batteries-included capabilities that simplify large-scale, GPU-efficient inference:

- Streaming execution processes datasets that exceed aggregate cluster memory.
- Automatic sharding, load balancing, and autoscaling distribute work across a Ray cluster with built-in fault tolerance.
- Continuous batching keeps vLLM replicas saturated and maximizes GPU utilization.
- Transparent support for tensor and pipeline parallelism enables efficient multi-GPU inference.
- Reading and writing to most popular file formats and cloud object storage.
- Scaling up the workload without code changes.

Code

```
importray  # Requires ray>=2.44.1
fromray.data.llmimport vLLMEngineProcessorConfig, build_llm_processor

config = vLLMEngineProcessorConfig(model_source="unsloth/Llama-3.2-1B-Instruct")
processor = build_llm_processor(
    config,
    preprocess=lambda row: {
        "messages": [
            {"role": "system", "content": "You are a bot that completes unfinished haikus."},
            {"role": "user", "content": row["item"]},
        ],
        "sampling_params": {"temperature": 0.3, "max_tokens": 250},
    },
    postprocess=lambda row: {"answer": row["generated_text"]},
)

ds = ray.data.from_items(["An old silent pond..."])
ds = processor(ds)
ds.write_parquet("local:///tmp/data/")
```

For more information about the Ray Data LLM API, see the [Ray Data LLM documentation](https://docs.ray.io/en/latest/data/working-with-llms.html).