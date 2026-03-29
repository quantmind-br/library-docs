---
title: LoRA Serving — SGLang
url: https://docs.sglang.io/advanced_features/lora.html
source: crawler
fetched_at: 2026-02-04T08:46:51.67041005-03:00
rendered_js: false
word_count: 2606
summary: This document explains how to efficiently serve multiple LoRA adapters using SGLang, detailing server configuration arguments and usage through OpenAI-compatible and native APIs.
tags:
    - lora
    - sglang
    - model-serving
    - multi-lora
    - adapter-weights
    - inference-optimization
category: guide
---

## LoRA Serving[#](#LoRA-Serving "Link to this heading")

SGLang enables the use of [LoRA adapters](https://arxiv.org/abs/2106.09685) with a base model. By incorporating techniques from [S-LoRA](https://arxiv.org/pdf/2311.03285) and [Punica](https://arxiv.org/pdf/2310.18547), SGLang can efficiently support multiple LoRA adapters for different sequences within a single batch of inputs.

## Arguments for LoRA Serving[#](#Arguments-for-LoRA-Serving "Link to this heading")

The following server arguments are relevant for multi-LoRA serving:

- `enable_lora`: Enable LoRA support for the model. This argument is automatically set to True if `--lora-paths` is provided for backward compatibility.
- `enable_lora_overlap_loading`: Enable asynchronous LoRA weight loading in order to overlap H2D transfers with GPU compute. This should be enabled if you find that your LoRA workloads are bottlenecked by adapter weight loading, for example when frequently loading large LoRA adapters.
- `lora_paths`: The list of LoRA adapters to load. Each adapter must be specified in one of the following formats: | = | JSON with schema {“lora\_name”:str,”lora\_path”:str,”pinned”:bool}.
- `max_loras_per_batch`: Maximum number of adaptors used by each batch. This argument can affect the amount of GPU memory reserved for multi-LoRA serving, so it should be set to a smaller value when memory is scarce. Defaults to be 8.
- `max_loaded_loras`: If specified, it limits the maximum number of LoRA adapters loaded in CPU memory at a time. The value must be greater than or equal to `max-loras-per-batch`.
- `lora_eviction_policy`: LoRA adapter eviction policy when GPU memory pool is full. `lru`: Least Recently Used (default, better cache efficiency). `fifo`: First-In-First-Out.
- `lora_backend`: The backend of running GEMM kernels for Lora modules. Currently we support Triton LoRA backend (`triton`) and Chunked SGMV backend (`csgmv`). In the future, faster backend built upon Cutlass or Cuda kernels will be added.
- `max_lora_rank`: The maximum LoRA rank that should be supported. If not specified, it will be automatically inferred from the adapters provided in `--lora-paths`. This argument is needed when you expect to dynamically load adapters of larger LoRA rank after server startup.
- `lora_target_modules`: The union set of all target modules where LoRA should be applied (e.g., `q_proj`, `k_proj`, `gate_proj`). If not specified, it will be automatically inferred from the adapters provided in `--lora-paths`. This argument is needed when you expect to dynamically load adapters of different target modules after server startup. You can also set it to `all` to enable LoRA for all supported modules. However, enabling LoRA on additional modules introduces a minor performance overhead. If your application is performance-sensitive, we recommend only specifying the modules for which you plan to load adapters.
- `--max-lora-chunk-size`: Maximum chunk size for the ChunkedSGMV LoRA backend. Only used when –lora-backend is ‘csgmv’. Choosing a larger value might improve performance. Please tune this value based on your hardware and workload as needed. Defaults to 16.
- `tp_size`: LoRA serving along with Tensor Parallelism is supported by SGLang. `tp_size` controls the number of GPUs for tensor parallelism. More details on the tensor sharding strategy can be found in [S-Lora](https://arxiv.org/pdf/2311.03285) paper.

From client side, the user needs to provide a list of strings as input batch, and a list of adaptor names that each input sequence corresponds to.

## Usage[#](#Usage "Link to this heading")

### Serving Single Adaptor[#](#Serving-Single-Adaptor "Link to this heading")

**Note:** SGLang supports LoRA adapters through two APIs:

1. **OpenAI-Compatible API** (`/v1/chat/completions`, `/v1/completions`): Use the `model:adapter-name` syntax. See [OpenAI API with LoRA](https://docs.sglang.io/basic_usage/openai_api_completions.html#Using-LoRA-Adapters) for examples.
2. **Native API** (`/generate`): Pass `lora_path` in the request body (shown below).

```
importjson
importrequests

fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport wait_for_server, terminate_process
```

```
[2026-02-04 11:20:20] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:20:20] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:20:20] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
server_process, port = launch_server_cmd(
    # Here we set max-loras-per-batch to 2: one slot for adaptor and another one for base model
"""
python3 -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --enable-lora \
    --lora-paths lora0=algoprog/fact-generation-llama-3.1-8b-instruct-lora \
    --max-loras-per-batch 2 \
    --log-level warning \
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:20:26] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:20:26] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:20:26] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:20:29] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:20:29] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:20:40] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:20:40] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:20:40] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:20:40] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:20:40] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:20:40] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:20:47] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:20:47] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:20:47] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:20:47] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:03<00:10,  3.39s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:07<00:07,  3.56s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:11<00:03,  4.00s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:12<00:00,  2.62s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:12<00:00,  3.02s/it]

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 21.62it/s]

Capturing batches (bs=1 avail_mem=18.50 GB): 100%|██████████| 3/3 [00:01<00:00,  2.88it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
url = f"http://127.0.0.1:{port}"
json_data = {
    "text": [
        "List 3 countries and their capitals.",
        "List 3 countries and their capitals.",
    ],
    "sampling_params": {"max_new_tokens": 32, "temperature": 0},
    # The first input uses lora0, and the second input uses the base model
    "lora_path": ["lora0", None],
}
response = requests.post(
    url + "/generate",
    json=json_data,
)
print(f"Output 0: {response.json()[0]['text']}")
print(f"Output 1: {response.json()[1]['text']}")
```

```
Output 0:  Each country and capital should be on a new line.
Country: France
Capital: Paris
Country: Japan
Capital: Tokyo
Country: Australia

Output 1:  1. 2. 3.
1.  United States - Washington D.C. 2.  Japan - Tokyo 3.  Australia -
```

```
terminate_process(server_process)
```

### Serving Multiple Adaptors[#](#Serving-Multiple-Adaptors "Link to this heading")

```
server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --enable-lora \
    --lora-paths lora0=algoprog/fact-generation-llama-3.1-8b-instruct-lora \
    lora1=Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16 \
    --max-loras-per-batch 2 \
    --log-level warning \
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:21:16] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:21:16] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:21:16] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:21:19] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:21:19] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:21:25] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:21:25] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:21:25] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:21:26] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:21:26] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:21:26] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:21:32] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:21:32] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:21:32] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:21:32] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:02,  1.05it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:02<00:02,  1.05s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:03<00:01,  1.02s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.34it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.18it/s]

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 117.06it/s]

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 88.31it/s]

Capturing batches (bs=1 avail_mem=35.77 GB): 100%|██████████| 3/3 [00:01<00:00,  1.55it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
url = f"http://127.0.0.1:{port}"
json_data = {
    "text": [
        "List 3 countries and their capitals.",
        "List 3 countries and their capitals.",
    ],
    "sampling_params": {"max_new_tokens": 32, "temperature": 0},
    # The first input uses lora0, and the second input uses lora1
    "lora_path": ["lora0", "lora1"],
}
response = requests.post(
    url + "/generate",
    json=json_data,
)
print(f"Output 0: {response.json()[0]['text']}")
print(f"Output 1: {response.json()[1]['text']}")
```

```
Output 0:  Each country and capital should be on a new line.
Country: France
Capital: Paris
Country: Japan
Capital: Tokyo
Country: Australia

Output 1:  Give the countries and capitals in the correct order.
Countries: Japan, Brazil, Australia
Capitals: Tokyo, Brasilia, Canberra
1. Japan -
```

```
terminate_process(server_process)
```

### Dynamic LoRA loading[#](#Dynamic-LoRA-loading "Link to this heading")

Instead of specifying all adapters during server startup via `--lora-paths`. You can also load & unload LoRA adapters dynamically via the `/load_lora_adapter` and `/unload_lora_adapter` API.

When using dynamic LoRA loading, it’s recommended to explicitly specify both `--max-lora-rank` and `--lora-target-modules` at startup. For backward compatibility, SGLang will infer these values from `--lora-paths` if they are not explicitly provided. However, in that case, you would have to ensure that all dynamically loaded adapters share the same shape (rank and target modules) as those in the initial `--lora-paths` or are strictly “smaller”.

```
lora0 = "Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16"  # rank - 4, target modules - q_proj, k_proj, v_proj, o_proj, gate_proj
lora1 = "algoprog/fact-generation-llama-3.1-8b-instruct-lora"  # rank - 64, target modules - q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
lora0_new = "philschmid/code-llama-3-1-8b-text-to-sql-lora"  # rank - 256, target modules - q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj


# The `--target-lora-modules` param below is technically not needed, as the server will infer it from lora0 which already has all the target modules specified.
# We are adding it here just to demonstrate usage.
server_process, port = launch_server_cmd(
"""
    python3 -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --enable-lora \
    --cuda-graph-max-bs 2 \
    --max-loras-per-batch 2 \
    --max-lora-rank 256
    --lora-target-modules all
    --log-level warning
    """
)

url = f"http://127.0.0.1:{port}"
wait_for_server(url)
```

```
[2026-02-04 11:21:56] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:21:56] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:21:56] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:21:59] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:21:59] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:21:59] LoRA backend 'csgmv' does not yet support embedding or lm_head layers; dropping 'embed_tokens' and 'lm_head' from --lora-target-modules=all. To apply LoRA to these, use --lora-backend triton.
[2026-02-04 11:22:05] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:05] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:05] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:22:05] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:05] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:05] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:22:11] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:22:11] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:22:11] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:22:11] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:02,  1.09it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.05it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:02<00:00,  1.01it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.36it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.22it/s]

Capturing batches (bs=1 avail_mem=33.68 GB): 100%|██████████| 3/3 [00:01<00:00,  2.99it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

Load adapter lora0

```
response = requests.post(
    url + "/load_lora_adapter",
    json={
        "lora_name": "lora0",
        "lora_path": lora0,
    },
)

if response.status_code == 200:
    print("LoRA adapter loaded successfully.", response.json())
else:
    print("Failed to load LoRA adapter.", response.json())
```

```
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 79.89it/s]

LoRA adapter loaded successfully. {'rid': None, 'http_worker_ipc': None, 'success': True, 'error_message': '', 'loaded_adapters': {'lora0': 'Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16'}}
```

Load adapter lora1:

```
response = requests.post(
    url + "/load_lora_adapter",
    json={
        "lora_name": "lora1",
        "lora_path": lora1,
    },
)

if response.status_code == 200:
    print("LoRA adapter loaded successfully.", response.json())
else:
    print("Failed to load LoRA adapter.", response.json())
```

```
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 109.57it/s]

LoRA adapter loaded successfully. {'rid': None, 'http_worker_ipc': None, 'success': True, 'error_message': '', 'loaded_adapters': {'lora0': 'Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16', 'lora1': 'algoprog/fact-generation-llama-3.1-8b-instruct-lora'}}
```

Check inference output:

```
url = f"http://127.0.0.1:{port}"
json_data = {
    "text": [
        "List 3 countries and their capitals.",
        "List 3 countries and their capitals.",
    ],
    "sampling_params": {"max_new_tokens": 32, "temperature": 0},
    # The first input uses lora0, and the second input uses lora1
    "lora_path": ["lora0", "lora1"],
}
response = requests.post(
    url + "/generate",
    json=json_data,
)
print(f"Output from lora0: \n{response.json()[0]['text']}\n")
print(f"Output from lora1 (updated): \n{response.json()[1]['text']}\n")
```

```
Output from lora0:
 Give the capital of each country.
Country 1: Japan
Capital: Tokyo
Country 2: Australia
Capital: Canberra
Country 3: Brazil

Output from lora1 (updated):
 Each country and capital should be on a new line.
France, Paris
Japan, Tokyo
Brazil, Brasília
List 3 countries and their capitals

```

Unload lora0 and replace it with a different adapter:

```
response = requests.post(
    url + "/unload_lora_adapter",
    json={
        "lora_name": "lora0",
    },
)

response = requests.post(
    url + "/load_lora_adapter",
    json={
        "lora_name": "lora0",
        "lora_path": lora0_new,
    },
)

if response.status_code == 200:
    print("LoRA adapter loaded successfully.", response.json())
else:
    print("Failed to load LoRA adapter.", response.json())
```

```
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 78.63it/s]

