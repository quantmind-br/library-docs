---
title: Server Arguments - SGLang Documentation
url: https://docs.sglang.io/cookbook/base/reference/server_arguments
source: sitemap
fetched_at: 2026-05-11T05:50:03.553114708-03:00
rendered_js: false
word_count: 77
summary: This document outlines the parallelism configuration parameters for SGLang models and defines their corresponding command-line arguments for server deployment.
tags:
    - sglang
    - parallelism
    - tensor-parallelism
    - data-parallelism
    - expert-parallelism
    - model-configuration
category: reference
---

- [Quick Reference](#quick-reference)

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This guide explains the parallelism configuration fields used in SGLang model configurations and how they map to SGLang server command-line arguments.

## Quick Reference

Config FieldSGLang CLI ArgumentDescription`tp``--tp-size`, `--tensor-parallel-size`Tensor Parallelism - splits model across GPUs`dp``--dp-size`, `--data-parallel-size`Data Parallelism - runs multiple model replicas`ep``--ep-size`, `--expert-parallel-size`, `--ep`Expert Parallelism - distributes MoE experts`enable_dp_attention``--enable-dp-attention`DP for attention, TP for FFN (hybrid)