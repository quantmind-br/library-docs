---
title: How to Run Qwen-Image-2512 Locally in ComfyUI
url: https://unsloth.ai/docs/models/tutorials/qwen-image-2512.md
source: llms
fetched_at: 2026-04-27T18:14:08.730282995-03:00
rendered_js: false
word_count: 1361
summary: This guide teaches users how to run the Qwen-Image-2512 text-to-image diffusion model locally using ComfyUI, leveraging Unsloth GGUF optimizations.
tags:
    - qwen-image-2512
    - comfyui
    - unsloth
    - gguf
    - text-to-image
    - diffusion-model
    - workflow-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T22:00:00Z
---

# How to Run Qwen-Image-2512 Locally in ComfyUI

**Qwen-Image-2512** — top open-source diffusion model (December update). Features: more realistic people, richer landscape/texture details, more accurate text rendering. Uses [[115-basics-unsloth-dynamic-2.0-ggufs|Unsloth Dynamic]] methodology (important layers upcasted to higher precision).

**Uploads:** [GGUF](https://huggingface.co/unsloth/Qwen-Image-2512-GGUF) | [FP8](https://huggingface.co/unsloth/Qwen-Image-2512-FP8) | [4-bit BnB](https://huggingface.co/unsloth/Qwen-Image-2512-unsloth-bnb-4bit)

Also see: [[042-models-tutorials-qwen-image-2512-stable-diffusion.cpp|stable-diffusion.cpp tutorial]]

## ComfyUI Tutorial

[ComfyUI](https://github.com/Comfy-Org/ComfyUI) — open-source node-based diffusion model GUI/API/backend.

> [!info] No GPU required; CPU + RAM works. Ensure total usable memory (RAM + VRAM/unified) exceeds GGUF size (e.g. 4-bit Q4_K_M is 13.1 GB, need 13.2+ GB).

### 1. Install & Setup

Download desktop app for Windows/Mac at <https://www.comfy.org/download>, or build from source:

```bash
mkdir comfy_ggufs
cd comfy_ggufs
python -m venv .venv
source .venv/bin/activate

git clone https://github.com/Comfy-Org/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt

cd custom_nodes
git clone https://github.com/city96/ComfyUI-GGUF
cd ComfyUI-GGUF
pip install -r requirements.txt
cd ../..
```

### 2. Download Models

Diffusion models need 3 components: VAE (pixel-to-latent), text encoder (text-to-embeddings), diffusion transformer. Diffusion + text encoder can be GGUF; VAE typically safetensors.

Text encoder: use **Qwen2.5-VL** (not Qwen3-VL) per [Qwen's repo](https://huggingface.co/Qwen/Qwen-Image-2512/blob/main/text_encoder/config.json).

```bash
cd models

## Diffusion Models
curl -L -C - -o unet/qwen-image-2512-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen-Image-2512-GGUF/resolve/main/qwen-image-2512-Q4_K_M.gguf
curl -L -C - -o unet/qwen-image-edit-2511-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF/resolve/main/qwen-image-edit-2511-Q4_K_M.gguf

## Text Encoder + Vision Tower + VAE
curl -L -C - -o text_encoders/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf \
  https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/resolve/main/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf
curl -L -C - -o text_encoders/Qwen2.5-VL-7B-Instruct-mmproj-BF16.gguf \
  https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/resolve/main/mmproj-BF16.gguf
curl -L -C - -o vae/qwen_image_vae.safetensors \
  https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors
```

Other GGUF uploads: [Qwen-Image-2512](https://huggingface.co/unsloth/Qwen-Image-2512-GGUF), [Qwen-Image-Edit-2511](https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF), [Qwen-Image-Layered](https://huggingface.co/unsloth/Qwen-Image-Layered-GGUF). FP8 upload also usable in ComfyUI: [FP8](https://huggingface.co/unsloth/Qwen-Image-2512-FP8).

> [!warning] VAE and diffusion model format may differ from diffusers checkpoints. Only use ComfyUI-compatible checkpoints. Vision tower (mmproj) must share the same prefix as the text encoder.

Download reference images:

```bash
curl -L -C - -o ../input/sloth1.jpg \
    "https://unsloth.ai/cgi/image/_1d5a5685-2d88-44ca-b50f-ba432cd646ef_9CGCY8lvw4D9JkOdueqsk.jpeg?width=1920&quality=80&format=jpeg"

curl -L -C - -o ../input/sloth2.jpg \
    "https://unsloth.ai/cgi/image/UnSloth_GPU_Front_-_Confetti_ArcSk-MR4MMN215UutOFZ.png?width=1920&quality=80&format=jpeg"
```

### 3. Workflow and Hyperparameters

Launch ComfyUI:

```bash
python main.py
```

> [!info] Use `python main.py --cpu` for CPU-only (slow).

Access at `https://127.0.0.1:8188` (set up port forwarding for cloud).

Workflow files: JSON embedded in output PNG metadata or separate `.json` files. Can drag-and-drop images, export/import, share as JSON.

Download workflow JSONs:
- `unsloth_qwen_image_2512.json` (text-to-image)
- `unsloth_qwen_image_edit_2511.json` (multi-reference edit)

Load via Comfy Logo -> File -> Open -> select JSON file.

**Default resolution:** 1024x1024 (native 1328x1328 adds ~50% runtime). 40 steps default; 20 steps sufficient for quick tests. Set `control after generate` to `fixed` to compare settings.

> [!warning] For realism, skip keywords like "photorealistic", "digital rendering", "3d render" — use "photograph" instead.

> [!info] Negative prompts: use NLP-style natural language describing what you don't want. Too many keywords hurts results.

### 4. Inference

#### Upload Models + Set Prompt

- **Unet Loader:** `qwen-image-2512-Q4_K_M.gguf`
- **CLIPLoader:** `Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf`
- **Load VAE:** `qwen_image_vae.safetensors`

Set any prompt + negative prompt.

#### Image Size + Sampler

Model supports different sizes (width/height). Experiment with samplers other than euler; adjust step count. 20 steps for quick tests, 40 for quality.

#### Run

Click Run — image generates in ~1 minute (30s for 20 steps). Output metadata contains full workflow. Share by loading image in ComfyUI.

> [!info] If blurry/bad output, raise **shift to 12-13** — solves most quality issues.

#### Multi Reference Generation

Qwen-Image-Edit-2511 supports multi-reference generation. Load `unsloth_qwen_image_edit_2511.json`, switch unet to `qwen-image-edit-2511-Q4_K_M.gguf`. Extra nodes select reference images. Prompt uses `image 1` and `image 2` as anchors. Click Run to generate output combining reference likenesses.

## Diffusers Tutorial

[Dynamic 4-bit BitsandBytes](https://huggingface.co/unsloth/Qwen-Image-2512-unsloth-bnb-4bit) version for Hugging Face `diffusers` library:

```python
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained(
    "unsloth/Qwen-Image-2512-unsloth-bnb-4bit",
    torch_dtype=torch.bfloat16,
).to('cuda')

# uncomment if you run out of memory
# pipe.enable_model_cpu_offload()

output = pipe(
    prompt="a kawaii sloth playing the drums",
    negative_prompt="blurry, unfocused",
    num_inference_steps=20,
    true_cfg_scale=4.0,
)

# Save output
image = output.images[0]
image.save('sample.png')
```

## stable-diffusion.cpp Tutorial

See [[042-models-tutorials-qwen-image-2512-stable-diffusion.cpp|step-by-step guide]].

#qwen-image-2512 #comfyui #diffusion #gguf #text-to-image
