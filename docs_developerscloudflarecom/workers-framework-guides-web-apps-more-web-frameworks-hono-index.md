---
title: Hono
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/index.md
source: llms
fetched_at: 2026-01-24T15:31:32.850933216-03:00
rendered_js: false
word_count: 479
summary: This document provides instructions for creating, developing, and deploying a full-stack web application using the Hono framework, React, and Vite on Cloudflare Workers.
tags:
    - hono
    - cloudflare-workers
    - react
    - vite
    - full-stack
    - workers-assets
    - deployment
category: guide
---

---
title: Hono · Cloudflare Workers docs
description: Create a Hono application and deploy it to Cloudflare Workers with
  Workers Assets.
lastUpdated: 2025-08-20T18:47:44.000Z
chatbotDeprioritize: false
tags: Hono
source_url:
  html: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/
  md: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/index.md
---

**Start from CLI** - scaffold a full-stack app with a Hono API, React SPA and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) for lightning-fast development.

* npm

  ```sh
  npm create cloudflare@latest -- my-hono-app --template=cloudflare/templates/vite-react-template
  ```

* yarn

  ```sh
  yarn create cloudflare my-hono-app --template=cloudflare/templates/vite-react-template
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest my-hono-app --template=cloudflare/templates/vite-react-template
  ```

***

**Or just deploy** - create a full-stack app using Hono, React and Vite, with CI/CD and previews all set up for you.

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://dash.cloudflare.com/?to=/:account/workers-and-pages/create/deploy-to-workers\&repository=https://github.com/cloudflare/templates/tree/main/vite-react-template)

## What is Hono?

[Hono](https://hono.dev/) is an ultra-fast, lightweight framework for building web applications, and works fantastically with Cloudflare Workers. With Workers Assets, you can easily combine a Hono API running on Workers with a SPA to create a full-stack app.

## Creating a full-stack Hono app with a React SPA

1. **Create a new project with the create-cloudflare CLI (C3)**

   * npm

     ```sh
     npm create cloudflare@latest -- my-hono-app --template=cloudflare/templates/vite-react-template
     ```

   * yarn

     ```sh
     yarn create cloudflare my-hono-app --template=cloudflare/templates/vite-react-template
     ```

   * pnpm

     ```sh
     pnpm create cloudflare@latest my-hono-app --template=cloudflare/templates/vite-react-template
     ```

   How is this project set up?

   Below is a simplified file tree of the project.

   `wrangler.jsonc` is your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). In this file:

   * `main` points to `src/worker/index.ts`. This is your Hono app, which will run in a Worker.
   * `assets.not_found_handling` is set to `single-page-application`, which means that routes that are handled by your SPA do not go to the Worker, and are thus free.
   * If you want to add bindings to resources on Cloudflare's developer platform, you configure them here. Read more about [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/).

   `vite.config.ts` is set up to use the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). This runs your Worker in the Cloudflare Workers runtime, ensuring your local development environment is as close to production as possible.

   `src/worker/index.ts` is your Hono app, which contains a single endpoint to begin with, `/api`. At `src/react-app/src/App.tsx`, your React app calls this endpoint to get a message back and displays this in your SPA.

2. **Develop locally with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/)**

   After creating your project, run the following command in your project directory to start a local development server.

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

   What's happening in local development?

   This project uses Vite for local development and build, and thus comes with all of Vite's features, including hot module replacement (HMR).

   In addition, `vite.config.ts` is set up to use the Cloudflare Vite plugin. This runs your application in the Cloudflare Workers runtime, just like in production, and enables access to local emulations of bindings.

3. **Deploy your project**

   Your project can be deployed to a `*.workers.dev` subdomain or a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), from your own machine or from any CI/CD system, including Cloudflare's own [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/).

   The following command will build and deploy your project. If you are using CI, ensure you update your ["deploy command"](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings) configuration appropriately.

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

The [Hono documentation](https://hono.dev/docs/getting-started/cloudflare-workers#bindings) provides information on how you can access bindings in your Hono app.

With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.

[Bindings ](https://developers.cloudflare.com/workers/runtime-apis/bindings/)Access to compute, storage, AI and more.