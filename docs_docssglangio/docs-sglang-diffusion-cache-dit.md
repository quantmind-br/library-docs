---
title: Cache-DiT Acceleration - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion/cache_dit
source: sitemap
fetched_at: 2026-05-11T05:51:27.0975646-03:00
rendered_js: false
word_count: 903
summary: This document describes how to configure and utilize the Cache-DiT acceleration engine within SGLang to optimize inference for Diffusion Transformers through caching, parallelization, and quantization strategies.
tags:
    - sglang
    - cache-dit
    - diffusion-transformers
    - model-inference
    - performance-optimization
    - parallel-computing
    - quantization
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang integrates [Cache-DiT](https://github.com/vipshop/cache-dit), a caching acceleration engine for Diffusion Transformers (DiT), to achieve up to **1.69x inference speedup** with minimal quality loss.

## Overview

**Cache-DiT** uses intelligent caching strategies to skip redundant computation in the denoising loop:

- **DBCache (Dual Block Cache)**: Dynamically decides when to cache transformer blocks based on residual differences
- **TaylorSeer**: Uses Taylor expansion for calibration to optimize caching decisions
- **SCM (Step Computation Masking)**: Step-level caching control for additional speedup

## Basic Usage

Enable Cache-DiT by exporting the environment variable and using `sglang generate` or `sglang serve` :

```
SGLANG_CACHE_DIT_ENABLED=true \
sglang generate --model-path Qwen/Qwen-Image \
    --prompt "A beautiful sunset over the mountains"
```

## Diffusers Backend

Cache-DiT supports loading acceleration configs from a custom YAML file. For diffusers pipelines (`diffusers` backend), pass the YAML/JSON path via `--cache-dit-config`. This flow requires cache-dit &gt;= 1.2.0 (`cache_dit.load_configs`).

### Single GPU inference

Define a `cache.yaml` file that contains:

- DBCache + TaylorSeer

```
cache_config:
  max_warmup_steps: 8
  warmup_interval: 2
  max_cached_steps: -1
  max_continuous_cached_steps: 2
  Fn_compute_blocks: 1
  Bn_compute_blocks: 0
  residual_diff_threshold: 0.12
  enable_taylorseer: true
  taylorseer_order: 1
```

Then apply the config with:

```
sglang generate \
  --backend diffusers \
  --model-path Qwen/Qwen-Image \
  --cache-dit-config cache.yaml \
  --prompt "A beautiful sunset over the mountains"
```

- DBCache + TaylorSeer + SCM (Step Computation Mask)

```
cache_config:
  max_warmup_steps: 8
  warmup_interval: 2
  max_cached_steps: -1
  max_continuous_cached_steps: 2
  Fn_compute_blocks: 1
  Bn_compute_blocks: 0
  residual_diff_threshold: 0.12
  enable_taylorseer: true
  taylorseer_order: 1
  # Must set the num_inference_steps for SCM. The SCM will automatically
  # generate the steps computation mask based on the num_inference_steps.
  # Reference: https://cache-dit.readthedocs.io/en/latest/user_guide/CACHE_API/#scm-steps-computation-masking
  num_inference_steps: 28
  steps_computation_mask: fast
```

- DBCache + TaylorSeer + SCM (Step Computation Mask) + Cache CFG

```
cache_config:
  max_warmup_steps: 8
  warmup_interval: 2
  max_cached_steps: -1
  max_continuous_cached_steps: 2
  Fn_compute_blocks: 1
  Bn_compute_blocks: 0
  residual_diff_threshold: 0.12
  enable_taylorseer: true
  taylorseer_order: 1
  num_inference_steps: 28
  steps_computation_mask: fast
  enable_sperate_cfg: true # e.g, Qwen-Image, Wan, Chroma, Ovis-Image, etc.
```

### Distributed inference

- 1D Parallelism

Define a parallelism only config yaml `parallel.yaml` file that contains:

```
parallelism_config:
  ulysses_size: auto
  attention_backend: native
```

Then, apply the distributed inference acceleration config from yaml. `ulysses_size: auto` means that cache-dit will auto detect the `world_size` as the ulysses\_size. Otherwise, you should manually set it as specific int number, e.g, 4. Then apply the distributed config with: (Note: please add `--num-gpus N` to specify the number of gpus for distributed inference)

```
sglang generate \
  --backend diffusers \
  --num-gpus 4 \
  --model-path Qwen/Qwen-Image \
  --cache-dit-config parallel.yaml \
  --prompt "A futuristic cityscape at sunset"
```

- 2D Parallelism

You can also define a 2D parallelism config yaml `parallel_2d.yaml` file that contains:

```
parallelism_config:
  ulysses_size: auto
  tp_size: 2
  attention_backend: native
```

Then, apply the 2D parallelism config from yaml. Here `tp_size: 2` means using tensor parallelism with size 2. The `ulysses_size: auto` means that cache-dit will auto detect the `world_size // tp_size` as the ulysses\_size.

- 3D Parallelism

You can also define a 3D parallelism config yaml `parallel_3d.yaml` file that contains:

```
parallelism_config:
  ulysses_size: 2
  ring_size: 2
  tp_size: 2
  attention_backend: native
```

Then, apply the 3D parallelism config from yaml. Here `ulysses_size: 2`, `ring_size: 2`, `tp_size: 2` means using ulysses parallelism with size 2, ring parallelism with size 2 and tensor parallelism with size 2.

- Ulysses Anything Attention

To enable Ulysses Anything Attention, you can define a parallelism config yaml `parallel_uaa.yaml` file that contains:

```
parallelism_config:
  ulysses_size: auto
  attention_backend: native
  ulysses_anything: true
```

- Ulysses FP8 Communication

For device that don’t have NVLink support, you can enable Ulysses FP8 Communication to further reduce the communication overhead. You can define a parallelism config yaml `parallel_fp8.yaml` file that contains:

```
parallelism_config:
  ulysses_size: auto
  attention_backend: native
  ulysses_float8: true
```

- Async Ulysses CP

You can also enable async ulysses CP to overlap the communication and computation. Define a parallelism config yaml `parallel_async.yaml` file that contains:

```
parallelism_config:
  ulysses_size: auto
  attention_backend: native
  ulysses_async: true # Now, only support for FLUX.1, Qwen-Image, Ovis-Image and Z-Image.
```

Then, apply the config from yaml. Here `ulysses_async: true` means enabling async ulysses CP.

- TE-P and VAE-P

You can also specify the extra parallel modules in the yaml config. For example, define a parallelism config yaml `parallel_extra.yaml` file that contains:

```
parallelism_config:
  ulysses_size: auto
  attention_backend: native
  extra_parallel_modules: ["text_encoder", "vae"]
```

### Hybrid Cache and Parallelism

Define a hybrid cache and parallel acceleration config yaml `hybrid.yaml` file that contains:

```
cache_config:
  max_warmup_steps: 8
  warmup_interval: 2
  max_cached_steps: -1
  max_continuous_cached_steps: 2
  Fn_compute_blocks: 1
  Bn_compute_blocks: 0
  residual_diff_threshold: 0.12
  enable_taylorseer: true
  taylorseer_order: 1
parallelism_config:
  ulysses_size: auto
  attention_backend: native
  extra_parallel_modules: ["text_encoder", "vae"]
```

Then, apply the hybrid cache and parallel acceleration config from yaml.

```
sglang generate \
  --backend diffusers \
  --num-gpus 4 \
  --model-path Qwen/Qwen-Image \
  --cache-dit-config hybrid.yaml \
  --prompt "A beautiful sunset over the mountains"
```

### Attention Backend

In some cases, users may want to only specify the attention backend without any other optimization configs. In this case, you can define a yaml file `attention.yaml` that only contains:

```
attention_backend: "flash" # '_flash_3' for Hopper
```

### Quantization

You can also specify the quantization config in the yaml file, required `torchao>=0.16.0`. For example, define a yaml file `quantize.yaml` that contains:

```
quantize_config: # quantization configuration for transformer modules
  # float8 (DQ), float8_weight_only, float8_blockwise, int8 (DQ), int8_weight_only, etc.
  quant_type: "float8"
  # layers to exclude from quantization (transformer). layers that contains any of the
  # keywords in the exclude_layers list will be excluded from quantization. This is useful
  # for some sensitive layers that are not robust to quantization, e.g., embedding layers.
  exclude_layers:
    - "embedder"
    - "embed"
  verbose: false # whether to print verbose logs during quantization
```

Then, apply the quantization config from yaml. Please also enable torch.compile for better performance if you are using quantization. For example:

```
sglang generate \
  --backend diffusers \
  --model-path Qwen/Qwen-Image \
  --warmup \
  --cache-dit-config quantize.yaml \
  --enable-torch-compile \
  --dit-cpu-offload false \
  --text-encoder-cpu-offload false \
  --prompt "A beautiful sunset over the mountains"
```

### Combined Configs: Cache + Parallelism + Quantization

You can also combine all the above configs together in a single yaml file `combined.yaml` that contains:

```
cache_config:
  max_warmup_steps: 8
  warmup_interval: 2
  max_cached_steps: -1
  max_continuous_cached_steps: 2
  Fn_compute_blocks: 1
  Bn_compute_blocks: 0
  residual_diff_threshold: 0.12
  enable_taylorseer: true
  taylorseer_order: 1
parallelism_config:
  ulysses_size: auto
  attention_backend: native
  extra_parallel_modules: ["text_encoder", "vae"]
quantize_config:
  quant_type: "float8"
  exclude_layers:
    - "embedder"
    - "embed"
  verbose: false
```

Then, apply the combined cache, parallelism and quantization config from yaml. Please also enable torch.compile for better performance if you are using quantization.

## Advanced Configuration

### DBCache Parameters

DBCache controls block-level caching behavior:

ParameterEnv VariableDefaultDescriptionFn`SGLANG_CACHE_DIT_FN`1Number of first blocks to always computeBn`SGLANG_CACHE_DIT_BN`0Number of last blocks to always computeW`SGLANG_CACHE_DIT_WARMUP`4Warmup steps before caching startsR`SGLANG_CACHE_DIT_RDT`0.24Residual difference thresholdMC`SGLANG_CACHE_DIT_MC`3Maximum continuous cached steps

### TaylorSeer Configuration

TaylorSeer improves caching accuracy using Taylor expansion:

ParameterEnv VariableDefaultDescriptionEnable`SGLANG_CACHE_DIT_TAYLORSEER`falseEnable TaylorSeer calibratorOrder`SGLANG_CACHE_DIT_TS_ORDER`1Taylor expansion order (1 or 2)

### Combined Configuration Example

DBCache and TaylorSeer are complementary strategies that work together, you can configure both sets of parameters simultaneously:

```
SGLANG_CACHE_DIT_ENABLED=true \
SGLANG_CACHE_DIT_FN=2 \
SGLANG_CACHE_DIT_BN=1 \
SGLANG_CACHE_DIT_WARMUP=4 \
SGLANG_CACHE_DIT_RDT=0.4 \
SGLANG_CACHE_DIT_MC=4 \
SGLANG_CACHE_DIT_TAYLORSEER=true \
SGLANG_CACHE_DIT_TS_ORDER=2 \
sglang generate --model-path black-forest-labs/FLUX.1-dev \
    --prompt "A curious raccoon in a forest"
```

### SCM (Step Computation Masking)

SCM provides step-level caching control for additional speedup. It decides which denoising steps to compute fully and which to use cached results. **SCM Presets** SCM is configured with presets:

PresetCompute RatioSpeedQuality`none`100%BaselineBest`slow`~75%~1.3xHigh`medium`~50%~2xGood`fast`~35%~3xAcceptable`ultra`~25%~4xLower

**Usage**

```
SGLANG_CACHE_DIT_ENABLED=true \
SGLANG_CACHE_DIT_SCM_PRESET=medium \
sglang generate --model-path Qwen/Qwen-Image \
    --prompt "A futuristic cityscape at sunset"
```

**Custom SCM Bins** For fine-grained control over which steps to compute vs cache:

```
SGLANG_CACHE_DIT_ENABLED=true \
SGLANG_CACHE_DIT_SCM_COMPUTE_BINS="8,3,3,2,2" \
SGLANG_CACHE_DIT_SCM_CACHE_BINS="1,2,2,2,3" \
sglang generate --model-path Qwen/Qwen-Image \
    --prompt "A futuristic cityscape at sunset"
```

**SCM Policy**

PolicyEnv VariableDescription`dynamic``SGLANG_CACHE_DIT_SCM_POLICY=dynamic`Adaptive caching based on content (default)`static``SGLANG_CACHE_DIT_SCM_POLICY=static`Fixed caching pattern

## Environment Variables

All Cache-DiT parameters can be configured via environment variables. See [Environment Variables](https://docs.sglang.io/docs/sglang-diffusion/environment_variables) for the complete list.

## Supported Models

SGLang Diffusion x Cache-DiT supports almost all models originally supported in SGLang Diffusion:

Model FamilyExample ModelsWanWan2.1, Wan2.2FluxFLUX.1-dev, FLUX.2-devZ-ImageZ-Image-TurboQwenQwen-Image, Qwen-Image-EditHunyuanHunyuanVideo

## Performance Tips

1. **Start with defaults**: The default parameters work well for most models
2. **Use TaylorSeer**: It typically improves both speed and quality
3. **Tune R threshold**: Lower values = better quality, higher values = faster
4. **SCM for extra speed**: Use `medium` preset for good speed/quality balance
5. **Warmup matters**: Higher warmup = more stable caching decisions

## Limitations

- **SGLang-native pipelines**: Distributed support (TP/SP) is not yet validated; Cache-DiT will be automatically disabled when `world_size > 1`.
- **SCM minimum steps**: SCM requires &gt;= 8 inference steps to be effective
- **Model support**: Only models registered in Cache-DiT’s BlockAdapterRegister are supported

## Troubleshooting

### SCM disabled for low step count

For models with &lt; 8 inference steps (e.g., DMD distilled models), SCM will be automatically disabled. DBCache acceleration still works.

## References

- [Cache-DiT](https://github.com/vipshop/cache-dit)
- [SGLang Diffusion](https://docs.sglang.io/docs/sglang-diffusion/performance-optimization)