---
title: Turborepo | Dokploy
url: https://docs.dokploy.com/docs/core/turborepo
source: crawler
fetched_at: 2026-02-14T14:18:48.09434-03:00
rendered_js: true
word_count: 90
summary: This document provides step-by-step instructions for deploying a Turborepo application on Dokploy using Nixpacks and environment variable configuration.
tags:
    - dokploy
    - turborepo
    - nixpacks
    - deployment
    - monorepo
category: tutorial
---

Examples

Deploy a simple Turborepo application.

This repository contains an example of turborepo application that is deployed on Dokploy.

1. **Use Git Provider in Your Application**:
   
   - Repository: `https://github.com/Dokploy/examples.git`
   - Branch: `main`
   - Build path: `/turborepo` (Nixpacks)
2. **Environment Variables**:
   
   - Add environment variables to the env tab.
   
   ```
   NIXPACKS_TURBO_APP_NAME="web"
   NIXPACKS_BUILD_CMD="turbo run build --filter=web"
   NIXPACKS_START_CMD="turbo run start --filter=web"
   ```
3. **Click on Deploy**:
   
   - Deploy your application by clicking the deploy button.
4. **Generate a Domain**:
   
   - Click on generate domain button.
   - A new domain will be generated for you.
   - Set Port `3000`
   - You can use this domain to access your application.

If you need further assistance, join our [Discord server](https://discord.com/invite/2tBnJ3jDJc).