---
title: Implementing System-Level Guardrails with Mistral API - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-moderation-system-level-guardrails
source: crawler
fetched_at: 2026-01-29T07:33:53.091605186-03:00
rendered_js: false
word_count: 499
summary: This tutorial explains how to implement Mistral's moderation API to classify conversational content and filter model responses based on safety categories.
tags:
    - mistral-ai
    - moderation-api
    - content-safety
    - guardrailing
    - text-classification
    - llm-security
category: tutorial
---

Mistral provides a moderation service powered by a classifier model based on Ministral 8B 24.10, high quality and fast to achieve compelling performance and moderate both:

- Text content
- Conversational content

For detailed information on safeguarding and moderation, please refer to our documentation [here](https://docs.mistral.ai/capabilities/guardrailing/).

## Overview

This tutorial will guide you through setting up a Mistral client, generating responses, moderating conversations, and visualizing the results.

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

We'll use datasets from Hugging Face and GitHub to test our implementation.

## Step 1: Setup

Before anything else, let's set up our client.

Cookbook tested with `v1.2.3`.

Add your API key, you can create one [here](https://console.mistral.ai/api-keys/).

## Step 2: Generate Responses

Create a function to generate responses from any Mistral model.

This function takes a user prompt and the number of generations as input and returns a list of generated responses from any Mistral model. Here, we chose `mistral-large-latest`.

Usually, each response will be a slight variation, depending on the temperature and other sampling settings. They can be less or more different from each other.

The `client.chat.complete` method is used to generate the responses.

## Step 3: Moderate Conversation

Create a function to moderate the conversation using the Mistral moderation API.

This function takes a user prompt and an assistant response as input and returns the moderation results.

## Step 4: Score and Sort Responses

Create a function to score and sort the responses based on the moderation results.

This function takes a user prompt and a list of generated responses as input and returns the final response and the list of scores. It scores each response based on the moderation results and sorts them in ascending order of the maximum score.

If the lowest score is above a certain threshold, it returns a default safe response.

## Step 5: Visualize Results

Create a function to visualize the moderation results.

This function takes a user prompt, a list of generated responses, a list of scores, and the final response as input and prints the responses with their scores and indicates whether they were chosen or not, if not chosen a default safe response was picked in their stead.

## Step 6: Dataset Function

Let's create a function to run the entire process on a dataset.

This function takes an input dataset as input and runs the entire process for each user prompt in the dataset. It generates responses, scores and sorts them, and visualizes the results.

## Step 7: Load Datasets

Load the datasets from Hugging Face and GitHub for testing.

## Step 8: Run

Run and visualize the results, here we will run 5 samples.

This code runs the function on the first 5 samples of the combined dataset and visualizes the results. As you may see, the responses were all moderated based on the threshold and the number of generations.