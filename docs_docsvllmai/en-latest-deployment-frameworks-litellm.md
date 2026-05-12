---
title: LiteLLM - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/litellm/
source: sitemap
fetched_at: 2026-05-07T21:11:49.182849081-03:00
rendered_js: false
word_count: 124
summary: This document provides instructions on how to integrate and use the LiteLLM library to interface with vLLM servers for chat completion and embedding tasks.
tags:
    - litellm
    - vllm
    - llm-deployment
    - chat-completion
    - embeddings
    - model-integration
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/litellm.md "Edit this page")

[LiteLLM](https://github.com/BerriAI/litellm) call all LLM APIs using the OpenAI format \[Bedrock, Huggingface, VertexAI, TogetherAI, Azure, OpenAI, Groq etc.]

LiteLLM manages:

- Translate inputs to provider's `completion`, `embedding`, and `image_generation` endpoints
- [Consistent output](https://docs.litellm.ai/docs/completion/output), text responses will always be available at `['choices'][0]['message']['content']`
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
- Set Budgets & Rate limits per project, api key, model [LiteLLM Proxy Server (LLM Gateway)](https://docs.litellm.ai/docs/simple_proxy)

And LiteLLM supports all models on VLLM.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM and litellm environment:

## Deploy[¶](#deploy "Permanent link")

### Chat completion[¶](#chat-completion "Permanent link")

1. Start the vLLM server with the supported chat completion model, e.g.
   
   ```
   vllmserveqwen/Qwen1.5-0.5B-Chat
   ```
2. Call it with litellm:

Code

```
importlitellm 

messages = [{"content": "Hello, how are you?", "role": "user"}]

# hosted_vllm is prefix key word and necessary
response = litellm.completion(
    model="hosted_vllm/qwen/Qwen1.5-0.5B-Chat", # pass the vllm model name
    messages=messages,
    api_base="http://{your-vllm-server-host}:{your-vllm-server-port}/v1",
    temperature=0.2,
    max_tokens=80,
)

print(response)
```

### Embeddings[¶](#embeddings "Permanent link")

1. Start the vLLM server with the supported embedding model, e.g.
   
   ```
   vllmserveBAAI/bge-base-en-v1.5
   ```
2. Call it with litellm:

```
fromlitellmimport embedding   
importos

os.environ["HOSTED_VLLM_API_BASE"] = "http://{your-vllm-server-host}:{your-vllm-server-port}/v1"

# hosted_vllm is prefix key word and necessary
# pass the vllm model name
embedding = embedding(model="hosted_vllm/BAAI/bge-base-en-v1.5", input=["Hello world"])

print(embedding)
```

For details, see the tutorial [Using vLLM in LiteLLM](https://docs.litellm.ai/docs/providers/vllm).