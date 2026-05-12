---
title: Hierarchical KV Caching (HiCache) - SGLang Documentation
url: https://docs.sglang.io/docs/advanced_features/hicache
source: sitemap
fetched_at: 2026-05-11T05:49:32.515574106-03:00
rendered_js: false
word_count: 117
summary: This document serves as the comprehensive technical documentation for SGLang, covering basic API usage, advanced model optimization features, architecture scaling, and production deployment references.
tags:
    - sglang
    - llm-inference
    - model-optimization
    - distributed-inference
    - kv-cache
    - speculative-decoding
    - cuda-graph
category: guide
---

##### Basic Usage

- [](https://docs.sglang.io/docs/basic_usage/overview)
- [](https://docs.sglang.io/docs/basic_usage/ollama_api)
- [](https://docs.sglang.io/docs/basic_usage/offline_engine_api)
- [](https://docs.sglang.io/docs/basic_usage/native_api)
- [](https://docs.sglang.io/docs/basic_usage/sampling_params)

##### Advanced Features

- [](https://docs.sglang.io/docs/advanced_features/overview)
- [](https://docs.sglang.io/docs/advanced_features/server_arguments)
- [Loading Models from Object Storage](https://docs.sglang.io/docs/advanced_features/object_storage)
- [](https://docs.sglang.io/docs/advanced_features/hyperparameter_tuning)
- [](https://docs.sglang.io/docs/advanced_features/attention_backend)
- [HiSparse: Hierarchical Sparse Attention](https://docs.sglang.io/docs/advanced_features/hisparse_guide)
- [](https://docs.sglang.io/docs/advanced_features/speculative_decoding)
- [Adaptive Speculative Decoding](https://docs.sglang.io/docs/advanced_features/adaptive_speculative_decoding)
- [](https://docs.sglang.io/docs/advanced_features/structured_outputs)
- [Structured Outputs For Reasoning Models](https://docs.sglang.io/docs/advanced_features/structured_outputs_for_reasoning_models)
- [](https://docs.sglang.io/docs/advanced_features/tool_parser)
- [](https://docs.sglang.io/docs/advanced_features/separate_reasoning)
- [](https://docs.sglang.io/docs/advanced_features/quantization)
- [](https://docs.sglang.io/docs/advanced_features/quantized_kv_cache)
- [DP, DPA and SGLang DP Router](https://docs.sglang.io/docs/advanced_features/dp_dpa_smg_guide)
- [](https://docs.sglang.io/docs/advanced_features/expert_parallelism)
- [](https://docs.sglang.io/docs/advanced_features/lora)
- [](https://docs.sglang.io/docs/advanced_features/pd_disaggregation)
- [](https://docs.sglang.io/docs/advanced_features/epd_disaggregation)
- [Pipeline Parallelism for Long Context](https://docs.sglang.io/docs/advanced_features/pipeline_parallelism)
- - [Hierarchical KV Caching (HiCache)](https://docs.sglang.io/docs/advanced_features/hicache)
  - [SGLang HiCache Best Practices](https://docs.sglang.io/docs/advanced_features/hicache_best_practices)
  - [HiCache System Design and Optimization](https://docs.sglang.io/docs/advanced_features/hicache_design)
  - [Runtime Attach/Detach HiCache Storage Backend (No Restart)](https://docs.sglang.io/docs/advanced_features/hicache_storage_runtime_attach_detach)
- [Query VLM with Offline Engine](https://docs.sglang.io/docs/advanced_features/vlm_query)
- [DP for Multi-Modal Encoder in SGLang](https://docs.sglang.io/docs/advanced_features/dp_for_multi_modal_encoder)
- [Cuda Graph for Multi-Modal Encoder in SGLang](https://docs.sglang.io/docs/advanced_features/cuda_graph_for_multi_modal_encoder)
- [](https://docs.sglang.io/docs/advanced_features/breakable_cuda_graph)
- [](https://docs.sglang.io/docs/advanced_features/piecewise_cuda_graph)
- [](https://docs.sglang.io/docs/advanced_features/sgl_model_gateway)
- [](https://docs.sglang.io/docs/advanced_features/deterministic_inference)
- [](https://docs.sglang.io/docs/advanced_features/observability)
- [Checkpoint Engine Integration](https://docs.sglang.io/docs/advanced_features/checkpoint_engine)
- [](https://docs.sglang.io/docs/advanced_features/sglang_for_rl)

##### Supported Models

- [](https://docs.sglang.io/docs/supported-models)

##### References

- [](https://docs.sglang.io/docs/references/overview)
- [Troubleshooting and Frequently Asked Questions](https://docs.sglang.io/docs/references/faq)
- [](https://docs.sglang.io/docs/references/environment_variables)
- [](https://docs.sglang.io/docs/references/production_metrics)
- [Production Request Tracing](https://docs.sglang.io/docs/references/production_request_trace)
- [](https://docs.sglang.io/docs/references/custom_chat_template)
- [Post-Training Integration](https://docs.sglang.io/docs/references/post_training_integration)