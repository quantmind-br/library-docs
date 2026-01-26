---
title: "null"
url: https://docs.clawd.bot/providers/glm.md
source: llms
fetched_at: 2026-01-26T09:53:19.164601474-03:00
rendered_js: false
word_count: 81
summary: Explains how to configure and use GLM models via the Z.AI platform in Clawdbot, including CLI setup and model ID references.
tags:
    - glm-models
    - zai-provider
    - clawdbot-config
    - model-setup
    - api-key-configuration
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