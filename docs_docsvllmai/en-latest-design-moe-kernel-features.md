---
title: Fused MoE Kernel Features - vLLM
url: https://docs.vllm.ai/en/latest/design/moe_kernel_features/
source: sitemap
fetched_at: 2026-05-07T21:12:24.785032527-03:00
rendered_js: false
word_count: 1098
summary: This document provides an overview of various MoE (Mixture-of-Experts) kernels and all2all communication backends in vLLM, detailing their supported features, quantization schemes, and configuration options to assist in kernel selection.
tags:
    - moe
    - all2all
    - kernel-optimization
    - quantization
    - vllm
    - expert-parallelism
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/design/moe_kernel_features.md "Edit this page")

The purpose of this document is to provide an overview of the various MoE kernels (both modular and non-modular) so it will be easier to select an appropriate set of kernels for any particular situation. This includes information about the all2all backends used by modular kernels.

## Fused MoE Modular All2All backends[¶](#fused-moe-modular-all2all-backends "Permanent link")

There are a number of all2all communication backends that are used to implement expert parallelism (EP) for the [`FusedMoE`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/layer/#vllm.model_executor.layers.fused_moe.layer.FusedMoE "            FusedMoE") layer. The different [`FusedMoEPrepareAndFinalizeModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular "            FusedMoEPrepareAndFinalizeModular") subclasses provide an interface for each all2all backend.

The following table describes the relevant features of each backend, i.e. activation format, supported quantization schemes and async support.

The output activation format (standard or batched) corresponds to the output of the prepare step of the [`FusedMoEPrepareAndFinalizeModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular "            FusedMoEPrepareAndFinalizeModular") subclass, and the finalize step requires the same format. All the backend `prepare` methods expect activations in the standard format and all the `finalize` methods return activations in standard format. More details on the formats can be found in the [Fused MoE Modular Kernel](https://docs.vllm.ai/en/latest/design/fused_moe_modular_kernel/) document.

The quantization types and formats enumerate which quantization schemes are supported by each [`FusedMoEPrepareAndFinalizeModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular "            FusedMoEPrepareAndFinalizeModular") class. The quantization can happen before or after the dispatch based on the format the all2all backend supports, e.g. deepep\_high\_throughput supports only block-quantized fp8 format. Any other format will result in dispatching in higher precision and quantizing afterwards. The output of the prepare step for each backend is the quantized type. The finalize step generally requires the same input type as the original activations, e.g. if the original input is bfloat16 and the quantization scheme is fp8 with per-tensor scales, `prepare` will return fp8/per-tensor scale activations and `finalize` will take bfloat16 activations. See the diagrams in [Fused MoE Modular Kernel](https://docs.vllm.ai/en/latest/design/fused_moe_modular_kernel/) for more details on the types and formats of activations at each step of the MoE process. If no quantization type is specified, the kernel operates on float16 and/or bfloat16.

Async backends support the use of DBO (Dual Batch Overlap) and shared expert overlap (where shared experts are computed during the combine step).

Certain models require the topk weights to be applied to the input activations rather than the output activations when topk==1, e.g. Llama. For modular kernels, this feature is supported by the [`FusedMoEPrepareAndFinalizeModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular "            FusedMoEPrepareAndFinalizeModular") subclass. For non-modular kernels, it is up to the experts function to deal with this flag.

Unless otherwise specified, backends are controlled via the `--all2all-backend` command-line argument (or the `all2all_backend` parameter in [`ParallelConfig`](https://docs.vllm.ai/en/latest/api/vllm/config/parallel/#vllm.config.parallel.ParallelConfig "            ParallelConfig")). All backends except `flashinfer` only work with EP+DP or EP+TP. `Flashinfer` can work with EP or DP without EP.

Backend Output act. format Quant. types Quant. format Async Apply Weight On Input Subclass naive standard all1 G,A,T N 6 [layer.py](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/layer/#vllm.model_executor.layers.fused_moe.layer.FusedMoE "            FusedMoE") deepep\_high\_throughput standard fp8 G(128),A,T2 Y Y [`DeepEPHTPrepareAndFinalize`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_ht.DeepEPHTPrepareAndFinalize "            DeepEPHTPrepareAndFinalize") deepep\_low\_latency batched fp8 G(128),A,T3 Y Y [`DeepEPLLPrepareAndFinalize`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ll/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_ll.DeepEPLLPrepareAndFinalize "            DeepEPLLPrepareAndFinalize") flashinfer\_nvlink\_two\_sided standard nvfp4,fp8 G,A,T N N [`FlashInferNVLinkTwoSidedPrepareAndFinalize`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_two_sided/#vllm.model_executor.layers.fused_moe.prepare_finalize.flashinfer_nvlink_two_sided.FlashInferNVLinkTwoSidedPrepareAndFinalize "            FlashInferNVLinkTwoSidedPrepareAndFinalize") flashinfer\_nvlink\_one\_sided standard nvfp4,bf16,mxfp8 G,A,T N N [`FlashInferNVLinkOneSidedPrepareAndFinalize`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_one_sided/#vllm.model_executor.layers.fused_moe.prepare_finalize.flashinfer_nvlink_one_sided.FlashInferNVLinkOneSidedPrepareAndFinalize "            FlashInferNVLinkOneSidedPrepareAndFinalize")

Table key

1. All types: mxfp4, nvfp4, int4, int8, fp8
2. A,T quantization occurs after dispatch.
3. All quantization happens after dispatch.
4. Controlled by different env vars (`VLLM_FLASHINFER_MOE_BACKEND` "throughput" or "latency")
5. This is a no-op dispatcher that can be used to pair with any modular experts to produce a modular kernel that runs without dispatch or combine. These cannot be selected via environment variable. These are generally use for testing or adapting an expert subclass to the `fused_experts` API.
6. This depends on the experts implementation.

* * *

- G - Grouped
- G(N) - Grouped w/block size N
- A - Per activation token
- T - Per tensor

Modular kernels are supported by the following `FusedMoEMethodBase` classes.

- [`ModelOptFp8MoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/modelopt/#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8MoEMethod "            ModelOptFp8MoEMethod")
- [`Fp8MoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/fp8/#vllm.model_executor.layers.quantization.fp8.Fp8MoEMethod "            Fp8MoEMethod")
- [`CompressedTensorsW4A4Nvfp4MoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a4_nvfp4/#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w4a4_nvfp4.CompressedTensorsW4A4Nvfp4MoEMethod "            CompressedTensorsW4A4Nvfp4MoEMethod")
- [`CompressedTensorsW8A8Fp8MoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w8a8_fp8/#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w8a8_fp8.CompressedTensorsW8A8Fp8MoEMethod "            CompressedTensorsW8A8Fp8MoEMethod")
- [`GptOssMxfp4MoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/mxfp4/#vllm.model_executor.layers.quantization.mxfp4.GptOssMxfp4MoEMethod "            GptOssMxfp4MoEMethod")
- [`UnquantizedFusedMoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method/#vllm.model_executor.layers.fused_moe.unquantized_fused_moe_method.UnquantizedFusedMoEMethod "            UnquantizedFusedMoEMethod")

## Fused Experts Kernels[¶](#fused-experts-kernels "Permanent link")

There are a number of MoE experts kernel implementations for different quantization types and architectures. Most follow the general API of the base Triton [`fused_experts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.fused_experts "            fused_experts") function. Many have modular kernel adapters, so they can be used with compatible all2all backends. This table lists each experts kernel and its particular properties.

Each kernel must be provided with one of the supported input activation formats. Some flavors of kernels support both standard and batched formats through different entry points, e.g. [`TritonExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.TritonExperts "            TritonExperts") and [`BatchedTritonExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_batched_moe/#vllm.model_executor.layers.fused_moe.fused_batched_moe.BatchedTritonExperts "            BatchedTritonExperts"). Batched format kernels are currently only needed for matching with certain all2all backends, e.g. [`DeepEPLLPrepareAndFinalize`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ll/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_ll.DeepEPLLPrepareAndFinalize "            DeepEPLLPrepareAndFinalize").

Similar to the backend kernels, each experts kernel only supports certain quantization formats. For non-modular experts, the activations will be in the original type and quantized internally by the kernel. Modular experts will expect the activations to already be in the quantized format. Both types of experts will yield outputs in the original activation type.

Each experts kernel supports one or more activation functions, e.g. silu or gelu, which are applied to the intermediate results.

As with the backends, some experts support applying topk weights on the input activations. The entries in the column in this table only apply to the non-modular experts.

Most experts flavors include an equivalent modular interface which will be a subclass of [`FusedMoEExpertsModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular "            FusedMoEExpertsModular").

To be used with a particular [`FusedMoEPrepareAndFinalizeModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular "            FusedMoEPrepareAndFinalizeModular") subclass, MoE kernels must have compatible activation formats, quantization types and quantization formats.

Kernel Input act. format Quant. types Quant. format Activation function Apply Weight On Input Modular Source triton standard all1 G,A,T silu, gelu,  
swigluoai,  
silu\_no\_mul,  
gelu\_no\_mul Y Y [`fused_experts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.fused_experts "            fused_experts"),  
[`TritonExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.TritonExperts "            TritonExperts") triton (batched) batched all1 G,A,T silu, gelu 6 Y [`BatchedTritonExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_batched_moe/#vllm.model_executor.layers.fused_moe.fused_batched_moe.BatchedTritonExperts "            BatchedTritonExperts") deep gemm standard,  
batched fp8 G(128),A,T silu, gelu 6 Y  
[`DeepGemmExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe/#vllm.model_executor.layers.fused_moe.experts.deep_gemm_moe.DeepGemmExperts "            DeepGemmExperts"),  
[`BatchedDeepGemmExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe/#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts "            BatchedDeepGemmExperts") cutlass\_fp4 standard,  
batched nvfp4 A,T silu Y Y [`CutlassExpertsFp4`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsFp4 "            CutlassExpertsFp4") cutlass\_fp8 standard,  
batched fp8 A,T silu, gelu Y Y [`CutlassExpertsFp8`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsFp8 "            CutlassExpertsFp8"),  
[`CutlasBatchedExpertsFp8`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassBatchedExpertsFp8 "            CutlassBatchedExpertsFp8") flashinfer standard nvfp4,  
fp8 T 5 N Y [`FlashInferExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe/#vllm.model_executor.layers.fused_moe.flashinfer_cutlass_moe.FlashInferExperts "            FlashInferExperts") gpt oss triton standard N/A N/A 5 Y Y [`triton_kernel_fused_experts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe/#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.triton_kernel_fused_experts "            triton_kernel_fused_experts"),  
[`OAITritonExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe/#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.OAITritonExperts "            OAITritonExperts") marlin standard,  
batched 3 / N/A 3 / N/A silu,  
swigluoai Y Y [`fused_marlin_moe`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.fused_marlin_moe "            fused_marlin_moe"),  
[`MarlinExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.MarlinExperts "            MarlinExperts"),  
[`BatchedMarlinExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.BatchedMarlinExperts "            BatchedMarlinExperts") trtllm standard mxfp4,  
nvfp4 G(16),G(32) 5 N Y [`TrtLlmMxfp4ExpertsMonolithic`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_mxfp4_moe.TrtLlmMxfp4ExpertsMonolithic "            TrtLlmMxfp4ExpertsMonolithic"),  
[`TrtLlmMxfp4ExpertsModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_mxfp4_moe.TrtLlmMxfp4ExpertsModular "            TrtLlmMxfp4ExpertsModular"),  
[`TrtLlmNvFp4ExpertsMonolithic`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsMonolithic "            TrtLlmNvFp4ExpertsMonolithic"),  
[`TrtLlmNvfp4ExpertsModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsModular "            TrtLlmNvFp4ExpertsModular") rocm aiter moe standard mxfp4,  
fp8 G(32),G(128),A,T silu, gelu,  
swigluoai Y N `rocm_aiter_fused_experts`,  
`AiterExperts` cpu\_fused\_moe standard N/A N/A silu N N [`CPUFusedMOE`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/cpu_fused_moe/#vllm.model_executor.layers.fused_moe.cpu_fused_moe.CPUFusedMOE "            CPUFusedMOE") naive batched4 batched int8,  
fp8 G,A,T silu, gelu 6 Y [`NaiveBatchedExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_batched_moe/#vllm.model_executor.layers.fused_moe.fused_batched_moe.NaiveBatchedExperts "            NaiveBatchedExperts")

Table key

1. All types: mxfp4, nvfp4, int4, int8, fp8
2. A dispatcher wrapper around triton and deep gemm experts. Will select based on type + shape + quantization params
3. uint4, uint8, fp8, fp4
4. This is a naive implementation of experts that supports batched format. Mainly used for testing.
5. The `activation` parameter is ignored and SwiGlu is used by default instead.
6. Only handled by or supported when used with modular kernels.

## Modular Kernel "families"[¶](#modular-kernel-families "Permanent link")

The following table shows "families" of modular kernels that are intended to work together. There are some combinations which may work but have not yet been tested, e.g. flashinfer with other fp8 experts.

backend [`FusedMoEPrepareAndFinalizeModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular "            FusedMoEPrepareAndFinalizeModular") subclasses [`FusedMoEExpertsModular`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular "            FusedMoEExpertsModular") subclasses deepep\_high\_throughput [`DeepEPHTPrepareAndFinalize`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_ht.DeepEPHTPrepareAndFinalize "            DeepEPHTPrepareAndFinalize") [`DeepGemmExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe/#vllm.model_executor.layers.fused_moe.experts.deep_gemm_moe.DeepGemmExperts "            DeepGemmExperts"),  
[`TritonExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.TritonExperts "            TritonExperts"),  
[`TritonOrDeepGemmExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/triton_deep_gemm_moe/#vllm.model_executor.layers.fused_moe.triton_deep_gemm_moe.TritonOrDeepGemmExperts "            TritonOrDeepGemmExperts"),  
[`CutlassExpertsFp8`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsFp8 "            CutlassExpertsFp8"),  
[`MarlinExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.MarlinExperts "            MarlinExperts") deepep\_low\_latency [`DeepEPLLPrepareAndFinalize`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ll/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_ll.DeepEPLLPrepareAndFinalize "            DeepEPLLPrepareAndFinalize") `BatchedDeepGemmExperts`,  
[`BatchedTritonExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_batched_moe/#vllm.model_executor.layers.fused_moe.fused_batched_moe.BatchedTritonExperts "            BatchedTritonExperts"),  
[`CutlassBatchedExpertsFp8`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassBatchedExpertsFp8 "            CutlassBatchedExpertsFp8"),  
[`BatchedMarlinExperts`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.BatchedMarlinExperts "            BatchedMarlinExperts") flashinfer `FlashInferCutlassMoEPrepareAndFinalize` `FlashInferExperts`