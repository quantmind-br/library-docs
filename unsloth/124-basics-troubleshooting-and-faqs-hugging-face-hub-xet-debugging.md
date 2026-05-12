---
title: Hugging Face Hub, XET debugging
url: https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md
source: llms
fetched_at: 2026-04-27T18:15:11.932716331-03:00
rendered_js: false
word_count: 180
summary: This document provides troubleshooting guidance for issues encountered while using Hugging Face Hub downloads with Unsloth, specifically addressing download stalls at 90-99% and rate limiting errors (429 Too Many Requests). It offers command-line flags and Python code solutions to resolve these problems.
tags:
    - huggingface-hub
    - xet-debugging
    - download-stuck
    - rate-limiting
    - unsloth
    - troubleshooting
category: guide
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Hugging Face Hub, XET Debugging

Troubleshooting for Hugging Face Hub download stalls (90-99%) and 429 rate-limit errors with Unsloth.

## Downloads Stuck at 90-99%

Cancel the stalled `hf download unsloth/*` run and retry with these env vars:

```bash
pip install -U huggingface_hub

HF_HOME=".cache_new/huggingface" \
HF_XET_CACHE=".cache_new/huggingface/xet" \
HF_HUB_CACHE=".cache_new/huggingface/hub" \
HF_XET_HIGH_PERFORMANCE=1 \
HF_XET_CHUNK_CACHE_SIZE_BYTES=0 \
HF_XET_RECONSTRUCT_WRITE_SEQUENTIALLY=0 \
HF_XET_NUM_CONCURRENT_RANGE_GETS=64 \
hf download unsloth/Qwen3-Coder-Next-GGUF \
    --local-dir unsloth/Qwen3-Coder-Next-GGUF \
    --include "*UD-Q6_K_XL*"
```

## Rate Limited / 429 Too Many Requests

**Option 1 — Use `snapshot_download`** (Unsloth sets the correct HF variables on import):

```python
import unsloth
import os

os.environ["HF_HOME"] = ".cache_new/huggingface"
os.environ["HF_XET_CACHE"] = ".cache_new/huggingface/xet"
os.environ["HF_HUB_CACHE"] = ".cache_new/huggingface/hub"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-Coder-Next-GGUF",
    local_dir = "unsloth/Qwen3-Coder-Next-GGUF",
    allow_patterns = ["*UD-Q6_K_XL*"],
)
```

**Option 2 — Add an HF token** from <https://huggingface.co/settings/tokens>:

```bash
pip install -U huggingface_hub

HF_HOME=".cache_new/huggingface" \
HF_XET_CACHE=".cache_new/huggingface/xet" \
HF_HUB_CACHE=".cache_new/huggingface/hub" \
HF_XET_HIGH_PERFORMANCE=1 \
HF_XET_CHUNK_CACHE_SIZE_BYTES=0 \
HF_XET_RECONSTRUCT_WRITE_SEQUENTIALLY=0 \
HF_XET_NUM_CONCURRENT_RANGE_GETS=64 \
    hf download unsloth/Qwen3-Coder-Next-GGUF \
    --local-dir unsloth/Qwen3-Coder-Next-GGUF \
    --include "*UD-Q6_K_XL*" \
    --token "hf_ADD_YOUR_HUGGING_FACE_TOKEN_HERE"
```

#huggingface-hub #xet-debugging #troubleshooting #rate-limiting