LoRA adapter loaded successfully. {'rid': None, 'http_worker_ipc': None, 'success': True, 'error_message': '', 'loaded_adapters': {'lora1': 'algoprog/fact-generation-llama-3.1-8b-instruct-lora', 'lora0': 'philschmid/code-llama-3-1-8b-text-to-sql-lora'}}
```

Check output again:

```
url = f"http://127.0.0.1:{port}"
json_data = {
    "text": [
        "List 3 countries and their capitals.",
        "List 3 countries and their capitals.",
    ],
    "sampling_params": {"max_new_tokens": 32, "temperature": 0},
    # The first input uses lora0, and the second input uses lora1
    "lora_path": ["lora0", "lora1"],
}
response = requests.post(
    url + "/generate",
    json=json_data,
)
print(f"Output from lora0: \n{response.json()[0]['text']}\n")
print(f"Output from lora1 (updated): \n{response.json()[1]['text']}\n")
```

```
Output from lora0:
 Country 1: Japan, Capital: Tokyo. Country 2: Australia, Capital: Canberra. Country 3: Brazil, Capital: Brasília.
A

Output from lora1 (updated):
 Each country and capital should be on a new line.
France, Paris
Japan, Tokyo
Brazil, Brasília
List 3 countries and their capitals

```

```
terminate_process(server_process)
```

### OpenAI-compatible API usage[#](#OpenAI-compatible-API-usage "Link to this heading")

You can use LoRA adapters via the OpenAI-compatible APIs by specifying the adapter in the `model` field using the `base-model:adapter-name` syntax (for example, `qwen/qwen2.5-0.5b-instruct:adapter_a`). For more details and examples, see the “Using LoRA Adapters” section in the OpenAI API documentation: [openai\_api\_completions.ipynb](https://docs.sglang.io/basic_usage/openai_api_completions.html).

### LoRA GPU Pinning[#](#LoRA-GPU-Pinning "Link to this heading")

Another advanced option is to specify adapters as `pinned` during loading. When an adapter is pinned, it is permanently assigned to one of the available GPU pool slots (as configured by `--max-loras-per-batch`) and will not be evicted from GPU memory during runtime. Instead, it remains resident until it is explicitly unloaded.

This can improve performance in scenarios where the same adapter is frequently used across requests, by avoiding repeated memory transfers and reinitialization overhead. However, since GPU pool slots are limited, pinning adapters reduces the flexibility of the system to dynamically load other adapters on demand. If too many adapters are pinned, it may lead to degraded performance, or in the most extreme case (`Number of pinned adapters == max-loras-per-batch`), halt all unpinned requests. Therefore, currently SGLang limits maximal number of pinned adapters to `max-loras-per-batch - 1` to prevent unexpected starvations.

In the example below, we start a server with `lora1` loaded as pinned, `lora2` and `lora3` loaded as regular (unpinned) adapters. Please note that, we intentionally specify `lora2` and `lora3` in two different formats to demonstrate that both are supported.

```
server_process, port = launch_server_cmd(
"""
    python3 -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --enable-lora \
    --cuda-graph-max-bs 8 \
    --max-loras-per-batch 3 \
    --max-lora-rank 256 \
    --lora-target-modules all \
    --lora-paths \
        {"lora_name":"lora0","lora_path":"Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16","pinned":true} \
        {"lora_name":"lora1","lora_path":"algoprog/fact-generation-llama-3.1-8b-instruct-lora"} \
        lora2=philschmid/code-llama-3-1-8b-text-to-sql-lora
    --log-level warning
    """
)


