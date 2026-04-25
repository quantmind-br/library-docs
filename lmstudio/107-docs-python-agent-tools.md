---
title: Tool Definition
url: https://lmstudio.ai/docs/python/agent/tools
source: sitemap
fetched_at: 2026-04-07T21:31:18.682218943-03:00
rendered_js: false
word_count: 425
summary: This document explains how to define and use tools with language models by passing Python functions or `ToolFunctionDef` objects. It also details how error handling for tool calls is managed by default and through custom callbacks.
tags:
    - tool-definition
    - llm-integration
    - agent-development
    - error-handling
    - python-sdk
category: guide
---

You can define tools as regular Python functions and pass them to the model in the `act()` call. Alternatively, tools can be defined with `lmstudio.ToolFunctionDef` in order to control the name and description passed to the language model.

Follow one of the following examples to define functions as tools (the first approach is typically going to be the most convenient):

**Important**: The tool name, description, and the parameter definitions are all passed to the model!

This means that your wording will affect the quality of the generation. Make sure to always provide a clear description of the tool so the model knows how to use it.

Tools can also have external effects, such as creating files or calling programs and even APIs. By implementing tools with external effects, you can essentially turn your LLMs into autonomous agents that can perform tasks on your local machine.

### Tool Definition[](#tool-definition)

### Example code using the `create_file` tool:[](#example-code-using-the-createfile-tool)

By default, version 1.3.0 and later of the Python SDK will automatically convert exceptions raised by tool calls to text and report them back to the language model. In many cases, when notified of an error in this way, a language model is able to either adjust its request to avoid the failure, or else accept the failure as a valid response to its request (consider a prompt like `Attempt to divide 1 by 0 using the provided tool. Explain the result.`, where the expected response is an explanation of the `ZeroDivisionError` exception the Python interpreter raises when instructed to divide by zero).

This error handling behaviour can be overridden using the `handle_invalid_tool_request` callback. For example, the following code reverts the error handling back to raising exceptions locally in the client:

When a tool request is passed in, the callback results are processed as follows:

- `None`: the original exception text is passed to the LLM unmodified
- a string: the returned string is passed to the LLM instead of the original exception text
- raising an exception (whether the passed in exception or a new exception): the raised exception is propagated locally in the client, terminating the prediction process

If no tool request is passed in, the callback invocation is a notification only, and the exception cannot be converted to text for passing pack to the LLM (although it can still be replaced with a different exception). These cases indicate failures in the expected communication with the server API that mean the prediction process cannot reasonably continue, so if the callback doesn't raise an exception, the calling code will raise the original exception directly.