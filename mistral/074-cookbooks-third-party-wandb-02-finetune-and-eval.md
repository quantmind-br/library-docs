---
title: 'Mistral and Weights & Biases: Finetune an LLM judge so detect hallucination - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/third_party-wandb-02_finetune_and_eval
source: crawler
fetched_at: 2026-01-29T07:34:00.703208951-03:00
rendered_js: false
word_count: 546
summary: A guide on fine-tuning a Mistral model to act as an LLM judge for hallucination detection, featuring integration with Weights & Biases.
tags:
    - Mistral
    - Weights & Biases
    - fine-tuning
    - hallucination detection
    - LLM judge
category: guide
---

In this notebooks you will learn how to trace your MistralAI Api calls using W&B Weave, how to evaluate the performance of your models and how to close the gap by leveraging the MistralAI finetuning capabilities.

In this notebooks we will fine-tune a mistral 7b model as an LLM Judge. This idea comes from the [amazing blog post from Eugene](https://eugeneyan.com/writing/finetuning/). The main goal is to fine-tune a small model like Mistral 7B to act as an hallucination judge. We will do this in 2 steps:

- Training on a [Factual Inconsistency Benchmark](https://arxiv.org/abs/2211.08412v1) challenging dataset to improve the model performance to detect hallucination by detecting inconsistencies beween a piece of text and a "summary"
- We will then mix that dataset with Wikipedia summaries dataset to increase the performance even more.

[![](https://docs.mistral.ai/cookbooks/third_party/wandb/static/eugene1.png)](https://eugeneyan.com/writing/finetuning/)

* * *

## Load some data

let's import the relevant pieces

some globals

![](https://docs.mistral.ai/cookbooks/third_party/wandb/static/nli.png)

We are going to map to 0 and 1 for the sake of it!

You will probably integrate MistralAI API calls in your codebase by creating a function like the one below:

Let's create a prompt that explains the task...

## Eval

Let's evaluate the model on the validation split of the dataset

## 7B

![](https://docs.mistral.ai/cookbooks/third_party/wandb/static/eval_7b.png)

## Iterate a bit on the prompt...

Let's try adding the example from Eugene's blog:

This is a hard dataset!

## Large

![](https://docs.mistral.ai/cookbooks/third_party/wandb/static/eval_large.png)

This model is considerably better! over 80% accuracy is great on this hard task 😎

## Fine-Tune FTW

Let's see if fine-tuning improves this.

You will need to format your prompts slightly different for FT

- instead of `ChatMessage` use a `dict`
- Add the output

You could use other fancy datasets or pandas, but this is a small dataset so let's not add more complexity...

## Upload dataset

## Create a fine-tuning job

Ok, now let's create a fine-tune job with the mistral api. Some thing to know:

- You only have 2 parameters to play wtih: `training_steps` and `learning_rate`
- You can use `dry_run=True` to get an estimate cost
- `training_steps` is not exactly linked to epochs in a direct way, they have a rule of thumbs on the docs. If you do a dry run the epochs will be calculated for you.

We want to run for 10 epochs to reproduce Eugene's results.

![](https://docs.mistral.ai/cookbooks/third_party/wandb/static/ft_dashboard.png)

## Use a fine-tuned model

Let's compute the predictions using the fine-tuned 7B model

quite substantial improvement! Some take aways:

- the Mistral 7B is a much more powerful model than the original Bart that eugene was using on his blog post
- With a relatively small high quality dataset the improvements for this downstream task are enormous!
- Now we can leverage a faster and cheaper 7B instead of taping into `mistral-large`. Of course we could have some filtering logic to decide when to use the big gun anyway.

## Pre-finetuning on USB to improve performance on FIB

The [Unified Summarization Benchmark (USB)](https://arxiv.org/abs/2305.14296) is made up of eight summarization tasks including abstractive summarization, evidence extraction, and factuality classification. While FIB documents are based on news, USB documents are based on a different domain—Wikipedia. Labels for factual consistency were created based on edits to summary sentences; inconsistent and consistent labels were assigned to the before and after versions respectively. Here’s the first sample in the dataset:

> Check Eugene's Analysis [here](https://eugeneyan.com/writing/finetuning/#pre-finetuning-on-usb-to-improve-performance-on-fib)

Let's mix the USB dataset in the training data...

## Final results

The fine-tuned model over USB + FIB is now 90%+ accurate!

![](https://docs.mistral.ai/cookbooks/third_party/wandb/static/compare.png)