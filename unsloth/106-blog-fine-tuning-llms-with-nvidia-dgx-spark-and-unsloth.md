---
title: Fine-tuning LLMs with NVIDIA DGX Spark and Unsloth
url: https://unsloth.ai/docs/blog/fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth.md
source: llms
fetched_at: 2026-04-27T18:15:23.741218703-03:00
rendered_js: false
word_count: 567
summary: This document serves as a tutorial detailing how to fine-tune Large Language Models (LLMs) using Unsloth on the NVIDIA DGX Spark. It provides step-by-step instructions covering Docker image creation, container launching, and running RL training notebooks for models like gpt-oss.
tags:
    - llm-fine-tuning
    - nvidia-dgx-spark
    - unsloth
    - docker-tutorial
    - rl-training
    - model-deployment
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Fine-tuning LLMs with NVIDIA DGX Spark and Unsloth

Unsloth enables local fine-tuning of LLMs with up to **200B parameters** on the NVIDIA DGX Spark (128 GB unified memory). Demonstrated at [OpenAI DevDay](https://x.com/UnslothAI/status/1976284209842118714): gpt-oss-20b trained with RL to auto-win 2048. gpt-oss-120b QLoRA 4-bit uses ~**68GB** unified memory.

After 1,000 steps / 4 hours RL training, gpt-oss greatly outperforms the original on 2048; longer training further improves results.

## Step-by-Step Tutorial

### 1. Build Docker image

```bash
sudo apt update && sudo apt install -y wget
wget -O Dockerfile "https://raw.githubusercontent.com/unslothai/notebooks/main/Dockerfile_DGX_Spark"
docker build -f Dockerfile -t unsloth-dgx-spark .
```

<details>
<summary>Full DGX Spark Dockerfile</summary>

```python
FROM nvcr.io/nvidia/pytorch:25.09-py3

# Set CUDA environment variables
ENV CUDA_HOME=/usr/local/cuda-13.0/
ENV CUDA_PATH=$CUDA_HOME
ENV PATH=$CUDA_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV C_INCLUDE_PATH=$CUDA_HOME/include:$C_INCLUDE_PATH
ENV CPLUS_INCLUDE_PATH=$CUDA_HOME/include:$CPLUS_INCLUDE_PATH

# Install triton from source for latest blackwell support
RUN git clone https://github.com/triton-lang/triton.git && \
    cd triton && \
    git checkout c5d671f91d90f40900027382f98b17a3e04045f6 && \
    pip install -r python/requirements.txt && \
    pip install . && \
    cd ..

# Install xformers from source for blackwell support
RUN git clone --depth=1 https://github.com/facebookresearch/xformers --recursive && \
    cd xformers && \
    export TORCH_CUDA_ARCH_LIST="12.1" && \
    python setup.py install && \
    cd ..

# Install unsloth and other dependencies
RUN pip install unsloth unsloth_zoo bitsandbytes==0.48.0 transformers==4.56.2 trl==0.22.2

# Launch the shell
CMD ["/bin/bash"]
```

</details>

### 2. Launch container

```bash
docker run -it \
    --gpus=all \
    --net=host \
    --ipc=host \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    -v $(pwd):$(pwd) \
    -v $HOME/.cache/huggingface:/root/.cache/huggingface \
    -w $(pwd) \
    unsloth-dgx-spark
```

### 3. Start Jupyter and run notebooks

All [[073-get-started-unsloth-notebooks|Unsloth notebooks]] work on DGX Spark (including 120b) -- just remove installation cells. RL notebook for gpt-oss 20b 2048: [gpt_oss_(20B)_Reinforcement_Learning_2048_Game_DGX_Spark.ipynb](https://github.com/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_Reinforcement_Learning_2048_Game_DGX_Spark.ipynb).

```bash
NOTEBOOK_URL="https://raw.githubusercontent.com/unslothai/notebooks/refs/heads/main/nb/gpt_oss_(20B)_Reinforcement_Learning_2048_Game_DGX_Spark.ipynb"
wget -O "gpt_oss_20B_RL_2048_Game.ipynb" "$NOTEBOOK_URL"

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

After fine-tuning, [[091-basics-inference-and-deployment|save and deploy]] models locally on DGX Spark.

## Unified Memory Usage

gpt-oss-120b QLoRA 4-bit: ~**68GB** unified memory.

## Video Tutorial

Fine-tuning tutorial by Tim from [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm): [YouTube](https://www.youtube.com/watch?t=962s&v=zs-J9sKxvoM)

Credits: [Lakshmi Ramesh](https://www.linkedin.com/in/rlakshmi24/) and [Barath Anandan](https://www.linkedin.com/in/barathsa/) from NVIDIA.

#unsloth #dgx-spark #docker #rl-training #fine-tuning
