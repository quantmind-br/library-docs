---
title: Explore and learn about Mistral's Moderation service - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-moderation-moderation-explored
source: crawler
fetched_at: 2026-01-29T07:33:53.678330134-03:00
rendered_js: false
word_count: 535
---

Mistral provides a moderation service powered by a classifier model based on Ministral 8B 24.10, high quality and fast to achieve compelling performance and moderate both:

- Text content
- Conversational content

For detailed information on safeguarding and moderation, please refer to our documentation [here](https://docs.mistral.ai/capabilities/guardrailing/).

## Overview

We will dig into our moderation API to implement a safe chatbot service to avoid any content that could be sexual, violent, or harmful. It will be split into 3 sections:

- Embeddings Study: Quick analysis of the representation of safe and unsafe content with our embedding model.
- User Side: How to filter and moderate user inputs.
- Assistant Side: How to filter and moderate assistant outputs.

Before anything else, let's set up our client.

### Install/Update `mistralai`

Cookbook tested with `v1.2.3`.

### Setup your client

Add your API key, you can create one [here](https://console.mistral.ai/api-keys/).

## Embeddings Study

Before diving into the moderation of user and assistant content, let's understand how embeddings represent different types of content in the vector space. Embeddings are numerical representations of text that capture semantic meaning. By visualizing these embeddings, we can see how distinctively they are represented.

### Sample Data

We'll use a set of sample texts labeled as "ultrachat" or "harmful" to generate embeddings and visualize them.

### Visualizing Embeddings

We'll use t-SNE to reduce the dimensionality of the embeddings to 2D for visualization.

Although we cannot observe the full representation of these samples in the entire vector space, we can reduce the dimensionality to gain a quick insight. Remarkably, we can discern a clear distinction between the two sets, which are plotted in completely opposite corners.

## User Side

You can easily classify text or conversational data into nine categories. For conversational data, the last user message will be classified.  
Categories:

- **Sexual**
- **Hate and Discrimination**
- **Violence and Threats**
- **Dangerous and Criminal Content**
- **Self-harm**
- **Health**
- **Financial**
- **Law**
- **PII (Personally Identifiable Information)**

In this case, we are specially interested in the first 5 categories that we will carefully monitor.

Let's give it a try with safe and unsafe examples.

### Safe

Here we define a simple plot function to visualize our results.

In this safe example, the moderation API that is also capable of detecting other types of contents only gave high results for the "financial" label.

We have internally a threshold that was defined after our internal testings to trigger or not a flag for each label, in this case our moderation triggered for "financial", however you can define a threshold by making use of the score provided by the API.

### Unsafe

In this scenario, the moderation properly triggered for "hate and discrimination" as well as "violence and threats"!

## System/Assistant Side

First, let's set up the moderation service together with our conversational API!

Here, no flag was triggered, and the values for each label are considerably low, meaning it did not trigger any of them!

Our models are by default fairly aligned, however malevolent users and other external factors can trigger the model to output unsafe content, lets simulate this behaviour.

Our moderation model properly detected and flagged the content as violence, allowing to moderate and control the output of the model.

You can also use this in a feedback loop, asking the model to deny the request if such label is triggered!