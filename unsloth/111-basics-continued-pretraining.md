---
title: Continued Pretraining
url: https://unsloth.ai/docs/basics/continued-pretraining.md
source: llms
fetched_at: 2026-04-27T18:15:15.616960257-03:00
rendered_js: false
word_count: 316
summary: This document explains Continued Pretraining (CPT), which is the process of steering large language models to understand new domains or out-of-distribution knowledge beyond their initial massive pretraining. It details advanced features for CPT, including loading saved LoRA adapters and fine-tuning specific matrices like `lm_head` and `embed_tokens`.
tags:
    - continued-pretraining
    - language-model
    - finetuning
    - lora-adapters
    - unsloth
    - llm-steering
category: concept
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Continued Pretraining

## What is Continued Pretraining?

Continued or continual pretraining (CPT) steers a language model to understand new or out-of-distribution knowledge domains. Base models (e.g. Llama-3 8B pretrained on 15T tokens) may be undertrained in specific languages or domains (law, medicine, etc.). CPT makes the model learn new tokens or datasets.

## Notebooks

- [Text completion notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_\(7B\)-Text_Completion.ipynb) — continued pretraining / raw text
- [Continued pretraining notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-CPT.ipynb) — learning another language

Blog post: [unsloth.ai/blog/contpretraining](https://unsloth.ai/blog/contpretraining)

## Advanced Features

### Loading LoRA adapters for continued finetuning

Load a previously saved LoRA adapter to continue training. The optimizer state will be reset. To also restore optimizer states, see the section below.

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "LORA_MODEL_NAME",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)
trainer = Trainer(...)
trainer.train()
```

### Finetuning `lm_head` and `embed_tokens` matrices

Add `lm_head` and `embed_tokens` to the target modules. On Colab, Llama-3 8B may OOM with both — if so, add only `lm_head`.

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",
                      "lm_head", "embed_tokens",],
    lora_alpha = 16,
)
```

Use 2 different learning rates — a 2-10x smaller one for `lm_head` / `embed_tokens`:

```python
from unsloth import UnslothTrainer, UnslothTrainingArguments

trainer = UnslothTrainer(
    ....
    args = UnslothTrainingArguments(
        ....
        learning_rate = 5e-5,
        embedding_learning_rate = 5e-6, # 2-10x smaller than learning_rate
    ),
)
```

#continued-pretraining #finetuning #lora-adapters #unsloth
