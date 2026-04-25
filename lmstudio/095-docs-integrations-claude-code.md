---
title: Claude Code
url: https://lmstudio.ai/docs/integrations/claude-code
source: sitemap
fetched_at: 2026-04-07T21:27:47.886334989-03:00
rendered_js: false
word_count: 199
summary: This guide explains how to configure Claude Code to interact with a local LLM server running in LM Studio using the Anthropic-compatible API endpoint.
tags:
    - claude-code
    - lm-studio
    - api-integration
    - environment-variables
    - local-llm
category: guide
---

Claude Code can talk to LM Studio via the Anthropic-compatible `POST /v1/messages` endpoint. See: [Anthropic-compatible Messages endpoint](https://lmstudio.ai/docs/developer/anthropic-compat/messages).

![undefined](https://lmstudio.ai/assets/docs/claude-code.webp)

Claude Code configured to use LM Studio via the Anthropic-compatible API

Have a powerful LLM rig? Use [LM Link](https://lmstudio.ai/docs/integrations/lmlink) to run Claude Code from your laptop while the model runs on your rig.

### 1) Start LM Studio's local server[](#1-start-lm-studios-local-server)

Make sure LM Studio is running as a server (default port `1234`).

You can start it from the app, or from the terminal with `lms`:

```

lms server start --port 1234
```

### 2) Configure Claude Code[](#2-configure-claude-code)

Set these environment variables so the `claude` CLI points to your local LM Studio:

```

export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
```

Notes:

- If Require Authentication is enabled, set `ANTHROPIC_AUTH_TOKEN` to your LM Studio API token. To learn more, see: [Authentication](https://lmstudio.ai/docs/developer/core/authentication).

### 3) Run Claude Code against a local model[](#3-run-claude-code-against-a-local-model)

```

claude --model openai/gpt-oss-20b
```

Use a model (and server/model settings) with more than ~25k context length. Tools like Claude Code can consume a lot of context.

### 4) If Require Authentication is enabled, use your LM Studio API token[](#4-if-require-authentication-is-enabled-use-your-lm-studio-api-token)

If you turned on "Require Authentication" in LM Studio, create an API token and set:

```

export LM_API_TOKEN=<LMSTUDIO_TOKEN>
export ANTHROPIC_AUTH_TOKEN=$LM_API_TOKEN
```

When Require Authentication is enabled, LM Studio accepts both `x-api-key` and `Authorization: Bearer <token>`.

If you're running into trouble, hop onto our [Discord](https://discord.gg/lmstudio)