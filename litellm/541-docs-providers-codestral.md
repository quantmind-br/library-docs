---
title: Codestral API [Mistral AI] | liteLLM
url: https://docs.litellm.ai/docs/providers/codestral
source: sitemap
fetched_at: 2026-01-21T19:48:43.734949477-03:00
rendered_js: false
word_count: 96
summary: This document provides instructions and code examples for integrating Codestral models via LiteLLM for both code completions and chat interactions.
tags:
    - codestral
    - litellm
    - text-completion
    - chat-completion
    - python
    - api-integration
category: reference
---

Codestral is available in select code-completion plugins but can also be queried directly. See the documentation for more details.

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['CODESTRAL_API_KEY']
```

## FIM / Completions[​](#fim--completions "Direct link to FIM / Completions")

- No Streaming
- Streaming

#### Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
import os
import litellm

os.environ['CODESTRAL_API_KEY']

response =await litellm.atext_completion(
    model="text-completion-codestral/codestral-2405",
    prompt="def is_odd(n): \n return n % 2 == 1 \ndef test_is_odd():",
    suffix="return True",# optional
    temperature=0,# optional
    top_p=1,# optional
    max_tokens=10,# optional
    min_tokens=10,# optional
    seed=10,# optional
    stop=["return"],# optional
)
```

#### Expected Response[​](#expected-response "Direct link to Expected Response")

```
{
"id":"b41e0df599f94bc1a46ea9fcdbc2aabe",
"object":"text_completion",
"created":1589478378,
"model":"codestral-latest",
"choices":[
{
"text":"\n assert is_odd(1)\n assert",
"index":0,
"logprobs":null,
"finish_reason":"length"
}
],
"usage":{
"prompt_tokens":5,
"completion_tokens":7,
"total_tokens":12
}
}

```

### Supported Models[​](#supported-models "Direct link to Supported Models")

All models listed here [https://docs.mistral.ai/platform/endpoints](https://docs.mistral.ai/platform/endpoints) are supported. We actively maintain the list of models, pricing, token window, etc. [here](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json).

Model NameFunction CallCodestral Latest`completion(model="text-completion-codestral/codestral-latest", messages)`Codestral 2405`completion(model="text-completion-codestral/codestral-2405", messages)`

## Chat Completions[​](#chat-completions "Direct link to Chat Completions")

- No Streaming
- Streaming

#### Sample Usage[​](#sample-usage-1 "Direct link to Sample Usage")

```
import os
import litellm

os.environ['CODESTRAL_API_KEY']

response =await litellm.acompletion(
    model="codestral/codestral-latest",
    messages=[
{
"role":"user",
"content":"Hey, how's it going?",
}
],
    temperature=0.0,# optional
    top_p=1,# optional
    max_tokens=10,# optional
    safe_prompt=False,# optional
    seed=12,# optional
)
```

#### Expected Response[​](#expected-response-2 "Direct link to Expected Response")

```
{
"id":"chatcmpl-123",
"object":"chat.completion",
"created":1677652288,
"model":"codestral/codestral-latest",
"system_fingerprint": None,
"choices":[{
"index":0,
"message":{
"role":"assistant",
"content":"\n\nHello there, how may I assist you today?",
},
"logprobs":null,
"finish_reason":"stop"
}],
"usage":{
"prompt_tokens":9,
"completion_tokens":12,
"total_tokens":21
}
}


```

### Supported Models[​](#supported-models-1 "Direct link to Supported Models")

All models listed here [https://docs.mistral.ai/platform/endpoints](https://docs.mistral.ai/platform/endpoints) are supported. We actively maintain the list of models, pricing, token window, etc. [here](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json).

Model NameFunction CallCodestral Latest`completion(model="codestral/codestral-latest", messages)`Codestral 2405`completion(model="codestral/codestral-2405", messages)`