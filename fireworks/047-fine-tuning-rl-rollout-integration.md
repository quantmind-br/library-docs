---
title: RL Rollouts with Your Own Trainer - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/rl-rollout-integration
source: sitemap
fetched_at: 2026-04-27T20:15:30.235665543-03:00
rendered_js: false
word_count: 402
summary: This guide details the end-to-end process of using Fireworks for large-scale inference during Reinforcement Learning (RL) rollouts, covering initial setup, hot-loading full and incremental model snapshots, and running subsequent inferences.
tags:
    - rl-rollout
    - hot-load
    - inference
    - snapshotting
    - fireworks-api
    - pytorch-fsdp
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# RL Rollouts with Your Own Trainer

Use Fireworks for large-scale inference during RL rollouts when you already run your own trainer (PyTorch FSDP, Megatron, custom Ray cluster, etc.).

> [!note]
> If using Fireworks-hosted RLOR trainers with `FW_HOSTED`, start from [[042-fine-tuning-full-parameter-rl-tuning|Full Parameter RL Tuning]] instead — Fireworks manages the bucket plumbing in that path.

**You own:** trainer, reward shaping, checkpoint cadence, rollout orchestration.
**Fireworks owns:** hot-load logistics, distributed weight swap, inference serving, KV cache across rollouts.

## End-to-end loop

1. Create a hot-load deployment
2. Upload and hot-load an initial **full** snapshot
3. Run rollouts against that snapshot
4. Upload and hot-load the next **incremental** snapshot
5. Run rollouts again
6. Every 20th or 30th step, publish another **full** snapshot instead of incremental
7. Repeat from step 4

## 1. Create a hot-load deployment

```bash
firectl create deployment <base_model> \
    --deployment-shape <shape_name> \
    --deployment-id <deployment_id> \
    --enable-hot-load \
    --hot-load-bucket-type S3 \
    --hot-load-bucket-url s3://<your_bucket>/<your_upload_path> \
    --region US_OHIO_1
```

Record the account ID, deployment ID, and model ID from the output for use in hot-load and rollout calls.

## 2. Upload and hot-load an initial full snapshot

### Snapshot layout

Place each snapshot under its own subdirectory keyed by `checkpoint_id`:

```
s3://<your_bucket>/<account_id>/<account_id>-<deployment_id>/<checkpoint_id>/
├── config.json
├── tokenizer.json
├── tokenizer_config.json
├── model-00000.safetensors
├── model-00001.safetensors
└── ...
```

- `checkpoint_id` is any string (e.g., `version_001`, `step_00100`)
- Checkpoint must match the base model format on HuggingFace: `config.json`, tokenizer, and safetensors weights
- Split weights into multiple safetensors files, each under ~5 GB

### Signal the snapshot is ready

Once all files are uploaded, signal Fireworks to begin loading:

```bash
curl -X POST https://api.fireworks.ai/hot_load/v1/models/hot_load \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "Content-Type: application/json" \
  -d '{ "identity": "version_001" }'
```

### Wait until replicas are ready

Poll until every replica reports readiness:

```bash
curl https://api.fireworks.ai/hot_load/v1/models/hot_load \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>"
```

Wait until:
- every replica has `readiness: true`
- every replica's `current_snapshot_identity` equals the `identity` you just signaled

## 3. Run rollouts

Use the regular OpenAI-compatible inference API with session-affinity headers for multi-turn trajectories to reuse KV cache on the same replica:

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "x-multi-turn-session-id: <trajectory_id>" \
  -H "x-session-affinity: <trajectory_id>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/<account_id>/models/<model_id>",
    "messages": [{"role": "user", "content": "..."}]
  }'
```

For rollout-time inference behavior (session affinity, prompt-cache behavior during weight swaps, MoE Router Replay), see [[081-guides-rollout-inference|Inference for RL rollouts]].

## 4. Upload and hot-load incremental snapshots

For intermediate training steps, publish an incremental snapshot using the public ARC2 format (`arc_v2`):

```bash
curl -X POST https://api.fireworks.ai/hot_load/v1/models/hot_load \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "Content-Type: application/json" \
  -d '{
    "identity": "version_002",
    "incremental_snapshot_metadata": {
      "previous_snapshot_identity": "version_001",
      "compression_format": "arc_v2"
    }
  }'
```

Poll the status endpoint until every replica reports `readiness: true` and `current_snapshot_identity == "version_002"`.

## 5. Repeat the loop

- Use a **full** snapshot for the first step and every 20th or 30th step after
- Use an **incremental** snapshot for intermediate steps
- If an incremental hot-load fails or the chain gets into a bad state, fall back to a new full snapshot
- For lower-level recovery steps, see [[046-fine-tuning-rl-rollout-debugging|Ledger & Debugging for RL Rollouts]]

#rl-rollout #hot-load #inference #snapshotting #fireworks-api #pytorch-fsdp
