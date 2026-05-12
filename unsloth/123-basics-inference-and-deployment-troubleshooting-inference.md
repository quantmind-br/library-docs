---
title: Troubleshooting Inference
url: https://unsloth.ai/docs/basics/inference-and-deployment/troubleshooting-inference.md
source: llms
fetched_at: 2026-04-27T18:14:54.459390432-03:00
rendered_js: false
word_count: 410
summary: Troubleshooting model inference after exporting from Unsloth to Ollama/vLLM — chat template issues, EOS tokens, saving formats, memory management.
tags:
    - inference-troubleshooting
    - chat-template
    - model-exporting
    - ollama
    - vllm
    - safetensors
    - gguf
category: guide
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Troubleshooting Inference

## Poor Results After Exporting to Other Platforms

Model works in Unsloth but produces gibberish, infinite generations, or repeated output on Ollama/vLLM:

- **Incorrect chat template** (most common) — Must use the SAME chat template used during training in Unsloth and later in llama.cpp/Ollama.
- **Incorrect `eos token`** — Wrong EOS token causes gibberish on longer generations.
- **Unnecessary "start of sequence" token** — Inference engine may add an unwanted SoS token (or omit a required one).
- **Fix:** Use [conversational notebooks](https://github.com/unslothai/notebooks) to force the chat template:
  - [Qwen-3 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)
  - [Gemma-3 4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb)
  - [Llama-3.2 3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb)
  - [Phi-4 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)
  - [Mistral v0.3 7B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Conversational.ipynb)

## Saving to `safetensors` Instead of `bin` in Colab

Colab defaults to `.bin` (~4x faster). To force `.safetensors`:

```python
model.save_pretrained(..., safe_serialization = None)
# or
model.push_to_hub(..., safe_serialization = None)
```

## GGUF / vLLM 16bit Save Crashes (OOM)

Reduce GPU memory usage during save by lowering `maximum_memory_usage`:

```python
# Default is 0.75 (75%); reduce to 0.5 (50%) or lower
model.save_pretrained(..., maximum_memory_usage = 0.5)
```

#inference #troubleshooting #ollama #vllm #gguf
