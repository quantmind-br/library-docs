---
title: SGLang Documentation — SGLang
url: https://docs.sglang.io/
source: crawler
fetched_at: 2026-02-04T08:46:29.709871492-03:00
rendered_js: false
word_count: 418
summary: SGLang is a high-performance serving framework designed for low-latency and high-throughput inference of large language and multimodal models across various hardware setups. It provides a comprehensive suite of features for model deployment, including advanced attention mechanisms and distributed computing support.
tags:
    - llm-serving
    - inference-engine
    - multimodal-models
    - model-deployment
    - distributed-computing
    - high-performance
category: guide
---

## SGLang Documentation[#](#sglang-documentation "Link to this heading")

[Star](https://github.com/sgl-project/sglang) [Fork](https://github.com/sgl-project/sglang/fork)

SGLang is a high-performance serving framework for large language models and multimodal models. It is designed to deliver low-latency and high-throughput inference across a wide range of setups, from a single GPU to large distributed clusters. Its core features include:

- **Fast Runtime**: Provides efficient serving with RadixAttention for prefix caching, a zero-overhead CPU scheduler, prefill-decode disaggregation, speculative decoding, continuous batching, paged attention, tensor/pipeline/expert/data parallelism, structured outputs, chunked prefill, quantization (FP4/FP8/INT4/AWQ/GPTQ), and multi-LoRA batching.
- **Broad Model Support**: Supports a wide range of language models (Llama, Qwen, DeepSeek, Kimi, GLM, GPT, Gemma, Mistral, etc.), embedding models (e5-mistral, gte, mcdse), reward models (Skywork), and diffusion models (WAN, Qwen-Image), with easy extensibility for adding new models. Compatible with most Hugging Face models and OpenAI APIs.
- **Extensive Hardware Support**: Runs on NVIDIA GPUs (GB200/B300/H100/A100/Spark), AMD GPUs (MI355/MI300), Intel Xeon CPUs, Google TPUs, Ascend NPUs, and more.
- **Active Community**: SGLang is open-source and supported by a vibrant community with widespread industry adoption, powering over 400,000 GPUs worldwide.
- **RL & Post-Training Backbone**: SGLang is a proven rollout backend across the world, with native RL integrations and adoption by well-known post-training frameworks such as AReaL, Miles, slime, Tunix, verl and more.

Basic Usage

- [Sending Requests](https://docs.sglang.io/basic_usage/send_request.html)
- [OpenAI-Compatible APIs](https://docs.sglang.io/basic_usage/openai_api.html)
- [Ollama-Compatible API](https://docs.sglang.io/basic_usage/ollama_api.html)
- [Offline Engine API](https://docs.sglang.io/basic_usage/offline_engine_api.html)
- [SGLang Native APIs](https://docs.sglang.io/basic_usage/native_api.html)
- [Sampling Parameters](https://docs.sglang.io/basic_usage/sampling_params.html)
- [Popular Model Usage (DeepSeek, GPT-OSS, GLM, Llama, MiniMax, Qwen, and more)](https://docs.sglang.io/basic_usage/popular_model_usage.html)

Advanced Features

- [Server Arguments](https://docs.sglang.io/advanced_features/server_arguments.html)
- [Hyperparameter Tuning](https://docs.sglang.io/advanced_features/hyperparameter_tuning.html)
- [Attention Backend](https://docs.sglang.io/advanced_features/attention_backend.html)
- [Speculative Decoding](https://docs.sglang.io/advanced_features/speculative_decoding.html)
- [Structured Outputs](https://docs.sglang.io/advanced_features/structured_outputs.html)
- [Structured Outputs For Reasoning Models](https://docs.sglang.io/advanced_features/structured_outputs_for_reasoning_models.html)
- [Tool Parser](https://docs.sglang.io/advanced_features/tool_parser.html)
- [Reasoning Parser](https://docs.sglang.io/advanced_features/separate_reasoning.html)
- [Quantization](https://docs.sglang.io/advanced_features/quantization.html)
- [Quantized KV Cache](https://docs.sglang.io/advanced_features/quantized_kv_cache.html)
- [Expert Parallelism](https://docs.sglang.io/advanced_features/expert_parallelism.html)
- [LoRA Serving](https://docs.sglang.io/advanced_features/lora.html)
- [PD Disaggregation](https://docs.sglang.io/advanced_features/pd_disaggregation.html)
- [EPD Disaggregation](https://docs.sglang.io/advanced_features/epd_disaggregation.html)
- [Pipeline Parallelism for Long Context](https://docs.sglang.io/advanced_features/pipeline_parallelism.html)
- [Hierarchical KV Caching (HiCache)](https://docs.sglang.io/advanced_features/hicache.html)
- [Query VLM with Offline Engine](https://docs.sglang.io/advanced_features/vlm_query.html)
- [DP for Multi-Modal Encoder in SGLang](https://docs.sglang.io/advanced_features/dp_for_multi_modal_encoder.html)
- [Cuda Graph for Multi-Modal Encoder in SGLang](https://docs.sglang.io/advanced_features/cuda_graph_for_multi_modal_encoder.html)
- [SGLang Model Gateway](https://docs.sglang.io/advanced_features/sgl_model_gateway.html)
- [Deterministic Inference](https://docs.sglang.io/advanced_features/deterministic_inference.html)
- [Observability](https://docs.sglang.io/advanced_features/observability.html)
- [Checkpoint Engine Integration](https://docs.sglang.io/advanced_features/checkpoint_engine.html)
- [SGLang for RL Systems](https://docs.sglang.io/advanced_features/sglang_for_rl.html)

Supported Models

- [Large Language Models](https://docs.sglang.io/supported_models/generative_models.html)
- [Multimodal Language Models](https://docs.sglang.io/supported_models/multimodal_language_models.html)
- [Diffusion Language Models](https://docs.sglang.io/supported_models/diffusion_language_models.html)
- [Diffusion Models](https://docs.sglang.io/supported_models/diffusion_models.html)
- [Install SGLang-diffusion](https://docs.sglang.io/supported_models/diffusion_models.html#install-sglang-diffusion)
- [ROCm quickstart for sgl-diffusion](https://docs.sglang.io/supported_models/diffusion_models.html#rocm-quickstart-for-sgl-diffusion)
- [Compatibility Matrix](https://docs.sglang.io/supported_models/diffusion_models.html#compatibility-matrix)
- [SGLang diffusion CLI Inference](https://docs.sglang.io/supported_models/diffusion_models.html#sglang-diffusion-cli-inference)
- [SGLang Diffusion OpenAI API](https://docs.sglang.io/supported_models/diffusion_models.html#sglang-diffusion-openai-api)
- [Attention Backends](https://docs.sglang.io/supported_models/diffusion_models.html#attention-backends)
- [Cache-DiT Acceleration](https://docs.sglang.io/supported_models/diffusion_models.html#cache-dit-acceleration)
- [Profiling Multimodal Generation](https://docs.sglang.io/supported_models/diffusion_models.html#profiling-multimodal-generation)
- [Contributing to SGLang Diffusion](https://docs.sglang.io/supported_models/diffusion_models.html#contributing-to-sglang-diffusion)
- [How to Support New Diffusion Models](https://docs.sglang.io/supported_models/diffusion_models.html#how-to-support-new-diffusion-models)
- [Embedding Models](https://docs.sglang.io/supported_models/embedding_models.html)
- [Reward Models](https://docs.sglang.io/supported_models/reward_models.html)
- [Rerank Models](https://docs.sglang.io/supported_models/rerank_models.html)
- [Classification API](https://docs.sglang.io/supported_models/classify_models.html)
- [How to Support New Models](https://docs.sglang.io/supported_models/support_new_models.html)
- [Transformers fallback in SGLang](https://docs.sglang.io/supported_models/transformers_fallback.html)
- [Use Models From ModelScope](https://docs.sglang.io/supported_models/modelscope.html)
- [MindSpore Models](https://docs.sglang.io/supported_models/mindspore_models.html)

Developer Guide

- [Contribution Guide](https://docs.sglang.io/developer_guide/contribution_guide.html)
- [Development Guide Using Docker](https://docs.sglang.io/developer_guide/development_guide_using_docker.html)
- [Development Guide for JIT Kernels](https://docs.sglang.io/developer_guide/development_jit_kernel_guide.html)
- [Benchmark and Profiling](https://docs.sglang.io/developer_guide/benchmark_and_profiling.html)
- [Bench Serving Guide](https://docs.sglang.io/developer_guide/bench_serving.html)
- [Evaluating New Models with SGLang](https://docs.sglang.io/developer_guide/evaluating_new_models.html)

References

- [Troubleshooting and Frequently Asked Questions](https://docs.sglang.io/references/faq.html)
- [Environment Variables](https://docs.sglang.io/references/environment_variables.html)
- [Production Metrics](https://docs.sglang.io/references/production_metrics.html)
- [Production Request Tracing](https://docs.sglang.io/references/production_request_trace.html)
- [Multi-Node Deployment](https://docs.sglang.io/references/multi_node_deployment/multi_node_index.html)
- [Custom Chat Template](https://docs.sglang.io/references/custom_chat_template.html)
- [Frontend Language](https://docs.sglang.io/references/frontend/frontend_index.html)
- [Post-Training Integration](https://docs.sglang.io/references/post_training_integration.html)
- [Learn More and Join the Community](https://docs.sglang.io/references/learn_more.html)