---
title: Mistral - Pydantic AI
url: https://ai.pydantic.dev/models/mistral/
source: sitemap
fetched_at: 2026-01-22T22:26:14.415362933-03:00
rendered_js: false
word_count: 108
summary: This document explains how to install and configure Mistral models for use with Pydantic AI, covering installation, API key setup, and model initialization.
tags:
    - pydantic-ai
    - mistral-ai
    - python-setup
    - api-configuration
    - llm-integration
category: configuration
---

## Install

To use `MistralModel`, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `mistral` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[mistral]"
```

```
uvadd"pydantic-ai-slim[mistral]"
```

## Configuration

To use [Mistral](https://mistral.ai) through their API, go to [console.mistral.ai/api-keys/](https://console.mistral.ai/api-keys/) and follow your nose until you find the place to generate an API key.

`LatestMistralModelNames` contains a list of the most popular Mistral models.

## Environment variable

Once you have the API key, you can set it as an environment variable:

```
exportMISTRAL_API_KEY='your-api-key'
```

You can then use `MistralModel` by name:

```
frompydantic_aiimport Agent

agent = Agent('mistral:mistral-large-latest')
...
```

Or initialise the model directly with just the model name:

```
frompydantic_aiimport Agent
frompydantic_ai.models.mistralimport MistralModel

model = MistralModel('mistral-small-latest')
agent = Agent(model)
...
```

## `provider` argument

You can provide a custom `Provider` via the `provider` argument:

```
frompydantic_aiimport Agent
frompydantic_ai.models.mistralimport MistralModel
frompydantic_ai.providers.mistralimport MistralProvider

model = MistralModel(
    'mistral-large-latest', provider=MistralProvider(api_key='your-api-key', base_url='https://<mistral-provider-endpoint>')
)
agent = Agent(model)
...
```

You can also customize the provider with a custom `httpx.AsyncClient`:

```
fromhttpximport AsyncClient

frompydantic_aiimport Agent
frompydantic_ai.models.mistralimport MistralModel
frompydantic_ai.providers.mistralimport MistralProvider

custom_http_client = AsyncClient(timeout=30)
model = MistralModel(
    'mistral-large-latest',
    provider=MistralProvider(api_key='your-api-key', http_client=custom_http_client),
)
agent = Agent(model)
...
```