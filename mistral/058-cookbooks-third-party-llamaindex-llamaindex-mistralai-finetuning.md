---
title: Fine Tuning MistralAI models using Finetuning API and LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-llamaindex_mistralai_finetuning
source: crawler
fetched_at: 2026-01-29T07:34:04.063657448-03:00
rendered_js: false
word_count: 613
---

In this notebook, we walk through an example of fine-tuning `open-mistral-7b` using MistralAI finetuning API.

Specifically, we attempt to distill `mistral-large-latest`'s knowledge, by generating training data with `mistral-large-latest` to then fine-tune `open-mistral-7b`.

All training data is generated using two different sections of our index data, creating both a training and evalution set.

We will use `mistral-small-largest` to create synthetic training and evaluation questions to avoid any biases towards `open-mistral-7b` and `mistral-large-latest`.

We then finetune with our `MistraAIFinetuneEngine` wrapper abstraction.

Evaluation is done using the `ragas` library, which we will detail later on.

We can monitor the metrics on `Weights & Biases`

## Set API Key

## Download Data

Here, we first down load the PDF that we will use to generate training data.

The next step is generating a training and eval dataset.

We will generate 40 training and 40 evaluation questions on different sections of the PDF we downloaded.

We can use `open-mistral-7b` on the eval questions to get our baseline performance.

Then, we will use `mistral-large-latest` on the train questions to generate our training data.

## Load Data

## Setup LLM and Embedding Model

## Training and Evaluation Data Generation

We will generate 40 training and 40 evaluation questions

Now, lets generate questions on a completely different set of documents, in order to create our eval dataset.

## Initial Eval with `open-mistral-7b` Query Engine

For this eval, we will be using the [`ragas` evaluation library](https://github.com/explodinggradients/ragas).

Ragas has a ton of evaluation metrics for RAG pipelines, and you can read about them [here](https://github.com/explodinggradients/ragas/blob/main/docs/metrics.md).

For this notebook, we will be using the following two metrics

- `answer_relevancy` - This measures how relevant is the generated answer to the prompt. If the generated answer is incomplete or contains redundant information the score will be low. This is quantified by working out the chance of an LLM generating the given question using the generated answer. Values range (0,1), higher the better.
- `faithfulness` - This measures the factual consistency of the generated answer against the given context. This is done using a multi step paradigm that includes creation of statements from the generated answer followed by verifying each of these statements against the context. The answer is scaled to (0,1) range. Higher the better.

Let's check the results before finetuning.

## `mistral-large-latest` to Collect Training Data

Here, we use `mistral-large-latest` to collect data that we want `open-mistral-7b` to finetune on.

## Create `MistralAIFinetuneEngine`

We create an `MistralAIFinetuneEngine`: the finetune engine will take care of launching a finetuning job, and returning an LLM model that you can directly plugin to the rest of LlamaIndex workflows.

We use the default constructor, but we can also directly pass in our finetuning\_handler into this engine with the `from_finetuning_handler` class method.

## Evaluation

Once the finetuned model is created, the next step is running our fine-tuned model on our eval dataset again to measure any performance increase.

Let's check the results with finetuned model

### Observation:

`open-mistral-7b` : 'answer\_relevancy': **0.8151**, 'faithfulness': **0.8360**

`open-mistral-7b-finetuned` : 'answer\_relevancy': **0.8016**, 'faithfulness': **0.8924**

As you can see there is an increase in faithfulness score and small drop in answer relevancy.

## Exploring Differences

Let's quickly compare the differences in responses, to demonstrate that fine tuning did indeed change something.

### Original `open-mistral-7b`

### Fine-Tuned `open-mistral-7b`

### Observation:

As we can see, the fine-tuned model provides a more thorough response! This lines up with the increased faithfullness score from ragas, since the answer is more representative of the retrieved context.

## Conclusion

So, in conclusion, finetuning with only ~40 questions actually helped improve our eval scores!

**answer\_relevancy: 0.0.8151 -&gt; 0.8016**

The answer relevancy dips slightly but it's very small.

**faithfulness: 0.8360 -&gt; 0.8924**

The faithfulness appears to have been improved! This mains the anwers given better fuffil the original question that was asked.