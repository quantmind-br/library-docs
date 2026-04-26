---
title: Classifier Factory | Mistral Docs
url: https://docs.mistral.ai/resources/deprecated/finetuning/classifier_factory
source: sitemap
fetched_at: 2026-04-26T04:11:29.883013313-03:00
rendered_js: false
word_count: 832
summary: This document provides an overview of the Classifier Factory, explaining how to create, manage, and utilize custom fine-tuned classification models for various data categorization tasks.
tags:
    - classification-models
    - fine-tuning
    - machine-learning
    - jsonl
    - api-integration
    - data-labeling
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!danger] Deprecated
> This feature is deprecated and is no longer actively supported.

## Overview

In various domains and enterprises, classification models play a crucial role in enhancing efficiency, improving user experience, and ensuring compliance. These models serve diverse purposes:

- **Moderation**: Classifying unwanted content in real-time
- **Intent Detection**: Understanding user behavior and predicting next actions
- **Sentiment Analysis**: Determining emotional tone behind text data
- **Data Clustering**: Grouping similar data points for pattern recognition
- **Fraud Detection**: Identifying fraudulent transactions
- **Spam Filtering**: Filtering out spam emails
- **Recommendation Systems**: Categorizing user preferences

For this reason, we designed a friendly and easy way to make your own classifiers. Leveraging our small but highly efficient models and training methods, the Classifier Factory is both available directly in the [AI Studio](https://console.mistral.ai/build/finetuned-models) and our API.

## Dataset

To fine-tune a model, you need to provide a dataset that contains the data you want to train on, it is also recommended to have a validation dataset and a test dataset.

The dataset must be in a specific format, and you can upload it to the Mistral Cloud before launching the fine-tuning job.

Data must be stored in JSON Lines (`.jsonl`) files, which allow storing multiple JSON objects, each on a new line.

## API Endpoints

We provide two endpoints:
- `v1/classifications`: To classify raw text.
- `v1/chat/classifications`: To classify chats and multi-turn interactions.

## Classification Types

There are 2 main kinds of classification models:

- Single Target
- Multi-Target

### Single Label Classification

For single label classification, data must have the label name and the value for that corresponding label:

```json
{"label": {"name": "spam", "value": true}, "text": "Buy now and get 50% off!"}
```

### Multi Label Classification

For multiple labels, you can provide a list:

```json
{"label": {"name": "topics", "value": ["sports", "news"]}, "text": "The championship game was held yesterday"}
```

When using the result model, you will be able to retrieve the scores for the corresponding label and value.

> [!note] The files must be in JSONL format, meaning every JSON object must be flattened into a single line, and each JSON object is on a new line.

## Create and Manage Fine-tuning Jobs

To create your custom model, you need to create a fine-tuning job. You can fully manage jobs via our API, from creation, to starting, monitoring and cancellation.

A fine-tuning job corresponds to a single training run. You can create a fine-tuning job with the following parameters:

| Parameter | Description |
|-----------|-------------|
| `model` | The specific model you would like to fine-tune. The choice is `ministral-3b-latest` |
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

Once your fine-tuning job is done, you can use your fine-tuned custom model to classify your data and use it in your applications.

Below is an example of how to use a fine-tuned model to classify your data:

```python
```

You can delete a fine-tuned model if you no longer need it:

```bash
```

## Cookbooks

Explore our guides and [cookbooks](https://github.com/mistralai/cookbook) leveraging the Classifier Factory:

- [Intent Classification](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/intent_classification.ipynb): Creating a single-target, single-label, intent classification model
- [Moderation Classifier](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/moderation_classifier.ipynb): Build a single-target, multi-label, simple moderation model
- [Product Classification](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/product_classification.ipynb): Create a multi-target, single-label and multi-label, food classification model