---
title: "null"
url: https://docs.clawd.bot/providers/zai.md
source: llms
fetched_at: 2026-01-26T09:53:30.508059701-03:00
rendered_js: false
word_count: 89
summary: This document explains how to integrate and configure the Z.AI API platform for using GLM models within the Clawdbot environment.
tags:
    - zai
    - glm-models
    - clawdbot
    - api-authentication
    - cli-setup
    - configuration
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Z.AI

Z.AI is the API platform for **GLM** models. It provides REST APIs for GLM and uses API keys
for authentication. Create your API key in the Z.AI console. Clawdbot uses the `zai` provider
with a Z.AI API key.

## CLI setup

```bash  theme={null}
clawdbot onboard --auth-choice zai-api-key
# or non-interactive
clawdbot onboard --zai-api-key "$ZAI_API_KEY"
```

## Config snippet

```json5  theme={null}
{
  env: { ZAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "zai/glm-4.7" } } }
}
```

## Notes

* GLM models are available as `zai/<model>` (example: `zai/glm-4.7`).
* See [/providers/glm](/providers/glm) for the model family overview.
* Z.AI uses Bearer auth with your API key.