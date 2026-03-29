---
title: Qwen3 examples — SGLang
url: https://docs.sglang.io/platforms/ascend_npu_qwen3_examples.html
source: crawler
fetched_at: 2026-02-04T08:48:15.737893163-03:00
rendered_js: false
word_count: 86
summary: Provides configuration instructions and command-line examples for deploying various Qwen3 models on Huawei Atlas 800I A3 NPUs using the SGLang framework.
tags:
    - qwen3
    - atlas-800i-a3
    - npu-inference
    - ascend
    - sglang
    - mixture-of-experts
    - speculative-decoding
category: tutorial
---

## Contents

## Qwen3 examples[#](#qwen3-examples "Link to this heading")

## Running Qwen3[#](#running-qwen3 "Link to this heading")

### Running Qwen3-32B on 1 x Atlas 800I A3.[#](#running-qwen3-32b-on-1-x-atlas-800i-a3 "Link to this heading")

Model weights could be found [here](https://huggingface.co/Qwen/Qwen3-32B)

```
exportSGLANG_SET_CPU_AFFINITY=1
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportHCCL_BUFFSIZE=1536
exportHCCL_OP_EXPANSION_MODE=AIV

python-msglang.launch_server\
--devicenpu\
--attention-backendascend\
--trust-remote-code\
--tp-size4\
--model-pathQwen/Qwen3-32B\
--mem-fraction-static0.8
```

### Running Qwen3-32B on 1 x Atlas 800I A3 with Qwen3-32B-Eagle3.[#](#running-qwen3-32b-on-1-x-atlas-800i-a3-with-qwen3-32b-eagle3 "Link to this heading")

Model weights could be found [here](https://huggingface.co/Qwen/Qwen3-32B)

Speculative model weights could be found [here](https://huggingface.co/Zhihu-ai/Zhi-Create-Qwen3-32B-Eagle3)

```
exportSGLANG_SET_CPU_AFFINITY=1
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportHCCL_OP_EXPANSION_MODE=AIV
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server\
--devicenpu\
--attention-backendascend\
--trust-remote-code\
--tp-size4\
--model-pathQwen/Qwen3-32B\
--mem-fraction-static0.8\
--speculative-algorithmEAGLE3\
--speculative-draft-model-pathQwen/Qwen3-32B-Eagle3\
--speculative-num-steps1\
--speculative-eagle-topk1\
--speculative-num-draft-tokens2
```

### Running Qwen3-30B-A3B MOE on 1 x Atlas 800I A3.[#](#running-qwen3-30b-a3b-moe-on-1-x-atlas-800i-a3 "Link to this heading")

Model weights could be found [here](https://huggingface.co/Qwen/Qwen3-30B-A3B)

```
exportSGLANG_SET_CPU_AFFINITY=1
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportHCCL_BUFFSIZE=1536
exportHCCL_OP_EXPANSION_MODE=AIV
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=32
exportSGLANG_DEEPEP_BF16_DISPATCH=1

python-msglang.launch_server\
--devicenpu\
--attention-backendascend\
--trust-remote-code\
--tp-size4\
--model-pathQwen/Qwen3-30B-A3B\
--mem-fraction-static0.8
```

### Running Qwen3-235B-A22B-Instruct-2507 MOE on 1 x Atlas 800I A3.[#](#running-qwen3-235b-a22b-instruct-2507-moe-on-1-x-atlas-800i-a3 "Link to this heading")

Model weights could be found [here](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)

```
exportSGLANG_SET_CPU_AFFINITY=1
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportHCCL_BUFFSIZE=1536
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=32
exportSGLANG_DEEPEP_BF16_DISPATCH=1

python-msglang.launch_server\
--model-pathQwen/Qwen3-235B-A22B-Instruct-2507\
--tp-size16\
--trust-remote-code\
--attention-backendascend\
--devicenpu\
--watchdog-timeout9000\
--mem-fraction-static0.8
```

### Running Qwen3-VL-8B-Instruct on 1 x Atlas 800I A3.[#](#running-qwen3-vl-8b-instruct-on-1-x-atlas-800i-a3 "Link to this heading")

Model weights could be found [here](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct)

```
exportSGLANG_SET_CPU_AFFINITY=1
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportHCCL_BUFFSIZE=1536
exportHCCL_OP_EXPANSION_MODE=AIV

python-msglang.launch_server\
--enable-multimodal\
--attention-backendascend\
--mm-attention-backendascend_attn\
--trust-remote-code\
--tp-size4\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--mem-fraction-static0.8
```