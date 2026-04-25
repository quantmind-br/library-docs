---
title: The `.act()` call
url: https://lmstudio.ai/docs/typescript/agent/act
source: sitemap
fetched_at: 2026-04-07T21:31:56.599278755-03:00
rendered_js: false
word_count: 330
summary: This document introduces the concept of 'execution rounds' to describe the iterative process where an LLM runs tools, receives the output, and then decides on subsequent actions until a final result is achieved.
tags:
    - llm-tool-use
    - execution-rounds
    - multi-round-calling
    - agent-behavior
    - api-design
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

> ***NOTE:*** at this time, this code expects zod v3

### What does it mean for an LLM to "use a tool"?[](#what-does-it-mean-for-an-llm-to-use-a-tool)

LLMs are largely text-in, text-out programs. So, you may ask "how can an LLM use a tool?". The answer is that some LLMs are trained to ask the human to call the tool for them, and expect the tool output to to be provided back in some format.

Imagine you're giving computer support to someone over the phone. You might say things like "run this command for me ... OK what did it output? ... OK now click there and tell me what it says ...". In this case you're the LLM! And you're "calling tools" vicariously through the person on the other side of the line.

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