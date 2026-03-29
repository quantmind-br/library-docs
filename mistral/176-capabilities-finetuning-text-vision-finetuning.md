---
title: Text & Vision Fine-tuning | Mistral Docs
url: https://docs.mistral.ai/capabilities/finetuning/text_vision_finetuning
source: crawler
fetched_at: 2026-01-29T07:34:12.760748614-03:00
rendered_js: false
word_count: 536
summary: A technical guide detailing the processes and requirements for fine-tuning Mistral models on text and vision datasets.
tags:
    - Mistral AI
    - fine-tuning
    - multimodal
    - vision-language models
    - machine learning
category: guide
---

Fine-tuning allows you to tailor a pre-trained language model to your specific needs by training it on your dataset. This guide explains how to fine-tune text and vision models, from preparing your data to training, whether you aim to improve domain-specific understanding or adapt to a unique conversational style.

You can both finetune directly in the [AI Studio](https://console.mistral.ai/build/finetuned-models) or via our API.

### Dataset

To fine-tune a model, you need to provide a dataset that contains the data you want to train on, it is also recommended to have a validation dataset and a test dataset.

The dataset must be in a specific format, and you can upload it to the Mistral Cloud before launching the fine-tuning job.

Data must be stored in JSON Lines (`.jsonl`) files, which allow storing multiple JSON objects, each on a new line.

SFT Datasets should follow an instruction-following format representing a user-assistant conversation. Each JSON data sample should either consist of only user and assistant messages or include function-calling logic.

Conversational text only data between user and assistant, which can be one-turn or multi-turn.

- Conversational data must be stored under the `"messages"` key as a list.
- Each list item is a dictionary containing the `"content"` and `"role"` keys. `"role"` is a string: `"system"`, `"user"`, `"assistant"` or `"tool"`.
- Loss computation is performed only on tokens corresponding to assistant messages (`"role" == "assistant"`).

While text-only fine-tuning covers multiple use cases, you can also fine-tune the vision capabilities of our models. This allows you to create models that can understand and generate responses based on both text and image inputs.

Note that the files must be in JSONL format, meaning every JSON object must be flattened into a single line, and each JSON object is on a new line.

Raw `.jsonl` file example:

### Create and Manage Fine-tuning Jobs

To create your custom model, you need to create a fine-tuning job. You can fully manage jobs via our API, from creation, to starting, monitoring and cancellation.

A fine-tuning job corresponds to a single training run. You can create a fine-tuning job with the following parameters:

- model: the specific model you would like to fine-tune. The choices are:
  
  - Text Only:
    
    - `open-mistral-7b`
    - `mistral-small-latest`
    - `codestral-latest`
    - `open-mistral-nemo`
    - `mistral-large-latest`
    - `ministral-8b-latest`
    - `ministral-3b-latest`
  - Vision:
    
    - `pixtral-12b-latest`
- training\_files: a collection of training file IDs, which can consist of a single file or multiple files
- validation\_files: a collection of validation file IDs, which can consist of a single file or multiple files
- hyperparameters: two adjustable hyperparameters, "training\_steps" and "learning\_rate", that users can modify.
- auto\_start:
  
  - `auto_start=True`: Your job will be launched immediately after validation.
  - `auto_start=False` (default): You can manually start the training after validation by sending a POST request to `/fine_tuning/jobs/<uuid>/start`.
- integrations: external integrations we support such as Weights and Biases for metrics tracking during training.

After creating a fine-tuning job, you can check the job status using:

Initially, the job status will be `"QUEUED"`. After a brief period, the status will update to `"VALIDATED"`. At this point, you can proceed to start the fine-tuning job:

### Use and Delete Fine-tuned Models

Once your fine-tuning job is done, you can use your fine-tuned custom model in your applications.

Below is an example of how to use a fine-tuned model to classify your data.

You can delete a fine-tuned model if you no longer need it.