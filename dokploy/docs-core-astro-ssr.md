---
title: Astro SSR | Dokploy
url: https://docs.dokploy.com/docs/core/astro-ssr
source: crawler
fetched_at: 2026-02-14T14:18:42.271388-03:00
rendered_js: true
word_count: 91
summary: This document provides a step-by-step guide for deploying an Astro Server-Side Rendering (SSR) application on Dokploy using a Git repository and environment variable configuration.
tags:
    - astro
    - ssr
    - dokploy
    - deployment
    - nixpacks
    - server-side-rendering
category: tutorial
---

Examples

Deploy a simple Astro SSR application.

This example will deploy a simple Astro SSR application.

1. **Use Git Provider in Your Application**:
   
   - Repository: `https://github.com/Dokploy/examples.git`
   - Branch: `main`
   - Build path: `/astro-ssr`
2. **Add Environment Variables**:

<!--THE END-->

- Navigate to the "Environments" tab and add the following variable:
  
  ```
  NIXPACKS_START_CMD="pnpm run preview"
  ```

<!--THE END-->

3. **Click on Deploy**:
   
   - Deploy your application by clicking the deploy button.
4. **Generate a Domain**:
   
   - Click on generate domain button.
   - A new domain will be generated for you.
   - You can use this domain to access your application.

If you need further assistance, join our [Discord server](https://discord.com/invite/2tBnJ3jDJc).