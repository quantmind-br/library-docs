---
title: Configuring the Model
url: https://lmstudio.ai/docs/typescript/llm-prediction/parameters
source: sitemap
fetched_at: 2026-04-07T21:31:54.449729615-03:00
rendered_js: false
word_count: 157
summary: 'This document explains how to customize model behavior by detailing two types of parameters: inference-time settings, which are set per request for controlling output generation, and load-time settings, which configure the model when it is initially loaded.'
tags:
    - inference-parameters
    - load-parameters
    - model-configuration
    - llm-api
    - prompt-tuning
category: reference
---

You can customize both inference-time and load-time parameters for your model. Inference parameters can be set on a per-request basis, while load parameters are set when loading the model.

## Inference Parameters[](#inference-parameters)

Set inference-time parameters such as `temperature`, `maxTokens`, `topP` and more.

See [`LLMPredictionConfigInput`](https://lmstudio.ai/docs/typescript/api-reference/llm-prediction-config-input) for all configurable fields.

Another useful inference-time configuration parameter is [`structured`](https://lmstudio.ai/docs/typescript/llm-prediction/%28./structured-responses%29), which allows you to rigorously enforce the structure of the output using a JSON or zod schema.

## Load Parameters[](#load-parameters)

Set load-time parameters such as the context length, GPU offload ratio, and more.

### Set Load Parameters with `.model()`[](#set-load-parameters-with-model)

The `.model()` retrieves a handle to a model that has already been loaded, or loads a new one on demand (JIT loading).

**Note**: if the model is already loaded, the configuration will be **ignored**.

See [`LLMLoadModelConfig`](https://lmstudio.ai/docs/typescript/api-reference/llm-load-model-config) for all configurable fields.

### Set Load Parameters with `.load()`[](#set-load-parameters-with-load)

The `.load()` method creates a new model instance and loads it with the specified configuration.

See [`LLMLoadModelConfig`](https://lmstudio.ai/docs/typescript/api-reference/llm-load-model-config) for all configurable fields.