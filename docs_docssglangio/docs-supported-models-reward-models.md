---
title: Reward models - SGLang Documentation
url: https://docs.sglang.io/docs/supported-models/reward_models
source: sitemap
fetched_at: 2026-05-11T05:48:04.284890757-03:00
rendered_js: false
word_count: 154
summary: This document provides an overview and technical configuration requirements for deploying reward models within the SGLang framework to support reinforcement learning and classification tasks.
tags:
    - reward-models
    - rlhf
    - model-deployment
    - sequence-classification
    - sglang
    - machine-learning-pipelines
category: reference
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

These models output a scalar reward score or classification result, often used in reinforcement learning or content moderation tasks. They are executed with `--is-embedding` and some may require `--trust-remote-code`.

## Example launch Command

## Supported models

Model Family (Reward)Example HuggingFace IdentifierDescription**Llama (3.1 Reward / `LlamaForSequenceClassification`)**`Skywork/Skywork-Reward-Llama-3.1-8B-v0.2`Reward model (preference classifier) based on Llama 3.1 (8B) for scoring and ranking responses for RLHF.**Gemma 2 (27B Reward / `Gemma2ForSequenceClassification`)**`Skywork/Skywork-Reward-Gemma-2-27B-v0.2`Derived from Gemma‑2 (27B), this model provides human preference scoring for RLHF and multilingual tasks.**InternLM 2 (Reward / `InternLM2ForRewardMode`)**`internlm/internlm2-7b-reward`InternLM 2 (7B)–based reward model used in alignment pipelines to guide outputs toward preferred behavior.**Qwen2.5 (Reward - Math / `Qwen2ForRewardModel`)**`Qwen/Qwen2.5-Math-RM-72B`A 72B math-specialized RLHF reward model from the Qwen2.5 series, tuned for evaluating and refining responses.**Qwen2.5 (Reward - Sequence / `Qwen2ForSequenceClassification`)**`jason9693/Qwen2.5-1.5B-apeach`A smaller Qwen2.5 variant used for sequence classification, offering an alternative RLHF scoring mechanism.