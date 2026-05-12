---
title: How to Run models with Unsloth Studio
url: https://unsloth.ai/docs/new/studio/chat.md
source: llms
fetched_at: 2026-04-27T18:13:22.967958613-03:00
rendered_js: false
word_count: 1071
summary: This document provides a guide to using Unsloth Studio, detailing its capabilities for running AI models entirely offline across various operating systems and hardware setups.
tags:
    - ai-studio
    - llm-models
    - offline-inference
    - gguf
    - tool-calling
    - multimodal
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# How to Run Models with Unsloth Studio

[[097-new-studio|Unsloth Studio]] runs AI models 100% offline. Supports GGUF, safetensors, LoRA adapters, and more from Hugging Face or local files.

- Works on **all MacOS, CPU, Windows, Linux, WSL** setups -- no GPU required
- Search + Download + Run any model (GGUFs, LoRA adapters, safetensors)
- [[#model-arena|Compare]] two models side-by-side
- [[#auto-healing-tool-calling|Self-healing tool calling]] / web search, [[#code-execution|code execution]], OpenAI-compatible APIs
- [[#auto-parameter-tuning|Auto inference parameter tuning]] (temp, top-p, etc.) and edit chat templates
- Upload images, audio, PDFs, code, DOCX as chat context

## Search and Run Models

Search/download any model via Hugging Face or use local files. Supports GGUF, vision-language, and text-to-speech models. Run latest models like [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5) or NVIDIA [Nemotron 3](https://unsloth.ai/docs/models/nemotron-3).

Upload images, audio, PDFs, code, DOCX and more as chat context.

> [!success] Auto works on multi-GPU setups for inference.

## Code Execution

LLMs run Bash and Python (not just JavaScript). Sandboxed like Claude Artifacts -- models can test code, generate files, and verify answers with real computation. Produces more reliable and accurate answers.

## Auto-healing Tool Calling

Tool calling and web search with auto-fix for any errors -- inference outputs always have working tool calls. Example: Qwen3.5-4B searched 20+ websites and cited sources with web search inside its thinking trace.

## Auto Parameter Tuning

Inference parameters (temperature, top-p, top-k) auto-preset for new models like Qwen3.5. Manual adjustment and system prompt editing available. llama.cpp's smart auto context uses only needed context without loading extra.

## Chat Workspace

Enter prompts, attach documents/images (webp, png), code files, txt, or audio as context. Real-time model responses. Toggle thinking + web search on/off.

## Model Arena

Compare any two models side-by-side with the same prompt (e.g. base model vs LoRA adapter). Inference loads sequentially (parallel inference in progress). After training, compare base and fine-tuned models to evaluate fine-tuning impact.

> [!success] Auto works on multi-GPU setups for inference.

## Using Existing GGUF Models

Studio auto-detects older/pre-existing models from Hugging Face, LM Studio, etc. You can also select an existing folder for detection.

**Manual:** Studio detects models in HF Hub cache (`C:\Users\{username}\.cache\huggingface\hub`). LM Studio models at `C:\Users\{username}\.cache\lm-studio\models` OR `C:\Users\{username}\lm-studio\models` -- copy `.gguf` files to the HF cache directory for Studio to load them.

After fine-tuning, export to GGUF and run local inference with llama.cpp directly in Studio Chat. Powered by llama.cpp and Hugging Face.

## Adding Files as Context

Attach documents, images, or audio directly in conversation. Supports PDFs, screenshots, reference material. Files processed locally and included as model context.

## Deleting Model Files

Delete from the bin icon in model search, or remove from the HF cache directory:

- **MacOS/Linux/WSL:** `~/.cache/huggingface/hub/`
- **Windows:** `%USERPROFILE%\.cache\huggingface\hub\`

If `HF_HUB_CACHE` or `HF_HOME` is set, use that location. On Linux/WSL, `XDG_CACHE_HOME` can also change the default cache root.

## GPU Not Detected

For Docker specifically:

1. Pull latest image: `docker pull unsloth/unsloth:latest`
2. Start container with GPU access:
   - `docker run`: `--gpus all`
   - Docker Compose: `capabilities: [gpu]`
3. **Linux:** Install NVIDIA Container Toolkit.
4. **Windows:** Check `nvcc --version` matches CUDA version in `nvidia-smi`. Follow: <https://docs.docker.com/desktop/features/gpu/>

## Agent Query Endpoint

```
GET https://unsloth.ai/docs/new/studio/chat.md?ask=<question>
```

#unsloth-studio #inference #gguf #tool-calling
