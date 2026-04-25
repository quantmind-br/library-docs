---
title: Text-only Generators
url: https://lmstudio.ai/docs/typescript/plugins/generator/text-only-generators
source: sitemap
fetched_at: 2026-04-07T21:32:28.06430749-03:00
rendered_js: false
word_count: 112
summary: This document explains how generators function within a controller context, detailing methods for reporting generated text and covering specific operational aspects like accessing custom configurations and handling user abort signals.
tags:
    - generator-api
    - conversation-state
    - custom-configurations
    - abort-signal
    - plugin-config
category: reference
---

Generators take in the the generator controller and the current conversation state, start the generation, and then report the generated text using the `ctl.fragmentGenerated` method.

The following is an example of a simple generator that echos back the last user message with 200 ms delay between each word:

## Custom Configurations[](#custom-configurations "Link to 'Custom Configurations'")

You can access custom configurations via `ctl.getPluginConfig` and `ctl.getGlobalPluginConfig`. See [Custom Configurations](https://lmstudio.ai/docs/typescript/plugins/generator/configurations) for more details.

## Handling Aborts[](#handling-aborts "Link to 'Handling Aborts'")

A prediction may be aborted by the user while your generator is still running. In such cases, you should handle the abort gracefully by handling the `ctl.abortSignal`.

You can learn more about `AbortSignal` in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal).