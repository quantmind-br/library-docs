---
title: Async - DSPy
url: https://dspy.ai/tutorials/async/
source: sitemap
fetched_at: 2026-01-23T08:03:37.323005523-03:00
rendered_js: false
word_count: 437
summary: This guide explains how to implement asynchronous programming in DSPy using methods like acall and aforward to build high-performance, concurrent applications. It covers the integration of async tools and the creation of custom asynchronous modules for scalable production environments.
tags:
    - dspy
    - async-programming
    - concurrency
    - python-asyncio
    - scalability
    - asynchronous-io
category: guide
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/tutorials/async/index.md "Edit this page")

## Async DSPy Programming[¶](#async-dspy-programming "Permanent link")

DSPy provides native support for asynchronous programming, allowing you to build more efficient and scalable applications. This guide will walk you through how to leverage async capabilities in DSPy, covering both built-in modules and custom implementations.

## Why Use Async in DSPy?[¶](#why-use-async-in-dspy "Permanent link")

Asynchronous programming in DSPy offers several benefits: - Improved performance through concurrent operations - Better resource utilization - Reduced waiting time for I/O-bound operations - Enhanced scalability for handling multiple requests

## When Should I use Sync or Async?[¶](#when-should-i-use-sync-or-async "Permanent link")

Choosing between synchronous and asynchronous programming in DSPy depends on your specific use case. Here's a guide to help you make the right choice:

Use Synchronous Programming When

- You're exploring or prototyping new ideas
- You're conducting research or experiments
- You're building small to medium-sized applications
- You need simpler, more straightforward code
- You want easier debugging and error tracking

Use Asynchronous Programming When:

- You're building a high-throughput service (high QPS)
- You're working with tools that only support async operations
- You need to handle multiple concurrent requests efficiently
- You're building a production service that requires high scalability

### Important Considerations[¶](#important-considerations "Permanent link")

While async programming offers performance benefits, it comes with some trade-offs:

- More complex error handling and debugging
- Potential for subtle, hard-to-track bugs
- More complex code structure
- Different code between ipython (Colab, Jupyter lab, Databricks notebooks, ...) and normal python runtime.

We recommend starting with synchronous programming for most development scenarios and switching to async only when you have a clear need for its benefits. This approach allows you to focus on the core logic of your application before dealing with the additional complexity of async programming.

## Using Built-in Modules Asynchronously[¶](#using-built-in-modules-asynchronously "Permanent link")

Most DSPy built-in modules support asynchronous operations through the `acall()` method. This method maintains the same interface as the synchronous `__call__` method but operates asynchronously.

Here's a basic example using `dspy.Predict`:

```
importdspy
importasyncio
importos

os.environ["OPENAI_API_KEY"] = "your_api_key"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
predict = dspy.Predict("question->answer")

async defmain():
    # Use acall() for async execution
    output = await predict.acall(question="why did a chicken cross the kitchen?")
    print(output)


asyncio.run(main())
```

### Working with Async Tools[¶](#working-with-async-tools "Permanent link")

DSPy's `Tool` class seamlessly integrates with async functions. When you provide an async function to `dspy.Tool`, you can execute it using `acall()`. This is particularly useful for I/O-bound operations or when working with external services.

```
importasyncio
importdspy
importos

os.environ["OPENAI_API_KEY"] = "your_api_key"

async deffoo(x):
    # Simulate an async operation
    await asyncio.sleep(0.1)
    print(f"I get: {x}")

# Create a tool from the async function
tool = dspy.Tool(foo)

async defmain():
    # Execute the tool asynchronously
    await tool.acall(x=2)

asyncio.run(main())
```

#### Using Async Tools in Synchronous Contexts[¶](#using-async-tools-in-synchronous-contexts "Permanent link")

If you need to call an async tool from synchronous code, you can enable automatic async-to-sync conversion:

```
importdspy

async defasync_tool(x: int) -> int:
"""An async tool that doubles a number."""
    await asyncio.sleep(0.1)
    return x * 2

tool = dspy.Tool(async_tool)

# Option 1: Use context manager for temporary conversion
with dspy.context(allow_tool_async_sync_conversion=True):
    result = tool(x=5)  # Works in sync context
    print(result)  # 10

# Option 2: Configure globally
dspy.configure(allow_tool_async_sync_conversion=True)
result = tool(x=5)  # Now works everywhere
print(result)  # 10
```

For more details on async tools, see the [Tools documentation](https://dspy.ai/learn/programming/tools/#async-tools).

Note: When using `dspy.ReAct` with tools, calling `acall()` on the ReAct instance will automatically execute all tools asynchronously using their `acall()` methods.

## Creating Custom Async DSPy Modules[¶](#creating-custom-async-dspy-modules "Permanent link")

To create your own async DSPy module, implement the `aforward()` method instead of `forward()`. This method should contain your module's async logic. Here's an example of a custom module that chains two async operations:

```
importdspy
importasyncio
importos

os.environ["OPENAI_API_KEY"] = "your_api_key"
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

classMyModule(dspy.Module):
    def__init__(self):
        self.predict1 = dspy.ChainOfThought("question->answer")
        self.predict2 = dspy.ChainOfThought("answer->simplified_answer")

    async defaforward(self, question, **kwargs):
        # Execute predictions sequentially but asynchronously
        answer = await self.predict1.acall(question=question)
        return await self.predict2.acall(answer=answer)


async defmain():
    mod = MyModule()
    result = await mod.acall(question="Why did a chicken cross the kitchen?")
    print(result)


asyncio.run(main())
```