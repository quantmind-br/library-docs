---
title: Embeddings
url: https://lmstudio.ai/docs/developer/openai-compat/embeddings
source: sitemap
fetched_at: 2026-04-07T21:30:44.180509818-03:00
rendered_js: false
word_count: 8
summary: This document demonstrates how to generate text embeddings using the OpenAI Python library by making a POST request.
tags:
    - openai-python
    - embeddings
    - api-call
    - text-embedding
    - http-post
category: tutorial
---

- Method: `POST`
- See OpenAI docs: [https://platform.openai.com/docs/api-reference/embeddings](https://platform.openai.com/docs/api-reference/embeddings)

##### Python example

```

from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_embedding(text, model="model-identifier"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input=[text], model=model).data[0].embedding

print(get_embedding("Once upon a time, there was a cat."))
```