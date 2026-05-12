---
title: AnythingLLM - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/anything-llm/
source: sitemap
fetched_at: 2026-05-07T21:11:37.052025437-03:00
rendered_js: false
word_count: 164
summary: This document provides instructions on how to integrate and deploy a vLLM-hosted large language model as an AI provider within the AnythingLLM desktop application.
tags:
    - vllm
    - anythingllm
    - deployment
    - openai-compatible
    - llm-integration
    - context-aware-chat
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/anything-llm.md "Edit this page")

[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) is a full-stack application that enables you to turn any document, resource, or piece of content into context that any LLM can use as references during chatting.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM environment:

## Deploy[¶](#deploy "Permanent link")

1. Start the vLLM server with a supported chat-completion model, for example:
   
   ```
   vllmserveQwen/Qwen1.5-32B-Chat-AWQ--max-model-len4096
   ```
2. Download and install [AnythingLLM Desktop](https://anythingllm.com/desktop).
3. Configure the AI provider:
   
   - At the bottom, click the 🔧 wrench icon -&gt; **Open settings** -&gt; **AI Providers** -&gt; **LLM**.
   - Enter the following values:
     
     - LLM Provider: Generic OpenAI
     - Base URL: `http://{vllm server host}:{vllm server port}/v1`
     - Chat Model Name: `Qwen/Qwen1.5-32B-Chat-AWQ`
   
   [![set AI providers](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-provider.png)](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-provider.png)
4. Create a workspace:
   
   1. At the bottom, click the ↺ back icon and back to workspaces.
   2. Create a workspace (e.g., `vllm`) and start chatting.
   
   [![create a workspace](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-chat-without-doc.png)](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-chat-without-doc.png)
5. Add a document.
   
   1. Click the 📎 attachment icon.
   2. Upload a document.
   3. Select and move the document into your workspace.
   4. Save and embed it.
   
   [![add a document](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-upload-doc.png)](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-upload-doc.png)
6. Chat using your document as context.
   
   [![chat with your context](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-chat-with-doc.png)](https://docs.vllm.ai/en/latest/assets/deployment/anything-llm-chat-with-doc.png)