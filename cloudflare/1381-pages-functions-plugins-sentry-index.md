---
title: Sentry · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/plugins/sentry/index.md
source: llms
fetched_at: 2026-01-24T15:18:55.81358484-03:00
rendered_js: false
word_count: 170
summary: Explains how to integrate, configure, and use the Sentry Pages Plugin to capture and log exceptions in Cloudflare Pages Functions.
tags:
    - cloudflare-pages
    - sentry
    - error-logging
    - middleware
    - exception-handling
    - javascript-plugin
category: guide
---

Note

Sentry now provides official support for Cloudflare Workers and Pages. Refer to the [Sentry documentation](https://docs.sentry.io/platforms/javascript/guides/cloudflare/) for more details.

The Sentry Pages Plugin captures and logs all exceptions which occur below it in the execution chain of your Pages Functions. It is therefore recommended that you install this Plugin at the root of your application in `functions/_middleware.ts` as the very first Plugin.

## Installation

* npm

  ```sh
  npm i @cloudflare/pages-plugin-sentry
  ```

* yarn

  ```sh
  yarn add @cloudflare/pages-plugin-sentry
  ```

* pnpm

  ```sh
  pnpm add @cloudflare/pages-plugin-sentry
  ```

## Usage

```typescript
import sentryPlugin from "@cloudflare/pages-plugin-sentry";


export const onRequest: PagesFunction = sentryPlugin({
  dsn: "https://sentry.io/welcome/xyz",
});
```

The Plugin uses [Toucan](https://github.com/robertcepa/toucan-js). Refer to the Toucan README to [review the options it can take](https://github.com/robertcepa/toucan-js#other-options). `context`, `request`, and `event` are automatically populated and should not be manually configured.

If your [DSN](https://docs.sentry.io/product/sentry-basics/dsn-explainer/) is held as an environment variable or in KV, you can access it like so:

```typescript
import sentryPlugin from "@cloudflare/pages-plugin-sentry";


export const onRequest: PagesFunction<{
  SENTRY_DSN: string;
}> = (context) => {
  return sentryPlugin({ dsn: context.env.SENTRY_DSN })(context);
};
```

```typescript
import sentryPlugin from "@cloudflare/pages-plugin-sentry";


export const onRequest: PagesFunction<{
  KV: KVNamespace;
}> = async (context) => {
  return sentryPlugin({ dsn: await context.env.KV.get("SENTRY_DSN") })(context);
};
```

### Additional context

If you need to set additional context for Sentry (for example, user information or additional logs), use the `data.sentry` instance in any Function below the Plugin in the execution chain.

For example, you can access `data.sentry` and set user information like so:

```typescript
import type { PluginData } from "@cloudflare/pages-plugin-sentry";


export const onRequest: PagesFunction<unknown, any, PluginData> = async ({
  data,
  next,
}) => {
  // Authenticate the user from the request and extract user's email address
  const email = await getEmailFromRequest(request);


  data.sentry.setUser({ email });


  return next();
};
```

Again, the full list of features can be found in [Toucan's documentation](https://github.com/robertcepa/toucan-js#features).