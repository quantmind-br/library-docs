---
title: litellm.aembedding() | liteLLM
url: https://docs.litellm.ai/docs/embedding/async_embedding
source: sitemap
fetched_at: 2026-01-21T19:45:05.113597275-03:00
rendered_js: false
word_count: 11
summary: This document explains how to perform asynchronous text embedding calls using LiteLLM's aembedding function.
tags:
    - litellm
    - asynchronous
    - embeddings
    - python
    - aembedding
category: api
---

LiteLLM provides an asynchronous version of the `embedding` function called `aembedding`

```
from litellm import aembedding
import asyncio

asyncdeftest_get_response():
    response =await aembedding('text-embedding-ada-002',input=["good morning from litellm"])
return response

response = asyncio.run(test_get_response())
print(response)
```