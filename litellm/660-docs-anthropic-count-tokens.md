---
title: /v1/messages/count_tokens | liteLLM
url: https://docs.litellm.ai/docs/anthropic_count_tokens
source: sitemap
fetched_at: 2026-01-21T19:44:01.211969585-03:00
rendered_js: false
word_count: 189
summary: This document explains how to use LiteLLM's Anthropic-compatible endpoint to count tokens across multiple providers including Anthropic, Vertex AI, and Bedrock.
tags:
    - litellm
    - token-counting
    - anthropic-api
    - claude
    - vertex-ai
    - aws-bedrock
    - llm-proxy
category: api
---

## Overview[​](#overview "Direct link to Overview")

Anthropic-compatible token counting endpoint. Count tokens for messages before sending them to the model.

FeatureSupportedNotesCost Tracking❌Token counting only, no cost incurredLogging✅Works across all integrationsEnd-user Tracking✅Supported ProvidersAnthropic, Vertex AI (Claude), Bedrock (Claude), Gemini, Vertex AIAuto-routes to provider-specific token counting APIs

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Start LiteLLM Proxy[​](#1-start-litellm-proxy "Direct link to 1. Start LiteLLM Proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 2. Count Tokens[​](#2-count-tokens "Direct link to 2. Count Tokens")

- curl
- Python (httpx)

```
curl -X POST "http://localhost:4000/v1/messages/count_tokens" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "claude-3-5-sonnet-20241022",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ]
  }'
```

**Expected Response:**

## LiteLLM Proxy Configuration[​](#litellm-proxy-configuration "Direct link to LiteLLM Proxy Configuration")

Add models to your `config.yaml`:

```
model_list:
-model_name: claude-3-5-sonnet
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY

-model_name: claude-vertex
litellm_params:
model: vertex_ai/claude-3-5-sonnet-v2@20241022
vertex_project: my-project
vertex_location: us-east5
vertex_count_tokens_location: us-east5 # Optional: Override location for token counting (count_tokens not available on global location)

-model_name: claude-bedrock
litellm_params:
model: bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0
aws_region_name: us-west-2
```

## Request Parameters[​](#request-parameters "Direct link to Request Parameters")

ParameterTypeRequiredDescription`model`string✅The model to use for token counting`messages`array✅Array of messages in Anthropic format

### Messages Format[​](#messages-format "Direct link to Messages Format")

```
{
"messages":[
{"role":"user","content":"Hello!"},
{"role":"assistant","content":"Hi there!"},
{"role":"user","content":"How are you?"}
]
}
```

## Response Format[​](#response-format "Direct link to Response Format")

```
{
"input_tokens": <number>
}
```

FieldTypeDescription`input_tokens`integerNumber of tokens in the input messages

## Supported Providers[​](#supported-providers "Direct link to Supported Providers")

The `/v1/messages/count_tokens` endpoint automatically routes to the appropriate provider-specific token counting API:

ProviderToken Counting MethodAnthropic[Anthropic Token Counting API](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)Vertex AI (Claude)Vertex AI Partner Models Token CounterBedrock (Claude)AWS Bedrock CountTokens APIGeminiGoogle AI Studio countTokens APIVertex AI (Gemini)Vertex AI countTokens API

## Examples[​](#examples "Direct link to Examples")

### Count Tokens with System Message[​](#count-tokens-with-system-message "Direct link to Count Tokens with System Message")

```
curl -X POST "http://localhost:4000/v1/messages/count_tokens" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "claude-3-5-sonnet-20241022",
    "messages": [
      {"role": "user", "content": "You are a helpful assistant. Please help me write a haiku about programming."}
    ]
  }'
```

### Count Tokens for Multi-turn Conversation[​](#count-tokens-for-multi-turn-conversation "Direct link to Count Tokens for Multi-turn Conversation")

```
curl -X POST "http://localhost:4000/v1/messages/count_tokens" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "claude-3-5-sonnet-20241022",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"},
      {"role": "assistant", "content": "The capital of France is Paris."},
      {"role": "user", "content": "What is its population?"}
    ]
  }'
```

### Using with Vertex AI Claude[​](#using-with-vertex-ai-claude "Direct link to Using with Vertex AI Claude")

```
curl -X POST "http://localhost:4000/v1/messages/count_tokens" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "claude-vertex",
    "messages": [
      {"role": "user", "content": "Hello, world!"}
    ]
  }'
```

### Using with Bedrock Claude[​](#using-with-bedrock-claude "Direct link to Using with Bedrock Claude")

```
curl -X POST "http://localhost:4000/v1/messages/count_tokens" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "claude-bedrock",
    "messages": [
      {"role": "user", "content": "Hello, world!"}
    ]
  }'
```

## Comparison with Anthropic Passthrough[​](#comparison-with-anthropic-passthrough "Direct link to Comparison with Anthropic Passthrough")

LiteLLM provides two ways to count tokens:

EndpointDescriptionUse Case`/v1/messages/count_tokens`LiteLLM's Anthropic-compatible endpointWorks with all supported providers (Anthropic, Vertex AI, Bedrock, etc.)`/anthropic/v1/messages/count_tokens`[Pass-through to Anthropic API](https://docs.litellm.ai/docs/pass_through/anthropic_completion#example-2-token-counting-api)Direct Anthropic API access with native headers

### Pass-through Example[​](#pass-through-example "Direct link to Pass-through Example")

For direct Anthropic API access with full native headers:

```
curl --request POST \
    --url http://0.0.0.0:4000/anthropic/v1/messages/count_tokens \
    --header "x-api-key: $LITELLM_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: token-counting-2024-11-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-3-5-sonnet-20241022",
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }'
```