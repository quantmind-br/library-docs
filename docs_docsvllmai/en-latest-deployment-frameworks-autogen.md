---
title: AutoGen - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/autogen/
source: sitemap
fetched_at: 2026-05-07T21:11:37.870894959-03:00
rendered_js: false
word_count: 58
summary: This document provides instructions for integrating vLLM with the AutoGen framework to enable multi-agent applications using locally hosted models.
tags:
    - vllm
    - autogen
    - multi-agent-systems
    - ai-deployment
    - python-integration
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/autogen.md "Edit this page")

[AutoGen](https://github.com/microsoft/autogen) is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM and [AutoGen](https://microsoft.github.io/autogen/0.2/docs/installation/) environment:

```
pipinstallvllm

# Install AgentChat and OpenAI client from Extensions
# AutoGen requires Python 3.10 or later.
pipinstall-U"autogen-agentchat""autogen-ext[openai]"
```

## Deploy[¶](#deploy "Permanent link")

1. Start the vLLM server with the supported chat completion model, e.g.
   
   ```
   vllmservemistralai/Mistral-7B-Instruct-v0.2
   ```
2. Call it with AutoGen:

Code

```
importasyncio
fromautogen_core.modelsimport UserMessage
fromautogen_ext.models.openaiimport OpenAIChatCompletionClient
fromautogen_core.modelsimport ModelFamily


async defmain() -> None:
    # Create a model client
    model_client = OpenAIChatCompletionClient(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        base_url="http://{your-vllm-host-ip}:{your-vllm-host-port}/v1",
        api_key="EMPTY",
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "family": ModelFamily.MISTRAL,
            "structured_output": True,
        },
    )

    messages = [UserMessage(content="Write a very short story about a dragon.", source="user")]

    # Create a stream.
    stream = model_client.create_stream(messages=messages)

    # Iterate over the stream and print the responses.
    print("Streamed responses:")
    async for response in stream:
        if isinstance(response, str):
            # A partial response is a string.
            print(response, flush=True, end="")
        else:
            # The last response is a CreateResult object with the complete message.
            print("\n\n------------\n")
            print("The complete response:", flush=True)
            print(response.content, flush=True)

    # Close the client when done.
    await model_client.close()


asyncio.run(main())
```

For details, see the tutorial:

- [Using vLLM in AutoGen](https://microsoft.github.io/autogen/0.2/docs/topics/non-openai-models/local-vllm/)
- [OpenAI-compatible API examples](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.models.openai.html#autogen_ext.models.openai.OpenAIChatCompletionClient)