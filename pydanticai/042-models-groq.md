---
title: Groq - Pydantic AI
url: https://ai.pydantic.dev/models/groq/
source: sitemap
fetched_at: 2026-01-22T22:26:12.151089941-03:00
rendered_js: false
word_count: 116
summary: This document provides instructions for installing, configuring, and using Groq models within the Pydantic AI framework, including API key setup and custom provider initialization.
tags:
    - groq
    - pydantic-ai
    - python
    - installation
    - api-key
    - llm-integration
category: guide
---

## Install

To use `GroqModel`, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `groq` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[groq]"
```

```
uvadd"pydantic-ai-slim[groq]"
```

## Configuration

To use [Groq](https://groq.com/) through their API, go to [console.groq.com/keys](https://console.groq.com/keys) and follow your nose until you find the place to generate an API key.

`GroqModelName` contains a list of available Groq models.

## Environment variable

Once you have the API key, you can set it as an environment variable:

```
exportGROQ_API_KEY='your-api-key'
```

You can then use `GroqModel` by name:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
frompydantic_aiimport Agent

agent = Agent('gateway/groq:llama-3.3-70b-versatile')
...
```

```
frompydantic_aiimport Agent

agent = Agent('groq:llama-3.3-70b-versatile')
...
```

Or initialise the model directly with just the model name:

```
frompydantic_aiimport Agent
frompydantic_ai.models.groqimport GroqModel

model = GroqModel('llama-3.3-70b-versatile')
agent = Agent(model)
...
```

## `provider` argument

You can provide a custom `Provider` via the `provider` argument:

```
frompydantic_aiimport Agent
frompydantic_ai.models.groqimport GroqModel
frompydantic_ai.providers.groqimport GroqProvider

model = GroqModel(
    'llama-3.3-70b-versatile', provider=GroqProvider(api_key='your-api-key')
)
agent = Agent(model)
...
```

You can also customize the `GroqProvider` with a custom `httpx.AsyncClient`:

```
fromhttpximport AsyncClient

frompydantic_aiimport Agent
frompydantic_ai.models.groqimport GroqModel
frompydantic_ai.providers.groqimport GroqProvider

custom_http_client = AsyncClient(timeout=30)
model = GroqModel(
    'llama-3.3-70b-versatile',
    provider=GroqProvider(api_key='your-api-key', http_client=custom_http_client),
)
agent = Agent(model)
...
```