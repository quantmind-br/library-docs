---
title: Configuring the Model
url: https://lmstudio.ai/docs/python/llm-prediction/parameters
source: sitemap
fetched_at: 2026-04-07T21:31:12.691871297-03:00
rendered_js: false
word_count: 206
summary: This document explains how to configure a model by detailing both inference-time parameters, which are set per request (like temperature and maxTokens), and load-time parameters, which are set when initializing the model instance.
tags:
    - inference-parameters
    - load-parameters
    - llm-configuration
    - model-setup
category: reference
---

You can customize both inference-time and load-time parameters for your model. Inference parameters can be set on a per-request basis, while load parameters are set when loading the model.

## Inference Parameters[](#inference-parameters)

Set inference-time parameters such as `temperature`, `maxTokens`, `topP` and more.

See [`LLMPredictionConfigInput`](https://lmstudio.ai/docs/typescript/api-reference/llm-prediction-config-input) in the Typescript SDK documentation for all configurable fields.

Note that while `structured` can be set to a JSON schema definition as an inference-time configuration parameter (Zod schemas are not supported in the Python SDK), the preferred approach is to instead set the [dedicated `response_format` parameter](https://lmstudio.ai/docs/python/llm-prediction/%28./structured-responses%29), which allows you to more rigorously enforce the structure of the output using a JSON or class based schema definition.

## Load Parameters[](#load-parameters)

Set load-time parameters such as the context length, GPU offload ratio, and more.

### Set Load Parameters with `.model()`[](#set-load-parameters-with-model)

The `.model()` retrieves a handle to a model that has already been loaded, or loads a new one on demand (JIT loading).

**Note**: if the model is already loaded, the given configuration will be **ignored**.

See [`LLMLoadModelConfig`](https://lmstudio.ai/docs/typescript/api-reference/llm-load-model-config) in the Typescript SDK documentation for all configurable fields.

### Set Load Parameters with `.load_new_instance()`[](#set-load-parameters-with-loadnewinstance)

The `.load_new_instance()` method creates a new model instance and loads it with the specified configuration.

See [`LLMLoadModelConfig`](https://lmstudio.ai/docs/typescript/api-reference/llm-load-model-config) in the Typescript SDK documentation for all configurable fields.