---
title: Expert Parallelism — SGLang
url: https://docs.sglang.io/advanced_features/expert_parallelism.html
source: crawler
fetched_at: 2026-02-04T08:46:50.568331457-03:00
rendered_js: false
word_count: 1145
summary: This document explains the architectural implementation and optimization of Expert Parallelism in SGLang, covering backend selection, framework extensibility, and techniques for overlapping computation and communication in MoE models.
tags:
    - expert-parallelism
    - moe
    - sglang
    - distributed-inference
    - mixture-of-experts
    - gpu-optimization
    - deep-learning
category: concept
---

## Expert Parallelism[#](#expert-parallelism "Link to this heading")

Expert Parallelism (EP) in SGLang distributes expert weights across multiple devices in Mixture-of-Experts (MoE) models, addressing memory bottlenecks and enabling efficient scaling for high-performance inference. It is particularly vital for serving large-scale MoE models where tokens are dynamically routed to specialized experts across GPUs. By leveraging optimized all-to-all communication and grouped matrix multiplications (GEMMs), EP reduces latency, boosts throughput, and minimizes idle GPU time. SGLang’s EP offers strong extensibility through its modular framework, allowing seamless integration of custom kernels, backends, and optimizations without refactoring core logic, supporting diverse hardware and quantization schemes.

## Supported Backends and Selection Guidance[#](#supported-backends-and-selection-guidance "Link to this heading")

SGLang’s EP integrates diverse, highly efficient backends for different use cases, allowing fine-grained control over performance trade-offs. Users specify backends via command-line flags:

- `--moe-a2a-backend`: Selects the backend for all-to-all communication.
- `--moe-runner-backend`: Selects the backend for MoE computation.

### Backends for All-to-All Communication[#](#backends-for-all-to-all-communication "Link to this heading")

DeepEP and Mooncake backends support two modes for token dispatch: `normal` mode (optimized for prefill workloads with high throughput) and `low_latency` mode (optimized for decode workloads with low latency and CUDA Graph compatibility). MORI backend only supports `normal` mode now. Users are recommended to set `--deepep-mode auto` to enable automatic dispatch mode switching during runtime. Setting `--deepep-mode normal` or `--deepep-mode low_latency` is useful for debugging or development purposes.

Currently, DeepEP, Mooncake, `ascend_fuseep` and MORI only support cases where `ep_size = tp_size`. For hybrid EP and TP (i.e., `ep_size < tp_size`), only the `none` backend (All-Reduce or All-Gather-based dispatching) is supported.

### Backends for MoE Computation[#](#backends-for-moe-computation "Link to this heading")

### Examples[#](#examples "Link to this heading")

Launch with DeepEP and DeepGEMM for DeepSeek-V3:

```
python-msglang.launch_server--model-pathdeepseek-ai/DeepSeek-V3--moe-a2a-backenddeepep--moe-runner-backenddeep_gemm--tp8--ep8
```

## Extensible EP Framework[#](#extensible-ep-framework "Link to this heading")

SGLang’s EP framework provides modular abstractions for easy integration of custom kernels, backends, and optimizations. It decouples the MoE forward pass into stages (dispatch → pre-permute → core runner → post-permute → combine), enabling seamless extensions without refactoring core logic.

### Framework Overview[#](#framework-overview "Link to this heading")

The framework centers on `FusedMoE` as the unified entry point for a single, extensible structure. Key components include:

- **Dispatcher**: Manages dispatch/combine for backends like DeepEP (implements `BaseDispatcher` subclasses).
- **MoeRunner**: Orchestrates grouped-GEMM execution via `MoeRunnerCore` implementations (e.g., `TritonRunnerCore`).
- **PermuteMethodPool**: Auto-registers layout conversions (e.g., pre/post-permute via `register_pre_permute` and `register_post_permute` for dynamic modes, or `register_fused_func` for static, torch.compile-compatible fused operations).
- **TopK Router**: Backend-agnostic expert selection.

This design supports multiple backends via `--moe-a2a-backend` and `--moe-runner-backend`, with quantization integrated through a standardized `apply()` method. The computation flow ensures modularity:

