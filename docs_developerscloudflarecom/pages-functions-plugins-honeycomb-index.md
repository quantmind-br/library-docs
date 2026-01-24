---
title: Honeycomb · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/plugins/honeycomb/index.md
source: llms
fetched_at: 2026-01-24T15:18:52.846108642-03:00
rendered_js: false
word_count: 168
summary: This document explains how to install and configure the Honeycomb Pages Plugin for Cloudflare Pages to automatically send traces for analysis and observability.
tags:
    - cloudflare-pages
    - honeycomb
    - observability
    - tracing
    - telemetry
    - plugin-integration
category: guide
---

The Honeycomb Pages Plugin automatically sends traces to Honeycomb for analysis and observability.

## Installation

* npm

  ```sh
  npm i @cloudflare/pages-plugin-honeycomb
  ```

* yarn

  ```sh
  yarn add @cloudflare/pages-plugin-honeycomb
  ```

* pnpm

  ```sh
  pnpm add @cloudflare/pages-plugin-honeycomb
  ```

## Usage

The following usage example uses environment variables you will need to set in your Pages project settings.

```typescript
import honeycombPlugin from "@cloudflare/pages-plugin-honeycomb";


export const onRequest: PagesFunction<{
  HONEYCOMB_API_KEY: string;
  HONEYCOMB_DATASET: string;
}> = (context) => {
  return honeycombPlugin({
    apiKey: context.env.HONEYCOMB_API_KEY,
    dataset: context.env.HONEYCOMB_DATASET,
  })(context);
};
```

Alternatively, you can hard-code (not advisable for API key) your settings the following way:

```typescript
import honeycombPlugin from "@cloudflare/pages-plugin-honeycomb";


export const onRequest = honeycombPlugin({
  apiKey: "YOUR_HONEYCOMB_API_KEY",
  dataset: "YOUR_HONEYCOMB_DATASET_NAME",
});
```

This Plugin is based on the `@cloudflare/workers-honeycomb-logger` and accepts the same [configuration options](https://github.com/cloudflare/workers-honeycomb-logger#config).

Ensure that you enable the option to **Automatically unpack nested JSON** and set the **Maximum unpacking depth** to **5** in your Honeycomb dataset settings.

![Follow the instructions above to toggle on Automatically unpack nested JSON and set the Maximum unpacking depth option to 5 in the Honeycomb dashboard](https://developers.cloudflare.com/_astro/honeycomb.MQ2Vf1tC_2kKhNs.webp)

### Additional context

`data.honeycomb.tracer` has two methods for attaching additional information about a given trace:

* `data.honeycomb.tracer.log` which takes a single argument, a `String`.
* `data.honeycomb.tracer.addData` which takes a single argument, an object of arbitrary data.

More information about these methods can be seen on [`@cloudflare/workers-honeycomb-logger`'s documentation](https://github.com/cloudflare/workers-honeycomb-logger#adding-logs-and-other-data).

For example, if you wanted to use the `addData` method to attach user information:

```typescript
import type { PluginData } from "@cloudflare/pages-plugin-honeycomb";


export const onRequest: PagesFunction<unknown, any, PluginData> = async ({
  data,
  next,
  request,
}) => {
  // Authenticate the user from the request and extract user's email address
  const email = await getEmailFromRequest(request);


  data.honeycomb.tracer.addData({ email });


  return next();
};
```