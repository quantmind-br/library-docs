---
title: firectl training-shape clone - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-clone
source: sitemap
fetched_at: 2026-04-27T20:16:31.756121709-03:00
rendered_js: false
word_count: 236
summary: This document describes the usage of the `firectl training-shape clone` command, which copies an existing training shape configuration while allowing users to override specific parameters via various flags.
tags:
    - training-shape-clone
    - fireworks-cli
    - configuration
    - overrides
    - command-usage
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
Copies an existing training shape and creates a new one with the same configuration. Override flags can change specific fields.

```bash
firectl training-shape clone <source-training-shape-id> [flags]
```

**Examples**

```bash
firectl training-shape clone my-source-shape --training-shape-id my-new-shape
firectl training-shape clone my-source-shape --training-shape-id my-new-shape --trainer-image-tag 0.24.11
firectl training-shape clone accounts/my-account/trainingShapes/my-source-shape \
  --training-shape-id my-new-shape --accelerator-count 16
```

| Flag | Type | Description |
|------|------|-------------|
| `--accelerator-count` | int32 | Number of accelerators (overrides source). |
| `--accelerator-type` | string | Accelerator type (overrides source). |
| `--cp` | int32 | Context-parallel degree (overrides source). |
| `--deployment-shape-version` | string | Deployment shape version (overrides source). |
| `--description` | string | Description (overrides source). |
| `--display-name` | string | Human-readable display name (overrides source). |
| `--ep` | int32 | Expert-parallel degree (overrides source). |
| `--max-context-length` | int32 | Max supported context length (overrides source). |
| `--node-count` | int32 | Node count (overrides source). |
| `--pp` | int32 | Pipeline-parallel degree (overrides source). |
| `--sequence-parallel` | flag | Enable sequence parallelism (overrides source). |
| `--tp` | int32 | Tensor-parallel degree (overrides source). |
| `--trainer-image-tag` | string | Trainer image tag (overrides source). |
| `--trainer-mode` | string | Trainer mode (overrides source). |
| `--training-shape-id` | string | **Required.** ID for the new training shape. |

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |