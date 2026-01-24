---
title: API Reference - Embedded function calling · Cloudflare Workers AI docs
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/index.md
source: llms
fetched_at: 2026-01-24T15:33:26.670604601-03:00
rendered_js: false
word_count: 214
summary: This document provides an API reference for Cloudflare Workers AI embedded function calling, detailing methods for executing AI models with tools and generating tool schemas from OpenAPI specifications.
tags:
    - cloudflare-workers-ai
    - function-calling
    - llm-tools
    - openapi-spec
    - ai-inference
    - api-reference
category: reference
---

Learn more about the API reference for [embedded function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded).

## runWithTools

This wrapper method enables you to do embedded function calling. You pass it the AI binding, model, inputs (`messages` array and `tools` array), and optional configurations.

* `AI Binding`Ai
  * The AI binding, such as `env.AI`.

* `model`BaseAiTextGenerationModels
  * The ID of the model that supports function calling. For example, `@hf/nousresearch/hermes-2-pro-mistral-7b`.

* `input`Object

  * `messages`RoleScopedChatInput\[]
  * `tools`AiTextGenerationToolInputWithFunction\[]

* `config`Object

  * `streamFinalResponse`boolean optional
  * `maxRecursiveToolRuns`number optional
  * `strictValidation`boolean optional
  * `verbose`boolean optional
  * `trimFunction`boolean optional - For the `trimFunction`, you can pass it `autoTrimTools`, which is another helper method we've devised to automatically choose the correct tools (using an LLM) before sending it off for inference. This means that your final inference call will have fewer input tokens.

## createToolsFromOpenAPISpec

This method lets you automatically create tool schemas based on OpenAPI specs, so you don't have to manually write or hardcode the tool schemas. You can pass the OpenAPI spec for any API in JSON or YAML format.

`createToolsFromOpenAPISpec` has a config input that allows you to perform overrides if you need to provide headers like Authentication or User-Agent.

* `spec`string
  * The OpenAPI specification in either JSON or YAML format, or a URL to a remote OpenAPI specification.

* `config`Config optional - Configuration options for the createToolsFromOpenAPISpec function

  * `overrides`ConfigRule\[] optional
  * `matchPatterns`RegExp\[] optional
  * `options` Object optional { `verbose` boolean optional }