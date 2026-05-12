---
title: fastokens - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/fastokens/
source: sitemap
fetched_at: 2026-05-07T21:35:40.8013104-03:00
rendered_js: false
word_count: 44
summary: This document explains how to utilize the fastokens shim to replace the internal Rust tokenizer in Hugging Face models and enable streaming detokenization.
tags:
    - fastokens
    - tokenization
    - hugging-face
    - rust-bindings
    - detokenization
    - patching
category: concept
---

`fastokens` tokenizer mode.

Loads a Hugging Face fast tokenizer whose internal Rust tokenizer is replaced by the fastokens shim. fastokens also rebinds `tokenizers.decoders.DecodeStream` so the streaming detokenizer accepts the shim. Both patches are installed for the lifetime of the process — `patch_transformers()` is idempotent.