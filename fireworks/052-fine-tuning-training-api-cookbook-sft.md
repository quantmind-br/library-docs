---
title: 'Cookbook: SFT - Fireworks AI Docs'
url: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/sft
source: sitemap
fetched_at: 2026-04-27T20:15:19.988957243-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - sft
    - fine-tuning
    - model-training
    - cookbook-recipe
category: tutorial
word_count: 264
---
## What this is

Supervised Fine-Tuning (SFT) trains the model to produce desired outputs by minimizing cross-entropy loss on (prompt, response) pairs. The cookbook's `sft_loop` recipe handles data loading, tokenization, batching, gradient accumulation, and checkpointing automatically.

## Using the recipe

```
from training.recipes.sft_loop import Config, main
from training.utils import InfraConfig

cfg = Config(
    log_path="./sft_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/training_data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    max_seq_len=4096,
    epochs=1,
    batch_size=4,
    learning_rate=1e-5,
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
)

main(cfg)
```

## Dataset format

SFT datasets use the standard messages format (JSONL with one example per line):

```
{"messages": [
  {"role": "user", "content": "What is the capital of France?"},
  {"role": "assistant", "content": "The capital of France is Paris."}
]}
```

Multi-turn conversations are supported:

```
{"messages": [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello"},
  {"role": "assistant", "content": "Hi! How can I help?"},
  {"role": "user", "content": "What is 2+2?"},
  {"role": "assistant", "content": "2+2 = 4"}
]}
```

The recipe automatically tokenizes conversations using the chat template, setting token weights to `0.0` for prompt tokens and `1.0` for response tokens.

### Vision datasets

Use multimodal `content` arrays with `image_url` objects in your JSONL, and specify a VLM training shape and tokenizer. See [[062-fine-tuning-training-api-vision-inputs]] for dataset format details and a full walkthrough.

## Checkpointing and resume

The `sft_loop` recipe manages the trainer-side loop only — it does not create a deployment or run weight sync during training. It exposes DCP checkpointing and resume controls:

```
from training.utils import InfraConfig, WandBConfig

cfg = Config(
    log_path="./sft_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/training_data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    max_seq_len=4096,
    epochs=1,
    batch_size=4,
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
    dcp_save_interval=50,
    init_from_checkpoint="previous-job-id:step-100",  # optional
    wandb=WandBConfig(entity="my-team", project="sft-experiment"),
)

main(cfg)
```

The recipe uses `checkpoint_utils.resolve_resume()` to automatically restore from the last saved state on restart.

> [!warning]
> DCP checkpoints are disabled by default (`dcp_save_interval=0`). To enable resume, set `dcp_save_interval` to a positive value (e.g., `50`).

## Operational guidance

- **Set `infra.training_shape_id`** — cookbook trainer launches use training shapes.
- **Only one trainer job needed** — SFT does not require a reference trainer.
- **The current recipe does not provision a deployment** — use the API directly for deployment-side evaluation or weight sync during SFT.
- **Use `batch_size`** to control the number of examples per optimizer step.
- **Gradient accumulation normalization defaults to `None`** — the SFT loss is already normalized client-side; adding server-side normalization would double-normalize gradients.

<!--THE END-->