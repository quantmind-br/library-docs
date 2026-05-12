---
title: GGUF - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/gguf/
source: sitemap
fetched_at: 2026-05-07T21:14:24.958887128-03:00
rendered_js: false
word_count: 205
summary: This document explains how to load and run GGUF format models within the vLLM framework, including instructions for using HuggingFace repositories or local files.
tags:
    - vllm
    - gguf
    - quantization
    - model-loading
    - llm-inference
    - gpu-acceleration
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/gguf.md "Edit this page")

Warning

Please note that GGUF support in vLLM is highly experimental and under-optimized at the moment, it might be incompatible with other features. Currently, you can use GGUF as a way to reduce memory footprint. If you encounter any issues, please report them to the vLLM team.

Warning

Currently, vllm only supports loading single-file GGUF models. If you have a multi-files GGUF model, you can use [gguf-split](https://github.com/ggerganov/llama.cpp/pull/6135) tool to merge them to a single-file model.

To run a GGUF model with vLLM, you can use the `repo_id:quant_type` format to load directly from HuggingFace. For example, to load a Q4\_K\_M quantized model from [unsloth/Qwen3-0.6B-GGUF](https://huggingface.co/unsloth/Qwen3-0.6B-GGUF):

```
# We recommend using the tokenizer from base model to avoid long-time and buggy tokenizer conversion.
vllmserveunsloth/Qwen3-0.6B-GGUF:Q4_K_M--tokenizerQwen/Qwen3-0.6B
```

You can also add `--tensor-parallel-size 2` to enable tensor parallelism inference with 2 GPUs:

```
vllmserveunsloth/Qwen3-0.6B-GGUF:Q4_K_M\
--tokenizerQwen/Qwen3-0.6B\
--tensor-parallel-size2
```

Alternatively, you can download and use a local GGUF file:

```
wgethttps://huggingface.co/unsloth/Qwen3-0.6B-GGUF/resolve/main/Qwen3-0.6B-Q4_K_M.gguf
vllmserve./Qwen3-0.6B-Q4_K_M.gguf--tokenizerQwen/Qwen3-0.6B
```

Warning

We recommend using the tokenizer from base model instead of GGUF model. Because the tokenizer conversion from GGUF is time-consuming and unstable, especially for some models with large vocab size.

GGUF assumes that HuggingFace can convert the metadata to a config file. In case HuggingFace doesn't support your model you can manually create a config and pass it as hf-config-path

```
# If your model is not supported by HuggingFace you can manually provide a HuggingFace compatible config path
vllmserveunsloth/Qwen3-0.6B-GGUF:Q4_K_M\
--tokenizerQwen/Qwen3-0.6B\
--hf-config-pathQwen/Qwen3-0.6B
```

You can also use the GGUF model directly through the LLM entrypoint:

Code

```
fromvllmimport LLM, SamplingParams

# In this script, we demonstrate how to pass input to the chat method:
conversation = [
   {
      "role": "system",
      "content": "You are a helpful assistant",
   },
   {
      "role": "user",
      "content": "Hello",
   },
   {
      "role": "assistant",
      "content": "Hello! How can I assist you today?",
   },
   {
      "role": "user",
      "content": "Write an essay about the importance of higher education.",
   },
]

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

# Create an LLM using repo_id:quant_type format.
llm = LLM(
   model="unsloth/Qwen3-0.6B-GGUF:Q4_K_M",
   tokenizer="Qwen/Qwen3-0.6B",
)
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.chat(conversation, sampling_params)

# Print the outputs.
for output in outputs:
   prompt = output.prompt
   generated_text = output.outputs[0].text
   print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```