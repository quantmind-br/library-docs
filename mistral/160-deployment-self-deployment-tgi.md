---
title: TGI | Mistral Docs
url: https://docs.mistral.ai/deployment/self-deployment/tgi
source: crawler
fetched_at: 2026-01-29T07:34:18.715793909-03:00
rendered_js: false
word_count: 194
summary: A technical guide for deploying and serving Mistral models using the Text-Generation-Inference (TGI) toolkit.
tags:
    - TGI
    - Mistral
    - deployment
    - inference
    - LLM
category: guide
---

## Text Generation Inference

Text Generation Inference (TGI) is a toolkit for deploying and serving Large Language Models (LLMs). TGI enables high-performance text generation for the most popular open-access LLMs. Among other features, it has quantization, tensor parallelism, token streaming, continuous batching, flash attention, guidance, and more. The easiest way of getting started with TGI is using the official Docker container.

This will spawn a TGI instance exposing an OpenAI-like API, as documented in the [API section](https://docs.mistral.ai/api). Make sure to set the `HUGGING_FACE_HUB_TOKEN` environment variable to your [Hugging Face user access token](https://huggingface.co/docs/hub/security-tokens). To use Mistral models, you must first visit the corresponding model page and fill out the small form. You then automatically get access to the model. If the model does not fit in your GPU, you can also use quantization methods (AWQ, GPTQ, etc.). You can find all TGI launch options at [their documentation](https://huggingface.co/docs/text-generation-inference/en/basic_tutorials/launcher).

TGI supports the [Messages API](https://huggingface.co/docs/text-generation-inference/en/messages_api), which is compatible with Mistral and OpenAI Chat Completion API.

If you want more control over what you send to the server, you can use the `generate` endpoint. In this case, you're responsible for formatting the prompt with the correct template and stop tokens.