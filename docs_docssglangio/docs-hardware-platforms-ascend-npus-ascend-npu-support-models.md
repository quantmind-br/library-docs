---
title: Support Models on Ascend NPU - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/ascend-npus/ascend_npu_support_models
source: sitemap
fetched_at: 2026-05-11T05:48:33.840718991-03:00
rendered_js: false
word_count: 168
summary: This document provides a comprehensive list of large language models, multimodal models, and specialized AI models that are supported for use on Ascend NPU hardware architectures.
tags:
    - ascend-npu
    - llm-support
    - multimodal-models
    - model-compatibility
    - embedding-models
    - reward-models
category: reference
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This section describes the models supported on the Ascend NPU, including Large Language Models, Multimodal Language Models, Embedding Models, Reward Models and Rerank Models. Mainstream DeepSeek/Qwen/GLM series are included. You are welcome to enable various models based on your business requirements.

## Large Language Models

ModelsModel FamilyA2 SupportedA3 SupportedDeepSeek V3/V3.1DeepSeek✅✅DeepSeek-V3.2-W8A8DeepSeek✅✅DeepSeek-R1-0528-W8A8DeepSeek✅✅DeepSeek-V2-Lite-W8A8DeepSeek✅✅Eco-Tech/Qwen3.6-35B-A3B-w8a8Qwen3.6✅✅Eco-Tech/Qwen3.6-27B-w8a8Qwen3.6✅✅Eco-Tech/Qwen3.5-397B-A17B-w8a8-mtpQwen3.5✅✅Eco-Tech/Qwen3.5-122B-A10B-w8a8-mtpQwen3.5✅✅Eco-Tech/Qwen3.5-35B-A3B-w8a8-mtpQwen3.5✅✅Eco-Tech/Qwen3.5-27B-w8a8-mtpQwen3.5✅✅Qwen/Qwen3.5-9BQwen3.5✅✅Qwen/Qwen3.5-4BQwen3.5✅✅Qwen/Qwen3.5-0.8BQwen3.5✅✅Qwen/Qwen3-30B-A3B-Instruct-2507Qwen3✅✅Qwen/Qwen3-32BQwen3✅✅Qwen/Qwen3-0.6BQwen3✅✅Qwen3-235B-A22B-W8A8Qwen3✅✅Qwen/Qwen3-Next-80B-A3B-InstructQwen3✅✅Qwen3-Coder-480B-A35B-Instruct-w8a8-QuaRotQwen3✅✅Qwen/Qwen2.5-7B-InstructQwen2.5✅✅QWQ-32B-W8A8QWQ✅✅meta-llama/Llama-4-Scout-17B-16E-InstructLlama✅✅AI-ModelScope/Llama-3.1-8B-InstructLlama✅✅LLM-Research/llama-2-7bLlama✅✅LLM-Research/Llama-3.2-1B-InstructLlama✅✅mistralai/Mistral-7B-Instruct-v0.2Mistral✅✅google/gemma-3-4b-itGemma✅✅microsoft/Phi-4-multimodal-instructPhi✅✅allenai/OLMoE-1B-7B-0924OLMoE✅✅stabilityai/stablelm-2-1\_6bStableLM✅✅CohereForAI/c4ai-command-r-v01Command-R✅✅huihui-ai/grok-2Grok✅✅ZhipuAI/chatglm2-6bChatGLM✅✅Shanghai\_AI\_Laboratory/internlm2-7bInternLM 2✅✅LGAI-EXAONE/EXAONE-3.5-7.8B-InstructExaONE 3✅✅xverse/XVERSE-MoE-A36BXVERSE✅✅HuggingFaceTB/SmolLM-1.7BSmolLM✅✅Eco-Tech/GLM-5.1-w4a8GLM-5.1✅✅Eco-Tech/GLM-5-w4a8GLM-5✅✅ZhipuAI/glm-4-9b-chatGLM-4✅✅XiaomiMiMo/MiMo-7B-RLMiMo✅✅arcee-ai/AFM-4.5B-BaseArcee AFM-4.5B✅✅Howeee/persimmon-8b-chatPersimmon✅✅inclusionAI/Ling-liteLing✅✅ibm-granite/granite-3.1-8b-instructGranite✅✅ibm-granite/granite-3.0-3b-a800m-instructGranite MoE✅✅AI-ModelScope/dbrx-instructDBRX (Databricks)✅✅baichuan-inc/Baichuan2-13B-ChatBaichuan 2 (7B, 13B)✅✅baidu/ERNIE-4.5-21B-A3B-PTERNIE-4.5 (4.5, 4.5MoE series)✅✅OpenBMB/MiniCPM3-4BMiniCPM (v3, 4B)✅✅Eco-Tech/Kimi-K2.6-w4a8Kimi✅✅Eco-Tech/Kimi-K2.5-w4a8Kimi✅✅moonshotai/Kimi-K2-ThinkingKimi✅✅moonshotai/Kimi-Linear-48B-A3B-InstructKimi Linear (48B-A3B)✅✅eigen-ai-labs/gpt-oss-120b-bf16GPTOSS✅✅allenai/OLMo-2-1124-7B-InstructOLMo✅✅Eco-Tech/MiniMax-M2.5-w8a8-QuaRotMiniMax-M2.5✅✅cyankiwi/MiniMax-M2-BF16MiniMax-M2✅✅upstage/SOLAR-10.7B-Instruct-v1.0Solar✅✅FLM/Tele-FLMTele FLM (52B-1T)✅✅bigcode/starcoder2-7bStarCoder2✅✅arcee-ai/Trinity-MiniTrinity (Nano, Mini)✅✅OrionStarAI/Orion-14B-BaseOrion (14B)✅✅EleutherAI/gpt-j-6bGPT-J (6B)✅✅

