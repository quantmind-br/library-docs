---
title: CLI reference - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion/api/cli
source: sitemap
fetched_at: 2026-05-11T05:51:10.645721135-03:00
rendered_js: false
word_count: 632
summary: This document provides a reference for using the SGLang CLI to generate content and serve diffusion models, detailing command-line options for configuration, hardware optimization, and component management.
tags:
    - sglang
    - cli
    - diffusion-models
    - model-serving
    - command-line-interface
    - gpu-optimization
category: reference
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

Use the CLI for one-off generation with `sglang generate` or to start a persistent HTTP server with `sglang serve`.

### Overlay repos for non-diffusers models

If `--model-path` points to a supported non-diffusers source repo, SGLang can resolve it through a self-hosted overlay repo. SGLang first checks a built-in overlay registry. Concrete built-in mappings can be added over time without changing the CLI surface. Override example:

```
export SGLANG_DIFFUSION_MODEL_OVERLAY_REGISTRY='{
  "Wan-AI/Wan2.2-S2V-14B": {
    "overlay_repo_id": "your-org/Wan2.2-S2V-14B-overlay",
    "overlay_revision": "main"
  }
}'

sglang generate \
  --model-path Wan-AI/Wan2.2-S2V-14B \
  --config configs/wan_s2v.yaml
```

The overlay repo should be a complete diffusers-style/componentized repo You can also pass the overlay repo itself as `--model-path` if it contains `_overlay/overlay_manifest.json`. Notes:

1. `SGLANG_DIFFUSION_MODEL_OVERLAY_REGISTRY` is only an optional override for development and debugging. It accepts either a JSON object or a path to a JSON file, and can extend or replace built-in entries for the current process.
2. On the first load, SGLang will:
   
   - download overlay metadata from the overlay repo
   - download the required files from the original source repo
   - materialize a local standard component repo under `~/.cache/sgl_diffusion/materialized_models/`
3. Later loads reuse the materialized local repo. The materialized repo is what the runtime loads as a normal componentized model directory.

## Quick Start

### Generate

```
sglang generate \
  --model-path Qwen/Qwen-Image \
  --prompt "A beautiful sunset over the mountains" \
  --save-output
```

### Serve

```
sglang serve \
  --model-path Wan-AI/Wan2.1-T2V-1.3B-Diffusers \
  --num-gpus 4 \
  --ulysses-degree 2 \
  --ring-degree 2 \
  --port 30010
```

