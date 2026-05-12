---
title: encoder_cudagraph_defs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/encoder_cudagraph_defs/
source: sitemap
fetched_at: 2026-05-07T21:42:15.000444337-03:00
rendered_js: false
word_count: 301
summary: Defines the data structures used for managing CUDA graph capture, configuration, and buffer updates for encoder-based vision models.
tags:
    - cuda-graphs
    - vision-encoder
    - data-transfer-objects
    - tensor-buffers
    - vllm
category: reference
---

Data transfer objects for encoder CUDA graph management.

## EncoderCudaGraphCaptureInputs `dataclass` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphCaptureInputs "Permanent link")

Everything needed for one CUDA graph capture.

Returned by `prepare_encoder_cudagraph_capture_inputs()`.

Source code in `vllm/v1/worker/encoder_cudagraph_defs.py`

```
@dataclass
classEncoderCudaGraphCaptureInputs:
"""Everything needed for one CUDA graph capture.

    Returned by ``prepare_encoder_cudagraph_capture_inputs()``.
    """

    mm_kwargs: dict[str, Any]
"""Dummy forward inputs (model-specific keys).
    For Qwen3-VL this contains pixel_values and grid_thw."""

    buffers: dict[str, torch.Tensor]
"""Precomputed tensor buffers that will be recorded into the
    CUDA graph.  The manager stores references to these exact
    tensor objects and copies new data into them before each
    ``graph.replay()`` call (buffer identity invariant)."""
```

### buffers `instance-attribute` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphCaptureInputs.buffers "Permanent link")

Precomputed tensor buffers that will be recorded into the CUDA graph. The manager stores references to these exact tensor objects and copies new data into them before each `graph.replay()` call (buffer identity invariant).

### mm\_kwargs `instance-attribute` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphCaptureInputs.mm_kwargs "Permanent link")

Dummy forward inputs (model-specific keys). For Qwen3-VL this contains pixel\_values and grid\_thw.

## EncoderCudaGraphConfig `dataclass` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphConfig "Permanent link")

Configuration for encoder CUDA graph management.

Provided by the model at init time via `get_encoder_cudagraph_config()`. Values are fixed for the lifetime of the manager.

Source code in `vllm/v1/worker/encoder_cudagraph_defs.py`

```
@dataclass
classEncoderCudaGraphConfig:
"""Configuration for encoder CUDA graph management.

    Provided by the model at init time via
    ``get_encoder_cudagraph_config()``. Values are fixed for the
    lifetime of the manager.
    """

    modalities: list[str]
"""Supported modalities (e.g. ["image"])."""

    input_key_by_modality: dict[str, str]
"""Per-modality input tensor key mapping, e.g.
    {"image": "pixel_values", "video": "pixel_values_videos"}.
    """

    buffer_keys: list[str]
"""Keys for the tensor buffers recorded into the CUDA graph.
    Before replay the manager zeros then slice-copies new data
    into these buffers."""

    out_hidden_size: int
"""Output hidden dim of the vision encoder.
    Used for DP gather buffer allocation."""
```

### buffer\_keys `instance-attribute` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphConfig.buffer_keys "Permanent link")

Keys for the tensor buffers recorded into the CUDA graph. Before replay the manager zeros then slice-copies new data into these buffers.

### input\_key\_by\_modality `instance-attribute` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphConfig.input_key_by_modality "Permanent link")

Per-modality input tensor key mapping, e.g. {"image": "pixel\_values", "video": "pixel\_values\_videos"}.

### modalities `instance-attribute` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphConfig.modalities "Permanent link")

Supported modalities (e.g. \["image"]).

### out\_hidden\_size `instance-attribute` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphConfig.out_hidden_size "Permanent link")

Output hidden dim of the vision encoder. Used for DP gather buffer allocation.

## EncoderCudaGraphReplayBuffers `dataclass` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphReplayBuffers "Permanent link")

New buffer values for graph replay, computed by the model from actual batch inputs.

Returned by `prepare_encoder_cudagraph_replay_buffers()`. Keys match `EncoderCudaGraphConfig.buffer_keys`.

Source code in `vllm/v1/worker/encoder_cudagraph_defs.py`

```
@dataclass
classEncoderCudaGraphReplayBuffers:
"""New buffer values for graph replay, computed by the model from
    actual batch inputs.

    Returned by ``prepare_encoder_cudagraph_replay_buffers()``.
    Keys match ``EncoderCudaGraphConfig.buffer_keys``.
    """

    buffers: dict[str, torch.Tensor | None]
"""Data to copy into the captured buffers before replay.
    ``None`` values leave the corresponding captured buffer
    unchanged."""
```

### buffers `instance-attribute` [¶](#vllm.v1.worker.encoder_cudagraph_defs.EncoderCudaGraphReplayBuffers.buffers "Permanent link")

Data to copy into the captured buffers before replay. `None` values leave the corresponding captured buffer unchanged.