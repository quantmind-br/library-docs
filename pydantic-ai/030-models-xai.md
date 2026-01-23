---
title: xAI - Pydantic AI
url: https://ai.pydantic.dev/models/xai/
source: sitemap
fetched_at: 2026-01-22T22:26:21.47048357-03:00
rendered_js: false
word_count: 88
summary: This document provides instructions for installing and configuring xAI models within the Pydantic AI framework, including API key setup and model initialization techniques.
tags:
    - pydantic-ai
    - xai-model
    - python-sdk
    - api-configuration
    - environment-variables
category: guide
---

## Install

To use [`XaiModel`](https://ai.pydantic.dev/api/models/xai/#pydantic_ai.models.xai.XaiModel "XaiModel"), you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `xai` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[xai]"
```

```
uvadd"pydantic-ai-slim[xai]"
```

## Configuration

To use xAI models from [xAI](https://x.ai/api) through their API, go to [console.x.ai](https://console.x.ai/team/default/api-keys) to create an API key.

\[docs.x.ai]\[https://docs.x.ai/docs/models] contains a list of available xAI models.

## Environment variable

Once you have the API key, you can set it as an environment variable:

```
exportXAI_API_KEY='your-api-key'
```

You can then use [`XaiModel`](https://ai.pydantic.dev/api/models/xai/#pydantic_ai.models.xai.XaiModel "XaiModel") by name:

```
frompydantic_aiimport Agent

agent = Agent('xai:grok-4-1-fast-non-reasoning')
...
```

Or initialise the model directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.xaiimport XaiModel

# Uses XAI_API_KEY environment variable
model = XaiModel('grok-4-1-fast-non-reasoning')
agent = Agent(model)
...
```

You can also customize the [`XaiModel`](https://ai.pydantic.dev/api/models/xai/#pydantic_ai.models.xai.XaiModel "XaiModel") with a custom provider:

```
frompydantic_aiimport Agent
frompydantic_ai.models.xaiimport XaiModel
frompydantic_ai.providers.xaiimport XaiProvider

# Custom API key
provider = XaiProvider(api_key='your-api-key')
model = XaiModel('grok-4-1-fast-non-reasoning', provider=provider)
agent = Agent(model)
...
```

Or with a custom `xai_sdk.AsyncClient`:

```
fromxai_sdkimport AsyncClient

frompydantic_aiimport Agent
frompydantic_ai.models.xaiimport XaiModel
frompydantic_ai.providers.xaiimport XaiProvider

xai_client = AsyncClient(api_key='your-api-key')
provider = XaiProvider(xai_client=xai_client)
model = XaiModel('grok-4-1-fast-non-reasoning', provider=provider)
agent = Agent(model)
...
```