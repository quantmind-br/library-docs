---
title: Loading model weights with fastsafetensors
url: https://docs.vllm.ai/en/latest/models/extensions/fastsafetensor/
source: sitemap
fetched_at: 2026-05-07T21:14:55.328682229-03:00
rendered_js: false
word_count: 36
summary: This document explains how to enable GPU direct storage for model weight loading in vLLM by using the fastsafetensors library.
tags:
    - vllm
    - gpu-acceleration
    - model-loading
    - fastsafetensors
    - performance-optimization
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/extensions/fastsafetensor.md "Edit this page")

Using fastsafetensors library enables loading model weights to GPU memory by leveraging GPU direct storage. See [their GitHub repository](https://github.com/foundation-model-stack/fastsafetensors) for more details.

To enable this feature, use the `--load-format fastsafetensors` command-line argument