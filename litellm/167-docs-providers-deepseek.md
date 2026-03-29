---
title: Deepseek | liteLLM
url: https://docs.litellm.ai/docs/providers/deepseek
source: sitemap
fetched_at: 2026-01-21T19:48:55.125522429-03:00
rendered_js: false
word_count: 103
summary: This document provides instructions and code samples for integrating Deepseek AI models via LiteLLM, including support for chat, coder, and reasoning models with specialized thinking modes.
tags:
    - deepseek
    - litellm
    - python
    - llm-api
    - streaming
    - reasoning-models
category: guide
---

[https://deepseek.com/](https://deepseek.com/)

**We support ALL Deepseek models, just set `deepseek/` as a prefix when sending completion requests**

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['DEEPSEEK_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['DEEPSEEK_API_KEY']=""
response = completion(
    model="deepseek/deepseek-chat",
    messages=[
{"role":"user","content":"hello from litellm"}
],
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['DEEPSEEK_API_KEY']=""
response = completion(
    model="deepseek/deepseek-chat",
    messages=[
{"role":"user","content":"hello from litellm"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

## Supported Models - ALL Deepseek Models Supported\![​](#supported-models---all-deepseek-models-supported "Direct link to Supported Models - ALL Deepseek Models Supported!")

We support ALL Deepseek models, just set `deepseek/` as a prefix when sending completion requests

Model NameFunction Calldeepseek-chat`completion(model="deepseek/deepseek-chat", messages)`deepseek-coder`completion(model="deepseek/deepseek-coder", messages)`

## Reasoning Models[​](#reasoning-models "Direct link to Reasoning Models")

Model NameFunction Calldeepseek-reasoner`completion(model="deepseek/deepseek-reasoner", messages)`

### Thinking / Reasoning Mode[​](#thinking--reasoning-mode "Direct link to Thinking / Reasoning Mode")

Enable thinking mode for DeepSeek reasoner models using `thinking` or `reasoning_effort` parameters:

- thinking param
- reasoning\_effort param

```
from litellm import completion
import os

os.environ['DEEPSEEK_API_KEY']=""

resp = completion(
    model="deepseek/deepseek-reasoner",
    messages=[{"role":"user","content":"What is 2+2?"}],
    thinking={"type":"enabled"},
)
print(resp.choices[0].message.reasoning_content)# Model's reasoning
print(resp.choices[0].message.content)# Final answer
```

note

DeepSeek only supports `{"type": "enabled"}` - unlike Anthropic, it doesn't support `budget_tokens`. Any `reasoning_effort` value other than `"none"` enables thinking mode.

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

- SDK
- PROXY

```
from litellm import completion
import os

os.environ['DEEPSEEK_API_KEY']=""
resp = completion(
    model="deepseek/deepseek-reasoner",
    messages=[{"role":"user","content":"Tell me a joke."}],
)

print(
    resp.choices[0].message.reasoning_content
)
```