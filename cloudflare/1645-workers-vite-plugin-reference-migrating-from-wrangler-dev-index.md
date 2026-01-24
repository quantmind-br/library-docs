---
title: Migrating from wrangler dev · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/vite-plugin/reference/migrating-from-wrangler-dev/index.md
source: llms
fetched_at: 2026-01-24T15:31:19.939398977-03:00
rendered_js: false
word_count: 308
summary: This document outlines the key differences and configuration adjustments needed when migrating from wrangler dev to the Cloudflare Vite plugin, including environment handling and configuration file changes.
tags:
    - cloudflare-workers
    - vite-plugin
    - migration-guide
    - wrangler-configuration
    - deployment
    - development-tools
category: guide
---

In most cases, migrating from [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/#dev) is straightforward and you can follow the instructions in [Get started](https://developers.cloudflare.com/workers/vite-plugin/get-started/). There are a few key differences to highlight:

## Input and output Worker config files

With the Cloudflare Vite plugin, your [Worker config file](https://developers.cloudflare.com/workers/wrangler/configuration/) (for example, `wrangler.jsonc`) is the input configuration and a separate output configuration is created as part of the build. This output file is a snapshot of your configuration at the time of the build and is modified to reference your build artifacts. It is the configuration that is used for preview and deployment. Once you have run `vite build`, running `wrangler deploy` or `vite preview` will automatically locate this output configuration file.

## Cloudflare Environments

With the Cloudflare Vite plugin, [Cloudflare Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/cloudflare-environments/) are applied at dev and build time. Running `wrangler deploy --env some-env` is therefore not applicable and the environment to deploy should instead be set by running `CLOUDFLARE_ENV=some-env vite build`.

## Redundant fields in the Wrangler config file

There are various options in the [Worker config file](https://developers.cloudflare.com/workers/wrangler/configuration/) that are ignored when using Vite, as they are either no longer applicable or are replaced by Vite equivalents. If these options are provided, then warnings will be printed to the console with suggestions for how to proceed.

### Not applicable

The following build-related options are handled by Vite and are not applicable when using the Cloudflare Vite plugin:

* `tsconfig`
* `rules`
* `build`
* `no_bundle`
* `find_additional_modules`
* `base_dir`
* `preserve_file_names`

### Not supported

* `site` — Use [Workers Assets](https://developers.cloudflare.com/workers/static-assets/) instead.

### Replaced by Vite equivalents

The following options have Vite equivalents that should be used instead:

| Wrangler option | Vite equivalent |
| - | - |
| `define` | [`define`](https://vite.dev/config/shared-options.html#define) |
| `alias` | [`resolve.alias`](https://vite.dev/config/shared-options.html#resolve-alias) |
| `minify` | [`build.minify`](https://vite.dev/config/build-options.html#build-minify) |
| Local dev settings (`ip`, `port`, `local_protocol`, etc.) | [Server options](https://vite.dev/config/server-options.html) |

See [Vite Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/) for more information about configuring your Worker environments in Vite.