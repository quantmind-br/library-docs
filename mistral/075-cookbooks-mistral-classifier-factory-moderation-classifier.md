---
title: 'Moderation: Train your own moderation service - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-classifier_factory-moderation_classifier
source: crawler
fetched_at: 2026-01-29T07:33:49.639398338-03:00
rendered_js: false
word_count: 427
summary: A comprehensive guide on training a custom content moderation service using Mistral AI to identify and filter sensitive or inappropriate content.
tags:
    - moderation
    - machine learning
    - Mistral AI
    - content safety
    - fine-tuning
category: guide
---

In this cookbook, we will explore classification for moderation using our Classifier Factory to build classifiers tailored to your specific needs and use cases.

To keep things straightforward, we will concentrate on a particular example that involves multilabel classification for content moderation.

## Dataset

We will use a subset of the [google/civil\_comments](https://huggingface.co/datasets/google/civil_comments) dataset. This subset includes several labels that we will for multi-label classification, allowing us to obtain scores for each type of moderation.

### Subset

Lets download and prepare the subset, we will install `datasets` and load it.

This will be the subset we will be training with. In an optimal scenario, you may need to do further curation and data preparation to balance the dataset and achieve better results. In this scenario, we have a fairly balanced dataset for `toxicity` and `insult`, but it is much less balanced for the rest of the labels.

## Format Data

Now that we have loaded our dataset, we will convert it to the proper desired format to upload for training.

The data will be converted to a **JSONL** format as follows:

With an example of a label being:

For multi-label classification, we arbitrarily defined a new label "safe" to represent samples that were not flagged.

The data was converted and saved properly. We can now train our model.

## Training

There are two methods to train the model: either upload and train via [la platforme](https://console.mistral.ai/build/finetuned-models) or via the [API](https://classifier-factory.platform-docs-9m1.pages.dev/capabilities/finetuning/classifier_factory/).

First, we need to install `mistralai`.

And setup our client, you can create an API key [here](https://console.mistral.ai/api-keys/).

We will upload 2 files, the training set and the validation set ( optional ) that will be used for validation loss.

With the data uploaded, we can create a job.

Once the job is created, we can review details such as the number of epochs and other relevant information. This allows us to make informed decisions before initiating the job.

We'll retrieve the job and wait for it to complete the validation process before starting. This validation step ensures the job is ready to begin.

We can now run the job.

The job is now starting. Let's keep track of the status and plot the loss.

For that, we highly recommend making use of our Weights and Biases integration, but we will also keep track of it directly in this notebook.

### WANDB

**Training:**

![moderation-train-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/moderation-train-loss.png)

**Eval/Validation:**

![moderation-validation-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/moderation-validation-loss.png)

### Inference

Our model is trained and ready for use! Let's test it on a sample from our test set!

For a more in-depth guide on multi-target, with an evaluation comparison between LLMs and our classifier API, visit this [cookbook](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/product_classification.ipynb).