```
[input_hidden_states]
          |
          v
     TopK.forward -> select_experts / triton_kernels.routing / bypass
          |
          v
     [TopKOutput]
          |
          v
   FusedMoE.forward -> Dispatcher.dispatch -> DeepEP / bypass
          |                     |
          |                     v
          |              [DispatchOutput]
          |                     |
          |                     v
          |             quant_method.apply -> MoeRunner.forward
          |                     |              |
          |                     |              v
          |                     | pre-permute + grouped_gemm + post-permute
          |                     |              |
          |                     |--------------
          |                     v
          |               [CombineInput]
          |                     |
          |                     v
          |            Dispatcher.combine -> DeepEP / bypass
          |                     |
          |---------------------
          v
[final_hidden_states]
```

For details, see the [MoE Refactor Roadmap](https://github.com/sgl-project/sglang/issues/8715).

### Implementing New Backends[#](#implementing-new-backends "Link to this heading")

To add a new backend:

1. For a new all-to-all dispatcher, implement a `BaseDispatcher` subclass with `dispatch` and `combine` methods.
2. For a new MoE runner backend, define a `MoeRunnerCore` subclass for core operations (e.g., grouped GEMMs).
3. Define new input/output formats for the dispatcher or model runner (e.g., `RunnerInput`, `RunnerOutput`).
4. Register permute/unpermute methods to ensure compatibility:
   
   - **Fused Mode** (static, torch.compile-compatible): Use `register_fused_func` for end-to-end operations.
   - **Permute Mode** (dynamic): Register `register_pre_permute` and `register_post_permute` for flexible layouts.

See the [MoE Refactor Implementation PR](https://github.com/sgl-project/sglang/pull/9269) for full changes, including type hints and config expansions.

### Examples[#](#id1 "Link to this heading")

For an example implementation, see [moe\_runner/triton.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/layers/moe/moe_runner/triton.py), which demonstrates Triton-based grouped GEMMs with registered fused and permutation functions.

## Computation and Communication Overlap[#](#computation-and-communication-overlap "Link to this heading")

SGLang’s EP employs advanced overlap techniques to hide communication latency behind computation, maximizing GPU utilization in MoE layers.

### Two-Batch Overlap (TBO)[#](#two-batch-overlap-tbo "Link to this heading")

TBO splits requests into micro-batches, interleaving attention computation with dispatch/combine operations. Yield points in the execution graph allow pausing for overlaps, increasing overall throughput without peak memory spikes:

```
operations = [
    self._forward_attn,
    YieldOperation(),  # Overlap with dispatch of prior micro-batch
    self._forward_dispatch,
    self._forward_mlp,
    YieldOperation(),  # Overlap with combine
    self._forward_combine,
]
```

Users need to specify `--enable-two-batch-overlap` to unlock up to 2x throughput. For details, see the [Large-Scale EP Blog](https://lmsys.org/blog/2025-05-05-large-scale-ep/#two-batch-overlap).

### Single-Batch Overlap (SBO)[#](#single-batch-overlap-sbo "Link to this heading")

SGLang introduces a dispatcher-hook system for Single-Batch Overlap (SBO), enabling the overlap of operations within a single batch—such as shared experts computation with communication—while decentralizing logic to enhance modularity. These hooks execute before and after the `dispatch` and `combine` operations without modifying core MoE modules. This design simplifies interfaces, reduces coupling, and improves extensibility. For implementation details and an example of overlapping shared experts with DeepEP’s combine operation, refer to [PR #13327](https://github.com/sgl-project/sglang/pull/13327). Users can set `--enable-single-batch-overlap` to enable this feature.

## Workload Balancer[#](#workload-balancer "Link to this heading")

SGLang integrates the [Expert Parallelism Load Balancer (EPLB)](https://github.com/deepseek-ai/EPLB) from DeepSeek to address routing imbalances in MoE models. By analyzing expert activation statistics, EPLB computes an optimal expert arrangement, strategically placing or replicating experts to minimize GPU utilization variance, reduce idle cycles, and enhance scalability.

To enable EPLB, use the flags `--enable-eplb`. For optimal performance, increase batch sizes to stabilize activation statistics and configure periodic rebalancing (e.g., every 1000 requests) to adapt to evolving workloads. Simulations demonstrate significant improvements in load balancedness (ratio of mean to max computation time), correlating strongly with throughput gains.

For more details, refer to the [EPLB Section in the Large-Scale EP Blog](https://lmsys.org/blog/2025-05-05-large-scale-ep/#expert-parallelism-load-balancer) and the [EPLB Repository](https://github.com/deepseek-ai/eplb).

## EP with Spectulative Decoding[#](#ep-with-spectulative-decoding "Link to this heading")

When utilizing speculative decoding with MTP on MoE architectures, use the `--speculative-moe-runner-backend` and `--speculative-moe-a2a-backend` arguments to customize the MoE layer behavior for the draft model. While they default to the target model’s settings, users can differentiate them for varying precisions between target and draft models.

For model like `nvidia/DeepSeek-R1-0528-NVFP4-v2`, the target model uses NVFP4 precision while the draft model uses BF16. To apply `flashinfer_trtllm` kernel for target MoE layer while falling back to triton fused MoE kernel for draft MoE layer, users can set the arguments as follows:

```
...
--moe-runner-backend flashinfer_trtllm \
--speculative-moe-runner-backend triton \
...
```

## Ascend NPU Guidance[#](#ascend-npu-guidance "Link to this heading")

### Guidance on SGLang configuration in Ascend NPU[#](#guidance-on-sglang-configuration-in-ascend-npu "Link to this heading")

- `--moe-a2a-backend` only supports `deepep` and `ascend_fuseep` backends,
  
  - `deepep`: The mechanism is consistent with the above description.
  - `ascend_fuseep`: Offer a large fused operator which integrates all operations between dispatch and combine to boost MoE computation. Only used for decode stage in PD Disaggregation Mode.
- `--moe-runner-backend` parameter does not need to be configured.
- `--deepep-mode`:
  
  - In PD mixed mode, please set `--deepep-mode auto`.
  - In PD Disaggregation Mode, prefill instance sets `--deepep-mode normal`, and decode instance sets `--deepep-mode low_latency`.

### DeepEP Ascend Introduction[#](#deepep-ascend-introduction "Link to this heading")

DeepEP Ascend is the adapted version of the DeepEP communication library for Huawei Ascend NPUs, specifically designed for Mixture-of-Experts (MoE) model Expert Parallelism (EP). It supports the Ant-moving Function (Split the sequence length into rounds for streaming batch transmission) to optimize the buffer size occupied during collective communication in prefill stage, especially for long sequences.

Ant-moving Function can be enabled for both the dispatch and combine phases via the following environment variables:

- `DEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS`: Enable ant-moving function in dispatch stage. Indicates the number of tokens transmitted per round on each rank, default 8192.
- `DEEPEP_NORMAL_LONG_SEQ_ROUND`: Enable ant-moving function in dispatch stage. Indicates the number of rounds transmitted on each rank, default 1.
- `DEEPEP_NORMAL_COMBINE_ENABLE_LONG_SEQ`: Enable ant-moving function in combine stage, default 0 (means disabled).

`DEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS * DEEPEP_NORMAL_LONG_SEQ_ROUND` means input sequence length. When the input sequence length exceeds 8192, it is recommended to enable the ant-moving function in both dispatch and combine phase.

The environment variable `HCCL_BUFFSIZE` is used to configure the buffer size (MB) actually allocated. Its calculation formula is as follows:

```
# Enable Ant-moving Function
HCCL_BUFFSIZE >= 2 * (102MB + 4MB + DEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS * (hidden_size + hidden_size + hidden_size) * topk) + PADDING_BUFFSIZE

# Disable Ant-moving Function
HCCL_BUFFSIZE >= 2 * (102MB + 4MB + TOTAL_SEQ_LEN * (hidden_size + hidden_size) * topk) + PADDING_BUFFSIZE
```

Wherein the parameters are described as follows:

- `hidden_size`: hidden size in model config.
- `topk`: The number of selected routing experts.
- `TOTAL_SEQ_LEN`: input sequence length.
- `PADDING_BUFFSIZE`: A value of 20 or greater is recommended.