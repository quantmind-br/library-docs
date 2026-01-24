---
title: Bring your own generation model
url: https://developers.cloudflare.com/ai-search/how-to/bring-your-own-generation-model/index.md
source: llms
fetched_at: 2026-01-24T14:00:32.89814066-03:00
rendered_js: false
word_count: 232
summary: This guide explains how to use Cloudflare AI Search for document retrieval while leveraging external language models, such as OpenAI, for response generation.
tags:
    - cloudflare-ai-search
    - llm
    - rag
    - openai
    - workers-ai
    - external-models
    - ai-gateway
category: guide
---

---
title: Bring your own generation model · Cloudflare AI Search docs
description: When using AI Search, AI Search leverages a Workers AI model to
  generate the response. If you want to use a model outside of Workers AI, you
  can use AI Search for search while leveraging a model outside of Workers AI to
  generate responses.
lastUpdated: 2025-09-24T17:03:07.000Z
chatbotDeprioritize: false
tags: AI
source_url:
  html: https://developers.cloudflare.com/ai-search/how-to/bring-your-own-generation-model/
  md: https://developers.cloudflare.com/ai-search/how-to/bring-your-own-generation-model/index.md
---

When using `AI Search`, AI Search leverages a Workers AI model to generate the response. If you want to use a model outside of Workers AI, you can use AI Search for `search` while leveraging a model outside of Workers AI to generate responses.

Here is an example of how you can use an OpenAI model to generate your responses. This example uses [Workers Binding](https://developers.cloudflare.com/ai-search/usage/workers-binding/), but can be easily adapted to use the [REST API](https://developers.cloudflare.com/ai-search/usage/rest-api/) instead.

Note

AI Search now supports [bringing your own models natively](https://developers.cloudflare.com/ai-search/configuration/models/). You can attach provider keys through AI Gateway and select third-party models directly in your AI Search settings. The example below still works, but the recommended way is to configure your external model through AI Gateway.

* JavaScript

  ```js
  import { openai } from "@ai-sdk/openai";
  import { generateText } from "ai";


  export default {
    async fetch(request, env) {
      // Parse incoming url
      const url = new URL(request.url);


      // Get the user query or default to a predefined one
      const userQuery =
        url.searchParams.get("query") ??
        "How do I train a llama to deliver coffee?";


      // Search for documents in AI Search
      const searchResult = await env.AI.autorag("my-rag").search({
        query: userQuery,
      });


      if (searchResult.data.length === 0) {
        // No matching documents
        return Response.json({ text: `No data found for query "${userQuery}"` });
      }


      // Join all document chunks into a single string
      const chunks = searchResult.data
        .map((item) => {
          const data = item.content
            .map((content) => {
              return content.text;
            })
            .join("\n\n");


          return `<file name="${item.filename}">${data}</file>`;
        })
        .join("\n\n");


      // Send the user query + matched documents to openai for answer
      const generateResult = await generateText({
        model: openai("gpt-4o-mini"),
        messages: [
          {
            role: "system",
            content:
              "You are a helpful assistant and your task is to answer the user question using the provided files.",
          },
          { role: "user", content: chunks },
          { role: "user", content: userQuery },
        ],
      });


      // Return the generated answer
      return Response.json({ text: generateResult.text });
    },
  };
  ```

* TypeScript

  ```ts
  import { openai } from "@ai-sdk/openai";
  import { generateText } from "ai";


  export interface Env {
    AI: Ai;
    OPENAI_API_KEY: string;
  }


  export default {
    async fetch(request, env): Promise<Response> {
      // Parse incoming url
      const url = new URL(request.url);


      // Get the user query or default to a predefined one
      const userQuery =
        url.searchParams.get("query") ??
        "How do I train a llama to deliver coffee?";


      // Search for documents in AI Search
      const searchResult = await env.AI.autorag("my-rag").search({
        query: userQuery,
      });


      if (searchResult.data.length === 0) {
        // No matching documents
        return Response.json({ text: `No data found for query "${userQuery}"` });
      }


      // Join all document chunks into a single string
      const chunks = searchResult.data
        .map((item) => {
          const data = item.content
            .map((content) => {
              return content.text;
            })
            .join("\n\n");


          return `<file name="${item.filename}">${data}</file>`;
        })
        .join("\n\n");


      // Send the user query + matched documents to openai for answer
      const generateResult = await generateText({
        model: openai("gpt-4o-mini"),
        messages: [
          {
            role: "system",
            content:
              "You are a helpful assistant and your task is to answer the user question using the provided files.",
          },
          { role: "user", content: chunks },
          { role: "user", content: userQuery },
        ],
      });


      // Return the generated answer
      return Response.json({ text: generateResult.text });
    },
  } satisfies ExportedHandler<Env>;
  ```