---
title: Diffusion Models — SGLang
url: https://docs.sglang.io/supported_models/diffusion_models.html
source: crawler
fetched_at: 2026-02-04T08:47:04.097906627-03:00
rendered_js: false
word_count: 2792
summary: This document introduces SGLang Diffusion, an optimized inference framework for high-performance image and video generation using various diffusion models on NVIDIA and AMD GPUs.
tags:
    - sglang
    - diffusion-models
    - image-generation
    - video-generation
    - gpu-acceleration
    - inference-engine
    - cuda
    - rocm
category: guide
---

## Diffusion Models[#](#diffusion-models "Link to this heading")

SGLang Diffusion is an inference framework for accelerated image and video generation using diffusion models. It provides an end-to-end unified pipeline with optimized kernels from sgl-kernel and an efficient scheduler loop.

## Key Features[#](#key-features "Link to this heading")

- **Broad Model Support**: Wan series, FastWan series, Hunyuan, Qwen-Image, Qwen-Image-Edit, Flux, Z-Image, GLM-Image, and more
- **Fast Inference**: Optimized kernels from sgl-kernel, efficient scheduler loop, and Cache-DiT acceleration
- **Ease of Use**: OpenAI-compatible API, CLI, and Python SDK
- **Multi-Platform**: NVIDIA GPUs (H100, H200, A100, B200, 4090) and AMD GPUs (MI300X, MI325X)

* * *

## Install SGLang-diffusion[#](#install-sglang-diffusion "Link to this heading")

You can install sglang-diffusion using one of the methods below.

