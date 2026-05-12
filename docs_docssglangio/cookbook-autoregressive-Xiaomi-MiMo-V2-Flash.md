---
title: MiMo-V2-Flash - SGLang Documentation
url: https://docs.sglang.io/cookbook/autoregressive/Xiaomi/MiMo-V2-Flash
source: sitemap
fetched_at: 2026-05-11T05:49:57.119787962-03:00
rendered_js: false
word_count: 367
summary: This document provides an overview and deployment guide for the MiMo-V2-Flash inference model within the SGLang framework, covering installation, hardware configuration, and performance optimization techniques.
tags:
    - mimo-v2-flash
    - sglang
    - llm-inference
    - model-deployment
    - speculative-decoding
    - hybrid-attention
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## Introduction

XiaomiMiMo/MiMo-V2-Flash, with 309B total parameters and 15B activated parameters, is a new inference-centric model designed to maximize decoding efficiency created by XiaomiMiMo Team explicitly co-designed for real-world serving workloads, enabling flexible tradeoffs between throughput and latency on different hardware. This model creates a new balance between long-context modeling capability and inference efficiency. Key features include:

- **Hybrid Attention Architecture**: Interleaves Sliding Window Attention (SWA) and Global Attention (GA) with a 5:1 ratio and an aggressive 128-token window. This reduces KV-cache storage by nearly 6x while maintaining long-context performance via learnable attention sink bias.
- **Multi-Token Prediction (MTP)**: Equipped with a lightweight MTP module (0.33B params/block) using dense FFNs. This triples output speed during inference and will be good to accelerates rollout in RL training.
- **Efficient Pre-Training**: Trained on 27T tokens using FP8 mixed precision and native 32k seq length. The context window supports up to 256k length.
- **Agentic Capabilities**: Post-training utilizes Multi-Teacher On-Policy Distillation (MOPD) and large-scale agentic RL, achieving superior performance on SWE-Bench and complex reasoning tasks.

## Installation

MiMo-V2-Flash is currently available in SGLang via Docker image and pip install.

### Docker

```
# Pull the docker image
docker pull lmsysorg/sglang:dev-pr-15207

# Launch the container
docker run -it --gpus all \
  --shm-size=32g \
  --ipc=host \
  --network=host \
  lmsysorg/sglang:dev-pr-15207 bash
```

### Pip Installation

```
# On a machine with SGLang dependencies installed or inside a SGLang nightly container
# Start an SGLang nightly container
docker run -it --gpus all \
  --shm-size=32g \
  --ipc=host \
  --network=host \
  lmsysorg/sglang:nightly-dev-20251215-4449c170 bash

# If you already have SGLang installed, uninstall the current SGLang version
pip uninstall sglang -y

# Install the PyPI Package
pip install sglang==0.5.6.post2.dev8005+pr.15207.g39d5bd57a \
  --extra-index-url https://sgl-project.github.io/whl/pr/
```

## Model Deployment

Use the configuration selector below to automatically generate the appropriate deployment command.

Hardware Platform

H200H100MI355X

Deployment Strategy

TP 8 (Required)DP Attention (DP 2)Multi-token Prediction (MTP)Performance Optimizations

Reasoning & Tools

Reasoning Parser (Qwen3)Tool Call Parser

Run this Command:

```
SGLANG_ENABLE_SPEC_V2=1 sglang serve \
  --model-path XiaomiMiMo/MiMo-V2-Flash \
  --trust-remote-code \
  --tp-size 8 \
  --dp-size 2 \
  --enable-dp-attention \
  --mem-fraction-static 0.75 \
  --max-running-requests 128 \
  --chunked-prefill-size 16384 \
  --model-loader-extra-config '{"enable_multithread_load": "true","num_threads": 64}' \
  --attention-backend fa3 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --enable-multi-layer-eagle \
  --reasoning-parser qwen3 \
  --tool-call-parser mimo
```

MI355X (ROCm) is validated in the selector above with `--tp-size 4`, Triton attention, and `--disable-custom-all-reduce`. `--tp-size 8` hit a QKV sharding error during validation. EAGLE speculative decoding is still WIP on MI355X.

## Testing the deployment

Once the server is running, test it with a chat completion request in another terminal:

```
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "XiaomiMiMo/MiMo-V2-Flash",
    "messages": [
      {"role": "user", "content": "Hello! What can you help me with?"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
  }'
```

**Expected response:**

```
{
  "id": "...",
  "object": "chat.completion",
  "model": "XiaomiMiMo/MiMo-V2-Flash",
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "Hello! I can help you with..."
    }
  }]
}
```

## Troubleshooting

**DeepGEMM Timeout Error** Occasionally DeepGEMM timeout errors occur during first launch. Simply rerun the server command in the same container - the compiled kernels are cached and subsequent launches will be fast. **ROCm MI355X Attention Backend** If you see an error such as `AiterAttnBackend.forward_decode() got an unexpected keyword argument 'sinks'` on MI355X, use the `MI355X` + `Performance Optimizations` command from the selector above, which switches to Triton attention and keeps `--disable-custom-all-reduce`.