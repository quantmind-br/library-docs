---
title: Use fetch() handler
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/fetch/index.md
source: llms
fetched_at: 2026-01-24T15:33:29.766361281-03:00
rendered_js: false
word_count: 150
summary: This document explains how to implement function calling within a Cloudflare Workers fetch handler to enable AI models to perform external API requests.
tags:
    - cloudflare-workers-ai
    - function-calling
    - fetch-api
    - serverless-ai
    - llm-tools
category: tutorial
---

---
title: Use fetch() handler · Cloudflare Workers AI docs
description: Learn how to use the fetch() handler in Cloudflare Workers AI to
  enable LLMs to perform API calls, like retrieving a 5-day weather forecast
  using function calling.
lastUpdated: 2025-04-03T16:21:18.000Z
chatbotDeprioritize: false
tags: AI
source_url:
  html: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/fetch/
  md: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/fetch/index.md
---

A very common use case is to provide the LLM with the ability to perform API calls via function calling.

In this example the LLM will retrieve the weather forecast for the next 5 days. To do so a `getWeather` function is defined that is passed to the LLM as tool.

The `getWeather`function extracts the user's location from the request and calls the external weather API via the Workers' [`Fetch API`](https://developers.cloudflare.com/workers/runtime-apis/fetch/) and returns the result.

```ts
import { runWithTools } from '@cloudflare/ai-utils';


type Env = {
  AI: Ai;
};


export default {
  async fetch(request, env, ctx) {
    // Define function
    const getWeather = async (args: { numDays: number }) => {
      const { numDays } = args;
      // Location is extracted from request based on
      // https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties
      const lat = request.cf?.latitude
      const long = request.cf?.longitude


      // Interpolate values for external API call
      const response = await fetch(
        `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${long}&daily=temperature_2m_max,precipitation_sum&timezone=GMT&forecast_days=${numDays}`
      );
      return response.text();
    };
    // Run AI inference with function calling
    const response = await runWithTools(
      env.AI,
      // Model with function calling support
      '@hf/nousresearch/hermes-2-pro-mistral-7b',
      {
        // Messages
        messages: [
          {
            role: 'user',
            content: 'What the weather like the next 5 days? Respond as text',
          },
        ],
        // Definition of available tools the AI model can leverage
        tools: [
          {
            name: 'getWeather',
            description: 'Get the weather for the next [numDays] days',
            parameters: {
              type: 'object',
              properties: {
                numDays: { type: 'numDays', description: 'number of days for the weather forecast' },
              },
              required: ['numDays'],
            },
            // reference to previously defined function
            function: getWeather,
          },
        ],
      }
    );
    return new Response(JSON.stringify(response));
  },
} satisfies ExportedHandler<Env>;
```