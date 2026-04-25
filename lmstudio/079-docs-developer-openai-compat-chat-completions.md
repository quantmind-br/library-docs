---
title: Chat Completions
url: https://lmstudio.ai/docs/developer/openai-compat/chat-completions
source: sitemap
fetched_at: 2026-04-07T21:30:41.721920303-03:00
rendered_js: false
word_count: 46
summary: This document illustrates how to make a chat completion request using the OpenAI Python library, providing code examples and listing supported payload parameters for generating model responses.
tags:
    - python-example
    - chat-completion
    - api-call
    - openai-sdk
    - inference-parameters
category: tutorial
---

- Method: `POST`
- Prompt template is applied automatically for chat‑tuned models
- Provide inference parameters (temperature, top\_p, etc.) in the payload
- See OpenAI docs: [https://platform.openai.com/docs/api-reference/chat](https://platform.openai.com/docs/api-reference/chat)
- Tip: keep a terminal open with [`lms log stream`](https://lmstudio.ai/docs/cli/serve/log-stream) to inspect model input

##### Python example

```

from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="model-identifier",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
```

### Supported payload parameters[](#supported-payload-parameters)

See [https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create) for parameter semantics.

```

model
top_p
top_k
messages
temperature
max_tokens
stream
stop
presence_penalty
frequency_penalty
logit_bias
repeat_penalty
seed
```