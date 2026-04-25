---
title: Codex
url: https://lmstudio.ai/docs/integrations/codex
source: sitemap
fetched_at: 2026-04-07T21:27:46.011478663-03:00
rendered_js: false
word_count: 157
summary: This document explains how to connect the Codex tool to a local Large Language Model (LLM) instance running via LM Studio using its OpenAI-compatible API endpoint.
tags:
    - codex
    - lm-studio
    - openai-api
    - local-model
    - llm-integration
    - server-setup
category: guide
---

Codex can talk to LM Studio via the OpenAI-compatible `POST /v1/responses` endpoint. See: [OpenAI-compatible Responses endpoint](https://lmstudio.ai/docs/developer/openai-compat/responses).

![undefined](https://lmstudio.ai/assets/docs/codex.webp)

Codex configured to use LM Studio via the OpenAI-compatible API

Have a powerful LLM rig? Use [LM Link](https://lmstudio.ai/docs/integrations/lmlink) to run Codex from your laptop while the model runs on your rig.

### 1) Start LM Studio's local server[](#1-start-lm-studios-local-server)

Make sure LM Studio is running as a server (default port `1234`).

You can start it from the app, or from the terminal with `lms`:

```

lms server start --port 1234
```

### 2) Run Codex against a local model[](#2-run-codex-against-a-local-model)

Run Codex as you normally would, but with the `--oss` flag to point it to LM Studio.

Example:


By default, Codex will download and use [openai/gpt-oss-20b](https://lmstudio.ai/models/openai/gpt-oss-20b).

Use a model (and server/model settings) with more than ~25k context length. Tools like Codex can consume a lot of context.

You can also use any other model you have available in LM Studio. For example:

```

codex --oss -m ibm/granite-4-micro
```

If you're running into trouble, hop onto our [Discord](https://discord.gg/lmstudio)