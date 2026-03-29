---
title: Qwen3-Next Usage — SGLang
url: https://docs.sglang.io/basic_usage/qwen3.html
source: crawler
fetched_at: 2026-02-04T08:47:39.850937598-03:00
rendered_js: false
word_count: 232
summary: This document provides instructions for serving and optimizing Qwen3-Next models using SGLang, covering configuration settings for Mamba cache and speculative decoding.
tags:
    - sglang
    - qwen3-next
    - llm-serving
    - mamba-radix-cache
    - speculative-decoding
    - inference-optimization
category: guide
---

## Contents

## Qwen3-Next Usage[#](#qwen3-next-usage "Link to this heading")

SGLang has supported Qwen3-Next-80B-A3B-Instruct and Qwen3-Next-80B-A3B-Thinking since [this PR](https://github.com/sgl-project/sglang/pull/10233).

## Launch Qwen3-Next with SGLang[#](#launch-qwen3-next-with-sglang "Link to this heading")

To serve Qwen3-Next models on 4xH100/H200 GPUs:

```
python3-msglang.launch_server--modelQwen/Qwen3-Next-80B-A3B-Instruct--tp4
```

### Configuration Tips[#](#configuration-tips "Link to this heading")

- `--max-mamba-cache-size`: Adjust `--max-mamba-cache-size` to increase mamba cache space and max running requests capability. It will decrease KV cache space as a trade-off. You can adjust it according to workload.
- `--mamba-ssm-dtype`: `bfloat16` or `float32`, use `bfloat16` to save mamba cache size and `float32` to get more accurate results. The default setting is `float32`.
- `--mamba-full-memory-ratio`: The ratio of mamba state memory to full kv cache memory. The default is 0.9.

### Mamba Radix Cache[#](#mamba-radix-cache "Link to this heading")

SGLang supports prefix caching for Qwen3-Next models named `MambaRadixCache`, which improves inference speed by reusing computation results. There are two versions of `MambaRadixCache`:

- `no_buffer`: The default version, which is also other hybrid linear models’ choice. When it is enabled, SGLang will automatically close overlap schedule for compatibility reasons.
- `extra_buffer`: An optimized version that is compatible with features like page size &gt; 1, overlap schedule, and speculative decoding. It also supports storing mamba state in branching positions. However, it requires two extra mamba spaces for a ping-pong buffer for each request. To enable it, add the argument `--mamba-scheduler-strategy extra_buffer` when launching the server.

### EAGLE Speculative Decoding[#](#eagle-speculative-decoding "Link to this heading")

**Description**: SGLang has supported Qwen3-Next models with [EAGLE speculative decoding](https://docs.sglang.io/advanced_features/speculative_decoding.html#EAGLE-Decoding).

**Usage**: Add arguments `--speculative-algorithm`, `--speculative-num-steps`, `--speculative-eagle-topk` and `--speculative-num-draft-tokens` to enable this feature. For example:

```
python3-msglang.launch_server\
--modelQwen/Qwen3-Next-80B-A3B-Instruct\
--tp4\
--speculative-num-steps3\
--speculative-eagle-topk1\
--speculative-num-draft-tokens4\
--speculative-algoNEXTN
```

Details can be seen in [this PR](https://github.com/sgl-project/sglang/pull/10233).