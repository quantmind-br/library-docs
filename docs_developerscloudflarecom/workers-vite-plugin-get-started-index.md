---
title: Get started · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/vite-plugin/get-started/index.md
source: llms
fetched_at: 2026-01-24T15:27:21.999833079-03:00
rendered_js: false
word_count: 231
summary: This guide provides instructions for setting up a standalone Cloudflare Worker from scratch using the Vite plugin and Wrangler for development and deployment.
tags:
    - cloudflare-workers
    - vite
    - wrangler
    - serverless
    - deployment
    - javascript-modules
category: tutorial
---

Note

This guide demonstrates creating a standalone Worker from scratch. If you would instead like to create a new application from a ready-to-go template, refer to the [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/), [React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/), [React](https://developers.cloudflare.com/workers/framework-guides/web-apps/react/) or [Vue](https://developers.cloudflare.com/workers/framework-guides/web-apps/vue/) framework guides.

## Start with a basic `package.json`

```json
{
  "name": "cloudflare-vite-get-started",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite dev",
    "build": "vite build",
    "preview": "npm run build && vite preview",
    "deploy": "npm run build && wrangler deploy"
  }
}
```

Note

Ensure that you include `"type": "module"` in order to use ES modules by default.

## Install the dependencies

* npm

  ```sh
  npm i -D vite @cloudflare/vite-plugin wrangler
  ```

* yarn

  ```sh
  yarn add -D vite @cloudflare/vite-plugin wrangler
  ```

* pnpm

  ```sh
  pnpm add -D vite @cloudflare/vite-plugin wrangler
  ```

## Create your Vite config file and include the Cloudflare plugin

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";


export default defineConfig({
  plugins: [cloudflare()],
});
```

The Cloudflare Vite plugin doesn't require any configuration by default and will look for a `wrangler.jsonc`, `wrangler.json` or `wrangler.toml` in the root of your application.

Refer to the [API reference](https://developers.cloudflare.com/workers/vite-plugin/reference/api/) for configuration options.

## Create your Worker config file

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "cloudflare-vite-get-started",
    "compatibility_date": "2025-04-03",
    "main": "./src/index.ts"
  }
  ```

* wrangler.toml

  ```toml
  name = "cloudflare-vite-get-started"
  compatibility_date = "2025-04-03"
  main = "./src/index.ts"
  ```

The `name` field specifies the name of your Worker. By default, this is also used as the name of the Worker's Vite Environment (see [Vite Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/) for more information). The `main` field specifies the entry file for your Worker code.

For more information about the Worker configuration, see [Configuration](https://developers.cloudflare.com/workers/wrangler/configuration/).

## Create your Worker entry file

```ts
export default {
  fetch() {
    return new Response(`Running in ${navigator.userAgent}!`);
  },
};
```

A request to this Worker will return **'Running in Cloudflare-Workers!'**, demonstrating that the code is running inside the Workers runtime.

## Dev, build, preview and deploy

You can now start the Vite development server (`npm run dev`), build the application (`npm run build`), preview the built application (`npm run preview`), and deploy to Cloudflare (`npm run deploy`).