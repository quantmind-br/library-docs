---
title: Set Up Ollama for Local Models | Guides | Warp
url: https://docs.warp.dev/guides/external-tools-and-integrations/how-to-set-up-ollama
source: sitemap
fetched_at: 2026-04-29T15:06:43.985237926-03:00
rendered_js: false
word_count: 318
summary: This guide provides instructions for setting up, running, and integrating Ollama models into local development environments using the Warp terminal.
tags:
    - ollama
    - local-llm
    - warp-terminal
    - ai-integration
    - gpu-optimization
    - model-deployment
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:43.985237926-03:00
---
Ollama lets you run AI models locally with faster inference. This guide covers installing, profiling, and integrating Ollama into your local setup.

## 1. Check Your System Specs

Before running LLMs locally, confirm your hardware can handle them.

| Setup | Specs | Notes |
|-------|-------|-------|
| Mac | 64GB unified memory | Good for larger models, lower throughput |
| Windows (NVIDIA RTX 5090) | 32GB VRAM | Excellent performance, limited by VRAM |

> [!tip]
> Rule of thumb: ~1GB of VRAM per billion parameters.

## 2. Run Your First Model

```bash
ollama run gpt-oss
```

Recommended models to try:

| Model | VRAM Required | Use Case |
|-------|---------------|----------|
| GPT-OSS 20B | 16GB+ | Supports tool calling |
| Mistral 8B | 8GB+ | Faster, smaller alternative |

Compare their performance and quality side-by-side. Use Warp to monitor GPU usage and model response time.

## 3. Understanding Model Terms

| Term | Definition |
|------|------------|
| **Thinking** | Model "thinks" before answering; better for complex reasoning |
| **Function Calling** | Models can use external utilities (e.g., web search) |
| **Vision** | Can process and respond to images |
| **Embedding** | Converts text to numeric form for search or RAG pipelines |
| **Quantization** | Reduces memory use by lowering precision (e.g., 4-bit) |

## 4. Integrate Ollama into Your App

Most apps use OpenAI-compatible APIs, so integration is simple:

1. Open your app's code in Warp
2. Locate the OpenAI client initialization
3. Replace the base URL with Ollama's
4. Update your API key and model name

Warp helps you quickly locate, edit, and test the integration directly from the terminal.

## 5. Customize Model Behavior

Pull and modify a model:
```bash
ollama pull llama3
ollama show llama3 --modelfile > Modelfile
```

Save it as a custom model with new settings like temperature or system prompt:
```bash
ollama create my-custom-llama3 -f Modelfile
```

Use Warp to generate a model file automatically with a structured system prompt for your task.

#ollama #local-llm #warp-terminal #ai-integration #gpu-optimization
