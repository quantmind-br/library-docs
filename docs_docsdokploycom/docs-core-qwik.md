---
title: Qwik | Dokploy
url: https://docs.dokploy.com/docs/core/qwik
source: crawler
fetched_at: 2026-02-14T14:14:00.048034-03:00
rendered_js: true
word_count: 89
summary: This document provides a step-by-step walkthrough for deploying a Qwik application via a Git repository, including environment variable configuration and domain generation.
tags:
    - qwik
    - deployment
    - git-integration
    - nixpacks
    - environment-variables
    - dokploy
category: tutorial
---

Examples

Deploy a simple Qwik application.

This example will deploy a simple Qwik application.

1. **Use Git Provider in Your Application**:
   
   - Repository: `https://github.com/Dokploy/examples.git`
   - Branch: `main`
   - Build path: `/qwik`
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