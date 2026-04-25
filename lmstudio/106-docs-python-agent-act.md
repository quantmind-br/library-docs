---
title: The `.act()` call
url: https://lmstudio.ai/docs/python/agent/act
source: sitemap
fetched_at: 2026-04-07T21:31:16.577725158-03:00
rendered_js: false
word_count: 891
summary: This document explains the concept of 'execution rounds' in LLM tool use, detailing the cycle of running a tool, providing results to the model, and waiting for the next decision. It also covers advanced topics like parallel tool calls, model selection best practices, and various progress callbacks available during complex agent interactions.
tags:
    - execution-rounds
    - tool-calling
    - llm-agents
    - progress-callbacks
    - api-usage
    - model-selection
category: concept
---

We introduce the concept of execution "rounds" to describe the combined process of running a tool, providing its output to the LLM, and then waiting for the LLM to decide what to do next.

**Execution Round**

```

 • run a tool →
 ↑   • provide the result to the LLM →
 │       • wait for the LLM to generate a response
 │
 └────────────────────────────────────────┘ └➔ (return)
```

A model might choose to run tools multiple times before returning a final result. For example, if the LLM is writing code, it might choose to compile or run the program, fix errors, and then run it again, rinse and repeat until it gets the desired result.

With this in mind, we say that the `.act()` API is an automatic "multi-round" tool calling API.

### Quick Example[](#quick-example)

### What does it mean for an LLM to "use a tool"?[](#what-does-it-mean-for-an-llm-to-use-a-tool)

LLMs are largely text-in, text-out programs. So, you may ask "how can an LLM use a tool?". The answer is that some LLMs are trained to ask the human to call the tool for them, and expect the tool output to to be provided back in some format.

Imagine you're giving computer support to someone over the phone. You might say things like "run this command for me ... OK what did it output? ... OK now click there and tell me what it says ...". In this case you're the LLM! And you're "calling tools" vicariously through the person on the other side of the line.

### Running multiple tool calls in parallel[](#running-multiple-tool-calls-in-parallel)

By default, version 1.4.0 and later of the Python SDK will only run a single tool call request at a time, even if the model requests multiple tool calls in a single response message. This ensures the requests will be processed correctly even if the tool implementations do not support multiple concurrent calls.

When the tool implementations are known to be thread-safe, and are both slow and frequent enough to be worth running in parallel, the `max_parallel_tool_calls` option specifies the maximum number of tool call requests that will be processed in parallel from a single model response. This value defaults to 1 (waiting for each tool call to complete before starting the next one). Setting this value to `None` will automatically scale the maximum number of parallel tool calls to a multiple of the number of CPU cores available to the process.

### Important: Model Selection[](#important-model-selection)

The model selected for tool use will greatly impact performance.

Some general guidance when selecting a model:

- Not all models are capable of intelligent tool use
- Bigger is better (i.e., a 7B parameter model will generally perform better than a 3B parameter model)
- We've observed [Qwen2.5-7B-Instruct](https://model.lmstudio.ai/download/lmstudio-community/Qwen2.5-7B-Instruct-GGUF) to perform well in a wide variety of cases
- This guidance may change

### Example: Multiple Tools[](#example-multiple-tools)

The following code demonstrates how to provide multiple tools in a single `.act()` call.

### Example: Chat Loop with Create File Tool[](#example-chat-loop-with-create-file-tool)

The following code creates a conversation loop with an LLM agent that can create files.

### Progress Callbacks[](#progress-callbacks)

Complex interactions with a tool using agent may take some time to process.

The regular progress callbacks for any prediction request are available, but the expected capabilities differ from those for single round predictions.

- `on_prompt_processing_progress`: called during prompt processing for each prediction round. Receives the progress ratio (as a float) and the round index as positional arguments.
- `on_first_token`: called after prompt processing is complete for each prediction round. Receives the round index as its sole argument.
- `on_prediction_fragment`: called for each prediction fragment received by the client. Receives the prediction fragment and the round index as positional arguments.
- `on_message`: called with an assistant response message when each prediction round is complete, and with tool result messages as each tool call request is completed. Intended for appending received messages to a chat history instance, and hence does *not* receive the round index as an argument.

The following additional callbacks are available to monitor the prediction rounds:

- `on_round_start`: called before submitting the prediction request for each round. Receives the round index as its sole argument.
- `on_prediction_completed`: called after the prediction for the round has been completed, but before any requested tool calls have been initiated. Receives the round's prediction result as its sole argument. A round prediction result is a regular prediction result with an additional `round_index` attribute.
- `on_round_end`: called after any tool call requests for the round have been resolved.

Finally, applications may request notifications when agents emit invalid tool requests:

- `handle_invalid_tool_request`: called when a tool request was unable to be processed. Receives the exception that is about to be reported, as well as the original tool request that resulted in the problem. When no tool request is given, this is purely a notification of an unrecoverable error before the agent interaction raises the given exception (allowing the application to raise its own exception instead). When a tool request is given, it indicates that rather than being raised locally, the text description of the exception is going to be passed back to the agent as the result of that failed tool request. In these cases, the callback may either return `None` to indicate that the error description should be sent to the agent, raise the given exception (or a different exception) locally, or return a text string that should be sent to the agent instead of the error description.

For additional details on defining tools, and an example of overriding the invalid tool request handling to raise all exceptions locally instead of passing them to back the agent, refer to [Tool Definition](https://lmstudio.ai/docs/python/agent/tools.md).