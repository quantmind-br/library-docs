---
title: Usage | Mistral Docs
url: https://docs.mistral.ai/capabilities/completion/usage
source: crawler
fetched_at: 2026-01-29T07:33:36.216579793-03:00
rendered_js: false
word_count: 826
summary: Documentation providing instructions and examples for using Mistral AI models, including API implementation, integration, and configuration.
tags:
    - Mistral AI
    - API
    - LLM
    - documentation
category: guide
---

Large Language Models (LLMs) are AI systems that generate text and engage in conversational interactions. They are fine-tuned to follow instructions and respond naturally to prompts—inputs like questions, instructions, or task examples. The model processes the prompt and produces a relevant text output as its response. Below, we have an overview on how to use the Chat Completion API to generate text and engage in conversational interactions with Mistral AI models.

### Use Chat Completions

The [Chat Completion API](https://docs.mistral.ai/api/#tag/chat) accepts a list of chat messages as input and generates a response. This response is in the form of a new chat message with the role "assistant" as output, the "content" of each response can either be a `string` or a `list` of chunks with different kinds of chunk types for different features. Visit our [API spec](https://docs.mistral.ai/api) for more details.

For non-streaming chat completions requests, you will provid a list of messages and the model will return a **single full completion response**. This response will contain the full completion **until the model decides to stop or the maximum number of tokens is reached**, important to know that the **longer the output and full completion, the higher the latency**.

Note that the response content of the model can have **interleaved events** instead of a single string, such as [citations](https://docs.mistral.ai/capabilities/citations) and [tool calls](https://docs.mistral.ai/capabilities/function_calling).  
The content can be either a string, the most standard usage of llms:

- `{'content': '...'}`

...or a list of different types of contents:

- `{'content': [{'type': 'text', 'text': '...'}, {'type': '...', '...': [...]}, ...]}`.

Chat `messages` are a collection of prompts or messages, with each message having a specific role assigned to it, such as "system," "user," "assistant," or "tool."

- A `system message` is an **optional** message that sets the behavior and context for an AI assistant in a conversation, such as modifying its personality or providing specific instructions. A system message can include task instructions, personality traits, contextual information, creativity constraints, and other relevant guidelines to help the AI better understand and respond to the user's input. See the [prompting](https://docs.mistral.ai/capabilities/completion/prompting_capabilities) for explanations on prompting capabilities in general.
- A `user message` is a message sent from the perspective of the human in a conversation with an AI assistant. It typically provides a request, question, or comment that the AI assistant should respond to. User prompts allow the human to initiate and guide the conversation, and they can be used to request information, ask for help, provide feedback, or engage in other types of interaction with the AI.
- An `assistant message` is a message sent by the AI assistant back to the user. It is usually meant to reply to a previous user message by following its instructions, but you can also find it at the beginning of a conversation, for example to greet the user.
- A `tool message` only appears in the context of **function calling**, it is used at the final response formulation step when the model has to format the tool call's output for the user. To learn more about function calling, see the [guide](https://docs.mistral.ai/capabilities/completion/function_calling).

When to use `user` prompt vs. `system` message then `user` message?

- You can either combine your `system` message and `user` message into a single `user` message or separate them into two distinct messages.
- We recommend you experiment with both ways to determine which one works better for your specific use case.

Chat Completions can be used for multi-turn conversations. This means that you can send multiple messages back and forth between the user and the assistant. This is useful for applications like chatbots, where the user can have a conversation with the assistant.

Interesting to note that you ma have different events interleaved between these interactions, such as tool calls for function calling, or even handoffs when handling agents.

if you are interested on a simplified way to handle multi-turn conversations, you may want to check out our [Agents and Conversations APIs](https://docs.mistral.ai/agents/introduction). Managing multi-turn conversations can be complex, and our APIs are designed to simplify this process while providing you with built-in tools and connectors.

Our Chat Completions service also has other features that can be used to customize your requests.

- The `prefix` flag enables prepending content to the assistant's response content. When used in a message, it allows the addition of an assistant's message at the end of the list, which will be prepended to the assistant's response.
- The `safe_prompt` flag is used to force chat completion to be moderated against sensitive content (see [Guardrailing](https://docs.mistral.ai/capabilities/completion/guardrailing)).
- A `stop` sequence allows forcing the model to stop generating after one or more chosen tokens or strings. The output will not contain the stop sequence.

You can find short examples on how to use them below.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.

This was a simple introduction to our Chat Completions service, however we have a lot more to offer we recommend taking a look; from [Vision](https://docs.mistral.ai/capabilities/vision) capabilities, to [Function Calling](https://docs.mistral.ai/capabilities/completion/function-calling), [Predicted Outputs](https://docs.mistral.ai/capabilities/completion/predicted-outputs), [Structured Outputs](https://docs.mistral.ai/capabilities/completion/structured-output) and much more.