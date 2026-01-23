---
title: Cerebras - Pydantic AI
url: https://ai.pydantic.dev/models/cerebras/
source: sitemap
fetched_at: 2026-01-22T22:26:08.960770274-03:00
rendered_js: false
word_count: 100
summary: This document explains how to install and configure Cerebras models within the PydanticAI framework, including environment variable setup and custom provider initialization.
tags:
    - pydantic-ai
    - cerebras
    - model-configuration
    - api-integration
    - python-library
category: configuration
---

## Install

To use `CerebrasModel`, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `cerebras` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[cerebras]"
```

```
uvadd"pydantic-ai-slim[cerebras]"
```

## Configuration

To use [Cerebras](https://cerebras.ai/) through their API, go to [cloud.cerebras.ai](https://cloud.cerebras.ai/?utm_source=3pi_pydantic-ai&utm_campaign=partner_doc) and generate an API key.

For a list of available models, see the [Cerebras models documentation](https://inference-docs.cerebras.ai/models).

## Environment variable

Once you have the API key, you can set it as an environment variable:

```
exportCEREBRAS_API_KEY='your-api-key'
```

You can then use `CerebrasModel` by name:

```
frompydantic_aiimport Agent

agent = Agent('cerebras:llama-3.3-70b')
...
```

Or initialise the model directly with just the model name:

```
frompydantic_aiimport Agent
frompydantic_ai.models.cerebrasimport CerebrasModel

model = CerebrasModel('llama-3.3-70b')
agent = Agent(model)
...
```

## `provider` argument

You can provide a custom `Provider` via the `provider` argument:

```
frompydantic_aiimport Agent
frompydantic_ai.models.cerebrasimport CerebrasModel
frompydantic_ai.providers.cerebrasimport CerebrasProvider

model = CerebrasModel(
    'llama-3.3-70b', provider=CerebrasProvider(api_key='your-api-key')
)
agent = Agent(model)
...
```

You can also customize the `CerebrasProvider` with a custom `httpx.AsyncClient`:

```
fromhttpximport AsyncClient

frompydantic_aiimport Agent
frompydantic_ai.models.cerebrasimport CerebrasModel
frompydantic_ai.providers.cerebrasimport CerebrasProvider

custom_http_client = AsyncClient(timeout=30)
model = CerebrasModel(
    'llama-3.3-70b',
    provider=CerebrasProvider(api_key='your-api-key', http_client=custom_http_client),
)
agent = Agent(model)
...
```