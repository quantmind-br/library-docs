---
title: Large Language Models — SGLang
url: https://docs.sglang.io/supported_models/generative_models.html
source: crawler
fetched_at: 2026-02-04T08:47:02.198137206-03:00
rendered_js: false
word_count: 74
summary: This document provides an overview of supported large language models and instructions for launching a model server. It also explains how to verify specific model architecture compatibility within the project repository.
tags:
    - llm
    - model-serving
    - sglang
    - inference-server
    - model-support
    - deployment
category: reference
---

## Large Language Models[#](#large-language-models "Link to this heading")

These models accept text input and produce text output (e.g., chat completions). They are primarily large language models (LLMs), some with mixture-of-experts (MoE) architectures for scaling.

## Example launch Command[#](#example-launch-command "Link to this heading")

```
python3-msglang.launch_server\
--model-pathmeta-llama/Llama-3.2-1B-Instruct\ # example HF/local path
--host0.0.0.0\
--port30000\
```

## Supported models[#](#supported-models "Link to this heading")

Below the supported models are summarized in a table.

If you are unsure if a specific architecture is implemented, you can search for it via GitHub. For example, to search for `Qwen3ForCausalLM`, use the expression:

```
repo:sgl-project/sglang path:/^python\/sglang\/srt\/models\// Qwen3ForCausalLM
```

in the GitHub search bar.