---
title: Fine Tuning Rft Cost Estimator
url: https://docs.fireworks.ai/fine-tuning/rft-cost-estimator
source: sitemap
fetched_at: 2026-04-27T20:15:49.708537791-03:00
rendered_js: false
word_count: 429
summary: Interactive cost calculator and formulas for estimating Reinforcement Fine-Tuning (RFT) job expenses based on model size, dataset, and rollout parameters.
tags:
    - cost-calculator
    - rft-pricing
    - training-estimation
    - gpu-hours
    - optimization-tips
    - parameter-impact
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# RFT Cost Estimator

RFT jobs are billed based on **GPU-seconds** consumed during training. The calculator uses these formulas:

1. **Total tokens**: Prompts × Epochs × Response candidates × (Max tokens × 0.6)
2. **GPU hours**: (Total tokens ÷ 1M) × (GPU hours per million tokens range, varies by model size)
3. **Cost**: GPU hours × GPU rate per hour

**Training time** = GPU hours ÷ Number of GPUs

## How parameters affect cost

Baseline: 500 prompts, 1 epoch, n=4, 2048 max tokens

| Change | Cost impact | Explanation |
|--------|--------------|-------------|
| Double dataset size (1000 prompts) | ~2× | Linear scaling with dataset size |
| Double rollouts (n=8) | ~2× | Linear scaling with rollout count |
| Double max tokens (4096) | ~1.5–2× | More tokens per rollout |
| Add epoch (epochs=2) | ~2× | Full additional pass through data |
| Double LoRA rank (16 → 32) | ~1.2–1.5× | More trainable parameters |
| Halve max tokens (1024) | ~0.5–0.7× | Fewer tokens generated |
| Halve rollouts (n=2) | ~0.5× | Fewer rollouts but less learning signal |

## Cost formula

```
Cost = GPU-hours × Price per GPU-hour
```

Where:

```
GPU-hours ≈ Num GPUs × (Prompts × Epochs × Rollouts (n) × Avg tokens per rollout) ÷ Throughput (tokens/sec) ÷ 3600
```

### Key variables

| Variable | Description | How to control |
|----------|-------------|----------------|
| Num GPUs | GPUs required for the model | Determined by model size |
| Prompts | Number of rows in your dataset | Your dataset size |
| Epochs | Passes through the dataset | `--epochs` flag (default: 1) |
| Response candidates (n) | Responses generated per prompt | `--n` flag (default: 4) |
| Avg tokens per rollout | Average response length | `--max-tokens` flag (default: 2048) |
| Throughput | Tokens generated per second | Determined by model + hardware |

## Cost optimization tips

- **Start small**: Experiment with smaller models before scaling
- **Reduce rollouts**: Lower `--n` if you can accept less learning signal
- **Shorter responses**: Set `--max-tokens` to minimum needed
- **Fewer epochs**: Start with 1 epoch, only add more if needed
- **Early stopping**: Cancel jobs that aren't progressing—the checkpoint from last completed step is still usable

## Monitoring costs during training

Cost information is only available after your job completes:

1. **Dashboard**: Final cost displays on the RFT job page once training finishes at [Fireworks Dashboard](https://app.fireworks.ai)
2. **Training progress**: While running, monitor elapsed time and estimated completion in the job overview
3. **Early stopping**: Cancel a job early if needed—the checkpoint from the last completed step is still usable. Final cost is calculated based on GPU-seconds consumed up to the cancellation point.

#cost-calculator #rft-pricing #gpu-hours
