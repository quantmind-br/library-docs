---
title: Analog
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/index.md
source: llms
fetched_at: 2026-01-24T15:31:29.065443654-03:00
rendered_js: false
word_count: 280
summary: This guide provides instructions for creating, developing locally, and deploying a full-stack Analog application to Cloudflare Workers using the create-cloudflare CLI.
tags:
    - analog
    - angular
    - cloudflare-workers
    - deployment
    - meta-framework
    - nitro-engine
    - web-development
category: guide
---

---
title: Analog · Cloudflare Workers docs
description: Create an Analog application and deploy it to Cloudflare Workers.
lastUpdated: 2026-01-08T11:26:09.000Z
chatbotDeprioritize: false
tags: Full stack,Angular
source_url:
  html: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/
  md: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/index.md
---

In this guide, you will create a new [Analog](https://analogjs.org/) application and deploy to Cloudflare Workers.

[Analog](https://analogjs.org/) is a fullstack meta-framework for Angular, powered by [Vite](https://vitejs.dev/) and [Nitro](https://nitro.unjs.io/).

## 1. Set up a new project

Use the [`create-cloudflare`](https://www.npmjs.com/package/create-cloudflare) CLI (C3) to set up a new project. C3 will create a new project directory, initiate Analog's official setup tool, and provide the option to deploy instantly.

To use `create-cloudflare` to create a new Analog project, run the following command:

* npm

  ```sh
  npm create cloudflare@latest -- my-analog-app --framework=analog
  ```

* yarn

  ```sh
  yarn create cloudflare my-analog-app --framework=analog
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest my-analog-app --framework=analog
  ```

After setting up your project, change your directory by running the following command:

```sh
cd my-analog-app
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

Your Analog application can be fully integrated with the Cloudflare Developer Platform, in both local development and in production, by using product bindings. The [Nitro documentation](https://nitro.unjs.io/deploy/providers/cloudflare#direct-access-to-cloudflare-bindings) provides information about configuring bindings and how you can access them in your Analog API routes.

With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.

[Bindings ](https://developers.cloudflare.com/workers/runtime-apis/bindings/)Access to compute, storage, AI and more.