---
title: Haystack - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/haystack/
source: sitemap
fetched_at: 2026-05-07T21:11:45.590381128-03:00
rendered_js: false
word_count: 123
summary: This document provides instructions on integrating the vLLM serving engine with the Haystack framework to deploy and utilize LLMs within NLP pipelines.
tags:
    - vllm
    - haystack
    - llm-deployment
    - rag
    - openai-api-compatibility
    - model-serving
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/haystack.md "Edit this page")

[Haystack](https://github.com/deepset-ai/haystack) is an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. Whether you want to perform retrieval-augmented generation (RAG), document search, question answering or answer generation, Haystack can orchestrate state-of-the-art embedding models and LLMs into pipelines to build end-to-end NLP applications and solve your use case.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM and Haystack environment:

```
pipinstallvllmhaystack-ai
```

## Deploy[¶](#deploy "Permanent link")

1. Start the vLLM server with the supported chat completion model, e.g.
   
   ```
   vllmservemistralai/Mistral-7B-Instruct-v0.1
   ```
2. Use the `OpenAIGenerator` and `OpenAIChatGenerator` components in Haystack to query the vLLM server.

Code

```
fromhaystack.components.generators.chatimport OpenAIChatGenerator
fromhaystack.dataclassesimport ChatMessage
fromhaystack.utilsimport Secret

generator = OpenAIChatGenerator(
    # for compatibility with the OpenAI API, a placeholder api_key is needed
    api_key=Secret.from_token("VLLM-PLACEHOLDER-API-KEY"),
    model="mistralai/Mistral-7B-Instruct-v0.1",
    api_base_url="http://{your-vLLM-host-ip}:{your-vLLM-host-port}/v1",
    generation_kwargs={"max_tokens": 512},
)

response = generator.run(
  messages=[ChatMessage.from_user("Hi. Can you help me plan my next trip to Italy?")]
)

print("-"*30)
print(response)
print("-"*30)

------------------------------
{'replies': [ChatMessage(_role=<ChatRole.ASSISTANT: 'assistant'>, _content=[TextContent(text=' Of course! Where in Italy would you like to go and what type of trip are you looking to plan?')], _name=None, _meta={'model': 'mistralai/Mistral-7B-Instruct-v0.1', 'index': 0, 'finish_reason': 'stop', 'usage': {'completion_tokens': 23, 'prompt_tokens': 21, 'total_tokens': 44, 'completion_tokens_details': None, 'prompt_tokens_details': None}})]}
------------------------------
```

For details, see the tutorial [Using vLLM in Haystack](https://github.com/deepset-ai/haystack-integrations/blob/main/integrations/vllm.md).