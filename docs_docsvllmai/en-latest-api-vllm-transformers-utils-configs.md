---
title: configs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/
source: sitemap
fetched_at: 2026-05-07T21:36:43.71332902-03:00
rendered_js: false
word_count: 161
summary: This document outlines the purpose and directory structure for custom model configuration definitions required to support specific architectures or overrides within the vLLM framework.
tags:
    - model-configuration
    - vllm-framework
    - transformers-library
    - model-architecture
    - config-overrides
category: configuration
---

Model configs may be defined in this directory for the following reasons:

- There is no configuration file defined by HF Hub or Transformers library.
- There is a need to override the existing config to support vLLM.
- The HF model\_type isn't recognized by the Transformers library but can be mapped to an existing Transformers config, such as deepseek-ai/DeepSeek-V3.2-Exp.

Modules:

Name Description `AXK1` `arctic`

Arctic model configuration

`bagel` `cheers` `colmodernvbert`

Configuration for ColModernVBERT visual document retrieval model.

`colpali`

ColPali configuration that extends PaliGemmaConfig with embedding projection

`colqwen3`

ColQwen3 configuration that extends Qwen3VLConfig with embedding projection

`extract_hidden_states`

Config definitions for ExtractHiddenStatesModel, to be used with

`falcon`

Falcon configuration

`fireredlid` `granite4_vision` `hunyuan_vl` `hy_v3` `hyperclovax`

HyperCLOVA X model configuration.

`isaac` `jais`

JAIS configuration

`kimi_k25`

Kimi-K2.5 Model Configuration.

`lfm2_moe` `mlp_speculator` `moondream3`

Configuration for Moondream3 model.

`nemotron`

Nemotron model configuration

`nemotron_h`

NemotronH model configuration

`olmo_hybrid` `ovis` `parakeet` `qwen3_5`

Qwen3.5 model configuration

`qwen3_5_moe`

Qwen3.5-MoE model configuration

`qwen3_asr` `qwen3_next`

Qwen3-Next model configuration

`radio`

Radio vision model configuration

`speculators` `tarsier2` `ultravox`