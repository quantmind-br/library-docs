---
title: Speculative Decoding
url: https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf/speculative-decoding.md
source: llms
fetched_at: 2026-04-27T18:14:43.686581133-03:00
rendered_js: false
word_count: 172
summary: This document explains how to implement Speculative Decoding within llama.cpp and llama-server by utilizing a draft model. It provides examples of enabling this feature via the `--model-draft` argument for models like GLM 4.7, demonstrating commands for both `llama-cli` and `llama-server`.
tags:
    - speculative-decoding
    - llama-cpp
    - llama-server
    - draft-model
    - gguf
    - inference
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Speculative Decoding

## Speculative Decoding in llama.cpp and llama-server

Speculative decoding is enabled via the `--model-draft` argument in `llama-cli` and `llama-server`. You must have a draft model (generally smaller) that shares the same tokenizer as the target model.

## Spec Decoding for GLM 4.7

### Download models

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/GLM-4.7-GGUF",
    local_dir = "unsloth/GLM-4.7-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*"], # Dynamic 2bit Use "*UD-TQ1_0*" for Dynamic 1bit
)
snapshot_download(
    repo_id = "unsloth/GLM-4.5-Air-GGUF",
    local_dir = "unsloth/GLM-4.5-Air-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"], # Dynamic 4bit. Use "*UD-TQ1_0*" for Dynamic 1bit
)
```

### llama-cli (no draft — baseline)

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --threads -1 \
    --fit on \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --jinja
```

### llama-cli (with speculative decoding)

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --model-draft unsloth/GLM-4.5-Air-GGUF/UD-Q4_K_XL/GLM-4.5-Air-UD-Q4_K_XL-00001-of-00002.gguf \
    --threads -1 \
    --fit on \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --ctx-size-draft 16384 \
    --jinja \
    --device CUDA0 \
    --device-draft CUDA0,CUDA1
```

### llama-server (no draft)

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --alias "unsloth/GLM-4.7" \
    --threads -1 \
    --fit on \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

#speculative-decoding #llama-cpp #gguf #inference
