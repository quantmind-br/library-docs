---
title: Mistral Fine-tuning API - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-fine_tune-mistral_finetune_api
source: crawler
fetched_at: 2026-01-29T07:33:59.17440672-03:00
rendered_js: false
word_count: 163
---

Check out the docs: [https://docs.mistral.ai/capabilities/finetuning/](https://docs.mistral.ai/capabilities/finetuning/)

## Prepare the dataset

In this example, let’s use the ultrachat\_200k dataset. We load a chunk of the data into Pandas Dataframes, split the data into training and validation, and save the data into the required jsonl format for fine-tuning.

## Reformat dataset

If you upload this ultrachat\_chunk\_train.jsonl to Mistral API, you might encounter an error message “Invalid file format” due to data formatting issues. To reformat the data into the correct format, you can download the reformat\_dataset.py script and use it to validate and reformat both the training and evaluation data:

## Upload dataset

## Create a fine-tuning job

## Use a fine-tuned model

## Integration with Weights and Biases

We can also offer support for integration with Weights & Biases (W&B) to monitor and track various metrics and statistics associated with our fine-tuning jobs. To enable integration with W&B, you will need to create an account with W&B and add your W&B information in the “integrations” section in the job creation request: