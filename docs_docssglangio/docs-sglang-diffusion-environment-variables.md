---
title: Environment Variables - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion/environment_variables
source: sitemap
fetched_at: 2026-05-11T05:51:25.313971957-03:00
rendered_js: false
word_count: 445
summary: This document lists the environment variables available for configuring runtime settings, platform-specific optimizations, caching acceleration, cloud storage, and CUDA debugging for SGLang diffusion models.
tags:
    - environment-variables
    - sglang
    - diffusion-models
    - configuration
    - performance-optimization
    - cuda-debugging
category: configuration
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## Runtime

Environment VariableDefaultDescription`SGLANG_DIFFUSION_TARGET_DEVICE``cuda`Target device for inference (`cuda`, `rocm`, `xpu`, `npu`, `musa`, `mps`, `cpu`)`SGLANG_DIFFUSION_ATTENTION_BACKEND`not setOverride attention backend via env var (e.g. `fa`, `torch_sdpa`, `sage_attn`)`SGLANG_DIFFUSION_ATTENTION_CONFIG`not setPath to attention backend configuration file (JSON/YAML)`SGLANG_DIFFUSION_STAGE_LOGGING`falseEnable per-stage timing logs`SGLANG_DIFFUSION_SERVER_DEV_MODE`falseEnable dev-only HTTP endpoints for debugging`SGLANG_DIFFUSION_TORCH_PROFILER_DIR`not setDirectory for torch profiler traces (absolute path). Enables profiling when set`SGLANG_DIFFUSION_CACHE_ROOT``~/.cache/sgl_diffusion`Root directory for cache files`SGLANG_DIFFUSION_CONFIG_ROOT``~/.config/sgl_diffusion`Root directory for configuration files`SGLANG_DIFFUSION_LOGGING_LEVEL``INFO`Default logging level`SGLANG_DIFFUSION_WORKER_MULTIPROC_METHOD``fork`Multiprocess context for workers (`fork` or `spawn`)`SGLANG_USE_RUNAI_MODEL_STREAMER`trueUse Run:AI model streamer for model loading

## Platform-Specific

### Apple MPS

Environment VariableDefaultDescription`SGLANG_USE_MLX`not setSet to `1` to enable MLX fused Metal kernels for norm ops on MPS

### ROCm (AMD GPUs)

Environment VariableDefaultDescription`SGLANG_USE_ROCM_VAE`falseUse AITer GroupNorm in VAE for improved performance on ROCm`SGLANG_USE_ROCM_CUDNN_BENCHMARK`falseEnable MIOpen auto-tuning for VAE conv layers on ROCm

### Quantization

Environment VariableDefaultDescription`SGLANG_DIFFUSION_FLASHINFER_FP4_GEMM_BACKEND`not setFlashInfer FP4 GEMM backend for generic NVFP4 fallback

## Caching Acceleration

These variables configure caching acceleration for Diffusion Transformer (DiT) models. SGLang supports multiple caching strategies - see [caching documentation](https://docs.sglang.io/docs/sglang-diffusion/caching-acceleration) for an overview.

### Cache-DiT Configuration

See [cache-dit documentation](https://docs.sglang.io/docs/sglang-diffusion/cache_dit) for detailed configuration.

Environment VariableDefaultDescription`SGLANG_CACHE_DIT_ENABLED`falseEnable Cache-DiT acceleration`SGLANG_CACHE_DIT_FN`1First N blocks to always compute`SGLANG_CACHE_DIT_BN`0Last N blocks to always compute`SGLANG_CACHE_DIT_WARMUP`4Warmup steps before caching`SGLANG_CACHE_DIT_RDT`0.24Residual difference threshold`SGLANG_CACHE_DIT_MC`3Max continuous cached steps`SGLANG_CACHE_DIT_TAYLORSEER`falseEnable TaylorSeer calibrator`SGLANG_CACHE_DIT_TS_ORDER`1TaylorSeer order (1 or 2)`SGLANG_CACHE_DIT_SCM_PRESET`noneSCM preset (none/slow/medium/fast/ultra)`SGLANG_CACHE_DIT_SCM_POLICY`dynamicSCM caching policy`SGLANG_CACHE_DIT_SCM_COMPUTE_BINS`not setCustom SCM compute bins`SGLANG_CACHE_DIT_SCM_CACHE_BINS`not setCustom SCM cache bins

### Cache-DiT Secondary Transformer

For dual-transformer models (e.g., Wan2.2 with high/low-noise experts), these variables configure caching for the secondary transformer. Each falls back to its primary counterpart if not set.

Environment VariableDefaultDescription`SGLANG_CACHE_DIT_SECONDARY_FN`(from primary)First N blocks to always compute`SGLANG_CACHE_DIT_SECONDARY_BN`(from primary)Last N blocks to always compute`SGLANG_CACHE_DIT_SECONDARY_WARMUP`(from primary)Warmup steps before caching`SGLANG_CACHE_DIT_SECONDARY_RDT`(from primary)Residual difference threshold`SGLANG_CACHE_DIT_SECONDARY_MC`(from primary)Max continuous cached steps`SGLANG_CACHE_DIT_SECONDARY_TAYLORSEER`(from primary)Enable TaylorSeer calibrator`SGLANG_CACHE_DIT_SECONDARY_TS_ORDER`(from primary)TaylorSeer order (1 or 2)

## Cloud Storage

These variables configure S3-compatible cloud storage for automatically uploading generated images and videos.

Environment VariableDefaultDescription`SGLANG_CLOUD_STORAGE_TYPE`not setSet to `s3` to enable cloud storage`SGLANG_S3_BUCKET_NAME`not setThe name of the S3 bucket`SGLANG_S3_ENDPOINT_URL`not setCustom endpoint URL (for MinIO, OSS, etc.)`SGLANG_S3_REGION_NAME`us-east-1AWS region name`SGLANG_S3_ACCESS_KEY_ID`not setAWS Access Key ID`SGLANG_S3_SECRET_ACCESS_KEY`not setAWS Secret Access Key

## CUDA Crash Debugging

These variables enable kernel API logging and optional input/output dumps around diffusion CUDA kernel call boundaries. They are useful when tracking down CUDA crashes such as illegal memory access, device-side assert, or shape mismatches in custom kernels.

Environment VariableDefaultDescription`SGLANG_KERNEL_API_LOGLEVEL``0`Controls crash-debug kernel API logging. `1` logs API names, `3` logs tensor metadata, `5` adds tensor statistics, and `10` also writes dump snapshots.`SGLANG_KERNEL_API_LOGDEST``stdout`Destination for crash-debug kernel API logs. Use `stdout`, `stderr`, or a file path. `%i` is replaced with the process PID.`SGLANG_KERNEL_API_DUMP_DIR``sglang_kernel_api_dumps`Output directory for level-10 kernel API dumps. `%i` is replaced with the process PID.`SGLANG_KERNEL_API_DUMP_INCLUDE`not setComma-separated wildcard patterns for kernel API names to include in level-10 dumps.`SGLANG_KERNEL_API_DUMP_EXCLUDE`not setComma-separated wildcard patterns for kernel API names to exclude from level-10 dumps.