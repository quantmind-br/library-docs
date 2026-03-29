---
title: Incremental Prompt Engineering and Model Comparison with Mistral using Pixeltable - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-pixeltable-incremental_prompt_engineering_and_model_comparison
source: crawler
fetched_at: 2026-01-29T07:33:55.899837163-03:00
rendered_js: false
word_count: 406
summary: This document demonstrates how to use Pixeltable for iterative prompt engineering and model comparison with Mistral AI models, highlighting persistent storage and incremental workflow updates.
tags:
    - pixeltable
    - mistral-ai
    - prompt-engineering
    - model-comparison
    - llm-evaluation
    - data-infrastructure
category: tutorial
---

[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https%3A%2F%2Fgithub.com%2Fmistralai%2Fcookbook%2Fblob%2Fmain%2Fthird_party%2FPixeltable%2Fincremental_prompt_engineering_and_model_comparison.ipynb)   [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/third_party/Pixeltable/incremental_prompt_engineering_and_model_comparison.ipynb)

This notebook shows how to use Pixeltable for iterative prompt engineering and model comparison with Mistral AI models. It showcases persistent storage, incremental updates, and how to benchmark different prompts and models easily.

[Pixeltable](https://github.com/pixeltable/pixeltable) is data infrastructure that provides a declarative, incremental approach for multimodal AI.

**Category:** Prompt Engineering & Model Comparison

## 1. Setup and Installation

## 2. Create a Pixeltable Table and Insert Examples

First, Pixeltable is persistent. Unlike in-memory Python libraries such as Pandas, Pixeltable is a database. When you reset a notebook kernel or start a new Python session, you'll have access to all the data you've stored previously in Pixeltable.

## 3. Run Mistral Inference Functions

We create **computed columns** to instruct Pixeltable to run the Mistral `chat_completions` function and store the output. Because computed columns are a permanent part of the table, they will be automatically updated any time new data is added to the table. For more information, see our [tutorial](https://docs.pixeltable.com/docs/computed-columns).

In this particular example we are running the `open_mistral_nemo` and `mistral_medium` models and make the output available in their respective columns.

The respective response columns have the JSON column type and we can now use JSON path expressions to extract the relevant pieces of data and make them available as additional computed columns.

We can see how data is computed across the different columns in our table.

## 4. Leveraging User-Defined Functions (UDFs) for Further Analysis

UDFs allow you to extend Pixeltable with custom Python code, enabling you to integrate any computation or analysis into your workflow. See our [tutorial](https://docs.pixeltable.com/docs/user-defined-functions-udfs) regarding UDFs to learn more.

We define three UDFs to compute two metrics (sentiment and readability scores) that give us insights into the quality of the LLM outputs.

For each model we want to compare we are adding the metrics as new computed columns, using the UDFs we created.

Once a UDF is defined and used in a computed column, Pixeltable automatically applies it to all relevant rows.

You don't need to write loops or worry about applying the function to each row manually.

## 5. Experiment with Different Prompts

We are inserting an additional two rows, and Pixeltable will automatically populate the computed columns.

Often you want to select only certain rows and/or certain columns in a table. You can do this with `where()`.

You can learn more about the available table and data operations [here](https://docs.pixeltable.com/docs/tables-and-data-operations).

Pixeltable's schema provides a holistic view of data ingestion, inference API calls, and metric computation, reflecting your entire workflow.