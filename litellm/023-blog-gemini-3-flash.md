---
title: 'DAY 0 Support: Gemini 3 Flash on LiteLLM'
url: https://docs.litellm.ai/blog/gemini_3_flash
source: sitemap
fetched_at: 2026-01-21T19:40:50.899730081-03:00
rendered_js: false
word_count: 318
summary: This document details the integration of Google Gemini 3 Flash Preview into LiteLLM, explaining how to implement thinking levels, thought signatures, and OpenAI-compatible reasoning parameters.
tags:
    - litellm
    - gemini-3-flash
    - google-gemini
    - reasoning-effort
    - thinking-level
    - llm-proxy
    - model-integration
category: guide
---

LiteLLM now supports `gemini-3-flash-preview` and all the new API changes along with it.

note

If you only want cost tracking, you need no change in your current Litellm version. But if you want the support for new features introduced along with it like thinking levels, you will need to use v1.80.8-stable.1 or above.

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
ghcr.io/berriai/litellm:main-v1.80.8-stable.1
```

## What's New[​](#whats-new "Direct link to What's New")

### 1. New Thinking Levels: `thinkingLevel` with MINIMAL & MEDIUM[​](#1-new-thinking-levels-thinkinglevel-with-minimal--medium "Direct link to 1-new-thinking-levels-thinkinglevel-with-minimal--medium")

Gemini 3 Flash introduces granular thinking control with `thinkingLevel` instead of `thinkingBudget`.

- **MINIMAL**: Ultra-lightweight thinking for fast responses
- **MEDIUM**: Balanced thinking for complex reasoning
- **HIGH**: Maximum reasoning depth

LiteLLM automatically maps the OpenAI `reasoning_effort` parameter to Gemini's `thinkingLevel`, so you can use familiar `reasoning_effort` values (`minimal`, `low`, `medium`, `high`) without changing your code!

### 2. Thought Signatures[​](#2-thought-signatures "Direct link to 2. Thought Signatures")

Like `gemini-3-pro`, this model also includes thought signatures for tool calls. LiteLLM handles signature extraction and embedding internally. [Learn more about thought signatures](https://docs.litellm.ai/blog/gemini_3#thought-signatures).

**Edge Case Handling**: If thought signatures are missing in the request, LiteLLM adds a dummy signature ensuring the API call doesn't break

* * *

## Supported Endpoints[​](#supported-endpoints "Direct link to Supported Endpoints")

LiteLLM provides **full end-to-end support** for Gemini 3 Flash on:

- ✅ `/v1/chat/completions` - OpenAI-compatible chat completions endpoint
- ✅ `/v1/responses` - OpenAI Responses API endpoint (streaming and non-streaming)
- ✅ [`/v1/messages`](https://docs.litellm.ai/docs/anthropic_unified) - Anthropic-compatible messages endpoint
- ✅ `/v1/generateContent` – [Google Gemini API](https://docs.litellm.ai/docs/generateContent.md) compatible endpoint All endpoints support:
- Streaming and non-streaming responses
- Function calling with thought signatures
- Multi-turn conversations
- All Gemini 3-specific features
- Converstion of provider specific thinking related param to thinkingLevel

## Quick Start[​](#quick-start "Direct link to Quick Start")

- SDK
- PROXY
- LOW
- MEDIUM (NEW)
- HIGH

**Basic Usage with MEDIUM thinking (NEW)**

```
from litellm import completion

# No need to make any changes to your code as we map openai reasoning param to thinkingLevel
response = completion(
    model="gemini/gemini-3-flash-preview",
    messages=[{"role":"user","content":"Solve this complex math problem: 25 * 4 + 10"}],
    reasoning_effort="medium",# NEW: MEDIUM thinking level
)

print(response.choices[0].message.content)
```

* * *

## Key Features[​](#key-features "Direct link to Key Features")

✅ **Thinking Levels**: MINIMAL, LOW, MEDIUM, HIGH  
✅ **Thought Signatures**: Track reasoning with unique identifiers  
✅ **Seamless Integration**: Works with existing OpenAI-compatible client  
✅ **Backward Compatible**: Gemini 2.5 models continue using `thinkingBudget`

* * *

## Installation[​](#installation "Direct link to Installation")

```
pip install litellm --upgrade
```

```
import litellm
from litellm import completion

response = completion(
    model="gemini/gemini-3-flash-preview",
    messages=[{"role":"user","content":"Your question here"}],
    reasoning_effort="medium",# Use MEDIUM thinking
)
print(response)
```

note

If using this model via vertex\_ai, keep the location as global as this is the only supported location as of now.

## `reasoning_effort` Mapping for Gemini 3+[​](#reasoning_effort-mapping-for-gemini-3 "Direct link to reasoning_effort-mapping-for-gemini-3")

reasoning\_effortthinking\_level`minimal``minimal``low``low``medium``medium``high``high``disable``minimal``none``minimal`