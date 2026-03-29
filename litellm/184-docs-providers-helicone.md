---
title: Helicone | liteLLM
url: https://docs.litellm.ai/docs/providers/helicone
source: sitemap
fetched_at: 2026-01-21T19:49:21.598470994-03:00
rendered_js: false
word_count: 360
summary: This document provides instructions and code examples for integrating the Helicone AI gateway with LiteLLM to enable observability, caching, and cost tracking.
tags:
    - helicone
    - litellm
    - ai-gateway
    - observability
    - llm-monitoring
    - caching
    - request-tracking
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionHelicone is an AI gateway and observability platform that provides OpenAI-compatible endpoints with advanced monitoring, caching, and analytics capabilities.Provider Route on LiteLLM`helicone/`Link to Provider Doc[Helicone Documentation ↗](https://docs.helicone.ai)Base URL`https://ai-gateway.helicone.ai/`Supported Operations[`/chat/completions`](#sample-usage), [`/completions`](#text-completion), [`/embeddings`](#embeddings)

**We support [ALL models available](https://helicone.ai/models) through Helicone's AI Gateway. Use `helicone/` as a prefix when sending requests.**

## What is Helicone?[​](#what-is-helicone "Direct link to What is Helicone?")

Helicone is an open-source observability platform for LLM applications that provides:

- **Request Monitoring**: Track all LLM requests with detailed metrics
- **Caching**: Reduce costs and latency with intelligent caching
- **Rate Limiting**: Control request rates per user/key
- **Cost Tracking**: Monitor spend across models and users
- **Custom Properties**: Tag requests with metadata for filtering and analysis
- **Prompt Management**: Version control for prompts

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["HELICONE_API_KEY"]=""# your Helicone API key
```

Get your Helicone API key from your [Helicone dashboard](https://helicone.ai).

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Helicone Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["HELICONE_API_KEY"]=""# your Helicone API key

messages =[{"content":"What is the capital of France?","role":"user"}]

# Helicone call - routes through Helicone gateway to OpenAI
response = completion(
    model="helicone/gpt-4",
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Helicone Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["HELICONE_API_KEY"]=""# your Helicone API key

messages =[{"content":"Write a short poem about AI","role":"user"}]

# Helicone call with streaming
response = completion(
    model="helicone/gpt-4",
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

### With Metadata (Helicone Custom Properties)[​](#with-metadata-helicone-custom-properties "Direct link to With Metadata (Helicone Custom Properties)")

Helicone with Custom Properties

```
import os
import litellm
from litellm import completion

os.environ["HELICONE_API_KEY"]=""# your Helicone API key

response = completion(
    model="helicone/gpt-4o-mini",
    messages=[{"role":"user","content":"What's the weather like?"}],
    metadata={
"Helicone-Property-Environment":"production",
"Helicone-Property-User-Id":"user_123",
"Helicone-Property-Session-Id":"session_abc"
}
)

print(response)
```

### Text Completion[​](#text-completion "Direct link to Text Completion")

Helicone Text Completion

```
import os
import litellm

os.environ["HELICONE_API_KEY"]=""# your Helicone API key

response = litellm.completion(
    model="helicone/gpt-4o-mini",# text completion model
    prompt="Once upon a time"
)

print(response)
```

## Retry and Fallback Mechanisms[​](#retry-and-fallback-mechanisms "Direct link to Retry and Fallback Mechanisms")

```
import litellm

litellm.api_base ="https://ai-gateway.helicone.ai/"
litellm.metadata ={
"Helicone-Retry-Enabled":"true",
"helicone-retry-num":"3",
"helicone-retry-factor":"2",
}

response = litellm.completion(
    model="helicone/gpt-4o-mini/openai,claude-3-5-sonnet-20241022/anthropic",# Try OpenAI first, then fallback to Anthropic, then continue with other models,
    messages=[{"role":"user","content":"Hello"}]
)
```

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

Helicone supports all standard OpenAI-compatible parameters:

ParameterTypeDescription`messages`array**Required**. Array of message objects with 'role' and 'content'`model`string**Required**. Model ID (e.g., gpt-4, claude-3-opus, etc.)`stream`booleanOptional. Enable streaming responses`temperature`floatOptional. Sampling temperature`top_p`floatOptional. Nucleus sampling parameter`max_tokens`integerOptional. Maximum tokens to generate`frequency_penalty`floatOptional. Penalize frequent tokens`presence_penalty`floatOptional. Penalize tokens based on presence`stop`string/arrayOptional. Stop sequences`n`integerOptional. Number of completions to generate`tools`arrayOptional. List of available tools/functions`tool_choice`string/objectOptional. Control tool/function calling`response_format`objectOptional. Response format specification`user`stringOptional. User identifier

Pass these as metadata to leverage Helicone features:

HeaderDescription`Helicone-Property-*`Custom properties for filtering (e.g., `Helicone-Property-User-Id`)`Helicone-Cache-Enabled`Enable caching for this request`Helicone-User-Id`User identifier for tracking`Helicone-Session-Id`Session identifier for grouping requests`Helicone-Prompt-Id`Prompt identifier for versioning`Helicone-Rate-Limit-Policy`Rate limiting policy name

Example with headers:

Helicone with Custom Headers

```
import litellm

response = litellm.completion(
    model="helicone/gpt-4",
    messages=[{"role":"user","content":"Hello"}],
    metadata={
"Helicone-Cache-Enabled":"true",
"Helicone-Property-Environment":"production",
"Helicone-Property-User-Id":"user_123",
"Helicone-Session-Id":"session_abc",
"Helicone-Prompt-Id":"prompt_v1"
}
)
```

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Using with Different Providers[​](#using-with-different-providers "Direct link to Using with Different Providers")

Helicone acts as a gateway and supports multiple providers:

Helicone with Anthropic

```
import litellm

# Set both Helicone and Anthropic keys
os.environ["HELICONE_API_KEY"]="your-helicone-key"

response = litellm.completion(
    model="helicone/claude-3.5-haiku/anthropic",
    messages=[{"role":"user","content":"Hello"}]
)
```

### Caching[​](#caching "Direct link to Caching")

Enable caching to reduce costs and latency:

Helicone Caching

```
import litellm

response = litellm.completion(
    model="helicone/gpt-4",
    messages=[{"role":"user","content":"What is 2+2?"}],
    metadata={
"Helicone-Cache-Enabled":"true"
}
)

# Subsequent identical requests will be served from cache
response2 = litellm.completion(
    model="helicone/gpt-4",
    messages=[{"role":"user","content":"What is 2+2?"}],
    metadata={
"Helicone-Cache-Enabled":"true"
}
)
```

## Features[​](#features "Direct link to Features")

### Request Monitoring[​](#request-monitoring "Direct link to Request Monitoring")

- Track all requests with detailed metrics
- View request/response pairs
- Monitor latency and errors
- Filter by custom properties

### Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

- Per-model cost tracking
- Per-user cost tracking
- Cost alerts and budgets
- Historical cost analysis

### Rate Limiting[​](#rate-limiting "Direct link to Rate Limiting")

- Per-user rate limits
- Per-API key rate limits
- Custom rate limit policies
- Automatic enforcement

### Analytics[​](#analytics "Direct link to Analytics")

- Request volume trends
- Cost trends
- Latency percentiles
- Error rates

Visit [Helicone Pricing](https://helicone.ai/pricing) for details.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Helicone Official Documentation](https://docs.helicone.ai)
- [Helicone Dashboard](https://helicone.ai)
- [Helicone GitHub](https://github.com/Helicone/helicone)
- [API Reference](https://docs.helicone.ai/rest/ai-gateway/post-v1-chat-completions)