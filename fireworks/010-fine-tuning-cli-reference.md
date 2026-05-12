---
title: Training Overview
url: https://docs.fireworks.ai/fine-tuning/cli-reference
source: sitemap
fetched_at: 2026-04-27T20:15:35.974292526-03:00
rendered_js: false
word_count: 375
summary: This document serves as a comprehensive guide on using the Eval Protocol CLI to launch Reinforcement Fine-Tuning (RFT) jobs, detailing installation prerequisites and numerous customization flags available via the `eval-protocol create rft` command.
tags:
    - eval-protocol
    - rft-job
    - cli-guide
    - fireworks-ai
    - model-tuning
    - command-line
category: tutorial
optimized: true
optimized_at: 2026-04-27T23:27:00Z
---
The Eval Protocol CLI provides the fastest, most reproducible way to launch RFT jobs. This covers using `eval-protocol create rft`.

## Installation and setup

1. Upload your evaluator to Fireworks. See [[096-fine-tuning-evaluators]] if you don't have one yet.
2. Upload your dataset to Fireworks.
3. Create and launch the RFT job.

## Common CLI options

### Model and output

| Flag | Description | Default |
|------|-------------|---------|
| `--base-model` | Base model to fine-tune | — |
| `--output-model` | Name for fine-tuned model | — |

### Training parameters

| Flag | Description | Default |
|------|-------------|---------|
| `--epochs` | Number of training epochs | 1 |
| `--learning-rate` | Learning rate | 1e-4 |
| `--lora-rank` | LoRA rank | 8 |
| `--batch-size` | Batch size in tokens | 32768 |
| `--chunk-size` | Prompts rolled out per GRPO step; `-1` disables | 200 |

### Loss method

| Flag | Description | Default |
|------|-------------|---------|
| `--rl-loss-method` | RL loss method: `grpo`, `dapo`, `gspo-token` | `grpo` |
| `--rl-kl-beta` | KL beta override (grpo only) | — |

### Rollout parameters

| Flag | Description | Default |
|------|-------------|---------|
| `--temperature` | Sampling temperature | 0.7 |
| `--n` / `--response-candidates-count` | Rollouts per prompt | 8 |
| `--max-tokens` | Max tokens per response | 32768 |
| `--top-p` | Top-p sampling | 1.0 |
| `--top-k` | Top-k sampling | 40 |
| `--max-concurrent-rollouts` | Max in-flight rollouts (throughput only) | 96 |

### Remote environments

| Flag | Description |
|------|-------------|
| `--remote-server-url` | For remote rollout processing |
| `--force` | Re-upload evaluator even if unchanged |

View all options:

```bash
eval-protocol create rft --help
```

> [!note]
> For other tuning parameters — rollout concurrency, chunk size, loss method, and more — see [[044-fine-tuning-parameter-tuning]].

## Examples

**Fast experimentation** (small model, 1 epoch):

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b \
  --output-model quick-test
```

**High-quality training** (more rollouts, higher temperature):

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model high-quality-model \
  --n 8 \
  --temperature 1.0
```

**Remote environment** (for multi-turn agents):

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --remote-server-url https://your-agent.example.com \
  --output-model remote-agent
```

**Multiple epochs with custom learning rate**:

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --epochs 3 \
  --learning-rate 5e-5 \
  --output-model multi-epoch-model
```

## Using `firectl` CLI (Alternative)

For users already familiar with Fireworks `firectl`, create RFT jobs directly:

```bash
firectl rftj create \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --dataset accounts/your-account/datasets/my-dataset \
  --evaluator accounts/your-account/evaluators/my-evaluator \
  --output-model my-finetuned-model
```

Differences from `eval-protocol`:

- Requires fully qualified resource names (`accounts/...`)
- Must manually upload evaluators and datasets first
- More verbose but offers finer control
- Same underlying API as `eval-protocol`

See [[152-tools-sdks-firectl-commands-reinforcement-fine-tuning-job-create]] for all `firectl` options.