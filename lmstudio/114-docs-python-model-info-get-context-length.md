---
title: Get Context Length
url: https://lmstudio.ai/docs/python/model-info/get-context-length
source: sitemap
fetched_at: 2026-04-07T21:31:28.535708518-03:00
rendered_js: false
word_count: 178
summary: This document explains the concept of context length in LLMs and embedding models, detailing why adhering to this limit is crucial for stable operation.
tags:
    - context-length
    - llm-models
    - token-limit
    - model-architecture
    - text-generation
category: concept
---

LLMs and embedding models, due to their fundamental architecture, have a property called `context length`, and more specifically a **maximum** context length. Loosely speaking, this is how many tokens the models can "keep in memory" when generating text or embeddings. Exceeding this limit will result in the model behaving erratically.

## Use the `get_context_length()` function on the model object[](#use-the-getcontextlength-function-on-the-model-object "Link to 'Use the ,[object Object], function on the model object'")

It's useful to be able to check the context length of a model, especially as an extra check before providing potentially long input to the model.

The `model` in the above code snippet is an instance of a loaded model you get from the `llm.model` method. See [Manage Models in Memory](https://lmstudio.ai/docs/python/manage-models/loading) for more information.

### Example: Check if the input will fit in the model's context window[](#example-check-if-the-input-will-fit-in-the-models-context-window)

You can determine if a given conversation fits into a model's context by doing the following:

- Convert the conversation to a string using the prompt template.
- Count the number of tokens in the string.
- Compare the token count to the model's context length.