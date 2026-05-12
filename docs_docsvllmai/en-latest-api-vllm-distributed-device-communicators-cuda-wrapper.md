---
title: cuda_wrapper - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/cuda_wrapper/
source: sitemap
fetched_at: 2026-05-07T21:17:30.783407066-03:00
rendered_js: false
word_count: 37
summary: This module provides a Python-based interface for interacting with the cudart library without requiring the compilation of external shared libraries.
tags:
    - cuda
    - python-wrapper
    - cudart
    - distributed-computing
    - vllm
category: reference
---

## vllm.distributed.device\_communicators.cuda\_wrapper [¶](#vllm.distributed.device_communicators.cuda_wrapper "Permanent link")

This file is a pure Python wrapper for the cudart library. It avoids the need to compile a separate shared library, and is convenient for use when we just need to call a few functions.