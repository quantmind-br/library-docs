---
title: Weight sync - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/weight-sync
source: sitemap
fetched_at: 2026-04-27T20:15:13.844429578-03:00
rendered_js: false
word_count: 305
summary: This document explains the mechanism by which policy weights are synchronized between an RL trainer and its deployment using a shared GCS bucket, detailing how the `WeightSyncScope` controls resource ownership for different operational needs.
tags:
    - rl-training
    - weight-sync
    - gcs-bucket
    - deployconfig
    - per-trainer
    - deployment-scope
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
During RL training, policy weights update step-by-step and the inference deployment needs updated weights to generate the next batch of rollouts. The cookbook wires this via a **shared GCS bucket**:

- The **trainer** writes a fresh checkpoint to the bucket after each optimizer step (or on a configurable cadence).
- The **deployment** watches the same bucket and swaps in new weights without a pod restart.

## Normal Flow

Use the cookbook's [`setup_infra`]([[051-fine-tuning-training-api-cookbook-rl#provision-resources-with-setup_infra|RL cookbook]]#provision-resources-with-setup_infra) entrypoint — it creates the trainer, then creates the deployment pointing at it, with no extra wiring.

> [!tip]
> The default `DeployConfig(weight_sync_scope=WeightSyncScope.PER_TRAINER)` is what you want for almost every run.

If you misconfigure the pairing, the server rejects the `CreateDeployment` or `CreateRlorTrainerJob` call up front with an error that links back here.

## `WeightSyncScope`: Who Owns the Bucket

`DeployConfig.weight_sync_scope` controls which resource must be created first:

| Scope | Bucket owner | Use when |
|---|---|---|
| `PER_TRAINER` (default) | Trainer — one bucket per run | Single run, or one trainer feeding multiple deployments (sampler + held-out eval) |
| `PER_DEPLOYMENT` | Deployment — stable bucket across trainer runs | Long-lived deployment, many sequential trainers, can't tolerate deployment restarts between runs |

> [!warning]
> The two scopes are mutually exclusive for the same trainer ↔ deployment pair — don't mix them.

`setup_infra` dispatches on this single field and wires the rest correctly.

## Diagnosing Errors

The control plane catches scope-mix mistakes at create time and returns an error that names both resources and suggests the fix. For the full list of server error strings and per-error recovery steps, see the cookbook skill: [`skills/dev/references/rl/hotload.md`](https://github.com/fw-ai/cookbook/blob/main/skills/dev/references/rl/hotload.md). It also covers trainer retention, the unified promote API, and runtime bucket-mismatch warnings.

## See Also

- [[051-fine-tuning-training-api-cookbook-rl|RL cookbook]] — end-to-end RL flow, including weight-sync cadence knobs
- [[049-fine-tuning-training-api-cookbook-checkpoints|Checkpoints]] — base/delta, promote

#weight-sync #rl-training #gcs-bucket #deployconfig
