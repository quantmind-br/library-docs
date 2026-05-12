---
title: Chatbox - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/chatbox/
source: sitemap
fetched_at: 2026-05-07T21:11:41.884765117-03:00
rendered_js: false
word_count: 101
summary: This document provides instructions on how to configure the Chatbox desktop client to interact with an LLM server running on vLLM using OpenAI-compatible endpoints.
tags:
    - chatbox
    - vllm
    - deployment
    - llm-client
    - openai-compatible
    - desktop-application
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/chatbox.md "Edit this page")

[Chatbox](https://github.com/chatboxai/chatbox) is a desktop client for LLMs, available on Windows, Mac, Linux.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM environment:

## Deploy[¶](#deploy "Permanent link")

1. Start the vLLM server with the supported chat completion model, e.g.
   
   ```
   vllmserveqwen/Qwen1.5-0.5B-Chat
   ```
2. Download and install [Chatbox desktop](https://chatboxai.app/en#download).
3. On the bottom left of settings, Add Custom Provider
   
   - API Mode: `OpenAI API Compatible`
   - Name: vllm
   - API Host: `http://{vllm server host}:{vllm server port}/v1`
   - API Path: `/chat/completions`
   - Model: `qwen/Qwen1.5-0.5B-Chat`
   
   [![Chatbox settings screen](https://docs.vllm.ai/en/latest/assets/deployment/chatbox-settings.png)](https://docs.vllm.ai/en/latest/assets/deployment/chatbox-settings.png)
4. Go to `Just chat`, and start to chat:
   
   [![Chatbot chat screen](https://docs.vllm.ai/en/latest/assets/deployment/chatbox-chat.png)](https://docs.vllm.ai/en/latest/assets/deployment/chatbox-chat.png)