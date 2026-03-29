---
title: Configuration - Zencoder Docs
url: https://docs.zencoder.ai/features/custom-models-configuration
source: crawler
fetched_at: 2026-01-23T09:28:10.743737238-03:00
rendered_js: false
word_count: 108
summary: This document explains how to integrate custom third-party, local, or VPC model providers into Zencoder using global or project-specific settings.json configurations.
tags:
    - zencoder
    - custom-models
    - configuration
    - settings-json
    - model-providers
    - byom
category: configuration
---

Configure custom models by adding providers to `settings.json`. The same file works globally (`~/.zencoder/settings.json`) or per project (`.zencoder/settings.json`), letting you expose local, VPC, or third-party endpoints right inside the Zencoder model selector. ![Model selector showing BYOM models](https://mintcdn.com/forgoodaiinc/zN5YYrfTXxN7HBxM/images/model-selector-private-config.png?fit=max&auto=format&n=zN5YYrfTXxN7HBxM&q=85&s=28c8d3148d1db3587ce1b09e3c0f0225)

## Model Definition

Everything—examples, provider lists, reference properties, and troubleshooting—lives inside the JSON structure shown below.

### Adding More Providers

Replicate the outer `"providers": { ... }` structure with new keys for each vendor or environment. Mix local runtimes, VPC gateways, and SaaS APIs—Zencoder lists every declared model in the selector.

### Reference

## Where to Configure

Use the same JSON schema at either scope depending on how broadly you want to share the providers.