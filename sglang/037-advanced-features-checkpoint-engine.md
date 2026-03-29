---
title: Checkpoint Engine Integration — SGLang
url: https://docs.sglang.io/advanced_features/checkpoint_engine.html
source: crawler
fetched_at: 2026-02-04T08:46:58.549662099-03:00
rendered_js: false
word_count: 491
summary: This document explains how to integrate and configure the SGLang checkpoint engine to enable fast, distributed loading of model weights across single and multi-node environments.
tags:
    - sglang
    - checkpoint-engine
    - distributed-loading
    - multi-node
    - performance-optimization
    - model-initialization
category: guide
---

## Contents

## Checkpoint Engine Integration[#](#checkpoint-engine-integration "Link to this heading")

The SGLang checkpoint engine integration provides an efficient way to load model weights using a distributed checkpoint loading system. This feature significantly reduces model loading time, especially for large models and multi-node setups, by parallelizing the weight loading process across multiple processes and nodes.

## Overview[#](#overview "Link to this heading")

The checkpoint engine integration allows SGLang to:

- Load model weights in parallel using multiple processes
- Distribute weight loading across multiple nodes to increase effective disk bandwidth
- Overlap weight loading with other initialization tasks like CUDA graph capture
- Support both single-node and multi-node deployments

## Installation[#](#installation "Link to this heading")

First, install the checkpoint engine package:

```
pipinstall'checkpoint-engine[p2p]'
```

## Architecture[#](#architecture "Link to this heading")

The system consists of two main components:

1. **SGLang Server**: Runs with `--wait-for-initial-weights` flag to wait for weights before becoming ready
2. **Checkpoint Engine Workers**: Separate processes (managed by torchrun) that load and distribute model weights

The checkpoint engine uses a parameter server architecture with support for:

- **Broadcast mode**: Weights are broadcast from loading processes to inference processes
- **P2P mode**: Direct peer-to-peer weight transfer between processes
- **All mode**: Combination of both broadcast and P2P methods

## Usage Examples[#](#usage-examples "Link to this heading")

### Single Node Setup[#](#single-node-setup "Link to this heading")

**Terminal 1 - Launch SGLang Server:**

```
python-msglang.launch_server\
--model-pathQwen/Qwen3-8B\
--tp8\
--load-formatdummy\
--wait-for-initial-weights
```

**Terminal 2 - Run Checkpoint Engine:**

Using sglang entrypoint:

```
python-msglang.srt.checkpoint_engine.update\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size8
```

Using torchrun directly:

```
torchrun--nproc-per-node8\
examples/checkpoint_engine/update.py\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size8
```

### Multi-Node Setup (2 Nodes)[#](#multi-node-setup-2-nodes "Link to this heading")

**Node 0:**

Launch SGLang server:

```
python-msglang.launch_server\
--model-pathQwen/Qwen3-8B\
--tp8\
--load-formatdummy\
--wait-for-initial-weights\
--host[IP]
```

Run checkpoint engine:

Using sglang entrypoint (recommended):

```
python-msglang.srt.checkpoint_engine.update\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size8
```

Using torchrun directly:

```
torchrun--nproc-per-node8\
--nnodes2\
--node-rank0\
--master-addr[IP]\
--master-port29500\
examples/checkpoint_engine/update.py\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size8
```

**Node 1:**

Launch SGLang server:

```
python-msglang.launch_server\
--model-pathQwen/Qwen3-8B\
--tp8\
--load-formatdummy\
--wait-for-initial-weights\
--host[IP]
```

Run checkpoint engine:

Using sglang entrypoint (recommended):

```
python-msglang.srt.checkpoint_engine.update\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size8
```

Using torchrun directly:

```
torchrun--nproc-per-node8\
--nnodes2\
--node-rank1\
--master-addr[IP]\
--master-port29500\
examples/checkpoint_engine/update.py\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size8
```

### Multi-Node Setup with Tensor Parallelism (TP=16)[#](#multi-node-setup-with-tensor-parallelism-tp-16 "Link to this heading")

**Node 0:**

Launch SGLang server:

```
python-msglang.launch_server\
--model-pathQwen/Qwen3-8B\
--tp8\
--load-formatdummy\
--wait-for-initial-weights\
--host[IP]\
--dist-init-addr[IP]:9120\
--nnodes2\
--node-rank0
```

Run checkpoint engine:

Using sglang entrypoint (recommended):

```
python-msglang.srt.checkpoint_engine.update\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size16
```

Using torchrun directly:

```
torchrun--nproc-per-node8\
--nnodes2\
--node-rank0\
--master-addr[IP]\
--master-port29500\
examples/checkpoint_engine/update.py\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size16
```

**Node 1:**

Launch SGLang server:

```
python-msglang.launch_server\
--model-pathQwen/Qwen3-8B\
--tp8\
--load-formatdummy\
--wait-for-initial-weights\
--host[IP]\
--dist-init-addr[IP]:9120\
--nnodes2\
--node-rank1
```

Run checkpoint engine:

Using sglang entrypoint (recommended):

```
python-msglang.srt.checkpoint_engine.update\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size16
```

Using torchrun directly:

```
torchrun--nproc-per-node8\
--nnodes2\
--node-rank1\
--master-addr[IP]\
--master-port29500\
examples/checkpoint_engine/update.py\
--update-methodbroadcast\
--checkpoint-path/path/to/Qwen/Qwen3-8B/\
--inference-parallel-size16
```

## Configuration Options[#](#configuration-options "Link to this heading")

### SGLang Server Options[#](#sglang-server-options "Link to this heading")

- `--load-format dummy`: Use dummy format for initial loading (allows overlapping with other tasks)
- `--wait-for-initial-weights`: Wait for checkpoint engine to provide weights before becoming ready
- `--host`: Host address for multi-node setups
- `--dist-init-addr`: Distributed initialization address for tensor parallelism

### Checkpoint Engine Options[#](#checkpoint-engine-options "Link to this heading")

- `--update-method`: Weight update method (`broadcast`, `p2p`, or `all`)
- `--checkpoint-path`: Path to model checkpoint directory
- `--inference-parallel-size`: Number of inference parallel processes
- `--endpoint`: SGLang server endpoint (default: `http://localhost:19730`)
- `--checkpoint-name`: Name for the checkpoint (default: `my-checkpoint-iter-0`)
- `--save-metas-file`: File to save checkpoint metadata
- `--load-metas-file`: File to load checkpoint metadata from
- `--uds`: Unix domain socket path for communication
- `--weight-version`: Version identifier for weights

## Performance Benefits[#](#performance-benefits "Link to this heading")

The checkpoint engine provides significant time savings in two main aspects:

1. **Multi-node Loading**: Each node only loads a portion of weights from disk, effectively increasing disk bandwidth. More participating nodes provide greater acceleration. Preliminary tests show 20-second acceleration when loading DeepSeek-R1 on H20-3e with two nodes.
2. **Single Process Optimization**: Using dummy format allows overlapping disk-to-CPU transfer with CUDA graph capture and other initialization tasks, providing additional time savings.

## Troubleshooting[#](#troubleshooting "Link to this heading")

- Ensure checkpoint engine package is installed: `pip install 'checkpoint-engine[p2p]'`
- Verify network connectivity between nodes in multi-node setups
- Check that the checkpoint path contains valid model files
- Monitor logs for connection errors between SGLang server and checkpoint engine
- Use `--sleep-time` parameter to add delays if needed for debugging

## References[#](#references "Link to this heading")

- [Checkpoint Engine Repository](https://github.com/MoonshotAI/checkpoint-engine)