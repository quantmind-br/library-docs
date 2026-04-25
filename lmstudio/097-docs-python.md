---
title: '`lmstudio-python` (Python SDK)'
url: https://lmstudio.ai/docs/python
source: sitemap
fetched_at: 2026-04-07T21:30:52.244256335-03:00
rendered_js: false
word_count: 512
summary: 'This document explains the `lmstudio-python` SDK, detailing its installation, key features like interacting with LLMs and creating agents, and describing different programming models for usage: interactive convenience, synchronous scoped resource, and asynchronous structured concurrency.'
tags:
    - llm-interaction
    - python-sdk
    - model-management
    - asynchronous-api
    - local-ai
category: guide
---

`lmstudio-python` provides you a set APIs to interact with LLMs, embeddings models, and agentic flows.

## Installing the SDK[](#installing-the-sdk "Link to 'Installing the SDK'")

`lmstudio-python` is available as a PyPI package. You can install it using pip.

For the source code and open source contribution, visit [lmstudio-python](https://github.com/lmstudio-ai/lmstudio-python) on GitHub.

## Features[](#features "Link to 'Features'")

- Use LLMs to [respond in chats](https://lmstudio.ai/docs/python/llm-prediction/chat-completion) or predict [text completions](https://lmstudio.ai/docs/python/llm-prediction/completion)
- Define functions as tools, and turn LLMs into [autonomous agents](https://lmstudio.ai/docs/python/agent) that run completely locally
- [Load](https://lmstudio.ai/docs/python/manage-models/loading), [configure](https://lmstudio.ai/docs/python/llm-prediction/parameters), and [unload](https://lmstudio.ai/docs/python/manage-models/loading) models from memory
- Generate embeddings for text, and more!

## Quick Example: Chat with a Llama Model[](#quick-example-chat-with-a-llama-model "Link to 'Quick Example: Chat with a Llama Model'")

### Getting Local Models[](#getting-local-models)

The above code requires the [qwen3-4b-2507](https://lmstudio.ai/models/qwen/qwen3-4b-2507) model. If you don't have the model, run the following command in the terminal to download it.

```

lms get qwen/qwen3-4b-2507
```

Read more about `lms get` in LM Studio's CLI [here](https://lmstudio.ai/docs/cli/get).

## Interactive Convenience, Deterministic Resource Management, or Structured Concurrency?[](#interactive-convenience-deterministic-resource-management-or-structured-concurrency)

As shown in the example above, there are three distinct approaches for working with the LM Studio Python SDK.

The first is the interactive convenience API (listed as "Python (convenience API)" in examples), which focuses on the use of a default LM Studio client instance for convenient interactions at a synchronous Python prompt, or when using Jupyter notebooks.

The second is a synchronous scoped resource API (listed as "Python (scoped resource API)" in examples), which uses context managers to ensure that allocated resources (such as network connections) are released deterministically, rather than potentially remaining open until the entire process is terminated.

The last is an asynchronous structured concurrency API (listed as "Python (asynchronous API)" in examples), which is designed for use in asynchronous programs that follow the design principles of ["structured concurrency"](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) in order to ensure the background tasks handling the SDK's connections to the API server host are managed correctly. Asynchronous applications which do not adhere to those design principles will need to rely on threaded access to the synchronous scoped resource API rather than attempting to use the SDK's native asynchronous API. Python SDK version 1.5.0 is the first version to fully support the asynchronous API.

Some examples are common between the interactive convenience API and the synchronous scoped resource API. These examples are listed as "Python (synchronous API)".

## Timeouts in the synchronous API[](#timeouts-in-the-synchronous-api "Link to 'Timeouts in the synchronous API'")

*Required Python SDK version*: **1.5.0**

Starting in Python SDK version 1.5.0, the synchronous API defaults to timing out after 60 seconds with no activity when waiting for a response or streaming event notification from the API server.

The number of seconds to wait for responses and event notifications can be adjusted using the `lmstudio.set_sync_api_timeout()` function. Setting the timeout to `None` disables the timeout entirely (restoring the behaviour of previous SDK versions).

The current synchronous API timeout can be queried using the `lmstudio.get_sync_api_timeout()` function.

## Timeouts in the asynchronous API[](#timeouts-in-the-asynchronous-api "Link to 'Timeouts in the asynchronous API'")

*Required Python SDK version*: **1.5.0**

As asynchronous coroutines support cancellation, there is no specific timeout support implemented in the asynchronous API. Instead, general purpose async timeout mechanisms, such as [`asyncio.wait_for()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for) or [`anyio.move_on_after()`](https://anyio.readthedocs.io/en/stable/cancellation.html#timeouts), should be used.