---
title: firectl deployment create - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-create
source: sitemap
fetched_at: 2026-04-27T20:16:48.711588195-03:00
rendered_js: false
word_count: 463
summary: This document details the `firectl deployment create` command and its associated flags, explaining how users can create a new model deployment with various configuration options.
tags:
    - deployment-create
    - firectl
    - command-line
    - configuration
    - api-flags
    - autoscaling
category: reference
optimized: true
optimized_at: 2026-04-27T23:16:48Z
---
# firectl deployment create

Create a new model deployment with configuration options for compute, scaling, and routing.

```bash
firectl deployment create [flags]
```

## Examples

```bash
firectl deployment create falcon-7b
firectl deployment create accounts/fireworks/models/falcon-7b
firectl deployment create falcon-7b --file=/path/to/deployment-config.json
firectl deployment create falcon-7b --deployment-shape=falcon-7b-shape
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--accelerator-count` | int32 | Number of accelerators per replica |
| `--accelerator-type` | string | Accelerator type: `NVIDIA_A100_80GB`, `NVIDIA_H100_80GB`, `NVIDIA_H200_141GB`, `AMD_MI300X_192GB` |
| `-c`, `--cluster-id` | string | Fireworks cluster ID |
| `--deployment-id` | string | Deployment ID (auto-generated if not specified) |
| `--deployment-shape` | string | Deployment shape to use |
| `--deployment-template` | string | Deployment template to use |
| `--description` | string | Deployment description |
| `--direct-route-api-keys` | stringArray | API keys for direct route (enterprise only) |
| `--direct-route-type` | string | Direct route bypass type: `INTERNET`, `GCP_PRIVATE_SERVICE_CONNECT`, `AWS_PRIVATELINK` (enterprise only) |
| `--disable-speculative-decoding` | | Disable speculative decoding |
| `--display-name` | string | Human-readable name (< 64 characters) |
| `--draft-model` | string | Draft model for speculative decoding |
| `--draft-token-count` | int32 | Tokens to generate per step for speculative decoding |
| `--dry-run` | | Print request proto without executing |
| `--enable-addons` | | Enable addons for this deployment |
| `--enable-session-affinity` | | Enable sticky routing based on 'user' field (enterprise only) |
| `--file` | string | Path to JSON configuration file |
| `--load-targets` | Map | Autoscaling load metric names to target utilization factors |
| `--long-prompt` | | Optimize for long prompts |
| `--max-context-length` | int32 | Maximum context length (0 = model default) |
| `--max-replica-count` | int32 | Maximum replicas (defaults to 1 if min > 0) |
| `--max-with-revocable-replica-count` | int32 | Maximum replicas including revocable ones |
| `--min-replica-count` | int32 | Minimum replicas (auto-scales between min and max) |
| `--ngram-speculation-length` | int32 | N-gram speculation input sequence length |
| `--precision` | string | Serving precision: `FP8`, `FP16`, `FP4`, `BF16` |
| `--region` | string | Placement: `global`, region group (`us`), or specific region (`us-iowa-1`) |
| `--scale-down-window` | duration | Autoscaler wait before scaling down (default: 10m) |
| `--scale-to-zero-window` | duration | Idle time before scale-to-zero (default: 1h) |
| `--scale-up-window` | duration | Autoscaler wait before scaling up (default: 30s) |
| `--validate-only` | | Validate without creating |
| `--wait` | | Wait until deployment is ready |
| `--wait-timeout` | duration | Maximum wait time (default: 1h0m0s) |
| `-o`, `--output` | Output | Output format: `text`, `json`, `flag` (default: text) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID (reads from `~/.fireworks/auth.ini` if not specified) |
| `--api-key` | string | API key for authentication |
| `-p`, `--profile` | string | Auth and settings profile to use |
