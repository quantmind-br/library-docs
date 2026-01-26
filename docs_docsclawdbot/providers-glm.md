---
title: "null"
url: https://docs.clawd.bot/providers/glm.md
source: llms
fetched_at: 2026-01-26T10:14:52.791044314-03:00
rendered_js: false
word_count: 81
summary: This document explains how to integrate and configure GLM models from the Z.AI platform within Clawdbot using the zai provider. It provides instructions for CLI onboarding and configuration snippets for setting primary model defaults.
tags:
    - clawdbot
    - zai-provider
    - glm-models
    - model-configuration
    - cli-setup
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# GLM models

GLM is a **model family** (not a company) available through the Z.AI platform. In Clawdbot, GLM
models are accessed via the `zai` provider and model IDs like `zai/glm-4.7`.

## CLI setup

```bash  theme={null}
clawdbot onboard --auth-choice zai-api-key
```

## Config snippet

```json5  theme={null}
{
  env: { ZAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "zai/glm-4.7" } } }
}
```

## Notes

* GLM versions and availability can change; check Z.AI's docs for the latest.
* Example model IDs include `glm-4.7` and `glm-4.6`.
* For provider details, see [/providers/zai](/providers/zai).