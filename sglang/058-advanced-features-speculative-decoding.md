---
title: Speculative Decoding — SGLang
url: https://docs.sglang.io/advanced_features/speculative_decoding.html
source: crawler
fetched_at: 2026-02-04T08:46:48.060461034-03:00
rendered_js: false
word_count: 3935
summary: This document explains how to enable and configure EAGLE-based speculative decoding in SGLang to improve LLM inference throughput. It provides details on key configuration parameters and examples for launching servers using EAGLE-2 and EAGLE-3 algorithms.
tags:
    - sglang
    - speculative-decoding
    - eagle-decoding
    - llm-inference
    - performance-optimization
    - model-serving
category: guide
---

## Speculative Decoding[#](#Speculative-Decoding "Link to this heading")

SGLang now provides an EAGLE-based (EAGLE-2/EAGLE-3) speculative decoding option. Our implementation aims to maximize speed and efficiency and is considered to be among the fastest in open-source LLM engines.

## Performance Highlights[#](#Performance-Highlights "Link to this heading")

Please see below for the huge improvements on throughput for LLaMA-Instruct 3.1 8B tested on MT bench that can be achieved via EAGLE3 decoding. For further details please see the [EAGLE3 paper](https://arxiv.org/pdf/2503.01840).

### EAGLE Decoding[#](#EAGLE-Decoding "Link to this heading")

To enable EAGLE speculative decoding the following parameters are relevant:

- `speculative_draft_model_path`: Specifies draft model. This parameter is required.
- `speculative_num_steps`: Depth of autoregressive drafting. Increases speculation range but risks rejection cascades. Default is 5.
- `speculative_eagle_topk`: Branching factor per step. Improves candidate diversity, will lead to higher acceptance rate, but more lead to higher memory/compute consumption. Default is 4.
- `speculative_num_draft_tokens`: Maximum parallel verification capacity. Allows deeper tree evaluation but will lead to higher GPU memory usage. Default is 8.

These parameters are the same for EAGLE-2 and EAGLE-3.

You can find the best combinations of these parameters with [bench\_speculative.py](https://github.com/sgl-project/sglang/blob/main/scripts/playground/bench_speculative.py).

In the documentation below, we set `--cuda-graph-max-bs` to be a small value for faster engine startup. For your own workloads, please tune the above parameters together with `--cuda-graph-max-bs`, `--max-running-requests`, `--mem-fraction-static` for the best performance.

## EAGLE-2 decoding[#](#EAGLE-2-decoding "Link to this heading")

You can enable EAGLE-2 decoding by setting `--speculative-algorithm EAGLE` and choosing an appropriate model.

```
fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport wait_for_server, print_highlight, terminate_process

importopenai
```

```
[2026-02-04 11:20:20] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:20:20] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:20:20] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model meta-llama/Llama-2-7b-chat-hf  --speculative-algorithm EAGLE \
    --speculative-draft-model-path lmsys/sglang-EAGLE-llama2-chat-7B --speculative-num-steps 3 \
    --speculative-eagle-topk 4 --speculative-num-draft-tokens 16 --cuda-graph-max-bs 8 --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:20:27] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:20:27] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:20:27] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:20:29] INFO server_args.py:1796: Attention backend not specified. Use flashinfer backend by default.
[2026-02-04 11:20:29] WARNING server_args.py:2304: Overlap scheduler is disabled when spec v2 is off or using unsupported speculative algorithm. You can set env SGLANG_ENABLE_SPEC_V2=True to enable the experimental overlap scheduler.
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
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:01<00:01,  1.69s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:02<00:00,  1.21s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:02<00:00,  1.28s/it]

Capturing batches (bs=1 avail_mem=22.97 GB): 100%|██████████| 4/4 [00:00<00:00,  7.86it/s]
[2026-02-04 11:20:53] SPECULATIVE_MOE_RUNNER_BACKEND is not initialized, using auto backend
[2026-02-04 11:20:53] SPECULATIVE_MOE_A2A_BACKEND is not initialized, using none backend
Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.26s/it]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.26s/it]

Capturing batches (bs=1 avail_mem=21.40 GB): 100%|██████████| 4/4 [00:09<00:00,  2.27s/it]
Capturing batches (bs=1 avail_mem=34.95 GB): 100%|██████████| 4/4 [00:00<00:00, 43.22it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)

print_highlight(f"Response: {response}")
```

**Response: ChatCompletion(id='5f43cd2be1ab4cb7aa260fe965106876', choices=\[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content=' Sure! Here are three countries and their capitals:\\n\\n1. Country: France\\nCapital: Paris\\n2. Country: Japan\\nCapital: Tokyo\\n3. Country: Brazil\\nCapital: Brasília', refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=None, reasoning\_content=None), matched\_stop=2)], created=1770204072, model='meta-llama/Llama-2-7b-chat-hf', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=48, prompt\_tokens=17, total\_tokens=65, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

```
terminate_process(server_process)
```

## EAGLE-2 Decoding with `torch.compile`[#](#EAGLE-2-Decoding-with-torch.compile "Link to this heading")

You can also enable `torch.compile` for further optimizations and optionally set `--torch-compile-max-bs`:

```
server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model meta-llama/Llama-2-7b-chat-hf  --speculative-algorithm EAGLE \
    --speculative-draft-model-path lmsys/sglang-EAGLE-llama2-chat-7B --speculative-num-steps 5 \
        --speculative-eagle-topk 8 --speculative-num-draft-tokens 64 --mem-fraction 0.6 \
            --enable-torch-compile --torch-compile-max-bs 2 --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:21:17] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:21:17] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:21:17] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:21:19] INFO server_args.py:1796: Attention backend not specified. Use flashinfer backend by default.
[2026-02-04 11:21:19] WARNING server_args.py:2304: Overlap scheduler is disabled when spec v2 is off or using unsupported speculative algorithm. You can set env SGLANG_ENABLE_SPEC_V2=True to enable the experimental overlap scheduler.
[2026-02-04 11:21:19] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:21:26] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:21:26] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:21:26] INFO utils.py:164: NumExpr defaulting to 16 threads.
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
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:01<00:01,  1.52s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:02<00:00,  1.12s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:02<00:00,  1.18s/it]

Capturing batches (bs=2 avail_mem=39.33 GB):  25%|██▌       | 1/4 [00:00<00:01,  2.89it/s]/usr/local/lib/python3.10/dist-packages/torch/_dynamo/variables/functions.py:1692: UserWarning: Dynamo detected a call to a `functools.lru_cache`-wrapped function. Dynamo ignores the cache wrapper and directly traces the wrapped function. Silent incorrectness is only a *potential* risk, not something we have observed. Enable TORCH_LOGS="+dynamo" for a DEBUG stack trace.
  torch._dynamo.utils.warn_once(msg)
Autotune Choices Stats:
{"num_choices": 20, "num_triton_choices": 19, "best_kernel": "mm", "best_time": 0.048448000103235245, "best_triton_pos": 1, "best_triton_time": 0.04947200044989586, "best_triton_kernel": "triton_mm_18", "best_triton_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8"}
AUTOTUNE mm(128x4096, 4096x12288)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  mm 0.0484 ms 100.0%
  triton_mm_18 0.0495 ms 97.9% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_12 0.0526 ms 92.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_8 0.0548 ms 88.4% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_11 0.0554 ms 87.4% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_7 0.0560 ms 86.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_17 0.0576 ms 84.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_10 0.0677 ms 71.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8
  triton_mm_14 0.0688 ms 70.4% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=128, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8
  triton_mm_4 0.0710 ms 68.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
SingleProcess AUTOTUNE benchmarking takes 0.3164 seconds and 0.4141 seconds precompiling for 20 choices
Autotune Choices Stats:
{"num_choices": 20, "num_triton_choices": 19, "best_kernel": "mm", "best_time": 0.022336000576615334, "best_triton_pos": 1, "best_triton_time": 0.023679999634623528, "best_triton_kernel": "triton_mm_27", "best_triton_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4"}
AUTOTUNE mm(128x4096, 4096x4096)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  mm 0.0223 ms 100.0%
  triton_mm_27 0.0237 ms 94.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_31 0.0270 ms 82.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_23 0.0304 ms 73.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_37 0.0322 ms 69.4% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_26 0.0402 ms 55.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_30 0.0416 ms 53.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_20 0.0420 ms 53.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=32, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4
  triton_mm_22 0.0426 ms 52.4% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_36 0.0432 ms 51.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
SingleProcess AUTOTUNE benchmarking takes 0.2848 seconds and 0.4028 seconds precompiling for 20 choices
Autotune Choices Stats:
{"num_choices": 20, "num_triton_choices": 19, "best_kernel": "triton_mm_49", "best_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4", "best_time": 0.07558400183916092, "best_triton_pos": 0}
AUTOTUNE mm(128x4096, 4096x22016)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  triton_mm_49 0.0756 ms 100.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  mm 0.0760 ms 99.5%
  triton_mm_55 0.0783 ms 96.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_50 0.0801 ms 94.4% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_56 0.0829 ms 91.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_45 0.0935 ms 80.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_46 0.0965 ms 78.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_47 0.0965 ms 78.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_48 0.0991 ms 76.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8
  triton_mm_54 0.1008 ms 75.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
SingleProcess AUTOTUNE benchmarking takes 0.6501 seconds and 0.1998 seconds precompiling for 20 choices
Autotune Choices Stats:
{"num_choices": 20, "num_triton_choices": 19, "best_kernel": "mm", "best_time": 0.04975999891757965, "best_triton_pos": 1, "best_triton_time": 0.05212799832224846, "best_triton_kernel": "triton_mm_65", "best_triton_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4"}
AUTOTUNE mm(128x11008, 11008x4096)
strides: [11008, 1], [1, 11008]
dtypes: torch.float16, torch.float16
  mm 0.0498 ms 100.0%
  triton_mm_65 0.0521 ms 95.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_69 0.0578 ms 86.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_61 0.0641 ms 77.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_75 0.0711 ms 70.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_64 0.0907 ms 54.9% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_68 0.0948 ms 52.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_58 0.0961 ms 51.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=32, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4
  triton_mm_60 0.0971 ms 51.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_74 0.0985 ms 50.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
SingleProcess AUTOTUNE benchmarking takes 0.6869 seconds and 0.0002 seconds precompiling for 20 choices
Autotune Choices Stats:
{"num_choices": 20, "num_triton_choices": 19, "best_kernel": "triton_mm_93", "best_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4", "best_time": 0.10380800068378448, "best_triton_pos": 0}
AUTOTUNE mm(128x4096, 4096x32000)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  triton_mm_93 0.1038 ms 100.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_94 0.1048 ms 99.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  mm 0.1060 ms 97.9%
  triton_mm_88 0.1084 ms 95.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_87 0.1159 ms 89.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_83 0.1165 ms 89.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_84 0.1287 ms 80.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_92 0.1303 ms 79.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=128, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_85 0.1365 ms 76.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_89 0.1448 ms 71.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=128, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
SingleProcess AUTOTUNE benchmarking takes 0.5232 seconds and 0.3267 seconds precompiling for 20 choices
Capturing batches (bs=1 avail_mem=36.51 GB):  75%|███████▌  | 3/4 [00:25<00:09,  9.26s/it]Autotune Choices Stats:
{"num_choices": 18, "num_triton_choices": 17, "best_kernel": "mm", "best_time": 0.047359999269247055, "best_triton_pos": 1, "best_triton_time": 0.04831999912858009, "best_triton_kernel": "triton_mm_107", "best_triton_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4"}
AUTOTUNE mm(64x4096, 4096x12288)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  mm 0.0474 ms 100.0%
  triton_mm_107 0.0483 ms 98.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_111 0.0487 ms 97.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_103 0.0492 ms 96.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_99 0.0510 ms 92.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_102 0.0549 ms 86.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_106 0.0557 ms 85.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_96 0.0562 ms 84.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=32, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4
  triton_mm_98 0.0623 ms 76.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_97 0.0644 ms 73.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=32, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
SingleProcess AUTOTUNE benchmarking takes 0.2870 seconds and 0.2329 seconds precompiling for 18 choices
Autotune Choices Stats:
{"num_choices": 18, "num_triton_choices": 17, "best_kernel": "mm", "best_time": 0.021695999428629875, "best_triton_pos": 1, "best_triton_time": 0.022463999688625336, "best_triton_kernel": "triton_mm_116", "best_triton_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4"}
AUTOTUNE mm(64x4096, 4096x4096)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  mm 0.0217 ms 100.0%
  triton_mm_116 0.0225 ms 96.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_120 0.0236 ms 91.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_124 0.0267 ms 81.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_128 0.0301 ms 72.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_119 0.0388 ms 55.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_113 0.0392 ms 55.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=32, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4
  triton_mm_123 0.0403 ms 53.9% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_115 0.0409 ms 53.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_114 0.0425 ms 51.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=32, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
SingleProcess AUTOTUNE benchmarking takes 0.2565 seconds and 0.2886 seconds precompiling for 18 choices
Autotune Choices Stats:
{"num_choices": 18, "num_triton_choices": 17, "best_kernel": "triton_mm_137", "best_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4", "best_time": 0.07507199794054031, "best_triton_pos": 0}
AUTOTUNE mm(64x4096, 4096x22016)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  triton_mm_137 0.0751 ms 100.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_140 0.0751 ms 100.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  mm 0.0754 ms 99.5%
  triton_mm_136 0.0754 ms 99.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_141 0.0763 ms 98.4% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_145 0.0797 ms 94.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_133 0.0828 ms 90.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_139 0.0909 ms 82.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8
  triton_mm_142 0.0937 ms 80.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_143 0.0942 ms 79.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8
SingleProcess AUTOTUNE benchmarking takes 0.4005 seconds and 0.1353 seconds precompiling for 18 choices
Autotune Choices Stats:
{"num_choices": 18, "num_triton_choices": 17, "best_kernel": "triton_mm_150", "best_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4", "best_time": 0.04793599992990494, "best_triton_pos": 0}
AUTOTUNE mm(64x11008, 11008x4096)
strides: [11008, 1], [1, 11008]
dtypes: torch.float16, torch.float16
  triton_mm_150 0.0479 ms 100.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  mm 0.0487 ms 98.5%
  triton_mm_154 0.0493 ms 97.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_158 0.0552 ms 86.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_162 0.0649 ms 73.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_153 0.0893 ms 53.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_149 0.0899 ms 53.3% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_148 0.0920 ms 52.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=32, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_157 0.0921 ms 52.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_147 0.0931 ms 51.5% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=32, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4
SingleProcess AUTOTUNE benchmarking takes 0.4294 seconds and 0.0003 seconds precompiling for 18 choices
Autotune Choices Stats:
{"num_choices": 18, "num_triton_choices": 17, "best_kernel": "triton_mm_179", "best_kernel_desc": "ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8", "best_time": 0.10044799745082855, "best_triton_pos": 0}
AUTOTUNE mm(64x4096, 4096x32000)
strides: [4096, 1], [1, 4096]
dtypes: torch.float16, torch.float16
  triton_mm_179 0.1004 ms 100.0% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8
  triton_mm_174 0.1006 ms 99.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_175 0.1009 ms 99.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=4
  triton_mm_170 0.1012 ms 99.2% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8
  triton_mm_171 0.1019 ms 98.6% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  mm 0.1030 ms 97.5%
  triton_mm_167 0.1103 ms 91.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4
  triton_mm_172 0.1181 ms 85.1% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_176 0.1213 ms 82.8% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4
  triton_mm_173 0.1327 ms 75.7% ACC_TYPE='tl.float32', ALLOW_TF32=False, BLOCK_K=32, BLOCK_M=64, BLOCK_N=128, EVEN_K=True, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8
SingleProcess AUTOTUNE benchmarking takes 0.4089 seconds and 0.2858 seconds precompiling for 18 choices
Capturing batches (bs=1 avail_mem=36.51 GB): 100%|██████████| 4/4 [00:43<00:00, 10.85s/it]
[2026-02-04 11:22:19] SPECULATIVE_MOE_RUNNER_BACKEND is not initialized, using auto backend
[2026-02-04 11:22:19] SPECULATIVE_MOE_A2A_BACKEND is not initialized, using none backend
Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.18s/it]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.18s/it]

Capturing batches (bs=1 avail_mem=35.30 GB): 100%|██████████| 4/4 [00:12<00:00,  3.08s/it]
Capturing batches (bs=1 avail_mem=53.80 GB): 100%|██████████| 4/4 [00:00<00:00, 13.13it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)

print_highlight(f"Response: {response}")
```

**Response: ChatCompletion(id='e5df50adca58406f92cbeee8a43e6efa', choices=\[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content=' Sure! Here are three countries and their capitals:\\n\\n1. Country: France\\nCapital: Paris\\n2. Country: Japan\\nCapital: Tokyo\\n3. Country: Brazil\\nCapital: Brasília', refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=None, reasoning\_content=None), matched\_stop=2)], created=1770204163, model='meta-llama/Llama-2-7b-chat-hf', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=48, prompt\_tokens=17, total\_tokens=65, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

