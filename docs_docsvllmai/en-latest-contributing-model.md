---
title: Summary - vLLM
url: https://docs.vllm.ai/en/latest/contributing/model/
source: sitemap
fetched_at: 2026-05-07T21:11:26.789207263-03:00
rendered_js: false
word_count: 150
summary: This document provides an overview and step-by-step guidance for developers interested in contributing new model implementations to the vLLM project.
tags:
    - vllm
    - model-integration
    - open-source
    - contributing
    - pytorch
    - machine-learning
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/contributing/model/README.md "Edit this page")

Important

Many decoder language models can now be automatically loaded using the [Transformers modeling backend](https://docs.vllm.ai/en/latest/models/supported_models/#transformers) without having to implement them in vLLM. See if `vllm serve <model>` works first!

vLLM models are specialized [PyTorch](https://pytorch.org/) models that take advantage of various [features](https://docs.vllm.ai/en/latest/features/#compatibility-matrix) to optimize their performance.

The complexity of integrating a model into vLLM depends heavily on the model's architecture. The process is considerably straightforward if the model shares a similar architecture with an existing model in vLLM. However, this can be more complex for models that include new operators (e.g., a new attention mechanism).

Read through these pages for a step-by-step guide:

- [Basic Model](https://docs.vllm.ai/en/latest/contributing/model/basic/)
- [Registering a Model](https://docs.vllm.ai/en/latest/contributing/model/registration/)
- [Unit Testing](https://docs.vllm.ai/en/latest/contributing/model/tests/)
- [Multi-Modal Support](https://docs.vllm.ai/en/latest/contributing/model/multimodal/)
- [Speech-to-Text Support](https://docs.vllm.ai/en/latest/contributing/model/transcription/)

Tip

If you are encountering issues while integrating your model into vLLM, feel free to open a [GitHub issue](https://github.com/vllm-project/vllm/issues) or ask on our [developer slack](https://slack.vllm.ai). We will be happy to help you out!