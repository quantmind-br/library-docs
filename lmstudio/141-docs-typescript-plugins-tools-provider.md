---
title: Introduction to Tools Provider
url: https://lmstudio.ai/docs/typescript/plugins/tools-provider
source: sitemap
fetched_at: 2026-04-07T21:32:03.958894566-03:00
rendered_js: false
word_count: 85
summary: This document explains the concept and purpose of writing tools providers for LM Studio plugins using TypeScript, detailing how these providers equip large language models with external functionalities.
tags:
    - lmstudio
    - tools-provider
    - typescript
    - plugin-development
    - llm-integration
category: guide
---

Writing tools providers for LM Studio plugins using TypeScript

Tools provider is a function that returns an array of tools that the model can use during generation.

## Examples[](#examples "Link to 'Examples'")

The following are some plugins that make use of tools providers:

- [lmstudio/wikipedia](https://lmstudio.ai/lmstudio/wikipedia)
  
  Gives the LLM tools to search and read Wikipedia articles.
- [lmstudio/js-code-sandbox](https://lmstudio.ai/lmstudio/js-code-sandbox)
  
  Gives the LLM tools to run JavaScript/TypeScript code in a sandbox environment using [deno](https://deno.com/).
- [lmstudio/dice](https://lmstudio.ai/lmstudio/dice)
  
  Allows the LLM to generate random numbers using "dice".

This page's source is available on [GitHub](https://github.com/lmstudio-ai/docs/blob/main/2_typescript/3_plugins/1_tools-provider/index.md)