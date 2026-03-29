---
title: Llama4 Usage — SGLang
url: https://docs.sglang.io/basic_usage/llama4.html
source: crawler
fetched_at: 2026-02-04T08:47:41.802789739-03:00
rendered_js: false
word_count: 309
summary: This document provides instructions and configuration guidelines for serving and optimizing Meta's Llama 4 models using the SGLang framework. It covers model deployment, memory management, attention backend selection, and advanced features like speculative decoding.
tags:
    - llama-4
    - sglang
    - llm-serving
    - speculative-decoding
    - gpu-optimization
    - inference-engine
category: guide
---

## Contents

## Llama4 Usage[#](#llama4-usage "Link to this heading")

[Llama 4](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md) is Meta’s latest generation of open-source LLM model with industry-leading performance.

SGLang has supported Llama 4 Scout (109B) and Llama 4 Maverick (400B) since [v0.4.5](https://github.com/sgl-project/sglang/releases/tag/v0.4.5).

Ongoing optimizations are tracked in the [Roadmap](https://github.com/sgl-project/sglang/issues/5118).

## Launch Llama 4 with SGLang[#](#launch-llama-4-with-sglang "Link to this heading")

To serve Llama 4 models on 8xH100/H200 GPUs:

```
python3-msglang.launch_server\
--model-pathmeta-llama/Llama-4-Scout-17B-16E-Instruct\
--tp8\
--context-length1000000
```

### Configuration Tips[#](#configuration-tips "Link to this heading")

- **OOM Mitigation**: Adjust `--context-length` to avoid a GPU out-of-memory issue. For the Scout model, we recommend setting this value up to 1M on 8\*H100 and up to 2.5M on 8\*H200. For the Maverick model, we don’t need to set context length on 8\*H200. When hybrid kv cache is enabled, `--context-length` can be set up to 5M on 8\*H100 and up to 10M on 8\*H200 for the Scout model.
- **Attention Backend Auto-Selection**: SGLang automatically selects the optimal attention backend for Llama 4 based on your hardware. You typically don’t need to specify `--attention-backend` manually:
  
  - **Blackwell GPUs (B200/GB200)**: `trtllm_mha`
  - **Hopper GPUs (H100/H200)**: `fa3`
  - **AMD GPUs**: `aiter`
  - **Intel XPU**: `intel_xpu`
  - **Other platforms**: `triton` (fallback)
  
  To override the auto-selection, explicitly specify `--attention-backend` with one of the supported backends: `fa3`, `aiter`, `triton`, `trtllm_mha`, or `intel_xpu`.
- **Chat Template**: Add `--chat-template llama-4` for chat completion tasks.
- **Enable Multi-Modal**: Add `--enable-multimodal` for multi-modal capabilities.
- **Enable Hybrid-KVCache**: Set `--swa-full-tokens-ratio` to adjust the ratio of SWA layer (for Llama4, it’s local attention layer) KV tokens / full layer KV tokens. (default: 0.8, range: 0-1)

### EAGLE Speculative Decoding[#](#eagle-speculative-decoding "Link to this heading")

**Description**: SGLang has supported Llama 4 Maverick (400B) with [EAGLE speculative decoding](https://docs.sglang.io/advanced_features/speculative_decoding.html#EAGLE-Decoding).

**Usage**: Add arguments `--speculative-draft-model-path`, `--speculative-algorithm`, `--speculative-num-steps`, `--speculative-eagle-topk` and `--speculative-num-draft-tokens` to enable this feature. For example:

```
python3 -m sglang.launch_server \
  --model-path meta-llama/Llama-4-Maverick-17B-128E-Instruct \
  --speculative-algorithm EAGLE3 \
  --speculative-draft-model-path nvidia/Llama-4-Maverick-17B-128E-Eagle3 \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --trust-remote-code \
  --tp 8 \
  --context-length 1000000
```

- **Note** The Llama 4 draft model *nvidia/Llama-4-Maverick-17B-128E-Eagle3* can only recognize conversations in chat mode.

## Benchmarking Results[#](#benchmarking-results "Link to this heading")

### Accuracy Test with `lm_eval`[#](#accuracy-test-with-lm-eval "Link to this heading")

The accuracy on SGLang for both Llama4 Scout and Llama4 Maverick can match the [official benchmark numbers](https://ai.meta.com/blog/llama-4-multimodal-intelligence/).

Benchmark results on MMLU Pro dataset with 8\*H100:

Commands:

```
# Llama-4-Scout-17B-16E-Instruct model
python-msglang.launch_server\
--model-pathmeta-llama/Llama-4-Scout-17B-16E-Instruct\
--port30000\
--tp8\
--mem-fraction-static0.8\
--context-length65536
lm_eval--modellocal-chat-completions--model_argsmodel=meta-llama/Llama-4-Scout-17B-16E-Instruct,base_url=http://localhost:30000/v1/chat/completions,num_concurrent=128,timeout=999999,max_gen_toks=2048--tasksmmlu_pro--batch_size128--apply_chat_template--num_fewshot0

# Llama-4-Maverick-17B-128E-Instruct
python-msglang.launch_server\
--model-pathmeta-llama/Llama-4-Maverick-17B-128E-Instruct\
--port30000\
--tp8\
--mem-fraction-static0.8\
--context-length65536
lm_eval--modellocal-chat-completions--model_argsmodel=meta-llama/Llama-4-Maverick-17B-128E-Instruct,base_url=http://localhost:30000/v1/chat/completions,num_concurrent=128,timeout=999999,max_gen_toks=2048--tasksmmlu_pro--batch_size128--apply_chat_template--num_fewshot0
```

Details can be seen in [this PR](https://github.com/sgl-project/sglang/pull/5092).