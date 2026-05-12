---
title: firectl training-shape create - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-create
source: sitemap
fetched_at: 2026-04-27T20:16:13.433378661-03:00
rendered_js: false
word_count: 319
summary: Create a new training shape by specifying base model, deployment version, and resource allocation.
tags:
    - firectl-training-shape
    - create-command
    - model-definition
    - resource-allocation
    - flags
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl training-shape create

Create a new training shape defining base model, resource allocation, parallelism, and trainer runtime.

```bash
firectl training-shape create [flags]
```

## Required Flags

| Flag | Type | Description |
|------|------|-------------|
| `--base-model` | string | Base model name or ID |
| `--deployment-shape-version` | string | Validated deployment shape version resource name |
| `--trainer-image-tag` | string | Validated trainer runtime image tag |

## Optional Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--accelerator-count` | int32 | — | Number of accelerators |
| `--accelerator-type` | string | — | Accelerator type (e.g. `NVIDIA_H200_141GB`, `NVIDIA_H100_80GB`, `NVIDIA_A100_80GB`) |
| `--cp` | int32 | server-side 1 | Context-parallel degree |
| `--description` | string | — | Description of the training shape |
| `--display-name` | string | — | Human-readable display name |
| `--dry-run` | flag | — | Print the request proto without running it |
| `--ep` | int32 | server-side 1 | Expert-parallel degree |
| `--max-context-length` | int32 | — | Max supported context length |
| `--node-count` | int32 | 1 | Node count for multi-node training |
| `--pp` | int32 | server-side 1 | Pipeline-parallel degree |
| `--sequence-parallel` | flag | — | Enable sequence parallelism |
| `--tp` | int32 | server-side 1 | Tensor-parallel degree |
| `--trainer-mode` | string | — | Trainer mode: `policy_trainer`, `forward_only`, or `lora_trainer` |
| `--training-shape-id` | string | — | Training shape ID (auto-generated if not set) |
| `-o, --output` | Output | `text` | Output format: `text`, `json`, or `flag` |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl training-shape create --base-model llama-v2-7b --deployment-shape-version accounts/fireworks/deploymentShapes/rft-qwen3-4b/versions/ra6uiv8w --trainer-image-tag 0.24.10

firectl training-shape create --base-model accounts/fireworks/models/llama-v2-7b --deployment-shape-version accounts/fireworks/deploymentShapes/my-shape/versions/v1 --trainer-image-tag 0.24.10 --accelerator-count 8 --max-context-length 4096 --node-count 1

firectl training-shape create --base-model qwen3-30b-a3b-instruct --deployment-shape-version accounts/fireworks/deploymentShapes/rft-qwen3-30b/versions/v1 --trainer-image-tag 0.32.9 --trainer-mode forward_only --tp 2 --pp 1 --accelerator-type NVIDIA_H200_141GB
```

#firectl-training-shape #create-command #cli #fine-tuning
