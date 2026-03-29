---
title: API · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/vite-plugin/reference/api/index.md
source: llms
fetched_at: 2026-01-24T15:31:13.465707207-03:00
rendered_js: false
word_count: 451
summary: This document provides a technical reference for the Cloudflare Vite plugin configuration, detailing parameters for Worker setup, environment customization, and auxiliary Worker integration.
tags:
    - cloudflare-workers
    - vite-plugin
    - configuration
    - wrangler
    - worker-config
    - auxiliary-workers
category: reference
---

## `cloudflare()`

The `cloudflare` plugin should be included in the Vite `plugins` array:

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";


export default defineConfig({
  plugins: [cloudflare()],
});
```

It accepts an optional `PluginConfig` parameter.

## `interface PluginConfig`

* `configPath` string optional

  An optional path to your Worker config file. By default, a `wrangler.jsonc`, `wrangler.json`, or `wrangler.toml` file in the root of your application will be used as the Worker config.

  For more information about the Worker configuration, see [Configuration](https://developers.cloudflare.com/workers/wrangler/configuration/).

* `config` WorkerConfigCustomizer\<true> optional

  Customize or override Worker configuration programmatically. Accepts a partial configuration object or a function that receives the current config.

  Applied after any config file loads. Use it to override values, modify the existing config, or define Workers entirely in code.

  See [Programmatic configuration](https://developers.cloudflare.com/workers/vite-plugin/reference/programmatic-configuration/) for details.

* `viteEnvironment` { name?: string } optional

  Optional Vite environment options. By default, the environment name is the Worker name with `-` characters replaced with `_`. Setting the name here will override this. A typical use case is setting `viteEnvironment: { name: "ssr" }` to apply the Worker to the SSR environment.

  See [Vite Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/) for more information.

* `persistState` boolean | { path: string } optional

  An optional override for state persistence. By default, state is persisted to `.wrangler/state`. A custom `path` can be provided or, alternatively, persistence can be disabled by setting the value to `false`.

* `inspectorPort` number | false optional

  An optional override for debugging your Workers. By default, the debugging inspector is enabled and listens on port `9229`. A custom port can be provided or, alternatively, setting this to `false` will disable the debugging inspector.

  See [Debugging](https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/) for more information.

* `auxiliaryWorkers` Array\<AuxiliaryWorkerConfig> optional

  An optional array of auxiliary Workers. Auxiliary Workers are additional Workers that are used as part of your application. You can use [service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) to call auxiliary Workers from your main (entry) Worker. All requests are routed through your entry Worker. During the build, each Worker is output to a separate subdirectory of `dist`.

  Note

  When running `wrangler deploy`, only your main (entry) Worker will be deployed. If using multiple Workers, each auxiliary Worker must be deployed individually. You can inspect the `dist` directory and then run `wrangler deploy -c dist/<auxiliary-worker>/wrangler.json` for each.

## `interface AuxiliaryWorkerConfig`

Auxiliary Workers require a `configPath`, a `config` option, or both.

* `configPath` string optional

  The path to your Worker config file. This field is required unless `config` is provided.

  For more information about the Worker configuration, see [Configuration](https://developers.cloudflare.com/workers/wrangler/configuration/).

* `config` WorkerConfigCustomizer\<false> optional

  Customize or override Worker configuration programmatically. When used without `configPath`, this allows defining auxiliary Workers entirely in code.

  See [Programmatic configuration](https://developers.cloudflare.com/workers/vite-plugin/reference/programmatic-configuration/) for usage examples.

* `viteEnvironment` { name?: string } optional

  Optional Vite environment options. By default, the environment name is the Worker name with `-` characters replaced with `_`. Setting the name here will override this.

  See [Vite Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/) for more information.