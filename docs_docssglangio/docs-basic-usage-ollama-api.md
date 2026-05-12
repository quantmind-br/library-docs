---
title: Ollama-Compatible API - SGLang Documentation
url: https://docs.sglang.io/docs/basic_usage/ollama_api
source: sitemap
fetched_at: 2026-05-11T05:49:12.403505105-03:00
rendered_js: false
word_count: 128
summary: This document explains how to configure SGLang to provide Ollama-compatible API endpoints for text generation and chat, enabling the use of Ollama CLI tools and client libraries with SGLang.
tags:
    - sglang
    - ollama-api
    - inference-backend
    - llm-serving
    - api-compatibility
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang provides Ollama API compatibility, allowing you to use the Ollama CLI and Python library with SGLang as the inference backend.

## Prerequisites

## Endpoints

EndpointMethodDescription`/`GET, HEADHealth check for Ollama CLI`/api/tags`GETList available models`/api/chat`POSTChat completions (streaming & non-streaming)`/api/generate`POSTText generation (streaming & non-streaming)`/api/show`POSTModel information

## Quick Start

### 1. Launch SGLang Server

### 2. Use Ollama CLI

If connecting to a remote server behind a firewall:

### 3. Use Ollama Python Library

```
import ollama

client = ollama.Client(host='http://localhost:30001')

# Non-streaming
response = client.chat(
    model='Qwen/Qwen2.5-1.5B-Instruct',
    messages=[{'role': 'user', 'content': 'Hello!'}]
)
print(response['message']['content'])

# Streaming
stream = client.chat(
    model='Qwen/Qwen2.5-1.5B-Instruct',
    messages=[{'role': 'user', 'content': 'Tell me a story'}],
    stream=True
)
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

## Smart Router

For intelligent routing between local Ollama (fast) and remote SGLang (powerful) using an LLM judge, see the [Smart Router documentation](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/entrypoints/ollama/README).

## Summary

ComponentPurpose**Ollama API**Familiar CLI/API that developers already know**SGLang Backend**High-performance inference engine**Smart Router**Intelligent routing - fast local for simple tasks, powerful remote for complex tasks