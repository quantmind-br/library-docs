---
title: Text Completions
url: https://lmstudio.ai/docs/python/llm-prediction/completion
source: sitemap
fetched_at: 2026-04-07T21:31:10.427648798-03:00
rendered_js: false
word_count: 442
summary: This document details how to use the `llm.complete()` function to generate text completions from a loaded language model. It covers steps for instantiating the model, generating predictions, and accessing prediction metadata, including options for customizing parameters and implementing progress callbacks.
tags:
    - text-completion
    - language-model
    - api-usage
    - progress-callbacks
    - llm-api
category: guide
---

Use `llm.complete(...)` to generate text completions from a loaded language model. Text completions mean sending a non-formatted string to the model with the expectation that the model will complete the text.

This is different from multi-turn chat conversations. For more information on chat completions, see [Chat Completions](https://lmstudio.ai/docs/python/llm-prediction/chat-completion).

## 1. Instantiate a Model[](#1-instantiate-a-model "Link to '1. Instantiate a Model'")

First, you need to load a model to generate completions from. This can be done using the top-level `llm` convenience API, or the `model` method in the `llm` namespace when using the scoped resource API. For example, here is how to use Qwen2.5 7B Instruct.

## 2. Generate a Completion[](#2-generate-a-completion "Link to '2. Generate a Completion'")

Once you have a loaded model, you can generate completions by passing a string to the `complete` method on the `llm` handle.

## 3. Print Prediction Stats[](#3-print-prediction-stats "Link to '3. Print Prediction Stats'")

You can also print prediction metadata, such as the model used for generation, number of generated tokens, time to first token, and stop reason.

Both the non-streaming and streaming result access is consistent across the synchronous and asynchronous APIs, as `prediction_stream.result()` is a non-blocking API that raises an exception if no result is available (either because the prediction is still running, or because the prediction request failed). Prediction streams also offer a blocking (synchronous API) or awaitable (asynchronous API) `prediction_stream.wait_for_result()` method that internally handles iterating the stream to completion before returning the result.

## Example: Get an LLM to Simulate a Terminal[](#example-get-an-llm-to-simulate-a-terminal "Link to 'Example: Get an LLM to Simulate a Terminal'")

Here's an example of how you might use the `complete` method to simulate a terminal.

## Customize Inferencing Parameters[](#customize-inferencing-parameters "Link to 'Customize Inferencing Parameters'")

You can pass in inferencing parameters via the `config` keyword parameter on `.complete()`.

See [Configuring the Model](https://lmstudio.ai/docs/python/llm-prediction/parameters) for more information on what can be configured.

### Progress Callbacks[](#progress-callbacks)

Long prompts will often take a long time to first token, i.e. it takes the model a long time to process your prompt. If you want to get updates on the progress of this process, you can provide a float callback to `complete` that receives a float from 0.0-1.0 representing prompt processing progress.

In addition to `on_prompt_processing_progress`, the other available progress callbacks are:

- `on_first_token`: called after prompt processing is complete and the first token is being emitted. Does not receive any arguments (use the streaming iteration API or `on_prediction_fragment` to process tokens as they are emitted).
- `on_prediction_fragment`: called for each prediction fragment received by the client. Receives the same prediction fragments as iterating over the stream iteration API.
- `on_message`: called with an assistant response message when the prediction is complete. Intended for appending received messages to a chat history instance.