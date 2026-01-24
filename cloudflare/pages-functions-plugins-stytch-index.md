---
title: Stytch · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/plugins/stytch/index.md
source: llms
fetched_at: 2026-01-24T15:18:57.719487529-03:00
rendered_js: false
word_count: 157
summary: Documentation guide for integrating Stytch authentication services with applications hosted on Cloudflare Pages.
tags:
    - Cloudflare Pages
    - Stytch
    - authentication
    - web development
category: guide
---

The Stytch Pages Plugin is a middleware which validates all requests and their `session_token`.

## Installation

* npm

  ```sh
  npm i @cloudflare/pages-plugin-stytch
  ```

* yarn

  ```sh
  yarn add @cloudflare/pages-plugin-stytch
  ```

* pnpm

  ```sh
  pnpm add @cloudflare/pages-plugin-stytch
  ```

## Usage

```typescript
import stytchPlugin from "@cloudflare/pages-plugin-stytch";
import { envs } from "@cloudflare/pages-plugin-stytch/api";


export const onRequest: PagesFunction = stytchPlugin({
  project_id: "YOUR_STYTCH_PROJECT_ID",
  secret: "YOUR_STYTCH_PROJECT_SECRET",
  env: envs.live,
});
```

We recommend storing your secret in KV rather than in plain text as above.

The Stytch Plugin takes a single argument, an object with several properties. `project_id` and `secret` are mandatory strings and can be found in [Stytch's dashboard](https://stytch.com/dashboard/api-keys). `env` is also a mandatory string, and can be populated with the `envs.test` or `envs.live` variables in the API. By default, the Plugin validates a `session_token` cookie of the incoming request, but you can also optionally pass in a `session_token` or `session_jwt` string yourself if you are using some other mechanism to identify user sessions. Finally, you can also pass in a `session_duration_minutes` in order to extend the lifetime of the session. More information on these parameters can be found in [Stytch's documentation](https://stytch.com/docs/api/session-auth).

The validated session response containing user information is made available to subsequent Pages Functions on `data.stytch.session`.