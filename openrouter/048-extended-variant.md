---
title: Extended Variant
url: https://openrouter.ai/docs/guides/routing/model-variants/extended.mdx
source: llms
fetched_at: 2026-02-13T15:13:47.606741-03:00
rendered_js: false
word_count: 100
summary: This document explains how to use the :extended variant suffix on OpenRouter to access model versions with larger context windows. It provides instructions on appending the suffix to model IDs to handle longer inputs and conversation histories.
tags:
    - openrouter
    - model-variants
    - context-window
    - extended-context
    - routing
category: guide
---

***

title: Extended Variant
subtitle: 'Extended context windows with :extended'
headline: Extended Variant | Extended Context Windows
canonical-url: '[https://openrouter.ai/docs/guides/routing/model-variants/extended](https://openrouter.ai/docs/guides/routing/model-variants/extended)'
'og:site\_name': OpenRouter Documentation
'og:title': Extended Variant - Extended Context Windows
'og:description': 'Access extended context window versions of models using the :extended variant.'
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Extended%20Variant\&description=Extended%20context%20windows](https://openrouter.ai/dynamic-og?title=Extended%20Variant\&description=Extended%20context%20windows)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

The `:extended` variant provides access to model versions with extended context windows.

## Usage

Append `:extended` to any model ID:

```json
{
  "model": "anthropic/claude-sonnet-4.5:extended"
}
```

## Details

Extended variants offer larger context windows than the standard model versions, allowing you to process longer inputs and maintain more conversation history.