---
title: 'Product Classification: Customise your own classifier for tailored food categorization - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-classifier_factory-product_classification
source: crawler
fetched_at: 2026-01-29T07:33:42.105285244-03:00
rendered_js: false
word_count: 718
summary: A guide from the Mistral AI Cookbook on how to build and customize a product classifier for food categorization using Mistral models.
tags:
    - Mistral AI
    - machine learning
    - product classification
    - fine-tuning
    - NLP
category: guide
---

In this cookbook, we will delve into classification, specifically focusing on how to leverage the Classifier Factory to create classifiers tailored to your needs and use cases.

For simplicity, we will concentrate on a specific example that requires multitarget classification.

## Food Classification

The specific use case we will explore is food classification. We aim to classify different dishes and recipes into various categories and further classify them by the main language of the recipe.

We will focus on three values:

- The dish or food name
- The country it belongs to
- The multi-categories

This means we need to classify two main aspects: the country and the categories to which the food belongs.

We will also arbitrarily decide that there should be no food without any category; there should always be at least one.

## Dataset

For this purpose, we will use a [subset](https://huggingface.co/datasets/pandora-s/openfood-classification) of the [Open Food Facts product database](https://huggingface.co/datasets/openfoodfacts/product-database) as the data relevant to our use case.

This subset was curated to focus on the most prevalent labels and underwent a few steps for balancing.

### Labels

There are 2 main labels:

- Country *single target*: The corresponding country of the food/dish among 8 possible values: `italy`, `spain`, `germany`, `france`, `united-states`, `belgium`, `united-kingdom` and `switzerland`.
- Category *multi-target*: The category it belongs to among 8 possible values: `snacks`, `beverages`, `cereals-and-potatoes`, `plant-based-foods`, `dairies`, `plant-based-foods-and-beverages`, `meats-and-their-products` and `sweet-snacks`.

There are 8 countries and 8 different categories. Due to the nature of each label, the dataset is split as follows:

- `name`: The name of the food/dish, extracted from the `product_name` of the openfoodfacts/product-database dataset.
- `country_label`: The country ID, extracted from `countries_tags` of the openfoodfacts/product-database dataset.
- `category_labels`: The categories it belongs to, extracted from `categories_tags` of the openfoodfacts/product-database dataset.

### Distribution

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64161701107962562e9b1006/UjF0RWnrYMTkN3SQZCjMl.png) Note that the food categories overlap each other, since a sample can have multiple categories.

### Splits

The dataset was split into 3 sets:

- `train`: 80%
- `validation`: 10%
- `test`: 10%

### Data Preparation

Lets download the dataset, we will install `datasets` and load it.

We can take a look at the test set directly via colab by converting it to a pandas dataframe.

Now that we have loaded our dataset, we will convert it to the proper desired format to upload for training.

The data will be converted to a jsonl format as follows:

With an example of a label being:

For multi-target classification.

The data was converted and saved properly. We can now train our model.

## Training

There are two methods to train the model: either upload and train via [la platforme](https://console.mistral.ai/build/finetuned-models) or via the [API](https://classifier-factory.platform-docs-9m1.pages.dev/capabilities/finetuning/classifier_factory/).

First, we need to install `mistralai`.

We will upload 2 files, the training set and the validation set ( optional ) that will be used for validation loss.

With the data uploaded, we can create a job.

We allow users to keep track of aconsiderable amount of metrics via our Weights and Biases integration that we strongly recommend, you can make use of it by providing the project name and your key.

Once the job is created, we can review details such as the number of epochs and other relevant information. This allows us to make informed decisions before initiating the job.

We'll retrieve the job and wait for it to complete the validation process before starting. This validation step ensures the job is ready to begin.

We can now run the job.

The job is now starting. Let's keep track of the status and plot the loss.

For that, we highly recommend making use of our Weights and Biases integration, but we will also keep track of it directly in this notebook.

### WANDB

**Training:**

![product-train-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/product-train-loss.png)

**Eval/Validation:**

![product-validation-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/product-eval-loss.png)

**More:**

![product-panel-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/product-panel-loss.png)

![product-loss.png](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/classifier_factory/product-loss.png)

### Inference

Our model is trained and ready for use! Let's test it on a sample from our test set!

We can go even further and compare side by side normal prompting techniques with LLMs VS our new classifier, for this we will run the test set on multiple llms with structured outputs and compare the results to our classifier.

For this specific use case, most llms are struggling, this can be due to various reasons, bad prompting, small models, too specific use case...

However, our finetuned classifier performs extremely well, outperforming all other models by a decent margin! Making it not only better, but also more efficient and cheaper, as a considerably smaller model compared to its older brothers.