---
title: kv_offload - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_offload/
source: sitemap
fetched_at: 2026-05-07T21:40:53.383673395-03:00
rendered_js: false
word_count: 24
summary: This document provides an overview of the core architectural modules and abstractions used for KV cache offloading within the vLLM v1 framework.
tags:
    - vllm
    - kv-cache
    - offloading
    - architecture
    - system-modules
category: reference
---

Modules:

Name Description `base`

Core abstractions for KV cache offloading in vLLM v1.

`cpu` `factory` `reuse_manager`

Reuse-frequency gating for CPU KV-cache offload stores.

`worker`