## Multimodal Language Models

ModelsModel Family (Variants)A2 SupportedA3 SupportedQwen/Qwen2.5-VL-3B-InstructQwen2.5-VL✅✅Qwen/Qwen2.5-VL-72B-InstructQwen2.5-VL✅✅Qwen/Qwen3-VL-30B-A3B-InstructQwen3-VL✅✅Qwen/Qwen3-VL-8B-InstructQwen3-VL✅✅Qwen/Qwen3-VL-4B-InstructQwen3-VL✅✅Qwen/Qwen3-VL-235B-A22B-InstructQwen3-VL✅✅deepseek-ai/deepseek-vl2DeepSeek-VL2✅✅deepseek-ai/Janus-Pro-1BJanus-Pro (1B, 7B)✅✅deepseek-ai/Janus-Pro-7BJanus-Pro (1B, 7B)✅✅openbmb/MiniCPM-V-2\_6MiniCPM-V / MiniCPM-o✅✅openbmb/MiniCPM-o-2\_6MiniCPM-V / MiniCPM-o✅✅google/gemma-3-4b-itGemma 3 (Multimodal)✅✅mistralai/Mistral-Small-3.1-24B-Instruct-2503Mistral-Small-3.1-24B✅✅microsoft/Phi-4-multimodal-instructPhi-4-multimodal-instruct✅✅XiaomiMiMo/MiMo-VL-7B-RLMiMo-VL (7B)✅✅AI-ModelScope/llava-v1.6-34bLLaVA (v1.5 & v1.6)✅✅lmms-lab/llava-next-72bLLaVA-NeXT (8B, 72B)✅✅lmms-lab/llava-onevision-qwen2-7b-ovLLaVA-OneVision✅✅moonshotai/Kimi-VL-A3B-InstructKimi-VL (A3B)✅✅ZhipuAI/GLM-4.5VGLM-4.5V (106B)✅✅LLM-Research/Llama-3.2-11B-Vision-InstructLlama 3.2 Vision (11B)✅✅rednote-hilab/dots.ocrDotsVLM-OCR✅✅PaddlePaddle/ERNIE-4.5-VL-28B-A3B-PTErnie4.5-VL✅✅Qwen/Qwen3-Omni-30B-A3B-InstructQwen3-Omni✅✅stepfun-ai/Step3-VL-10BStep3-VL (10B)✅✅

## Diffusion language models

ModelsModel FamilyA2 SupportedA3 SupportedinclusionAI/LLaDA2.0-flashLLaDA2.0 (mini, flash)✅✅JetLM/SDAR-8B-ChatSDAR (JetLM)✅✅JetLM/SDAR-30B-A3B-ChatSDAR (JetLM)✅✅

## Embedding Models

ModelsModel FamilyA2 SupportedA3 Supportedintfloat/e5-mistral-7b-instructE5 (Llama/Mistral based)✅✅iic/gte\_Qwen2-1.5B-instructGTE-Qwen2✅✅Qwen/Qwen3-Embedding-8BQwen3-Embedding✅✅Alibaba-NLP/gme-Qwen2-VL-2B-InstructGME (Multimodal)✅✅AI-ModelScope/clip-vit-large-patch14-336CLIP✅✅BAAI/bge-large-en-v1.5BGE✅✅

## Reward Models

ModelsModel FamilyA2 SupportedA3 SupportedSkywork/Skywork-Reward-Llama-3.1-8B-v0.2Llama3.1 Reward✅✅Shanghai\_AI\_Laboratory/internlm2-7b-rewardInternLM 2 Reward✅✅Qwen/Qwen2.5-Math-RM-72BQwen2.5 Reward - Math✅✅Howeee/Qwen2.5-1.5B-apeachQwen2.5 Reward - Sequence✅✅AI-ModelScope/Skywork-Reward-Gemma-2-27B-v0.2Gemma 2-27B Reward✅✅

## Rerank Models

ModelsModel FamilyA2 SupportedA3 SupportedBAAI/bge-reranker-v2-m3BGE-Reranker✅✅Qwen/Qwen3-Reranker-8BQwen3-Reranker (decoder-only yes/no)✅✅Qwen/Qwen3-VL-Reranker-2BQwen3-VL-Reranker (multimodal yes/no)✅✅