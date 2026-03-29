---
title: Secrets · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/vite-plugin/reference/secrets/index.md
source: llms
fetched_at: 2026-01-24T15:31:20.265504362-03:00
rendered_js: false
word_count: 101
summary: This document explains how to manage sensitive information using secrets in Cloudflare Workers, specifically focusing on local development configurations and integration with the Vite plugin.
tags:
    - cloudflare-workers
    - secrets
    - environment-variables
    - local-development
    - vite-plugin
    - wrangler
category: configuration
---

[Secrets](https://developers.cloudflare.com/workers/configuration/secrets/) are typically used for storing sensitive information such as API keys and auth tokens. For deployed Workers, they are set via the dashboard or Wrangler CLI.

In local development, secrets can be provided to your Worker by using a [`.dev.vars`](https://developers.cloudflare.com/workers/configuration/secrets/#local-development-with-secrets) file. If you are using [Cloudflare Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/cloudflare-environments/) then the relevant `.dev.vars` file will be selected. For example, `CLOUDFLARE_ENV=staging vite dev` will load `.dev.vars.staging` if it exists and fall back to `.dev.vars`.

Note

The `vite build` command copies the relevant `.dev.vars` file to the output directory. This is only used when running `vite preview` and is not deployed with your Worker.