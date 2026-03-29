---
title: Using Text Completion Format - with Completion() | liteLLM
url: https://docs.litellm.ai/docs/tutorials/text_completion
source: sitemap
fetched_at: 2026-01-21T19:55:52.706748357-03:00
rendered_js: false
word_count: 33
summary: This tutorial explains how to use LiteLLM to interface with various language models using the OpenAI Text Completion format. It provides implementation examples for models like GPT-3.5 and Llama-2 using the text_completion function.
tags:
    - litellm
    - text-completion
    - openai-api-format
    - python-library
    - llm-integration
    - gpt-3-5
    - llama-2
category: tutorial
---

If your prefer interfacing with the OpenAI Text Completion format this tutorial covers how to use LiteLLM in this format

```
response = openai.Completion.create(
    model="text-davinci-003",
    prompt='Write a tagline for a traditional bavarian tavern',
    temperature=0,
    max_tokens=100)
```

## Using LiteLLM in the Text Completion format[​](#using-litellm-in-the-text-completion-format "Direct link to Using LiteLLM in the Text Completion format")

### With gpt-3.5-turbo[​](#with-gpt-35-turbo "Direct link to With gpt-3.5-turbo")

```
from litellm import text_completion
response = text_completion(
    model="gpt-3.5-turbo",
    prompt='Write a tagline for a traditional bavarian tavern',
    temperature=0,
    max_tokens=100)
```

### With text-davinci-003[​](#with-text-davinci-003 "Direct link to With text-davinci-003")

```
response = text_completion(
    model="text-davinci-003",
    prompt='Write a tagline for a traditional bavarian tavern',
    temperature=0,
    max_tokens=100)
```

### With llama2[​](#with-llama2 "Direct link to With llama2")

```
response = text_completion(
    model="togethercomputer/llama-2-70b-chat",
    prompt='Write a tagline for a traditional bavarian tavern',
    temperature=0,
    max_tokens=100)
```