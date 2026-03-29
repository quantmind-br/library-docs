---
title: Cuda Graph for Multi-Modal Encoder in SGLang — SGLang
url: https://docs.sglang.io/advanced_features/cuda_graph_for_multi_modal_encoder.html
source: crawler
fetched_at: 2026-02-04T08:46:58.037368156-03:00
rendered_js: false
word_count: 497
summary: This document explains the implementation and configuration of CUDA Graph for vision transformers in SGLang to reduce kernel launch overhead and improve performance in multi-modal models.
tags:
    - sglang
    - cuda-graph
    - vision-transformer
    - vit
    - gpu-optimization
    - multimodal-reasoning
category: guide
---

## Contents

## Cuda Graph for Multi-Modal Encoder in SGLang[#](#cuda-graph-for-multi-modal-encoder-in-sglang "Link to this heading")

## Motivation[#](#motivation "Link to this heading")

In multimodal reasoning services, the visual encoder (ViT / Vision Transformer) typically has a few characteristic traits:

Many layers, fragmented operators: Each layer includes LN, QKV projections, attention, MLP, residual connections, etc., resulting in extremely frequent kernel launches.

Server-side “small batch / low latency” is common: The batch size is very small (sometimes it looks like 1 after “flattening” the batch), so kernel launch overhead accounts for a large portion of end-to-end latency.

Input token count (number of patches) varies frequently: Different image/video resolutions and different batch composition lead to different sequence lengths S — and this is precisely the biggest obstacle for CUDA Graph (unstable shapes).

The value of CUDA Graph: It captures a long sequence of GPU kernels with fixed shapes and fixed memory addresses into a graph; later, for the same shapes, it can replay the graph directly, dramatically reducing launch overhead and making GPU scheduling more compact.

This led us to seek a CUDA Graph enabled feature for ViT in order to improve ViT performance.

## Design and Restrictions[#](#design-and-restrictions "Link to this heading")

The new CUDA Graph enabled ViT logic is built on ViTCudaGraphRunner. This runner captures the “blocks + merger + deepstack merger (optional)” part of a vision transformer into a CUDA graph and replays it for identical shapes. See the following design consideration and restrictions for more details.

### Dynamic inputs to fit static constraints of CUDA Graph[#](#dynamic-inputs-to-fit-static-constraints-of-cuda-graph "Link to this heading")

Variable sequence length S is very common in ViT. While CUDA Graph requires fixed shapes. The solution is to build a graph cache by S(e.g., graph\_key = S). The first time create a new S, and then capture a graph; afterwards, replay it.

If there are many distinct S values, we need to increase VRAM usage which is graph-private memory pools for many graphs.

### Stable addresses[#](#stable-addresses "Link to this heading")

Everything “parameter-like” becomes a static buffer:

- block\_input / block\_ws / block\_output
- cu\_full\_len / cu\_window\_len and their kk variants
- sin\_cos\_ws

In this way to solve the underlying requirement: during replay, not allowed to swap tensors, can only modify tensor contents.

### Attention backend arguments[#](#attention-backend-arguments "Link to this heading")

Attention backend arguments are fixed inside the graph:

TritonAttn expects \[cu\_seqlens, cu\_seqlens\_kk, max\_len] FA3 expects \[cu\_seqlens, max\_len]

max\_len is frozen as an int constant. cu\_seqlens is cached into a dict during create\_graph(), and its contents are not updated during subsequent replays.

For the same graph\_key = S, you not only require the input shape to match, but also require the segmentation pattern in cu\_seqlens (and window seqlens) to be identical. Otherwise, attention will segment the sequence incorrectly.

### Rotary buffer management[#](#rotary-buffer-management "Link to this heading")

The feature reallocates a larger sin\_cos\_ws when seq\_len increases. The max\_content\_len is used to make sure the maximum size of the allocated rotary buffer.

## Command Example[#](#command-example "Link to this heading")

You can enable CUDA Graph for ViT by setting env variable `SGLANG_VIT_ENABLE_CUDA_GRAPH=1`, for example:

```
SGLANG_VIT_ENABLE_CUDA_GRAPH=1 \
python3 -m sglang.launch_server \
  --model Qwen/Qwen3-VL-8B-Instruct
```

Or you can run CUDA Graph for ViT together with Piecewise CUDA Graph feature by both setting env variable `SGLANG_VIT_ENABLE_CUDA_GRAPH=1` and setting `--enable-piecewise-cuda-graph`, for example:

```
SGLANG_VIT_ENABLE_CUDA_GRAPH=1 \
python3 -m sglang.launch_server \
  --model Qwen/Qwen3-VL-8B-Instruct \
  --piecewise-cuda-graph-max-tokens 4096 \
  --enable-piecewise-cuda-graph \
  --piecewise-cuda-graph-compiler eager
```

## Known supported models[#](#known-supported-models "Link to this heading")

- Qwen2.5-VL (https://github.com/sgl-project/sglang/pull/14422)
- Qwen3-VL (https://github.com/sgl-project/sglang/pull/15320)