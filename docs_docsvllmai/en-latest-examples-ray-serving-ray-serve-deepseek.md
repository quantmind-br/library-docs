---
title: Ray Serve Deepseek - vLLM
url: https://docs.vllm.ai/en/latest/examples/ray_serving/ray_serve_deepseek/
source: sitemap
fetched_at: 2026-05-07T21:13:37.009791629-03:00
rendered_js: false
word_count: 114
summary: This document provides a template and instructions for deploying DeepSeek large language models in a production environment using Ray Serve and the vLLM engine.
tags:
    - vllm
    - ray-serve
    - deepseek
    - model-deployment
    - openai-api
    - distributed-computing
    - llm-serving
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/ray_serving/ray_serve_deepseek.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/ray\_serving/ray\_serve\_deepseek.py](https://github.com/vllm-project/vllm/blob/main/examples/ray_serving/ray_serve_deepseek.py).

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Deploy DeepSeek R1 or V3 with Ray Serve LLM.

Ray Serve LLM is a scalable and production-grade model serving library built
on the Ray distributed computing framework and first-class support for the vLLM engine.

Key features:
- Automatic scaling, back-pressure, and load balancing across a Ray cluster.
- Unified multi-node multi-model deployment.
- Exposes an OpenAI-compatible HTTP API.
- Multi-LoRA support with shared base models.

Run `python3 ray_serve_deepseek.py` to launch an endpoint.

Learn more in the official Ray Serve LLM documentation:
https://docs.ray.io/en/latest/serve/llm/serving-llms.html
"""

fromrayimport serve
fromray.serve.llmimport LLMConfig, build_openai_app

llm_config = LLMConfig(
    model_loading_config={
        "model_id": "deepseek",
        # Pre-downloading the model to local storage is recommended since
        # the model is large. Set model_source="/path/to/the/model".
        "model_source": "deepseek-ai/DeepSeek-R1",
    },
    deployment_config={
        "autoscaling_config": {
            "min_replicas": 1,
            "max_replicas": 1,
        }
    },
    # Set to the node's accelerator type.
    accelerator_type="H100",
    # Customize engine arguments as required (for example, vLLM engine kwargs).
    engine_kwargs={
        "tensor_parallel_size": 8,
        "pipeline_parallel_size": 2,
        "gpu_memory_utilization": 0.92,
        "dtype": "auto",
        "max_num_seqs": 40,
        "max_model_len": 16384,
        "enable_chunked_prefill": True,
        "enable_prefix_caching": True,
        "trust_remote_code": True,
    },
)

# Deploy the application.
llm_app = build_openai_app({"llm_configs": [llm_config]})
serve.run(llm_app)
```