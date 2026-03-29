---
title: Reward Models — SGLang
url: https://docs.sglang.io/supported_models/reward_models.html
source: crawler
fetched_at: 2026-02-04T08:47:04.028711752-03:00
rendered_js: false
word_count: 153
summary: This document provides instructions for deploying reward models used in RLHF and content moderation, detailing specific launch commands and a list of supported model architectures.
tags:
    - reward-models
    - rlhf
    - model-deployment
    - sequence-classification
    - inference-server
    - tensor-parallelism
category: reference
---

## Reward Models[#](#reward-models "Link to this heading")

These models output a scalar reward score or classification result, often used in reinforcement learning or content moderation tasks.

Important

They are executed with `--is-embedding` and some may require `--trust-remote-code`.

## Example launch Command[#](#example-launch-command "Link to this heading")

```
python3-msglang.launch_server\
--model-pathQwen/Qwen2.5-Math-RM-72B\ # example HF/local path
--is-embedding\
--host0.0.0.0\
--tp-size=4\ # set for tensor parallelism
--port30000\
```

## Supported models[#](#supported-models "Link to this heading")

Model Family (Reward)

Example HuggingFace Identifier

Description

**Llama (3.1 Reward / `LlamaForSequenceClassification`)**

`Skywork/Skywork-Reward-Llama-3.1-8B-v0.2`

Reward model (preference classifier) based on Llama 3.1 (8B) for scoring and ranking responses for RLHF.

**Gemma 2 (27B Reward / `Gemma2ForSequenceClassification`)**

`Skywork/Skywork-Reward-Gemma-2-27B-v0.2`

Derived from Gemma‑2 (27B), this model provides human preference scoring for RLHF and multilingual tasks.

**InternLM 2 (Reward / `InternLM2ForRewardMode`)**

`internlm/internlm2-7b-reward`

InternLM 2 (7B)–based reward model used in alignment pipelines to guide outputs toward preferred behavior.

**Qwen2.5 (Reward - Math / `Qwen2ForRewardModel`)**

`Qwen/Qwen2.5-Math-RM-72B`

A 72B math-specialized RLHF reward model from the Qwen2.5 series, tuned for evaluating and refining responses.

**Qwen2.5 (Reward - Sequence / `Qwen2ForSequenceClassification`)**

`jason9693/Qwen2.5-1.5B-apeach`

A smaller Qwen2.5 variant used for sequence classification, offering an alternative RLHF scoring mechanism.