```
terminate_process(server_process)
```

## EAGLE-2 Decoding via Frequency-Ranked Speculative Sampling[#](#EAGLE-2-Decoding-via-Frequency-Ranked-Speculative-Sampling "Link to this heading")

By employing a truncated high-frequency token vocabulary in the draft model, Eagle speculative decoding reduces `lm_head` computational overhead while accelerating the pipeline without quality degradation. For more details, checkout [the paper](https://arxiv.org/pdf/arXiv:2502.14856).

In our implementation, set `--speculative-token-map` to enable the optimization. You can get the high-frequency token in FR-Spec from [this model](https://huggingface.co/thunlp/LLaMA3-Instruct-8B-FR-Spec). Or you can obtain high-frequency token by directly downloading these token from [this repo](https://github.com/thunlp/FR-Spec/tree/main?tab=readme-ov-file#prepare-fr-spec-vocabulary-subset).

Thanks for the contribution from [Weilin Zhao](https://github.com/Achazwl) and [Zhousx](https://github.com/Zhou-sx).

```
server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model meta-llama/Meta-Llama-3-8B-Instruct --speculative-algorithm EAGLE \
    --speculative-draft-model-path lmsys/sglang-EAGLE-LLaMA3-Instruct-8B --speculative-num-steps 5 \
    --speculative-eagle-topk 8 --speculative-num-draft-tokens 64 --speculative-token-map thunlp/LLaMA3-Instruct-8B-FR-Spec/freq_32768.pt \
    --mem-fraction 0.7 --cuda-graph-max-bs 2 --dtype float16  --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:22:48] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:48] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:48] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:22:51] WARNING model_config.py:1134: Casting torch.bfloat16 to torch.float16.
[2026-02-04 11:22:51] INFO server_args.py:1796: Attention backend not specified. Use flashinfer backend by default.
[2026-02-04 11:22:51] WARNING server_args.py:2304: Overlap scheduler is disabled when spec v2 is off or using unsupported speculative algorithm. You can set env SGLANG_ENABLE_SPEC_V2=True to enable the experimental overlap scheduler.
[2026-02-04 11:22:51] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:22:51] Casting torch.bfloat16 to torch.float16.
[2026-02-04 11:22:57] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:57] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:57] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:22:57] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:22:57] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:22:57] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:22:59] Casting torch.bfloat16 to torch.float16.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:23:00] Casting torch.bfloat16 to torch.float16.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:23:03] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:23:03] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:23:03] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:23:03] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:05<00:15,  5.10s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:11<00:11,  5.65s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:17<00:05,  5.85s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:18<00:00,  4.10s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:18<00:00,  4.66s/it]

Capturing batches (bs=1 avail_mem=41.15 GB): 100%|██████████| 4/4 [00:00<00:00,  6.59it/s]
[2026-02-04 11:23:24] SPECULATIVE_MOE_RUNNER_BACKEND is not initialized, using auto backend
[2026-02-04 11:23:24] SPECULATIVE_MOE_A2A_BACKEND is not initialized, using none backend
[2026-02-04 11:23:24] Warning: Target model's context_length (8192) is greater than the derived context_length (2048). This may lead to incorrect model outputs or CUDA errors. Note that the derived context_length may differ from max_position_embeddings in the model's config.
[2026-02-04 11:23:24] Overriding the draft model's max_position_embeddings to 8192.
Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.00it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.00it/s]

Capturing batches (bs=1 avail_mem=20.64 GB): 100%|██████████| 4/4 [00:07<00:00,  1.85s/it]
Capturing batches (bs=1 avail_mem=20.44 GB): 100%|██████████| 4/4 [00:00<00:00, 49.34it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)

print_highlight(f"Response: {response}")
```

**Response: ChatCompletion(id='bfbe7d065ade429ca2fc641abe31c84b', choices=\[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Here are 3 countries and their capitals:\\n\\n1. \*\*France\** - \*\*Paris\*\*\\n2. \*\*Japan\** - \*\*Tokyo\*\*\\n3. \*\*Australia\** - \*\*Canberra\*\*', refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=None, reasoning\_content=None), matched\_stop=128009)], created=1770204224, model='meta-llama/Meta-Llama-3-8B-Instruct', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=39, prompt\_tokens=18, total\_tokens=57, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

```
terminate_process(server_process)
```

## EAGLE-3 Decoding[#](#EAGLE-3-Decoding "Link to this heading")

You can enable EAGLE-3 decoding by setting `--speculative-algorithm EAGLE3` and choosing an appropriate model.

```
server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model meta-llama/Llama-3.1-8B-Instruct  --speculative-algorithm EAGLE3 \
    --speculative-draft-model-path jamesliu1/sglang-EAGLE3-Llama-3.1-Instruct-8B --speculative-num-steps 5 \
        --speculative-eagle-topk 8 --speculative-num-draft-tokens 32 --mem-fraction 0.6 \
        --cuda-graph-max-bs 2 --dtype float16 --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:23:49] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:23:49] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:23:49] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:23:52] WARNING model_config.py:1134: Casting torch.bfloat16 to torch.float16.
[2026-02-04 11:23:52] INFO server_args.py:1796: Attention backend not specified. Use flashinfer backend by default.
[2026-02-04 11:23:52] WARNING server_args.py:2304: Overlap scheduler is disabled when spec v2 is off or using unsupported speculative algorithm. You can set env SGLANG_ENABLE_SPEC_V2=True to enable the experimental overlap scheduler.
[2026-02-04 11:23:52] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:23:52] Casting torch.bfloat16 to torch.float16.
[2026-02-04 11:23:58] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:23:58] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:23:58] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:23:58] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:23:58] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:23:58] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:24:00] Casting torch.bfloat16 to torch.float16.
[2026-02-04 11:24:01] Casting torch.bfloat16 to torch.float16.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:24:04] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:24:04] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:24:04] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:24:04] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:04<00:12,  4.33s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:08<00:08,  4.40s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:13<00:04,  4.36s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:14<00:00,  3.14s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:14<00:00,  3.59s/it]

Capturing batches (bs=1 avail_mem=43.25 GB): 100%|██████████| 4/4 [00:00<00:00,  6.78it/s]
[2026-02-04 11:24:21] SPECULATIVE_MOE_RUNNER_BACKEND is not initialized, using auto backend
[2026-02-04 11:24:21] SPECULATIVE_MOE_A2A_BACKEND is not initialized, using none backend
[2026-02-04 11:24:21] Warning: Target model's context_length (131072) is greater than the derived context_length (2048). This may lead to incorrect model outputs or CUDA errors. Note that the derived context_length may differ from max_position_embeddings in the model's config.
[2026-02-04 11:24:21] Overriding the draft model's max_position_embeddings to 131072.
Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.91it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.91it/s]

Capturing batches (bs=1 avail_mem=41.24 GB): 100%|██████████| 4/4 [00:05<00:00,  1.36s/it]
Capturing batches (bs=1 avail_mem=40.42 GB): 100%|██████████| 4/4 [00:00<00:00, 56.82it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)

print_highlight(f"Response: {response}")
```

**Response: ChatCompletion(id='71783f1290c441779f439db059262be1', choices=\[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Here are 3 countries and their capitals:\\n\\n1. Country: Japan\\n Capital: Tokyo\\n\\n2. Country: Australia\\n Capital: Canberra\\n\\n3. Country: Brazil\\n Capital: Brasília', refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=None, reasoning\_content=None), matched\_stop=128009)], created=1770204276, model='meta-llama/Meta-Llama-3.1-8B-Instruct', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=43, prompt\_tokens=43, total\_tokens=86, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

```
terminate_process(server_process)
```

### Multi Token Prediction[#](#Multi-Token-Prediction "Link to this heading")

We support [MTP(Multi-Token Prediction)](https://arxiv.org/pdf/2404.19737) in SGLang by using speculative decoding. We use Xiaomi/MiMo-7B-RL model as example here (deepseek mtp usage refer to [deepseek doc](https://docs.sglang.io/basic_usage/deepseek.md#multi-token-prediction))

```
server_process, port = launch_server_cmd(
"""
    python3 -m sglang.launch_server --model-path XiaomiMiMo/MiMo-7B-RL --host 0.0.0.0 --trust-remote-code \
    --speculative-algorithm EAGLE --speculative-num-steps 1 --speculative-eagle-topk 1 --speculative-num-draft-tokens 2 \
    --mem-fraction 0.5 --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:24:42] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:24:42] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:24:42] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:24:44] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:24:44] WARNING server_args.py:2304: Overlap scheduler is disabled when spec v2 is off or using unsupported speculative algorithm. You can set env SGLANG_ENABLE_SPEC_V2=True to enable the experimental overlap scheduler.
[2026-02-04 11:24:44] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:24:50] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:24:50] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:24:50] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:24:50] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:24:50] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:24:50] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:24:56] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:24:56] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:24:56] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:24:56] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:03<00:10,  3.50s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:06<00:06,  3.45s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:10<00:03,  3.57s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:13<00:00,  3.30s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:13<00:00,  3.38s/it]

Capturing batches (bs=1 avail_mem=46.04 GB): 100%|██████████| 4/4 [00:00<00:00,  4.97it/s]
[2026-02-04 11:25:13] SPECULATIVE_MOE_RUNNER_BACKEND is not initialized, using auto backend
[2026-02-04 11:25:13] SPECULATIVE_MOE_A2A_BACKEND is not initialized, using none backend
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:00,  4.49it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:00<00:00,  7.56it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:00<00:00,  7.19it/s]

Capturing batches (bs=1 avail_mem=44.08 GB): 100%|██████████| 4/4 [00:00<00:00, 63.83it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
importrequests

url = f"http://localhost:{port}/v1/chat/completions"

data = {
    "model": "XiaomiMiMo/MiMo-7B-RL",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
}

response = requests.post(url, json=data)
print_highlight(response.json())
```

**{'id': '16a543fe25ba47249e03e3c0f13a1be6', 'object': 'chat.completion', 'created': 1770204323, 'model': 'XiaomiMiMo/MiMo-7B-RL', 'choices': \[{'index': 0, 'message': {'role': 'assistant', 'content': '\\nOkay, so the user is asking, "What is the capital of France?" Let me start by recalling what I know about France. France is a country in Europe, right? I remember that Paris is a major city there. But wait, maybe I should double-check to be sure. Sometimes people might confuse other cities, like maybe Lyon or Marseille? But no, I think Paris is definitely the capital.\\n\\nLet me think about why Paris is the capital. It\\'s the political and cultural center. The Eiffel Tower is in Paris, which is a major landmark. Also, the French government and many international institutions are based there. The President of France resides in-uppercaseE, and the National Assembly is in Paris as well. So all these factors confirm that Paris is the capital. \\n\\nI don\\'t think there\\'s any other city that serves as the capital of France. Maybe in some historical context, but currently, it\\'s Paris. The user might be asking this question for a school project or just general knowledge. Either way, the answer is straightforward. \\n\\nWait, could there be any confusion with another country\\'s capital? For example, Germany\\'s capital is Berlin, Italy\\'s is Rome. So no, France\\'s is Paris. Yeah, that\\'s correct. I should make sure there\\'s no trick question here. Sometimes quizzes might ask about capitals of regions within France, like Provence or something, but the country\\'s capital is definitely Paris. \\n\\nSo the answer should be simple and direct. Just state that the capital of France is Paris. Maybe add a bit more detail, like its location or significance, to be helpful. But the user might just want the name. Still, providing a little context could be useful. For example, mentioning that it\\'s located in the north-central region of France, or that it\\'s one of the largest cities in Europe. But perhaps that\\'s unnecessary unless the user asks for more details. \\n\\nIn summary, the capital is Paris. No complications here. Just need to confirm and present the answer clearly.\\n\\n\\nThe capital of France is \*\*Paris\*\*, a major global city known for landmarks like the Eiffel Tower, Louvre Museum, and its vibrant cultural scene. It is strategically located in the north-central region of France and serves as the political, economic, and cultural hub of the country.', 'reasoning\_content': None, 'tool\_calls': None}, 'logprobs': None, 'finish\_reason': 'stop', 'matched\_stop': 151645}], 'usage': {'prompt\_tokens': 26, 'total\_tokens': 503, 'completion\_tokens': 477, 'prompt\_tokens\_details': None, 'reasoning\_tokens': 0}, 'metadata': {'weight\_version': 'default'}}**

```
terminate_process(server_process)
```

### References[#](#References "Link to this heading")

EAGLE process is as follows:

- Within EAGLE the draft model predicts the next feature vector, i.e. the last hidden state of the original LLM, using the feature sequence \\((f\_1, ..., f\_k)\\) and the token sequence \\((t\_2, ..., t\_{k+1})\\).
- The next token is then sampled from \\(p\_{k+2}=\\text{LMHead}(f\_{k+1})\\). Afterwards, the two sequences are extended in a tree style—branching out multiple potential continuations, with the branching factor per step controlled by the `speculative_eagle_topk` parameter—to ensure a more coherent connection of context, and are given as input again.
- EAGLE-2 additionally uses the draft model to evaluate how probable certain branches in the draft tree are, dynamically stopping the expansion of unlikely branches. After the expansion phase, reranking is employed to select only the top `speculative_num_draft_tokens` final nodes as draft tokens.
- EAGLE-3 removes the feature prediction objective, incorporates low and mid-layer features, and is trained in an on-policy manner.

This enhances drafting accuracy by operating on the features instead of tokens for more regular inputs and passing the tokens from the next timestep additionally to minimize randomness effects from sampling. Furthermore the dynamic adjustment of the draft tree and selection of reranked final nodes increases acceptance rate of draft tokens further. For more details see [EAGLE-2](https://arxiv.org/abs/2406.16858) and [EAGLE-3](https://arxiv.org/abs/2503.01840) paper.

For guidance how to train your own EAGLE model please see the [EAGLE repo](https://github.com/SafeAILab/EAGLE/tree/main?tab=readme-ov-file#train).