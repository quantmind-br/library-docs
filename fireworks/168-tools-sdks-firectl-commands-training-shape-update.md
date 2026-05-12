---
title: firectl training-shape update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-update
source: sitemap
fetched_at: 2026-04-27T20:16:12.642976962-03:00
rendered_js: false
word_count: 284
summary: This document describes the command structure and available flags for the `firectl training-shape update` command, detailing parameters for configuring a training shape resource.
tags:
    - command-line-interface
    - training-shape
    - update
    - flags
    - fireworks
    - configuration
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl training-shape update

Update a training shape resource configuration.

```
firectl training-shape update [flags]
```

## Examples

```bash
firectl training-shape update my-shape --trainer-image-tag 0.24.11
firectl training-shape update my-shape --trainer-mode forward_only --node-count 2 --tp 2 --pp 4
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--accelerator-count` | int32 | | Number of accelerators |
| `--accelerator-type` | string | | Accelerator type (e.g. `NVIDIA_H200_141GB`, `NVIDIA_H100_80GB`) |
| `--base-model-weight-precision` | string | | Base model weight precision (e.g. `BFLOAT16`, `FP8`) |
| `--cp` | int32 | server-side 1 | Context-parallel degree |
| `--deployment-shape-version` | string | | Validated deployment shape version resource name |
| `--description` | string | | Description of the training shape |
| `--display-name` | string | | Human-readable display name |
| `--dry-run` | | | Print the request proto without running it |
| `--ep` | int32 | server-side 1 | Expert-parallel degree |
| `--max-context-length` | int32 | | Max supported context length |
| `--node-count` | int32 | | Node count for multi-node training |
| `-o, --output` | Output | `text` | Set the output format to `text`, `json`, or `flag` |
| `--pp` | int32 | server-side 1 | Pipeline-parallel degree |
| `--sequence-parallel` | | | Enable sequence parallelism |
| `--tp` | int32 | server-side 1 | Tensor-parallel degree |
| `--trainer-image-tag` | string | | Validated trainer runtime image tag |
| `--trainer-mode` | string | | Trainer mode: `policy_trainer` or `forward_only` |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #training-shape #command-line #reference
