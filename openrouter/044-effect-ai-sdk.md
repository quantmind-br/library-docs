---
title: Effect AI SDK
url: https://openrouter.ai/docs/guides/community/effect-ai-sdk.mdx
source: llms
fetched_at: 2026-02-13T15:15:37.119851-03:00
rendered_js: false
word_count: 146
summary: This document provides instructions for integrating OpenRouter with the Effect AI SDK, including necessary package installations and a TypeScript implementation example for streaming text.
tags:
    - openrouter
    - effect-ai-sdk
    - typescript
    - ai-integration
    - sdk-setup
    - streaming-api
category: guide
---

***

title: Effect AI SDK
subtitle: Integrate OpenRouter using the Effect AI SDK
headline: Effect AI SDK Integration | OpenRouter SDK Support
canonical-url: '[https://openrouter.ai/docs/guides/community/effect-ai-sdk](https://openrouter.ai/docs/guides/community/effect-ai-sdk)'
'og:site\_name': OpenRouter Documentation
'og:title': Effect AI SDK Integration - OpenRouter SDK Support
'og:description': >-
Integrate OpenRouter using the Effect AI SDK. Complete guide for integrating
the Effect AI SDK with OpenRouter.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Effect%20AI%20SDK\&description=Effect%20AI%20SDK%20Integration](https://openrouter.ai/dynamic-og?title=Effect%20AI%20SDK\&description=Effect%20AI%20SDK%20Integration)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

## Effect AI SDK

You can use the [Effect AI SDK](https://www.npmjs.com/package/@effect/ai) to integrate OpenRouter with your Effect applications. To get started, install the following packages:

* [effect](https://www.npmjs.com/package/effect): the Effect core (if not already installed)
* [@effect/ai](https://www.npmjs.com/package/@effect/ai): the core Effect AI SDK abstractions
* [@effect/ai-openrouter](https://www.npmjs.com/package/@effect/ai-openrouter): the Effect AI provider integration for OpenRouter
* [@effect/platform](https://www.npmjs.com/package/@effect/platform): platform-agnostic abstractions for Effect

```bash
npm install effect @effect/ai @effect/ai-openrouter @effect/platform
```

Once that's done you can use the [LanguageModel](https://effect.website/docs/ai/getting-started/#define-an-interaction-with-a-language-model) module to define interactions with a large language model via OpenRouter.

<CodeGroup>
  ```typescript title="TypeScript"
  import { LanguageModel } from "@effect/ai"
  import { OpenRouterClient, OpenRouterLanguageModel } from "@effect/ai-openrouter"
  import { FetchHttpClient } from "@effect/platform"
  import { Config, Effect, Layer, Stream } from "effect"

  const Gpt4o = OpenRouterLanguageModel.model("openai/gpt-4o")

  const program = LanguageModel.streamText({
    prompt: [
      { role: "system", content: "You are a comedian with a penchant for groan-inducing puns" },
      { role: "user", content: [{ type: "text", text: "Tell me a dad joke" }] }
    ]
  }).pipe(
    Stream.filter((part) => part.type === "text-delta"),
    Stream.runForEach((part) => Effect.sync(() => process.stdout.write(part.delta))),
    Effect.provide(Gpt4o)
  )

  const OpenRouter = OpenRouterClient.layerConfig({
    apiKey: Config.redacted("OPENROUTER_API_KEY")
  }).pipe(Layer.provide(FetchHttpClient.layer))

  program.pipe(
    Effect.provide(OpenRouter),
    Effect.runPromise
  )
  ```
</CodeGroup>