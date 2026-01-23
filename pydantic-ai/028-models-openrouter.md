---
title: OpenRouter - Pydantic AI
url: https://ai.pydantic.dev/models/openrouter/
source: sitemap
fetched_at: 2026-01-22T22:26:15.802375281-03:00
rendered_js: false
word_count: 92
summary: This document provides instructions for installing and configuring OpenRouter models within the PydanticAI framework, covering authentication, app attribution, and custom model settings.
tags:
    - pydantic-ai
    - openrouter
    - model-configuration
    - installation
    - python-sdk
    - api-integration
category: guide
---

## Install

To use `OpenRouterModel`, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `openrouter` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[openrouter]"
```

```
uvadd"pydantic-ai-slim[openrouter]"
```

## Configuration

To use [OpenRouter](https://openrouter.ai), first create an API key at [openrouter.ai/keys](https://openrouter.ai/keys).

You can set the `OPENROUTER_API_KEY` environment variable and use [`OpenRouterProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.openrouter.OpenRouterProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('openrouter:anthropic/claude-3.5-sonnet')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openrouterimport OpenRouterModel
frompydantic_ai.providers.openrouterimport OpenRouterProvider

model = OpenRouterModel(
    'anthropic/claude-3.5-sonnet',
    provider=OpenRouterProvider(api_key='your-openrouter-api-key'),
)
agent = Agent(model)
...
```

## App Attribution

OpenRouter has an [app attribution](https://openrouter.ai/docs/app-attribution) feature to track your application in their public ranking and analytics.

You can pass in an `app_url` and `app_title` when initializing the provider to enable app attribution.

```
frompydantic_ai.providers.openrouterimport OpenRouterProvider

provider=OpenRouterProvider(
    api_key='your-openrouter-api-key',
    app_url='https://your-app.com',
    app_title='Your App',
),
...
```

## Model Settings

You can customize model behavior using [`OpenRouterModelSettings`](https://ai.pydantic.dev/api/models/openrouter/#pydantic_ai.models.openrouter.OpenRouterModelSettings "OpenRouterModelSettings"):

```
frompydantic_aiimport Agent
frompydantic_ai.models.openrouterimport OpenRouterModel, OpenRouterModelSettings

settings = OpenRouterModelSettings(
    openrouter_reasoning={
        'effort': 'high',
    },
    openrouter_usage={
        'include': True,
    }
)
model = OpenRouterModel('openai/gpt-5')
agent = Agent(model, model_settings=settings)
...
```