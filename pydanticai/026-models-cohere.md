---
title: Cohere - Pydantic AI
url: https://ai.pydantic.dev/models/cohere/
source: sitemap
fetched_at: 2026-01-22T22:26:09.515123312-03:00
rendered_js: false
word_count: 108
summary: This document explains how to install and configure Cohere models for use with PydanticAI, covering authentication, environment variables, and custom provider setup.
tags:
    - cohere
    - pydantic-ai
    - installation
    - configuration
    - llm
    - api-authentication
category: guide
---

## Install

To use `CohereModel`, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `cohere` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[cohere]"
```

```
uvadd"pydantic-ai-slim[cohere]"
```

## Configuration

To use [Cohere](https://cohere.com/) through their API, go to [dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys) and follow your nose until you find the place to generate an API key.

`CohereModelName` contains a list of the most popular Cohere models.

## Environment variable

Once you have the API key, you can set it as an environment variable:

```
exportCO_API_KEY='your-api-key'
```

You can then use `CohereModel` by name:

```
frompydantic_aiimport Agent

agent = Agent('cohere:command-r7b-12-2024')
...
```

Or initialise the model directly with just the model name:

```
frompydantic_aiimport Agent
frompydantic_ai.models.cohereimport CohereModel

model = CohereModel('command-r7b-12-2024')
agent = Agent(model)
...
```

## `provider` argument

You can provide a custom `Provider` via the `provider` argument:

```
frompydantic_aiimport Agent
frompydantic_ai.models.cohereimport CohereModel
frompydantic_ai.providers.cohereimport CohereProvider

model = CohereModel('command-r7b-12-2024', provider=CohereProvider(api_key='your-api-key'))
agent = Agent(model)
...
```

You can also customize the `CohereProvider` with a custom `http_client`:

```
fromhttpximport AsyncClient

frompydantic_aiimport Agent
frompydantic_ai.models.cohereimport CohereModel
frompydantic_ai.providers.cohereimport CohereProvider

custom_http_client = AsyncClient(timeout=30)
model = CohereModel(
    'command-r7b-12-2024',
    provider=CohereProvider(api_key='your-api-key', http_client=custom_http_client),
)
agent = Agent(model)
...
```