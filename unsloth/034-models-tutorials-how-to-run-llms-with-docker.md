---
title: 'How to Run Local LLMs with Docker: Step-by-Step Guide'
url: https://unsloth.ai/docs/models/tutorials/how-to-run-llms-with-docker.md
source: llms
fetched_at: 2026-04-27T18:14:33.395697095-03:00
rendered_js: false
word_count: 1067
summary: 'This guide explains how users can run various Large Language Models (LLMs), including Unsloth Dynamic GGUFs, locally using Docker via two primary methods: the command-line terminal or a no-code interface in Docker Desktop. It also provides hardware requirements and quantization recommendations for optimal performance.'
tags:
    - docker-llms
    - unsloth
    - model-deployment
    - cli-tutorial
    - hardware-guide
    - gguf
category: guide
optimized: true
optimized_at: 2026-04-27T22:10:00Z
---

# How to Run Local LLMs with Docker: Step-by-Step Guide

Run any model -- including Unsloth [Dynamic GGUFs](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) -- on Mac/Windows/Linux with a single command or no code. Unsloth powers most GGUF models on [Docker Model Runner](https://github.com/docker/model-runner) (DMR), which uses `llama.cpp` under the hood.

Quick start:

```bash
docker model run ai/gpt-oss:20B
```

Or a specific Unsloth quant from Hugging Face:

```bash
docker model run hf.co/unsloth/gpt-oss-20b-GGUF:F16
```

> [!tip] Docker CE is sufficient; Docker Desktop is not required.

## Hardware Requirements

- **VRAM + RAM >= quantized model size** for best performance. Less = slower inference (~5 tokens/s if barely fits).
- Extra RAM/VRAM improves speed; extra VRAM gives biggest boost if model fits entirely.
- **Example:** gpt-oss-20b (F16) = 13.8 GB -- ensure disk space and RAM + VRAM > 13.8 GB.

**Quantization recommendations:**

| Model Size | Min Quant |
| ---------- | --------- |
| < 30B params | 4-bit (Q4) |
| >= 70B params | 2-bit (e.g., UD_Q2_K_XL) |

## Method 1: Docker Terminal

Docker Model Runner available in both [Docker Desktop](https://docs.docker.com/ai/model-runner/get-started/#docker-desktop) and [Docker CE](https://docs.docker.com/ai/model-runner/get-started/#docker-engine).

1. Browse models on [Docker Hub](https://hub.docker.com/r/ai) or [Unsloth's Hugging Face](https://huggingface.co/unsloth) page
2. Run via terminal. Docker Hub defaults to Unsloth Dynamic 4-bit.

```bash
# Docker Hub (default Unsloth 4-bit)
docker model run ai/gpt-oss:20B

# Specific Unsloth quant from Hugging Face
docker model run hf.co/unsloth/gpt-oss-20b-GGUF:UD-Q8_K_XL
```

3. To select a specific quantization, append `:` + quant name. View available quants on each model's Docker Hub page (e.g., [gpt-oss quants](https://hub.docker.com/r/ai/gpt-oss#gptoss)) or [HF page](https://huggingface.co/unsloth/gpt-oss-20b-GGUF?show_file_info=gpt-oss-20b-Q2_K_L.gguf).

```bash
docker model run hf.co/unsloth/gpt-oss-20b-GGUF:Q2_K_L
```

## Method 2: Docker Desktop (no code)

Available in [Docker Desktop](https://docs.docker.com/ai/model-runner/get-started/#docker-desktop).

1. Open Docker Desktop, click **Models** tab, then **Add models +**
2. Search [Docker Hub](https://hub.docker.com/r/ai) for the model
3. Select quantization (1-16 bits). For < 30B params, use at least 4-bit (`Q4`). Choose size that fits your hardware.
4. Wait for download, then click **Run**
5. Type prompts in the **Ask a question** box

## Running Latest Models

Any model supported by `llama.cpp` or `vllm` and available on Docker Hub can be run.

## What Is Docker Model Runner?

[Docker Model Runner (DMR)](https://github.com/docker/model-runner) is an open-source tool for pulling and running AI models like containers. Uses `llama.cpp` for hardware-efficient inference. Provides consistent runtime, avoids dependency issues, enables reproducible setups.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/how-to-run-llms-with-docker.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#docker #llm-inference #gguf #local-deployment
