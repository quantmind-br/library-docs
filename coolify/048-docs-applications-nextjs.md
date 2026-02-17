---
title: NextJS
url: https://coolify.io/docs/applications/nextjs.md
source: llms
fetched_at: 2026-02-17T14:39:01.600935-03:00
rendered_js: false
word_count: 108
summary: This document provides instructions for deploying NextJS applications using Nixpacks or Dockerfile, covering both server-side and static site configurations.
tags:
    - nextjs
    - deployment
    - nixpacks
    - dockerfile
    - static-site
    - server-side-rendering
category: guide
---

# NextJS

NextJS is a React framework that enables functionality such as server-side rendering and generating static websites.

[Example repository.](https://github.com/coollabsio/coolify-examples/tree/main/nextjs)

## Deploy with Nixpacks

### Server build (NodeJS)

* Set `Build Pack` to `nixpacks`.

### Static build (SPA)

* Set `Build Pack` to `nixpacks`.
* Enable `Is it a static site?`.
* Set `Output Directory` to `out`.

## Deploy with Dockerfile

If you are having problems with Nixpacks or want more control over the building stage, you can use a Dockerfile to deploy your NextJS application.

### Prerequisites

1. Set `Ports Exposes` field to `3000`.
2. Create a `Dockerfile` in the root of your project and copy the content from the official [NextJS Repository](https://github.com/vercel/next.js/blob/canary/examples/with-docker/Dockerfile).
3. Set the Build Pack to `Dockerfile`.