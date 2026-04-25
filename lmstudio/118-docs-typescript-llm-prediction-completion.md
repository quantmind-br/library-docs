---
title: Generate Completions
url: https://lmstudio.ai/docs/typescript/llm-prediction/completion
source: sitemap
fetched_at: 2026-04-07T21:31:52.494494314-03:00
rendered_js: false
word_count: 176
summary: This document explains the sequence of steps required to generate text completions using a loaded language model, covering model instantiation and prediction statistics retrieval.
tags:
    - llm-completion
    - text-generation
    - api-usage
    - language-model
    - prediction-stats
category: guide
---

Use `llm.complete(...)` to generate text completions from a loaded language model. Text completions mean sending an non-formatted string to the model with the expectation that the model will complete the text.

This is different from multi-turn chat conversations. For more information on chat completions, see [Chat Completions](https://lmstudio.ai/docs/typescript/llm-prediction/chat-completion).

## 1. Instantiate a Model[](#1-instantiate-a-model "Link to '1. Instantiate a Model'")

First, you need to load a model to generate completions from. This can be done using the `model` method on the `llm` handle.

## 2. Generate a Completion[](#2-generate-a-completion "Link to '2. Generate a Completion'")

Once you have a loaded model, you can generate completions by passing a string to the `complete` method on the `llm` handle.

## 3. Print Prediction Stats[](#3-print-prediction-stats "Link to '3. Print Prediction Stats'")

You can also print prediction metadata, such as the model used for generation, number of generated tokens, time to first token, and stop reason.

## Example: Get an LLM to Simulate a Terminal[](#example-get-an-llm-to-simulate-a-terminal "Link to 'Example: Get an LLM to Simulate a Terminal'")

Here's an example of how you might use the `complete` method to simulate a terminal.