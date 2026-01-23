---
title: Usage | liteLLM
url: https://docs.litellm.ai/docs/completion/usage
source: sitemap
fetched_at: 2026-01-21T19:44:47.125713965-03:00
rendered_js: false
word_count: 65
summary: This document explains how to retrieve token usage statistics in LiteLLM when using streaming responses by enabling the include_usage option in stream_options.
tags:
    - litellm
    - token-usage
    - streaming
    - openai-compatibility
    - usage-statistics
category: configuration
---

LiteLLM returns the OpenAI compatible usage object across all providers.

if `stream_options={"include_usage": True}` is set, an additional chunk will be streamed before the data: \[DONE] message. The usage field on this chunk shows the token usage statistics for the entire request, and the choices field will always be an empty array. All other chunks will also include a usage field, but with a null value.

```
from litellm import completion 

completion = completion(
  model="gpt-4o",
  messages=[
{"role":"system","content":"You are a helpful assistant."},
{"role":"user","content":"Hello!"}
],
  stream=True,
  stream_options={"include_usage":True}
)

for chunk in completion:
print(chunk.choices[0].delta)

```