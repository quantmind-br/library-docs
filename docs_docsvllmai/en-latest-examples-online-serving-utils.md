---
title: Utils - vLLM
url: https://docs.vllm.ai/en/latest/examples/online_serving/utils/
source: sitemap
fetched_at: 2026-05-07T21:13:23.57960237-03:00
rendered_js: false
word_count: 6
summary: This document provides a utility function to retrieve and validate the first available model from a running vLLM server using the OpenAI Python client.
tags:
    - vllm
    - openai-client
    - model-retrieval
    - server-connectivity
    - python-utility
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/utils.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/online\_serving/utils.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/utils.py).

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
fromopenaiimport APIConnectionError, OpenAI
fromopenai.paginationimport SyncPage
fromopenai.types.modelimport Model


defget_first_model(client: OpenAI) -> str:
"""
    Get the first model from the vLLM server.
    """
    try:
        models: SyncPage[Model] = client.models.list()
    except APIConnectionError as e:
        raise RuntimeError(
            "Failed to get the list of models from the vLLM server at "
            f"{client.base_url} with API key {client.api_key}. Check\n"
            "1. the server is running\n"
            "2. the server URL is correct\n"
            "3. the API key is correct"
        ) frome

    if len(models.data) == 0:
        raise RuntimeError(f"No models found on the vLLM server at {client.base_url}")

    return models.data[0].id
```