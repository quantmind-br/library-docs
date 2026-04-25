---
title: Parallel Requests
url: https://lmstudio.ai/docs/app/advanced/parallel-requests
source: sitemap
fetched_at: 2026-04-07T21:29:36.449764954-03:00
rendered_js: false
word_count: 158
summary: This document explains how to enable concurrent processing of multiple model requests using continuous batching, allowing for higher throughput when loading models with llama.cpp.
tags:
    - concurrent-requests
    - continuous-batching
    - llama-cpp
    - model-loading
    - throughput
    - lm-studio
category: guide
---

When loading a model, you can now set Max Concurrent Predictions to allow multiple requests to be processed in parallel, instead of queued. This is supported for LM Studio's llama.cpp engine, with MLX coming soon.

Please make sure your GGUF runtime is upgraded to llama.cpp v2.0.0.

* * *

### Parallel Requests via Continuous Batching[](#parallel-requests-via-continuous-batching)

Parallel requests via continuous batching allows the LM Studio server to dynamically combine multiple requests into a single batch. This enables concurrent workflows and results in higher throughput.

### Setting Max Concurrent Predictions[](#setting-max-concurrent-predictions)

Open the model loader and toggle on Manually choose model load parameters. Select a model to load, and toggle on Show advanced settings to set Max Concurrent Predictions. By default, Max Concurrent Predictions is set to 4.

### Sending parallel requests to chats in Split View[](#sending-parallel-requests-to-chats-in-split-view)

Use the [split view in chat feature](https://lmstudio.ai/docs/basics/chat) to send two requests simultaneously to two chats and view them side by side.

![undefined](https://lmstudio.ai/assets/docs/parallel-requests.png)

Send parallel requests using split view in chat