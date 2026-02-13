---
title: Thinking Variant
url: https://openrouter.ai/docs/guides/routing/model-variants/thinking.mdx
source: llms
fetched_at: 2026-02-13T15:13:51.073237-03:00
rendered_js: false
word_count: 107
summary: This document explains how to use the :thinking model variant on OpenRouter to enable extended reasoning and chain-of-thought capabilities for complex problem-solving.
tags:
    - openrouter
    - model-variants
    - thinking-variant
    - extended-reasoning
    - chain-of-thought
    - ai-inference
category: guide
---

***

title: Thinking Variant
subtitle: 'Enable extended reasoning with :thinking'
headline: Thinking Variant | Extended Reasoning
canonical-url: '[https://openrouter.ai/docs/guides/routing/model-variants/thinking](https://openrouter.ai/docs/guides/routing/model-variants/thinking)'
'og:site\_name': OpenRouter Documentation
'og:title': Thinking Variant - Extended Reasoning
'og:description': 'Enable extended reasoning capabilities using the :thinking variant.'
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Thinking%20Variant\&description=Extended%20reasoning](https://openrouter.ai/dynamic-og?title=Thinking%20Variant\&description=Extended%20reasoning)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

The `:thinking` variant enables extended reasoning capabilities for complex problem-solving tasks.

## Usage

Append `:thinking` to any model ID:

```json
{
  "model": "deepseek/deepseek-r1:thinking"
}
```

## Details

Thinking variants provide access to models with extended reasoning capabilities, allowing for more thorough analysis and step-by-step problem solving. This is particularly useful for complex tasks that benefit from chain-of-thought reasoning.

See also: [Reasoning Tokens](/docs/best-practices/reasoning-tokens)