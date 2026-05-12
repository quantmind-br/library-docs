---
title: BitsAndBytes - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/bnb/
source: sitemap
fetched_at: 2026-05-07T21:14:22.280459481-03:00
rendered_js: false
word_count: 151
summary: This document explains how to implement BitsAndBytes quantization within vLLM to optimize model memory usage and inference performance.
tags:
    - vllm
    - quantization
    - bitsandbytes
    - model-inference
    - memory-optimization
    - deep-learning
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/bnb.md "Edit this page")

vLLM now supports [BitsAndBytes](https://github.com/TimDettmers/bitsandbytes) for more efficient model inference. BitsAndBytes quantizes models to reduce memory usage and enhance performance without significantly sacrificing accuracy. Compared to other quantization methods, BitsAndBytes eliminates the need for calibrating the quantized model with input data.

Below are the steps to utilize BitsAndBytes with vLLM.

```
pipinstallbitsandbytes>=0.49.2
```

vLLM reads the model's config file and supports both in-flight quantization and pre-quantized checkpoint.

You can find bitsandbytes quantized models on [Hugging Face](https://huggingface.co/models?search=bitsandbytes). And usually, these repositories have a config.json file that includes a quantization\_config section.

## Read quantized checkpoint[¶](#read-quantized-checkpoint "Permanent link")

For pre-quantized checkpoints, vLLM will try to infer the quantization method from the config file, so you don't need to explicitly specify the quantization argument.

```
fromvllmimport LLM
importtorch
# unsloth/tinyllama-bnb-4bit is a pre-quantized checkpoint.
model_id = "unsloth/tinyllama-bnb-4bit"
llm = LLM(
    model=model_id,
    dtype=torch.bfloat16,
    trust_remote_code=True,
)
```

## Inflight quantization: load as 4bit quantization[¶](#inflight-quantization-load-as-4bit-quantization "Permanent link")

For inflight 4bit quantization with BitsAndBytes, you need to explicitly specify the quantization argument.

```
fromvllmimport LLM
importtorch
model_id = "huggyllama/llama-7b"
llm = LLM(
    model=model_id,
    dtype=torch.bfloat16,
    trust_remote_code=True,
    quantization="bitsandbytes",
)
```

## OpenAI Compatible Server[¶](#openai-compatible-server "Permanent link")

Append the following to your model arguments for 4bit inflight quantization:

```
--quantizationbitsandbytes
```