---
title: Deploy a Worker that connects to OpenAI via AI Gateway
url: https://developers.cloudflare.com/ai-gateway/tutorials/deploy-aig-worker/index.md
source: llms
fetched_at: 2026-01-24T15:07:40.593881391-03:00
rendered_js: false
word_count: 665
summary: This tutorial provides a step-by-step guide on how to deploy a Cloudflare Worker that connects to the OpenAI API through Cloudflare AI Gateway to enable better analytics, caching, and rate limiting.
tags:
    - cloudflare-workers
    - ai-gateway
    - openai
    - javascript
    - serverless
    - api-integration
    - deployment
category: tutorial
---

---
title: Deploy a Worker that connects to OpenAI via AI Gateway · Cloudflare AI
  Gateway docs
description: Learn how to deploy a Worker that makes calls to OpenAI through AI Gateway
lastUpdated: 2025-11-14T10:07:26.000Z
chatbotDeprioritize: false
tags: AI,JavaScript
source_url:
  html: https://developers.cloudflare.com/ai-gateway/tutorials/deploy-aig-worker/
  md: https://developers.cloudflare.com/ai-gateway/tutorials/deploy-aig-worker/index.md
---

In this tutorial, you will learn how to deploy a Worker that makes calls to OpenAI through AI Gateway. AI Gateway helps you better observe and control your AI applications with more analytics, caching, rate limiting, and logging.

This tutorial uses the most recent v4 OpenAI node library, an update released in August 2023.

## Before you start

All of the tutorials assume you have already completed the [Get started guide](https://developers.cloudflare.com/workers/get-started/guide/), which gets you set up with a Cloudflare Workers account, [C3](https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare), and [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/).

## 1. Create an AI Gateway and OpenAI API key

On the AI Gateway page in the Cloudflare dashboard, create a new AI Gateway by clicking the plus button on the top right. You should be able to name the gateway as well as the endpoint. Click on the API Endpoints button to copy the endpoint. You can choose from provider-specific endpoints such as OpenAI, HuggingFace, and Replicate. Or you can use the universal endpoint that accepts a specific schema and supports model fallback and retries.

For this tutorial, we will be using the OpenAI provider-specific endpoint, so select OpenAI in the dropdown and copy the new endpoint.

You will also need an OpenAI account and API key for this tutorial. If you do not have one, create a new OpenAI account and create an API key to continue with this tutorial. Make sure to store your API key somewhere safe so you can use it later.

## 2. Create a new Worker

Create a Worker project in the command line:

* npm

  ```sh
  npm create cloudflare@latest -- openai-aig
  ```

* yarn

  ```sh
  yarn create cloudflare openai-aig
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest openai-aig
  ```

For setup, select the following options:

* For *What would you like to start with?*, choose `Hello World example`.
* For *Which template would you like to use?*, choose `Worker only`.
* For *Which language do you want to use?*, choose `JavaScript`.
* For *Do you want to use git for version control?*, choose `Yes`.
* For *Do you want to deploy your application?*, choose `No` (we will be making some changes before deploying).

Go to your new open Worker project:

```sh
cd openai-aig
```

Inside of your new openai-aig directory, find and open the `src/index.js` file. You will configure this file for most of the tutorial.

Initially, your generated `index.js` file should look like this:

```js
export default {
  async fetch(request, env, ctx) {
    return new Response("Hello World!");
  },
};
```

## 3. Configure OpenAI in your Worker

With your Worker project created, we can learn how to make your first request to OpenAI. You will use the OpenAI node library to interact with the OpenAI API. Install the OpenAI node library with `npm`:

* npm

  ```sh
  npm i openai
  ```

* yarn

  ```sh
  yarn add openai
  ```

* pnpm

  ```sh
  pnpm add openai
  ```

In your `src/index.js` file, add the import for `openai` above `export default`:

```js
import OpenAI from "openai";
```

Within your `fetch` function, set up the configuration and instantiate your `OpenAIApi` client with the AI Gateway endpoint you created:

```js
import OpenAI from "openai";


export default {
  async fetch(request, env, ctx) {
    const openai = new OpenAI({
      apiKey: env.OPENAI_API_KEY,
      baseURL:
        "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai", // paste your AI Gateway endpoint here
    });
  },
};
```

To make this work, you need to use [`wrangler secret put`](https://developers.cloudflare.com/workers/wrangler/commands/#secret-put) to set your `OPENAI_API_KEY`. This will save the API key to your environment so your Worker can access it when deployed. This key is the API key you created earlier in the OpenAI dashboard:

* npm

  ```sh
  npx wrangler secret put OPENAI_API_KEY
  ```

* yarn

  ```sh
  yarn wrangler secret put OPENAI_API_KEY
  ```

* pnpm

  ```sh
  pnpm wrangler secret put OPENAI_API_KEY
  ```

To make this work in local development, create a new file `.dev.vars` in your Worker project and add this line. Make sure to replace `OPENAI_API_KEY` with your own OpenAI API key:

```txt
OPENAI_API_KEY = "<YOUR_OPENAI_API_KEY_HERE>"
```

## 4. Make an OpenAI request

Now we can make a request to the OpenAI [Chat Completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api).

You can specify what model you'd like, the role and prompt, as well as the max number of tokens you want in your total request.

```js
import OpenAI from "openai";


export default {
  async fetch(request, env, ctx) {
    const openai = new OpenAI({
      apiKey: env.OPENAI_API_KEY,
      baseURL:
        "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
    });


    try {
      const chatCompletion = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        messages: [{ role: "user", content: "What is a neuron?" }],
        max_tokens: 100,
      });


      const response = chatCompletion.choices[0].message;


      return new Response(JSON.stringify(response));
    } catch (e) {
      return new Response(e);
    }
  },
};
```

## 5. Deploy your Worker application

To deploy your application, run the `npx wrangler deploy` command to deploy your Worker application:

* npm

  ```sh
  npx wrangler deploy
  ```

* yarn

  ```sh
  yarn wrangler deploy
  ```

* pnpm

  ```sh
  pnpm wrangler deploy
  ```

You can now preview your Worker at \<YOUR\_WORKER>.\<YOUR\_SUBDOMAIN>.workers.dev.

## 6. Review your AI Gateway

When you go to AI Gateway in your Cloudflare dashboard, you should see your recent request being logged. You can also [tweak your settings](https://developers.cloudflare.com/ai-gateway/configuration/) to manage your logs, caching, and rate limiting settings.