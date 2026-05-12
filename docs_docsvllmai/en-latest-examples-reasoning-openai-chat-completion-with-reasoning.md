---
title: OpenAI Chat Completion With Reasoning
url: https://docs.vllm.ai/en/latest/examples/reasoning/openai_chat_completion_with_reasoning/
source: sitemap
fetched_at: 2026-05-07T21:13:39.858314959-03:00
rendered_js: false
word_count: 56
summary: This document provides a code example demonstrating how to interface with reasoning-capable models in vLLM using the OpenAI Python client library to access both reasoning and response content.
tags:
    - vllm
    - openai-client
    - reasoning-models
    - chat-completion
    - deepseek-r1
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/reasoning/openai_chat_completion_with_reasoning.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/reasoning/openai\_chat\_completion\_with\_reasoning.py](https://github.com/vllm-project/vllm/blob/main/examples/reasoning/openai_chat_completion_with_reasoning.py).

````
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
An example shows how to generate chat completions from reasoning models
like DeepSeekR1.

To run this example, you need to start the vLLM server
with the reasoning parser:

```bash
vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
    --reasoning-parser deepseek_r1
```

This example demonstrates how to generate chat completions from reasoning models
using the OpenAI Python client library.
"""

fromopenaiimport OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"


defmain():
    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    models = client.models.list()
    model = models.data[0].id

    # Round 1
    messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
    # ruff: noqa: E501
    # For granite, add: `extra_body={"chat_template_kwargs": {"thinking": True}}`
    response = client.chat.completions.create(model=model, messages=messages)

    reasoning = response.choices[0].message.reasoning
    content = response.choices[0].message.content

    print("reasoning for Round 1:", reasoning)
    print("content for Round 1:", content)

    # Round 2
    messages.append({"role": "assistant", "content": content})
    messages.append(
        {
            "role": "user",
            "content": "How many Rs are there in the word 'strawberry'?",
        }
    )
    response = client.chat.completions.create(model=model, messages=messages)

    reasoning = response.choices[0].message.reasoning
    content = response.choices[0].message.content

    print("reasoning for Round 2:", reasoning)
    print("content for Round 2:", content)


if __name__ == "__main__":
    main()
````