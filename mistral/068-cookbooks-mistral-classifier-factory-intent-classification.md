---
title: 'Intent Detection: Identify user intent efficiently with a custom classifier - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-classifier_factory-intent_classification
source: crawler
fetched_at: 2026-01-29T07:33:48.88628017-03:00
rendered_js: false
word_count: 406
summary: A guide from the Mistral AI Cookbook on building a custom classifier to efficiently identify user intent in natural language queries.
tags:
    - intent detection
    - Mistral AI
    - classifier
    - machine learning
    - NLP
category: guide
---

In this cookbook, we will explore classification for intent detection and classification using our Classifier Factory.

To keep things straightforward, we will concentrate on a particular example that involves single-target classification.

## Dataset

We will use a subset of the [mteb/amazon\_massive\_intent](https://huggingface.co/datasets/mteb/amazon_massive_intent) dataset. This subset includes an intent for different user requests.

### Subset

Let's download and prepare the subset. We will install the `datasets` library and load the dataset.

## Format Data

Now that we have loaded our dataset, we will convert it to the proper desired format to upload for training.

The data will be converted to a **JSONL** format as follows:

With an example of a label being:

For **single-target** classification.

The data was converted and saved properly. We can now train our model.

## Training

There are two methods to train the model: either upload and train via [la platforme](https://console.mistral.ai/build/finetuned-models) or via the [API](https://classifier-factory.platform-docs-9m1.pages.dev/capabilities/finetuning/classifier_factory/).

First, we need to install `mistralai`.

And setup our client, you can create an API key [here](https://console.mistral.ai/api-keys/).

We will upload 2 files, the training set and the validation set ( optional ) that will be used for validation loss.

With the data uploaded, we can create a job.

We allow users to keep track of aconsiderable amount of metrics via our Weights and Biases integration that we strongly recommend, you can make use of it by providing the project name and your key.

Once the job is created, we can review details such as the number of epochs and other relevant information. This allows us to make informed decisions before initiating the job.

We'll retrieve the job and wait for it to complete the validation process before starting. This validation step ensures the job is ready to begin.

We can now run the job.

The job is now starting. Let's keep track of the status and print the information.

We highly recommend making use of our Weights and Biases integration to keep track of multiple metrics.

### WANDB

**Training:**

![intent-train-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/intent-train-loss.png)

**Eval/Validation:**

![intent-validation-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/intent-validation-loss.png)

### Inference

Our model is trained and ready for use! Let's test it on a sample from our test set!

The score with the highest result is `weather_query`, with an over 99% score!

There you have it: a simple guide on how to train your own classifier and use our batch inference.

For a more specific multi-label classifier, visit this [cookbook](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/moderation_classifier.ipynb).

For a more product focused in-depth guide on both multi-target, with an evaluation comparison between LLMs and our classifier, visit this [cookbook](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/product_classification.ipynb).