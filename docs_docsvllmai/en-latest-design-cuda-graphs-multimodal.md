---
title: Vision Encoder (ViT) CUDA Graphs
url: https://docs.vllm.ai/en/latest/design/cuda_graphs_multimodal/
source: sitemap
fetched_at: 2026-05-07T21:12:11.802578229-03:00
rendered_js: false
word_count: 1117
summary: This document explains the encoder CUDA Graph infrastructure in vLLM, which optimizes vision model inference by pre-capturing and replaying forward passes at various token budget levels.
tags:
    - cuda-graphs
    - vision-encoder
    - multimodal-inference
    - performance-optimization
    - vllm
    - deep-learning
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/design/cuda_graphs_multimodal.md "Edit this page")

The [CUDA Graphs](https://docs.vllm.ai/en/latest/design/cuda_graphs/) infrastructure in vLLM primarily targets the **decoder** (language model) forward pass. vLLM also supports capturing the **encoder** (vision transformer) forward pass as CUDA Graphs, independently from the decoder. This is based on [Pull Request #35963](https://github.com/vllm-project/vllm/pull/35963).

Note

Encoder CUDA Graphs are orthogonal to decoder CUDA Graphs — both can be enabled simultaneously. Encoder graphs capture the vision encoder execution (e.g., ViT in Qwen3-VL), while decoder graphs capture the language model execution as described in the [CUDA Graphs design document](https://docs.vllm.ai/en/latest/design/cuda_graphs/).

## Motivation[¶](#motivation "Permanent link")

Vision encoder inference incurs CUDA kernel launch overhead on the host side. The overhead is more significant when the batch size is small or image size is small.

Encoder CUDA Graphs eliminate this overhead by pre-capturing the full encoder forward pass at multiple token budget levels during model initialization, then replaying the appropriate graph at runtime.

## Design[¶](#design "Permanent link")

The encoder CUDA Graph system uses a **budget-based capture/replay** strategy, managed by [EncoderCudaGraphManager](https://docs.vllm.ai/en/latest/api/vllm/v1/worker/encoder_cudagraph/#vllm.v1.worker.encoder_cudagraph.EncoderCudaGraphManager "            EncoderCudaGraphManager"). The system contains the following core components:

- [EncoderCudaGraphManager](https://docs.vllm.ai/en/latest/api/vllm/v1/worker/encoder_cudagraph/#vllm.v1.worker.encoder_cudagraph.EncoderCudaGraphManager "            EncoderCudaGraphManager"): orchestrates capture, replay, greedy packing, and data-parallel execution for encoder CUDA Graphs.
- [SupportsEncoderCudaGraph](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph "            SupportsEncoderCudaGraph"): a runtime-checkable protocol that models implement to opt-in to encoder CUDA Graphs.
- [BudgetGraphMetadata](https://docs.vllm.ai/en/latest/api/vllm/v1/worker/encoder_cudagraph/#vllm.v1.worker.encoder_cudagraph.BudgetGraphMetadata "            BudgetGraphMetadata            dataclass   "): holds the captured CUDA Graph and its associated I/O buffers for a single token budget level.

### Budget-based graph capture[¶](#budget-based-graph-capture "Permanent link")

Multiple CUDA Graphs are pre-captured at different **token budget** levels (e.g., `[2048, 4096, 8192, 13824]`). Each budget defines a fixed token capacity, and all budgets share the same maximum batch size (number of images). The [`BudgetGraphMetadata`](https://docs.vllm.ai/en/latest/api/vllm/v1/worker/encoder_cudagraph/#vllm.v1.worker.encoder_cudagraph.BudgetGraphMetadata "            BudgetGraphMetadata            dataclass   ") for each level stores the graph along with pre-allocated input, metadata, and output buffers:

```
@dataclass
classBudgetGraphMetadata:
    token_budget: int
    max_batch_size: int
    max_frames_per_batch: int
    graph: torch.cuda.CUDAGraph
    input_buffer: torch.Tensor       # e.g. pixel_values
    metadata_buffers: dict[str, torch.Tensor]  # e.g. embeddings, seq metadata
    output_buffer: torch.Tensor      # encoder hidden states
```

Budgets are auto-generated as power-of-2 levels from a model-provided range via `get_encoder_cudagraph_budget_range()`, with the maximum budget always included even if it does not fall on a power-of-2 boundary. Budgets can also be explicitly specified by the user via `encoder_cudagraph_token_budgets` in [`CompilationConfig`](https://docs.vllm.ai/en/latest/api/vllm/config/compilation/#vllm.config.compilation.CompilationConfig "            CompilationConfig").

### Greedy bin-packing at runtime[¶](#greedy-bin-packing-at-runtime "Permanent link")

When a batch of images arrives, the manager sorts images by output token count (smallest first) and greedily packs as many images as possible into each sub-batch while staying within the **largest** token budget and the maximum batch size. Once a sub-batch is finalized (the next image would overflow either constraint), the manager finds the **smallest** budget that fits the sub-batch's total tokens and replays the corresponding CUDA Graph. This repeats until the batch is exhausted. Images that exceed all budgets fall back to eager execution.

For each graph replay:

1. Zero the pre-allocated `input_buffer`, then copy input tensors (e.g., `pixel_values`) into it.
2. Zero `metadata_buffers`, then slice-copy precomputed values (e.g., rotary embeddings, sequence metadata).
3. Replay the CUDA Graph.
4. Clone outputs from `output_buffer` (cloning is necessary since the buffer is reused across replays).

### Data-parallel support[¶](#data-parallel-support "Permanent link")

When `mm_encoder_tp_mode="data"`, the manager distributes images across TP ranks using load-balanced assignment via `get_load_balance_assignment`, executes locally on each rank, then gathers results back in the original order via `tensor_model_parallel_all_gather`.

### Video inference support[¶](#video-inference-support "Permanent link")

Following [Pull Request #35963](https://github.com/vllm-project/vllm/pull/35963) (ViT full CUDA graph support for image inference), [Pull Request #38061](https://github.com/vllm-project/vllm/pull/38061) extends the encoder CUDA graph framework to support video inference for Qwen3-VL. Previously, the CUDA graph capture/replay path only handled image inputs (`pixel_values` + `image_grid_thw`). Video inputs use different keys (`pixel_values_videos` + `video_grid_thw`) and require larger `cu_seqlens` buffers because each video item contributes multiple frames (`T` attention sequences). This PR generalizes the protocol and manager to handle both modalities through a single shared graph manager.

Note

Video CUDA graphs are automatically disabled when EVS (Efficient Video Sampling) pruning is enabled, since EVS makes the token count data-dependent and incompatible with CUDA graph capture.

Mixed inputs (image+video) per prompt are also supported now.

## Model integration via [`SupportsEncoderCudaGraph`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph " SupportsEncoderCudaGraph")[¶](#model-integration-via-supportsencodercudagraph "Permanent link")

Models opt-in to encoder CUDA Graphs by implementing the [SupportsEncoderCudaGraph](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph "            SupportsEncoderCudaGraph") protocol. This protocol encapsulates all model-specific logic so that the manager remains model-agnostic. The protocol defines the following methods:

- `get_encoder_cudagraph_config()` — returns static configuration (supported modalities, input key, buffer keys, output hidden size).
- `get_encoder_cudagraph_budget_range(vllm_config)` — returns `(min_budget, max_budget)` for auto-inference of token budgets.
- `get_encoder_cudagraph_num_items(mm_kwargs)` — returns the number of items (e.g. images) in the batch.
- `get_encoder_cudagraph_per_item_output_tokens(mm_kwargs)` — returns per-item output token counts, used for greedy packing.
- `get_encoder_cudagraph_per_item_input_sizes(mm_kwargs)` — returns per-item input sizes (e.g. patch counts), used for DP load balancing.
- `select_encoder_cudagraph_items(mm_kwargs, indices)` — extracts a sub-batch of items by index, used during greedy packing and DP sharding.
- `prepare_encoder_cudagraph_capture_inputs(...)` — creates dummy inputs for graph capture.
- `prepare_encoder_cudagraph_replay_buffers(...)` — computes new buffer values from actual batch inputs before replay.
- `encoder_cudagraph_forward(...)` — forward pass using precomputed buffers (called during capture and replay).
- `encoder_eager_forward(...)` — fallback eager forward when no graph fits.
- `get_input_modality(...)` - return the modality of the inputs.
- `get_max_frames_per_video()` - return model-specific max frames per video.

Note

The [`SupportsEncoderCudaGraph`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph "            SupportsEncoderCudaGraph") protocol is designed to be model-agnostic. New vision encoder models can opt-in by implementing the protocol methods without modifying the manager.

**Supported models:**

Architecture Models CG for Image CG for Video `Qwen3VLForConditionalGeneration` `Qwen3-VL` ✅︎ ✅︎ `Qwen2_5_VLForConditionalGeneration` `Qwen2.5-VL` ✅︎ ✅︎

Note

Encoder CUDA Graphs have currently been tested with `--mm-encoder-attn-backend=FLASH_ATTN` and `--mm-encoder-attn-backend=FLASHINFER` on Blackwell GPUs. For Qwen2.5-VL only FA2 and FA3 has been tested.

## Configuration[¶](#configuration "Permanent link")

Three fields in [`CompilationConfig`](https://docs.vllm.ai/en/latest/api/vllm/config/compilation/#vllm.config.compilation.CompilationConfig "            CompilationConfig") control encoder CUDA Graphs:

- `cudagraph_mm_encoder` (`bool`, default `False`) — enable CUDA Graph capture for multimodal encoder. When enabled, captures the full encoder forward as a CUDA Graph for each token budget level.
- `encoder_cudagraph_token_budgets` (`list[int]`, default `[]`) — token budget levels for capture. If empty (default), auto-inferred from model architecture as power-of-2 levels. User-provided values override auto-inference.
- `encoder_cudagraph_max_vision_items_per_batch` (`int`, default `0`) — maximum number of images/videos per batch during capture. If 0 (default), auto-inferred as `max_budget // min_budget`.
- `encoder_cudagraph_max_frames_per_batch` (`int`, default `None`) — maximum number of video frames per batch during capture. If `None` (default), auto-inferred as `encoder_cudagraph_max_vision_items_per_batch * max_frames_per_video` (`max_frames_per_video` is a model-specific value according to its `processing_info`). If we limit the video count per prompt to `0`, it will also be set to `0` (i.e., fall back to image-only mode).

## Usage guide[¶](#usage-guide "Permanent link")

### Image inference[¶](#image-inference "Permanent link")

Enable encoder CUDA Graphs via `compilation_config`:

```
vllmserveQwen/Qwen3-VL-32B\
--compilation-config'{"cudagraph_mm_encoder": true}'
```

With explicit budgets:

```
vllmserveQwen/Qwen3-VL-32B\
--compilation-config'{"cudagraph_mm_encoder": true, "encoder_cudagraph_token_budgets": [2048, 4096, 8192, 13824], "encoder_cudagraph_max_vision_items_per_batch": 8}'
```

Python example:

```
importvllm

compilation_config = {
    "cudagraph_mm_encoder": True,
    # Optional: override auto-inferred budgets
    # "encoder_cudagraph_token_budgets": [2048, 4096, 8192, 13824],
    # "encoder_cudagraph_max_vision_items_per_batch": 8,
}

model = vllm.LLM(
    model="Qwen/Qwen3-VL-32B",
    compilation_config=compilation_config,
)
```

The manager tracks hit/miss statistics and logs them periodically. A "hit" means an image was processed via CUDA Graph replay; a "miss" means eager fallback (image exceeded all budgets).

### Video inference[¶](#video-inference "Permanent link")

Enable encoder CUDA Graphs via `compilation_config`:

```
vllmserveQwen/Qwen3-VL-32B\
--compilation-config'{"cudagraph_mm_encoder": true}'
```

With explicit budgets:

```
vllmserveQwen/Qwen3-VL-32B\
--compilation-config'{"cudagraph_mm_encoder": true, "encoder_cudagraph_token_budgets": [2048, 4096, 8192, 13824], "encoder_cudagraph_max_vision_items_per_batch": 8, "encoder_cudagraph_max_frames_per_batch": 64}'
```

Python example:

```
importvllm

compilation_config = {
    "cudagraph_mm_encoder": True,
    # Optional: override auto-inferred budgets
    # "encoder_cudagraph_token_budgets": [2048, 4096, 8192, 13824],
    # "encoder_cudagraph_max_vision_items_per_batch": 8,
    # "encoder_cudagraph_max_frames_per_batch": 64,
}

model = vllm.LLM(
    model="Qwen/Qwen3-VL-32B",
    compilation_config=compilation_config,
)
```

## About the Performance[¶](#about-the-performance "Permanent link")

The following benchmarks were run on Blackwell GPUs (GB200) using `vllm bench mm-processor`. See [#35963](https://github.com/vllm-project/vllm/pull/35963) for full details.

### Single GPU (1x GB200)[¶](#single-gpu-1x-gb200 "Permanent link")

Model: `Qwen/Qwen3-VL-30B-A3B-Instruct`, dataset: `lmarena-ai/VisionArena-Chat` (3000 prompts, 300 warmup), `max_model_len=32768`.

Backend Mean latency improvement P99 latency improvement FLASH\_ATTN +11.8% (5.13→4.52ms) +31.6% (9.16→6.26ms) FLASHINFER +19.6% (5.42→4.36ms) +40.3% (10.87→6.49ms)

To reproduce:

```
vllmbenchmm-processor\
--modelQwen/Qwen3-VL-30B-A3B-Instruct\
--dataset-namehf--dataset-pathlmarena-ai/VisionArena-Chat\
--num-prompts3000--num-warmups300\
--max-model-len32768--seed42\
--mm-encoder-attn-backendFLASH_ATTN\
--compilation-config'{"cudagraph_mm_encoder": true, "encoder_cudagraph_token_budgets": [512, 1024, 1536, 2048, 2560, 3072, 3584, 4096, 4864], "encoder_cudagraph_max_vision_items_per_batch": 8}'
```

### Multi-GPU (4x GB200, TP=4, DP=4)[¶](#multi-gpu-4x-gb200-tp4-dp4 "Permanent link")

Model: `Qwen/Qwen3-VL-32B-Instruct`, dataset: `random-mm` (1000 prompts, 200 warmup, 20 images/request at 336x336), `max_model_len=8192`.

Backend Mean latency improvement P99 latency improvement FLASH\_ATTN +18.4% (28.39→23.16ms) +14.0% (238.78→205.28ms) FLASHINFER +44.4% (23.24→12.91ms) +84.9% (172.41→26.05ms)

To reproduce:

```
vllmbenchmm-processor\
--modelQwen/Qwen3-VL-32B-Instruct\
--dataset-namerandom-mm\
--random-mm-base-items-per-request20\
--random-mm-num-mm-items-range-ratio0.0\
--random-mm-bucket-config'{"(336,336,1)": 1.0}'\
--num-prompts1000--num-warmups200\
--max-model-len8192--seed42\
--mm-encoder-attn-backendFLASHINFER\
--tensor-parallel-size4--mm-encoder-tp-modedata\
--compilation-config'{"cudagraph_mm_encoder": true, "encoder_cudagraph_token_budgets": [512, 1024, 1536, 2048, 2560, 3072, 3584, 4096, 4864], "encoder_cudagraph_max_vision_items_per_batch": 8}'
```

Note

Find more details about benchmarks on GPUs (A100) for video inference at [#38061](https://github.com/vllm-project/vllm/pull/38061).