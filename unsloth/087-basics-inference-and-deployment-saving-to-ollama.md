---
title: Saving to Ollama
url: https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-ollama.md
source: llms
fetched_at: 2026-04-27T18:14:47.786502675-03:00
rendered_js: false
word_count: 745
summary: Export finetuned models to Ollama via GGUF format with automatic Modelfile creation.
tags:
    - ollama-saving
    - model-exporting
    - llama-cpp
    - colab-setup
    - gguf-format
    - finetuning
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Saving to Ollama

Full tutorial: [[062-get-started-fine-tuning-llms-guide-tutorial-how-to-finetune-llama-3-and-use-in-ollama|How to Finetune Llama-3 and Use In Ollama]].

## Saving on Google Colab

Save the finetuned model as a LoRA adapter (~100MB). Optionally push to Hugging Face Hub (token from <https://huggingface.co/settings/tokens>).

After saving, reload with `FastLanguageModel` for inference directly in Colab.

## Exporting to Ollama

1. **Install Ollama** in the Colab notebook
2. **Export to GGUF** via Unsloth's built-in converter — set only the first row's `False` to `True` for `Q8_0` (8-bit). Popular alternative: `q4_k_m`. Export takes 5-10 minutes.
3. **Run Ollama** in background via `subprocess` (Colab doesn't support async calls; normally use `ollama serve`)

More on GGUF: <https://github.com/ggerganov/llama.cpp>. Manual GGUF export: <https://github.com/unslothai/unsloth/wiki#manually-saving-to-gguf>.

## Automatic Modelfile creation

Unsloth auto-generates a `Modelfile` with settings and the chat template used during finetuning. Print it to inspect.

Create the Ollama model from the Modelfile.

## Ollama Inference

Call the Ollama server running locally or in the Colab background for inference.

## Poor results after exporting to Ollama

Model works in Unsloth but produces gibberish/repeated output on Ollama.

> [!warning] Common causes
> - **Incorrect chat template** — use the SAME template used during training in Unsloth and when running in Ollama
> - **Wrong `eos token`** — causes gibberish on longer generations
> - **Unnecessary start-of-sequence token** — check if the inference engine adds/removes one
>
> **Fix:** Use conversational notebooks to force the chat template:
> - [Qwen-3 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)
> - [Gemma-3 4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb)
> - [Llama-3.2 3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb)
> - [Phi-4 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)
> - [Mistral v0.3 7B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Conversational.ipynb)
> - [More notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks)

#ollama #gguf #model-export #finetuning #colab
