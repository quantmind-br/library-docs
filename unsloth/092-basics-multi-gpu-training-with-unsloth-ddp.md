---
title: Multi-GPU Fine-tuning with Distributed Data Parallel (DDP)
url: https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth/ddp.md
source: llms
fetched_at: 2026-04-27T18:14:59.829455742-03:00
rendered_js: false
word_count: 898
summary: This document serves as a guide detailing how to perform multi-GPU fine-tuning of a model using Distributed Data Parallel (DDP) strategy, specifically showcasing this process via the Unsloth command-line interface (CLI).
tags:
    - multi-gpu
    - ddp
    - unsloth-cli
    - fine-tuning
    - pytorch
    - llm-training
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Multi-GPU Fine-tuning with Distributed Data Parallel (DDP)

DDP creates one model copy per GPU, feeds each distinct samples, and aggregates weight updates per optimizer step. More GPUs = more stable gradients + ~linear throughput increase.

> [!note] Unsloth DDP works with any training script, not just the CLI.

## Install Unsloth from Source

Use a [virtual environment](https://docs.python.org/3/tutorial/venv.html) (e.g. `uv venv --python 3.12 && source .venv/bin/activate`).

```bash
git clone https://github.com/unslothai/unsloth.git
cd unsloth
pip install .
```

## Demo: Qwen3-8B on alpaca-cleaned

Model: [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | Dataset: [yahma/alpaca-cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned) (SFT workload)

## Unsloth CLI Reference

```bash
$ python unsloth-cli.py --help
usage: unsloth-cli.py [-h] [--model_name MODEL_NAME] [--max_seq_length MAX_SEQ_LENGTH] [--dtype DTYPE]
                      [--load_in_4bit] [--dataset DATASET] [--r R] [--lora_alpha LORA_ALPHA]
                      [--lora_dropout LORA_DROPOUT] [--bias BIAS]
                      [--use_gradient_checkpointing USE_GRADIENT_CHECKPOINTING]
                      ...

options:
  -h, --help            show this help message and exit

Model Options:
  --model_name MODEL_NAME
                        Model name to load
  --max_seq_length MAX_SEQ_LENGTH
                        Maximum sequence length, default is 2048. We auto support RoPE Scaling
                        internally!

LoRA Options:
  --r R                 Rank for Lora model, default is 16. (common values: 8, 16, 32, 64, 128)
  --lora_alpha LORA_ALPHA
                        LoRA alpha parameter, default is 16. (common values: 8, 16, 32, 64, 128)

Training Options:
  --per_device_train_batch_size PER_DEVICE_TRAIN_BATCH_SIZE
                        Batch size per device during training, default is 2.
  --per_device_eval_batch_size PER_DEVICE_EVAL_BATCH_SIZE
                        Batch size per device during evaluation, default is 4.
  --gradient_accumulation_steps GRADIENT_ACCUMULATION_STEPS
                        Number of gradient accumulation steps, default is 4.
```

## Launching Multi-GPU Training

Use [torchrun](https://docs.pytorch.org/docs/stable/elastic/run.html) to spin up distributed processes. Verify GPU status first:

```bash
$ nvidia-smi
Mon Nov 24 12:53:00 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 80GB HBM3          On  |   00000000:04:00.0 Off |                    0 |
| N/A   32C    P0             69W /  700W |       0MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H100 80GB HBM3          On  |   00000000:05:00.0 Off |                    0 |
| N/A   30C    P0             68W /  700W |       0MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
```

### Training Command

```bash
# required:
#   --model_name
#   --dataset
# optional; experiment with these:
#   --learning_rate, --max_seq_length, --per_device_train_batch_size, --gradient_accumulation_steps, --max_steps
# to save the model at the end of training:
#   --save_model

torchrun --nproc_per_node=2 unsloth-cli.py \
  --model_name=Qwen/Qwen3-8B \
  --dataset=yahma/alpaca-cleaned \
  --learning_rate=2e-5 \
  --max_seq_length=2048 \
  --per_device_train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_steps=1000 \
  --save_model
```

Set `--nproc_per_node` to match your GPU count.

> [!tip] `torchrun` works with any Unsloth training script, including [scripts converted from Colab notebooks](https://github.com/unslothai/notebooks/tree/main/python_scripts). DDP auto-enables with >1 GPU.

### GPU Utilization During Training

```bash
$ nvidia-smi
Mon Nov 24 12:58:42 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 80GB HBM3          On  |   00000000:04:00.0 Off |                    0 |
| N/A   38C    P0            193W /  700W |   18903MiB /  81559MiB |     25%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H100 80GB HBM3          On  |   00000000:05:00.0 Off |                    0 |
| N/A   37C    P0            199W /  700W |   18905MiB /  81559MiB |     28%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
```

~19GB VRAM per H100. Training speed: ~1.1 iterations/s (constant per GPU; throughput scales ~linearly with GPU count).

## Training Metrics

Tested on [unsloth/Llama-3.2-1B-Instruct](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct) with [yahma/alpaca-cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned), rank-16 LoRA, 500 steps.

### LoRA Fine-tune (Full Precision)

- **Loss curves:** single GPU vs multi-GPU DDP match in scale/trend, but differ slightly since DDP processes 2x data per step (less step-to-step variability).
- **Epoch progress:** DDP completes an epoch in half the steps. Per-step timing is slightly slower due to distributed communication overhead.

### QLoRA Fine-tune (4-bit)

Same behaviors hold for QLoRA (4-bit loading). Useful for training large models on limited VRAM. Loss curves and epoch progress show identical relative patterns.

## Agent Query Endpoint

```
GET https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth/ddp.md?ask=<question>
```

#multi-gpu #ddp #pytorch #fine-tuning
