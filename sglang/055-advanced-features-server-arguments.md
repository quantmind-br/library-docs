---
title: Server Arguments — SGLang
url: https://docs.sglang.io/advanced_features/server_arguments.html
source: crawler
fetched_at: 2026-02-04T08:46:45.037548851-03:00
rendered_js: false
word_count: 562
summary: This document provides a comprehensive list and explanation of command-line arguments used to configure and optimize the SGLang language model server. It covers essential deployment settings including parallelism policies, memory management, quantization, and distributed serving.
tags:
    - sglang
    - server-arguments
    - llm-deployment
    - tensor-parallelism
    - quantization
    - memory-management
    - distributed-computing
category: reference
---

## Server Arguments[#](#server-arguments "Link to this heading")

This page provides a list of server arguments used in the command line to configure the behavior and performance of the language model server during deployment. These arguments enable users to customize key aspects of the server, including model selection, parallelism policies, memory management, and optimization techniques. You can find all arguments by `python3 -m sglang.launch_server --help`

## Common launch commands[#](#common-launch-commands "Link to this heading")

- To use a configuration file, create a YAML file with your server arguments and specify it with `--config`. CLI arguments will override config file values.
  
  ```
  # Create config.yaml
  cat>config.yaml<< EOF
  model-path: meta-llama/Meta-Llama-3-8B-Instruct
  host: 0.0.0.0
  port: 30000
  tensor-parallel-size: 2
  enable-metrics: true
  log-requests: true
  EOF
  
  # Launch server with config file
  python-msglang.launch_server--configconfig.yaml
  ```
- To enable multi-GPU tensor parallelism, add `--tp 2`. If it reports the error “peer access is not supported between these two devices”, add `--enable-p2p-check` to the server launch command.
  
  ```
  python-msglang.launch_server--model-pathmeta-llama/Meta-Llama-3-8B-Instruct--tp2
  ```
