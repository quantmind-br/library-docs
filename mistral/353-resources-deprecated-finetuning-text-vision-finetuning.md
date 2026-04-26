---
title: Text & Vision Fine-tuning | Mistral Docs
url: https://docs.mistral.ai/resources/deprecated/finetuning/text_vision_finetuning
source: sitemap
fetched_at: 2026-04-26T04:11:30.997428678-03:00
rendered_js: false
word_count: 547
summary: This document provides instructions on how to fine-tune pre-trained language and vision models by preparing custom JSONL datasets and managing training jobs via the API.
tags:
    - fine-tuning
    - machine-learning
    - model-training
    - jsonl-format
    - data-preparation
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!danger] Deprecated
> This feature is deprecated and is no longer actively supported.

Fine-tuning allows you to tailor a pre-trained language model to your specific needs by training it on your dataset. This guide explains how to fine-tune text and vision models, from preparing your data to training.

You can both finetune directly in the [AI Studio](https://console.mistral.ai/build/finetuned-models) or via our API.

## Dataset

To fine-tune a model, you need to provide a dataset that contains the data you want to train on, it is also recommended to have a validation dataset and a test dataset.

The dataset must be in a specific format, and you can upload it to the Mistral Cloud before launching the fine-tuning job.

Data must be stored in JSON Lines (`.jsonl`) files.

## SFT Dataset Format

SFT Datasets should follow an instruction-following format representing a user-assistant conversation. Each JSON data sample should either consist of only user and assistant messages or include function-calling logic.

**Conversational text only** data between user and assistant, which can be one-turn or multi-turn:
- Conversational data must be stored under the `"messages"` key as a list.
- Each list item is a dictionary containing the `"content"` and `"role"` keys. `"role"` is a string: `"system"`, `"user"`, `"assistant"` or `"tool"`.
- Loss computation is performed only on tokens corresponding to assistant messages (`"role" == "assistant"`).

While text-only fine-tuning covers multiple use cases, you can also fine-tune the vision capabilities of our models. This allows you to create models that can understand and generate responses based on both text and image inputs.

> [!note] The files must be in JSONL format, meaning every JSON object must be flattened into a single line, and each JSON object is on a new line.

## Available Models

| Type | Models |
|------|--------|
| Text Only | `open-mistral-7b`, `mistral-small-latest`, `codestral-latest`, `open-mistral-nemo`, `mistral-large-latest`, `ministral-8b-latest`, `ministral-3b-latest` |
| Vision | `pixtral-12b-latest` |

## Create and Manage Fine-tuning Jobs

To create your custom model, you need to create a fine-tuning job. You can fully manage jobs via our API, from creation, to starting, monitoring and cancellation.

A fine-tuning job corresponds to a single training run. You can create a fine-tuning job with the following parameters:

| Parameter | Description |
|-----------|-------------|
| `model` | The specific model you would like to fine-tune |
| `training_files` | A collection of training file IDs |
| `validation_files` | A collection of validation file IDs |
| `hyperparameters` | Two adjustable hyperparameters: "training_steps" and "learning_rate" |
| `auto_start` | `True`: job launched immediately after validation; `False` (default): manually start after validation |
| `integrations` | External integrations such as Weights and Biases for metrics tracking |

After creating a fine-tuning job, you can check the job status using:

```bash
```

Initially, the job status will be `"QUEUED"`. After a brief period, the status will update to `"VALIDATED"`. At this point, you can proceed to start the fine-tuning job:

```bash
```

## Use and Delete Fine-tuned Models

Once your fine-tuning job is done, you can use your fine-tuned custom model in your applications.

Below is an example of how to use a fine-tuned model to classify your data:

```python
```

You can delete a fine-tuned model if you no longer need it:

```bash
```