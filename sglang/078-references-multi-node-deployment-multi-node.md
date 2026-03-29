---
title: Multi-Node Deployment — SGLang
url: https://docs.sglang.io/references/multi_node_deployment/multi_node.html
source: crawler
fetched_at: 2026-02-04T08:48:05.210191357-03:00
rendered_js: false
word_count: 82
summary: This document provides instructions for deploying large language models like Llama 3.1 405B across multiple nodes using SGLang. It covers manual command-line configuration and automated multi-node inference using SLURM job scripts.
tags:
    - multi-node-deployment
    - distributed-inference
    - sglang
    - slurm
    - llama-3-1
    - tensor-parallelism
category: guide
---

## Multi-Node Deployment[#](#multi-node-deployment "Link to this heading")

## Llama 3.1 405B[#](#llama-3-1-405b "Link to this heading")

**Run 405B (fp16) on Two Nodes**

```
# replace 172.16.4.52:20000 with your own node ip address and port of the first node

python3-msglang.launch_server\
--model-pathmeta-llama/Meta-Llama-3.1-405B-Instruct\
--tp16\
--dist-init-addr172.16.4.52:20000\
--nnodes2\
--node-rank0

python3-msglang.launch_server\
--model-pathmeta-llama/Meta-Llama-3.1-405B-Instruct\
--tp16\
--dist-init-addr172.16.4.52:20000\
--nnodes2\
--node-rank1
```

Note that LLama 405B (fp8) can also be launched on a single node.

```
python-msglang.launch_server--model-pathmeta-llama/Meta-Llama-3.1-405B-Instruct-FP8--tp8
```

## DeepSeek V3/R1[#](#deepseek-v3-r1 "Link to this heading")

Please refer to [DeepSeek documents for reference](https://docs.sglang.io/basic_usage/deepseek.html#running-examples-on-multi-node).

## Multi-Node Inference on SLURM[#](#multi-node-inference-on-slurm "Link to this heading")

This example showcases how to serve SGLang server across multiple nodes by SLURM. Submit the following job to the SLURM cluster.

```
#!/bin/bash -l

#SBATCH -o SLURM_Logs/%x_%j_master.out
#SBATCH -e SLURM_Logs/%x_%j_master.err
#SBATCH -D ./
#SBATCH -J Llama-405B-Online-Inference-TP16-SGL

#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1  # Ensure 1 task per node
#SBATCH --cpus-per-task=18
#SBATCH --mem=224GB
#SBATCH --partition="lmsys.org"
#SBATCH --gres=gpu:8
#SBATCH --time=12:00:00

echo "[INFO] Activating environment on node $SLURM_PROCID"
if ! source ENV_FOLDER/bin/activate; then
    echo "[ERROR] Failed to activate environment" >&2
    exit 1
fi

# Define parameters
model=MODEL_PATH
tp_size=16

echo "[INFO] Running inference"
echo "[INFO] Model: $model"
echo "[INFO] TP Size: $tp_size"

# Set NCCL initialization address using the hostname of the head node
HEAD_NODE=$(scontrol show hostname "$SLURM_NODELIST" | head -n 1)
NCCL_INIT_ADDR="${HEAD_NODE}:8000"
echo "[INFO] NCCL_INIT_ADDR: $NCCL_INIT_ADDR"

# Launch the model server on each node using SLURM
srun --ntasks=2 --nodes=2 --output="SLURM_Logs/%x_%j_node$SLURM_NODEID.out" \
    --error="SLURM_Logs/%x_%j_node$SLURM_NODEID.err" \
    python3 -m sglang.launch_server \
    --model-path "$model" \
    --grammar-backend "xgrammar" \
    --tp "$tp_size" \
    --dist-init-addr "$NCCL_INIT_ADDR" \
    --nnodes 2 \
    --node-rank "$SLURM_NODEID" &

# Wait for the NCCL server to be ready on port 30000
while ! nc -z "$HEAD_NODE" 30000; do
    sleep 1
    echo "[INFO] Waiting for $HEAD_NODE:30000 to accept connections"
done

echo "[INFO] $HEAD_NODE:30000 is ready to accept connections"

# Keep the script running until the SLURM job times out
wait
```

Then, you can test the server by sending requests following other [documents](https://docs.sglang.io/basic_usage/openai_api_completions.html).

Thanks for [aflah02](https://github.com/aflah02) for providing the example, based on his [blog post](https://aflah02.substack.com/p/multi-node-llm-inference-with-sglang).