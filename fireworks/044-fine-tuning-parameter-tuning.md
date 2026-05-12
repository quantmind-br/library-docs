---
title: Parameter Tuning - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/parameter-tuning
source: sitemap
fetched_at: 2026-04-27T20:15:38.036632847-03:00
rendered_js: false
word_count: 297
summary: This document explains the two main categories of reinforcement fine-tuning parameters—training and rollout/sampling—and details how these settings influence model learning, particularly focusing on zero-variance group filtering.
tags:
    - reinforcement-fine-tuning
    - model-training
    - parameter-tuning
    - rollout-parameters
    - zero-variance-filtering
    - policy-optimization
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Reinforcement fine-tuning uses two parameter categories: **training parameters** (how the model learns) and **rollout/sampling parameters** (how the model generates responses during training). Most experiments converge well with defaults — adjust only when you have a clear hypothesis from training metrics and reward curves.

## Training Parameters

Core parameters governing how your model learns.

## Loss Method

Controls the policy optimization algorithm used during training.

## Rollout (Sampling) Parameters

Controls how the model generates responses during training rollouts.

## Zero-Variance Group Filtering

During each training iteration, the model generates K response candidates per prompt (controlled by `--response-candidates-count` or `--n`). Your evaluator scores each candidate. If **all K candidates for a prompt receive the same score**, that group provides no learning signal — the model cannot distinguish better from worse responses.

> [!warning]
> Managed RFT automatically filters out zero-variance groups. This applies to all loss methods (GRPO, DAPO, and GSPO-token), not just DAPO.

Key behaviors:
- Filtered prompts are **dropped from the batch**, not replaced. Your effective batch size may be smaller than configured when many groups are homogeneous.
- Filtering happens at both the full-group level and at the chunk level within groups.
- If your evaluator returns the same score for all rollouts across most prompts, training will make limited progress and may trigger early stopping.

**To reduce zero-variance groups:**
- Increase `--temperature` (e.g., 0.8–1.0) for more diverse responses
- Increase `--response-candidates-count` for more candidates
- Ensure your evaluator returns a range of scores, not just 0 and 1

## Parameter Interactions

Parameters don't work in isolation — they interact in important ways.

## Tuning Strategies

Best practices for adjusting parameters to achieve your training goals.

## Next Steps

For the full parameter reference and detailed interactions, see the cookbook skill: [`skills/dev/references/rft/parameter-tuning.md`](https://github.com/fw-ai/cookbook/blob/main/skills/dev/references/rft/parameter-tuning.md).

#reinforcement-fine-tuning #parameter-tuning #zero-variance-filtering #rollout-parameters
