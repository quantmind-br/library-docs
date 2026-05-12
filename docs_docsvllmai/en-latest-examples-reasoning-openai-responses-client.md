---
title: OpenAI Responses Client - vLLM
url: https://docs.vllm.ai/en/latest/examples/reasoning/openai_responses_client/
source: sitemap
fetched_at: 2026-05-07T21:13:42.837077532-03:00
rendered_js: false
word_count: 6
summary: This document provides a code example for interacting with vLLM's OpenAI-compatible server to access reasoning models through the Responses API.
tags:
    - vllm
    - openai-api
    - reasoning-models
    - large-language-models
    - inference
    - client-implementation
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/reasoning/openai_responses_client.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/reasoning/openai\_responses\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/reasoning/openai_responses_client.py).

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Set up this example by starting a vLLM OpenAI-compatible server.
Reasoning models can be used through the Responses API as seen here
https://platform.openai.com/docs/api-reference/responses
For example:
vllm serve Qwen/Qwen3-8B --reasoning-parser qwen3

"""

fromopenaiimport OpenAI

input_messages = [{"role": "user", "content": "What model are you?"}]


defmain():
    base_url = "http://localhost:8000/v1"
    client = OpenAI(base_url=base_url, api_key="empty")
    model = "Qwen/Qwen3-8B"  # get_first_model(client)
    response = client.responses.create(
        model=model,
        input=input_messages,
    )

    for message in response.output:
        if message.type == "reasoning":
            # append reasoning message
            input_messages.append(message)

    response_2 = client.responses.create(
        model=model,
        input=input_messages,
    )
    print(response_2.output_text)
    # I am Qwen, a large language model developed by Alibaba Cloud.
    # I am designed to assist with a wide range of tasks, including
    # answering questions, creating content, coding, and engaging in
    # conversations. I can help with various topics and provide
    # information or support in multiple languages. How can I assist you today?


if __name__ == "__main__":
    main()
```