- To enable multi-GPU data parallelism, add `--dp 2`. Data parallelism is better for throughput if there is enough memory. It can also be used together with tensor parallelism. The following command uses 4 GPUs in total. We recommend [SGLang Model Gateway (former Router)](https://docs.sglang.io/advanced_features/sgl_model_gateway.html) for data parallelism.
  
  ```
  python-msglang_router.launch_server--model-pathmeta-llama/Meta-Llama-3-8B-Instruct--dp2--tp2
  ```
- If you see out-of-memory errors during serving, try to reduce the memory usage of the KV cache pool by setting a smaller value of `--mem-fraction-static`. The default value is `0.9`.
  
  ```
  python-msglang.launch_server--model-pathmeta-llama/Meta-Llama-3-8B-Instruct--mem-fraction-static0.7
  ```
- See [hyperparameter tuning](https://docs.sglang.io/advanced_features/hyperparameter_tuning.html) on tuning hyperparameters for better performance.
- For docker and Kubernetes runs, you need to set up shared memory which is used for communication between processes. See `--shm-size` for docker and `/dev/shm` size update for Kubernetes manifests.
- If you see out-of-memory errors during prefill for long prompts, try to set a smaller chunked prefill size.
  
  ```
  python-msglang.launch_server--model-pathmeta-llama/Meta-Llama-3-8B-Instruct--chunked-prefill-size4096
  ```
- To enable fp8 weight quantization, add `--quantization fp8` on a fp16 checkpoint or directly load a fp8 checkpoint without specifying any arguments.
- To enable fp8 kv cache quantization, add `--kv-cache-dtype fp8_e4m3` or `--kv-cache-dtype fp8_e5m2`.
- To enable deterministic inference and batch invariant operations, add `--enable-deterministic-inference`. More details can be found in [deterministic inference document](https://docs.sglang.io/advanced_features/deterministic_inference.html).
- If the model does not have a chat template in the Hugging Face tokenizer, you can specify a [custom chat template](https://docs.sglang.io/references/custom_chat_template.html). If the tokenizer has multiple named templates (e.g., ‘default’, ‘tool\_use’), you can select one using `--hf-chat-template-name tool_use`.
- To run tensor parallelism on multiple nodes, add `--nnodes 2`. If you have two nodes with two GPUs on each node and want to run TP=4, let `sgl-dev-0` be the hostname of the first node and `50000` be an available port, you can use the following commands. If you meet deadlock, please try to add `--disable-cuda-graph`
- (Note: This feature is out of maintenance and might cause error) To enable `torch.compile` acceleration, add `--enable-torch-compile`. It accelerates small models on small batch sizes. By default, the cache path is located at `/tmp/torchinductor_root`, you can customize it using environment variable `TORCHINDUCTOR_CACHE_DIR`. For more details, please refer to [PyTorch official documentation](https://pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html) and [Enabling cache for torch.compile](https://docs.sglang.io/references/torch_compile_cache.html).
  
  ```
  # Node 0
  python-msglang.launch_server\
  --model-pathmeta-llama/Meta-Llama-3-8B-Instruct\
  --tp4\
  --dist-init-addrsgl-dev-0:50000\
  --nnodes2\
  --node-rank0
  
  # Node 1
  python-msglang.launch_server\
  --model-pathmeta-llama/Meta-Llama-3-8B-Instruct\
  --tp4\
  --dist-init-addrsgl-dev-0:50000\
  --nnodes2\
  --node-rank1
  ```

Please consult the documentation below and [server\_args.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/server_args.py) to learn more about the arguments you may provide when launching a server.

## Model and tokenizer[#](#model-and-tokenizer "Link to this heading")

## HTTP server[#](#http-server "Link to this heading")

## Quantization and data type[#](#quantization-and-data-type "Link to this heading")

## Memory and scheduling[#](#memory-and-scheduling "Link to this heading")

## Runtime options[#](#runtime-options "Link to this heading")

## Logging[#](#logging "Link to this heading")

## RequestMetricsExporter configuration[#](#requestmetricsexporter-configuration "Link to this heading")

## Data parallelism[#](#data-parallelism "Link to this heading")

## Multi-node distributed serving[#](#multi-node-distributed-serving "Link to this heading")

## Model override args[#](#model-override-args "Link to this heading")

## LoRA[#](#lora "Link to this heading")

## Kernel Backends (Attention, Sampling, Grammar, GEMM)[#](#kernel-backends-attention-sampling-grammar-gemm "Link to this heading")

## Speculative decoding[#](#speculative-decoding "Link to this heading")

## Ngram speculative decoding[#](#ngram-speculative-decoding "Link to this heading")

## Multi-layer Eagle speculative decoding[#](#multi-layer-eagle-speculative-decoding "Link to this heading")

## MoE[#](#moe "Link to this heading")

## Mamba Cache[#](#mamba-cache "Link to this heading")

## Hierarchical cache[#](#hierarchical-cache "Link to this heading")

## Hierarchical sparse attention[#](#hierarchical-sparse-attention "Link to this heading")

## LMCache[#](#lmcache "Link to this heading")

## Ktransformers[#](#ktransformers "Link to this heading")

## Diffusion LLM[#](#diffusion-llm "Link to this heading")

## Double Sparsity[#](#double-sparsity "Link to this heading")

## Offloading[#](#offloading "Link to this heading")

## Args for multi-item scoring[#](#args-for-multi-item-scoring "Link to this heading")

## Optimization/debug options[#](#optimization-debug-options "Link to this heading")

## Dynamic batch tokenizer[#](#dynamic-batch-tokenizer "Link to this heading")

## Debug tensor dumps[#](#debug-tensor-dumps "Link to this heading")

## PD disaggregation[#](#pd-disaggregation "Link to this heading")

## Encode prefill disaggregation[#](#encode-prefill-disaggregation "Link to this heading")

## Custom weight loader[#](#custom-weight-loader "Link to this heading")

## For PD-Multiplexing[#](#for-pd-multiplexing "Link to this heading")

## Configuration file support[#](#configuration-file-support "Link to this heading")

## For Multi-Modal[#](#for-multi-modal "Link to this heading")

## For checkpoint decryption[#](#for-checkpoint-decryption "Link to this heading")

## Forward hooks[#](#forward-hooks "Link to this heading")

## Deprecated arguments[#](#deprecated-arguments "Link to this heading")