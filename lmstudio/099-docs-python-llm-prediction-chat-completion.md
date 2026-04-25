---
title: Chat Completions
url: https://lmstudio.ai/docs/python/llm-prediction/chat-completion
source: sitemap
fetched_at: 2026-04-07T21:31:00.529411867-03:00
rendered_js: false
word_count: 534
summary: This document provides various methods and concepts related to interacting with Language Models (LLMs), covering tasks such as generating standard or streamed chat responses, managing conversational context, obtaining model handles, and customizing inference parameters.
tags:
    - llm-interaction
    - chat-completion
    - inference-parameters
    - context-management
    - streaming-response
category: tutorial
---

Use `llm.respond(...)` to generate completions for a chat conversation.

## Quick Example: Generate a Chat Response[](#quick-example-generate-a-chat-response "Link to 'Quick Example: Generate a Chat Response'")

The following snippet shows how to obtain the AI's response to a quick chat prompt.

## Streaming a Chat Response[](#streaming-a-chat-response "Link to 'Streaming a Chat Response'")

The following snippet shows how to stream the AI's response to a chat prompt, displaying text fragments as they are received (rather than waiting for the entire response to be generated before displaying anything).

## Cancelling a Chat Response[](#cancelling-a-chat-response "Link to 'Cancelling a Chat Response'")

See the [Cancelling a Prediction](https://lmstudio.ai/docs/python/llm-prediction/cancelling-predictions) section for how to cancel a prediction in progress.

## Obtain a Model[](#obtain-a-model "Link to 'Obtain a Model'")

First, you need to get a model handle. This can be done using the top-level `llm` convenience API, or the `model` method in the `llm` namespace when using the scoped resource API. For example, here is how to use Qwen2.5 7B Instruct.

There are other ways to get a model handle. See [Managing Models in Memory](https://lmstudio.ai/docs/python/manage-models/loading) for more info.

## Manage Chat Context[](#manage-chat-context "Link to 'Manage Chat Context'")

The input to the model is referred to as the "context". Conceptually, the model receives a multi-turn conversation as input, and it is asked to predict the assistant's response in that conversation.

See [Working with Chats](https://lmstudio.ai/docs/python/llm-prediction/working-with-chats) for more information on managing chat context.

## Generate a response[](#generate-a-response "Link to 'Generate a response'")

You can ask the LLM to predict the next response in the chat context using the `respond()` method.

## Customize Inferencing Parameters[](#customize-inferencing-parameters "Link to 'Customize Inferencing Parameters'")

You can pass in inferencing parameters via the `config` keyword parameter on `.respond()`.

See [Configuring the Model](https://lmstudio.ai/docs/python/llm-prediction/parameters) for more information on what can be configured.

## Print prediction stats[](#print-prediction-stats "Link to 'Print prediction stats'")

You can also print prediction metadata, such as the model used for generation, number of generated tokens, time to first token, and stop reason.

Both the non-streaming and streaming result access is consistent across the synchronous and asynchronous APIs, as `prediction_stream.result()` is a non-blocking API that raises an exception if no result is available (either because the prediction is still running, or because the prediction request failed). Prediction streams also offer a blocking (synchronous API) or awaitable (asynchronous API) `prediction_stream.wait_for_result()` method that internally handles iterating the stream to completion before returning the result.

## Example: Multi-turn Chat[](#example-multi-turn-chat "Link to 'Example: Multi-turn Chat'")

### Progress Callbacks[](#progress-callbacks)

Long prompts will often take a long time to first token, i.e. it takes the model a long time to process your prompt. If you want to get updates on the progress of this process, you can provide a float callback to `respond` that receives a float from 0.0-1.0 representing prompt processing progress.

In addition to `on_prompt_processing_progress`, the other available progress callbacks are:

- `on_first_token`: called after prompt processing is complete and the first token is being emitted. Does not receive any arguments (use the streaming iteration API or `on_prediction_fragment` to process tokens as they are emitted).
- `on_prediction_fragment`: called for each prediction fragment received by the client. Receives the same prediction fragments as iterating over the stream iteration API.
- `on_message`: called with an assistant response message when the prediction is complete. Intended for appending received messages to a chat history instance.