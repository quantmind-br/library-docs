---
title: ChatGPT Subscription | liteLLM
url: https://docs.litellm.ai/docs/providers/chatgpt
source: sitemap
fetched_at: 2026-01-21T19:48:39.01181084-03:00
rendered_js: false
word_count: 201
summary: This document explains how to integrate ChatGPT Pro/Max subscription models with LiteLLM using OAuth device flow authentication and describes supported API endpoints and configuration settings.
tags:
    - litellm
    - chatgpt-api
    - oauth-device-flow
    - python-sdk
    - llm-proxy
    - authentication
category: guide
---

Use ChatGPT Pro/Max subscription models through LiteLLM with OAuth device flow authentication.

PropertyDetailsDescriptionChatGPT subscription access (Codex + GPT-5.2 family) via ChatGPT backend APIProvider Route on LiteLLM`chatgpt/`Supported Endpoints`/responses`, `/chat/completions` (bridged to Responses for supported models)API Reference[https://chatgpt.com](https://chatgpt.com)

ChatGPT subscription access is native to the Responses API. Chat Completions requests are bridged to Responses for supported models (for example `chatgpt/gpt-5.2`).

Notes:

- The ChatGPT subscription backend rejects token limit fields (`max_tokens`, `max_output_tokens`, `max_completion_tokens`) and `metadata`. LiteLLM strips these fields for this provider.
- `/v1/chat/completions` honors `stream`. When `stream` is false (default), LiteLLM aggregates the Responses stream into a single JSON response.

## Authentication[​](#authentication "Direct link to Authentication")

ChatGPT subscription access uses an OAuth device code flow:

1. LiteLLM prints a device code and verification URL
2. Open the URL, sign in, and enter the code
3. Tokens are stored locally for reuse

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Responses (recommended for Codex models)[​](#responses-recommended-for-codex-models "Direct link to Responses (recommended for Codex models)")

ChatGPT Responses

```
import litellm

response = litellm.responses(
    model="chatgpt/gpt-5.2-codex",
input="Write a Python hello world"
)

print(response)
```

### Chat Completions (bridged to Responses)[​](#chat-completions-bridged-to-responses "Direct link to Chat Completions (bridged to Responses)")

ChatGPT Chat Completions

```
import litellm

response = litellm.completion(
    model="chatgpt/gpt-5.2",
    messages=[{"role":"user","content":"Write a Python hello world"}]
)

print(response)
```

## Usage - LiteLLM Proxy[​](#usage---litellm-proxy "Direct link to Usage - LiteLLM Proxy")

config.yaml

```
model_list:
-model_name: chatgpt/gpt-5.2
model_info:
mode: responses
litellm_params:
model: chatgpt/gpt-5.2
-model_name: chatgpt/gpt-5.2-codex
model_info:
mode: responses
litellm_params:
model: chatgpt/gpt-5.2-codex
```

Start LiteLLM Proxy

```
litellm --config config.yaml
```

## Configuration[​](#configuration "Direct link to Configuration")

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

- `CHATGPT_TOKEN_DIR`: Custom token storage directory
- `CHATGPT_AUTH_FILE`: Auth file name (default: `auth.json`)
- `CHATGPT_API_BASE`: Override API base (default: `https://chatgpt.com/backend-api/codex`)
- `OPENAI_CHATGPT_API_BASE`: Alias for `CHATGPT_API_BASE`
- `CHATGPT_ORIGINATOR`: Override the `originator` header value
- `CHATGPT_USER_AGENT`: Override the `User-Agent` header value
- `CHATGPT_USER_AGENT_SUFFIX`: Optional suffix appended to the `User-Agent` header