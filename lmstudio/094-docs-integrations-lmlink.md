---
title: Using LM Link with Integrations
url: https://lmstudio.ai/docs/integrations/lmlink
source: sitemap
fetched_at: 2026-04-07T21:27:49.938111153-03:00
rendered_js: false
word_count: 165
summary: This document explains how to use LM Link to allow coding tools on a local machine to run language models hosted on a remote device, detailing the necessary setup for API routing.
tags:
    - lmlink
    - remote-llm
    - api-connection
    - local-development
    - model-hosting
category: guide
---

With [LM Link](https://lmstudio.ai/docs/lmlink), your coding tools can run models on a remote device (like a dedicated LLM rig on your network) while you work from your laptop

![undefined](https://lmstudio.ai/assets/docs/lmlink-claudecode.gif)

Claude Code using a model loaded on a remote device via LM Link

## Use your integration as normal[](#use-your-integration-as-normal "Link to 'Use your integration as normal'")

Start LM Studio's server on your local machine and configure your tool to point to it. Model loads are routed to the device the model is loaded on or the preferred device if set.

Your local machine handles the API surface at `localhost:1234`, while the model runs on the device the model is present on.

```

lms server start --port 1234
```

### Claude Code[](#claude-code)

```

export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
claude --model qwen3-8b
```

See the full [Claude Code](https://lmstudio.ai/docs/integrations/claude-code) guide.

### Codex[](#codex)


See the full [Codex](https://lmstudio.ai/docs/integrations/codex) guide.

## Set a preferred device[](#set-a-preferred-device "Link to 'Set a preferred device'")

To use a model on a specific remote device, set the device as the preferred device.

See [set a preferred device](https://lmstudio.ai/docs/lmlink/basics/preferred-device) for more details.

If you're running into trouble, hop onto our [Discord](https://discord.gg/lmstudio)