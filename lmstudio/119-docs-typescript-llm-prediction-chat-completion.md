---
title: Chat Completions
url: https://lmstudio.ai/docs/typescript/llm-prediction/chat-completion
source: sitemap
fetched_at: 2026-04-07T21:31:40.504662641-03:00
rendered_js: false
word_count: 241
summary: This document details various methods for interacting with an LLM through the `llm` object, covering obtaining a model handle, managing conversation context, generating responses, customizing inference parameters, and printing prediction statistics.
tags:
    - llm-interaction
    - generate-response
    - chat-context
    - model-handling
    - inference-parameters
category: guide
---

Use `llm.respond(...)` to generate completions for a chat conversation.

## Quick Example: Generate a Chat Response[](#quick-example-generate-a-chat-response "Link to 'Quick Example: Generate a Chat Response'")

The following snippet shows how to stream the AI's response to quick chat prompt.

## Obtain a Model[](#obtain-a-model "Link to 'Obtain a Model'")

First, you need to get a model handle. This can be done using the `model` method in the `llm` namespace. For example, here is how to use Qwen2.5 7B Instruct.

There are other ways to get a model handle. See [Managing Models in Memory](https://lmstudio.ai/docs/typescript/manage-models/loading) for more info.

## Manage Chat Context[](#manage-chat-context "Link to 'Manage Chat Context'")

The input to the model is referred to as the "context". Conceptually, the model receives a multi-turn conversation as input, and it is asked to predict the assistant's response in that conversation.

See [Working with Chats](https://lmstudio.ai/docs/typescript/llm-prediction/working-with-chats) for more information on managing chat context.

## Generate a response[](#generate-a-response "Link to 'Generate a response'")

You can ask the LLM to predict the next response in the chat context using the `respond()` method.

## Customize Inferencing Parameters[](#customize-inferencing-parameters "Link to 'Customize Inferencing Parameters'")

You can pass in inferencing parameters as the second parameter to `.respond()`.

See [Configuring the Model](https://lmstudio.ai/docs/typescript/llm-prediction/parameters) for more information on what can be configured.

## Print prediction stats[](#print-prediction-stats "Link to 'Print prediction stats'")

You can also print prediction metadata, such as the model used for generation, number of generated tokens, time to first token, and stop reason.

## Example: Multi-turn Chat[](#example-multi-turn-chat "Link to 'Example: Multi-turn Chat'")