url = f"http://127.0.0.1:{port}"
wait_for_server(url)
```

```
[2026-02-04 11:22:32] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:32] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:32] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:22:34] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:22:34] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:22:35] LoRA backend 'csgmv' does not yet support embedding or lm_head layers; dropping 'embed_tokens' and 'lm_head' from --lora-target-modules=all. To apply LoRA to these, use --lora-backend triton.
[2026-02-04 11:22:40] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:40] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:40] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:22:40] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:40] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:40] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:22:46] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:22:46] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:22:46] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:22:46] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:02,  1.20it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.09it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:02<00:00,  1.03it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.37it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.25it/s]

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 84.88it/s]

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 112.01it/s]

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 79.57it/s]

Capturing batches (bs=1 avail_mem=56.69 GB): 100%|██████████| 3/3 [00:01<00:00,  1.97it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

You can also specify adapter as pinned during dynamic adapter loading. In the example below, we reload `lora2` as pinned adapter:

```
response = requests.post(
    url + "/unload_lora_adapter",
    json={
        "lora_name": "lora1",
    },
)

response = requests.post(
    url + "/load_lora_adapter",
    json={
        "lora_name": "lora1",
        "lora_path": "algoprog/fact-generation-llama-3.1-8b-instruct-lora",
        "pinned": True,  # Pin the adapter to GPU
    },
)
```

```
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 108.36it/s]

```

Verify that the results are expected:

```
url = f"http://127.0.0.1:{port}"
json_data = {
    "text": [
        "List 3 countries and their capitals.",
        "List 3 countries and their capitals.",
        "List 3 countries and their capitals.",
    ],
    "sampling_params": {"max_new_tokens": 32, "temperature": 0},
    # The first input uses lora0, and the second input uses lora1
    "lora_path": ["lora0", "lora1", "lora2"],
}
response = requests.post(
    url + "/generate",
    json=json_data,
)
print(f"Output from lora0 (pinned): \n{response.json()[0]['text']}\n")
print(f"Output from lora1 (pinned): \n{response.json()[1]['text']}\n")
print(f"Output from lora2 (not pinned): \n{response.json()[2]['text']}\n")
```

```
Output from lora0 (pinned):
 Give the capital of each country.
Country 1: Japan
Capital: Tokyo
Country 2: Australia
Capital: Canberra
Country 3: Brazil

Output from lora1 (pinned):
 Each country and capital should be on a new line.
France, Paris
Japan, Tokyo
Brazil, Brasília
List 3 countries and their capitals

Output from lora2 (not pinned):
 Country 1: Australia, Capital: Canberra. Country 2: Japan, Capital: Tokyo. Country 3: Brazil, Capital: Brasília.
The

```

```
terminate_process(server_process)
```

## Choosing LoRA Backend[#](#Choosing-LoRA-Backend "Link to this heading")

SGLang supports two LoRA backends that you can choose from using the `--lora-backend` argument:

- `triton`: Basic Triton-based backend.
- `csgmv`: Default chunked SGMV backend optimized for high concurrency scenarios.

The `csgmv` backend was recently introduced to improve performance especially at high-concurrency scenarios. Our benchmark shows that it achieves 20% to 80% latency improvements over the basic triton backend.

```
server_process, port = launch_server_cmd(
"""
    python3 -m sglang.launch_server \
    --model-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --enable-lora \
    --lora-backend csgmv \
    --max-loras-per-batch 16 \
    --lora-paths lora1=path/to/lora1 lora2=path/to/lora2
    """
)
```

```
terminate_process(server_process)
```

## LoRA Overlap Loading[#](#LoRA-Overlap-Loading "Link to this heading")

By using the `--enable-lora-overlap-loading` server argument, the SGLang engine is able to overlap the loading of LoRA weights with prefill and decode compute, essentially hiding the data movement for LoRA weights behind GPU computation. Our benchmarks show that under adversarial conditions, enabling this feature can result in a ~35% reduction in median TTFT - (see the [LoRA overlap loading PR](https://github.com/sgl-project/sglang/pull/15512) for detailed benchmarks).

```
lora0 = "Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16"
lora1 = "algoprog/fact-generation-llama-3.1-8b-instruct-lora"
lora2 = "philschmid/code-llama-3-1-8b-text-to-sql-lora"


server_process, port = launch_server_cmd(
"""
    python3 -m sglang.launch_server \
    --model-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --enable-lora \
    --enable-lora-overlap-loading \
    --lora-paths lora0=Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16 \
    lora1=algoprog/fact-generation-llama-3.1-8b-instruct-lora \
    lora2=philschmid/code-llama-3-1-8b-text-to-sql-lora \
    --max-lora-rank 256 \
    --max-loras-per-batch 2 \
    --max-loaded-loras 4
    """
)

url = f"http://127.0.0.1:{port}"
wait_for_server(url)
```

```
[2026-02-04 11:23:07] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:23:07] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:23:07] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:23:10] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:23:10] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:23:11] server_args=ServerArgs(model_path='meta-llama/Meta-Llama-3.1-8B-Instruct', tokenizer_path='meta-llama/Meta-Llama-3.1-8B-Instruct', tokenizer_mode='auto', tokenizer_worker_num=1, skip_tokenizer_init=False, load_format='auto', model_loader_extra_config='{}', trust_remote_code=False, context_length=None, is_embedding=False, enable_multimodal=None, revision=None, model_impl='auto', host='127.0.0.1', port=31021, fastapi_root_path='', grpc_mode=False, skip_server_warmup=False, warmups=None, nccl_port=None, checkpoint_engine_wait_weights_before_ready=False, dtype='auto', quantization=None, quantization_param_path=None, kv_cache_dtype='auto', enable_fp32_lm_head=False, modelopt_quant=None, modelopt_checkpoint_restore_path=None, modelopt_checkpoint_save_path=None, modelopt_export_path=None, quantize_and_serve=False, rl_quant_profile=None, mem_fraction_static=0.841, max_running_requests=128, max_queued_requests=None, max_total_tokens=20480, chunked_prefill_size=8192, enable_dynamic_chunking=False, max_prefill_tokens=16384, prefill_max_requests=None, schedule_policy='fcfs', enable_priority_scheduling=False, abort_on_priority_when_disabled=False, schedule_low_priority_values_first=False, priority_scheduling_preemption_threshold=10, schedule_conservativeness=1.0, page_size=1, swa_full_tokens_ratio=0.8, disable_hybrid_swa_memory=False, radix_eviction_policy='lru', enable_prefill_delayer=False, prefill_delayer_max_delay_passes=30, prefill_delayer_token_usage_low_watermark=None, prefill_delayer_forward_passes_buckets=None, prefill_delayer_wait_seconds_buckets=None, device='cuda', tp_size=1, pp_size=1, pp_max_micro_batch_size=None, pp_async_batch_depth=0, stream_interval=1, stream_output=False, random_seed=48355042, constrained_json_whitespace_pattern=None, constrained_json_disable_any_whitespace=False, watchdog_timeout=300, soft_watchdog_timeout=300, dist_timeout=None, download_dir=None, model_checksum=None, base_gpu_id=0, gpu_id_step=1, sleep_on_idle=False, custom_sigquit_handler=None, log_level='info', log_level_http=None, log_requests=False, log_requests_level=2, log_requests_format='text', log_requests_target=None, uvicorn_access_log_exclude_prefixes=[], crash_dump_folder=None, show_time_cost=False, enable_metrics=False, enable_metrics_for_all_schedulers=False, tokenizer_metrics_custom_labels_header='x-custom-labels', tokenizer_metrics_allowed_custom_labels=None, extra_metric_labels=None, bucket_time_to_first_token=None, bucket_inter_token_latency=None, bucket_e2e_request_latency=None, collect_tokens_histogram=False, prompt_tokens_buckets=None, generation_tokens_buckets=None, gc_warning_threshold_secs=0.0, decode_log_interval=40, enable_request_time_stats_logging=False, kv_events_config=None, enable_trace=False, otlp_traces_endpoint='localhost:4317', export_metrics_to_file=False, export_metrics_to_file_dir=None, api_key=None, admin_api_key=None, served_model_name='meta-llama/Meta-Llama-3.1-8B-Instruct', weight_version='default', chat_template=None, hf_chat_template_name=None, completion_template=None, file_storage_path='sglang_storage', enable_cache_report=False, reasoning_parser=None, tool_call_parser=None, tool_server=None, sampling_defaults='model', dp_size=1, load_balance_method='round_robin', dist_init_addr=None, nnodes=1, node_rank=0, json_model_override_args='{}', preferred_sampling_params=None, enable_lora=True, enable_lora_overlap_loading=True, max_lora_rank=256, lora_target_modules=None, lora_paths=[LoRARef(lora_id='250047b1e277493691be41030426505c', lora_name='lora0', lora_path='Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16', pinned=False), LoRARef(lora_id='fbae36dbdf0344f58dd52e740770f720', lora_name='lora1', lora_path='algoprog/fact-generation-llama-3.1-8b-instruct-lora', pinned=False), LoRARef(lora_id='cf9b51e260aa43c7bf1f398906625661', lora_name='lora2', lora_path='philschmid/code-llama-3-1-8b-text-to-sql-lora', pinned=False)], max_loaded_loras=4, max_loras_per_batch=2, lora_eviction_policy='lru', lora_backend='csgmv', max_lora_chunk_size=16, attention_backend='fa3', decode_attention_backend=None, prefill_attention_backend=None, sampling_backend='flashinfer', grammar_backend='xgrammar', mm_attention_backend=None, fp8_gemm_runner_backend='auto', fp4_gemm_runner_backend='auto', nsa_prefill_backend=None, nsa_decode_backend=None, disable_flashinfer_autotune=False, speculative_algorithm=None, speculative_draft_model_path=None, speculative_draft_model_revision=None, speculative_draft_load_format=None, speculative_num_steps=None, speculative_eagle_topk=None, speculative_num_draft_tokens=None, speculative_accept_threshold_single=1.0, speculative_accept_threshold_acc=1.0, speculative_token_map=None, speculative_attention_mode='prefill', speculative_draft_attention_backend=None, speculative_moe_runner_backend='auto', speculative_moe_a2a_backend=None, speculative_draft_model_quantization=None, speculative_ngram_min_match_window_size=1, speculative_ngram_max_match_window_size=12, speculative_ngram_min_bfs_breadth=1, speculative_ngram_max_bfs_breadth=10, speculative_ngram_match_type='BFS', speculative_ngram_branch_length=18, speculative_ngram_capacity=10000000, enable_multi_layer_eagle=False, ep_size=1, moe_a2a_backend='none', moe_runner_backend='auto', flashinfer_mxfp4_moe_precision='default', enable_flashinfer_allreduce_fusion=False, deepep_mode='auto', ep_num_redundant_experts=0, ep_dispatch_algorithm=None, init_expert_location='trivial', enable_eplb=False, eplb_algorithm='auto', eplb_rebalance_num_iterations=1000, eplb_rebalance_layers_per_chunk=None, eplb_min_rebalancing_utilization_threshold=1.0, expert_distribution_recorder_mode=None, expert_distribution_recorder_buffer_size=1000, enable_expert_distribution_metrics=False, deepep_config=None, moe_dense_tp_size=None, elastic_ep_backend=None, mooncake_ib_device=None, max_mamba_cache_size=None, mamba_ssm_dtype='float32', mamba_full_memory_ratio=0.9, mamba_scheduler_strategy='no_buffer', mamba_track_interval=256, enable_hierarchical_cache=False, hicache_ratio=2.0, hicache_size=0, hicache_write_policy='write_through', hicache_io_backend='kernel', hicache_mem_layout='layer_first', disable_hicache_numa_detect=False, hicache_storage_backend=None, hicache_storage_prefetch_policy='best_effort', hicache_storage_backend_extra_config=None, hierarchical_sparse_attention_extra_config=None, enable_lmcache=False, kt_weight_path=None, kt_method='AMXINT4', kt_cpuinfer=None, kt_threadpool_count=2, kt_num_gpu_experts=None, kt_max_deferred_experts_per_token=None, dllm_algorithm=None, dllm_algorithm_config=None, enable_double_sparsity=False, ds_channel_config_path=None, ds_heavy_channel_num=32, ds_heavy_token_num=256, ds_heavy_channel_type='qk', ds_sparse_decode_threshold=4096, cpu_offload_gb=0, offload_group_size=-1, offload_num_in_group=1, offload_prefetch_step=1, offload_mode='cpu', multi_item_scoring_delimiter=None, disable_radix_cache=False, cuda_graph_max_bs=4, cuda_graph_bs=[1, 2, 4], disable_cuda_graph=False, disable_cuda_graph_padding=False, enable_profile_cuda_graph=False, enable_cudagraph_gc=False, enable_layerwise_nvtx_marker=False, enable_nccl_nvls=False, enable_symm_mem=False, disable_flashinfer_cutlass_moe_fp4_allgather=False, enable_tokenizer_batch_encode=False, disable_tokenizer_batch_decode=False, disable_outlines_disk_cache=False, disable_custom_all_reduce=False, enable_mscclpp=False, enable_torch_symm_mem=False, disable_overlap_schedule=False, enable_mixed_chunk=False, enable_dp_attention=False, enable_dp_lm_head=False, enable_two_batch_overlap=False, enable_single_batch_overlap=False, tbo_token_distribution_threshold=0.48, enable_torch_compile=False, enable_piecewise_cuda_graph=False, enable_torch_compile_debug_mode=False, torch_compile_max_bs=32, piecewise_cuda_graph_max_tokens=8192, piecewise_cuda_graph_tokens=[4, 8, 12, 16, 20, 24, 28, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 288, 320, 352, 384, 416, 448, 480, 512, 576, 640, 704, 768, 832, 896, 960, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072, 3328, 3584, 3840, 4096, 4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192], piecewise_cuda_graph_compiler='eager', torchao_config='', enable_nan_detection=False, enable_p2p_check=False, triton_attention_reduce_in_fp32=False, triton_attention_num_kv_splits=8, triton_attention_split_tile_size=None, num_continuous_decode_steps=1, delete_ckpt_after_loading=False, enable_memory_saver=False, enable_weights_cpu_backup=False, enable_draft_weights_cpu_backup=False, allow_auto_truncate=False, enable_custom_logit_processor=False, flashinfer_mla_disable_ragged=False, disable_shared_experts_fusion=False, disable_chunked_prefix_cache=False, disable_fast_image_processor=False, keep_mm_feature_on_device=False, enable_return_hidden_states=False, enable_return_routed_experts=False, scheduler_recv_interval=1, numa_node=None, enable_deterministic_inference=False, rl_on_policy_target=None, enable_attn_tp_input_scattered=False, enable_nsa_prefill_context_parallel=False, nsa_prefill_cp_mode='in-seq-split', enable_fused_qk_norm_rope=False, enable_precise_embedding_interpolation=False, enable_dynamic_batch_tokenizer=False, dynamic_batch_tokenizer_batch_size=32, dynamic_batch_tokenizer_batch_timeout=0.002, debug_tensor_dump_output_folder=None, debug_tensor_dump_layers=None, debug_tensor_dump_input_file=None, debug_tensor_dump_inject=False, disaggregation_mode='null', disaggregation_transfer_backend='mooncake', disaggregation_bootstrap_port=8998, disaggregation_decode_tp=None, disaggregation_decode_dp=None, disaggregation_prefill_pp=1, disaggregation_ib_device=None, disaggregation_decode_enable_offload_kvcache=False, disaggregation_decode_enable_fake_auto=False, num_reserved_decode_tokens=512, disaggregation_decode_polling_interval=1, encoder_only=False, language_only=False, encoder_transfer_backend='zmq_to_scheduler', encoder_urls=[], custom_weight_loader=[], weight_loader_disable_mmap=False, remote_instance_weight_loader_seed_instance_ip=None, remote_instance_weight_loader_seed_instance_service_port=None, remote_instance_weight_loader_send_weights_group_ports=None, remote_instance_weight_loader_backend='nccl', remote_instance_weight_loader_start_seed_via_transfer_engine=False, enable_pdmux=False, pdmux_config_path=None, sm_group_num=8, mm_max_concurrent_calls=32, mm_per_request_timeout=10.0, enable_broadcast_mm_inputs_process=False, enable_prefix_mm_cache=False, mm_enable_dp_encoder=False, mm_process_config={}, limit_mm_data_per_request=None, decrypted_config_file=None, decrypted_draft_config_file=None, forward_hooks=None)
[2026-02-04 11:23:11] Watchdog TokenizerManager initialized.
[2026-02-04 11:23:11] Using default HuggingFace chat template with detected content format: string
[2026-02-04 11:23:16] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:23:16] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:23:16] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:23:16] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:23:16] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:23:16] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:23:19] Watchdog DetokenizerManager initialized.
[2026-02-04 11:23:19] Init torch distributed begin.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:23:21] Init torch distributed ends. elapsed=1.37 s, mem usage=0.09 GB
[2026-02-04 11:23:21] MOE_RUNNER_BACKEND is not initialized, the backend will be automatically selected
[2026-02-04 11:23:23] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:23:23] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:23:23] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:23:23] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
[2026-02-04 11:23:23] Load weight begin. avail mem=42.24 GB
[2026-02-04 11:23:23] Found local HF snapshot for meta-llama/Meta-Llama-3.1-8B-Instruct at /hf_home/hub/models--meta-llama--Meta-Llama-3.1-8B-Instruct/snapshots/0e9e39f249a16976918f6564b8830bc894c89659; skipping download.
[2026-02-04 11:23:23] Beginning to load weights
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:02,  1.04it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:02<00:02,  1.04s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:03<00:01,  1.03s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.33it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.18it/s]

[2026-02-04 11:23:27] Loading weights took 3.42 seconds
[2026-02-04 11:23:27] Load weight end. elapsed=3.67 s, type=LlamaForCausalLM, dtype=torch.bfloat16, avail mem=25.31 GB, mem usage=16.93 GB.
[2026-02-04 11:23:27] Using csgmv as backend of LoRA kernels.
[2026-02-04 11:23:27] Found local HF snapshot for Nutanix/Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16 at /hf_home/hub/models--Nutanix--Meta-Llama-3.1-8B-Instruct_lora_4_alpha_16/snapshots/a2b27aa70a66dc36ce71116f6c6a259dd1b23c17; skipping download.
[2026-02-04 11:23:27] No model.safetensors.index.json found in remote.
[2026-02-04 11:23:27] Beginning to load weights
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 88.00it/s]

[2026-02-04 11:23:27] Found local HF snapshot for algoprog/fact-generation-llama-3.1-8b-instruct-lora at /hf_home/hub/models--algoprog--fact-generation-llama-3.1-8b-instruct-lora/snapshots/dc8cdfb21993a6cb46199d6b1d79f68a42b06439; skipping download.
[2026-02-04 11:23:27] No model.safetensors.index.json found in remote.
[2026-02-04 11:23:27] Beginning to load weights
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 114.71it/s]

[2026-02-04 11:23:28] Found local HF snapshot for philschmid/code-llama-3-1-8b-text-to-sql-lora at /hf_home/hub/models--philschmid--code-llama-3-1-8b-text-to-sql-lora/snapshots/141fc3a09386a8baf0d7495c247ae2d1a565f69f; skipping download.
[2026-02-04 11:23:28] No model.safetensors.index.json found in remote.
[2026-02-04 11:23:28] Beginning to load weights
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 78.95it/s]

[2026-02-04 11:23:32] Using KV cache dtype: torch.bfloat16
[2026-02-04 11:23:32] KV Cache is allocated. #tokens: 20480, K size: 1.25 GB, V size: 1.25 GB
[2026-02-04 11:23:32] Memory pool end. avail mem=20.81 GB
[2026-02-04 11:23:32] Init attention backend begin.
[2026-02-04 11:23:32] Init attention backend end. elapsed=0.03 s
[2026-02-04 11:23:32] Capture cuda graph begin. This can take up to several minutes. avail mem=20.72 GB
[2026-02-04 11:23:32] Capture cuda graph bs [1, 2, 4]
Capturing batches (bs=1 avail_mem=20.53 GB): 100%|██████████| 3/3 [00:00<00:00,  3.18it/s]
[2026-02-04 11:23:33] Capture cuda graph end. Time elapsed: 1.51 s. mem usage=0.19 GB. avail mem=20.52 GB.
[2026-02-04 11:23:34] max_total_num_tokens=20480, chunked_prefill_size=8192, max_prefill_tokens=16384, max_running_requests=128, context_len=131072, available_gpu_mem=20.52 GB
[2026-02-04 11:23:34] INFO:     Started server process [1763677]
[2026-02-04 11:23:34] INFO:     Waiting for application startup.
[2026-02-04 11:23:34] Using default chat sampling params from model generation config: {'repetition_penalty': 1.0, 'temperature': 0.6, 'top_k': 50, 'top_p': 0.9}
[2026-02-04 11:23:34] Using default chat sampling params from model generation config: {'repetition_penalty': 1.0, 'temperature': 0.6, 'top_k': 50, 'top_p': 0.9}
[2026-02-04 11:23:34] INFO:     Application startup complete.
[2026-02-04 11:23:34] INFO:     Uvicorn running on http://127.0.0.1:31021 (Press CTRL+C to quit)
[2026-02-04 11:23:35] INFO:     127.0.0.1:47336 - "GET /v1/models HTTP/1.1" 200 OK
[2026-02-04 11:23:35] INFO:     127.0.0.1:47342 - "GET /model_info HTTP/1.1" 200 OK
[2026-02-04 11:23:36] Prefill batch, #new-seq: 1, #new-token: 7, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0, input throughput (token/s): 0.00, cuda graph: False
[2026-02-04 11:23:36] INFO:     127.0.0.1:47346 - "POST /generate HTTP/1.1" 200 OK
[2026-02-04 11:23:36] The server is fired up and ready to roll!
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
json_data = {
    "text": [
        "Write a very long fairy-tale.",
        "List 3 countries and their capitals.",
        "List 3 countries and their capitals.",
    ],
    "sampling_params": [
        {"max_new_tokens": 1024, "temperature": 0},
        {"max_new_tokens": 64, "temperature": 0},
        {"max_new_tokens": 64, "temperature": 0},
    ],
    "lora_path": ["lora0", "lora1", "lora2"],
}

# lora0 and lora1 will be loaded into the memory pool first, and because max_loras_per_batch = 2, lora2's request will remain in the queue.
# lora1's request will likely finish first, and once it does, lora2 will be loaded. With --enable-lora-overlap-loading, this loading will
# occur asynchronously and thus decoding for lora0's request won't be blocked.
response = requests.post(
    url + "/generate",
    json=json_data,
)

for i in range(3):
    print(f"Output from lora{i}: \n{response.json()[i]['text']}\n")
```

```
[2026-02-04 11:23:40] Prefill batch, #new-seq: 1, #new-token: 9, #cached-token: 0, token usage: 0.00, #running-req: 1, #queue-req: 1, input throughput (token/s): 1.61, cuda graph: False
[2026-02-04 11:23:41] Prefill batch, #new-seq: 1, #new-token: 9, #cached-token: 0, token usage: 0.00, #running-req: 1, #queue-req: 1, input throughput (token/s): 149.74, cuda graph: False
[2026-02-04 11:23:41] Decode batch, #running-req: 2, #token: 84, token usage: 0.00, cuda graph: True, gen throughput (token/s): 3.17, #queue-req: 1
[2026-02-04 11:23:42] Prefill batch, #new-seq: 1, #new-token: 9, #cached-token: 0, token usage: 0.00, #running-req: 1, #queue-req: 0, input throughput (token/s): 5.71, cuda graph: False
[2026-02-04 11:23:42] Decode batch, #running-req: 2, #token: 93, token usage: 0.00, cuda graph: True, gen throughput (token/s): 79.77, #queue-req: 0
[2026-02-04 11:23:43] Decode batch, #running-req: 2, #token: 173, token usage: 0.01, cuda graph: True, gen throughput (token/s): 68.47, #queue-req: 0
[2026-02-04 11:23:44] Decode batch, #running-req: 1, #token: 162, token usage: 0.01, cuda graph: True, gen throughput (token/s): 64.55, #queue-req: 0
[2026-02-04 11:23:45] Decode batch, #running-req: 1, #token: 202, token usage: 0.01, cuda graph: True, gen throughput (token/s): 47.39, #queue-req: 0
[2026-02-04 11:23:46] Decode batch, #running-req: 1, #token: 242, token usage: 0.01, cuda graph: True, gen throughput (token/s): 47.16, #queue-req: 0
[2026-02-04 11:23:47] Decode batch, #running-req: 1, #token: 282, token usage: 0.01, cuda graph: True, gen throughput (token/s): 47.41, #queue-req: 0
[2026-02-04 11:23:48] Decode batch, #running-req: 1, #token: 322, token usage: 0.02, cuda graph: True, gen throughput (token/s): 47.52, #queue-req: 0
[2026-02-04 11:23:48] Decode batch, #running-req: 1, #token: 362, token usage: 0.02, cuda graph: True, gen throughput (token/s): 47.26, #queue-req: 0
[2026-02-04 11:23:49] Decode batch, #running-req: 1, #token: 402, token usage: 0.02, cuda graph: True, gen throughput (token/s): 47.32, #queue-req: 0
[2026-02-04 11:23:50] Decode batch, #running-req: 1, #token: 442, token usage: 0.02, cuda graph: True, gen throughput (token/s): 47.40, #queue-req: 0
[2026-02-04 11:23:51] Decode batch, #running-req: 1, #token: 482, token usage: 0.02, cuda graph: True, gen throughput (token/s): 47.21, #queue-req: 0
[2026-02-04 11:23:52] Decode batch, #running-req: 1, #token: 522, token usage: 0.03, cuda graph: True, gen throughput (token/s): 47.79, #queue-req: 0
[2026-02-04 11:23:53] Decode batch, #running-req: 1, #token: 562, token usage: 0.03, cuda graph: True, gen throughput (token/s): 47.14, #queue-req: 0
[2026-02-04 11:23:54] Decode batch, #running-req: 1, #token: 602, token usage: 0.03, cuda graph: True, gen throughput (token/s): 47.68, #queue-req: 0
[2026-02-04 11:23:54] Decode batch, #running-req: 1, #token: 642, token usage: 0.03, cuda graph: True, gen throughput (token/s): 47.30, #queue-req: 0
[2026-02-04 11:23:55] Decode batch, #running-req: 1, #token: 682, token usage: 0.03, cuda graph: True, gen throughput (token/s): 47.45, #queue-req: 0
[2026-02-04 11:23:56] Decode batch, #running-req: 1, #token: 722, token usage: 0.04, cuda graph: True, gen throughput (token/s): 47.64, #queue-req: 0
[2026-02-04 11:23:57] Decode batch, #running-req: 1, #token: 762, token usage: 0.04, cuda graph: True, gen throughput (token/s): 54.72, #queue-req: 0
[2026-02-04 11:23:58] Decode batch, #running-req: 1, #token: 802, token usage: 0.04, cuda graph: True, gen throughput (token/s): 47.67, #queue-req: 0
[2026-02-04 11:23:58] Decode batch, #running-req: 1, #token: 842, token usage: 0.04, cuda graph: True, gen throughput (token/s): 47.08, #queue-req: 0
[2026-02-04 11:23:59] Decode batch, #running-req: 1, #token: 882, token usage: 0.04, cuda graph: True, gen throughput (token/s): 47.50, #queue-req: 0
[2026-02-04 11:24:00] Decode batch, #running-req: 1, #token: 922, token usage: 0.05, cuda graph: True, gen throughput (token/s): 47.40, #queue-req: 0
[2026-02-04 11:24:01] Decode batch, #running-req: 1, #token: 962, token usage: 0.05, cuda graph: True, gen throughput (token/s): 46.74, #queue-req: 0
[2026-02-04 11:24:02] Decode batch, #running-req: 1, #token: 1002, token usage: 0.05, cuda graph: True, gen throughput (token/s): 47.15, #queue-req: 0
[2026-02-04 11:24:02] INFO:     127.0.0.1:47360 - "POST /generate HTTP/1.1" 200 OK
Output from lora0:
 Write a very long fairy-tale.
Once upon a time, in a far-off kingdom, there lived a beautiful princess named Sophia. She had long, golden hair and sparkling blue eyes that shone like the stars in the night sky. Sophia was kind and gentle, loved by all who knew her, and she spent her days helping those in need and spreading joy wherever she went.
One day, while out for a walk in the castle gardens, Sophia stumbled upon a hidden path she had never seen before. The path was overgrown with vines and shrubs, and it seemed to lead to a secret place that only a few knew about. Sophia's curiosity was piqued, and she decided to follow the path to see where it would take her.
As she walked, the path grew narrower and the trees grew taller, casting deep shadows that made it difficult to see. Sophia heard the sound of running water and followed the sound until she came upon a beautiful waterfall. The water cascaded down a rocky cliff, creating a misty veil that surrounded Sophia like a mystical aura.
Behind the waterfall, Sophia discovered a hidden cave. The cave was filled with glittering crystals and precious gems that sparkled in the dim light. In the center of the cave, Sophia saw a magnificent throne, carved from a single piece of black marble. The throne seemed to be waiting for her, and Sophia felt an inexplicable sense of belonging as she approached it.
As she sat down on the throne, Sophia heard a soft whispering in her ear. It was the voice of the ancient magic that dwelled within the cave. The magic spoke to Sophia in a language she couldn't understand, but somehow, she knew exactly what it was saying. The magic told her that she was the chosen one, destined to wield its power and bring peace and prosperity to the kingdom.
Sophia was both thrilled and terrified by the revelation. She had always felt a deep connection to the natural world and had often wondered if there was more to her life than the mundane routine of being a princess. Now, she knew that she had a greater purpose, and she was eager to learn more about her destiny.
The magic began to teach Sophia the secrets of the cave and the ancient magic that dwelled within. Sophia spent many hours studying and practicing, and soon she became proficient in the art of magic. She learned how to communicate with animals, control the elements, and heal the sick.
As Sophia's powers grew, so did her reputation. People from all over the kingdom began to seek her out, hoping to benefit from her magical abilities. Sophia was happy to help, but she knew that she couldn't do it alone. She needed a trusted companion to aid her in her quest.
One day, while out on a walk, Sophia met a handsome young man named Finn. Finn was a skilled warrior and a member of the kingdom's elite guard. He was strong, brave, and kind, and Sophia was immediately drawn to him. As they talked, Sophia discovered that Finn was also searching for a way to use his skills for good. He was tired of fighting wars and wanted to find a way to bring peace to the kingdom.
Sophia and Finn quickly became inseparable. They spent their days exploring the kingdom, helping those in need, and learning more about the ancient magic that dwelled within the cave. As they worked together, Sophia and Finn grew closer, and their friendship blossomed into something more.
But not everyone was happy about Sophia and Finn's relationship. The king, Sophia's father, was opposed to their romance. He believed that Sophia was too important to be distracted by a mere mortal, and he wanted her to marry a prince from a neighboring kingdom. Sophia was heartbroken, but she knew that she couldn't give up on Finn.
Determined to be with Finn, Sophia and Finn hatched a plan to sneak into the neighboring kingdom and meet with the prince. They knew it wouldn't be easy, but they were willing to take the risk. As they made their way through the forest, they encountered all sorts of obstacles, from ferocious beasts to treacherous terrain.
But Sophia and Finn were undaunted. They used their combined skills to overcome every challenge, and soon they found themselves standing in front of the prince's castle. The prince, a tall, dark-haired man named Alexander, was charming and handsome, but Sophia knew that she didn't love him. She was still in love with Finn, and she knew that she had to be honest with him.
As Sophia and Finn prepared to meet with Alexander, they were ambushed by a group of bandits. The bandits were led by a ruthless leader named Victor, who had a personal vendetta against the kingdom. Victor had been seeking revenge for years, and he was determined to destroy the kingdom and everyone in it.
Sophia and Finn fought bravely, using all of their skills to defeat the bandits. But Victor was too powerful, and he managed to escape. Sophia and Finn were left to face the consequences of their

Output from lora1:
 Each country and capital should be on a new line.
France, Paris
Japan, Tokyo
Brazil, Brasília
List 3 countries and their capitals. Each country and capital should be on a new line.
France, Paris
Japan, Tokyo
Brazil, Brasília
List 3 countries and their

Output from lora2:
 Country 1 has a capital of Bogor? No, that's not correct. The capital of Country 1 is actually Bogor is not the capital, but a city in the country. The capital of Country 1 is actually Bogor is not the capital, but a city in the country. The capital of

```

```
terminate_process(server_process)
```

However, LoRA overlap loading is not free and comes with two important caveats:

1. **Pinned CPU memory requirement**: Asynchronous H2D memory copies require LoRA weights to be pinned in CPU memory, which is a finite system resource. To mitigate excessive pinned-memory usage, SGLang currently restricts `max_loaded_loras` to be at most 2× `max_loras_per_batch` when LoRA overlap loading is enabled.
2. **Reduced multi-adapter prefill batching**: With overlap loading, adapters become available on the GPU at different times because each adapter is loaded asynchronously. This can reduce the scheduler’s ability to form multi-adapter prefill batches, since only requests whose adapters are currently loaded can be grouped together. As a result, requests for different adapters will be scheduled in separate (or smaller) prefill batches, which can increase TTFT when adapter load time is small compared to prefill compute time. This is why LoRA overlap loading is disabled by default: it should only be enabled when users have determined that LoRA weight loading is a bottleneck (EG high adapter churn, heavy adapter weights, or PCIe-bottlenecked workloads).

For instance, suppose we have four LoRA adapters: `lora0`, `lora1`, `lora2`, and `lora3`. Loading any adapter takes 2ms, while the prefill step for requests for that adapter takes 20ms.

1. **Baseline**: The engine loads all four adapters synchronously, then runs one combined prefill batch, giving us a total time of ≈ `2 * 4 + 20 = 28ms`
2. **With LoRA overlap loading enabled**: The engine begins loading `lora0` and, once it is ready, schedules a prefill batch containing only `lora0` while `lora1` loads in the background. Then it schedules `lora1`’s prefill while `lora2` loads, and so on. In the worst case where prefill cannot be batched across adapters, total time is ≈ `2 + 4 * 20 = 82ms`

In this scenario, overlap loading reduces adapter-load overhead, but the loss of multi-adapter prefill batching dominates and leads to higher TTFT.

## Future Works[#](#Future-Works "Link to this heading")

The development roadmap for LoRA-related features can be found in this [issue](https://github.com/sgl-project/sglang/issues/2929). Other features, including Embedding Layer, Unified Paging, Cutlass backend are still under development.