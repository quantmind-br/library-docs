---
title: Rollbacks · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/configuration/rollbacks/index.md
source: llms
fetched_at: 2026-01-24T15:17:08.604440733-03:00
rendered_js: false
word_count: 125
summary: This document explains how to revert a Cloudflare Pages project to a previous successful production deployment using the dashboard. it outlines the requirements for valid rollback targets and provides step-by-step instructions for the process.
tags:
    - cloudflare-pages
    - rollbacks
    - deployment-management
    - production-deployments
    - version-control
category: guide
---

Rollbacks allow you to instantly revert your project to a previous production deployment.

Any production deployment that has been successfully built is a valid rollback target. When your project has rolled back to a previous deployment, you may still rollback to deployments that are newer than your current version. Note that preview deployments are not valid rollback targets.

In order to perform a rollback, go to **Deployments** in your Pages project. Browse the **All deployments** list and select the three dotted actions menu for the desired target. Select **Rollback to this deployment** for a confirmation window to appear. When confirmed, your project's production deployment will change instantly.

![Deployments for your Pages project that can be used for rollbacks](https://developers.cloudflare.com/_astro/rollbacks.DNHeRPOm_ZSEvgH.webp)

## Related resources

* [Preview Deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)
* [Branch deployment controls](https://developers.cloudflare.com/pages/configuration/branch-build-controls/)