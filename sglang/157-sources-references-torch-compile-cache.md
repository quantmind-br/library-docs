---
title: Enabling cache for torch.compile
url: https://docs.sglang.io/_sources/references/torch_compile_cache.md
source: crawler
fetched_at: 2026-02-04T08:48:29.259806392-03:00
rendered_js: false
word_count: 69
summary: This document explains how to enable and share the torch.compile cache in SGLang to speed up deployments by skipping the compilation process across multiple machines.
tags:
    - sglang
    - torch-compile
    - caching
    - deployment
    - performance-optimization
    - pytorch-inductor
category: guide
---

# Enabling cache for torch.compile

SGLang uses `max-autotune-no-cudagraphs` mode of torch.compile. The auto-tuning can be slow.
If you want to deploy a model on many different machines, you can ship the torch.compile cache to these machines and skip the compilation steps.

This is based on https://pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html


1. Generate the cache by setting TORCHINDUCTOR_CACHE_DIR and running the model once.
```
TORCHINDUCTOR_CACHE_DIR=/root/inductor_root_cache python3 -m sglang.launch_server --model meta-llama/Llama-3.1-8B-Instruct --enable-torch-compile
```
2. Copy the cache folder to other machines and launch the server with `TORCHINDUCTOR_CACHE_DIR`.