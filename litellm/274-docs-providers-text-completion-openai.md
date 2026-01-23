---
title: OpenAI (Text Completion) | liteLLM
url: https://docs.litellm.ai/docs/providers/text_completion_openai
source: sitemap
fetched_at: 2026-01-21T19:50:29.542518211-03:00
rendered_js: false
word_count: 119
summary: This document explains how to use OpenAI text completion and instruct models with LiteLLM, covering direct integration, environment setup, and proxy server configuration.
tags:
    - openai
    - litellm
    - text-completion
    - instruct-models
    - proxy-server
    - python-sdk
category: guide
---

LiteLLM supports OpenAI text completion models

### Required API Keys[​](#required-api-keys "Direct link to Required API Keys")

```
import os 
os.environ["OPENAI_API_KEY"]="your-api-key"
```

### Usage[​](#usage "Direct link to Usage")

```
import os 
from litellm import completion

os.environ["OPENAI_API_KEY"]="your-api-key"

# openai call
response = completion(
    model ="gpt-3.5-turbo-instruct",
    messages=[{"content":"Hello, how are you?","role":"user"}]
)
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

Here's how to call OpenAI models with the LiteLLM Proxy Server

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

- config.yaml
- config.yaml - proxy all OpenAI models
- CLI

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo                          # The `openai/` prefix will call openai.chat.completions.create
api_key: os.environ/OPENAI_API_KEY
-model_name: gpt-3.5-turbo-instruct
litellm_params:
model: text-completion-openai/gpt-3.5-turbo-instruct # The `text-completion-openai/` prefix will call openai.completions.create
api_key: os.environ/OPENAI_API_KEY
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+
- Langchain

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-3.5-turbo-instruct",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

## OpenAI Text Completion Models / Instruct Models[​](#openai-text-completion-models--instruct-models "Direct link to OpenAI Text Completion Models / Instruct Models")

Model NameFunction Callgpt-3.5-turbo-instruct`response = completion(model="gpt-3.5-turbo-instruct", messages=messages)`gpt-3.5-turbo-instruct-0914`response = completion(model="gpt-3.5-turbo-instruct-0914", messages=messages)`text-davinci-003`response = completion(model="text-davinci-003", messages=messages)`ada-001`response = completion(model="ada-001", messages=messages)`curie-001`response = completion(model="curie-001", messages=messages)`babbage-001`response = completion(model="babbage-001", messages=messages)`babbage-002`response = completion(model="babbage-002", messages=messages)`davinci-002`response = completion(model="davinci-002", messages=messages)`