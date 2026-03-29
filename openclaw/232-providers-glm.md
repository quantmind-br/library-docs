---
title: Glm - OpenClaw
url: https://docs.openclaw.ai/providers/glm
source: sitemap
fetched_at: 2026-01-30T20:25:38.705446411-03:00
rendered_js: false
word_count: 59
summary: This document explains how to access GLM models through the Z.AI platform using OpenClaw, including setup instructions and configuration details.
tags:
    - glm-models
    - z-ai-platform
    - openclaw
    - api-integration
    - model-configuration
category: guide
---

## GLM models

GLM is a **model family** (not a company) available through the Z.AI platform. In OpenClaw, GLM models are accessed via the `zai` provider and model IDs like `zai/glm-4.7`.

## CLI setup

```
openclaw onboard --auth-choice zai-api-key
```

## Config snippet

```
{
  env: { ZAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "zai/glm-4.7" } } }
}
```

## Notes

- GLM versions and availability can change; check Z.AI’s docs for the latest.
- Example model IDs include `glm-4.7` and `glm-4.6`.
- For provider details, see [/providers/zai](https://docs.openclaw.ai/providers/zai).