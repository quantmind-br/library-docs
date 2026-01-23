---
title: Clarifai | liteLLM
url: https://docs.litellm.ai/docs/providers/clarifai
source: sitemap
fetched_at: 2026-01-21T19:48:39.63495613-03:00
rendered_js: false
word_count: 15
summary: This document demonstrates how to use the LiteLLM library to integrate various Clarifai-hosted large language models into applications, covering basic completion, streaming, and tool calling.
tags:
    - clarifai
    - litellm
    - llm-integration
    - streaming
    - tool-calling
    - python-sdk
category: tutorial
---

Anthropic, OpenAI, Qwen, xAI, Gemini and most of Open soured LLMs are Supported on Clarifai.

```
import os
from litellm import completion

os.environ["CLARIFAI_API_KEY"]=""

response = completion(
  model="clarifai/openai.chat-completion.gpt-oss-20b",
  messages=[{"content":"Tell me a joke about physics?","role":"user"}]
)
```

```
import litellm

for chunk in litellm.completion(
    model="clarifai/openai.chat-completion.gpt-oss-20b",
    api_key="CLARIFAI_API_KEY",
    messages=[
{"role":"user","content":"Tell me a fun fact about space."}
],
    stream=True,
):
print(chunk.choices[0].delta)
```

```
import litellm

tools =[{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get current temperature for a given location.",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"City and country e.g. Tokyo, Japan"
}
},
"required":["location"],
"additionalProperties":False
},
}
}
}]

response = litellm.completion(
    model="clarifai/openai.chat-completion.gpt-oss-20b",
    api_key="CLARIFAI_API_KEY",
    messages=[{"role":"user","content":"What is the weather in Paris today?"}],
    tools=tools,
)

print(response.choices[0].message.tool_calls)
```