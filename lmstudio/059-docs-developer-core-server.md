---
title: LM Studio as a Local LLM API Server
url: https://lmstudio.ai/docs/developer/core/server
source: sitemap
fetched_at: 2026-04-07T21:30:04.3001422-03:00
rendered_js: false
word_count: 113
summary: This document explains multiple methods for serving local Large Language Models (LLMs) from LM Studio, including using the Developer tab, the command line interface, and accessing various API formats.
tags:
    - llm-serving
    - local-models
    - rest-api
    - client-libraries
    - openai-compatibility
category: guide
---

You can serve local LLMs from LM Studio's Developer tab, either on `localhost` or on the network.

LM Studio's APIs can be used through [REST API](https://lmstudio.ai/docs/developer/rest), client libraries like [lmstudio-js](https://lmstudio.ai/docs/typescript) and [lmstudio-python](https://lmstudio.ai/docs/python), and compatibility endpoints like [OpenAI-compatible](https://lmstudio.ai/docs/developer/openai-compat) and [Anthropic-compatible](https://lmstudio.ai/docs/developer/anthropic-compat).

![undefined](https://lmstudio.ai/assets/docs/server.png)

Load and serve LLMs from LM Studio

### Running the server[](#running-the-server)

To run the server, go to the Developer tab in LM Studio, and toggle the "Start server" switch to start the API server.

![undefined](https://lmstudio.ai/assets/docs/server-start.png)

Start the LM Studio API Server

Alternatively, you can use `lms` ([LM Studio's CLI](https://lmstudio.ai/docs/cli)) to start the server from your terminal:

```

lms server start
```

### API options[](#api-options)

- [LM Studio REST API](https://lmstudio.ai/docs/developer/rest)
- [TypeScript SDK](https://lmstudio.ai/docs/typescript) - `lmstudio-js`
- [Python SDK](https://lmstudio.ai/docs/python) - `lmstudio-python`
- [OpenAI-compatible endpoints](https://lmstudio.ai/docs/developer/openai-compat)
- [Anthropic-compatible endpoints](https://lmstudio.ai/docs/developer/anthropic-compat)