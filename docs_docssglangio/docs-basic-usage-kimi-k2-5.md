---
title: Kimi-K2.5 Usage - SGLang Documentation
url: https://docs.sglang.io/docs/basic_usage/kimi_k2_5
source: sitemap
fetched_at: 2026-05-11T05:49:06.498294715-03:00
rendered_js: false
word_count: 145
summary: This document provides instructions for deploying and interacting with the Kimi-K2.5 multimodal model using the SGLang inference framework.
tags:
    - sglang
    - kimi-k2-5
    - model-deployment
    - multimodal-ai
    - inference-server
    - llm-configuration
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5) is Moonshot AI’s open-source, native multimodal, agentic MoE. It is a 1T-parameter model (32B active) with 256K context, MLA attention, and a MoonViT vision encoder, supporting both thinking and instant modes. In SGLang, Kimi-K2.5 uses the `kimi_k2` reasoning and tool-call parsers for correct thinking and tool handling.

```
Kimi-K2.5 support is in SGLang main and will land in the next release. Use the latest main or a nightly image until then.
```

Official deployment guide: [Kimi-K2.5 deployment guide](https://huggingface.co/moonshotai/Kimi-K2.5/blob/main/docs/deploy_guidance)

## Install (Latest Main)

```
uv pip install "sglang @ git+https://github.com/sgl-project/sglang.git#subdirectory=python"
# For CUDA 12:
uv pip install "nvidia-cudnn-cu12==9.16.0.29"
# For CUDA 13:
uv pip install "nvidia-cudnn-cu13==9.16.0.29"
```

## Launch Kimi-K2.5 with SGLang

Example: single node, TP8 on H200.

```
python3 -m sglang.launch_server \
  --model-path moonshotai/Kimi-K2.5 \
  --tp 8 \
  --trust-remote-code \
  --tool-call-parser kimi_k2 \
  --reasoning-parser kimi_k2
```

### Parser Requirements

- `--tool-call-parser kimi_k2`: Required for tool calling.
- `--reasoning-parser kimi_k2`: Required to parse thinking content; thinking mode is enabled by default.

## Test the Deployment

Thinking mode is enabled by default. To disable thinking (instant mode), pass `extra_body.chat_template_kwargs.thinking=false`.

```
# Thinking mode (default)
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonshotai/Kimi-K2.5",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Explain mixture-of-experts in one sentence."}
    ],
    "max_tokens": 256
  }'

# Instant mode (thinking disabled)
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonshotai/Kimi-K2.5",
    "messages": [
      {"role": "user", "content": "Give one sentence on MoE models."}
    ],
    "max_tokens": 128,
    "extra_body": {"chat_template_kwargs": {"thinking": false}}
  }'
```

## Multimodal Inputs (Image/Video)

Kimi-K2.5 is multimodal. Image inputs are supported via the OpenAI-compatible vision API. For more details, see `openai_api_vision.ipynb`.

```
# Image input (SGLang)
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonshotai/Kimi-K2.5",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "Describe this image."},
          {
            "type": "image_url",
            "image_url": {
              "url": "https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true"
            }
          }
        ]
      }
    ],
    "max_tokens": 256
  }'
```