---
title: Vertex AI - Anthropic, DeepSeek, Model Garden | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_partner
source: sitemap
fetched_at: 2026-01-21T19:50:46.87904539-03:00
rendered_js: false
word_count: 319
summary: This document provides configuration details and code examples for accessing partner models like Claude, Llama, and Mistral via Google Vertex AI using LiteLLM. It outlines the specific routing prefixes and environment variables required for successful integration.
tags:
    - vertex-ai
    - litellm
    - model-routing
    - anthropic-claude
    - mistral-ai
    - meta-llama
    - python-sdk
category: reference
---

## Supported Partner Providers[​](#supported-partner-providers "Direct link to Supported Partner Providers")

ProviderLiteLLM RouteVertex DocumentationAnthropic (Claude)`vertex_ai/claude-*`[Vertex AI - Anthropic Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude)DeepSeek`vertex_ai/deepseek-ai/{MODEL}`[Vertex AI - DeepSeek Models](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/deepseek)Meta/Llama`vertex_ai/meta/{MODEL}`[Vertex AI - Meta Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/llama)Mistral`vertex_ai/mistral-*`[Vertex AI - Mistral Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/mistral)AI21 (Jamba)`vertex_ai/jamba-*`[Vertex AI - AI21 Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/ai21)Qwen`vertex_ai/qwen/*`[Vertex AI - Qwen Models](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/qwen)OpenAI (GPT-OSS)`vertex_ai/openai/gpt-oss-*`[Vertex AI - GPT-OSS Models](https://console.cloud.google.com/vertex-ai/publishers/openai/model-garden/)

## Vertex AI - Anthropic (Claude)[​](#vertex-ai---anthropic-claude "Direct link to Vertex AI - Anthropic (Claude)")

Model NameFunction Callclaude-3-opus@20240229`completion('vertex_ai/claude-3-opus@20240229', messages)`claude-3-5-sonnet@20240620`completion('vertex_ai/claude-3-5-sonnet@20240620', messages)`claude-3-sonnet@20240229`completion('vertex_ai/claude-3-sonnet@20240229', messages)`claude-3-haiku@20240307`completion('vertex_ai/claude-3-haiku@20240307', messages)`claude-3-7-sonnet@20250219`completion('vertex_ai/claude-3-7-sonnet@20250219', messages)`

#### Usage[​](#usage "Direct link to Usage")

- SDK
- Proxy

```
from litellm import completion
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

model ="claude-3-sonnet@20240229"

vertex_ai_project ="your-vertex-project"# can also set this as os.environ["VERTEXAI_PROJECT"]
vertex_ai_location ="your-vertex-location"# can also set this as os.environ["VERTEXAI_LOCATION"]

response = completion(
    model="vertex_ai/"+ model,
    messages=[{"role":"user","content":"hi"}],
    temperature=0.7,
    vertex_ai_project=vertex_ai_project,
    vertex_ai_location=vertex_ai_location,
)
print("\nModel Response", response)
```

#### Usage - `thinking` / `reasoning_content`[​](#usage---thinking--reasoning_content "Direct link to usage---thinking--reasoning_content")

- SDK
- PROXY

```
from litellm import completion

resp = completion(
    model="vertex_ai/claude-3-7-sonnet-20250219",
    messages=[{"role":"user","content":"What is the capital of France?"}],
    thinking={"type":"enabled","budget_tokens":1024},
)

```

**Expected Response**

```
ModelResponse(
id='chatcmpl-c542d76d-f675-4e87-8e5f-05855f5d0f5e',
    created=1740470510,
    model='claude-3-7-sonnet-20250219',
object='chat.completion',
    system_fingerprint=None,
    choices=[
        Choices(
            finish_reason='stop',
            index=0,
            message=Message(
                content="The capital of France is Paris.",
                role='assistant',
                tool_calls=None,
                function_call=None,
                provider_specific_fields={
'citations':None,
'thinking_blocks':[
{
'type':'thinking',
'thinking':'The capital of France is Paris. This is a very straightforward factual question.',
'signature':'EuYBCkQYAiJAy6...'
}
]
}
),
            thinking_blocks=[
{
'type':'thinking',
'thinking':'The capital of France is Paris. This is a very straightforward factual question.',
'signature':'EuYBCkQYAiJAy6AGB...'
}
],
            reasoning_content='The capital of France is Paris. This is a very straightforward factual question.'
)
],
    usage=Usage(
        completion_tokens=68,
        prompt_tokens=42,
        total_tokens=110,
        completion_tokens_details=None,
        prompt_tokens_details=PromptTokensDetailsWrapper(
            audio_tokens=None,
            cached_tokens=0,
            text_tokens=None,
            image_tokens=None
),
        cache_creation_input_tokens=0,
        cache_read_input_tokens=0
)
)
```

## VertexAI DeepSeek[​](#vertexai-deepseek "Direct link to VertexAI DeepSeek")

PropertyDetailsProvider Route`vertex_ai/deepseek-ai/{MODEL}`Vertex Documentation[Vertex AI - DeepSeek Models](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/deepseek)

#### Usage[​](#usage-1 "Direct link to Usage")

**LiteLLM Supports all Vertex AI DeepSeek Models.** Ensure you use the `vertex_ai/deepseek-ai/` prefix for all Vertex AI DeepSeek models.

Model NameUsagevertex\_ai/deepseek-ai/deepseek-r1-0528-maas`completion('vertex_ai/deepseek-ai/deepseek-r1-0528-maas', messages)`

Model NameFunction Callmeta/llama-3.2-90b-vision-instruct-maas`completion('vertex_ai/meta/llama-3.2-90b-vision-instruct-maas', messages)`meta/llama3-8b-instruct-maas`completion('vertex_ai/meta/llama3-8b-instruct-maas', messages)`meta/llama3-70b-instruct-maas`completion('vertex_ai/meta/llama3-70b-instruct-maas', messages)`meta/llama3-405b-instruct-maas`completion('vertex_ai/meta/llama3-405b-instruct-maas', messages)`meta/llama-4-scout-17b-16e-instruct-maas`completion('vertex_ai/meta/llama-4-scout-17b-16e-instruct-maas', messages)`meta/llama-4-scout-17-128e-instruct-maas`completion('vertex_ai/meta/llama-4-scout-128b-16e-instruct-maas', messages)`meta/llama-4-maverick-17b-128e-instruct-maas`completion('vertex_ai/meta/llama-4-maverick-17b-128e-instruct-maas',messages)`meta/llama-4-maverick-17b-16e-instruct-maas`completion('vertex_ai/meta/llama-4-maverick-17b-16e-instruct-maas',messages)`

#### Usage[​](#usage-2 "Direct link to Usage")

- SDK
- Proxy

```
from litellm import completion
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

model ="meta/llama3-405b-instruct-maas"

vertex_ai_project ="your-vertex-project"# can also set this as os.environ["VERTEXAI_PROJECT"]
vertex_ai_location ="your-vertex-location"# can also set this as os.environ["VERTEXAI_LOCATION"]

response = completion(
    model="vertex_ai/"+ model,
    messages=[{"role":"user","content":"hi"}],
    vertex_ai_project=vertex_ai_project,
    vertex_ai_location=vertex_ai_location,
)
print("\nModel Response", response)
```

## VertexAI Mistral API[​](#vertexai-mistral-api "Direct link to VertexAI Mistral API")

[**Supported OpenAI Params**](https://github.com/BerriAI/litellm/blob/e0f3cd580cb85066f7d36241a03c30aa50a8a31d/litellm/llms/openai.py#L137)

**LiteLLM Supports all Vertex AI Mistral Models.** Ensure you use the `vertex_ai/mistral-` prefix for all Vertex AI Mistral models.

Overview

PropertyDetailsProvider Route`vertex_ai/mistral-{MODEL}`Vertex Documentation[Vertex AI - Mistral Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/mistral)

Model NameFunction Callmistral-large@latest`completion('vertex_ai/mistral-large@latest', messages)`mistral-large@2407`completion('vertex_ai/mistral-large@2407', messages)`mistral-small-2503`completion('vertex_ai/mistral-small-2503', messages)`mistral-large-2411`completion('vertex_ai/mistral-large-2411', messages)`mistral-nemo@latest`completion('vertex_ai/mistral-nemo@latest', messages)`codestral@latest`completion('vertex_ai/codestral@latest', messages)`codestral@@2405`completion('vertex_ai/codestral@2405', messages)`

#### Usage[​](#usage-3 "Direct link to Usage")

- SDK
- Proxy

```
from litellm import completion
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

model ="mistral-large@2407"

vertex_ai_project ="your-vertex-project"# can also set this as os.environ["VERTEXAI_PROJECT"]
vertex_ai_location ="your-vertex-location"# can also set this as os.environ["VERTEXAI_LOCATION"]

response = completion(
    model="vertex_ai/"+ model,
    messages=[{"role":"user","content":"hi"}],
    vertex_ai_project=vertex_ai_project,
    vertex_ai_location=vertex_ai_location,
)
print("\nModel Response", response)
```

#### Usage - Codestral FIM[​](#usage---codestral-fim "Direct link to Usage - Codestral FIM")

Call Codestral on VertexAI via the OpenAI [`/v1/completion`](https://platform.openai.com/docs/api-reference/completions/create) endpoint for FIM tasks.

Note: You can also call Codestral via `/chat/completion`.

- SDK
- Proxy

```
from litellm import completion
import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
# OR run `!gcloud auth print-access-token` in your terminal

model ="codestral@2405"

vertex_ai_project ="your-vertex-project"# can also set this as os.environ["VERTEXAI_PROJECT"]
vertex_ai_location ="your-vertex-location"# can also set this as os.environ["VERTEXAI_LOCATION"]

response = text_completion(
    model="vertex_ai/"+ model,
    vertex_ai_project=vertex_ai_project,
    vertex_ai_location=vertex_ai_location,
    prompt="def is_odd(n): \n return n % 2 == 1 \ndef test_is_odd():",
    suffix="return True",# optional
    temperature=0,# optional
    top_p=1,# optional
    max_tokens=10,# optional
    min_tokens=10,# optional
    seed=10,# optional
    stop=["return"],# optional
)

print("\nModel Response", response)
```

## VertexAI AI21 Models[​](#vertexai-ai21-models "Direct link to VertexAI AI21 Models")

Model NameFunction Calljamba-1.5-mini@001`completion(model='vertex_ai/jamba-1.5-mini@001', messages)`jamba-1.5-large@001`completion(model='vertex_ai/jamba-1.5-large@001', messages)`

#### Usage[​](#usage-4 "Direct link to Usage")

- SDK
- Proxy

```
from litellm import completion
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

model ="meta/jamba-1.5-mini@001"

vertex_ai_project ="your-vertex-project"# can also set this as os.environ["VERTEXAI_PROJECT"]
vertex_ai_location ="your-vertex-location"# can also set this as os.environ["VERTEXAI_LOCATION"]

response = completion(
    model="vertex_ai/"+ model,
    messages=[{"role":"user","content":"hi"}],
    vertex_ai_project=vertex_ai_project,
    vertex_ai_location=vertex_ai_location,
)
print("\nModel Response", response)
```

## VertexAI Qwen API[​](#vertexai-qwen-api "Direct link to VertexAI Qwen API")

PropertyDetailsProvider Route`vertex_ai/qwen/{MODEL}`Vertex Documentation[Vertex AI - Qwen Models](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/qwen)

**LiteLLM Supports all Vertex AI Qwen Models.** Ensure you use the `vertex_ai/qwen/` prefix for all Vertex AI Qwen models.

Model NameUsagevertex\_ai/qwen/qwen3-coder-480b-a35b-instruct-maas`completion('vertex_ai/qwen/qwen3-coder-480b-a35b-instruct-maas', messages)`vertex\_ai/qwen/qwen3-235b-a22b-instruct-2507-maas`completion('vertex_ai/qwen/qwen3-235b-a22b-instruct-2507-maas', messages)`

#### Usage[​](#usage-5 "Direct link to Usage")

- SDK
- Proxy

```
from litellm import completion
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

model ="qwen/qwen3-coder-480b-a35b-instruct-maas"

vertex_ai_project ="your-vertex-project"# can also set this as os.environ["VERTEXAI_PROJECT"]
vertex_ai_location ="your-vertex-location"# can also set this as os.environ["VERTEXAI_LOCATION"]

response = completion(
    model="vertex_ai/"+ model,
    messages=[{"role":"user","content":"hi"}],
    vertex_ai_project=vertex_ai_project,
    vertex_ai_location=vertex_ai_location,
)
print("\nModel Response", response)
```

## VertexAI GPT-OSS Models[​](#vertexai-gpt-oss-models "Direct link to VertexAI GPT-OSS Models")

PropertyDetailsProvider Route`vertex_ai/openai/{MODEL}`Vertex Documentation[Vertex AI - GPT-OSS Models](https://console.cloud.google.com/vertex-ai/publishers/openai/model-garden/)

**LiteLLM Supports all Vertex AI GPT-OSS Models.** Ensure you use the `vertex_ai/openai/` prefix for all Vertex AI GPT-OSS models.

Model NameUsagevertex\_ai/openai/gpt-oss-20b-maas`completion('vertex_ai/openai/gpt-oss-20b-maas', messages)`

#### Usage[​](#usage-6 "Direct link to Usage")

- SDK
- Proxy

```
from litellm import completion
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

model ="openai/gpt-oss-20b-maas"

vertex_ai_project ="your-vertex-project"# can also set this as os.environ["VERTEXAI_PROJECT"]
vertex_ai_location ="your-vertex-location"# can also set this as os.environ["VERTEXAI_LOCATION"]

response = completion(
    model="vertex_ai/"+ model,
    messages=[{"role":"user","content":"hi"}],
    vertex_ai_project=vertex_ai_project,
    vertex_ai_location=vertex_ai_location,
)
print("\nModel Response", response)
```

#### Usage - `reasoning_effort`[​](#usage---reasoning_effort "Direct link to usage---reasoning_effort")

GPT-OSS models support the `reasoning_effort` parameter for enhanced reasoning capabilities.

- SDK
- PROXY

```
from litellm import completion

response = completion(
    model="vertex_ai/openai/gpt-oss-20b-maas",
    messages=[{"role":"user","content":"Solve this complex problem step by step"}],
    reasoning_effort="low",# Options: "minimal", "low", "medium", "high"
    vertex_ai_project="your-vertex-project",
    vertex_ai_location="us-central1",
)
```