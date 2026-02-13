---
title: LiveKit
url: https://openrouter.ai/docs/guides/community/livekit.mdx
source: llms
fetched_at: 2026-02-13T15:15:42.120412-03:00
rendered_js: false
word_count: 207
summary: This document explains how to integrate OpenRouter with the LiveKit Agents framework to build voice-enabled AI agents with access to multiple models. It covers installation, authentication, and advanced features like fallback models and provider routing.
tags:
    - livekit-agents
    - openrouter
    - voice-ai
    - python-sdk
    - llm-integration
    - model-routing
category: guide
---

***

title: LiveKit
subtitle: Using OpenRouter with LiveKit Agents
headline: LiveKit Integration | OpenRouter SDK Support
canonical-url: '[https://openrouter.ai/docs/guides/community/livekit](https://openrouter.ai/docs/guides/community/livekit)'
'og:site\_name': OpenRouter Documentation
'og:title': LiveKit Integration - OpenRouter SDK Support
'og:description': >-
Integrate OpenRouter using LiveKit Agents framework. Complete guide for
LiveKit integration with OpenRouter to build voice AI agents with access to
300+ models.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=LiveKit\&description=LiveKit%20Integration](https://openrouter.ai/dynamic-og?title=LiveKit\&description=LiveKit%20Integration)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

## Using LiveKit Agents

[LiveKit Agents](https://docs.livekit.io/agents/) is an open-source framework for building voice AI agents. The OpenRouter plugin allows you to access 300+ AI models from multiple providers through a unified API, with automatic fallback support and intelligent routing.

### Installation

Install the OpenAI plugin to add OpenRouter support:

```bash
uv add "livekit-agents[openai]~=1.2"
```

### Authentication

The OpenRouter plugin requires an [OpenRouter API key](https://openrouter.ai/settings/keys). Set `OPENROUTER_API_KEY` in your `.env` file.

### Basic Usage

Create an OpenRouter LLM using the `with_openrouter` method:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  session = AgentSession(
      llm=openai.LLM.with_openrouter(model="anthropic/claude-sonnet-4.5"),
      # ... tts, stt, vad, turn_detection, etc.
  )
  ```
</CodeGroup>

### Advanced Features

#### Fallback Models

Configure multiple fallback models to use if the primary model is unavailable:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="openai/gpt-4o",
      fallback_models=[
          "anthropic/claude-sonnet-4",
          "openai/gpt-5-mini",
      ],
  )
  ```
</CodeGroup>

#### Provider Routing

Control which providers are used for model inference:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="deepseek/deepseek-chat-v3.1",
      provider={
          "order": ["novita/fp8", "gmicloud/fp8", "google-vertex"],
          "allow_fallbacks": True,
          "sort": "latency",
      },
  )
  ```
</CodeGroup>

#### Web Search Plugin

Enable OpenRouter's web search capabilities:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="google/gemini-2.5-flash-preview-09-2025",
      plugins=[
          openai.OpenRouterWebPlugin(
              max_results=5,
              search_prompt="Search for relevant information",
          )
      ],
  )
  ```
</CodeGroup>

#### Analytics Integration

Include site and app information for OpenRouter analytics:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="openrouter/auto",
      site_url="https://myapp.com",
      app_name="My Voice Agent",
  )
  ```
</CodeGroup>

### Resources

* [LiveKit OpenRouter Plugin Documentation](https://docs.livekit.io/agents/models/llm/plugins/openrouter/)
* [LiveKit Agents GitHub](https://github.com/livekit/agents)
* [OpenRouter Models](https://openrouter.ai/models)