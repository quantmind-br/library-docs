---
title: LM Studio Developer Docs
url: https://lmstudio.ai/docs/developer
source: sitemap
fetched_at: 2026-04-07T21:29:49.137654383-03:00
rendered_js: false
word_count: 175
summary: This document provides a comprehensive overview of the various ways to interact with LM Studio, detailing SDKs for TypeScript and Python, REST API endpoints, and command-line tools. It also includes quick start examples for setting up connections.
tags:
    - sdk
    - rest-api
    - cli
    - developer-tools
    - typescript
    - python
category: guide
---

## Get to know the stack[](#get-to-know-the-stack "Link to 'Get to know the stack'")

- TypeScript SDK: [lmstudio-js](https://lmstudio.ai/docs/typescript)
- Python SDK: [lmstudio-python](https://lmstudio.ai/docs/python)
- LM Studio REST API: [Stateful Chats, MCPs via API](https://lmstudio.ai/docs/developer/rest)
- OpenAI‑compatible: [Chat, Responses, Embeddings](https://lmstudio.ai/docs/developer/openai-compat)
- Anthropic-compatible: [Messages](https://lmstudio.ai/docs/developer/anthropic-compat)
- LM Studio CLI: [`lms`](https://lmstudio.ai/docs/cli)

## What you can build[](#what-you-can-build "Link to 'What you can build'")

- Chat and text generation with streaming
- Tool calling and local agents with MCP
- Structured output (JSON schema)
- Embeddings and tokenization
- Model management (load, download, list)

## Install `llmster` for headless deployments[](#install-llmster-for-headless-deployments "Link to 'Install ,[object Object], for headless deployments'")

`llmster` is LM Studio's core, packaged as a daemon for headless deployment on servers, cloud instances, or CI. The daemon runs standalone, and it is not dependent on the LM Studio GUI.

**Mac / Linux**

```

curl -fsSL https://lmstudio.ai/install.sh | bash
```

**Windows**

```

irm https://lmstudio.ai/install.ps1 | iex
```

**Basic usage**

```

lms daemon up          # Start the daemon
lms get <model>        # Download a model
lms server start       # Start the local server
lms chat               # Open an interactive session
```

Learn more: [Headless deployments](https://lmstudio.ai/blog/0.4.0#deploy-on-servers-deploy-in-ci-deploy-anywhere)

## Super quick start[](#super-quick-start "Link to 'Super quick start'")

### TypeScript (`lmstudio-js`)[](#typescript-lmstudio-js)

```

npm install @lmstudio/sdk

import { LMStudioClient } from "@lmstudio/sdk";

const client = new LMStudioClient();
const model = await client.llm.model("openai/gpt-oss-20b");
const result = await model.respond("Who are you, and what can you do?");

console.info(result.content);
```

Full docs: [lmstudio-js](https://lmstudio.ai/docs/typescript), Source: [GitHub](https://github.com/lmstudio-ai/lmstudio-js)

### Python (`lmstudio-python`)[](#python-lmstudio-python)


```

import lmstudio as lms

with lms.Client() as client:
    model = client.llm.model("openai/gpt-oss-20b")
    result = model.respond("Who are you, and what can you do?")
    print(result)
```

Full docs: [lmstudio-python](https://lmstudio.ai/docs/python), Source: [GitHub](https://github.com/lmstudio-ai/lmstudio-python)

### HTTP (LM Studio REST API)[](#http-lm-studio-rest-api)

```

lms server start --port 1234

curl http://localhost:1234/api/v1/chat \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LM_API_TOKEN" \
  -d '{
    "model": "openai/gpt-oss-20b",
    "input": "Who are you, and what can you do?"
  }'
```

Full docs: [LM Studio REST API](https://lmstudio.ai/docs/developer/rest)

## Helpful links[](#helpful-links "Link to 'Helpful links'")

- [API Changelog](https://lmstudio.ai/docs/developer/api-changelog)
- [Local server basics](https://lmstudio.ai/docs/developer/core/server)
- [CLI reference](https://lmstudio.ai/docs/cli)
- [Discord Community](https://discord.gg/lmstudio)