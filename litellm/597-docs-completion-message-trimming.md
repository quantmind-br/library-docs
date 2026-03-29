---
title: Trimming Input Messages | liteLLM
url: https://docs.litellm.ai/docs/completion/message_trimming
source: sitemap
fetched_at: 2026-01-21T19:44:30.919235102-03:00
rendered_js: false
word_count: 95
summary: This document explains how to use the litellm.trim_messages() utility function to ensure message lists stay within model token limits or a specified maximum token count.
tags:
    - litellm
    - token-management
    - message-trimming
    - context-window
    - python-sdk
category: reference
---

**Use litellm.trim\_messages() to ensure messages does not exceed a model's token limit or specified `max_tokens`**

## Usage[​](#usage "Direct link to Usage")

```
from litellm import completion
from litellm.utils import trim_messages

response = completion(
    model=model,
    messages=trim_messages(messages, model)# trim_messages ensures tokens(messages) < max_tokens(model)
)
```

## Usage - set max\_tokens[​](#usage---set-max_tokens "Direct link to Usage - set max_tokens")

```
from litellm import completion
from litellm.utils import trim_messages

response = completion(
    model=model,
    messages=trim_messages(messages, model, max_tokens=10),# trim_messages ensures tokens(messages) < max_tokens
)
```

## Parameters[​](#parameters "Direct link to Parameters")

The function uses the following parameters:

- `messages`:\[Required] This should be a list of input messages
- `model`:\[Optional] This is the LiteLLM model being used. This parameter is optional, as you can alternatively specify the `max_tokens` parameter.
- `max_tokens`:\[Optional] This is an int, manually set upper limit on messages
- `trim_ratio`:\[Optional] This represents the target ratio of tokens to use following trimming. It's default value is 0.75, which implies that messages will be trimmed to utilise about 75%