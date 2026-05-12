---
title: main - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/main/
source: sitemap
fetched_at: 2026-05-07T21:19:35.62631162-03:00
rendered_js: false
word_count: 24
summary: This document describes the structure and module loading strategy for the vLLM command-line interface entrypoints.
tags:
    - vllm
    - cli
    - entrypoints
    - module-loading
    - python-architecture
category: reference
---

## vllm.entrypoints.cli.main [¶](#vllm.entrypoints.cli.main "Permanent link")

The CLI entrypoints of vLLM

Note that all future modules must be lazily loaded within main to avoid certain eager import breakage.