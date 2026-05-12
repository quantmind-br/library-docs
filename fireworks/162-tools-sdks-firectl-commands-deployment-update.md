---
title: firectl deployment update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-update
source: sitemap
fetched_at: 2026-04-27T20:16:51.47862629-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - deployment-update
    - cli-flags
    - fireworks-cli
    - resource-management
    - autoscaling-config
category: reference
word_count: 396
---
Modify an existing deployment via `firectl deployment update [flags]`.

## Examples

```bash
firectl deployment update my-deployment
firectl deployment update accounts/my-account/deployments/my-deployment
firectl deployment update my-deployment --file=/path/to/deployment.json
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--accelerator-count` | int32 | Number of accelerators per replica |
| `--accelerator-type` | string | Accelerator type: `NVIDIA_A100_80GB`, `NVIDIA_H100_80GB`, `NVIDIA_H200_141GB`, `AMD_MI300X_192GB` |
| `--deployment-shape` | string | Deployment shape to use |
| `--description` | string | Description of the deployment |
| `--direct-route-api-keys` | stringArray | API keys for the direct route (enterprise only) |
| `--direct-route-type` | string | Bypass the API gateway: `INTERNET`, `GCP_PRIVATE_SERVICE_CONNECT`, `AWS_PRIVATELINK` (enterprise only) |
| `--display-name` | string | Human-readable name; must be under 64 characters |
| `--draft-model` | string | Draft model for speculative decoding |
| `--draft-token-count` | int32 | Tokens to generate per speculative step |
| `--dry-run` | flag | Print the request proto without running it |
| `--enable-addons` | flag | Enable addons for this deployment |
| `--enable-session-affinity` | flag | Enable sticky routing based on the `user` field (enterprise only) |
| `--load-targets` | Map | Autoscaling load metric names → target utilization factors |
| `--long-prompt` | flag | Optimize for long prompts |
| `--max-context-length` | int32 | Maximum context length; defaults to model's default if 0 or unset |
| `--max-replica-count` | int32 | Maximum replicas |
| `--max-with-revocable-replica-count` | int32 | Maximum replicas including revocable replicas |
| `--min-replica-count` | int32 | Minimum replicas; deployment auto-scales between min and max |
| `--ngram-speculation-length` | int32 | Length of previous input sequence for N-gram speculation |
| `--precision` | string | Serving precision: `FP8`, `FP16`, `FP4`, `BF16` |
| `--region` | string | Placement: `global`, region group (e.g. `us`), or specific region (e.g. `us-iowa-1`) |
| `--scale-down-window` | duration | Wait time before scaling down after decreased load (default `10m`) |
| `--scale-to-zero-window` | duration | Wait time before scaling to zero replicas (default `1h`) |
| `--scale-up-window` | duration | Wait time before scaling up after increased load (default `30s`) |
| `-o`, `--output` | Output | Output format: `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID; falls back to `~/.fireworks/auth.ini` |
| `--api-key` | string | API key for authentication |
| `-p`, `--profile` | string | Auth and settings profile to use |
