---
title: firectl reinforcement-fine-tuning-job create - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-create
source: sitemap
fetched_at: 2026-04-27T20:16:37.627233-03:00
rendered_js: false
word_count: 571
summary: This document describes the `firectl reinforcement-fine-tuning-job create` command and details all available flags for initiating a reinforcement fine-tuning job, allowing users to specify models, datasets, training parameters, and various integration options.
tags:
    - command
    - reinforcement-fine-tuning
    - create
    - flags
    - model-training
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T23:16:37Z
---
# firectl reinforcement-fine-tuning-job create

Create a reinforcement fine-tuning job with evaluator, RL parameters, and inference configuration.

```bash
firectl reinforcement-fine-tuning-job create [flags]
```

## Examples

```bash
firectl reinforcement-fine-tuning-job create \
    --base-model llama-v3-8b-instruct \
    --dataset sample-dataset \
    --epochs 5 \
    --output-model name-of-the-trained-model \
    --evaluator accounts/my-account/evaluators/abc123

# Create from source job:
firectl reinforcement-fine-tuning-job create \
    --source-job my-previous-job \
    --output-model new-model
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--base-model` | string | Base model (mutually exclusive with `--warm-start-from`) |
| `--batch-size` | int32 | Batch size in tokens per training step |
| `--batch-size-samples` | int32 | Samples per gradient update (0 = based on batch-size) |
| `--chunk-size` | int32 | Minimum chunk size to split dataset before RL flow (-1 to disable, default: 200) |
| `--dataset` | string | Dataset (**Required**) |
| `--dry-run` | | Print request proto without executing |
| `--epochs` | int32 | Number of epochs (default: 1) |
| `--evaluator` | string | Evaluator resource name (**Required**) |
| `--extra-body` | string | Additional inference parameters as JSON (e.g., `'{"stop": ["\n"]}'`) |
| `--gradient-accumulation-steps` | int32 | Steps to accumulate gradients before updating (default: 1) |
| `--job-id` | string | Job ID (auto-generated if not set) |
| `--learning-rate` | float32 | Learning rate (default: 0.0001) |
| `--learning-rate-warmup-steps` | int32 | Warmup steps for learning rate |
| `--lora-rank` | int32 | LoRA rank (default: 8) |
| `--max-concurrent-evaluations` | int32 | Maximum concurrent evaluations (defaults to evaluator config) |
| `--max-concurrent-rollouts` | int32 | Maximum concurrent rollouts (defaults to evaluator config) |
| `--max-context-length` | int32 | Maximum token length for sequences (shorter concatenated, longer truncated) |
| `--max-inference-replica-count` | int32 | Maximum replicas for batch inference (default: 1) |
| `--max-output-tokens` | int32 | Maximum tokens to generate in response |
| `--optimizer-weight-decay` | float32 | Weight decay / L2 regularization (default: 0.01) |
| `--output-model` | string | Output model name |
| `--quiet` | | Print only errors |
| `--response-candidates-count` | int32 | Response candidates to generate per input |
| `--rl-kl-beta` | float32 | Override KL beta for GRPO-like methods (must be >= 0) |
| `--rl-loss-method` | string | RL loss method: `grpo`, `dapo`, `gspo-token` |
| `--source-job` | string | Source RFT job to copy configuration from |
| `--temperature` | float32 | Randomness of token selection during generation |
| `--top-k` | int32 | Top-k sampling parameter |
| `--top-p` | float32 | Top-p (nucleus) sampling threshold |
| `--warm-start-from` | string | Model to warm start from (mutually exclusive with `--base-model`) |
| `--aws-credentials-secret` | string | AWS credentials secret (mutually exclusive with `--aws-iam-role`) |
| `--aws-iam-role` | string | AWS IAM role ARN (mutually exclusive with `--aws-credentials-secret`) |
| `--azure-credentials-secret` | string | Azure credentials secret |
| `--azure-managed-identity-client-id` | string | Azure managed identity client ID for Workload Identity Federation |
| `--azure-tenant-id` | string | Azure tenant ID (required with `--azure-managed-identity-client-id`) |
| `--wandb` | | Enable Weights & Biases |
| `--wandb-api-key` | string | WANDB_API_KEY (**Required** if any WandB flag is set) |
| `--wandb-entity` | string | WANDB_ENTITY (**Required** if any WandB flag is set) |
| `--wandb-project` | string | WANDB_PROJECT (**Required** if any WandB flag is set) |
| `-o`, `--output` | Output | Output format: `text`, `json`, `flag` (default: text) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID (reads from `~/.fireworks/auth.ini` if not specified) |
| `--api-key` | string | API key for authentication |
| `-p`, `--profile` | string | Auth and settings profile to use |
