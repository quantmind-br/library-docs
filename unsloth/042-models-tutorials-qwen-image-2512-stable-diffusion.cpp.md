---
title: Run Qwen-Image-2512 in stable-diffusion.cpp Tutorial
url: https://unsloth.ai/docs/models/tutorials/qwen-image-2512/stable-diffusion.cpp.md
source: llms
fetched_at: 2026-04-27T18:14:11.226917609-03:00
rendered_js: false
word_count: 474
summary: This tutorial provides step-by-step instructions on how to set up and run Qwen-Image-2512, a text-to-image model from Qwen, using the stable-diffusion.cpp library for local inference.
tags:
    - qwen-image-2512
    - stable-diffusion
    - text-to-image
    - local-inference
    - cpp-tutorial
    - gguf-model
category: tutorial
optimized: true
optimized_at: 2026-04-27T22:00:00Z
---

# Run Qwen-Image-2512 in stable-diffusion.cpp Tutorial

Run [Qwen-Image-2512](https://huggingface.co/unsloth/Qwen-Image-2512-GGUF) locally via [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) — pure C/C++ inference engine for diffusion models.

> [!info] No GPU required; CPU + RAM works. Ensure total usable memory (RAM + VRAM/unified) exceeds GGUF size (e.g. 4-bit Q4_K_M is 13.1 GB, need 13.2+ GB combined).

Tutorial focuses on CUDA; Apple/CPU-only instructions are similar and in the repo.

## 1. Setup Environment

```bash
sudo apt update
sudo apt install -y git cmake build-essential pkg-config
```

> [!info] [Releases Page](https://github.com/leejet/stable-diffusion.cpp/releases) may have pre-built binaries for your hardware.

Set CUDA environment variables:

```bash
export CUDA_HOME=/usr/local/cuda
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib64:${LD_LIBRARY_PATH:-}"
```

Verify:

```bash
nvcc --version  // if not found install nvidia-cuda-toolkit
ldconfig -p | grep -E 'libcudart\.so|libcublas\.so'
```

Clone and build:

```bash
git clone --recursive https://github.com/leejet/stable-diffusion.cpp
cd stable-diffusion.cpp

mkdir -p build
cd build

cmake .. -DCMAKE_BUILD_TYPE=Release -DSD_CUDA=ON
cmake --build . -j"$(nproc)"
```

Confirm build:

```bash
ls bin/sd-cli
```

## 2. Download Models

Diffusion models need 3 components: VAE (pixel-to-latent encoder), text encoder (text-to-embeddings), and diffusion transformer. Diffusion + text encoder can be GGUF; VAE typically safetensors.

```bash
cd ..
mkdir models
mkdir outputs

## Diffusion Models
curl -L -C - -o models/qwen-image-2512-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen-Image-2512-GGUF/resolve/main/qwen-image-2512-Q4_K_M.gguf
curl -L -C - -o models/qwen-image-edit-2511-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF/resolve/main/qwen-image-edit-2511-Q4_K_M.gguf

## Text Encoder + VAE
curl -L -C - -o models/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf \
  https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/resolve/main/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf
curl -L -C - -o models/qwen_image_vae.safetensors \
  https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors

```

> [!warning] VAE/diffusion model format may differ from diffusers checkpoints. Only use checkpoints compatible with stable-diffusion.cpp and ComfyUI.

Q4 variants shown; try smaller/larger quants depending on VRAM/RAM.

## 3. Inference

```bash
./build/bin/sd-cli --diffusion-model models/qwen-image-2512-Q4_K_M.gguf \
    --vae models/qwen_image_vae.safetensors \
    --llm models/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf \
    --cfg-scale 2.5 --sampling-method euler -v --steps 40 \
    -H 1024 -W 1024 --diffusion-fa --flow-shift 3 \
    -p 'Aerial drone photograph of a vast field of bright yellow wildflowers with the text "Unsloth + Diffusion" spelled out in deep purple lavender flowers, sharp contrast between yellow and purple, natural organic letter shapes formed by flower beds, golden hour lighting, rolling countryside landscape, high altitude perspective looking straight down, photorealistic, 8K resolution'  \
    --offload-to-cpu -o outputs/unsloth_diffusion.png
```

> [!tip] No need for `--offload-to-cpu` if you have enough VRAM.

For workflow and hyperparameter details, see the [ComfyUI guide](https://unsloth.ai/docs/blog/comfyui#workflow-and-hyperparameters-1).

#qwen-image-2512 #stable-diffusion #text-to-image #gguf #cpp
