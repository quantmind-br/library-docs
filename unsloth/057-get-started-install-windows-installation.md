---
title: How to Fine-Tune LLMs on Windows with Unsloth (Step-by-Step Guide)
url: https://unsloth.ai/docs/get-started/install/windows-installation.md
source: llms
fetched_at: 2026-04-27T18:12:57.357500741-03:00
rendered_js: false
word_count: 1486
summary: 'This guide provides step-by-step instructions on how to fine-tune Large Language Models (LLMs) locally on a Windows machine using the Unsloth library. It details three methods of installation: via Conda, Docker, and WSL, with an in-depth walkthrough of the Conda method.'
tags:
    - llm-finetuning
    - windows
    - unsloth
    - conda
    - pytorch
    - setup-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# How to Fine-Tune LLMs on Windows with Unsloth

Three methods: [Conda](#method-1-windows-via-conda), [Docker](#method-2-docker), [WSL](#method-3-wsl). If PyTorch is already installed, `pip install unsloth` may work directly.

## Unsloth Studio (Web UI)

Works on Windows out of the box:

```bash
irm https://unsloth.ai/install.ps1 | iex
```

Update with `unsloth studio update`. Launch:

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Details: https://unsloth.ai/docs/new/studio/install

## Method 1 - Windows via Conda

### 1. Install Miniconda

Use [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions) or [Anaconda](https://www.anaconda.com/download). In PowerShell:

```ps
Invoke-WebRequest -Uri "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -OutFile ".\miniconda.exe"
Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
del .\miniconda.exe
```

After installing, open **Anaconda Powershell Prompt** from Start.

### 2. Create conda environment

```bash
conda create --name unsloth_env python==3.12 -y
conda activate unsloth_env
```

### 3. Verify GPU

Run `nvidia-smi` in PowerShell to confirm GPU and note CUDA version. If it fails, reinstall [NVIDIA drivers](https://www.nvidia.com/en-us/drivers/).

### 4. Install PyTorch

Match the CUDA version shown by `nvidia-smi` (change `130` below). Verify the version exists at https://pytorch.org/:

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
```

Verify in Python:

```python
import torch
print(torch.cuda.is_available())
A = torch.ones((10, 10), device = "cuda")
B = torch.ones((10, 10), device = "cuda")
A @ B
```

`torch.cuda.is_available()` must return `True`. The matrix multiplication should output 10s.

> [!danger] Confirm PyTorch works before proceeding. If it fails, reinstall CUDA drivers.

### 5. Install Unsloth

Exit Python first (`exit()`), then:

```bash
pip install unsloth
```

### 6. Verify Unsloth

Use any script from [[073-get-started-unsloth-notebooks|Unsloth Notebooks]] (save as `.py`), or the test script below:

```python
from unsloth import FastLanguageModel, FastModel
import torch
from trl import SFTTrainer, SFTConfig
from datasets import load_dataset
max_seq_length = 512
url = "https://huggingface.co/datasets/laion/OIG/resolve/main/unified_chip2.jsonl"
dataset = load_dataset("json", data_files = {"train" : url}, split = "train")

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gemma-3-270m-it",
    max_seq_length = max_seq_length, # Choose any for long context!
    load_in_4bit = True,  # 4-bit quantization. False = 16-bit LoRA.
    load_in_8bit = False, # 8-bit quantization
    load_in_16bit = False, # 16-bit LoRA
    full_finetuning = False, # Use for full fine-tuning.
    trust_remote_code = False, # Enable to support new models
    # token = "hf_...", # use one if using gated models
)

# Do model patching and add fast LoRA weights
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    max_seq_length = max_seq_length,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)

trainer = SFTTrainer(
    model = model,
    train_dataset = dataset,
    tokenizer = tokenizer,
    args = SFTConfig(
        max_seq_length = max_seq_length,
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 10,
        max_steps = 60,
        logging_steps = 1,
        output_dir = "outputs",
        optim = "adamw_8bit",
        seed = 3407,
        dataset_num_proc = 1,
    ),
)
trainer.train()
```

Expected output on success:

```
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
🦥 Unsloth Zoo will now patch everything to make training faster!
==((====))==  Unsloth 2026.1.4: Fast Gemma3 patching. Transformers: 4.57.6.
   \   /|    NVIDIA GeForce RTX 3060. Num GPUs = 1. Max memory: 12.0 GB. Platform: Windows.
O^O/ \_/ \    Torch: 2.10.0+cu130. CUDA: 8.6. CUDA Toolkit: 13.0. Triton: 3.6.0
\        /    Bfloat16 = TRUE. FA [Xformers = 0.0.34. FA2 = False]
 "-____-"     Free license: http://github.com/unslothai/unsloth
```

## Method 2 - Docker

No setup or dependency issues. [`unsloth/unsloth`](https://hub.docker.com/r/unsloth/unsloth) is the only Docker image (works for Blackwell/50-series GPUs too). Full guide: https://unsloth.ai/docs/blog/how-to-fine-tune-llms-with-unsloth-and-docker

### 1. Install Docker and NVIDIA Container Toolkit

Docker via [Linux](https://docs.docker.com/engine/install/) or [Desktop](https://docs.docker.com/desktop/), then [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation):

```bash
export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
sudo apt-get update && sudo apt-get install -y \
  nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```

### 2. Run the container

```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
```

### 3. Access Jupyter Lab

Go to http://localhost:8888, open `unsloth-notebooks` tabs.

### 4. Start training

Follow the [[064-get-started-fine-tuning-llms-guide|Fine-tuning Guide]], [[072-get-started-reinforcement-learning-rl-guide|RL Guide]], or use premade [[073-get-started-unsloth-notebooks|notebooks]].

### GPU not discovered?

Try [#method-3-wsl](#method-3-wsl) instead.

## Method 3 - WSL

### 1. Install WSL

```bash
wsl.exe --install Ubuntu-24.04
wsl.exe -d Ubuntu-24.04
```

If WSL is already installed, enter via `wsl` in Command Prompt.

### 2. Install Python

```bash
sudo apt update
sudo apt install python3 python3-full python3-pip python3-venv -y
```

### 3. Install PyTorch

```bash
pip install torch torchvision --force-reinstall --index-url https://download.pytorch.org/whl/cu130
```

If permission issues, add `--break-system-packages`.

### 4. Install Unsloth and Jupyter

```bash
pip install unsloth jupyter
```

If permission issues, add `--break-system-packages`.

### 5. Launch

```bash
jupyter notebook
```

Load notebooks from [[073-get-started-unsloth-notebooks|unsloth-notebooks]] or download `.ipynb` from Colab.

> [!warning] GRPO/vLLM do not support Windows directly -- only via WSL or Linux.

## Troubleshooting / Advanced

1. Install `torch` and `triton` from https://pytorch.org. Example: `pip install torch torchvision torchaudio triton`
2. Confirm CUDA via `nvcc`. If it fails, install `cudatoolkit` or CUDA drivers.
3. Intel GPU: follow the [[053-get-started-install-intel|Intel Windows guide]]
4. Install `xformers` manually. Check with `python -m xformers.info`. See https://github.com/facebookresearch/xformers. Alternatively, install `flash-attn` for Ampere GPUs. You can also try installing `vllm` to test.
5. Verify Python, CUDA, CUDNN, `torch`, `triton`, and `xformers` version compatibility via the [PyTorch Compatibility Matrix](https://github.com/pytorch/pytorch/blob/main/RELEASE.md#release-compatibility-matrix).
6. Install `bitsandbytes` and verify with `python -m bitsandbytes`.
7. GPU not detected in Docker on Windows: `nvcc --version` must match the CUDA version shown by `nvidia-smi` on the host. Follow [Docker's GPU guide](https://docs.docker.com/desktop/features/gpu/).

## Uninstall Unsloth Studio

### 1. Remove application

- WSL: `rm -rf ~/.unsloth/studio/unsloth_studio`
- Windows (PowerShell): `Remove-Item -Recurse -Force "$HOME\.unsloth\studio\unsloth_studio"`

Keeps model checkpoints, exports, history, cache, and chats intact.

### 2. Remove shortcuts and symlinks

```bash
Remove-Item -Force "$HOME\Desktop\Unsloth Studio.lnk"
Remove-Item -Force "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Unsloth Studio.lnk"
```

### 3. Remove CLI command

- WSL: `rm -f ~/.local/bin/unsloth`
- Windows: open Settings > System > About > Advanced system settings > Environment Variables, find `Path` under User variables, remove the entry pointing to `.unsloth\studio\...\Scripts`.

### 4. Remove everything (optional)

Delete entire Unsloth folder (history, cache, chats, checkpoints, exports):

- WSL/Linux: `rm -rf ~/.unsloth`
- Windows (PowerShell): `Remove-Item -Recurse -Force "$HOME\.unsloth"`

HF model files are stored separately in the Hugging Face cache and are not removed by any of the above steps.

#dataset-preparation #llm-finetuning #windows #unsloth #setup-guide
