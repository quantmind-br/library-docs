---
title: firectl supervised-fine-tuning-job create - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/supervised-fine-tuning-job-create
source: sitemap
fetched_at: 2026-04-27T20:16:28.517037579-03:00
rendered_js: false
word_count: 498
summary: This document details the command structure and available flags for creating a supervised fine-tuning job using the `firectl` tool. It outlines various parameters that control model selection, dataset usage, training configuration, and infrastructure credentials.
tags:
    - job-creation
    - supervised-fine-tuning
    - firectl
    - training-configuration
    - model-tuning
    - command-line
category: reference
optimized: true
optimized_at: 2026-04-27T23:16:28Z
---
# firectl supervised-fine-tuning-job create

Create a supervised fine-tuning (SFT) job with LoRA or full-parameter tuning options.

```bash
firectl supervised-fine-tuning-job create [flags]
```

## Examples

```bash
firectl supervised-fine-tuning-job create \
    --base-model llama-v3-8b-instruct \
    --dataset sample-dataset \
    --output-model name-of-the-trained-model

# Create from source job:
firectl supervised-fine-tuning-job create \
    --source-job my-previous-job \
    --output-model new-model
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--base-model` | string | Base model (mutually exclusive with `--warm-start-from`) |
| `--batch-size` | int32 | Batch size in tokens per training step |
| `--batch-size-samples` | int32 | Samples per gradient update (0 = based on batch-size) |
| `--dataset` | string | Dataset (**Required**) |
| `--display-name` | string | Display name for the job |
| `--dry-run` | | Print request proto without executing |
| `--early-stop` | | Enable early stopping |
| `--epochs` | int32 | Number of training epochs |
| `--evaluation-dataset` | string | Evaluation dataset |
| `--eval-auto-carveout` | | Auto-carve evaluation dataset |
| `--full-parameter-tuning` | | Enable full parameter fine-tuning (equivalent to `--lora-rank=0`, requires bf16 precision) |
| `--gradient-accumulation-steps` | int32 | Steps to accumulate gradients before updating (default: 1) |
| `--job-id` | string | Job ID (auto-generated if not set) |
| `--learning-rate` | float32 | Learning rate |
| `--learning-rate-warmup-steps` | int32 | Warmup steps for learning rate |
| `--lora-rank` | int32 | LoRA rank (set to 0 for full parameter tuning, default: 8) |
| `--max-context-length` | int32 | Maximum token length for sequences (shorter concatenated, longer truncated) |
| `--mtp-enable` | | Enable Multi-Token Prediction layer (Deepseek finetuning only) |
| `--mtp-freeze-base-model` | | Freeze base model parameters during MTP training |
| `--mtp-num-draft-tokens` | int32 | Number of draft tokens in MTP (1-3, default: 1) |
| `--optimizer-weight-decay` | float32 | Weight decay / L2 regularization (default: 0.01) |
| `--output-model` | string | Output model name |
| `--quiet` | | Print only errors |
| `--source-job` | string | Source SFT job to copy configuration from |
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
