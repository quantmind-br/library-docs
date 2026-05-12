---
title: Sleep Mode - vLLM
url: https://docs.vllm.ai/en/latest/features/sleep_mode/
source: sitemap
fetched_at: 2026-05-07T21:14:17.805417625-03:00
rendered_js: false
word_count: 618
summary: This document explains how to use vLLM's sleep mode to temporarily offload model weights and KV cache to free up GPU memory without shutting down the server.
tags:
    - vllm
    - gpu-memory-management
    - inference
    - memory-optimization
    - rlhf
    - model-serving
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/sleep_mode.md "Edit this page")

vLLM's Sleep Mode allows you to temporarily release most GPU memory used by a model, including model weights and KV cache, without stopping the server or unloading the Docker container. This is especially useful for RLHF, training, or cost-saving scenarios where GPU resources need to be freed between inference workloads.

Key benefits:

- **Frees GPU memory**: Offloads model weights to CPU RAM and discards KV cache, releasing up to 90%+ of GPU memory for other tasks.
- **Fast resume**: Quickly wake up the engine and resume inference without full model reload.
- **API endpoints**: Control sleep/wake\_up state via HTTP endpoints or Python API.
- **Supports distributed workloads**: Works with tensor parallelism, pipeline parallelism, etc.
- **Fine-grained control**: Optionally wake up only model weights or KV cache to avoid OOM during weight updates.

Note

This feature is now supported on CUDA and ROCm platform.

Note

For more information, see this [Blog Post](https://blog.vllm.ai/2025/10/26/sleep-mode.html).

## Sleep levels[¶](#sleep-levels "Permanent link")

Level 1 sleep will offload the model weights and discard the KV cache. The content of KV cache is forgotten. Level 1 sleep is good for sleeping and waking up the engine to run the same model again. The model weights are backed up in CPU memory. Please make sure there's enough CPU memory to store the model weights. Level 2 sleep will discard both the model weights and the KV cache (while the model's buffers are kept in CPU, like rope scaling tensors). The content of both the model weights and KV cache is forgotten. Level 2 sleep is good for sleeping and waking up the engine to run a different model or update the model, where previous model weights are not needed, e.g. RLHF weight update.

## Usage[¶](#usage "Permanent link")

### Offline inference[¶](#offline-inference "Permanent link")

Enable sleep mode by passing `enable_sleep_mode=True` to the [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") class.

```
fromvllmimport LLM
llm = LLM("Qwen/Qwen3-0.6B", enable_sleep_mode=True)
```

#### Python API[¶](#python-api "Permanent link")

```
# Sleep level 1
# Put the engine to sleep (level=1: offload weights to CPU RAM, discard KV cache)
llm.sleep(level=1)

# Wake up the engine (restore weights)
llm.wake_up()

# Sleep level 2
# Put the engine to sleep (level=2: discard both weights and KV cache)
llm.sleep(level=2)

# Reallocate weights memory only
llm.wake_up(tags=["weights"])

# Load weights in-place
llm.collective_rpc("reload_weights")

# Reallocate KV cache
llm.wake_up(tags=["kv_cache"])
```

#### RLHF weight updates[¶](#rlhf-weight-updates "Permanent link")

During RLHF training, vLLM allows you to selectively wake up only the model weights or the KV cache using the tags argument in wake\_up(). This fine-grained control is especially useful when updating model weights: by waking up just the weights (e.g., llm.wake\_up(tags=\["weights"])), you avoid allocating memory for the KV cache until after the weight update is complete. This approach helps prevent GPU out-of-memory (OOM) errors, particularly with large models, by minimizing peak memory usage during weight synchronization and update operations.

Use `tags=["weights"]` or `tags=["kv_cache"]` to control which resources are restored, useful for RLHF and weight updates. **Note** that `is_sleeping` will report `true` until all components are awake.

```
# Put engine to deep sleep (level=2)
llm.sleep(level=2)
# ... Get the new weights
# Wake up only weights to avoid OOM
llm.wake_up(tags=["weights"])
# ... Update the weights
# wake up KV cache after weights are updated
llm.wake_up(tags=["kv_cache"])
```

### Online Serving[¶](#online-serving "Permanent link")

To enable sleep mode in a vLLM server you need to initialize it with the flag `VLLM_SERVER_DEV_MODE=1` and pass `--enable-sleep-mode` to the vLLM server.

#### Server in development mode[¶](#server-in-development-mode "Permanent link")

When using the flag `VLLM_SERVER_DEV_MODE=1` you enable development endpoints, and these endpoints should not be exposed to users.

```
VLLM_SERVER_DEV_MODE=1vllmserveQwen/Qwen3-0.6B\
--enable-sleep-mode\
--port8000
```

Below is an example of how to sleep and wake up a model in level 1.

```
curl-XPOST'http://localhost:8000/sleep?level=1'
curl-XPOST'http://localhost:8000/wake_up'
```

And this is an example of how to sleep and wake up a model in level 2.

```
curl-XPOST'http://localhost:8000/sleep?level=2'
# Reallocate weights memory only
curl-XPOST'http://localhost:8000/wake_up?tags=weights'
# Load weights in-place
curl-XPOST'http://localhost:8000/collective_rpc'-H'Content-Type: application/json'-d'{"method":"reload_weights"}'
# Reallocate KV cache
curl-XPOST'http://localhost:8000/wake_up?tags=kv_cache'
```

#### HTTP endpoints[¶](#http-endpoints "Permanent link")

- `POST /sleep?level=1` — Put the model to sleep (`level=1`).
- `POST /wake_up` — Wake up the model. Supports optional `tags` query parameters for partial wake-up (e.g., `?tags=weights`).
- `POST /collective_rpc` — Perform a collective remote procedure call (RPC).
- `GET /is_sleeping` — Check if the model is sleeping.

Note

These endpoints are only available when passing `VLLM_SERVER_DEV_MODE=1`.

## Limitation[¶](#limitation "Permanent link")

On ROCm, the virtual memory allocation on ROCm is done through chunked memory allocation. You can control the chunk size through `VLLM_ROCM_SLEEP_MEM_CHUNK_SIZE` (in MB). The default value is set at 256MB. The larger the chunk size the faster the performance. However, setting it too large will cause OOM. So if you encounter OOM when using sleep mode. Try reducing the chunk size. It is recommended to define the chunk size as a power of 2.