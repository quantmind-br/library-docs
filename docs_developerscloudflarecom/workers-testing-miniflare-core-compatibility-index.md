---
title: "\U0001F4C5 Compatibility Dates · Cloudflare Workers docs"
url: https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/index.md
source: llms
fetched_at: 2026-01-24T15:31:43.807579122-03:00
rendered_js: false
word_count: 44
summary: This document explains how to use compatibility dates and flags in Miniflare to manage backwards-incompatible changes and specific runtime behaviors.
tags:
    - miniflare
    - compatibility-dates
    - compatibility-flags
    - configuration
    - cloudflare-workers
category: configuration
---

* [Compatibility Dates Reference](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

## Compatibility Dates

Miniflare uses compatibility dates to opt-into backwards-incompatible changes from a specific date. If one isn't set, it will default to some time far in the past.

```js
const mf = new Miniflare({
  compatibilityDate: "2021-11-12",
});
```

## Compatibility Flags

Miniflare also lets you opt-in/out of specific changes using compatibility flags:

```js
const mf = new Miniflare({
  compatibilityFlags: [
    "formdata_parser_supports_files",
    "durable_object_fetch_allows_relative_url",
  ],
});
```