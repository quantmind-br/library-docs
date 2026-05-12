---
title: Reinforcement Learning from Human Feedback
url: https://docs.vllm.ai/en/latest/training/rlhf/
source: sitemap
fetched_at: 2026-05-07T21:15:20.815459351-03:00
rendered_js: false
word_count: 143
summary: This document provides an overview of using vLLM to facilitate Reinforcement Learning from Human Feedback (RLHF) by integrating with various open-source training libraries and optimizing throughput.
tags:
    - rlhf
    - language-models
    - model-alignment
    - distributed-training
    - gpu-utilization
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/training/rlhf.md "Edit this page")

Reinforcement Learning from Human Feedback (RLHF) is a technique that fine-tunes language models using human-generated preference data to align model outputs with desired behaviors. vLLM can be used to generate the completions for RLHF.

The following open-source RL libraries use vLLM for fast rollouts (sorted alphabetically and non-exhaustive):

- [Cosmos-RL](https://github.com/nvidia-cosmos/cosmos-rl)
- [ms-swift](https://github.com/modelscope/ms-swift/tree/main)
- [NeMo-RL](https://github.com/NVIDIA-NeMo/RL)
- [Open Instruct](https://github.com/allenai/open-instruct)
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [PipelineRL](https://github.com/ServiceNow/PipelineRL)
- [Prime-RL](https://github.com/PrimeIntellect-ai/prime-rl)
- [SkyRL](https://github.com/NovaSky-AI/SkyRL)
- [TRL](https://github.com/huggingface/trl)
- [Unsloth](https://github.com/unslothai/unsloth)
- [verl](https://github.com/volcengine/verl)

For weight synchronization between training and inference, see the [Weight Transfer](https://docs.vllm.ai/en/latest/training/weight_transfer/) documentation, which covers the pluggable backend system with [NCCL](https://docs.vllm.ai/en/latest/training/weight_transfer/nccl/) (multi-GPU) and [IPC](https://docs.vllm.ai/en/latest/training/weight_transfer/ipc/) (same-GPU) engines.

For pipelining generation and training to improve GPU utilization and throughput, see the [Async Reinforcement Learning](https://docs.vllm.ai/en/latest/training/async_rl/) guide, which covers the pause/resume API for safely updating weights mid-flight.

See the following notebooks showing how to use vLLM for GRPO:

- [Efficient Online Training with GRPO and vLLM in TRL](https://huggingface.co/learn/cookbook/grpo_vllm_online_training)
- [Qwen-3 4B GRPO using Unsloth + vLLM](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_%284B%29-GRPO.ipynb)