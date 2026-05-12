---
title: Open WebUI - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/open-webui/
source: sitemap
fetched_at: 2026-05-07T21:11:52.789990219-03:00
rendered_js: false
word_count: 116
summary: This document provides instructions on how to integrate and deploy the Open WebUI platform with a vLLM server instance using Docker.
tags:
    - vllm
    - open-webui
    - docker-deployment
    - llm-serving
    - chat-interface
    - ai-infrastructure
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/open-webui.md "Edit this page")

[Open WebUI](https://github.com/open-webui/open-webui) is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various LLM runners like Ollama and OpenAI-compatible APIs, with built-in RAG capabilities, making it a powerful AI deployment solution.

To get started with Open WebUI using vLLM, follow these steps:

1. Install the [Docker](https://docs.docker.com/engine/install/).
2. Start the vLLM server with a supported chat completion model:
   
   ```
   vllm serve Qwen/Qwen3-0.6B-Chat
   ```
   
   Note
   
   When starting the vLLM server, be sure to specify the host and port using the `--host` and `--port` flags. For example:
   
   ```
   vllm serve <model> --host 0.0.0.0 --port 8000
   ```
3. Start the Open WebUI Docker container:
   
   ```
   docker run -d \
       --name open-webui \
       -p 3000:8080 \
       -v open-webui:/app/backend/data \
       -e OPENAI_API_BASE_URL=http://0.0.0.0:8000/v1 \
       --restart always \
       ghcr.io/open-webui/open-webui:main
   ```
4. Open it in the browser: [http://open-webui-host:3000/](http://open-webui-host:3000/)
   
   At the top of the page, you should see the model `Qwen/Qwen3-0.6B-Chat`.
   
   [![Web portal of model Qwen/Qwen3-0.6B-Chat](https://docs.vllm.ai/en/latest/assets/deployment/open_webui.png)](https://docs.vllm.ai/en/latest/assets/deployment/open_webui.png)