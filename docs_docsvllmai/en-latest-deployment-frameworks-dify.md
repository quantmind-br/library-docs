---
title: Dify - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/dify/
source: sitemap
fetched_at: 2026-05-07T21:11:43.00540188-03:00
rendered_js: false
word_count: 205
summary: This document provides step-by-step instructions for deploying the Dify LLM development platform using vLLM as the backend inference provider.
tags:
    - dify
    - vllm
    - llm-deployment
    - model-provider
    - docker-compose
    - chatbot-development
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/dify.md "Edit this page")

[Dify](https://github.com/langgenius/dify) is an open-source LLM app development platform. Its intuitive interface combines agentic AI workflow, RAG pipeline, agent capabilities, model management, observability features, and more, allowing you to quickly move from prototype to production.

It supports vLLM as a model provider to efficiently serve large language models.

This guide walks you through deploying Dify using a vLLM backend.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM environment:

And install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

## Deploy[¶](#deploy "Permanent link")

1. Start the vLLM server with the supported chat completion model, e.g.
   
   ```
   vllmserveQwen/Qwen1.5-7B-Chat
   ```
2. Start the Dify server with docker compose ([details](https://github.com/langgenius/dify?tab=readme-ov-file#quick-start)):
   
   ```
   gitclonehttps://github.com/langgenius/dify.git
   cddify
   cddocker
   cp.env.example.env
   dockercomposeup-d
   ```
3. Open the browser to access `http://localhost/install`, config the basic login information and login.
4. In the top-right user menu (under the profile icon), go to Settings, then click `Model Provider`, and locate the `vLLM` provider to install it.
5. Fill in the model provider details as follows:
   
   - **Model Type**: [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM")
   - **Model Name**: `Qwen/Qwen1.5-7B-Chat`
   - **API Endpoint URL**: `http://{vllm_server_host}:{vllm_server_port}/v1`
   - **Model Name for API Endpoint**: `Qwen/Qwen1.5-7B-Chat`
   - **Completion Mode**: `Completion`
   
   [![Dify settings screen](https://docs.vllm.ai/en/latest/assets/deployment/dify-settings.png)](https://docs.vllm.ai/en/latest/assets/deployment/dify-settings.png)
6. To create a test chatbot, go to `Studio → Chatbot → Create from Blank`, then select Chatbot as the type:
   
   [![Dify create chatbot screen](https://docs.vllm.ai/en/latest/assets/deployment/dify-create-chatbot.png)](https://docs.vllm.ai/en/latest/assets/deployment/dify-create-chatbot.png)
7. Click the chatbot you just created to open the chat interface and start interacting with the model:
   
   [![Dify chat screen](https://docs.vllm.ai/en/latest/assets/deployment/dify-chat.png)](https://docs.vllm.ai/en/latest/assets/deployment/dify-chat.png)