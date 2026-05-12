---
title: Configuration Options - vLLM
url: https://docs.vllm.ai/en/latest/configuration/
source: sitemap
fetched_at: 2026-05-07T21:11:11.048024591-03:00
rendered_js: false
word_count: 36
summary: This document outlines the hierarchy and priority levels for configuring vLLM, explaining how to manage settings through request parameters, engine arguments, and environment variables.
tags:
    - vllm
    - configuration
    - deployment
    - inference-engine
    - environment-variables
    - engine-arguments
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/configuration/README.md "Edit this page")

This section lists the most common options for running vLLM.

There are three main levels of configuration, from highest priority to lowest priority:

- [Request parameters](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#completions-api) and [input arguments](https://docs.vllm.ai/en/latest/api/#inference-parameters)
- [Engine arguments](https://docs.vllm.ai/en/latest/configuration/engine_args/)
- [Environment variables](https://docs.vllm.ai/en/latest/configuration/env_vars/)