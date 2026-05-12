---
title: Unsloth Model Catalog
url: https://unsloth.ai/docs/get-started/unsloth-model-catalog.md
source: llms
fetched_at: 2026-04-27T18:12:53.53461107-03:00
rendered_js: false
word_count: 4512
summary: Official catalog of Unsloth LLMs — Dynamic GGUF, 4-bit, 16-bit models on Hugging Face.
tags:
  - model-catalog
  - gguf
  - llm
  - unsloth
  - huggingface
  - inference
category: reference
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Model Catalog

Directory of all Unsloth [Dynamic](https://docs.unsloth.ai/basics/unsloth-dynamic-2.0-ggufs) GGUF, 4-bit, and 16-bit models on Hugging Face.

- **GGUFs** — run in [[099-new-studio-start|Unsloth Studio]], Ollama, llama.cpp
- **Instruct (4-bit)** safetensors — inference or fine-tuning via Unsloth

## GGUF + 4-bit

### New & Recommended

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| [**Qwen3.6**](https://unsloth.ai/docs/models/qwen3.6) | 27B | [link](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF) | — |
| | 35B-A3B | [link](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF) | — |
| [**Gemma 4**](https://unsloth.ai/docs/models/gemma-4) | 26B-A4B | [link](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF) | — |
| | 31B | [link](https://huggingface.co/unsloth/gemma-4-31B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-4-31B-it-unsloth-bnb-4bit) |
| | E4B | [link](https://huggingface.co/unsloth/gemma-4-E4B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-4-E4B-it-unsloth-bnb-4bit) |
| | E2B | [link](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-4-E2B-it-unsloth-bnb-4bit) |
| **Kimi** | [**K2.6**](https://unsloth.ai/docs/models/kimi-k2.6) | [link](https://huggingface.co/unsloth/Kimi-K2.6-GGUF) | — |
| [**Qwen3.5**](https://github.com/unslothai/docs/blob/main/models/qwen3.5) | 35B-A3B | [link](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF) | — |
| | 27B | [link](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF) | — |
| | 122B-A10B | [link](https://huggingface.co/unsloth/Qwen3.5-122B-A10B-GGUF) | — |
| | 0.8B | [link](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) | — |
| | 2B | [link](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF) | — |
| | 4B | [link](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF) | — |
| | 9B | [link](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF) | — |
| | 397B-A17B | [link](https://huggingface.co/unsloth/Qwen3.5-397B-A17B-GGUF) | — |
| **Qwen3** | [Coder-Next](https://unsloth.ai/docs/models/qwen3-coder-next) | [link](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF) | — |
| NVIDIA Nemotron 3 | [Super-120B-A12B](https://unsloth.ai/docs/models/nemotron-3/nemotron-3-super) | [link](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF) | [link](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4) |
| | [Nano-4B](https://unsloth.ai/docs/models/nemotron-3) | [link](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Nano-4B-GGUF) | — |
| **GLM** | [4.7-Flash](https://unsloth.ai/docs/models/glm-4.7-flash) | [link](https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF) | — |
| | [5](https://unsloth.ai/docs/models/tutorials/glm-5) | [link](https://huggingface.co/unsloth/GLM-5-GGUF) | — |
| **Kimi** | [K2.5](https://unsloth.ai/docs/models/kimi-k2.5) | [link](https://huggingface.co/unsloth/Kimi-K2.5-GGUF) | — |
| [**gpt-oss**](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune) | 120B | [link](https://huggingface.co/unsloth/gpt-oss-120b-GGUF) | [link](https://huggingface.co/unsloth/gpt-oss-120b-unsloth-bnb-4bit) |
| | 20B | [link](https://huggingface.co/unsloth/gpt-oss-20b-GGUF) | [link](https://huggingface.co/unsloth/gpt-oss-20b-unsloth-bnb-4bit) |
| **MiniMax** | [M2.5](https://unsloth.ai/docs/models/tutorials/minimax-m25) | [link](https://huggingface.co/unsloth/MiniMax-M2.5-GGUF) | — |
| NVIDIA [Nemotron 3](https://unsloth.ai/docs/models/nemotron-3) | 30B | [link](https://huggingface.co/unsloth/Nemotron-3-Nano-30B-A3B-GGUF) | — |
| [**Qwen-Image**](https://unsloth.ai/docs/models/tutorials/qwen-image-2512) | 2512 | [link](https://huggingface.co/unsloth/Qwen-Image-2512-GGUF) | — |
| | Edit-2511 | [link](https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF) | — |
| [**Ministral 3**](https://unsloth.ai/docs/models/tutorials/ministral-3) | 3B | [Instruct](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-GGUF) · [Reasoning](https://huggingface.co/unsloth/Ministral-3-3B-Reasoning-2512-GGUF) | [Instruct](https://huggingface.co/unsloth/Ministral-3-14B-Instruct-2512-unsloth-bnb-4bit) · [Reasoning](https://huggingface.co/unsloth/Ministral-3-3B-Reasoning-2512-GGUF) |
| | 8B | [Instruct](https://huggingface.co/unsloth/Ministral-3-8B-Instruct-2512-GGUF) · [Reasoning](https://huggingface.co/unsloth/Ministral-3-8B-Reasoning-2512-GGUF) | [Instruct](https://huggingface.co/unsloth/Ministral-3-8B-Instruct-2512-unsloth-bnb-4bit) · [Reasoning](https://huggingface.co/unsloth/Ministral-3-8B-Reasoning-2512-unsloth-bnb-4bit) |
| | 14B | [Instruct](https://huggingface.co/unsloth/Ministral-3-14B-Instruct-2512-GGUF) · [Reasoning](https://huggingface.co/unsloth/Ministral-3-14B-Reasoning-2512-GGUF) | [Instruct](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-unsloth-bnb-4bit) · [Reasoning](https://huggingface.co/unsloth/Ministral-3-14B-Reasoning-2512-unsloth-bnb-4bit) |
| [**Devstral 2**](https://unsloth.ai/docs/models/tutorials/devstral-2) | 24B | [link](https://huggingface.co/unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF) | — |
| | 123B | [link](https://huggingface.co/unsloth/Devstral-2-123B-Instruct-2512-GGUF) | — |
| **Mistral Large 3** | 675B | [link](https://huggingface.co/unsloth/Mistral-Large-3-675B-Instruct-2512-GGUF) | [link](https://huggingface.co/unsloth/Mistral-Large-3-675B-Instruct-2512-NVFP4) |
| [**Qwen3-Next**](https://unsloth.ai/docs/models/tutorials/qwen3-next) | 80B-A3B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-Next-80B-A3B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-Next-80B-A3B-Instruct-bnb-4bit/) |
| | 80B-A3B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-Next-80B-A3B-Thinking-GGUF) | — |
| [**Qwen3-VL**](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune) | 2B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-unsloth-bnb-4bit) |
| | 2B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Thinking-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Thinking-unsloth-bnb-4bit) |
| | 4B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Instruct-unsloth-bnb-4bit) |
| | 4B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-unsloth-bnb-4bit) |
| | 8B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Instruct-unsloth-bnb-4bit) |
| | 8B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-unsloth-bnb-4bit) |
| | 30B-A3B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-30B-A3B-Instruct-GGUF) | — |
| | 30B-A3B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-30B-A3B-Thinking-GGUF) | — |
| | 32B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-32B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-32B-Instruct-unsloth-bnb-4bit) |
| | 32B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-32B-Thinking-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-32B-Thinking-unsloth-bnb-4bit) |
| | 235B-A22B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-235B-A22B-Instruct-GGUF) | — |
| | 235B-A22B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-235B-A22B-Thinking-GGUF) | — |
| [**Qwen3-2507**](https://unsloth.ai/docs/models/tutorials/qwen3-next) | 30B-A3B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF) | — |
| | 30B-A3B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF) | — |
| | 235B-A22B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF/) | — |
| [**Qwen3-Coder**](https://unsloth.ai/docs/models/tutorials/qwen3-coder-how-to-run-locally) | 30B-A3B | [link](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF) | — |
| [**GLM**](https://unsloth.ai/docs/models/tutorials/glm-4.6-how-to-run-locally) | 4.7 | [link](https://huggingface.co/unsloth/GLM-4.7-GGUF) | — |
| | 4.6V-Flash | [link](https://huggingface.co/unsloth/GLM-4.6V-Flash-GGUF) | — |
| [**DeepSeek-V3.1**](https://unsloth.ai/docs/models/tutorials/deepseek-v3.1-how-to-run-locally) | Terminus | [link](https://huggingface.co/unsloth/DeepSeek-V3.1-Terminus-GGUF) | — |
| | V3.1 | [link](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF) | — |
| **Granite-4.0** | H-Small | [link](https://huggingface.co/unsloth/granite-4.0-h-small-GGUF) | [link](https://huggingface.co/unsloth/granite-4.0-h-small-unsloth-bnb-4bit) |
| **Kimi-K2** | Thinking | [link](https://huggingface.co/unsloth/Kimi-K2-Thinking-GGUF) | — |
| | 0905 | [link](https://huggingface.co/unsloth/Kimi-K2-Instruct-0905-GGUF) | — |

### DeepSeek

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| **DeepSeek-V3.1** | Terminus | [link](https://huggingface.co/unsloth/DeepSeek-V3.1-Terminus-GGUF) | |
| | V3.1 | [link](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF) | |
| **DeepSeek-V3** | V3-0324 | [link](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF) | — |
| | V3 | [link](https://huggingface.co/unsloth/DeepSeek-V3-GGUF) | — |
| **DeepSeek-R1** | R1-0528 | [link](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF) | — |
| | R1-0528-Qwen3-8B | [link](https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF) | [link](https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-unsloth-bnb-4bit) |
| | R1 | [link](https://huggingface.co/unsloth/DeepSeek-R1-GGUF) | — |
| | R1 Zero | [link](https://huggingface.co/unsloth/DeepSeek-R1-Zero-GGUF) | — |
| | Distill Llama 3 8B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-8B-GGUF) | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-8B-unsloth-bnb-4bit) |
| | Distill Llama 3.3 70B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-70B-GGUF) | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit) |
| | Distill Qwen 2.5 1.5B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF) | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B-unsloth-bnb-4bit) |
| | Distill Qwen 2.5 7B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF) | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B-unsloth-bnb-4bit) |
| | Distill Qwen 2.5 14B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B-GGUF) | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B-unsloth-bnb-4bit) |
| | Distill Qwen 2.5 32B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B-GGUF) | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B-bnb-4bit) |

### Llama

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| **Llama 4** | Scout 17B-16E | [link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit) |
| | Maverick 17B-128E | [link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF) | — |
| **Llama 3.3** | 70B | [link](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-bnb-4bit) |
| **Llama 3.2** | 1B | [link](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-bnb-4bit) |
| | 3B | [link](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-bnb-4bit) |
| | 11B Vision | — | [link](https://huggingface.co/unsloth/Llama-3.2-11B-Vision-Instruct-unsloth-bnb-4bit) |
| | 90B Vision | — | [link](https://huggingface.co/unsloth/Llama-3.2-90B-Vision-Instruct-bnb-4bit) |
| **Llama 3.1** | 8B | [link](https://huggingface.co/unsloth/Llama-3.1-8B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit) |
| | 70B | — | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-70B-Instruct-bnb-4bit) |
| | 405B | — | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-405B-Instruct-bnb-4bit) |
| **Llama 3** | 8B | — | [link](https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit) |
| | 70B | — | [link](https://huggingface.co/unsloth/llama-3-70b-bnb-4bit) |
| **Llama 2** | 7B | — | [link](https://huggingface.co/unsloth/llama-2-7b-chat-bnb-4bit) |
| | 13B | — | [link](https://huggingface.co/unsloth/llama-2-13b-bnb-4bit) |
| **CodeLlama** | 7B | — | [link](https://huggingface.co/unsloth/codellama-7b-bnb-4bit) |
| | 13B | — | [link](https://huggingface.co/unsloth/codellama-13b-bnb-4bit) |
| | 34B | — | [link](https://huggingface.co/unsloth/codellama-34b-bnb-4bit) |

### Gemma

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| **Gemma 4** | E2B | [link](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-4-E2B-it-unsloth-bnb-4bit) |
| | E4B | [link](https://huggingface.co/unsloth/gemma-4-E4B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-4-E4B-it-unsloth-bnb-4bit) |
| | 26B-A4B | [link](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF) | — |
| | 31B | [link](https://huggingface.co/unsloth/gemma-4-31B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-4-31B-it-unsloth-bnb-4bit) |
| **FunctionGemma** | 270M | [link](https://huggingface.co/unsloth/functiongemma-270m-it-GGUF) | — |
| **Gemma 3n** | E2B | [link](https://huggingface.co/unsloth/gemma-3n-E2B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-3n-E2B-it-unsloth-bnb-4bit) |
| | E4B | [link](https://huggingface.co/unsloth/gemma-3n-E4B-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-3n-E4B-it-unsloth-bnb-4bit) |
| **Gemma 3** | 270M | [link](https://huggingface.co/unsloth/gemma-3-270m-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-3-270m-it) |
| | 1B | [link](https://huggingface.co/unsloth/gemma-3-1b-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-3-1b-it-unsloth-bnb-4bit) |
| | 4B | [link](https://huggingface.co/unsloth/gemma-3-4b-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-3-4b-it-unsloth-bnb-4bit) |
| | 12B | [link](https://huggingface.co/unsloth/gemma-3-12b-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-3-12b-it-unsloth-bnb-4bit) |
| | 27B | [link](https://huggingface.co/unsloth/gemma-3-27b-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-3-27b-it-unsloth-bnb-4bit) |
| **MedGemma** | 4B (vision) | [link](https://huggingface.co/unsloth/medgemma-4b-it-GGUF) | [link](https://huggingface.co/unsloth/medgemma-4b-it-unsloth-bnb-4bit) |
| | 27B (vision) | [link](https://huggingface.co/unsloth/medgemma-27b-it-GGUF) | [link](https://huggingface.co/unsloth/medgemma-27b-text-it-unsloth-bnb-4bit) |
| **Gemma 2** | 2B | [link](https://huggingface.co/unsloth/gemma-2-it-GGUF) | [link](https://huggingface.co/unsloth/gemma-2-2b-it-bnb-4bit) |
| | 9B | — | [link](https://huggingface.co/unsloth/gemma-2-9b-it-bnb-4bit) |
| | 27B | — | [link](https://huggingface.co/unsloth/gemma-2-27b-it-bnb-4bit) |

### Qwen

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| [**Qwen3.6**](https://unsloth.ai/docs/models/qwen3.6) | 27B | [link](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF) | — |
| | 35B-A3B | [link](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF) | — |
| [**Qwen3.5**](https://github.com/unslothai/docs/blob/main/models/qwen3.5) | 35B-A3B | [link](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF) | — |
| | 27B | [link](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF) | — |
| | 122B-A10B | [link](https://huggingface.co/unsloth/Qwen3.5-122B-A10B-GGUF) | — |
| | 0.8B | [link](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) | — |
| | 2B | [link](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF) | — |
| | 4B | [link](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF) | — |
| | 9B | [link](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF) | — |
| | 397B-A17B | [link](https://huggingface.co/unsloth/Qwen3.5-397B-A17B-GGUF) | — |
| **Qwen3** | [Coder-Next](https://unsloth.ai/docs/models/qwen3-coder-next) | [link](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF) | — |
| [**Qwen-Image**](https://unsloth.ai/docs/models/tutorials/qwen-image-2512) | 2512 | [link](https://huggingface.co/unsloth/Qwen-Image-2512-GGUF) | — |
| | Edit-2511 | [link](https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF) | — |
| [**Qwen3-VL**](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune) | 2B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-unsloth-bnb-4bit) |
| | 2B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Thinking-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-2B-Thinking-unsloth-bnb-4bit) |
| | 4B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Instruct-unsloth-bnb-4bit) |
| | 4B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-unsloth-bnb-4bit) |
| | 8B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Instruct-unsloth-bnb-4bit) |
| | 8B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-unsloth-bnb-4bit) |
| **Qwen3-Coder** | 30B-A3B | [link](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF) | — |
| | 480B-A35B | [link](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF) | — |
| [**Qwen3-2507**](https://unsloth.ai/docs/models/tutorials/qwen3-next) | 30B-A3B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF) | — |
| | 30B-A3B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF) | — |
| | 235B-A22B-Thinking | [link](https://huggingface.co/unsloth/Qwen3-235B-A22B-Thinking-2507-GGUF/) | — |
| | 235B-A22B-Instruct | [link](https://huggingface.co/unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF/) | — |
| **Qwen 3** | 0.6B | [link](https://huggingface.co/unsloth/Qwen3-0.6B-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-0.6B-unsloth-bnb-4bit) |
| | 1.7B | [link](https://huggingface.co/unsloth/Qwen3-1.7B-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-1.7B-unsloth-bnb-4bit) |
| | 4B | [link](https://huggingface.co/unsloth/Qwen3-4B-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-4B-unsloth-bnb-4bit) |
| | 8B | [link](https://huggingface.co/unsloth/Qwen3-8B-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-8B-unsloth-bnb-4bit) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen3-14B-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-14B-unsloth-bnb-4bit) |
| | 30B-A3B | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-bnb-4bit) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen3-32B-GGUF) | [link](https://huggingface.co/unsloth/Qwen3-32B-unsloth-bnb-4bit) |
| | 235B-A22B | [link](https://huggingface.co/unsloth/Qwen3-235B-A22B-GGUF) | — |
| **Qwen 2.5 Omni** | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-Omni-3B-GGUF) | — |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-Omni-7B-GGUF) | — |
| **Qwen 2.5 VL** | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-3B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-VL-3B-Instruct-unsloth-bnb-4bit) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-unsloth-bnb-4bit) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-32B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-VL-32B-Instruct-unsloth-bnb-4bit) |
| | 72B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-72B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-VL-72B-Instruct-unsloth-bnb-4bit) |
| **Qwen 2.5** | 0.5B | — | [link](https://huggingface.co/unsloth/Qwen2.5-0.5B-Instruct-bnb-4bit) |
| | 1.5B | — | [link](https://huggingface.co/unsloth/Qwen2.5-1.5B-Instruct-bnb-4bit) |
| | 3B | — | [link](https://huggingface.co/unsloth/Qwen2.5-3B-Instruct-bnb-4bit) |
| | 7B | — | [link](https://huggingface.co/unsloth/Qwen2.5-7B-Instruct-bnb-4bit) |
| | 14B | — | [link](https://huggingface.co/unsloth/Qwen2.5-14B-Instruct-bnb-4bit) |
| | 32B | — | [link](https://huggingface.co/unsloth/Qwen2.5-32B-Instruct-bnb-4bit) |
| | 72B | — | [link](https://huggingface.co/unsloth/Qwen2.5-72B-Instruct-bnb-4bit) |
| **Qwen 2.5 Coder (128K)** | 0.5B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-0.5B-Instruct-128K-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-0.5B-Instruct-bnb-4bit) |
| | 1.5B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-1.5B-Instruct-128K-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-1.5B-Instruct-bnb-4bit) |
| | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-3B-Instruct-128K-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-3B-Instruct-bnb-4bit) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-7B-Instruct-128K-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-7B-Instruct-bnb-4bit) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-14B-Instruct-128K-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-14B-Instruct-bnb-4bit) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-32B-Instruct-128K-GGUF) | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-32B-Instruct-bnb-4bit) |
| **QwQ** | 32B | [link](https://huggingface.co/unsloth/QwQ-32B-GGUF) | [link](https://huggingface.co/unsloth/QwQ-32B-unsloth-bnb-4bit) |
| **QVQ (preview)** | 72B | — | [link](https://huggingface.co/unsloth/QVQ-72B-Preview-bnb-4bit) |
| **Qwen 2 (chat)** | 1.5B | — | [link](https://huggingface.co/unsloth/Qwen2-1.5B-Instruct-bnb-4bit) |
| | 7B | — | [link](https://huggingface.co/unsloth/Qwen2-7B-Instruct-bnb-4bit) |
| | 72B | — | [link](https://huggingface.co/unsloth/Qwen2-72B-Instruct-bnb-4bit) |
| **Qwen 2 VL** | 2B | — | [link](https://huggingface.co/unsloth/Qwen2-VL-2B-Instruct-unsloth-bnb-4bit) |
| | 7B | — | [link](https://huggingface.co/unsloth/Qwen2-VL-7B-Instruct-unsloth-bnb-4bit) |
| | 72B | — | [link](https://huggingface.co/unsloth/Qwen2-VL-72B-Instruct-bnb-4bit) |

### GLM

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| **GLM** | [4.7-Flash](https://unsloth.ai/docs/models/glm-4.7-flash) | [link](https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF) | — |
| | [5](https://unsloth.ai/docs/models/tutorials/glm-5) | [link](https://huggingface.co/unsloth/GLM-5-GGUF) | — |
| | 4.6V-Flash | [link](https://huggingface.co/unsloth/GLM-4.6V-Flash-GGUF) | — |
| | 4.6 | [link](https://huggingface.co/unsloth/GLM-4.6-GGUF) | — |
| | 4.5-Air | [link](https://huggingface.co/unsloth/GLM-4.5-Air-GGUF) | — |

### Mistral

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| **Magistral** | Small (2506) | [link](https://huggingface.co/unsloth/Magistral-Small-2506-GGUF) | [link](https://huggingface.co/unsloth/Magistral-Small-2506-unsloth-bnb-4bit) |
| | Small (2509) | [link](https://huggingface.co/unsloth/Magistral-Small-2509-GGUF) | [link](https://huggingface.co/unsloth/Magistral-Small-2509-unsloth-bnb-4bit) |
| | Small (2507) | [link](https://huggingface.co/unsloth/Magistral-Small-2507-GGUF) | [link](https://huggingface.co/unsloth/Magistral-Small-2507-unsloth-bnb-4bit) |
| **Mistral Small** | 3.2-24B (2506) | [link](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506-GGUF) | [link](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506-unsloth-bnb-4bit) |
| | 3.1-24B (2503) | [link](https://huggingface.co/unsloth/Mistral-Small-3.1-24B-Instruct-2503-GGUF) | [link](https://huggingface.co/unsloth/Mistral-Small-3.1-24B-Instruct-2503-unsloth-bnb-4bit) |
| | 3-24B (2501) | [link](https://huggingface.co/unsloth/Mistral-Small-24B-Instruct-2501-GGUF) | [link](https://huggingface.co/unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit) |
| | 2409-22B | — | [link](https://huggingface.co/unsloth/Mistral-Small-Instruct-2409-bnb-4bit) |
| **Devstral** | Small-24B (2507) | [link](https://huggingface.co/unsloth/Devstral-Small-2507-GGUF) | [link](https://huggingface.co/unsloth/Devstral-Small-2507-unsloth-bnb-4bit) |
| | Small-24B (2505) | [link](https://huggingface.co/unsloth/Devstral-Small-2505-GGUF) | [link](https://huggingface.co/unsloth/Devstral-Small-2505-unsloth-bnb-4bit) |
| **Pixtral** | 12B (2409) | — | [link](https://huggingface.co/unsloth/Pixtral-12B-2409-bnb-4bit) |
| **Mistral NeMo** | 12B (2407) | [link](https://huggingface.co/unsloth/Mistral-Nemo-Instruct-2407-GGUF) | [link](https://huggingface.co/unsloth/Mistral-Nemo-Instruct-2407-bnb-4bit) |
| **Mistral Large** | 2407 | — | [link](https://huggingface.co/unsloth/Mistral-Large-Instruct-2407-bnb-4bit) |
| **Mistral 7B** | v0.3 | — | [link](https://huggingface.co/unsloth/mistral-7b-instruct-v0.3-bnb-4bit) |
| | v0.2 | — | [link](https://huggingface.co/unsloth/mistral-7b-instruct-v0.2-bnb-4bit) |
| **Mixtral** | 8x7B | — | [link](https://huggingface.co/unsloth/Mixtral-8x7B-Instruct-v0.1-unsloth-bnb-4bit) |

### Phi

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| **Phi-4** | Reasoning-plus | [link](https://huggingface.co/unsloth/Phi-4-reasoning-plus-GGUF) | [link](https://huggingface.co/unsloth/Phi-4-reasoning-plus-unsloth-bnb-4bit) |
| | Reasoning | [link](https://huggingface.co/unsloth/Phi-4-reasoning-GGUF) | [link](https://huggingface.co/unsloth/phi-4-reasoning-unsloth-bnb-4bit) |
| | Mini-Reasoning | [link](https://huggingface.co/unsloth/Phi-4-mini-reasoning-GGUF) | [link](https://huggingface.co/unsloth/Phi-4-mini-reasoning-unsloth-bnb-4bit) |
| | Phi-4 (instruct) | [link](https://huggingface.co/unsloth/phi-4-GGUF) | [link](https://huggingface.co/unsloth/phi-4-unsloth-bnb-4bit) |
| | mini (instruct) | [link](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF) | [link](https://huggingface.co/unsloth/Phi-4-mini-instruct-unsloth-bnb-4bit) |
| **Phi-3.5** | mini | — | [link](https://huggingface.co/unsloth/Phi-3.5-mini-instruct-bnb-4bit) |
| **Phi-3** | mini | — | [link](https://huggingface.co/unsloth/Phi-3-mini-4k-instruct-bnb-4bit) |
| | medium | — | [link](https://huggingface.co/unsloth/Phi-3-medium-4k-instruct-bnb-4bit) |

### Other (GLM, Orpheus, Smol, LLava, etc.)

| Model | Variant | GGUF | Instruct (4-bit) |
|---|---|---|---|
| GLM | 4.5-Air | [link](https://huggingface.co/unsloth/GLM-4.5-Air-GGUF) | — |
| | 4.5 | [4.5](https://huggingface.co/unsloth/GLM-4.5-GGUF) | — |
| | 4-32B-0414 | [4-32B-0414](https://huggingface.co/unsloth/GLM-4-32B-0414-GGUF) | — |
| **Grok 2** | 270B | [link](https://huggingface.co/unsloth/grok-2-GGUF) | — |
| **Baidu-ERNIE** | 4.5-21B-A3B-Thinking | [link](https://huggingface.co/unsloth/ERNIE-4.5-21B-A3B-Thinking-GGUF) | — |
| Hunyuan | A13B | [link](https://huggingface.co/unsloth/Hunyuan-A13B-Instruct-GGUF) | — |
| Orpheus | 0.1-ft (3B) | [link](https://app.gitbook.com/o/HpyELzcNe0topgVLGCZY/s/xhOjnexMCB3dmuQFQ2Zq/) | [link](https://huggingface.co/unsloth/orpheus-3b-0.1-ft-unsloth-bnb-4bit) |
| **LLava** | 1.5 (7B) | — | [link](https://huggingface.co/unsloth/llava-1.5-7b-hf-bnb-4bit) |
| | 1.6 Mistral (7B) | — | [link](https://huggingface.co/unsloth/llava-v1.6-mistral-7b-hf-bnb-4bit) |
| **TinyLlama** | Chat | — | [link](https://huggingface.co/unsloth/tinyllama-chat-bnb-4bit) |
| **SmolLM 2** | 135M | [link](https://huggingface.co/unsloth/SmolLM2-135M-Instruct-GGUF) | [link](https://huggingface.co/unsloth/SmolLM2-135M-Instruct-bnb-4bit) |
| | 360M | [link](https://huggingface.co/unsloth/SmolLM2-360M-Instruct-GGUF) | [link](https://huggingface.co/unsloth/SmolLM2-360M-Instruct-bnb-4bit) |
| | 1.7B | [link](https://huggingface.co/unsloth/SmolLM2-1.7B-Instruct-GGUF) | [link](https://huggingface.co/unsloth/SmolLM2-1.7B-Instruct-bnb-4bit) |
| **Zephyr-SFT** | 7B | — | [link](https://huggingface.co/unsloth/zephyr-sft-bnb-4bit) |
| **Yi** | 6B (v1.5) | — | [link](https://huggingface.co/unsloth/Yi-1.5-6B-bnb-4bit) |
| | 6B (v1.0) | — | [link](https://huggingface.co/unsloth/yi-6b-bnb-4bit) |
| | 34B (chat) | — | [link](https://huggingface.co/unsloth/yi-34b-chat-bnb-4bit) |
| | 34B (base) | — | [link](https://huggingface.co/unsloth/yi-34b-bnb-4bit) |

## Instruct 16-bit

16-bit and 8-bit instruct models for inference or fine-tuning in [[099-new-studio-start|Unsloth Studio]].

### New

| Model | Variant | Instruct (16-bit) |
|---|---|---|
| **gpt-oss** | 20b | [link](https://huggingface.co/unsloth/gpt-oss-20b) |
| | 120b | [link](https://huggingface.co/unsloth/gpt-oss-120b) |
| **Gemma 3n** | E2B | [link](https://huggingface.co/unsloth/gemma-3n-E4B-it) |
| | E4B | [link](https://huggingface.co/unsloth/gemma-3n-E2B-it) |
| **DeepSeek-R1-0528** | R1-0528-Qwen3-8B | [link](https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B) |
| | R1-0528 | [link](https://huggingface.co/unsloth/DeepSeek-R1-0528) |
| **Mistral** | Small 3.2 24B (2506) | [link](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506) |
| | Small 3.1 24B (2503) | [link](https://huggingface.co/unsloth/Mistral-Small-3.1-24B-Instruct-2503) |
| | Small 3.0 24B (2501) | [link](https://huggingface.co/unsloth/Mistral-Small-24B-Instruct-2501) |
| | Magistral Small (2506) | [link](https://huggingface.co/unsloth/Magistral-Small-2506) |
| **Qwen 3** | 0.6B | [link](https://huggingface.co/unsloth/Qwen3-0.6B) |
| | 1.7B | [link](https://huggingface.co/unsloth/Qwen3-1.7B) |
| | 4B | [link](https://huggingface.co/unsloth/Qwen3-4B) |
| | 8B | [link](https://huggingface.co/unsloth/Qwen3-8B) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen3-14B) |
| | 30B-A3B | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen3-32B) |
| | 235B-A22B | [link](https://huggingface.co/unsloth/Qwen3-235B-A22B) |
| **Llama 4** | Scout 17B-16E | [link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct) |
| | Maverick 17B-128E | [link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct) |
| **Qwen 2.5 Omni** | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-Omni-3B) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-Omni-7B) |
| **Phi-4** | Reasoning-plus | [link](https://huggingface.co/unsloth/Phi-4-reasoning-plus) |
| | Reasoning | [link](https://huggingface.co/unsloth/Phi-4-reasoning) |

### DeepSeek

| Model | Variant | Instruct (16-bit) |
|---|---|---|
| **DeepSeek-V3** | V3-0324 | [link](https://huggingface.co/unsloth/DeepSeek-V3-0324) |
| | V3 | [link](https://huggingface.co/unsloth/DeepSeek-V3) |
| **DeepSeek-R1** | R1-0528 | [link](https://huggingface.co/unsloth/DeepSeek-R1-0528) |
| | R1-0528-Qwen3-8B | [link](https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B) |
| | R1 | [link](https://huggingface.co/unsloth/DeepSeek-R1) |
| | R1 Zero | [link](https://huggingface.co/unsloth/DeepSeek-R1-Zero) |
| | Distill Llama 3 8B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-8B) |
| | Distill Llama 3.3 70B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-70B) |
| | Distill Qwen 2.5 1.5B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B) |
| | Distill Qwen 2.5 7B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B) |
| | Distill Qwen 2.5 14B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B) |
| | Distill Qwen 2.5 32B | [link](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B) |

### Llama

| Model | Variant | Instruct (16-bit) |
|---|---|---|
| **Llama 4** | Scout 17B-16E | [link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct) |
| | Maverick 17B-128E | [link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct) |
| **Llama 3.3** | 70B | [link](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct) |
| **Llama 3.2** | 1B | [link](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct) |
| | 3B | [link](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct) |
| | 11B Vision | [link](https://huggingface.co/unsloth/Llama-3.2-11B-Vision-Instruct) |
| | 90B Vision | [link](https://huggingface.co/unsloth/Llama-3.2-90B-Vision-Instruct) |
| **Llama 3.1** | 8B | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-8B-Instruct) |
| | 70B | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-70B-Instruct) |
| | 405B | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-405B-Instruct) |
| **Llama 3** | 8B | [link](https://huggingface.co/unsloth/llama-3-8b-Instruct) |
| | 70B | [link](https://huggingface.co/unsloth/llama-3-70b-Instruct) |
| **Llama 2** | 7B | [link](https://huggingface.co/unsloth/llama-2-7b-chat) |

### Gemma

| Model | Variant | Instruct (16-bit) |
|---|---|---|
| **Gemma 3n** | E2B | [link](https://huggingface.co/unsloth/gemma-3n-E4B-it) |
| | E4B | [link](https://huggingface.co/unsloth/gemma-3n-E2B-it) |
| **Gemma 3** | 1B | [link](https://huggingface.co/unsloth/gemma-3-1b-it) |
| | 4B | [link](https://huggingface.co/unsloth/gemma-3-4b-it) |
| | 12B | [link](https://huggingface.co/unsloth/gemma-3-12b-it) |
| | 27B | [link](https://huggingface.co/unsloth/gemma-3-27b-it) |
| **Gemma 2** | 2B | [link](https://huggingface.co/unsloth/gemma-2b-it) |
| | 9B | [link](https://huggingface.co/unsloth/gemma-9b-it) |
| | 27B | [link](https://huggingface.co/unsloth/gemma-27b-it) |

### Qwen

| Model | Variant | Instruct (16-bit) |
|---|---|---|
| **Qwen 3** | 0.6B | [link](https://huggingface.co/unsloth/Qwen3-0.6B) |
| | 1.7B | [link](https://huggingface.co/unsloth/Qwen3-1.7B) |
| | 4B | [link](https://huggingface.co/unsloth/Qwen3-4B) |
| | 8B | [link](https://huggingface.co/unsloth/Qwen3-8B) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen3-14B) |
| | 30B-A3B | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen3-32B) |
| | 235B-A22B | [link](https://huggingface.co/unsloth/Qwen3-235B-A22B) |
| **Qwen 2.5 Omni** | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-Omni-3B) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-Omni-7B) |
| **Qwen 2.5 VL** | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-3B-Instruct) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-32B-Instruct) |
| | 72B | [link](https://huggingface.co/unsloth/Qwen2.5-VL-72B-Instruct) |
| **Qwen 2.5** | 0.5B | [link](https://huggingface.co/unsloth/Qwen2.5-0.5B-Instruct) |
| | 1.5B | [link](https://huggingface.co/unsloth/Qwen2.5-1.5B-Instruct) |
| | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-3B-Instruct) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-7B-Instruct) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen2.5-14B-Instruct) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen2.5-32B-Instruct) |
| | 72B | [link](https://huggingface.co/unsloth/Qwen2.5-72B-Instruct) |
| **Qwen 2.5 Coder 128K** | 0.5B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-0.5B-Instruct-128K) |
| | 1.5B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-1.5B-Instruct-128K) |
| | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-3B-Instruct-128K) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-7B-Instruct-128K) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-14B-Instruct-128K) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen2.5-Coder-32B-Instruct-128K) |
| **QwQ** | 32B | [link](https://huggingface.co/unsloth/QwQ-32B) |
| **QVQ (preview)** | 72B | — |
| **Qwen 2 (Chat)** | 1.5B | [link](https://huggingface.co/unsloth/Qwen2-1.5B-Instruct) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2-7B-Instruct) |
| | 72B | [link](https://huggingface.co/unsloth/Qwen2-72B-Instruct) |
| **Qwen 2 VL** | 2B | [link](https://huggingface.co/unsloth/Qwen2-VL-2B-Instruct) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2-VL-7B-Instruct) |
| | 72B | [link](https://huggingface.co/unsloth/Qwen2-VL-72B-Instruct) |

### Mistral

| Model | Variant | Instruct (16-bit) |
|---|---|---|
| **Mistral** | Small 2409-22B | [link](https://huggingface.co/unsloth/Mistral-Small-Instruct-2409) |
| | Large 2407 | [link](https://huggingface.co/unsloth/Mistral-Large-Instruct-2407) |
| | 7B v0.3 | [link](https://huggingface.co/unsloth/mistral-7b-instruct-v0.3) |
| | 7B v0.2 | [link](https://huggingface.co/unsloth/mistral-7b-instruct-v0.2) |
| **Pixtral** | 12B 2409 | [link](https://huggingface.co/unsloth/Pixtral-12B-2409) |
| **Mixtral** | 8x7B | [link](https://huggingface.co/unsloth/Mixtral-8x7B-Instruct-v0.1) |
| **Mistral NeMo** | 12B 2407 | [link](https://huggingface.co/unsloth/Mistral-Nemo-Instruct-2407) |
| **Devstral** | Small 2505 | [link](https://huggingface.co/unsloth/Devstral-Small-2505) |

### Phi

| Model | Variant | Instruct (16-bit) |
|---|---|---|
| **Phi-4** | Reasoning-plus | [link](https://huggingface.co/unsloth/Phi-4-reasoning-plus) |
| | Reasoning | [link](https://huggingface.co/unsloth/Phi-4-reasoning) |
| | Phi-4 (core) | [link](https://huggingface.co/unsloth/Phi-4) |
| | Mini-Reasoning | [link](https://huggingface.co/unsloth/Phi-4-mini-reasoning) |
| | Mini | [link](https://huggingface.co/unsloth/Phi-4-mini) |
| **Phi-3.5** | Mini | [link](https://huggingface.co/unsloth/Phi-3.5-mini-instruct) |
| **Phi-3** | Mini | [link](https://huggingface.co/unsloth/Phi-3-mini-4k-instruct) |
| | Medium | [link](https://huggingface.co/unsloth/Phi-3-medium-4k-instruct) |

### Text-to-Speech (TTS)

| Model | Instruct (16-bit) |
|---|---|
| Orpheus-3B (v0.1 ft) | [link](https://huggingface.co/unsloth/orpheus-3b-0.1-ft) |
| Orpheus-3B (v0.1 pt) | [link](https://huggingface.co/unsloth/orpheus-3b-0.1-pretrained) |
| Sesame-CSM 1B | [link](https://huggingface.co/unsloth/csm-1b) |
| Whisper Large V3 (STT) | [link](https://huggingface.co/unsloth/whisper-large-v3) |
| Llasa-TTS 1B | [link](https://huggingface.co/unsloth/Llasa-1B) |
| Spark-TTS 0.5B | [link](https://huggingface.co/unsloth/Spark-TTS-0.5B) |
| Oute-TTS 1B | [link](https://huggingface.co/unsloth/Llama-OuteTTS-1.0-1B) |

## Base 4-bit & 16-bit

Base models for fine-tuning.

### New

| Model | Variant | Base (16-bit) | Base (4-bit) |
|---|---|---|---|
| **Gemma 3n** | E2B | [link](https://huggingface.co/unsloth/gemma-3n-E2B) | [link](https://huggingface.co/unsloth/gemma-3n-E2B-unsloth-bnb-4bit) |
| | E4B | [link](https://huggingface.co/unsloth/gemma-3n-E4B) | [link](https://huggingface.co/unsloth/gemma-3n-E4B-unsloth-bnb-4bit) |
| **Qwen 3** | 0.6B | [link](https://huggingface.co/unsloth/Qwen3-0.6B-Base) | [link](https://huggingface.co/unsloth/Qwen3-0.6B-Base-unsloth-bnb-4bit) |
| | 1.7B | [link](https://huggingface.co/unsloth/Qwen3-1.7B-Base) | [link](https://huggingface.co/unsloth/Qwen3-1.7B-Base-unsloth-bnb-4bit) |
| | 4B | [link](https://huggingface.co/unsloth/Qwen3-4B-Base) | [link](https://huggingface.co/unsloth/Qwen3-4B-Base-unsloth-bnb-4bit) |
| | 8B | [link](https://huggingface.co/unsloth/Qwen3-8B-Base) | [link](https://huggingface.co/unsloth/Qwen3-8B-Base-unsloth-bnb-4bit) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen3-14B-Base) | [link](https://huggingface.co/unsloth/Qwen3-14B-Base-unsloth-bnb-4bit) |
| | 30B-A3B | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Base) | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Base-bnb-4bit) |
| **Llama 4** | Scout 17B-16E | [link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E) | [link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit) |
| | Maverick 17B-128E | [link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E) | — |

### Llama

| Model | Variant | Base (16-bit) | Base (4-bit) |
|---|---|---|---|
| **Llama 4** | Scout 17B-16E | [link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E) | — |
| | Maverick 17B-128E | [link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E) | — |
| **Llama 3.3** | 70B | [link](https://huggingface.co/unsloth/Llama-3.3-70B) | — |
| **Llama 3.2** | 1B | [link](https://huggingface.co/unsloth/Llama-3.2-1B) | — |
| | 3B | [link](https://huggingface.co/unsloth/Llama-3.2-3B) | — |
| | 11B Vision | [link](https://huggingface.co/unsloth/Llama-3.2-11B-Vision) | — |
| | 90B Vision | [link](https://huggingface.co/unsloth/Llama-3.2-90B-Vision) | — |
| **Llama 3.1** | 8B | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-8B) | — |
| | 70B | [link](https://huggingface.co/unsloth/Meta-Llama-3.1-70B) | — |
| **Llama 3** | 8B | [link](https://huggingface.co/unsloth/llama-3-8b) | [link](https://huggingface.co/unsloth/llama-3-8b-bnb-4bit) |
| **Llama 2** | 7B | [link](https://huggingface.co/unsloth/llama-2-7b) | [link](https://huggingface.co/unsloth/llama-2-7b-bnb-4bit) |
| | 13B | [link](https://huggingface.co/unsloth/llama-2-13b) | [link](https://huggingface.co/unsloth/llama-2-13b-bnb-4bit) |

### Qwen

| Model | Variant | Base (16-bit) | Base (4-bit) |
|---|---|---|---|
| **Qwen 3** | 0.6B | [link](https://huggingface.co/unsloth/Qwen3-0.6B-Base) | [link](https://huggingface.co/unsloth/Qwen3-0.6B-Base-unsloth-bnb-4bit) |
| | 1.7B | [link](https://huggingface.co/unsloth/Qwen3-1.7B-Base) | [link](https://huggingface.co/unsloth/Qwen3-1.7B-Base-unsloth-bnb-4bit) |
| | 4B | [link](https://huggingface.co/unsloth/Qwen3-4B-Base) | [link](https://huggingface.co/unsloth/Qwen3-4B-Base-unsloth-bnb-4bit) |
| | 8B | [link](https://huggingface.co/unsloth/Qwen3-8B-Base) | [link](https://huggingface.co/unsloth/Qwen3-8B-Base-unsloth-bnb-4bit) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen3-14B-Base) | [link](https://huggingface.co/unsloth/Qwen3-14B-Base-unsloth-bnb-4bit) |
| | 30B-A3B | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Base) | [link](https://huggingface.co/unsloth/Qwen3-30B-A3B-Base-unsloth-bnb-4bit) |
| **Qwen 2.5** | 0.5B | [link](https://huggingface.co/unsloth/Qwen2.5-0.5B) | [link](https://huggingface.co/unsloth/Qwen2.5-0.5B-bnb-4bit) |
| | 1.5B | [link](https://huggingface.co/unsloth/Qwen2.5-1.5B) | [link](https://huggingface.co/unsloth/Qwen2.5-1.5B-bnb-4bit) |
| | 3B | [link](https://huggingface.co/unsloth/Qwen2.5-3B) | [link](https://huggingface.co/unsloth/Qwen2.5-3B-bnb-4bit) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2.5-7B) | [link](https://huggingface.co/unsloth/Qwen2.5-7B-bnb-4bit) |
| | 14B | [link](https://huggingface.co/unsloth/Qwen2.5-14B) | [link](https://huggingface.co/unsloth/Qwen2.5-14B-bnb-4bit) |
| | 32B | [link](https://huggingface.co/unsloth/Qwen2.5-32B) | [link](https://huggingface.co/unsloth/Qwen2.5-32B-bnb-4bit) |
| | 72B | [link](https://huggingface.co/unsloth/Qwen2.5-72B) | [link](https://huggingface.co/unsloth/Qwen2.5-72B-bnb-4bit) |
| **Qwen 2** | 1.5B | [link](https://huggingface.co/unsloth/Qwen2-1.5B) | [link](https://huggingface.co/unsloth/Qwen2-1.5B-bnb-4bit) |
| | 7B | [link](https://huggingface.co/unsloth/Qwen2-7B) | [link](https://huggingface.co/unsloth/Qwen2-7B-bnb-4bit) |

### Gemma

| Model | Variant | Base (16-bit) | Base (4-bit) |
|---|---|---|---|
| **Gemma 3** | 1B | [link](https://huggingface.co/unsloth/gemma-3-1b-pt) | [link](https://huggingface.co/unsloth/gemma-3-1b-pt-unsloth-bnb-4bit) |
| | 4B | [link](https://huggingface.co/unsloth/gemma-3-4b-pt) | [link](https://huggingface.co/unsloth/gemma-3-4b-pt-unsloth-bnb-4bit) |
| | 12B | [link](https://huggingface.co/unsloth/gemma-3-12b-pt) | [link](https://huggingface.co/unsloth/gemma-3-12b-pt-unsloth-bnb-4bit) |
| | 27B | [link](https://huggingface.co/unsloth/gemma-3-27b-pt) | [link](https://huggingface.co/unsloth/gemma-3-27b-pt-unsloth-bnb-4bit) |
| **Gemma 2** | 2B | [link](https://huggingface.co/unsloth/gemma-2-2b) | — |
| | 9B | [link](https://huggingface.co/unsloth/gemma-2-9b) | — |
| | 27B | [link](https://huggingface.co/unsloth/gemma-2-27b) | — |

### Mistral

| Model | Variant | Base (16-bit) | Base (4-bit) |
|---|---|---|---|
| **Mistral** | Small 24B 2501 | [link](https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501) | — |
| | NeMo 12B 2407 | [link](https://huggingface.co/unsloth/Mistral-Nemo-Base-2407) | — |
| | 7B v0.3 | [link](https://huggingface.co/unsloth/mistral-7b-v0.3) | [link](https://huggingface.co/unsloth/mistral-7b-v0.3-bnb-4bit) |
| | 7B v0.2 | [link](https://huggingface.co/unsloth/mistral-7b-v0.2) | [link](https://huggingface.co/unsloth/mistral-7b-v0.2-bnb-4bit) |
| | Pixtral 12B 2409 | [link](https://huggingface.co/unsloth/Pixtral-12B-Base-2409) | — |

### Other (TTS, TinyLlama)

| Model | Variant | Base (16-bit) | Base (4-bit) |
|---|---|---|---|
| **TinyLlama** | 1.1B (Base) | [link](https://huggingface.co/unsloth/tinyllama) | [link](https://huggingface.co/unsloth/tinyllama-bnb-4bit) |
| **Orpheus-3b** | 0.1-pretrained | [link](https://huggingface.co/unsloth/orpheus-3b-0.1-pretrained) | [link](https://huggingface.co/unsloth/orpheus-3b-0.1-pretrained-unsloth-bnb-4bit) |

## FP8

For training or serving/deployment. FP8 Dynamic = faster training + lower VRAM vs FP8 Block, slight accuracy trade-off.

| Model | Variant | FP8 (Dynamic / Block) |
|---|---|---|
| Qwen3 | Coder-Next | [Dynamic](https://huggingface.co/unsloth/Qwen3-Coder-Next-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Qwen3-Coder-Next-FP8) |
| GLM | 4.7-Flash | [Dynamic](https://huggingface.co/unsloth/GLM-4.7-Flash-FP8-Dynamic) |
| **Llama 3.3** | 70B Instruct | [Dynamic](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-FP8-Block) |
| **Llama 3.2** | 1B Base | [Dynamic](https://huggingface.co/unsloth/Llama-3.2-1B-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.2-1B-FP8-Block) |
| | 1B Instruct | [Dynamic](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-FP8-Block) |
| | 3B Base | [Dynamic](https://huggingface.co/unsloth/Llama-3.2-3B-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.2-3B-FP8-Block) |
| | 3B Instruct | [Dynamic](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-FP8-Block) |
| **Llama 3.1** | 8B Base | [Dynamic](https://huggingface.co/unsloth/Llama-3.1-8B-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.1-8B-FP8-Block) |
| | 8B Instruct | [Dynamic](https://huggingface.co/unsloth/Llama-3.1-8B-Instruct-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.1-8B-Instruct-FP8-Block) |
| | 70B Base | [Dynamic](https://huggingface.co/unsloth/Llama-3.1-70B-FP8-Dynamic) · [Block](https://huggingface.co/unsloth/Llama-3.1-70B-FP8-Block) |
| **Qwen3** | 0.6B | [FP8](https://huggingface.co/unsloth/Qwen3-0.6B-FP8) |
| | 1.7B | [FP8](https://huggingface.co/unsloth/Qwen3-1.7B-FP8) |
| | 4B | [FP8](https://huggingface.co/unsloth/Qwen3-4B-FP8) |
| | 8B | [FP8](https://huggingface.co/unsloth/Qwen3-8B-FP8) |
| | 14B | [FP8](https://huggingface.co/unsloth/Qwen3-14B-FP8) |
| | 32B | [FP8](https://huggingface.co/unsloth/Qwen3-32B-FP8) |
| | 235B-A22B | [FP8](https://huggingface.co/unsloth/Qwen3-235B-A22B-FP8) |
| **Qwen3 (2507)** | 4B Instruct | [FP8](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-FP8) |
| | 4B Thinking | [FP8](https://huggingface.co/unsloth/Qwen3-4B-Thinking-2507-FP8) |
| | 30B-A3B Instruct | [FP8](https://huggingface.co/unsloth/Qwen3-30B-A3B-Instruct-2507-FP8) |
| | 30B-A3B Thinking | [FP8](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507-FP8) |
| | 235B-A22B Instruct | [FP8](https://huggingface.co/unsloth/Qwen3-235B-A22B-Instruct-2507-FP8) |
| | 235B-A22B Thinking | [FP8](https://huggingface.co/unsloth/Qwen3-235B-A22B-Thinking-2507-FP8) |
| **Qwen3-VL** | 4B Instruct | [FP8](https://huggingface.co/unsloth/Qwen3-VL-4B-Instruct-FP8) |
| | 4B Thinking | [FP8](https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-FP8) |
| | 8B Instruct | [FP8](https://huggingface.co/unsloth/Qwen3-VL-8B-Instruct-FP8) |
| | 8B Thinking | [FP8](https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-FP8) |
| **Qwen3-Coder** | 480B-A35B Instruct | [FP8](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-FP8) |
| **Granite 4.0** | h-tiny | [FP8 Dynamic](https://huggingface.co/unsloth/granite-4.0-h-tiny-FP8-Dynamic) |
| | h-small | [FP8 Dynamic](https://huggingface.co/unsloth/granite-4.0-h-small-FP8-Dynamic) |
| **Magistral Small** | 2509 | [FP8 Dynamic](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-Dynamic) · [FP8 torchao](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-torchao) |
| **Mistral Small 3.2** | 24B Instruct-2506 | [FP8](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8) |
| **Gemma 3** | 270M-it | [FP8 Dynamic](https://huggingface.co/unsloth/gemma-3-270m-it-FP8-Dynamic) · [FP8 torchao](https://huggingface.co/unsloth/gemma-3-270m-it-torchao-FP8) |
| | 1B | [FP8](https://huggingface.co/unsloth/gemma-3-1b-it-FP8-Dynamic) |
| | 4B | [FP8](https://huggingface.co/unsloth/gemma-3-4b-it-FP8-Dynamic) |
| | 12B | [FP8](https://huggingface.co/unsloth/gemma-3-12B-it-FP8-Dynamic) |
| | 27B | [FP8](https://huggingface.co/unsloth/gemma-3-27b-it-FP8-Dynamic) |

---

> [!info] Querying this documentation
> For info not on this page, query dynamically:
> `GET https://unsloth.ai/docs/get-started/unsloth-model-catalog.md?ask=<question>`

#model-catalog #gguf #unsloth #llm #huggingface