This page primarily applies to common NVIDIA GPU platforms. For AMD Instinct/ROCm environments see the dedicated [ROCm quickstart](#rocm-quickstart-for-sgl-diffusion), which lists the exact steps (including kernel builds) we used to validate sgl-diffusion on MI300X.

## Method 1: With pip or uv[#](#method-1-with-pip-or-uv "Link to this heading")

It is recommended to use uv for a faster installation:

```
pipinstall--upgradepip
pipinstalluv
uvpipinstall"sglang[diffusion]"--prerelease=allow
```

## Method 2: From source[#](#method-2-from-source "Link to this heading")

```
# Use the latest release branch
gitclonehttps://github.com/sgl-project/sglang.git
cdsglang

# Install the Python packages
pipinstall--upgradepip
pipinstall-e"python[diffusion]"

# With uv
uvpipinstall-e"python[diffusion]"--prerelease=allow
```

## Method 3: Using Docker[#](#method-3-using-docker "Link to this heading")

The Docker images are available on Docker Hub at [lmsysorg/sglang](https://hub.docker.com/r/lmsysorg/sglang), built from the [Dockerfile](https://github.com/sgl-project/sglang/blob/main/docker/Dockerfile). Replace `<secret>` below with your HuggingFace Hub [token](https://huggingface.co/docs/hub/en/security-tokens).

```
dockerrun--gpusall\
--shm-size32g\
-p30000:30000\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=<secret>"\
--ipc=host\
lmsysorg/sglang:dev\
sglanggenerate--model-pathblack-forest-labs/FLUX.1-dev\
--prompt"A logo With Bold Large text: SGL Diffusion"\
--save-output
```

* * *

## ROCm quickstart for sgl-diffusion[#](#rocm-quickstart-for-sgl-diffusion "Link to this heading")

```
dockerrun--device=/dev/kfd--device=/dev/dri--ipc=host\
-v~/.cache/huggingface:/root/.cache/huggingface\
--envHF_TOKEN=<secret>\
lmsysorg/sglang:v0.5.5.post2-rocm700-mi30x\
sglanggenerate--model-pathblack-forest-labs/FLUX.1-dev--prompt"A logo With Bold Large text: SGL Diffusion"--save-output
```

* * *

## Compatibility Matrix[#](#compatibility-matrix "Link to this heading")

The table below shows every supported model and the optimizations supported for them.

The symbols used have the following meanings:

- ✅ = Full compatibility
- ❌ = No compatibility
- ⭕ = Does not apply to this model

## Models x Optimization[#](#models-x-optimization "Link to this heading")

The `HuggingFace Model ID` can be passed directly to `from_pretrained()` methods, and sglang-diffusion will use the optimal default parameters when initializing and generating videos.

### Video Generation Models[#](#video-generation-models "Link to this heading")

**Note**: Wan2.2 TI2V 5B has some quality issues when performing I2V generation. We are working on fixing this issue.

### Image Generation Models[#](#image-generation-models "Link to this heading")

## Verified LoRA Examples[#](#verified-lora-examples "Link to this heading")

This section lists example LoRAs that have been explicitly tested and verified with each base model in the **SGLang Diffusion** pipeline.

> Important:  
> LoRAs that are not listed here are not necessarily incompatible. In practice, most standard LoRAs are expected to work, especially those following common Diffusers or SD-style conventions. The entries below simply reflect configurations that have been manually validated by the SGLang team.

### Verified LoRAs by Base Model[#](#verified-loras-by-base-model "Link to this heading")

#### Special Requirements[#](#special-requirements "Link to this heading")

> \[!NOTE] Sliding Tile Attention: Currently, only Hopper GPUs (H100s) are supported.

* * *

## SGLang diffusion CLI Inference[#](#sglang-diffusion-cli-inference "Link to this heading")

The SGLang-diffusion CLI provides a quick way to access the inference pipeline for image and video generation.

## Prerequisites[#](#prerequisites "Link to this heading")

- A working SGLang diffusion installation and the `sglang` CLI available in `$PATH`.
- Python 3.11+ if you plan to use the OpenAI Python SDK.

## Supported Arguments[#](#supported-arguments "Link to this heading")

### Server Arguments[#](#server-arguments "Link to this heading")

- `--model-path {MODEL_PATH}`: Path to the model or model ID
- `--vae-path {VAE_PATH}`: Path to a custom VAE model or HuggingFace model ID (e.g., `fal/FLUX.2-Tiny-AutoEncoder`). If not specified, the VAE will be loaded from the main model path.
- `--lora-path {LORA_PATH}`: Path to a LoRA adapter (local path or HuggingFace model ID). If not specified, LoRA will not be applied.
- `--lora-nickname {NAME}`: Nickname for the LoRA adapter. (default: `default`).
- `--num-gpus {NUM_GPUS}`: Number of GPUs to use
- `--tp-size {TP_SIZE}`: Tensor parallelism size (only for the encoder; should not be larger than 1 if text encoder offload is enabled, as layer-wise offload plus prefetch is faster)
- `--sp-degree {SP_SIZE}`: Sequence parallelism size (typically should match the number of GPUs)
- `--ulysses-degree {ULYSSES_DEGREE}`: The degree of DeepSpeed-Ulysses-style SP in USP
- `--ring-degree {RING_DEGREE}`: The degree of ring attention-style SP in USP

### Sampling Parameters[#](#sampling-parameters "Link to this heading")

- `--prompt {PROMPT}`: Text description for the video you want to generate
- `--num-inference-steps {STEPS}`: Number of denoising steps
- `--negative-prompt {PROMPT}`: Negative prompt to guide generation away from certain concepts
- `--seed {SEED}`: Random seed for reproducible generation

#### Image/Video Configuration[#](#image-video-configuration "Link to this heading")

- `--height {HEIGHT}`: Height of the generated output
- `--width {WIDTH}`: Width of the generated output
- `--num-frames {NUM_FRAMES}`: Number of frames to generate
- `--fps {FPS}`: Frames per second for the saved output, if this is a video-generation task

#### Output Options[#](#output-options "Link to this heading")

- `--output-path {PATH}`: Directory to save the generated video
- `--save-output`: Whether to save the image/video to disk
- `--return-frames`: Whether to return the raw frames

### Using Configuration Files[#](#using-configuration-files "Link to this heading")

Instead of specifying all parameters on the command line, you can use a configuration file:

```
sglanggenerate--config{CONFIG_FILE_PATH}
```

The configuration file should be in JSON or YAML format with the same parameter names as the CLI options. Command-line arguments take precedence over settings in the configuration file, allowing you to override specific values while keeping the rest from the configuration file.

Example configuration file (config.json):

```
{
"model_path":"FastVideo/FastHunyuan-diffusers",
"prompt":"A beautiful woman in a red dress walking down a street",
"output_path":"outputs/",
"num_gpus":2,
"sp_size":2,
"tp_size":1,
"num_frames":45,
"height":720,
"width":1280,
"num_inference_steps":6,
"seed":1024,
"fps":24,
"precision":"bf16",
"vae_precision":"fp16",
"vae_tiling":true,
"vae_sp":true,
"vae_config":{
"load_encoder":false,
"load_decoder":true,
"tile_sample_min_height":256,
"tile_sample_min_width":256
},
"text_encoder_precisions":[
"fp16",
"fp16"
],
"mask_strategy_file_path":null,
"enable_torch_compile":false
}
```

Or using YAML format (config.yaml):

```
model_path:"FastVideo/FastHunyuan-diffusers"
prompt:"Abeautifulwomaninareddresswalkingdownastreet"
output_path:"outputs/"
num_gpus:2
sp_size:2
tp_size:1
num_frames:45
height:720
width:1280
num_inference_steps:6
seed:1024
fps:24
precision:"bf16"
vae_precision:"fp16"
vae_tiling:true
vae_sp:true
vae_config:
load_encoder:false
load_decoder:true
tile_sample_min_height:256
tile_sample_min_width:256
text_encoder_precisions:
-"fp16"
-"fp16"
mask_strategy_file_path:null
enable_torch_compile:false
```

To see all the options, you can use the `--help` flag:

## Serve[#](#serve "Link to this heading")

Launch the SGLang diffusion HTTP server and interact with it using the OpenAI SDK and curl.

### Start the server[#](#start-the-server "Link to this heading")

Use the following command to launch the server:

```
SERVER_ARGS=(
--model-pathWan-AI/Wan2.1-T2V-1.3B-Diffusers
--text-encoder-cpu-offload
--pin-cpu-memory
--num-gpus4
--ulysses-degree=2
--ring-degree=2
)

sglangserve"${SERVER_ARGS[@]}"
```

- **–model-path**: Which model to load. The example uses `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`.
- **–port**: HTTP port to listen on (the default here is `30010`).

For detailed API usage, including Image, Video Generation and LoRA management, please refer to the [OpenAI API Documentation](#sglang-diffusion-openai-api).

## Generate[#](#generate "Link to this heading")

Run a one-off generation task without launching a persistent server.

To use it, pass both server arguments and sampling parameters in one command, after the `generate` subcommand, for example:

```
SERVER_ARGS=(
--model-pathWan-AI/Wan2.2-T2V-A14B-Diffusers
--text-encoder-cpu-offload
--pin-cpu-memory
--num-gpus4
--ulysses-degree=2
--ring-degree=2
)

SAMPLING_ARGS=(
--prompt"A curious raccoon"
--save-output
--output-pathoutputs
--output-file-name"A curious raccoon.mp4"
)

sglanggenerate"${SERVER_ARGS[@]}""${SAMPLING_ARGS[@]}"

# Or, users can set `SGLANG_CACHE_DIT_ENABLED` env as `true` to enable cache acceleration
SGLANG_CACHE_DIT_ENABLED=truesglanggenerate"${SERVER_ARGS[@]}""${SAMPLING_ARGS[@]}"
```

Once the generation task has finished, the server will shut down automatically.

> \[!NOTE] The HTTP server-related arguments are ignored in this subcommand.

## Diffusers Backend[#](#diffusers-backend "Link to this heading")

SGLang diffusion supports a **diffusers backend** that allows you to run any diffusers-compatible model through SGLang’s infrastructure using vanilla diffusers pipelines. This is useful for running models without native SGLang implementations or models with custom pipeline classes.

### Arguments[#](#arguments "Link to this heading")

### Example: Running Ovis-Image-7B[#](#example-running-ovis-image-7b "Link to this heading")

[Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) is a 7B text-to-image model optimized for high-quality text rendering.

```
sglanggenerate\
--model-pathAIDC-AI/Ovis-Image-7B\
--backenddiffusers\
--trust-remote-code\
--diffusers-attention-backendflash\
--prompt"A serene Japanese garden with cherry blossoms"\
--height1024\
--width1024\
--num-inference-steps30\
--save-output\
--output-pathoutputs\
--output-file-nameovis_garden.png
```

* * *

## SGLang Diffusion OpenAI API[#](#sglang-diffusion-openai-api "Link to this heading")

The SGLang diffusion HTTP server implements an OpenAI-compatible API for image and video generation, as well as LoRA adapter management.

## Serve[#](#id1 "Link to this heading")

Launch the server using the `sglang serve` command.

### Start the server[#](#id2 "Link to this heading")

```
SERVER_ARGS=(
--model-pathWan-AI/Wan2.1-T2V-1.3B-Diffusers
--text-encoder-cpu-offload
--pin-cpu-memory
--num-gpus4
--ulysses-degree=2
--ring-degree=2
--port30010
)

sglangserve"${SERVER_ARGS[@]}"
```

- **–model-path**: Path to the model or model ID.
- **–port**: HTTP port to listen on (default: `30000`).

#### Get Model Information[#](#get-model-information "Link to this heading")

**Endpoint:** `GET /models`

Returns information about the model served by this server, including model path, task type, pipeline configuration, and precision settings.

**Curl Example:**

```
curl-sS-XGET"http://localhost:30010/models"
```

**Response Example:**

```
{
"model_path":"Wan-AI/Wan2.1-T2V-1.3B-Diffusers",
"task_type":"T2V",
"pipeline_name":"wan_pipeline",
"pipeline_class":"WanPipeline",
"num_gpus":4,
"dit_precision":"bf16",
"vae_precision":"fp16"
}
```

* * *

## Endpoints[#](#endpoints "Link to this heading")

### Image Generation[#](#image-generation "Link to this heading")

The server implements an OpenAI-compatible Images API under the `/v1/images` namespace.

#### Create an image[#](#create-an-image "Link to this heading")

**Endpoint:** `POST /v1/images/generations`

**Python Example (b64\_json response):**

```
importbase64
fromopenaiimport OpenAI

client = OpenAI(api_key="sk-proj-1234567890", base_url="http://localhost:30010/v1")

img = client.images.generate(
    prompt="A calico cat playing a piano on stage",
    size="1024x1024",
    n=1,
    response_format="b64_json",
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
```

**Curl Example:**

```
curl-sS-XPOST"http://localhost:30010/v1/images/generations"\
-H"Content-Type: application/json"\
-H"Authorization: Bearer sk-proj-1234567890"\
-d'{
        "prompt": "A calico cat playing a piano on stage",
        "size": "1024x1024",
        "n": 1,
        "response_format": "b64_json"
      }'
```

> **Note** The `response_format=url` option is not supported for `POST /v1/images/generations` and will return a `400` error.

#### Edit an image[#](#edit-an-image "Link to this heading")

**Endpoint:** `POST /v1/images/edits`

This endpoint accepts a multipart form upload with input images and a text prompt. The server can return either a base64-encoded image or a URL to download the image.

**Curl Example (b64\_json response):**

```
curl-sS-XPOST"http://localhost:30010/v1/images/edits"\
-H"Authorization: Bearer sk-proj-1234567890"\
-F"image=@local_input_image.png"\
-F"url=image_url.jpg"\
-F"prompt=A calico cat playing a piano on stage"\
-F"size=1024x1024"\
-F"response_format=b64_json"
```

**Curl Example (URL response):**

```
curl-sS-XPOST"http://localhost:30010/v1/images/edits"\
-H"Authorization: Bearer sk-proj-1234567890"\
-F"image=@local_input_image.png"\
-F"url=image_url.jpg"\
-F"prompt=A calico cat playing a piano on stage"\
-F"size=1024x1024"\
-F"response_format=url"
```

#### Download image content[#](#download-image-content "Link to this heading")

When `response_format=url` is used with `POST /v1/images/edits`, the API returns a relative URL like `/v1/images/<IMAGE_ID>/content`.

**Endpoint:** `GET /v1/images/{image_id}/content`

**Curl Example:**

```
curl-sS-L"http://localhost:30010/v1/images/<IMAGE_ID>/content"\
-H"Authorization: Bearer sk-proj-1234567890"\
-ooutput.png
```

### Video Generation[#](#video-generation "Link to this heading")

The server implements a subset of the OpenAI Videos API under the `/v1/videos` namespace.

#### Create a video[#](#create-a-video "Link to this heading")

**Endpoint:** `POST /v1/videos`

**Python Example:**

```
fromopenaiimport OpenAI

client = OpenAI(api_key="sk-proj-1234567890", base_url="http://localhost:30010/v1")

video = client.videos.create(
    prompt="A calico cat playing a piano on stage",
    size="1280x720"
)
print(f"Video ID: {video.id}, Status: {video.status}")
```

**Curl Example:**

```
curl-sS-XPOST"http://localhost:30010/v1/videos"\
-H"Content-Type: application/json"\
-H"Authorization: Bearer sk-proj-1234567890"\
-d'{
        "prompt": "A calico cat playing a piano on stage",
        "size": "1280x720"
      }'
```

#### List videos[#](#list-videos "Link to this heading")

**Endpoint:** `GET /v1/videos`

**Python Example:**

```
videos = client.videos.list()
for item in videos.data:
    print(item.id, item.status)
```

**Curl Example:**

```
curl-sS-XGET"http://localhost:30010/v1/videos"\
-H"Authorization: Bearer sk-proj-1234567890"
```

#### Download video content[#](#download-video-content "Link to this heading")

**Endpoint:** `GET /v1/videos/{video_id}/content`

**Python Example:**

```
importtime

# Poll for completion
while True:
    page = client.videos.list()
    item = next((v for v in page.data if v.id == video_id), None)
    if item and item.status == "completed":
        break
    time.sleep(5)

# Download content
resp = client.videos.download_content(video_id=video_id)
with open("output.mp4", "wb") as f:
    f.write(resp.read())
```

**Curl Example:**

```
curl-sS-L"http://localhost:30010/v1/videos/<VIDEO_ID>/content"\
-H"Authorization: Bearer sk-proj-1234567890"\
-ooutput.mp4
```

* * *

### LoRA Management[#](#lora-management "Link to this heading")

The server supports dynamic loading, merging, and unmerging of LoRA adapters.

**Important Notes:**

- Mutual Exclusion: Only one LoRA can be *merged* (active) at a time
- Switching: To switch LoRAs, you must first `unmerge` the current one, then `set` the new one
- Caching: The server caches loaded LoRA weights in memory. Switching back to a previously loaded LoRA (same path) has little cost

#### Set LoRA Adapter[#](#set-lora-adapter "Link to this heading")

Loads one or more LoRA adapters and merges their weights into the model. Supports both single LoRA (backward compatible) and multiple LoRA adapters.

**Endpoint:** `POST /v1/set_lora`

**Parameters:**

- `lora_nickname` (string or list of strings, required): A unique identifier for the LoRA adapter(s). Can be a single string or a list of strings for multiple LoRAs
- `lora_path` (string or list of strings/None, optional): Path to the `.safetensors` file(s) or Hugging Face repo ID(s). Required for the first load; optional if re-activating a cached nickname. If a list, must match the length of `lora_nickname`
- `target` (string or list of strings, optional): Which transformer(s) to apply the LoRA to. If a list, must match the length of `lora_nickname`. Valid values:
  
  - `"all"` (default): Apply to all transformers
  - `"transformer"`: Apply only to the primary transformer (high noise for Wan2.2)
  - `"transformer_2"`: Apply only to transformer\_2 (low noise for Wan2.2)
  - `"critic"`: Apply only to the critic model
- `strength` (float or list of floats, optional): LoRA strength for merge, default 1.0. If a list, must match the length of `lora_nickname`. Values &lt; 1.0 reduce the effect, values &gt; 1.0 amplify the effect

**Single LoRA Example:**

```
curl-XPOSThttp://localhost:30010/v1/set_lora\
-H"Content-Type: application/json"\
-d'{
        "lora_nickname": "lora_name",
        "lora_path": "/path/to/lora.safetensors",
        "target": "all",
        "strength": 0.8
      }'
```

**Multiple LoRA Example:**

```
curl-XPOSThttp://localhost:30010/v1/set_lora\
-H"Content-Type: application/json"\
-d'{
        "lora_nickname": ["lora_1", "lora_2"],
        "lora_path": ["/path/to/lora1.safetensors", "/path/to/lora2.safetensors"],
        "target": ["transformer", "transformer_2"],
        "strength": [0.8, 1.0]
      }'
```

**Multiple LoRA with Same Target:**

```
curl-XPOSThttp://localhost:30010/v1/set_lora\
-H"Content-Type: application/json"\
-d'{
        "lora_nickname": ["style_lora", "character_lora"],
        "lora_path": ["/path/to/style.safetensors", "/path/to/character.safetensors"],
        "target": "all",
        "strength": [0.7, 0.9]
      }'
```

> \[!NOTE] When using multiple LoRAs:
> 
> - All list parameters (`lora_nickname`, `lora_path`, `target`, `strength`) must have the same length
> - If `target` or `strength` is a single value, it will be applied to all LoRAs
> - Multiple LoRAs applied to the same target will be merged in order

#### Merge LoRA Weights[#](#merge-lora-weights "Link to this heading")

Manually merges the currently set LoRA weights into the base model.

> \[!NOTE] `set_lora` automatically performs a merge, so this is typically only needed if you have manually unmerged but want to re-apply the same LoRA without calling `set_lora` again.*

**Endpoint:** `POST /v1/merge_lora_weights`

**Parameters:**

- `target` (string, optional): Which transformer(s) to merge. One of “all” (default), “transformer”, “transformer\_2”, “critic”
- `strength` (float, optional): LoRA strength for merge, default 1.0. Values &lt; 1.0 reduce the effect, values &gt; 1.0 amplify the effect

**Curl Example:**

```
curl-XPOSThttp://localhost:30010/v1/merge_lora_weights\
-H"Content-Type: application/json"\
-d'{"strength": 0.8}'
```

#### Unmerge LoRA Weights[#](#unmerge-lora-weights "Link to this heading")

Unmerges the currently active LoRA weights from the base model, restoring it to its original state. This **must** be called before setting a different LoRA.

**Endpoint:** `POST /v1/unmerge_lora_weights`

**Curl Example:**

```
curl-XPOSThttp://localhost:30010/v1/unmerge_lora_weights\
-H"Content-Type: application/json"
```

#### List LoRA Adapters[#](#list-lora-adapters "Link to this heading")

Returns loaded LoRA adapters and current application status per module.

**Endpoint:** `GET /v1/list_loras`

**Curl Example:**

```
curl-sS-XGET"http://localhost:30010/v1/list_loras"
```

**Response Example:**

```
{
"loaded_adapters":[
{"nickname":"lora_a","path":"/weights/lora_a.safetensors"},
{"nickname":"lora_b","path":"/weights/lora_b.safetensors"}
],
"active":{
"transformer":[
{
"nickname":"lora2",
"path":"tarn59/pixel_art_style_lora_z_image_turbo",
"merged":true,
"strength":1.0
}
]
}
}
```

Notes:

- If LoRA is not enabled for the current pipeline, the server will return an error.
- `num_lora_layers_with_weights` counts only layers that have LoRA weights applied for the active adapter.

### Example: Switching LoRAs[#](#example-switching-loras "Link to this heading")

1. Set LoRA A:
   
   ```
   curl-XPOSThttp://localhost:30010/v1/set_lora-d'{"lora_nickname": "lora_a", "lora_path": "path/to/A"}'
   ```
2. Generate with LoRA A…
3. Unmerge LoRA A:
   
   ```
   curl-XPOSThttp://localhost:30010/v1/unmerge_lora_weights
   ```
4. Set LoRA B:
   
   ```
   curl-XPOSThttp://localhost:30010/v1/set_lora-d'{"lora_nickname": "lora_b", "lora_path": "path/to/B"}'
   ```
5. Generate with LoRA B…

* * *

## Attention Backends[#](#attention-backends "Link to this heading")

This document describes the attention backends available in sglang diffusion (`sglang.multimodal_gen`) and how to select them.

## Overview[#](#overview "Link to this heading")

Attention backends are defined by `AttentionBackendEnum` (`sglang.multimodal_gen.runtime.platforms.interface.AttentionBackendEnum`) and selected via the CLI flag `--attention-backend`.

Backend selection is performed by the shared attention layers (e.g. `LocalAttention` / `USPAttention` / `UlyssesAttention` in `sglang.multimodal_gen.runtime.layers.attention.layer`) and therefore applies to any model component using these layers (e.g. diffusion transformer / DiT and encoders).

- **CUDA**: prefers FlashAttention (FA3/FA4) when supported; otherwise falls back to PyTorch SDPA.
- **ROCm**: uses FlashAttention when available; otherwise falls back to PyTorch SDPA.
- **MPS**: always uses PyTorch SDPA.

## Backend options[#](#backend-options "Link to this heading")

The CLI accepts the lowercase names of `AttentionBackendEnum`. The table below lists the backends implemented by the built-in platforms. `fa3`/`fa4` are accepted as aliases for `fa`.

## Selection priority[#](#selection-priority "Link to this heading")

The selection order in `runtime/layers/attention/selector.py` is:

1. `global_force_attn_backend(...)` / `global_force_attn_backend_context_manager(...)`
2. CLI `--attention-backend` (`ServerArgs.attention_backend`)
3. Auto selection (platform capability, dtype, and installed packages)

## Platform support matrix[#](#platform-support-matrix "Link to this heading")

## Usage[#](#usage "Link to this heading")

### Select a backend via CLI[#](#select-a-backend-via-cli "Link to this heading")

```
sglanggenerate\
--model-path<MODEL_PATH_OR_ID>\
--prompt"..."\
--attention-backendfa
```

```
sglanggenerate\
--model-path<MODEL_PATH_OR_ID>\
--prompt"..."\
--attention-backendtorch_sdpa
```

### Using Sliding Tile Attention (STA)[#](#using-sliding-tile-attention-sta "Link to this heading")

```
exportSGLANG_DIFFUSION_ATTENTION_CONFIG=/abs/path/to/mask_strategy.json

sglanggenerate\
--model-path<MODEL_PATH_OR_ID>\
--prompt"..."\
--attention-backendsliding_tile_attn
```

### Notes for ROCm / MPS[#](#notes-for-rocm-mps "Link to this heading")

- ROCm: use `--attention-backend torch_sdpa` or `fa` depending on what is available in your environment.
- MPS: the platform implementation always uses `torch_sdpa`.

* * *

## Cache-DiT Acceleration[#](#cache-dit-acceleration "Link to this heading")

SGLang integrates [Cache-DiT](https://github.com/vipshop/cache-dit), a caching acceleration engine for Diffusion Transformers (DiT), to achieve up to **7.4x inference speedup** with minimal quality loss.

## Overview[#](#id3 "Link to this heading")

**Cache-DiT** uses intelligent caching strategies to skip redundant computation in the denoising loop:

- **DBCache (Dual Block Cache)**: Dynamically decides when to cache transformer blocks based on residual differences
- **TaylorSeer**: Uses Taylor expansion for calibration to optimize caching decisions
- **SCM (Step Computation Masking)**: Step-level caching control for additional speedup

## Basic Usage[#](#basic-usage "Link to this heading")

Enable Cache-DiT by exporting the environment variable and using `sglang generate` or `sglang serve` :

```
SGLANG_CACHE_DIT_ENABLED=true\
sglanggenerate--model-pathQwen/Qwen-Image\
--prompt"A beautiful sunset over the mountains"
```

## Advanced Configuration[#](#advanced-configuration "Link to this heading")

### DBCache Parameters[#](#dbcache-parameters "Link to this heading")

DBCache controls block-level caching behavior:

### TaylorSeer Configuration[#](#taylorseer-configuration "Link to this heading")

TaylorSeer improves caching accuracy using Taylor expansion:

### Combined Configuration Example[#](#combined-configuration-example "Link to this heading")

DBCache and TaylorSeer are complementary strategies that work together, you can configure both sets of parameters simultaneously:

```
SGLANG_CACHE_DIT_ENABLED=true\
SGLANG_CACHE_DIT_FN=2\
SGLANG_CACHE_DIT_BN=1\
SGLANG_CACHE_DIT_WARMUP=4\
SGLANG_CACHE_DIT_RDT=0.4\
SGLANG_CACHE_DIT_MC=4\
SGLANG_CACHE_DIT_TAYLORSEER=true\
SGLANG_CACHE_DIT_TS_ORDER=2\
sglanggenerate--model-pathblack-forest-labs/FLUX.1-dev\
--prompt"A curious raccoon in a forest"
```

### SCM (Step Computation Masking)[#](#scm-step-computation-masking "Link to this heading")

SCM provides step-level caching control for additional speedup. It decides which denoising steps to compute fully and which to use cached results.

#### SCM Presets[#](#scm-presets "Link to this heading")

SCM is configured with presets:

##### Usage[#](#id4 "Link to this heading")

```
SGLANG_CACHE_DIT_ENABLED=true\
SGLANG_CACHE_DIT_SCM_PRESET=medium\
sglanggenerate--model-pathQwen/Qwen-Image\
--prompt"A futuristic cityscape at sunset"
```

#### Custom SCM Bins[#](#custom-scm-bins "Link to this heading")

For fine-grained control over which steps to compute vs cache:

```
SGLANG_CACHE_DIT_ENABLED=true\
SGLANG_CACHE_DIT_SCM_COMPUTE_BINS="8,3,3,2,2"\
SGLANG_CACHE_DIT_SCM_CACHE_BINS="1,2,2,2,3"\
sglanggenerate--model-pathQwen/Qwen-Image\
--prompt"A futuristic cityscape at sunset"
```

#### SCM Policy[#](#scm-policy "Link to this heading")

## Environment Variables[#](#environment-variables "Link to this heading")

All Cache-DiT parameters can be set via the following environment variables:

## Supported Models[#](#supported-models "Link to this heading")

SGLang Diffusion x Cache-DiT supports almost all models originally supported in SGLang Diffusion:

## Performance Tips[#](#performance-tips "Link to this heading")

1. **Start with defaults**: The default parameters work well for most models
2. **Use TaylorSeer**: It typically improves both speed and quality
3. **Tune R threshold**: Lower values = better quality, higher values = faster
4. **SCM for extra speed**: Use `medium` preset for good speed/quality balance
5. **Warmup matters**: Higher warmup = more stable caching decisions

## Limitations[#](#limitations "Link to this heading")

- **Single GPU only**: Distributed support (TP/SP) is not yet validated; Cache-DiT will be automatically disabled when `world_size > 1`
- **SCM minimum steps**: SCM requires &gt;= 8 inference steps to be effective
- **Model support**: Only models registered in Cache-DiT’s BlockAdapterRegister are supported

## Troubleshooting[#](#troubleshooting "Link to this heading")

### Distributed environment warning[#](#distributed-environment-warning "Link to this heading")

```
WARNING: cache-dit is disabled in distributed environment (world_size=N)
```

This is expected behavior. Cache-DiT currently only supports single-GPU inference.

### SCM disabled for low step count[#](#scm-disabled-for-low-step-count "Link to this heading")

For models with &lt; 8 inference steps (e.g., DMD distilled models), SCM will be automatically disabled. DBCache acceleration still works.

## References[#](#references "Link to this heading")

- [Cache-Dit](https://github.com/vipshop/cache-dit)
- [SGLang Diffusion](https://github.com/sgl-project/sglang/tree/main/python/sglang/multimodal_gen)

* * *

## Profiling Multimodal Generation[#](#profiling-multimodal-generation "Link to this heading")

This guide covers profiling techniques for multimodal generation pipelines in SGLang.

## PyTorch Profiler[#](#pytorch-profiler "Link to this heading")

PyTorch Profiler provides detailed kernel execution time, call stack, and GPU utilization metrics.

### Denoising Stage Profiling[#](#denoising-stage-profiling "Link to this heading")

Profile the denoising stage with sampled timesteps (default: 5 steps after 1 warmup step):

```
sglanggenerate\
--model-pathQwen/Qwen-Image\
--prompt"A Logo With Bold Large Text: SGL Diffusion"\
--seed0\
--profile
```

**Parameters:**

- `--profile`: Enable profiling for the denoising stage
- `--num-profiled-timesteps N`: Number of timesteps to profile after warmup (default: 5)
  
  - Smaller values reduce trace file size
  - Example: `--num-profiled-timesteps 10` profiles 10 steps after 1 warmup step

### Full Pipeline Profiling[#](#full-pipeline-profiling "Link to this heading")

Profile all pipeline stages (text encoding, denoising, VAE decoding, etc.):

```
sglanggenerate\
--model-pathQwen/Qwen-Image\
--prompt"A Logo With Bold Large Text: SGL Diffusion"\
--seed0\
--profile\
--profile-all-stages
```

**Parameters:**

- `--profile-all-stages`: Used with `--profile`, profile all pipeline stages instead of just denoising

### Output Location[#](#output-location "Link to this heading")

By default, trace files are saved in the ./logs/ directory.

The exact output file path will be shown in the console output, for example:

```
[mm-ddhh:mm:ss]Savedprofilertracesto:/sgl-workspace/sglang/logs/mocked_fake_id_for_offline_generate-5_steps-global-rank0.trace.json.gz
```

### View Traces[#](#view-traces "Link to this heading")

Load and visualize trace files at:

- https://ui.perfetto.dev/ (recommended)
- chrome://tracing (Chrome only)

For large trace files, reduce `--num-profiled-timesteps` or avoid using `--profile-all-stages`.

### `--perf-dump-path` (Stage/Step Timing Dump)[#](#perf-dump-path-stage-step-timing-dump "Link to this heading")

Besides profiler traces, you can also dump a lightweight JSON report that contains:

- stage-level timing breakdown for the full pipeline
- step-level timing breakdown for the denoising stage (per diffusion step)

This is useful to quickly identify which stage dominates end-to-end latency, and whether denoising steps have uniform runtimes (and if not, which step has an abnormal spike).

The dumped JSON contains a `denoise_steps_ms` field formatted as an array of objects, each with a `step` key (the step index) and a `duration_ms` key.

Example:

```
sglanggenerate\
--model-path<MODEL_PATH_OR_ID>\
--prompt"<PROMPT>"\
--perf-dump-pathperf.json
```

## Nsight Systems[#](#nsight-systems "Link to this heading")

Nsight Systems provides low-level CUDA profiling with kernel details, register usage, and memory access patterns.

### Installation[#](#installation "Link to this heading")

See the [SGLang profiling guide](https://github.com/sgl-project/sglang/blob/main/docs/developer_guide/benchmark_and_profiling.md#profile-with-nsight) for installation instructions.

### Basic Profiling[#](#basic-profiling "Link to this heading")

Profile the entire pipeline execution:

```
nsysprofile\
--trace-fork-before-exec=true\
--cuda-graph-trace=node\
--force-overwrite=true\
-oQwenImage\
sglanggenerate\
--model-pathQwen/Qwen-Image\
--prompt"A Logo With Bold Large Text: SGL Diffusion"\
--seed0
```

### Targeted Stage Profiling[#](#targeted-stage-profiling "Link to this heading")

Use `--delay` and `--duration` to capture specific stages and reduce file size:

```
nsysprofile\
--trace-fork-before-exec=true\
--cuda-graph-trace=node\
--force-overwrite=true\
--delay10\
--duration30\
-oQwenImage_denoising\
sglanggenerate\
--model-pathQwen/Qwen-Image\
--prompt"A Logo With Bold Large Text: SGL Diffusion"\
--seed0
```

**Parameters:**

- `--delay N`: Wait N seconds before starting capture (skip initialization overhead)
- `--duration N`: Capture for N seconds (focus on specific stages)
- `--force-overwrite`: Overwrite existing output files

## Notes[#](#notes "Link to this heading")

- **Reduce trace size**: Use `--num-profiled-timesteps` with smaller values or `--delay`/`--duration` with Nsight Systems
- **Stage-specific analysis**: Use `--profile` alone for denoising stage, add `--profile-all-stages` for full pipeline
- **Multiple runs**: Profile with different prompts and resolutions to identify bottlenecks across workloads

## FAQ[#](#faq "Link to this heading")

- If you are profiling `sglang generate` with Nsight Systems and find that the generated profiler file did not capture any CUDA kernels, you can resolve this issue by increasing the model’s inference steps to extend the execution time.

* * *

## Contributing to SGLang Diffusion[#](#contributing-to-sglang-diffusion "Link to this heading")

This guide outlines the requirements for contributing to the SGLang Diffusion module (`sglang.multimodal_gen`).

## 1. Commit Message Convention[#](#commit-message-convention "Link to this heading")

We follow a structured commit message format to maintain a clean history.

**Format:**

```
[diffusion] <scope>: <subject>
```

**Examples:**

- `[diffusion] cli: add --perf-dump-path argument`
- `[diffusion] scheduler: fix deadlock in batch processing`
- `[diffusion] model: support Stable Diffusion 3.5`

**Rules:**

- **Prefix**: Always start with `[diffusion]`.
- **Scope** (Optional): `cli`, `scheduler`, `model`, `pipeline`, `docs`, etc.
- **Subject**: Imperative mood, short and clear (e.g., “add feature” not “added feature”).

## 2. Performance Reporting[#](#performance-reporting "Link to this heading")

For PRs that impact **latency**, **throughput**, or **memory usage**, you **should** provide a performance comparison report.

### How to Generate a Report[#](#how-to-generate-a-report "Link to this heading")

1. **Baseline**: run the benchmark (for a single generation task)
   
   ```
   $sglanggenerate--model-path<model>--prompt"A benchmark prompt"--perf-dump-pathbaseline.json
   ```
2. **New**: run the same benchmark, without modifying any server\_args or sampling\_params
   
   ```
   $sglanggenerate--model-path<model>--prompt"A benchmark prompt"--perf-dump-pathnew.json
   ```
3. **Compare**: run the compare script, which will print a Markdown table to the console
   
   ```
   $pythonpython/sglang/multimodal_gen/benchmarks/compare_perf.pybaseline.jsonnew.json[new2.json...]
   ### Performance Comparison Report
   ...
   ```
4. **Paste**: paste the table into the PR description

## 3. CI-Based Change Protection[#](#ci-based-change-protection "Link to this heading")

Consider adding tests to the `pr-test` or `nightly-test` suites to safeguard your changes, especially for PRs that:

1. support a new model
2. support or fix important features
3. significantly improve performance

See [test](https://github.com/sgl-project/sglang/tree/main/python/sglang/multimodal_gen/test) for examples

* * *

## How to Support New Diffusion Models[#](#how-to-support-new-diffusion-models "Link to this heading")

SGLang diffusion uses a modular pipeline architecture built around two key concepts:

- **`ComposedPipeline`** : Orchestrates `PipelineStage`s to define the complete generation process
- **`PipelineStage`** : Modular components (prompt encoding, denoising loop, VAE decoding, etc.)

To add a new model, you’ll need to define:

1. **`PipelineConfig`** : Static model configurations (paths, precision settings)
2. **`SamplingParams`** : Runtime generation parameters (prompt, guidance\_scale, steps)
3. **`ComposedPipeline`** : Chain together pipeline stages
4. **Modules**: Model components (text\_encoder, transformer, vae, scheduler)

For the complete implementation guide with examples, see: [**How to Support New Diffusion Models**](https://github.com/sgl-project/sglang/blob/main/python/sglang/multimodal_gen/docs/support_new_models.md)

* * *

## References[#](#id5 "Link to this heading")

- [SGLang GitHub](https://github.com/sgl-project/sglang)
- [Cache-DiT](https://github.com/vipshop/cache-dit)
- [FastVideo](https://github.com/hao-ai-lab/FastVideo)
- [xDiT](https://github.com/xdit-project/xDiT)
- [Diffusers](https://github.com/huggingface/diffusers)