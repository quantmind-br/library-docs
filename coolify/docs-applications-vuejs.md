---
title: Vue
url: https://coolify.io/docs/applications/vuejs.md
source: llms
fetched_at: 2026-02-17T14:39:03.415367-03:00
rendered_js: false
word_count: 70
summary: This document provides configuration instructions for deploying Vue.js applications as either server-side or static sites using Nixpacks.
tags:
    - vue-js
    - deployment
    - nixpacks
    - static-site
    - spa
    - configuration
category: configuration
---

# Vue

Vue.js is an approachable, performant and versatile framework for building web user interfaces.

[Example repository.](https://github.com/coollabsio/coolify-examples/tree/main/vue)

## Server build (NodeJS|Express)

* Set `Build Pack` to `nixpacks`.
* Set 'Start Command' to `node server.js`.

## Static build (SPA)

* Set `Build Pack` to `nixpacks`.
* Enable `Is it a static site?`.
* Set `Output Directory` to `dist`.

## Static build with Router (SPA)

* Set `Build Pack` to `nixpacks`.
* Enable `Is it a static site?`.
* Set `Output Directory` to `dist`.