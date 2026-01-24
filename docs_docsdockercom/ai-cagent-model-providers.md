---
title: Model providers
url: https://docs.docker.com/ai/cagent/model-providers/
source: llms
fetched_at: 2026-01-24T14:13:33.107848787-03:00
rendered_js: false
word_count: 338
summary: This document explains how to configure cloud-based large language model providers for cagent, including setup instructions for Anthropic, OpenAI, and Google Gemini.
tags:
    - cagent
    - cloud-providers
    - llm-configuration
    - api-keys
    - anthropic
    - openai
    - google-gemini
    - environment-variables
category: guide
---

To run cagent, you need a model provider. You can either use a cloud provider with an API key or run models locally with [Docker Model Runner](https://docs.docker.com/ai/cagent/local-models/).

This guide covers cloud providers. For the local alternative, see [Local models with Docker Model Runner](https://docs.docker.com/ai/cagent/local-models/).

## [Supported providers](#supported-providers)

cagent supports these cloud model providers:

- Anthropic - Claude models
- OpenAI - GPT models
- Google - Gemini models

## [Anthropic](#anthropic)

Anthropic provides the Claude family of models, including Claude Sonnet and Claude Opus.

To get an API key:

1. Go to [console.anthropic.com](https://console.anthropic.com/).
2. Sign up or sign in to your account.
3. Navigate to the API Keys section.
4. Create a new API key.
5. Copy the key.

Set your API key as an environment variable:

```
$ export ANTHROPIC_API_KEY=your_key_here
```

Use Anthropic models in your agent configuration:

```
agents:root:model:anthropic/claude-sonnet-4-5instruction:You are a helpful coding assistant
```

Available models include:

- `anthropic/claude-sonnet-4-5`
- `anthropic/claude-opus-4-5`
- `anthropic/claude-haiku-4-5`

## [OpenAI](#openai)

OpenAI provides the GPT family of models, including GPT-5 and GPT-5 mini.

To get an API key:

1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
2. Sign up or sign in to your account.
3. Navigate to the API Keys section.
4. Create a new API key.
5. Copy the key.

Set your API key as an environment variable:

```
$ export OPENAI_API_KEY=your_key_here
```

Use OpenAI models in your agent configuration:

```
agents:root:model:openai/gpt-5instruction:You are a helpful coding assistant
```

Available models include:

- `openai/gpt-5`
- `openai/gpt-5-mini`

## [Google Gemini](#google-gemini)

Google provides the Gemini family of models.

To get an API key:

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey).
2. Sign in with your Google account.
3. Create an API key.
4. Copy the key.

Set your API key as an environment variable:

```
$ export GOOGLE_API_KEY=your_key_here
```

Use Gemini models in your agent configuration:

```
agents:root:model:google/gemini-2.5-flashinstruction:You are a helpful coding assistant
```

Available models include:

- `google/gemini-2.5-flash`
- `google/gemini-2.5-pro`

## [OpenAI-compatible providers](#openai-compatible-providers)

You can use the `openai` provider type to connect to any model or provider that implements the OpenAI API specification. This includes services like Azure OpenAI, local inference servers, and other compatible endpoints.

Configure an OpenAI-compatible provider by specifying the base URL:

```
agents:root:model:openai/your-model-nameinstruction:You are a helpful coding assistantprovider:base_url:https://your-provider.example.com/v1
```

By default, cagent uses the `OPENAI_API_KEY` environment variable for authentication. If your provider uses a different variable, specify it with `token_key`:

```
agents:root:model:openai/your-model-nameinstruction:You are a helpful coding assistantprovider:base_url:https://your-provider.example.com/v1token_key:YOUR_PROVIDER_API_KEY
```

## [What's next](#whats-next)

- Follow the [tutorial](https://docs.docker.com/ai/cagent/tutorial/) to build your first agent
- Learn about [local models with Docker Model Runner](https://docs.docker.com/ai/cagent/local-models/) as an alternative to cloud providers
- Review the [configuration reference](https://docs.docker.com/ai/cagent/reference/config/) for advanced model settings