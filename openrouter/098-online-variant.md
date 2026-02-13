---
title: Online Variant
url: https://openrouter.ai/docs/guides/routing/model-variants/online.mdx
source: llms
fetched_at: 2026-02-13T15:13:52.621244-03:00
rendered_js: false
word_count: 131
summary: This document explains how to use the :online model variant to enable real-time web search capabilities for models on OpenRouter.
tags:
    - openrouter
    - web-search
    - model-variants
    - real-time-data
    - api-plugins
category: guide
---

***

title: Online Variant
subtitle: 'Real-time web search with :online'
headline: Online Variant | Real-Time Web Search
canonical-url: '[https://openrouter.ai/docs/guides/routing/model-variants/online](https://openrouter.ai/docs/guides/routing/model-variants/online)'
'og:site\_name': OpenRouter Documentation
'og:title': Online Variant - Real-Time Web Search
'og:description': 'Enable real-time web search capabilities using the :online variant.'
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Online%20Variant\&description=Real-time%20web%20search](https://openrouter.ai/dynamic-og?title=Online%20Variant\&description=Real-time%20web%20search)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

The `:online` variant enables real-time web search capabilities for any model on OpenRouter.

## Usage

Append `:online` to any model ID:

```json
{
  "model": "openai/gpt-5.2:online"
}
```

This is a shortcut for using the `web` plugin, and is exactly equivalent to:

```json
{
  "model": "openrouter/auto",
  "plugins": {
    "web": {}
  }
}
```

## Details

The Online variant incorporates relevant web search results into model responses, providing access to real-time information and current events. This is particularly useful for queries that require up-to-date information beyond the model's training data.

For more details, see: [Web Search](/docs/guides/features/plugins/web-search)