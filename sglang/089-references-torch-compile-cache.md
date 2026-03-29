---
title: Enabling cache for torch.compile — SGLang
url: https://docs.sglang.io/references/torch_compile_cache.html
source: crawler
fetched_at: 2026-02-04T08:47:44.20641342-03:00
rendered_js: false
word_count: 69
summary: This document explains how to enable and share the torch.compile cache in SGLang to accelerate model deployment by skipping time-consuming auto-tuning steps.
tags:
    - sglang
    - torch-compile
    - inductor-cache
    - performance-optimization
    - model-deployment
category: guide
---

## Enabling cache for torch.compile[#](#enabling-cache-for-torch-compile "Link to this heading")

SGLang uses `max-autotune-no-cudagraphs` mode of torch.compile. The auto-tuning can be slow. If you want to deploy a model on many different machines, you can ship the torch.compile cache to these machines and skip the compilation steps.

This is based on https://pytorch.org/tutorials/recipes/torch\_compile\_caching\_tutorial.html

1. Generate the cache by setting TORCHINDUCTOR\_CACHE\_DIR and running the model once.

```
TORCHINDUCTOR_CACHE_DIR=/root/inductor_root_cache python3 -m sglang.launch_server --model meta-llama/Llama-3.1-8B-Instruct --enable-torch-compile
```

2. Copy the cache folder to other machines and launch the server with `TORCHINDUCTOR_CACHE_DIR`.