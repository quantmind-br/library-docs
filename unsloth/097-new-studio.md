---
title: Introducing Unsloth Studio
url: https://unsloth.ai/docs/new/studio.md
source: llms
fetched_at: 2026-04-27T18:13:21.193802686-03:00
rendered_js: false
word_count: 1876
summary: Unsloth Studio — open-source, no-code web UI for training, running, and exporting AI models locally.
tags:
    - ai-studio
    - local-ui
    - model-training
    - no-code
    - llm-tools
    - data-recipes
category: guide
optimized: true
optimized_at: 2026-04-27T21:22:00Z
---

# Introducing Unsloth Studio

**Unsloth Studio (Beta)** — open-source, no-code web UI for training, running, and exporting open models in one unified **local** interface.

- Run GGUF and safetensor models locally on **Mac**, Windows, Linux
- Train 500+ models 2x faster with 70% less VRAM (no accuracy loss)
- Run and train text, vision, TTS audio, embedding models

> [!note] Changelog
> For all updates, see [[128-new-changelog|Unsloth Updates]].

**Platform support:**
- **MacOS/CPU** — Chat GGUF inference and [[100-new-studio-data-recipe|Data Recipes]]. MLX training coming soon.
- No dataset needed — auto-create datasets from **PDF, CSV, JSON, DOCX, TXT** files.
- [[101-new-studio-export|Export/save]] models to GGUF, 16-bit safetensor, etc.
- [Self-healing tool calling](https://unsloth.ai/docs/new/chat#auto-healing-tool-calling) / web search + code execution
- [Auto inference parameter tuning](https://unsloth.ai/docs/new/chat#auto-parameter-tuning) and edit chat templates.

## Features

### Run models locally

[Search and run GGUF](https://unsloth.ai/docs/new/studio/chat) and safetensor models with self-healing tool calling / web search, auto inference parameter tuning, code execution (Bash + Python), APIs (soon). Upload images, docs, audio, code.

Battle models side-by-side via Model Arena. Powered by llama.cpp + Hugging Face. Supports multi-GPU inference, automatic offloading and fitting.

### Execute code + heal tool calling

LLMs run Bash and Python (not just JavaScript). Sandboxed execution like Claude Artifacts — models test code, generate files, verify answers with real computation. E.g. Qwen3.5-4B searched 20+ websites and cited sources within its thinking trace.

### No-code training

Upload PDF, CSV, JSON docs or YAML configs and start training on NVIDIA. Unsloth kernels optimize LoRA, FP8, FFT, PT across 500+ text, vision, TTS/audio and embedding models. Fine-tune LLMs like [[020-models-qwen3.5-fine-tune|Qwen3.5]] and [[017-models-nemotron-3-nemotron-3-super|Nemotron 3]]. [[093-basics-multi-gpu-training-with-unsloth|Multi-GPU]] works automatically (major upgrade coming).

### Data Recipes

[[100-new-studio-data-recipe|Data Recipes]] transforms docs into usable/synthetic datasets via graph-node workflow. Upload unstructured or structured files (PDFs, CSV, JSON). Powered by NVIDIA Nemo [Data Designer](https://github.com/NVIDIA-NeMo/DataDesigner).

### Observability

[Complete visibility](https://unsloth.ai/docs/new/start#training-progress) into training runs — track training loss, gradient norms, GPU utilization in real time. View training progress on other devices (e.g. phone).

### Export / Save models

[[101-new-studio-export|Export any model]] (including fine-tuned) to safetensors or GGUF for llama.cpp, vLLM, Ollama, LM Studio, etc. Stores training history for revisiting runs and re-exporting.

### Model Arena

[Compare 2 models](https://unsloth.ai/docs/new/chat#model-arena) (e.g. base vs fine-tuned) side-by-side. Load first GGUF/model, then second — inference loads sequentially.

### Privacy first + Secure

100% offline and local. Token-based auth with encrypted password and JWT access/refresh flows. Use pre-existing models/GGUFs from HuggingFace — [auto-detected or manual instructions](https://unsloth.ai/docs/new/chat#using-old-existing-gguf-models).

> [!warning] Beta
> This is the BETA version. Expect improvements, fixes, and new features.

## Quickstart

Works on Windows, Linux, WSL, MacOS (chat only currently).

- **CPU:** Chat inference + [[100-new-studio-data-recipe|Data Recipes]] only
- **Training:** NVIDIA (RTX 30, 40, 50, Blackwell, DGX Spark/Station) + Intel GPUs
- **Mac:** Chat + Data Recipes only; **MLX** training coming soon
- **AMD:** Chat works; train with [[051-get-started-install-amd|Unsloth Core]]. Studio support coming soon
- **Coming soon:** Apple MLX training, AMD training, multi-GPU major upgrade

Same install commands below also update.

### MacOS, Linux, WSL

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

### Windows PowerShell

```bash
irm https://unsloth.ai/install.ps1 | iex
```

#### Launch Unsloth

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

### Docker

Official image: [`unsloth/unsloth`](https://hub.docker.com/r/unsloth/unsloth) — Windows, WSL, Linux (MacOS coming soon).

```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
```

> [!tip] Faster installs
> First install now 6x faster with 50% reduced size due to precompiled llama.cpp binaries.

For install/uninstall details see [[098-new-studio-install|Unsloth Studio Installation]].

### Google Colab notebook

[Free Colab notebook](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb) — explore all features on Colab T4 GPUs. Train/run most models up to 22B params. Click 'Run all', UI pops up after install. Scroll to **Start Unsloth Studio** and click **Open Unsloth Studio**.

> [!warning] Colab link issues
> If the Studio link returns an error, disable cookies/adblocker/Mozilla or scroll below the button to access the UI.

## Workflow

1. Launch Studio from [[098-new-studio-install|install instructions]]
2. Load a model from local files or a supported integration
3. Import training data from PDFs, CSVs, or JSONL files, or build a dataset from scratch
4. Clean, refine, and expand dataset in [[100-new-studio-data-recipe|Data Recipes]]
5. Start training with recommended presets or customize config
6. Chat with trained model, compare against base model
7. [[101-new-studio-export|Save or export]] locally to your stack

Deep-dive sections: [[102-new-studio-start|Start]], [[101-new-studio-export|Export]], [[100-new-studio-data-recipe|Data Recipe]], [[099-new-studio-chat|Chat]].

## Video Tutorials

> [!warning] Videos show older Studio versions and may not reflect current UI.

- [NVIDIA: Getting started with Studio](https://www.youtube.com/watch?v=mmbkP8NARH4)
- [How to Install Unsloth Studio](https://youtu.be/1lEDuRJWHh4?si=GHaS77ZZPOGjn3GJ)

## FAQ

**Does Unsloth collect or store data?**
No usage telemetry. Only collects minimal hardware info for compatibility (GPU type, device). Runs 100% offline and locally.

**How to use an old/existing model downloaded from Hugging Face?**
Yes — pre-existing models/GGUFs are auto-detected or see [manual instructions](https://unsloth.ai/docs/new/chat#using-old-existing-gguf-models).

**Why is inference sometimes slower in Unsloth?**
Powered by llama.cpp (same speeds as other local apps). Slower if web-search, code execution, or self-healing tool-calling is enabled. If still slower with all features off, [file a GitHub issue](https://github.com/unslothai/unsloth/issues).

**Does Studio support OpenAI-compatible APIs?**
Yes for Data Recipes. Inference support in development.

**License?**
Dual-license: core Unsloth = [Apache 2.0](https://github.com/unslothai/unsloth?tab=Apache-2.0-1-ov-file); optional components (Studio UI) = [AGPL-3.0](https://github.com/unslothai/unsloth?tab=AGPL-3.0-2-ov-file).

**Does Studio only support LLMs?**
No — supports all `transformers`-compatible model families: text, multimodal, [[094-basics-text-to-speech-tts-fine-tuning|TTS]], audio, [[079-basics-embedding-finetuning|embeddings]], BERT-style.

**Can I use my own training config?**
Yes — import a YAML config and Studio pre-fills relevant settings.

**How to adjust context length?**
Not needed with llama.cpp smart auto context (loads only what you need). Manual override coming soon.

**Do I need to train models to use the UI?**
No — download any GGUF or model without fine-tuning.

### Future of Unsloth

Coming: multi-GPU, Apple Silicon/MLX, AMD support. Beta — expect announcements and improvements soon. Working with NVIDIA on multi-GPU.

#ai-studio #no-code #model-training #local-llm #gguf
