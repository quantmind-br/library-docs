---
title: Fine-tuning with Synthetically Generated Data - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-data_generation-synthetic_data_gen_and_finetune
source: crawler
fetched_at: 2026-01-29T07:34:01.007586447-03:00
rendered_js: false
word_count: 1044
summary: This document explains how to use Mistral models to generate synthetic datasets by rewriting existing data to instill specific personalities and identities. It provides a comprehensive workflow including asynchronous data generation, validation, and fine-tuning using the Mistral API.
tags:
    - synthetic-data-generation
    - mistral-api
    - fine-tuning
    - async-processing
    - data-validation
    - llm-personality
category: tutorial
---

Synthetic Data Generation is a crucial aspect of today's training and fine-tuning of models. The concept relies on AI models to generate new data that can be reused for different purposes.

In this notebook, we will generate synthetic data for specific use cases and quickly showcase the results after fine-tuning with the API for demonstration.

There are no fixed methods for synthetic data generation; different use cases, data formats, and limitations will greatly change how you would generate the corresponding data.

For this reason, we will showcase a full example of synthetic data generation to give a personality to a model.

First, we will for both examples require `mistralai`, so let's setup everything:

## Objective: Personality

When designing an Application, we might envision an Assistant with a specific personality trait or even an entire identity. Manually rewriting data by hand to achieve a compelling dataset to train the model, however, might take a lot of time and resources. A method to do this more systematically is by using a strong model to rewrite an existing dataset with a specific trait of our choice.

While we could generate entire conversations from scratch using our models, that would require a lot of steps and a pipeline that could easily get very big and expensive, but there is no need to start from scratch. Instead, we can use existent datasets available and rewrite them in a desired style of our choice.

For this reason, we will make use of `mistral-small-latest` capabilities to rewrite a dataset following a specific personality and trait of our choice. This dataset can later be used to fine-tune a different model. Here we will fine-tune `open-mistral-7b` with this data and chat with a newly tuned model!

*Note: For better quality, it's recommended to use `mistral-large-latest` instead!*

Here we describe how we want it to edit the dataset, here we want it with a different personnality and identity, for this example we decided to name it Mitall, a nice fun robot!

## Generate Data

First, let's create a function that will handle the conversion from one style to another. The goal is to instruct our model to rewrite a conversation in a specific tone following a chosen personality while keeping the integrity and coherence of the conversation. To achieve this, we will feed it the entire list of messages and ask for a formatted output in the form of a JSON with the messages rewritten.

## Dataset

Now, let's download a dataset that we are going to parse. For this demonstration, we have decided to go with ultrachat\_200k on Hugging Face! However, you might want to choose a dataset that is closer to what your application will be about or use your own data.

## Generation

Before generating, however, it's important to note that LLMs may not always parse the conversation correctly and might sometimes provide the wrong JSON for our use case, resulting in an incorrect messages dictionary. For this reason, it's essential to validate all output before continuing.

Let's make a function that validates whether the output follows the correct format or not.

There are different methods to validate, one of them would be to hardcode it with multiple gates. However, a more elegant way is to use a template or expression. Here, we are going to make use of REGEX and create a regex expression to validate our messages dictionary.

Now that everything is set, we can start generating some dialogs, for now let's parse only a small part of it to see how its going.

Let's see one example side by side.

Seems like it's working as intended! However, 3 minutes for 8 conversations is a long time to wait...

## Async

While we could parse one conversation at a time and iterate through all of them, it would take a long time. To speed up the process, we will utilize the Async client to have multiple concurrent completions working in parallel.

For this, we will create a class to handle everything asynchronously. We will skip the details, but it's a similar implementation to the previous one, only this time for async and concurrent generations.

It's time for the generation. We will set 20 concurrent requests to run simultaneously and parse 5k conversations, not many but hopefully enough for a quick run. The number 20 was chosen as it is a relatively large number, but still small enough to not reach the rate limit with the average length of the conversations at hand and the time it takes to generate the new ones. Previously for 8 generations it took 3 minutes, with 20 concurrent we should have around 3 requests/generations per second in average.

Let's evaluate how many tokens we have approximately. For this, let's use `mistral-common` with the tokenizer V3.

5m tokens approximately! This should be ennough for a quick fine tunning using our API!

## Finetuning

Data gen done, we can finally fine tune our model with it! For this we need to first convert the list of messages into a json file in the proper format, since we already got rid of most issues on the generation step we can easily save the files like this:

Now that is saved, we can fine tune our model.  
First let's send our files with the training and evaluation datasets to Mistral.

Now that our data is ready, we can start the fine tuning process.  
To decide the number of steps, we can approximate the number of epochs desired with a simple formula.  
For this fine tuning we will go with 3 epochs.

It's finally time, let's create our job and start the fine tuning of `open-mistral-7b` with our generated data.

Now that the job is created, let's keep track of the process with a simple loop so we can see the progress.

Finished!! We can now freely test our new model:

Meanwhile the original `open-mistral-7b` model:

The total cost for generating and training this model was approximately $50 with `mistral-small-latest` and `open-mistral-7b`, for production we recommend using `mistral-large-latest` and `mistral-small-latest` but the cost will be higher.

This was a simplified and straightforward approach to data generation! However, it's important to note that different use cases may require more intricate pipelines for data generation, often involving multiple calls, collaborating agents, and external sources for data extraction.