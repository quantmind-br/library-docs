---
title: Zai - OpenClaw
url: https://docs.openclaw.ai/providers/zai
source: sitemap
fetched_at: 2026-01-30T20:25:09.128439444-03:00
rendered_js: false
word_count: 67
summary: This document explains how to configure and use the Z.AI API platform for GLM models with OpenClaw, including authentication setup and configuration details.
tags:
    - api-integration
    - glm-models
    - authentication
    - cli-setup
    - openclaw
category: guide
---

## Z.AI

Z.AI is the API platform for **GLM** models. It provides REST APIs for GLM and uses API keys for authentication. Create your API key in the Z.AI console. OpenClaw uses the `zai` provider with a Z.AI API key.

## CLI setup

```
openclaw onboard --auth-choice zai-api-key
# or non-interactive
openclaw onboard --zai-api-key "$ZAI_API_KEY"
```

## Config snippet

```
{
  env: { ZAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "zai/glm-4.7" } } }
}
```

## Notes

- GLM models are available as `zai/<model>` (example: `zai/glm-4.7`).
- See [/providers/glm](https://docs.openclaw.ai/providers/glm) for the model family overview.
- Z.AI uses Bearer auth with your API key.