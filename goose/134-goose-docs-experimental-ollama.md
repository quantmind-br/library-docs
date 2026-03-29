---
title: Ollama Tool Shim | goose
url: https://block.github.io/goose/docs/experimental/ollama
source: github_pages
fetched_at: 2026-01-22T22:13:19.239626486-03:00
rendered_js: true
word_count: 189
summary: This document explains how to use the experimental Ollama tool shim to enable tool-calling capabilities for models that do not natively support them.
tags:
    - ollama
    - tool-calling
    - tool-shim
    - configuration
    - llm-integration
category: guide
---

The Ollama tool shim enables tool calling capabilities for language models that don't natively support tool calling (like DeepSeek).

Experimental Feature

Ollama tool shim is an experimental feature. Behavior and configuration may change in future releases.

The tool shim works by instructing the primary model to output json for intended tool usage, the interpretive model uses ollama structured outputs to translate the primary model's message into valid json, and then that json is translated into valid tool calls to be invoked.

#### How to use the Ollama Tool Shim[​](#how-to-use-the-ollama-tool-shim "Direct link to How to use the Ollama Tool Shim")

1. Make sure you have [Ollama](https://ollama.com/download) installed and running
2. The default interpreter model is `mistral-nemo`, if you want to proceed with this, you have to pull it from ollama server by running:
3. If you want to use a different model, make sure to pull it first from the Ollama server. Then override the default interpreter model using the `GOOSE_TOOLSHIM_OLLAMA_MODEL` environment variable. For example, to use the `llama3.2` model, run:
   
   Then,
   
   ```
   GOOSE_TOOLSHIM_OLLAMA_MODEL=llama3.2 
   ```
4. For optimal performance, run the Ollama server with an increased context length:
   
   ```
   OLLAMA_CONTEXT_LENGTH=32768 ollama serve
   ```
5. Enable the tool shim by setting the `GOOSE_TOOLSHIM` environment variable:

Start a new goose session with your tool shim preferences:

```
GOOSE_TOOLSHIM=1 GOOSE_TOOLSHIM_OLLAMA_MODEL=llama3.2 cargo run --bin goose session
```