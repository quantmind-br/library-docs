---
title: RAGFlow | liteLLM
url: https://docs.litellm.ai/docs/providers/ragflow
source: sitemap
fetched_at: 2026-01-21T19:50:11.500950089-03:00
rendered_js: false
word_count: 281
summary: This document explains how to integrate RAGFlow with LiteLLM, detailing the specific model naming conventions, authentication methods, and configuration for both chat and agent endpoints.
tags:
    - litellm
    - ragflow
    - api-integration
    - chat-completions
    - llm-proxy
    - streaming-responses
category: guide
---

Litellm supports Ragflow's chat completions APIs

## Supported Features[​](#supported-features "Direct link to Supported Features")

- ✅ Chat completions
- ✅ Streaming responses
- ✅ Both chat and agent endpoints
- ✅ Multiple credential sources (params, env vars, litellm\_params)
- ✅ OpenAI-compatible API format

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['RAGFLOW_API_KEY']
```

## API Base[​](#api-base "Direct link to API Base")

```
# env variable
os.environ['RAGFLOW_API_BASE']
```

## Overview[​](#overview "Direct link to Overview")

RAGFlow provides OpenAI-compatible APIs with unique path structures that include chat and agent IDs:

- **Chat endpoint**: `/api/v1/chats_openai/{chat_id}/chat/completions`
- **Agent endpoint**: `/api/v1/agents_openai/{agent_id}/chat/completions`

The model name format embeds the endpoint type and ID:

- Chat: `ragflow/chat/{chat_id}/{model_name}`
- Agent: `ragflow/agent/{agent_id}/{model_name}`

## Sample Usage - Chat Endpoint[​](#sample-usage---chat-endpoint "Direct link to Sample Usage - Chat Endpoint")

```
from litellm import completion
import os

os.environ['RAGFLOW_API_KEY']="your-ragflow-api-key"
os.environ['RAGFLOW_API_BASE']="http://localhost:9380"# or your hosted URL

response = completion(
    model="ragflow/chat/my-chat-id/gpt-4o-mini",
    messages=[{"role":"user","content":"How does the deep doc understanding work?"}]
)
print(response)
```

## Sample Usage - Agent Endpoint[​](#sample-usage---agent-endpoint "Direct link to Sample Usage - Agent Endpoint")

```
from litellm import completion
import os

os.environ['RAGFLOW_API_KEY']="your-ragflow-api-key"
os.environ['RAGFLOW_API_BASE']="http://localhost:9380"# or your hosted URL

response = completion(
    model="ragflow/agent/my-agent-id/gpt-4o-mini",
    messages=[{"role":"user","content":"What are the key features?"}]
)
print(response)
```

## Sample Usage - With Parameters[​](#sample-usage---with-parameters "Direct link to Sample Usage - With Parameters")

You can also pass `api_key` and `api_base` directly as parameters:

```
from litellm import completion

response = completion(
    model="ragflow/chat/my-chat-id/gpt-4o-mini",
    messages=[{"role":"user","content":"Hello!"}],
    api_key="your-ragflow-api-key",
    api_base="http://localhost:9380"
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['RAGFLOW_API_KEY']="your-ragflow-api-key"
os.environ['RAGFLOW_API_BASE']="http://localhost:9380"

response = completion(
    model="ragflow/agent/my-agent-id/gpt-4o-mini",
    messages=[{"role":"user","content":"Explain RAGFlow"}],
    stream=True
)

for chunk in response:
print(chunk)
```

## Model Name Format[​](#model-name-format "Direct link to Model Name Format")

The model name must follow one of these formats:

### Chat Endpoint[​](#chat-endpoint "Direct link to Chat Endpoint")

```
ragflow/chat/{chat_id}/{model_name}
```

Example: `ragflow/chat/my-chat-id/gpt-4o-mini`

### Agent Endpoint[​](#agent-endpoint "Direct link to Agent Endpoint")

```
ragflow/agent/{agent_id}/{model_name}
```

Example: `ragflow/agent/my-agent-id/gpt-4o-mini`

Where:

- `{chat_id}` or `{agent_id}` is the ID of your chat or agent in RAGFlow
- `{model_name}` is the actual model name (e.g., `gpt-4o-mini`, `gpt-4o`, etc.)

## Configuration Sources[​](#configuration-sources "Direct link to Configuration Sources")

LiteLLM supports multiple ways to provide credentials, checked in this order:

1. **Function parameters**: `api_key="..."`, `api_base="..."`
2. **litellm\_params**: `litellm_params={"api_key": "...", "api_base": "..."}`
3. **Environment variables**: `RAGFLOW_API_KEY`, `RAGFLOW_API_BASE`
4. **Global litellm settings**: `litellm.api_key`, `litellm.api_base`

## Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

```
export RAGFLOW_API_KEY="your-ragflow-api-key"
export RAGFLOW_API_BASE="http://localhost:9380"
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

- config.yaml
- CLI

```
model_list:
-model_name: ragflow-chat-gpt4
litellm_params:
model: ragflow/chat/my-chat-id/gpt-4o-mini
api_key: os.environ/RAGFLOW_API_KEY
api_base: os.environ/RAGFLOW_API_BASE
-model_name: ragflow-agent-gpt4
litellm_params:
model: ragflow/agent/my-agent-id/gpt-4o-mini
api_key: os.environ/RAGFLOW_API_KEY
api_base: os.environ/RAGFLOW_API_BASE
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- Python SDK

```
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "ragflow-chat-gpt4",
    "messages": [
      {"role": "user", "content": "How does RAGFlow work?"}
    ]
  }'
```

## API Base URL Handling[​](#api-base-url-handling "Direct link to API Base URL Handling")

The `api_base` parameter can be provided with or without `/v1` suffix. LiteLLM will automatically handle it:

- `http://localhost:9380` → `http://localhost:9380/api/v1/chats_openai/{chat_id}/chat/completions`
- `http://localhost:9380/v1` → `http://localhost:9380/api/v1/chats_openai/{chat_id}/chat/completions`
- `http://localhost:9380/api/v1` → `http://localhost:9380/api/v1/chats_openai/{chat_id}/chat/completions`

All three formats will work correctly.

## Error Handling[​](#error-handling "Direct link to Error Handling")

If you encounter errors:

1. **Invalid model format**: Ensure your model name follows `ragflow/{chat|agent}/{id}/{model_name}` format
2. **Missing api\_base**: Provide `api_base` via parameter, environment variable, or litellm\_params
3. **Connection errors**: Verify your RAGFlow server is running and accessible at the provided `api_base`

info

For more information about passing provider-specific parameters, [go here](https://docs.litellm.ai/docs/completion/provider_specific_params)