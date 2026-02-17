---
title: Private NPM Registry
url: https://coolify.io/docs/knowledge-base/how-to/private-npm-registry.md
source: llms
fetched_at: 2026-02-17T14:40:44.173509-03:00
rendered_js: false
word_count: 50
summary: This document provides instructions on how to configure a private NPM registry for applications deployed using Coolify by utilizing a .npmrc file and environment variables.
tags:
    - coolify
    - npm
    - private-registry
    - npmrc
    - deployment-configuration
    - environment-variables
category: guide
---

# Private NPM Registry

If you would like to use a private NPM registry with Coolify, you can do so by following the steps below.

1. Add `.npmrc` file to your project root with the following content:

```bash
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
```

2. Add the following environment variables to your project as a `build` variable:

```bash
NPM_TOKEN=your_npm_token
```

3. Deploy your application.