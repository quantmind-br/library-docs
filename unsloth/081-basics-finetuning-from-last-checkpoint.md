---
title: Finetuning from Last Checkpoint
url: https://unsloth.ai/docs/basics/finetuning-from-last-checkpoint.md
source: llms
fetched_at: 2026-04-27T18:15:17.134701568-03:00
rendered_js: false
word_count: 247
summary: This document explains how to perform various advanced finetuning operations, including saving checkpoints at specified intervals, integrating with Weights & Biases (Wandb), and implementing early stopping within a training run.
tags:
    - finetuning
    - checkpointing
    - wandb-integration
    - early-stopping
    - training-arguments
    - trainer
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Finetuning from Last Checkpoint

## Save & Resume Checkpoints

Add `save_strategy` and `save_steps` to `TrainingArguments` — this saves a checkpoint every 50 steps to `outputs`:

```python
trainer = SFTTrainer(
    ....
    args = TrainingArguments(
        ....
        output_dir = "outputs",
        save_strategy = "steps",
        save_steps = 50,
    ),
)
```

Resume from latest checkpoint:

```python
trainer_stats = trainer.train(resume_from_checkpoint = True)
```

## Wandb Integration

```bash
pip install wandb --upgrade
wandb login <token>
```

```python
import os
os.environ["WANDB_PROJECT"] = "<name>"
os.environ["WANDB_LOG_MODEL"] = "checkpoint"
```

Add to `TrainingArguments()`:

```
report_to = "wandb",
logging_steps = 1,    # adjust as needed
save_steps = 100      # adjust as needed
run_name = "<name>"   # optional
```

Resume from a Wandb artifact:

```python
import wandb
run = wandb.init()
artifact = run.use_artifact('<username>/<Wandb-project-name>/<run-id>', type='model')
artifact_dir = artifact.download()
trainer.train(resume_from_checkpoint=artifact_dir)
```

## Early Stopping

Stops training when `eval_loss` stops decreasing. Uses `EarlyStoppingCallback`.

### Trainer Config

```python
from trl import SFTConfig, SFTTrainer
trainer = SFTTrainer(
    args = SFTConfig(
        fp16_full_eval = True,
        per_device_eval_batch_size = 2,
        eval_accumulation_steps = 4,
        output_dir = "training_checkpoints",
        save_strategy = "steps",
        save_steps = 10,
        save_total_limit = 3,
        eval_strategy = "steps",
        eval_steps = 10,
        load_best_model_at_end = True,       # REQUIRED for early stopping
        metric_for_best_model = "eval_loss",
        greater_is_better = False,           # lower loss = better
    ),
    model = model,
    tokenizer = tokenizer,
    train_dataset = new_dataset["train"],
    eval_dataset = new_dataset["test"],
)
```

### Callback

```python
from transformers import EarlyStoppingCallback
early_stopping_callback = EarlyStoppingCallback(
    early_stopping_patience = 3,     # steps to wait if loss doesn't decrease
    early_stopping_threshold = 0.0,  # min loss decrease to consider stopping (e.g. 0.01)
)
trainer.add_callback(early_stopping_callback)
```

Then train as usual: `trainer.train()`.

#finetuning #checkpointing #wandb #early-stopping #trainer
