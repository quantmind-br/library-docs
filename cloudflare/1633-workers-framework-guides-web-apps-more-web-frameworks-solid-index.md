---
title: Solid
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/solid/index.md
source: llms
fetched_at: 2026-01-24T15:31:38.253592453-03:00
rendered_js: false
word_count: 295
summary: This guide provides instructions on how to create, develop, and deploy a Solid application to Cloudflare Workers using the create-cloudflare CLI and Workers Assets.
tags:
    - solidjs
    - cloudflare-workers
    - workers-assets
    - deployment
    - web-frameworks
    - full-stack
category: tutorial
---

---
title: Solid · Cloudflare Workers docs
description: Create a Solid application and deploy it to Cloudflare Workers with
  Workers Assets.
lastUpdated: 2025-08-20T18:47:44.000Z
chatbotDeprioritize: false
tags: Full stack
source_url:
  html: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/solid/
  md: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/solid/index.md
---

Note

Support for SolidStart projects on Cloudflare Workers is currently in beta.

In this guide, you will create a new [Solid](https://www.solidjs.com/) application and deploy to Cloudflare Workers (with the new [Workers Assets](https://developers.cloudflare.com/workers/static-assets/)).

## 1. Set up a new project

Use the [`create-cloudflare`](https://www.npmjs.com/package/create-cloudflare) CLI (C3) to set up a new project. C3 will create a new project directory, initiate Solid's official setup tool, and provide the option to deploy instantly.

To use `create-cloudflare` to create a new Solid project with Workers Assets, run the following command:

* npm

  ```sh
  npm create cloudflare@latest -- my-solid-app --framework=solid --experimental
  ```

* yarn

  ```sh
  yarn create cloudflare my-solid-app --framework=solid --experimental
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest my-solid-app --framework=solid --experimental
  ```

After setting up your project, change your directory by running the following command:

```sh
cd my-solid-app
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

Your Solid application can be fully integrated with the Cloudflare Developer Platform, in both local development and in production, by using product bindings. The [Solid documentation](https://docs.solidjs.com/reference/server-utilities/get-request-event) provides information about how to access platform primitives, including bindings. Specifically, for Cloudflare, you can use [`getRequestEvent().nativeEvent.context.cloudflare.env`](https://docs.solidjs.com/solid-start/advanced/request-events#nativeevent) to access bindings.

With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.

[Bindings ](https://developers.cloudflare.com/workers/runtime-apis/bindings/)Access to compute, storage, AI and more.