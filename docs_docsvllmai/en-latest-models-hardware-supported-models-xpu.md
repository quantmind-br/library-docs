---
title: XPU - Intel® GPUs - vLLM
url: https://docs.vllm.ai/en/latest/models/hardware_supported_models/xpu/
source: sitemap
fetched_at: 2026-05-07T21:14:58.999242011-03:00
rendered_js: false
word_count: 218
summary: This document lists hardware compatibility and validated support for various language models on Intel XPU architectures using the vLLM framework.
tags:
    - vllm
    - intel-xpu
    - hardware-compatibility
    - model-support
    - llm-deployment
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/hardware_supported_models/xpu.md "Edit this page")

## Validated Hardware[¶](#validated-hardware "Permanent link")

Hardware [Intel® Arc™ Pro B-Series Graphics](https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html)

## Recommended Models[¶](#recommended-models "Permanent link")

### Text-only Language Models[¶](#text-only-language-models "Permanent link")

Model Architecture FP16 Dynamic FP8 MXFP4 openai/gpt-oss-20b GPTForCausalLM ✅ openai/gpt-oss-120b GPTForCausalLM ✅ deepseek-ai/DeepSeek-R1-Distill-Llama-8B LlamaForCausalLM ✅ ✅ deepseek-ai/DeepSeek-R1-Distill-Qwen-14B QwenForCausalLM ✅ ✅ deepseek-ai/DeepSeek-R1-Distill-Qwen-32B QwenForCausalLM ✅ ✅ deepseek-ai/DeepSeek-R1-Distill-Llama-70B LlamaForCausalLM ✅ ✅ Qwen/Qwen2.5-72B-Instruct Qwen2ForCausalLM ✅ ✅ Qwen/Qwen3-14B Qwen3ForCausalLM ✅ ✅ Qwen/Qwen3-32B Qwen3ForCausalLM ✅ ✅ Qwen/Qwen3-30B-A3B Qwen3ForCausalLM ✅ ✅ Qwen/Qwen3-30B-A3B-GPTQ-Int4 Qwen3ForCausalLM ✅ ✅ Qwen/Qwen3-coder-30B-A3B-Instruct Qwen3ForCausalLM ✅ ✅ Qwen/QwQ-32B QwenForCausalLM ✅ ✅ deepseek-ai/DeepSeek-V2-Lite DeepSeekForCausalLM ✅ ✅ meta-llama/Llama-3.1-8B-Instruct LlamaForCausalLM ✅ ✅ baichuan-inc/Baichuan2-13B-Chat BaichuanForCausalLM ✅ ✅ THUDM/GLM-4-9B-chat GLMForCausalLM ✅ ✅ THUDM/CodeGeex4-All-9B CodeGeexForCausalLM ✅ ✅ chuhac/TeleChat2-35B LlamaForCausalLM (TeleChat2 based on Llama arch) ✅ ✅ 01-ai/Yi1.5-34B-Chat YiForCausalLM ✅ ✅ THUDM/CodeGeex4-All-9B CodeGeexForCausalLM ✅ ✅ deepseek-ai/DeepSeek-Coder-33B-base DeepSeekCoderForCausalLM ✅ ✅ baichuan-inc/Baichuan2-13B-Chat BaichuanForCausalLM ✅ ✅ meta-llama/Llama-2-13b-chat-hf LlamaForCausalLM ✅ ✅ THUDM/CodeGeex4-All-9B CodeGeexForCausalLM ✅ ✅ Qwen/Qwen1.5-14B-Chat QwenForCausalLM ✅ ✅ Qwen/Qwen1.5-32B-Chat QwenForCausalLM ✅ ✅

### Multimodal Language Models[¶](#multimodal-language-models "Permanent link")

Model Architecture FP16 Dynamic FP8 MXFP4 OpenGVLab/InternVL3\_5-8B InternVLForConditionalGeneration ✅ ✅ OpenGVLab/InternVL3\_5-14B InternVLForConditionalGeneration ✅ ✅ OpenGVLab/InternVL3\_5-38B InternVLForConditionalGeneration ✅ ✅ Qwen/Qwen2-VL-7B-Instruct Qwen2VLForConditionalGeneration ✅ ✅ Qwen/Qwen2.5-VL-72B-Instruct Qwen2VLForConditionalGeneration ✅ ✅ Qwen/Qwen2.5-VL-32B-Instruct Qwen2VLForConditionalGeneration ✅ ✅ THUDM/GLM-4v-9B GLM4vForConditionalGeneration ✅ ✅ openbmb/MiniCPM-V-4 MiniCPMVForConditionalGeneration ✅ ✅

### Embedding and Reranker Language Models[¶](#embedding-and-reranker-language-models "Permanent link")

Model Architecture FP16 Dynamic FP8 MXFP4 Qwen/Qwen3-Embedding-8B Qwen3ForTextEmbedding ✅ ✅ Qwen/Qwen3-Reranker-8B Qwen3ForSequenceClassification ✅ ✅

✅ Runs and optimized.  
🟨 Runs and correct but not optimized to green yet.  
❌ Does not pass accuracy test or does not run.