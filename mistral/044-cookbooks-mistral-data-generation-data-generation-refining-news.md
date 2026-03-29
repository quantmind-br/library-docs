---
title: 'Data Generation: Refining News Articles - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-data_generation-data_generation_refining_news
source: crawler
fetched_at: 2026-01-29T07:34:03.281611087-03:00
rendered_js: false
word_count: 435
---

In this cookbook, we will dig into the process of generating data to fine-tune a model for rewriting articles in a specific, refined format. We will utilize a two-step pipeline for this purpose. First, we will generate critiques about the articles making use of guides that our model should respect and use as reference. Then, using these critiques, we will produce new, refined articles. The goal is to create a dataset that includes at least the original article and its refined version, which could potentially be used to fine-tune a model in the future or other purposes.

You can download the guides for this notebook with the following:

First step is to install `mistralai` and create a client with your api key!

The next step is to download the dataset. We will be making use of a dataset available on Hugging Face, but you could provide your own!

For this example, we will be generating 100 pairs of the original articles and the refined ones, but you are free to generate as many as you require.

Our pipeline will consist of two steps. First, we will generate critiques using a style guideline of our choice. Here, we have four different guidelines that are more or less the same, but you could rewrite your own.

Once the critiques have been generated, we will use them to generate the new rewritten articles!

Let's get started with the criticism!

Let's create a folder where we will cache our data as we generate it. This can be handy for debugging and to have a backup in case something goes wrong.

Now, let's define the first process. We will make use of `mistral-large-latest` capabilities to both criticize and rewrite our articles, but you are free to use any combination of your choice.

To generate diverse output each time, it might be a good idea to have multiple system prompts instead of a single one. Here, we provide a few system prompts that are all very similar but overall different.

Now, it's time to generate. Let's get the guides we made and start the generation using `process_map`, which will create multiple workers to generate the new data in parallel and more efficiently.

Perfect! Critiques generated, now it's time to refine and rewrite our articles using the feedback!

We will replace our multiple system variations with a generalized one to give it context, but the key part of our second step is our instruction to rewrite the article with the provided feedback. This instruction might require a lot of changes depending on your requirements!

Articles generated! Let's take a look at them.