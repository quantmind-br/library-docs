---
title: Introduction
url: https://lmstudio.ai/docs/typescript/plugins/generator
source: sitemap
fetched_at: 2026-04-07T21:32:26.472823808-03:00
rendered_js: false
word_count: 143
summary: This document explains that generators serve as substitutes for local LLMs, directing text generation through external or remote sources instead of the locally loaded model.
tags:
    - generators
    - llm-adapters
    - remote-models
    - api-integration
    - plugin-functionality
category: guide
---

Generators are replacement for local LLMs. They act like a token source. When a plugin with a generator is used, LM Studio will no longer use the local model to generate text. The generator will be used instead.

Generators are useful for implementing adapters for external models, such as using a remote LM Studio instance or other online models.

If a plugin contains a generator, it will no longer show up in the plugins list. Instead, it will show up in the model dropdown and act as a model. If your plugins contains [Tools Provider](https://lmstudio.ai/docs/typescript/plugins/tools-providers.md) or [Prompt Preprocessor](https://lmstudio.ai/docs/typescript/plugins/prompt-preprocessors.md), they will be used when your generator is being selected.

## Examples[](#examples "Link to 'Examples'")

The following are some plugins that make use of generators:

- [lmstudio/remote-lmstudio](https://lmstudio.ai/lmstudio/remote-lmstudio)
  
  Basic support for using a remote LM Studio instance to generate text.
- [lmstudio/openai-compat-endpoint](https://lmstudio.ai/lmstudio/openai-compat-endpoint)
  
  Use any OpenAI-compatible API in LM Studio.