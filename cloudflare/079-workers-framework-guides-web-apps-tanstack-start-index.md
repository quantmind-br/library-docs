---
title: TanStack Start
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/index.md
source: llms
fetched_at: 2026-01-24T15:28:57.068015586-03:00
rendered_js: false
word_count: 407
summary: This guide provides instructions for creating, configuring, and deploying TanStack Start applications on Cloudflare Workers, including integration with Cloudflare bindings and static prerendering.
tags:
    - tanstack-start
    - cloudflare-workers
    - full-stack
    - deployment
    - vite-plugin
    - server-side-rendering
category: guide
---

---
title: TanStack Start · Cloudflare Workers docs
description: Deploy a TanStack Start application to Cloudflare Workers.
lastUpdated: 2026-01-22T13:27:40.000Z
chatbotDeprioritize: false
tags: Full stack
source_url:
  html: https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/
  md: https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/index.md
---

[TanStack Start](https://tanstack.com/start) is a full-stack framework for building web applications with server-side rendering, streaming, server functions, and bundling.

## Create a new application

Create a TanStack Start application pre-configured for Cloudflare Workers:

* npm

  ```sh
  npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start
  ```

* yarn

  ```sh
  yarn create cloudflare my-tanstack-start-app --framework=tanstack-start
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start
  ```

Start a local development server to preview your project during development:

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

## Configure an existing application

If you have an existing TanStack Start application, configure it to run on Cloudflare Workers:

1. Install `@cloudflare/vite-plugin` and `wrangler`:

   * npm

     ```sh
     npm i @cloudflare/vite-plugin wrangler -- -D
     ```

   * yarn

     ```sh
     yarn add @cloudflare/vite-plugin wrangler -D
     ```

   * pnpm

     ```sh
     pnpm add @cloudflare/vite-plugin wrangler -D
     ```

2. Add the Cloudflare plugin to your Vite configuration:

   * JavaScript

     ```js
     import { defineConfig } from "vite";
     import { tanstackStart } from "@tanstack/react-start/plugin/vite";
     import { cloudflare } from "@cloudflare/vite-plugin";
     import react from "@vitejs/plugin-react";


     export default defineConfig({
       plugins: [
         cloudflare({ viteEnvironment: { name: "ssr" } }),
         tanstackStart(),
         react(),
       ],
     });
     ```

   * TypeScript

     ```ts
     import { defineConfig } from "vite";
     import { tanstackStart } from "@tanstack/react-start/plugin/vite";
     import { cloudflare } from "@cloudflare/vite-plugin";
     import react from "@vitejs/plugin-react";


     export default defineConfig({
       plugins: [
         cloudflare({ viteEnvironment: { name: "ssr" } }),
         tanstackStart(),
         react(),
       ],
     });
     ```

3. Add a `wrangler.jsonc` configuration file:

   * wrangler.jsonc

     ```jsonc
     {
       "$schema": "node_modules/wrangler/config-schema.json",
       "name": "<YOUR_PROJECT_NAME>",
       "compatibility_date": "2025-01-01",
       "compatibility_flags": ["nodejs_compat"],
       "main": "@tanstack/react-start/server-entry",
       "observability": {
         "enabled": true,
       },
     }
     ```

   * wrangler.toml

     ```toml
     "$schema" = "node_modules/wrangler/config-schema.json"
     name = "<YOUR_PROJECT_NAME>"
     compatibility_date = "2025-01-01"
     compatibility_flags = [ "nodejs_compat" ]
     main = "@tanstack/react-start/server-entry"


     [observability]
     enabled = true
     ```

4. Update the `scripts` section in `package.json`:

   ```json
   {
     "scripts": {
       "dev": "vite dev",
       "build": "vite build",
       "preview": "vite preview",
       "deploy": "npm run build && wrangler deploy",
       "cf-typegen": "wrangler types"
     }
   }
   ```

## Deploy

Deploy to a `*.workers.dev` subdomain or a [custom domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) from your machine or any CI/CD system, including [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/).

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

Note

Preview the build locally before deploying:

* npm

  ```sh
  npm run preview
  ```

* yarn

  ```sh
  yarn run preview
  ```

* pnpm

  ```sh
  pnpm run preview
  ```

## Bindings

Your TanStack Start application can be fully integrated with the Cloudflare Developer Platform, in both local development and in production, by using [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/).

Access bindings by [importing the `env` object](https://developers.cloudflare.com/workers/runtime-apis/bindings/#importing-env-as-a-global) in your server-side code:

* JavaScript

  ```js
  import { createFileRoute } from "@tanstack/react-router";
  import { createServerFn } from "@tanstack/react-start";
  import { env } from "cloudflare:workers";


  export const Route = createFileRoute("/")({
    loader: () => getData(),
    component: RouteComponent,
  });


  const getData = createServerFn().handler(() => {
    // Access bindings via env
    // For example: env.MY_KV, env.MY_BUCKET, env.AI, etc.
  });


  function RouteComponent() {
    // ...
  }
  ```

* TypeScript

  ```ts
  import { createFileRoute } from "@tanstack/react-router";
  import { createServerFn } from "@tanstack/react-start";
  import { env } from "cloudflare:workers";


  export const Route = createFileRoute("/")({
    loader: () => getData(),
    component: RouteComponent,
  });


  const getData = createServerFn().handler(() => {
    // Access bindings via env
    // For example: env.MY_KV, env.MY_BUCKET, env.AI, etc.
  });


  function RouteComponent() {
    // ...
  }
  ```

Generate TypeScript types for your bindings based on your Wrangler configuration:

* npm

  ```sh
  npm run cf-typegen
  ```

* yarn

  ```sh
  yarn run cf-typegen
  ```

* pnpm

  ```sh
  pnpm run cf-typegen
  ```

With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.

[Bindings ](https://developers.cloudflare.com/workers/runtime-apis/bindings/)Access to compute, storage, AI and more.

### Use R2 in a server function

Add an [R2 bucket binding](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/#4-bind-your-bucket-to-a-worker) to your Wrangler configuration:

* wrangler.jsonc

  ```jsonc
  {
    "r2_buckets": [
      {
        "binding": "MY_BUCKET",
        "bucket_name": "<YOUR_BUCKET_NAME>",
      },
    ],
  }
  ```

* wrangler.toml

  ```toml
  [[r2_buckets]]
  binding = "MY_BUCKET"
  bucket_name = "<YOUR_BUCKET_NAME>"
  ```

Access the bucket in a server function:

* JavaScript

  ```js
  import { createServerFn } from "@tanstack/react-start";
  import { env } from "cloudflare:workers";


  const uploadFile = createServerFn({ method: "POST" })
    .validator((data) => data)
    .handler(async ({ data }) => {
      await env.MY_BUCKET.put(data.key, data.content);
      return { success: true };
    });


  const getFile = createServerFn()
    .validator((key) => key)
    .handler(async ({ data: key }) => {
      const object = await env.MY_BUCKET.get(key);
      return object ? await object.text() : null;
    });
  ```

* TypeScript

  ```ts
  import { createServerFn } from "@tanstack/react-start";
  import { env } from "cloudflare:workers";


  const uploadFile = createServerFn({ method: "POST" })
    .validator((data: { key: string; content: string }) => data)
    .handler(async ({ data }) => {
      await env.MY_BUCKET.put(data.key, data.content);
      return { success: true };
    });


  const getFile = createServerFn()
    .validator((key: string) => key)
    .handler(async ({ data: key }) => {
      const object = await env.MY_BUCKET.get(key);
      return object ? await object.text() : null;
    });
  ```

## Static prerendering

Prerender your application to static HTML at build time and serve as [static assets](https://developers.cloudflare.com/workers/static-assets/).

* JavaScript

  ```js
  import { defineConfig } from "vite";
  import { cloudflare } from "@cloudflare/vite-plugin";
  import { tanstackStart } from "@tanstack/react-start/plugin/vite";
  import react from "@vitejs/plugin-react";


  export default defineConfig({
    plugins: [
      cloudflare({ viteEnvironment: { name: "ssr" } }),
      tanstackStart({
        prerender: {
          enabled: true,
        },
      }),
      react(),
    ],
  });
  ```

* TypeScript

  ```ts
  import { defineConfig } from "vite";
  import { cloudflare } from "@cloudflare/vite-plugin";
  import { tanstackStart } from "@tanstack/react-start/plugin/vite";
  import react from "@vitejs/plugin-react";


  export default defineConfig({
    plugins: [
      cloudflare({ viteEnvironment: { name: "ssr" } }),
      tanstackStart({
        prerender: {
          enabled: true,
        },
      }),
      react(),
    ],
  });
  ```

For more options, refer to [TanStack Start static prerendering](https://tanstack.com/start/latest/docs/framework/react/guide/static-prerendering).

Note

Requires `@tanstack/react-start` v1.138.0 or later.

Warning

Prerendering runs during build and uses local environment variables, secrets, and bindings storage data. Use [remote bindings](https://developers.cloudflare.com/workers/development-testing/#remote-bindings) to prerender with production data.

### Prerender in CI environments

When prerendering in CI, your Worker code may need environment variables or secrets not available in the build environment. Include a `.env` file with variable references that resolve to values from your CI environment:

```sh
API_KEY=${API_KEY}
DATABASE_URL=${DATABASE_URL}
```

Set `CLOUDFLARE_INCLUDE_PROCESS_ENV=true` in your CI environment and provide the required values as environment variables. If using [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), update your [build settings](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings).

Note

For local development, create a `.env.local` file with actual values. Do not commit this file to your repository. Values in `.env.local` override references in `.env`:

```sh
API_KEY=my-local-dev-key
DATABASE_URL=postgres://localhost/mydb
```