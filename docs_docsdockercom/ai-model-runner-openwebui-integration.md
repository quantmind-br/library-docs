---
title: Open WebUI integration
url: https://docs.docker.com/ai/model-runner/openwebui-integration/
source: llms
fetched_at: 2026-01-24T14:14:22.269583927-03:00
rendered_js: false
word_count: 480
summary: This document provides instructions for setting up and configuring Open WebUI as a graphical chat interface for local AI models using Docker Model Runner. It covers deployment via Docker Compose, platform-specific network configurations, and troubleshooting common integration issues.
tags:
    - open-webui
    - docker-model-runner
    - docker-compose
    - self-hosted
    - local-ai
    - chat-interface
    - configuration
category: tutorial
---

Table of contents

* * *

[Open WebUI](https://github.com/open-webui/open-webui) is an open-source, self-hosted web interface that provides a ChatGPT-like experience for local AI models. You can connect it to Docker Model Runner to get a polished chat interface for your models.

## [Prerequisites](#prerequisites)

- Docker Model Runner enabled with TCP access
- A model pulled (e.g., `docker model pull ai/llama3.2`)

## [Quick start with Docker Compose](#quick-start-with-docker-compose)

The easiest way to run Open WebUI with Docker Model Runner is using Docker Compose.

Create a `compose.yaml` file:

```
services:open-webui:image:ghcr.io/open-webui/open-webui:mainports:- "3000:8080"environment:- OLLAMA_BASE_URL=http://host.docker.internal:12434- WEBUI_AUTH=falseextra_hosts:- "host.docker.internal:host-gateway"volumes:- open-webui:/app/backend/datavolumes:open-webui:
```

Start the services:

Open your browser to [http://localhost:3000](http://localhost:3000).

## [Configuration options](#configuration-options)

### [Environment variables](#environment-variables)

VariableDescriptionDefault`OLLAMA_BASE_URL`URL of Docker Model RunnerRequired`WEBUI_AUTH`Enable authentication`true``OPENAI_API_BASE_URL`Use OpenAI-compatible API instead-`OPENAI_API_KEY`API key (use any value for DMR)-

### [Using OpenAI-compatible API](#using-openai-compatible-api)

If you prefer to use the OpenAI-compatible API instead of the Ollama API:

```
services:open-webui:image:ghcr.io/open-webui/open-webui:mainports:- "3000:8080"environment:- OPENAI_API_BASE_URL=http://host.docker.internal:12434/engines/v1- OPENAI_API_KEY=not-needed- WEBUI_AUTH=falseextra_hosts:- "host.docker.internal:host-gateway"volumes:- open-webui:/app/backend/datavolumes:open-webui:
```

## [Network configuration](#network-configuration)

### [Docker Desktop](#docker-desktop)

On Docker Desktop, `host.docker.internal` automatically resolves to the host machine. The previous example works without modification.

### [Docker Engine (Linux)](#docker-engine-linux)

On Docker Engine, you may need to configure the network differently:

```
services:open-webui:image:ghcr.io/open-webui/open-webui:mainnetwork_mode:hostenvironment:- OLLAMA_BASE_URL=http://localhost:12434- WEBUI_AUTH=falsevolumes:- open-webui:/app/backend/datavolumes:open-webui:
```

Or use the host gateway:

```
services:open-webui:image:ghcr.io/open-webui/open-webui:mainports:- "3000:8080"environment:- OLLAMA_BASE_URL=http://172.17.0.1:12434- WEBUI_AUTH=falsevolumes:- open-webui:/app/backend/datavolumes:open-webui:
```

## [Using Open WebUI](#using-open-webui)

### [Select a model](#select-a-model)

1. Open [http://localhost:3000](http://localhost:3000)
2. Select the model drop-down in the top-left
3. Select from your pulled models (they appear with `ai/` prefix)

### [Pull models through the UI](#pull-models-through-the-ui)

Open WebUI can pull models directly:

1. Select the model drop-down
2. Enter a model name: `ai/llama3.2`
3. Select the download icon

### [Chat features](#chat-features)

Open WebUI provides:

- Multi-turn conversations with context
- Message editing and regeneration
- Code syntax highlighting
- Markdown rendering
- Conversation history and search
- Export conversations

## [Complete example with multiple models](#complete-example-with-multiple-models)

This example sets up Open WebUI with Docker Model Runner and pre-pulls several models:

```
services:open-webui:image:ghcr.io/open-webui/open-webui:mainports:- "3000:8080"environment:- OLLAMA_BASE_URL=http://host.docker.internal:12434- WEBUI_AUTH=false- DEFAULT_MODELS=ai/llama3.2extra_hosts:- "host.docker.internal:host-gateway"volumes:- open-webui:/app/backend/datadepends_on:model-setup:condition:service_completed_successfullymodel-setup:image:docker:clivolumes:- /var/run/docker.sock:/var/run/docker.sockcommand:>      sh -c "
        docker model pull ai/llama3.2 &&
        docker model pull ai/qwen2.5-coder &&
        docker model pull ai/smollm2
      "volumes:open-webui:
```

## [Enabling authentication](#enabling-authentication)

For multi-user setups or security, enable authentication:

```
services:open-webui:image:ghcr.io/open-webui/open-webui:mainports:- "3000:8080"environment:- OLLAMA_BASE_URL=http://host.docker.internal:12434- WEBUI_AUTH=trueextra_hosts:- "host.docker.internal:host-gateway"volumes:- open-webui:/app/backend/datavolumes:open-webui:
```

On first visit, you'll create an admin account.

## [Troubleshooting](#troubleshooting)

### [Models don't appear in the drop-down](#models-dont-appear-in-the-drop-down)

1. Verify Docker Model Runner is accessible:
   
   ```
   $ curl http://localhost:12434/api/tags
   ```
2. Check that models are pulled:
3. Verify the `OLLAMA_BASE_URL` is correct and accessible from the container.

### ["Connection refused" errors](#connection-refused-errors)

1. Ensure TCP access is enabled for Docker Model Runner.
2. On Docker Desktop, verify `host.docker.internal` resolves:
   
   ```
   $ docker run --rm alpine ping -c 1 host.docker.internal
   ```
3. On Docker Engine, try using `network_mode: host` or the explicit host IP.

### [Slow response times](#slow-response-times)

1. First requests load the model into memory, which takes time.
2. Subsequent requests are much faster.
3. If consistently slow, consider:
   
   - Using a smaller model
   - Reducing context size
   - Checking GPU acceleration is working

### [CORS errors](#cors-errors)

If running Open WebUI on a different host:

1. In Docker Desktop, go to Settings &gt; AI
2. Add the Open WebUI URL to **CORS Allowed Origins**

## [Customization](#customization)

### [Custom system prompts](#custom-system-prompts)

Open WebUI supports setting system prompts per model. Configure these in the UI under Settings &gt; Models.

### [Model parameters](#model-parameters)

Adjust model parameters in the chat interface:

1. Select the settings icon next to the model name
2. Adjust temperature, top-p, max tokens, etc.

These settings are passed through to Docker Model Runner.

## [Running on a different port](#running-on-a-different-port)

To run Open WebUI on a different port:

```
services:open-webui:image:ghcr.io/open-webui/open-webui:mainports:- "8080:8080"# Change first port number# ... rest of config
```

## [What's next](#whats-next)

- [API reference](https://docs.docker.com/ai/model-runner/api-reference/) - Learn about the APIs Open WebUI uses
- [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) - Tune model behavior
- [IDE integrations](https://docs.docker.com/ai/model-runner/ide-integrations/) - Connect other tools to DMR