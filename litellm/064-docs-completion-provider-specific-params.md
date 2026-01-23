---
title: Provider-specific Params | liteLLM
url: https://docs.litellm.ai/docs/completion/provider_specific_params
source: sitemap
fetched_at: 2026-01-21T19:44:42.069741168-03:00
rendered_js: false
word_count: 108
summary: This document explains how to pass provider-specific parameters through LiteLLM using the SDK or Proxy, allowing for non-OpenAI standard arguments in API requests.
tags:
    - litellm
    - provider-parameters
    - api-configuration
    - llm-proxy
    - python-sdk
category: guide
---

Providers might offer params not supported by OpenAI (e.g. top\_k). LiteLLM treats any non-openai param, as a provider-specific param, and passes it to the provider in the request body, as a kwarg. [**See Reserved Params**](https://github.com/BerriAI/litellm/blob/aa2fd29e48245f360e771a8810a69376464b195e/litellm/main.py#L700)

You can pass those in 2 ways:

- via completion(): We'll pass the non-openai param, straight to the provider as part of the request body.
  
  - e.g. `completion(model="claude-instant-1", top_k=3)`
- via provider-specific config variable (e.g. `litellm.OpenAIConfig()`).

## SDK Usage[​](#sdk-usage "Direct link to SDK Usage")

- OpenAI
- OpenAI Text Completion
- Azure OpenAI
- Anthropic
- Huggingface
- TogetherAI
- Ollama
- Replicate
- Petals
- Palm
- AI21
- Cohere

```
import litellm, os

# set env variables
os.environ["OPENAI_API_KEY"]="your-openai-key"

## SET MAX TOKENS - via completion() 
response_1 = litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"content":"Hello, how are you?","role":"user"}],
            max_tokens=10
)

response_1_text = response_1.choices[0].message.content

## SET MAX TOKENS - via config
litellm.OpenAIConfig(max_tokens=10)

response_2 = litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"content":"Hello, how are you?","role":"user"}],
)

response_2_text = response_2.choices[0].message.content

## TEST OUTPUT
assertlen(response_2_text)>len(response_1_text)
```

[**Check out the tutorial!**](https://docs.litellm.ai/docs/tutorials/provider_specific_params)

## Proxy Usage[​](#proxy-usage "Direct link to Proxy Usage")

**via Config**

```
model_list:
-model_name: llama-3-8b-instruct
litellm_params:
model: predibase/llama-3-8b-instruct
api_key: os.environ/PREDIBASE_API_KEY
tenant_id: os.environ/PREDIBASE_TENANT_ID
max_tokens:256
adapter_base: <my-special_base># 👈 PROVIDER-SPECIFIC PARAM
```

**via Request**

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
  "model": "llama-3-8b-instruct",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Boston today?"
    }
  ],
  "adapater_id": "my-special-adapter-id"
}'
```

ProviderParameterUse Case**AWS Bedrock**`requestMetadata`Cost attribution, logging**Gemini/Vertex AI**`labels`Resource labeling**Anthropic**`metadata`User identification

- AWS Bedrock
- Gemini/Vertex AI
- Anthropic

```
import litellm

response = litellm.completion(
    model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
    messages=[{"role":"user","content":"Hello!"}],
    requestMetadata={"cost_center":"engineering"}
)
```