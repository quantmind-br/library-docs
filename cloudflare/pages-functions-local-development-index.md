---
title: Local development · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/local-development/index.md
source: llms
fetched_at: 2026-01-24T15:17:19.236095956-03:00
rendered_js: false
word_count: 223
summary: This document provides instructions on how to use the Wrangler CLI to develop and preview Cloudflare Pages applications locally, including support for static assets, Functions, and HTTPS.
tags:
    - cloudflare-pages
    - wrangler-cli
    - local-development
    - dev-server
    - web-hosting
category: guide
---

Run your Pages application locally with our Wrangler Command Line Interface (CLI).

## Install Wrangler

To get started with Wrangler, refer to the [Install/Update Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/).

## Run your Pages project locally

The main command for local development on Pages is `wrangler pages dev`. This will let you run your Pages application locally, which includes serving static assets and running your Functions.

With your folder of static assets set up, run the following command to start local development:

```sh
npx wrangler pages dev <DIRECTORY-OF-ASSETS>
```

This will then start serving your Pages project. You can press `b` to open the browser on your local site, (available, by default, on <http://localhost:8788>).

Note

If you have a [Wrangler configuration file](https://developers.cloudflare.com/pages/functions/wrangler-configuration/) file configured for your Pages project, you can run [`wrangler pages dev`](https://developers.cloudflare.com/workers/wrangler/commands/#dev-1) without specifying a directory.

### HTTPS support

To serve your local development server over HTTPS with a self-signed certificate, you can \[set `local_protocol` via the [Wrangler configuration file](https://developers.cloudflare.com/pages/functions/wrangler-configuration/#local-development-settings) or you can pass the `--local-protocol=https` argument to [`wrangler pages dev`](https://developers.cloudflare.com/workers/wrangler/commands/#dev-1):

```sh
npx wrangler pages dev --local-protocol=https <DIRECTORY-OF-ASSETS>
```

## Attach bindings to local development

To attach a binding to local development, refer to [Bindings](https://developers.cloudflare.com/pages/functions/bindings/) and find the Cloudflare Developer Platform resource you would like to work with.

## Additional Wrangler configuration

If you are using a Wrangler configuration file in your project, you can set up dev server values like: `port`, `local protocol`, `ip`, and `port`. For more information, read about [configuring local development settings](https://developers.cloudflare.com/pages/functions/wrangler-configuration/#local-development-settings).