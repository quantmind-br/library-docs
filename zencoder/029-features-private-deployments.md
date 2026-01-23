---
title: Private Deployments - Zencoder Docs
url: https://docs.zencoder.ai/features/private-deployments
source: crawler
fetched_at: 2026-01-23T09:28:11.979890342-03:00
rendered_js: false
word_count: 287
summary: This document explains the benefits and configuration steps for setting up a private Zencoder deployment to ensure data remains within a self-managed network boundary.
tags:
    - private-deployment
    - security-configuration
    - on-premise
    - data-privacy
    - network-isolation
    - custom-models
category: guide
---

## What Is a Private Deployment?

The standard Zencoder cloud experience is already secure for most teams: code runs ephemerally, data is encrypted in transit and at rest, access is gated by role-based controls, and Zencoder maintains ISO 27001/42001 plus SOC 2 Type II certifications. If you are comfortable with those guarantees, you can keep using the default service without extra configuration. A private deployment gives you deeper control by running agents, orchestration, and inference on infrastructure you operate. Typical benefits include:

- Full isolation inside your own network perimeter.
- Support for customer-hosted models and runtimes.
- Zero dependency on external endpoints for sensitive workloads.

Private deployments are recommended for regulated industries, strict data-residency mandates, air-gapped environments, and teams with proprietary models they must keep on-premise.

## Configure a Private Deployment

A full private deployment is a layered approach. Follow these steps to keep Zencoder inside infrastructure you manage:

1. **Configure custom models from local or VPC endpoints.** Use the [Custom Models configuration guide](https://docs.zencoder.ai/features/custom-models-configuration) to declare every model you plan to expose to your users. This is how agents call the runtimes that live within your network boundary.
2. **Hide the managed catalog.** Inside `settings.json`, set `"useDefaultProviders": false` so the selector only lists the providers you declared. This prevents accidental routing to Zencoder-hosted models after you stand up custom ones.
3. **Deactivate code completion.** Code completion today runs on Zencoder-managed models. In VS Code open the Zencoder menu → `Settings` and uncheck **Zencoder Code Completion**. In JetBrains go to `Tools → Zencoder → Settings` and uncheck **Enable code completion** (see [Code Completion](https://docs.zencoder.ai/features/code-completion) for screenshots). This keeps autocomplete traffic from leaving your environment while the team codes against private models.

After applying these steps, all interactive chat and agent runs are served by your endpoints.