For request and response examples, see [OpenAI-Compatible API](https://docs.sglang.io/docs/sglang-diffusion/api/openai_api).

## Common Options

### Model and runtime

- `--model-path &#123;MODEL&#125;`: model path or Hugging Face model ID
- `--lora-path &#123;PATH&#125;` and `--lora-nickname &#123;NAME&#125;`: load a LoRA adapter
- `--num-gpus &#123;N&#125;`: number of GPUs to use
- `--tp-size &#123;N&#125;`: tensor parallelism size, mainly for encoders
- `--sp-degree &#123;N&#125;`: sequence parallelism size
- `--ulysses-degree &#123;N&#125;` and `--ring-degree &#123;N&#125;`: USP parallelism controls
- `--attention-backend &#123;BACKEND&#125;`: attention backend for native SGLang pipelines
- `--component-attention-backends &#123;MAP&#125;`: per-component attention backend overrides, for example `text_encoder=torch_sdpa,transformer=fa`
- `--attention-backend-config &#123;CONFIG&#125;`: attention backend configuration

### Sampling and output

- `--prompt &#123;PROMPT&#125;` and `--negative-prompt &#123;PROMPT&#125;`
- `--image-path &#123;PATH&#125; [&#123;PATH&#125; ...]`: input image(s) for image-to-video or image-to-image generation
- `--num-inference-steps &#123;STEPS&#125;` and `--seed &#123;SEED&#125;`
- `--height &#123;HEIGHT&#125;`, `--width &#123;WIDTH&#125;`, `--num-frames &#123;N&#125;`, `--fps &#123;FPS&#125;`
- `--output-path &#123;PATH&#125;`, `--output-file-name &#123;NAME&#125;`, `--save-output`, `--return-frames`

For frame interpolation and upscaling, see [Post-Processing](https://docs.sglang.io/docs/sglang-diffusion/api/post_processing).

### Quantized transformers

For quantized transformer checkpoints, prefer:

- `--model-path` for the base pipeline
- `--transformer-path` for a quantized `transformers` transformer component folder
- `--transformer-weights-path` for a quantized safetensors file, directory, or repo

See [Quantization](https://docs.sglang.io/docs/sglang-diffusion/quantization) for supported quantization families and examples.

## Configuration Files

Use `--config` to load JSON or YAML configuration. Command-line flags override values from the config file.

```
sglang generate --config config.yaml
```

Example:

```
model_path: FastVideo/FastHunyuan-diffusers
prompt: A beautiful woman in a red dress walking down a street
output_path: outputs/
num_gpus: 2
sp_size: 2
tp_size: 1
num_frames: 45
height: 720
width: 1280
num_inference_steps: 6
seed: 1024
fps: 24
precision: bf16
vae_precision: fp16
vae_tiling: true
vae_sp: true
enable_torch_compile: false
```

## Generate

`sglang generate` runs a single generation job and exits when the job finishes.

```
sglang generate \
  --model-path Wan-AI/Wan2.2-T2V-A14B-Diffusers \
  --text-encoder-cpu-offload \
  --pin-cpu-memory \
  --num-gpus 4 \
  --ulysses-degree 2 \
  --ring-degree 2 \
  --prompt "A curious raccoon" \
  --save-output \
  --output-path outputs \
  --output-file-name "a-curious-raccoon.mp4"
```

For diffusers pipelines, Cache-DiT can be enabled with `SGLANG_CACHE_DIT_ENABLED=true` or `--cache-dit-config`. See [Cache-DiT](https://docs.sglang.io/docs/sglang-diffusion/cache_dit).

## Serve

`sglang serve` starts the HTTP server and keeps the model loaded for repeated requests.

```
sglang serve \
  --model-path Wan-AI/Wan2.1-T2V-1.3B-Diffusers \
  --text-encoder-cpu-offload \
  --pin-cpu-memory \
  --num-gpus 4 \
  --ulysses-degree 2 \
  --ring-degree 2 \
  --port 30010
```

### Cloud Storage

SGLang Diffusion can upload generated images and videos to S3-compatible object storage after generation.

```
export SGLANG_CLOUD_STORAGE_TYPE=s3
export SGLANG_S3_BUCKET_NAME=my-bucket
export SGLANG_S3_ACCESS_KEY_ID=your-access-key
export SGLANG_S3_SECRET_ACCESS_KEY=your-secret-key
export SGLANG_S3_ENDPOINT_URL=https://minio.example.com
```

See [Environment Variables](https://docs.sglang.io/docs/sglang-diffusion/environment_variables) for the full set of storage options.

## Component Path Overrides

Override individual pipeline components such as `vae`, `transformer`, or `text_encoder` with `--<component>-path`.

```
sglang serve \
  --model-path black-forest-labs/FLUX.2-dev \
  --vae-path fal/FLUX.2-Tiny-AutoEncoder
```

The component key must match the key in the model’s `model_index.json`, and the path must be either a Hugging Face repo ID or a complete component directory.

## Component Attention Backend Overrides

Use `--component-attention-backends` when one pipeline component needs a different native attention backend from the global `--attention-backend`.

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --attention-backend fa \
  --component-attention-backends text_encoder=torch_sdpa
```

The component key must match a pipeline module key such as `text_encoder`, `text_encoder_2`, `transformer`, `transformer_2`, or `connectors`. Component overrides take precedence over the global `--attention-backend` only while that component is being constructed. You can also pass dotted CLI entries:

```
sglang generate \
  --model-path <MODEL_PATH_OR_ID> \
  --component-attention-backends.text_encoder torch_sdpa \
  --component-attention-backends.transformer fa
```

## Diffusers Backend

Use `--backend diffusers` to force vanilla diffusers pipelines when no native SGLang implementation exists or when a model requires a custom pipeline class.

### Key Options

ArgumentValuesDescription`—backend``auto`, `sglang`, `diffusers`Choose native SGLang, force native, or force diffusers`—diffusers-attention-backend``flash`, `_flash_3_hub`, `sage`, `xformers`, `native`Attention backend for diffusers pipelines`—trust-remote-code`flagRequired for models with custom pipeline classes`—vae-tiling` and `—vae-slicing`flagLower memory usage for VAE decode`—dit-precision` and `—vae-precision``fp16`, `bf16`, `fp32`Precision controls`—enable-torch-compile`flagEnable `torch.compile``—cache-dit-config``{PATH}`Cache-DiT config for diffusers pipelines

### Example

```
sglang generate \
  --model-path AIDC-AI/Ovis-Image-7B \
  --backend diffusers \
  --trust-remote-code \
  --diffusers-attention-backend flash \
  --prompt "A serene Japanese garden with cherry blossoms" \
  --height 1024 \
  --width 1024 \
  --num-inference-steps 30 \
  --save-output \
  --output-path outputs \
  --output-file-name ovis_garden.png
```

For pipeline-specific arguments not exposed in the CLI, pass `diffusers_kwargs` in a config file.