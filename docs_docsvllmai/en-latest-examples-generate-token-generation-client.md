---
title: Token Generation Client - vLLM
url: https://docs.vllm.ai/en/latest/examples/generate/token_generation_client/
source: sitemap
fetched_at: 2026-05-07T21:13:06.842068625-03:00
rendered_js: false
word_count: 6
summary: This document provides a Python script demonstrating how to interact with the vLLM inference API using raw token IDs for text generation.
tags:
    - vllm
    - inference-api
    - token-generation
    - httpx
    - python-client
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/generate/token_generation_client.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/generate/token\_generation\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/generate/token_generation_client.py).

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
importhttpx
fromtransformersimport AutoTokenizer

GEN_ENDPOINT = "http://localhost:8000/inference/v1/generate"
DUMMY_API_KEY = "empty"
MODEL_NAME = "Qwen/Qwen3-0.6B"

transport = httpx.HTTPTransport()
headers = {"Authorization": f"Bearer {DUMMY_API_KEY}"}
client = httpx.Client(
    transport=transport,
    base_url=GEN_ENDPOINT,
    timeout=600,
    headers=headers,
)
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "How many countries are in the EU?"},
]


defmain(client):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    token_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        enable_thinking=False,
        return_dict=True,
    ).input_ids
    payload = {
        "model": MODEL_NAME,
        "token_ids": token_ids,
        "sampling_params": {"max_tokens": 24, "temperature": 0.2, "detokenize": False},
        "stream": False,
    }
    resp = client.post(GEN_ENDPOINT, json=payload)
    resp.raise_for_status()
    data = resp.json()
    print(data)
    print("-" * 50)
    print("Token generation results:")
    res = tokenizer.decode(data["choices"][0]["token_ids"])
    print(res)
    print("-" * 50)


if __name__ == "__main__":
    main(client)
```