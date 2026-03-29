---
title: Nuxt
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/nuxt/index.md
source: llms
fetched_at: 2026-01-24T15:31:35.208259601-03:00
rendered_js: false
word_count: 279
summary: This guide provides instructions for creating, developing, and deploying a Nuxt application to Cloudflare Workers using the create-cloudflare CLI and Workers Assets. It also details how to integrate Cloudflare product bindings into a Nuxt project for access to storage, AI, and compute services.
tags:
    - nuxt
    - cloudflare-workers
    - workers-assets
    - deployment
    - full-stack
    - create-cloudflare
    - nitro
category: guide
---

---
title: Nuxt · Cloudflare Workers docs
description: Create a Nuxt application and deploy it to Cloudflare Workers with
  Workers Assets.
lastUpdated: 2025-08-20T18:47:44.000Z
chatbotDeprioritize: false
tags: Full stack,Nuxt
source_url:
  html: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/nuxt/
  md: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/nuxt/index.md
---

In this guide, you will create a new [Nuxt](https://nuxt.com/) application and deploy to Cloudflare Workers (with the new [Workers Assets](https://developers.cloudflare.com/workers/static-assets/)).

## 1. Set up a new project

Use the [`create-cloudflare`](https://www.npmjs.com/package/create-cloudflare) CLI (C3) to set up a new project. C3 will create a new project directory, initiate Nuxt's official setup tool, and provide the option to deploy instantly.

To use `create-cloudflare` to create a new Nuxt project with Workers Assets, run the following command:

* npm

  ```sh
  npm create cloudflare@latest -- my-nuxt-app --framework=nuxt
  ```

* yarn

  ```sh
  yarn create cloudflare my-nuxt-app --framework=nuxt
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest my-nuxt-app --framework=nuxt
  ```

After setting up your project, change your directory by running the following command:

```sh
cd my-nuxt-app
```

## 2. Develop locally

After you have created your project, run the following command in the project directory to start a local server. This will allow you to preview your project locally during development.

* npm

  ```sh
  npm run dev
  ```

* yarn

  ```sh
  yarn run dev
  ```

* pnpm

  ```sh
  pnpm run dev
  ```

## 3. Deploy your Project

Your project can be deployed to a `*.workers.dev` subdomain or a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), from your own machine or from any CI/CD system, including [Cloudflare's own](https://developers.cloudflare.com/workers/ci-cd/builds/).

The following command will build and deploy your project. If you're using CI, ensure you update your ["deploy command"](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings) configuration appropriately.

* npm

  ```sh
  npm run deploy
  ```

* yarn

  ```sh
  yarn run deploy
  ```

* pnpm

  ```sh
  pnpm run deploy
  ```

***

## Bindings

Your Nuxt application can be fully integrated with the Cloudflare Developer Platform, in both local development and in production, by using product bindings. The [Nuxt documentation](https://nitro.unjs.io/deploy/providers/cloudflare#direct-access-to-cloudflare-bindings) provides information about configuring bindings and how you can access them in your Nuxt event handlers.

With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.

[Bindings ](https://developers.cloudflare.com/workers/runtime-apis/bindings/)Access to compute, storage, AI and more.