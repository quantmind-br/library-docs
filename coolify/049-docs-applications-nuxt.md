---
title: Nuxt
url: https://coolify.io/docs/applications/nuxt.md
source: llms
fetched_at: 2026-02-17T14:39:05.116573-03:00
rendered_js: false
word_count: 128
summary: This document provides deployment configuration instructions for Nuxt and Nitro applications using Nixpacks, covering both server-side and static build processes.
tags:
    - nuxt
    - nitro
    - nixpacks
    - deployment
    - static-site
    - server-build
    - web-development
category: configuration
---

# Nuxt

Nuxt is an open source framework that makes web development intuitive and powerful.
Create performant and production-grade full-stack web apps and websites with confidence.

[Example repository.](https://github.com/coollabsio/coolify-examples/tree/main/nuxt)

## Server build (Nuxt, using `nuxt build`)

* Set `Build Pack` to `nixpacks`.
* Set Start Command to `node .output/server/index.mjs`

Alternatively, you can set the `start` script inside package.json to `node .output/server/index.mjs`. Then Nixpacks will automatically use it as the start command.

## Static build (Nuxt, using `nuxt generate`)

* Set `Build Pack` to `nixpacks`.
* Enable `Is it a static site?`.
* Set `Output Directory` to `dist`.

## Nitro server build (Nitro, using `nitro build`)

* Set `Build Pack` to `nixpacks`.
* Set Start Command to `node .output/server/index.mjs`

Alternatively, you can set the `start` script inside package.json to `node .output/server/index.mjs`. Then Nixpacks will automatically use it as the start command.