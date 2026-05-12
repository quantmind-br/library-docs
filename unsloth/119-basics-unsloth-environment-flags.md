---
title: Unsloth Environment Flags
url: https://unsloth.ai/docs/basics/unsloth-environment-flags.md
source: llms
fetched_at: 2026-04-27T18:15:13.981421537-03:00
rendered_js: false
word_count: 221
summary: This document provides a reference table detailing various environment variables available in the Unsloth framework and explains the specific purpose of each flag, such as controlling logging, compilation behavior, and generation modes.
tags:
    - unsloth-environment
    - flags
    - configuration
    - logging
    - torch-compile
    - model-tuning
category: reference
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Unsloth Environment Flags

Reference table of all Unsloth environment variables for controlling logging, compilation, precision, and generation behavior.

## Environment Variables

| Variable | Purpose |
|---|---|
| `UNSLOTH_RETURN_LOGITS` = `"1"` | Forcibly returns logits — useful for evaluation. |
| `UNSLOTH_COMPILE_DISABLE` = `"1"` | Disables auto compiler; helps debug incorrect finetune results. |
| `UNSLOTH_DISABLE_FAST_GENERATION` = `"1"` | Disables fast generation for generic models. |
| `UNSLOTH_ENABLE_LOGGING` = `"1"` | Enables auto compiler logging — shows which functions are compiled. |
| `UNSLOTH_FORCE_FLOAT32` = `"1"` | Use float32 instead of float16 mixed precision on float16 machines. Useful for Gemma 3. |
| `UNSLOTH_STUDIO_DISABLED` = `"1"` | Disables extra features. |
| `UNSLOTH_COMPILE_DEBUG` = `"1"` | Extremely verbose `torch.compile` logs. |
| `UNSLOTH_COMPILE_MAXIMUM` = `"0"` | Maximum `torch.compile` optimizations — not recommended. |
| `UNSLOTH_COMPILE_IGNORE_ERRORS` = `"1"` | Turn off to enable fullgraph parsing. |
| `UNSLOTH_FULLGRAPH` = `"0"` | Enable `torch.compile` fullgraph mode. |
| `UNSLOTH_DISABLE_AUTO_UPDATES` = `"1"` | Forces no updates to `unsloth-zoo`. |

## Corrupted Model Uploads

If uploads appear corrupted (unlikely), try loading with exact model name:

```python
model, tokenizer = FastVisionModel.from_pretrained(
    "Qwen/Qwen2-VL-7B-Instruct",
    use_exact_model_name = True,
)
```

#unsloth #environment-flags #configuration #torch-compile
