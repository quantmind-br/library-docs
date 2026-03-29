---
title: Tools based on OpenAPI Spec
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/index.md
source: llms
fetched_at: 2026-01-24T15:33:34.395835231-03:00
rendered_js: false
word_count: 103
summary: This document explains how to use the Cloudflare ai-utils package to automatically generate function-calling tools for LLMs from an OpenAPI specification.
tags:
    - cloudflare-workers
    - workers-ai
    - openapi
    - function-calling
    - ai-utils
    - javascript-sdk
category: guide
---

---
title: Tools based on OpenAPI Spec · Cloudflare Workers AI docs
description: Oftentimes APIs are defined and documented via OpenAPI
  specification. The Cloudflare ai-utils package's createToolsFromOpenAPISpec
  function creates tools from the OpenAPI spec, which the LLM can then leverage
  to fulfill the prompt.
lastUpdated: 2025-04-03T16:21:18.000Z
chatbotDeprioritize: false
tags: AI
source_url:
  html: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/
  md: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/index.md
---

Oftentimes APIs are defined and documented via [OpenAPI specification](https://swagger.io/specification/). The Cloudflare `ai-utils` package's `createToolsFromOpenAPISpec` function creates tools from the OpenAPI spec, which the LLM can then leverage to fulfill the prompt.

In this example the LLM will describe the a Github user, based Github's API and its OpenAPI spec.

```ts
import { createToolsFromOpenAPISpec, runWithTools } from '@cloudflare/ai-utils';


type Env = {
  AI: Ai;
};


const APP_NAME = 'cf-fn-calling-example-app';


export default {
  async fetch(request, env, ctx) {
    const toolsFromOpenAPISpec = [
      // You can pass the OpenAPI spec link or contents directly
      ...(await createToolsFromOpenAPISpec(
        'https://gist.githubusercontent.com/mchenco/fd8f20c8f06d50af40b94b0671273dc1/raw/f9d4b5cd5944cc32d6b34cad0406d96fd3acaca6/partial_api.github.com.json',
        {
          overrides: [
            {
              matcher: ({ url }) => {
                return url.hostname === 'api.github.com';
              },
              // for all requests on *.github.com, we'll need to add a User-Agent.
              values: {
                headers: {
                  'User-Agent': APP_NAME,
                },
              },
            },
          ],
        }
      )),
    ];


    const response = await runWithTools(
      env.AI,
      '@hf/nousresearch/hermes-2-pro-mistral-7b',
      {
        messages: [
          {
            role: 'user',
            content: 'Who is cloudflare on Github and how many repos does the organization have?',
          },
        ],
        tools: toolsFromOpenAPISpec,
      }
    );


    return new Response(JSON.stringify(response));
  },
} satisfies ExportedHandler<Env>;
```