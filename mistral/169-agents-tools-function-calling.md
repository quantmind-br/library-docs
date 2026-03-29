---
title: Function Calling | Mistral Docs
url: https://docs.mistral.ai/agents/tools/function_calling
source: crawler
fetched_at: 2026-01-29T07:34:17.736740255-03:00
rendered_js: false
word_count: 224
summary: This document provides a guide on how to implement function calling with Mistral AI models, enabling the models to interact with external tools and APIs by generating structured arguments.
tags:
    - Mistral AI
    - Function Calling
    - API
    - LLM
category: guide
---

The core of an agent relies on its tool usage capabilities, enabling it to use and call tools and workflows depending on the task it must accomplish.

Built into our API, we provide [built-in tools](https://docs.mistral.ai/agents/tools/built-in) tools such as `websearch`, `code_interpreter`, `image_generation` and `document_library`. However, you can also use standard function tool calling by defining a JSON schema for your function.

You can also leverage our MCP Orchestration to implement local Function Calling, visit our [Local MCP docs](https://docs.mistral.ai/agents/mcp/#step-4-register-mcp-client) for further details.

For more information regarding function calling, we recommend to visit our [function calling docs](https://docs.mistral.ai/capabilities/function_calling).

To use function calling, we can either create an Agent or use the Conversations API directly without. Below we will show you how to create an Agent with function calling and use it.

We need to define our function that we want our model to call when needed, in this case, the function is a dummy for demonstration purposes.

Once defined, we provide a Shema corresponding to the same function.

The output of the agent creation is the agent object, which contains the agent ID, which we will use to start a conversation.

Then, to use it, we start a conversation or continue a previously existing one.

The model will output either an answer, or a function call, we need to detect and return the result of the expected function.