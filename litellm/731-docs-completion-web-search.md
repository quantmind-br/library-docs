---
title: Web Search | liteLLM
url: https://docs.litellm.ai/docs/completion/web_search
source: sitemap
fetched_at: 2026-01-21T19:44:51.694997461-03:00
rendered_js: false
word_count: 223
summary: This guide explains how to enable and configure web search capabilities across multiple AI providers using LiteLLM's chat and response endpoints. It covers SDK implementation, proxy configuration, and methods for managing search context and model routing for real-time data retrieval.
tags:
    - litellm
    - web-search
    - ai-search
    - python-sdk
    - llm-integration
    - model-routing
    - search-context
category: guide
---

Use web search with litellm

FeatureDetailsSupported Endpoints- `/chat/completions`  
\- `/responses`Supported Providers`openai`, `xai`, `vertex_ai`, `anthropic`, `gemini`, `perplexity`LiteLLM Cost Tracking✅ SupportedLiteLLM Version`v1.71.0+`

## Which Search Engine is Used?[​](#which-search-engine-is-used "Direct link to Which Search Engine is Used?")

Each provider uses their own search backend:

ProviderSearch EngineNotes**OpenAI** (`gpt-4o-search-preview`)OpenAI's internal searchReal-time web data**xAI** (`grok-3`)xAI's search + X/TwitterReal-time social media data**Google AI/Vertex** (`gemini-2.0-flash`)**Google Search**Uses actual Google search results**Anthropic** (`claude-3-5-sonnet`)Anthropic's web searchReal-time web data**Perplexity**Perplexity's search engineAI-powered search and reasoning

info

**Anthropic Web Search Models**: Claude models that support web search: `claude-3-5-sonnet-latest`, `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-latest`, `claude-3-5-haiku-20241022`, `claude-3-7-sonnet-20250219`

## `/chat/completions` (litellm.completion)[​](#chatcompletions-litellmcompletion "Direct link to chatcompletions-litellmcompletion")

### Quick Start[​](#quick-start "Direct link to Quick Start")

- SDK
- PROXY

```
from litellm import completion

response = completion(
    model="openai/gpt-4o-search-preview",
    messages=[
{
"role":"user",
"content":"What was a positive news story from today?",
}
],
    web_search_options={
"search_context_size":"medium"# Options: "low", "medium", "high"
}
)
```

### Search context size[​](#search-context-size "Direct link to Search context size")

- SDK
- PROXY

**OpenAI (using web\_search\_options)**

```
from litellm import completion

# Customize search context size
response = completion(
    model="openai/gpt-4o-search-preview",
    messages=[
{
"role":"user",
"content":"What was a positive news story from today?",
}
],
    web_search_options={
"search_context_size":"low"# Options: "low", "medium" (default), "high"
}
)
```

**xAI (using web\_search\_options)**

```
from litellm import completion

# Customize search context size for xAI
response = completion(
    model="xai/grok-3",
    messages=[
{
"role":"user",
"content":"What was a positive news story from today?",
}
],
    web_search_options={
"search_context_size":"high"# Options: "low", "medium" (default), "high"
}
)
```

**Anthropic (using web\_search\_options)**

```
from litellm import completion

# Customize search context size for Anthropic
response = completion(
    model="anthropic/claude-3-5-sonnet-latest",
    messages=[
{
"role":"user",
"content":"What was a positive news story from today?",
}
],
    web_search_options={
"search_context_size":"medium",# Options: "low", "medium" (default), "high"
"user_location":{
"type":"approximate",
"approximate":{
"city":"San Francisco",
},
}
}
)
```

**VertexAI/Gemini (using web\_search\_options)**

```
from litellm import completion

# Customize search context size for Gemini
response = completion(
    model="gemini-2.0-flash",
    messages=[
{
"role":"user",
"content":"What was a positive news story from today?",
}
],
    web_search_options={
"search_context_size":"low"# Options: "low", "medium" (default), "high"
}
)
```

## `/responses` (litellm.responses)[​](#responses-litellmresponses "Direct link to responses-litellmresponses")

### Quick Start[​](#quick-start-1 "Direct link to Quick Start")

- SDK
- PROXY

```
from litellm import responses

response = responses(
    model="openai/gpt-4o",
input=[
{
"role":"user",
"content":"What was a positive news story from today?"
}
],
    tools=[{
"type":"web_search_preview"# enables web search with default medium context size
}]
)
```

### Search context size[​](#search-context-size-1 "Direct link to Search context size")

- SDK
- PROXY

```
from litellm import responses

# Customize search context size
response = responses(
    model="openai/gpt-4o",
input=[
{
"role":"user",
"content":"What was a positive news story from today?"
}
],
    tools=[{
"type":"web_search_preview",
"search_context_size":"low"# Options: "low", "medium" (default), "high"
}]
)
```

## Configuring Web Search in config.yaml[​](#configuring-web-search-in-configyaml "Direct link to Configuring Web Search in config.yaml")

You can set default web search options directly in your proxy config file:

- Default Web Search
- Custom Search Context

```
model_list:
# Enable web search by default for all requests to this model
-model_name: grok-3
litellm_params:
model: xai/grok-3
api_key: os.environ/XAI_API_KEY
web_search_options:{}# Enables web search with default settings
```

### Advanced[​](#advanced "Direct link to Advanced")

You can configure LiteLLM's router to optionally drop models that do not support WebSearch, for example

```
-model_name: gpt-4.1
litellm_params:
model: openai/gpt-4.1
-model_name: gpt-4.1
litellm_params:
model: azure/gpt-4.1
api_base:"x.openai.azure.com/"
api_version: 2025-03-01-preview
model_info:
supports_web_search: False <---- KEY CHANGE!
```

In this example, LiteLLM will still route LLM requests to both deployments, but for WebSearch, will solely route to OpenAI.

**Note:** When `web_search_options` is set in the config, it applies to all requests to that model. Users can still override these settings by passing `web_search_options` in their API requests.

## Checking if a model supports web search[​](#checking-if-a-model-supports-web-search "Direct link to Checking if a model supports web search")

- SDK
- PROXY

Use `litellm.supports_web_search(model="model_name")` -&gt; returns `True` if model can perform web searches

```
# Check OpenAI models
assert litellm.supports_web_search(model="openai/gpt-4o-search-preview")==True

# Check xAI models
assert litellm.supports_web_search(model="xai/grok-3")==True

# Check Anthropic models
assert litellm.supports_web_search(model="anthropic/claude-3-5-sonnet-latest")==True

# Check VertexAI models
assert litellm.supports_web_search(model="gemini-2.0-flash")==True

# Check Google AI Studio models
assert litellm.supports_web_search(model="gemini/gemini-2.0-flash")==True
```