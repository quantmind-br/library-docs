---
title: Mistral Docs
url: https://docs.mistral.ai/capabilities/structured_output
source: crawler
fetched_at: 2026-01-29T07:33:10.461599024-03:00
rendered_js: false
word_count: 184
summary: This document explains how to configure Mistral AI models to provide structured outputs, specifically detailing the differences and use cases for JSON mode and custom schemas.
tags:
    - structured-outputs
    - json-mode
    - mistral-ai
    - output-formatting
    - api-integration
category: guide
---

## Structured Outputs

When utilizing LLMs as agents or steps within a lengthy process, chain, or pipeline, it is often necessary for the outputs to adhere to a specific structured format. JSON is the most commonly used format for this purpose.

Before continuing, we recommend reading the [Chat Competions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.

We offer a reliable method to obtain structured output in your desired format.

Our system includes a built-in mode for JSON output, along with the capability to use custom structured outputs.

For JSON mode, it is essential to explicitly instruct the model in your prompt to output JSON and specify the desired format.

Custom structured outputs are more reliable and are recommended whenever possible. However, it is still advisable to iterate on your prompts.  
Use JSON mode when more flexibility in the output is required while maintaining a JSON structure, and customize it if you want to enforce a clearer format to improve reliability.

- [Custom](https://docs.mistral.ai/capabilities/structured_output/custom): Use your own schema to enforce a specific format.
- [JSON](https://docs.mistral.ai/capabilities/structured_output/json_mode): To enforce a JSON output.