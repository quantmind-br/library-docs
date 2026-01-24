---
title: RedwoodSDK
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/redwoodsdk/index.md
source: llms
fetched_at: 2026-01-24T15:28:56.042202428-03:00
rendered_js: false
word_count: 330
summary: This guide provides step-by-step instructions for creating, developing locally, and deploying a RedwoodSDK application to Cloudflare Workers using Vite and React Server Components.
tags:
    - redwoodsdk
    - cloudflare-workers
    - full-stack
    - react-server-components
    - server-side-rendering
    - vite-plugin
    - deployment
category: tutorial
---

---
title: RedwoodSDK · Cloudflare Workers docs
description: Create a RedwoodSDK application and deploy it to Cloudflare Workers.
lastUpdated: 2026-01-20T19:08:43.000Z
chatbotDeprioritize: false
tags: Full stack
source_url:
  html: https://developers.cloudflare.com/workers/framework-guides/web-apps/redwoodsdk/
  md: https://developers.cloudflare.com/workers/framework-guides/web-apps/redwoodsdk/index.md
---

In this guide, you will create a new [RedwoodSDK](https://rwsdk.com/) application and deploy it to Cloudflare Workers.

RedwoodSDK is a framework for building server-side web applications on Cloudflare. It is a Vite plugin that provides SSR, React Server Components, Server Functions, and realtime capabilities.

## Deploy a new RedwoodSDK application on Workers

1. **Create a new project.**

   Run the following command, replacing `my-project-name` with your desired project name:

   * npm

     ```sh
     npx create-rwsdk my-project-name
     ```

   * yarn

     ```sh
     yarn dlx create-rwsdk my-project-name
     ```

   * pnpm

     ```sh
     pnpx create-rwsdk my-project-name
     ```

2. **Change the directory.**

   ```sh
   cd my-project-name
   ```

3. **Install dependencies.**

   * npm

     ```sh
     npm install
     ```

   * yarn

     ```sh
     yarn install
     ```

   * pnpm

     ```sh
     pnpm install
     ```

4. **Develop locally.**

   Run the following command in the project directory to start a local development server. RedwoodSDK is a Vite plugin, so you can use the same development workflow as any other Vite project:

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

   Access the development server in your browser at `http://localhost:5173`, where you should see "Hello, World!" displayed on the page.

5. **Add your first route.**

   The entry point of your application is `src/worker.tsx`. Open that file in your editor.

   You will see the `defineApp` function, which handles requests by returning responses to the client:

   ```tsx
   import { defineApp } from "rwsdk/worker";
   import { route, render } from "rwsdk/router";


   import { Document } from "@/app/Document";
   import { Home } from "@/app/pages/Home";


   export default defineApp([
     render(Document, [route("/", () => new Response("Hello, World!"))]),
   ]);
   ```

   Add a `/ping` route handler:

   ```tsx
   import { defineApp } from "rwsdk/worker";
   import { route, render } from "rwsdk/router";


   export default defineApp([
     render(Document, [
       route("/", () => new Response("Hello, World!")),
       route("/ping", function () {
         return <h1>Pong!</h1>;
       }),
     ]),
   ]);
   ```

   Navigate to `http://localhost:5173/ping` to see "Pong!" displayed on the page.

   Routes can return JSX directly. RedwoodSDK has support for React Server Components, which renders JSX on the server and sends HTML to the client.

6. **Deploy your project.**

   You can deploy your project to a `*.workers.dev` subdomain or a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), either from your local machine or from any CI/CD system, including [Cloudflare Workers CI/CD](https://developers.cloudflare.com/workers/ci-cd/builds/).

   Use the following command to build and deploy. If you are using CI, make sure to update your [deploy command](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings) configuration accordingly.

   * npm

     ```sh
     npm run release
     ```

   * yarn

     ```sh
     yarn run release
     ```

   * pnpm

     ```sh
     pnpm run release
     ```

   The first time you run the command it might fail and ask you to create a workers.dev subdomain. Go to the dashboard and open the Workers menu. Opening the Workers landing page for the first time will create a workers.dev subdomain automatically.