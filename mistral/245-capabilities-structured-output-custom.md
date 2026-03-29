---
title: Custom | Mistral Docs
url: https://docs.mistral.ai/capabilities/structured_output/custom
source: crawler
fetched_at: 2026-01-29T07:34:13.033305543-03:00
rendered_js: false
word_count: 189
summary: Documentation providing instructions on how to create and fine-tune custom models within the Mistral AI ecosystem.
tags:
    - Mistral AI
    - fine-tuning
    - custom models
    - LLM
category: guide
---

## Custom Structured Outputs

Custom Structured Outputs allow you to ensure the model provides an answer in a very specific JSON format by supplying a clear JSON schema. This approach allows the model to consistently deliver responses with the correct typing and keywords.

### Generate and Use custom Structured Outputs

Here is an example of how to achieve this using the Mistral AI client and Pydantic/Zod/JSON Schemas:

First, define the structure of the output using a Pydantic, Zod or a JSON Schema:

Next, make a request and ensure the response adheres to the defined structure using `response_format` set to the corresponding model:

In this example, the `Book` class defines the structure of the output, ensuring that the model's response adheres to the specified format.

There are two types of possible outputs that are easily accessible via our SDK.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.

To better guide the model, the following is being always prepended to the System Prompt when using this method:

However, it is recommended to add more explanations and iterate on your system prompt to better clarify the expected schema and behavior.