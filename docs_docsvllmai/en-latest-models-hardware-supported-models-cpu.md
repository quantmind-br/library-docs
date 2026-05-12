---
title: CPU - Intel® Xeon® - vLLM
url: https://docs.vllm.ai/en/latest/models/hardware_supported_models/cpu/
source: sitemap
fetched_at: 2026-05-07T21:14:58.445520793-03:00
rendered_js: false
word_count: 83
summary: This document lists the validated CPU hardware and recommended language models that are supported and optimized for use with the vLLM project.
tags:
    - vllm
    - cpu-support
    - hardware-validation
    - language-models
    - model-compatibility
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/hardware_supported_models/cpu.md "Edit this page")

## Validated Hardware[¶](#validated-hardware "Permanent link")

Hardware [Intel® Xeon® 6 Processors](https://www.intel.com/content/www/us/en/products/details/processors/xeon.html) [Intel® Xeon® 5 Processors](https://www.intel.com/content/www/us/en/products/docs/processors/xeon/5th-gen-xeon-scalable-processors.html)

## Recommended Models[¶](#recommended-models "Permanent link")

### Text-only Language Models[¶](#text-only-language-models "Permanent link")

Model Architecture Supported meta-llama/Llama-3.1-8B-Instruct LlamaForCausalLM ✅ meta-llama/Llama-3.2-3B-Instruct LlamaForCausalLM ✅ ibm-granite/granite-3.2-2b-instruct GraniteForCausalLM ✅ Qwen/Qwen3-1.7B Qwen3ForCausalLM ✅ Qwen/Qwen3-4B Qwen3ForCausalLM ✅ Qwen/Qwen3-8B Qwen3ForCausalLM ✅ zai-org/glm-4-9b-hf GLMForCausalLM ✅ google/gemma-7b GemmaForCausalLM ✅

### Multimodal Language Models[¶](#multimodal-language-models "Permanent link")

Model Architecture Supported Qwen/Qwen2.5-VL-7B-Instruct Qwen2VLForConditionalGeneration ✅ openai/whisper-large-v3 WhisperForConditionalGeneration ✅

✅ Runs and optimized.  
🟨 Runs and correct but not optimized to green yet.  
❌ Does not pass accuracy test or does not run.