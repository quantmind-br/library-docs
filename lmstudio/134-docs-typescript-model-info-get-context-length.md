---
title: Get Context Length
url: https://lmstudio.ai/docs/typescript/model-info/get-context-length
source: sitemap
fetched_at: 2026-04-07T21:28:45.522536012-03:00
rendered_js: false
word_count: 178
summary: This document explains the concept of maximum context length for LLMs and embedding models, detailing how checking this limit is crucial before submitting long inputs to prevent erratic behavior.
tags:
    - llm-context-length
    - embedding-models
    - token-limit
    - model-memory
    - input-checking
category: guide
---

LLMs and embedding models, due to their fundamental architecture, have a property called `context length`, and more specifically a **maximum** context length. Loosely speaking, this is how many tokens the models can "keep in memory" when generating text or embeddings. Exceeding this limit will result in the model behaving erratically.

## Use the `getContextLength()` Function on the Model Object[](#use-the-getcontextlength-function-on-the-model-object "Link to 'Use the ,[object Object], Function on the Model Object'")

It's useful to be able to check the context length of a model, especially as an extra check before providing potentially long input to the model.

The `model` in the above code snippet is an instance of a loaded model you get from the `llm.model` method. See [Manage Models in Memory](https://lmstudio.ai/docs/typescript/manage-models/loading) for more information.

### Example: Check if the input will fit in the model's context window[](#example-check-if-the-input-will-fit-in-the-models-context-window)

You can determine if a given conversation fits into a model's context by doing the following:

- Convert the conversation to a string using the prompt template.
- Count the number of tokens in the string.
- Compare the token count to the model's context length.