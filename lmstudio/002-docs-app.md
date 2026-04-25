---
title: Welcome to LM Studio Docs!
url: https://lmstudio.ai/docs/app
source: sitemap
fetched_at: 2026-04-07T21:27:37.682306672-03:00
rendered_js: false
word_count: 466
summary: This document serves as a comprehensive overview of LM Studio, detailing what it can do with local LLMs, its system requirements, how to run different types of models, and providing information on advanced features like RAG, headless operation, and accessing the built-in API.
tags:
    - local-llm
    - desktop-application
    - api-access
    - model-management
    - runnable-modes
    - huggingface
category: guide
---

To get LM Studio, head over to the [Downloads page](https://lmstudio.ai/download) and download an installer for your operating system.

LM Studio is available for macOS, Windows, and Linux.

## What can I do with LM Studio?[](#what-can-i-do-with-lm-studio "Link to 'What can I do with LM Studio?'")

- Download and run local LLMs like gpt-oss or Llama, Qwen
- Use a simple and flexible chat interface
- Connect MCP servers and use them with local models
- Search & download functionality (via Hugging Face 🤗)
- Serve local models on OpenAI-like endpoints, locally and on the network
- Manage your local models, prompts, and configurations

## System requirements[](#system-requirements "Link to 'System requirements'")

LM Studio generally supports Apple Silicon Macs, x64/ARM64 Windows PCs, and x64 Linux PCs.

Consult the [System Requirements](https://lmstudio.ai/docs/app/system-requirements) page for more detailed information.

## Run llama.cpp (GGUF) or MLX models[](#run-llamacpp-gguf-or-mlx-models "Link to 'Run llama.cpp (GGUF) or MLX models'")

LM Studio supports running LLMs on Mac, Windows, and Linux using [`llama.cpp`](https://github.com/ggerganov/llama.cpp).

On Apple Silicon Macs, LM Studio also supports running LLMs using Apple's [`MLX`](https://github.com/ml-explore/mlx).

To install or manage LM Runtimes, press `⌘` `Shift` `R` on Mac or `Ctrl` `Shift` `R` on Windows/Linux.

## LM Studio as an MCP client[](#lm-studio-as-an-mcp-client "Link to 'LM Studio as an MCP client'")

You can install MCP servers in LM Studio and use them with your local models.

See the docs for more: [Use MCP server](https://lmstudio.ai/docs/app/plugins/mcp).

If you're develping an MCP server, check out [Add to LM Studio Button](https://lmstudio.ai/docs/app/plugins/mcp/deeplink).

## Run an LLM like `gpt-oss`, `Llama`, `Qwen`, `Mistral`, or `DeepSeek R1` on your computer[](#run-an-llm-like-gpt-oss-llama-qwen-mistral-or-deepseek-r1-on-your-computer "Link to 'Run an LLM like ,[object Object],, ,[object Object],, ,[object Object],, ,[object Object],, or ,[object Object], on your computer'")

To run an LLM on your computer you first need to download the model weights.

You can do this right within LM Studio! See [Download an LLM](https://lmstudio.ai/docs/app/basics/download-model) for guidance.

## Chat with documents entirely offline on your computer[](#chat-with-documents-entirely-offline-on-your-computer "Link to 'Chat with documents entirely offline on your computer'")

You can attach documents to your chat messages and interact with them entirely offline, also known as "RAG".

Read more about how to use this feature in the [Chat with Documents](https://lmstudio.ai/docs/app/basics/rag) guide.

## Run LM Studio without the GUI (llmster)[](#run-lm-studio-without-the-gui-llmster "Link to 'Run LM Studio without the GUI (llmster)'")

llmster is the headless version of LM Studio, no desktop app required. It's ideal for servers, CI environments, or any machine where you don't need a GUI.

Learn more: [Headless Mode](https://lmstudio.ai/docs/developer/core/headless).

## Use LM Studio's API from your own apps and scripts[](#use-lm-studios-api-from-your-own-apps-and-scripts "Link to 'Use LM Studio's API from your own apps and scripts'")

LM Studio provides a REST API that you can use to interact with your local models from your own apps and scripts.

- [OpenAI Compatibility API](https://lmstudio.ai/docs/api/openai-api)
- [LM Studio REST API (beta)](https://lmstudio.ai/docs/api/rest-api)

Join the LM Studio community on [Discord](https://discord.gg/aPQfnNkxGC) to ask questions, share knowledge, and get help from other users and the LM Studio team.