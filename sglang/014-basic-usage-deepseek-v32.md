---
title: DeepSeek V3.2 Usage — SGLang
url: https://docs.sglang.io/basic_usage/deepseek_v32.html
source: crawler
fetched_at: 2026-02-04T08:47:37.333313119-03:00
rendered_js: false
word_count: 1342
summary: This document provides comprehensive instructions for installing, configuring, and serving the DeepSeek V3.2 model family using the SGLang framework across various hardware platforms.
tags:
    - deepseek-v3-2
    - sglang
    - model-deployment
    - distributed-inference
    - gpu-acceleration
    - speculative-decoding
category: guide
---

## DeepSeek V3.2 Usage[#](#deepseek-v3-2-usage "Link to this heading")

DeepSeek-V3.2 model family equips DeepSeek-V3.1-Terminus with DeepSeek Sparse Attention (DSA) through continued training. With DSA, a fine-grained sparse attention mechanism powered by a lightning indexer, DeepSeek-V3.2 achieves efficiency improvements in long-context scenarios.

For reporting issues or tracking upcoming features, please refer to this [Roadmap](https://github.com/sgl-project/sglang/issues/11060).

Note: This document is originally written for the usage of [DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) model. The usage of [DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) or [DeepSeek-V3.2-Speciale](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale) is the same as DeepSeek-V3.2-Exp except for the tool call parser.

## Installation[#](#installation "Link to this heading")

### Docker[#](#docker "Link to this heading")

```
# H200/B200
dockerpulllmsysorg/sglang:latest

# MI350/MI355
dockerpulllmsysorg/sglang:v0.5.8-rocm700-mi35x

# MI300
# v0.5.8-rocm700-mi30x does not include PR #17504. Prefer the newest MI30x ROCm
# image tag from Docker Hub when available, or build from source (below).
dockerpulllmsysorg/sglang:v0.5.8-rocm700-mi30x


# NPUs
dockerpulllmsysorg/sglang:dsv32-a2
dockerpulllmsysorg/sglang:dsv32-a3
```

### Build From Source[#](#build-from-source "Link to this heading")

```
# Install SGLang
gitclonehttps://github.com/sgl-project/sglang
cdsglang
pip3installpip--upgrade
pip3install-e"python"
```

## Launch DeepSeek V3.2 with SGLang[#](#launch-deepseek-v3-2-with-sglang "Link to this heading")

To serve [DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) on 8xH200/B200 GPUs:

```
# Launch with TP + DP (Recommended)
python-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8--dp8--enable-dp-attention

# Launch with EP + DP
python-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8--ep8--dp8--enable-dp-attention

# Launch with Pure TP
python-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8

# Launch with TP on MI30x/MI35x
python3-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8--nsa-prefill-backendtilelang--nsa-decode-backendtilelang
```

### Configuration Tips[#](#configuration-tips "Link to this heading")

- **DP Attention (Recommended)**: For DeepSeek V3.2 model, the kernels are customized for the use case of `dp_size=8`, so DP attention (`--dp 8 --enable-dp-attention`) is the recommended configuration for better stability and performance. All test cases use this configuration by default.
- **Pure TP Mode**: Launching with pure TP (without `--dp` and `--enable-dp-attention`) is also supported. Note that this mode has not been fully validated in PD disaggregation scenarios.
- **Short-sequence MHA prefill (adaptive)**: For short prefill sequences (default threshold: **2048 tokens**), the NSA backend uses standard MHA automatically (no extra flags). On H200 (SM90) this path uses the FlashAttention variable-length kernel; on B200 (SM100) it uses TRT-LLM ragged MHA. MHA uses `MHA_ONE_SHOT` for best performance. `MHA_ONE_SHOT` computes multi-head attention over all tokens (both cached prefix and newly extended tokens) in a single kernel invocation, avoiding the overhead of chunked KV cache processing. This achieves optimal throughput for short sequences where total sequence length fits within the chunk capacity limit.
- **Choices of Attention Kernels**: The attention backend is automatically set to `nsa` attention backend for DeepSeek V3.2 model. In this backend, different kernels for sparse prefilling/decoding are implemented, which can be specified by `--nsa-prefill-backend` and `--nsa-decode-backend` server arguments. The choices of nsa prefill/decode attention kernels include:
  
  - `flashmla_sparse`: `flash_mla_sparse_fwd` kernel from `flash_mla` library. Can run on both Hopper and Blackwell GPUs. It requires bf16 q, kv inputs.
  - `flashmla_kv`: `flash_mla_with_kvcache` kernel from `flash_mla` library. Can run on both Hopper and Blackwell GPUs. It requires bf16 q, fp8 k\_cache inputs.
  - `fa3`: `flash_attn_with_kvcache` kernel from `flash_attn` library. Can only run on Hopper GPUs. It requires bf16 q, kv inputs.
  - `tilelang`: `tilelang` implementation that can run on GPU, HPU and NPU.
  - `aiter`: Aiter kernel on AMD HPUs. Can only be used as decode kernel.
- On the basis of performance benchmarks, the default configuration on H200 and B200 are set as follows :
  
  - H200: `flashmla_sparse` prefill attention (short-seq prefill uses MHA via FlashAttention varlen), `fa3` decode attention, `bf16` kv cache dtype.
  - B200: `flashmla_auto` prefill attention (short-seq prefill uses MHA via TRT-LLM ragged), `flashmla_kv` decode attention, `fp8_e4m3` kv cache dtype. `flashmla_auto` enables automatic selection of either `flashmla_sparse` or `flashmla_kv` kernel for prefill based on KV cache dtype, hardware, and heuristics. When FP8 KV cache is enabled and `total_kv_tokens < total_q_tokens * 512`, it uses the `flashmla_sparse` kernel; otherwise, it falls back to the `flashmla_kv` kernel. The heuristics may need to be tuned if the performance of either the `flashmla_sparse` or `flashmla_kv` kernel changes significantly.

## Multi-token Prediction[#](#multi-token-prediction "Link to this heading")

SGLang implements Multi-Token Prediction (MTP) for DeepSeek V3.2 based on [EAGLE speculative decoding](https://docs.sglang.io/advanced_features/speculative_decoding.html#EAGLE-Decoding). With this optimization, the decoding speed can be improved significantly on small batch sizes. Please look at [this PR](https://github.com/sgl-project/sglang/pull/11652) for more information.

Example usage with DP Attention:

```
python-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8--dp8--enable-dp-attention--speculative-algorithmEAGLE--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4
```

Example usage with Pure TP:

```
python-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8--speculative-algorithmEAGLE--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4
```

- The best configuration for `--speculative-num-steps`, `--speculative-eagle-topk` and `--speculative-num-draft-tokens` can be searched with [bench\_speculative.py](https://github.com/sgl-project/sglang/blob/main/scripts/playground/bench_speculative.py) script for given batch size. The minimum configuration is `--speculative-num-steps 1 --speculative-eagle-topk 1 --speculative-num-draft-tokens 2`, which can achieve speedup for larger batch sizes.
- The default value of `--max-running-requests` is set to `48` for MTP. For larger batch sizes, this value should be increased beyond the default value.

Tip

To enable the experimental overlap scheduler for EAGLE speculative decoding, set the environment variable `SGLANG_ENABLE_SPEC_V2=1`. This can improve performance by enabling overlap scheduling between draft and verification stages.

## Function Calling and Reasoning Parser[#](#function-calling-and-reasoning-parser "Link to this heading")

The usage of function calling and reasoning parser is the same as DeepSeek V3.1. Please refer to [Reasoning Parser](https://docs.sglang.io/advanced_features/separate_reasoning.html) and [Tool Parser](https://docs.sglang.io/advanced_features/tool_parser.html) documents.

To launch `DeepSeek-V3.2-Exp` with function calling and reasoning parser:

> Note: It is recommended to specify the chat-template, ensuring that you are within the sglang’s root directory.

```
python3-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Exp\
--trust-remote-code\
--tp-size8--dp-size8--enable-dp-attention\
--tool-call-parserdeepseekv31\
--reasoning-parserdeepseek-v3\
--chat-template./examples/chat_template/tool_chat_template_deepseekv32.jinja
```

To launch `DeepSeek-V3.2` with function calling and reasoning parser:

```
python3-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2\
--trust-remote-code\
--tp-size8--dp-size8--enable-dp-attention\
--tool-call-parserdeepseekv32\
--reasoning-parserdeepseek-v3
```

`DeepSeek-V3.2-Speciale` doesn’t support tool calling, so can only be launched with reasoning parser:

```
python3-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Speciale\
--trust-remote-code\
--tp-size8--dp-size8--enable-dp-attention\
--reasoning-parserdeepseek-v3
```

## NVFP4 Checkpoint[#](#nvfp4-checkpoint "Link to this heading")

To launch deepseek v3.2 [NVFP4 checkpoint](https://huggingface.co/nvidia/DeepSeek-V3.2-NVFP4) on Blackwell devices, the user needs to specify the quantization method as `modelopt_fp4`, and moe runner backend as one of `flashinfer_trtllm`(recommended), `flashinfer_cutlass` and `flashinfer_cutedsl`. Any other usage (parallelism, reasoning parser, …) is the same as FP8 checkpoint.

An example launching command can be:

```
python-msglang.launch_server--modelnvidia/DeepSeek-V3.2-NVFP4--tp4--quantizationmodelopt_fp4--moe-runner-backendflashinfer_trtllm--tool-call-parserdeepseekv32--reasoning-parserdeepseek-v3
```

## PD Disaggregation[#](#pd-disaggregation "Link to this heading")

Prefill Command:

```
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Exp\
--disaggregation-modeprefill\
--host$LOCAL_IP\
--port$PORT\
--tp8\
--dp8\
--enable-dp-attention\
--dist-init-addr${HOST}:${DIST_PORT}\
--trust-remote-code\
--disaggregation-bootstrap-port8998\
--mem-fraction-static0.9\
```

Decode command:

```
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Exp\
--disaggregation-modedecode\
--host$LOCAL_IP\
--port$PORT\
--tp8\
--dp8\
--enable-dp-attention\
--dist-init-addr${HOST}:${DIST_PORT}\
--trust-remote-code\
--mem-fraction-static0.9\
```

Router command:

```
python-msglang_router.launch_router--pd-disaggregation\
--prefill$PREFILL_ADDR8998\
--decode$DECODE_ADDR\
--host127.0.0.1\
--port8000\
```

If you need more advanced deployment methods or production-ready deployment methods, such as RBG or LWS-based deployment, please refer to [references/multi\_node\_deployment/rbg\_pd/deepseekv32\_pd.md](https://docs.sglang.io/references/multi_node_deployment/rbg_pd/deepseekv32_pd.html). Additionally, you can also find startup commands for DeepEP-based EP parallelism in the aforementioned documentation.

## Benchmarking Results[#](#benchmarking-results "Link to this heading")

### Accuracy Test with `gsm8k`[#](#accuracy-test-with-gsm8k "Link to this heading")

A simple accuracy benchmark can be tested with `gsm8k` dataset:

```
python3benchmark/gsm8k/bench_sglang.py--num-shots8--num-questions1319--parallel1319
```

The result is 0.956, which matches our expectation:

```
Accuracy:0.956
Invalid:0.000
Latency:25.109s
Outputthroughput:5226.235token/s
```

To test long-context accuracy, run gsm8k with `--num-shots 20`. The results are very close to the 8 shots results:

```
Accuracy: 0.956
Invalid: 0.000
Latency: 29.545 s
Output throughput: 4418.617 token/s
```

### Accuracy Test with `gpqa-diamond`[#](#accuracy-test-with-gpqa-diamond "Link to this heading")

Accuracy benchmark on long context can be tested on GPQA-diamond dataset with long output tokens and thinking enabled:

```
python3-msglang.test.run_eval--port30000--eval-namegpqa--num-examples198--max-tokens128000--repeat8--thinking-modedeepseek-v3
```

The mean accuracy over 8 runs shows 0.797, which matches the number 0.799 in official tech report.

```
Repeat:8,mean:0.797
Scores:['0.808','0.798','0.808','0.798','0.783','0.788','0.803','0.793']
```

For Deepseek V3.2, Deepseek recommends setting the sampling parameters to temperature = 1.0, top\_p = 0.95:

```
python3-msglang.test.run_eval--port30000--eval-namegpqa--num-examples198--max-tokens128000--repeat8--top-p0.95--temperature1.0--thinking-modedeepseek-v3

Repeat:8,mean:0.840
Scores:['0.848','0.808','0.848','0.838','0.879','0.813','0.838','0.848']
```

which matches the official score, 0.824, as reported in the [Deepseek-V3.2 technical report](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/assets/paper.pdf).

### Accuracy Test with `aime 2025`[#](#accuracy-test-with-aime-2025 "Link to this heading")

Prepare the environment by installing NeMo-Skills in the docker or your own virtual environment:

```
pip install git+https://github.com/NVIDIA/NeMo-Skills.git --ignore-installed blinker
```

Then launch the SGLang server:

```
python -m sglang.launch_server --model deepseek-ai/DeepSeek-V3.2-Exp --tp 8 --dp 8 --enable-dp-attention
```

**For `DeepSeek-V3.2` and `DeepSeek-V3.2-Speciale`** :

```
python3 -m sglang.launch_server   --model-path deepseek-ai/DeepSeek-V3.2   --trust-remote-code   --tp-size 8 --dp-size 8 --enable-dp-attention   --tool-call-parser deepseekv32   --reasoning-parser deepseek-v3
```

Run the following script to evaluate AIME 2025:

```
#! /bin/bash
export NEMO_SKILLS_DISABLE_UNCOMMITTED_CHANGES_CHECK=1

ns prepare_data aime25

PORT=30000
BACKEND=sglang
MODEL="deepseek-ai/DeepSeek-V3.2-Exp" # Should be changed to the model name
MODEL_NAME="dsv32-fp8"

echo "Starting AIME25 evaluation with model $MODEL on port $PORT using backend $BACKEND..."
ns eval \
  --benchmarks=aime25:4 \
  --server_type=$BACKEND \
  --model=$MODEL \
  --server_address=http://localhost:${PORT}/v1 \
  --output_dir=nemo_skills_aime25_${MODEL_NAME}_output_${BACKEND}_$(date +%Y%m%d_%H%M%S) \
  ++chat_template_kwargs.thinking=true \
  ++inference.temperature=1.0 \
  ++inference.top_p=0.95 \
  ++inference.tokens_to_generate=64000
  # ++inference.tokens_to_generate=120000 for Speciale model
```

Test results (8\*B200):

DeepSeek-V3.2-Exp：

DeepSeek-V3.2:

DeepSeek-V3.2-Speciale:

## DSA long sequence context parallel optimization(experimental)[#](#dsa-long-sequence-context-parallel-optimization-experimental "Link to this heading")

**Note: This feature is only verified on Hopper machines**

For context parallel in DeepSeek V3.2 model, we provide two different modes of splitting tokens, which can be controlled with argument `--nsa-prefill-cp-mode`.

### In sequence splitting (default setting)[#](#in-sequence-splitting-default-setting "Link to this heading")

The first mode can be enabled by `--nsa-prefill-cp-mode in-seq-split`. This mode implements context parallel for DSA by splitting the sequence uniformly between context parallel ranks. At attention stage, each cp rank computes the indexer results of sharded sequence, and collects the whole kv cache through all gather operator.

The communication group for context parallel reuses the one for attention tp, thus `cp_size` equals `atten_tp_size = tp_size / dp_size`.

Note that in sequence splitting mode has the following restrictions:

- The batch size is restricted to 1 for prefill batches
- Multi-node/PD disaggregation is still not supported
- `moe_dense_tp_size=1`, `kv_cache_dtype = "bf16"`, `moe_a2a_backend = "deepep"`
- To ensure `cp_size > 1`, the passed in `tp_size` must be larger than `dp_size`

For more details, please refer to PR https://github.com/sgl-project/sglang/pull/12065.

Example:

```
# In-seq splitting mode launched with EP + DP
python-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8--ep8--dp2--enable-dp-attention--enable-nsa-prefill-context-parallel--nsa-prefill-cp-modein-seq-split--max-running-requests32
```

### Round robin splitting[#](#round-robin-splitting "Link to this heading")

This mode can be enabled by specifying the parameter `--nsa-prefill-cp-mode round-robin-split`, which distributes tokens across ranks based on `token_idx % cp_size`.

In this scenario, compared with the aforementioned method, it additionally supports the fused MoE backend (the fused MoE backend may deliver better performance than DeepEP in single-machine scenarios), FP8 KV-cache, and multi-batch prefill inference. But it cannot be enabled with dp attention together.

For more details, please refer to PR https://github.com/sgl-project/sglang/pull/13959.

Example usage:

```
# Launch with FusedMoe + CP8
python-msglang.launch_server--modeldeepseek-ai/DeepSeek-V3.2-Exp--tp8--enable-nsa-prefill-context-parallel--nsa-prefill-cp-moderound-robin-split--max-running-requests32
```

### Pipeline Parallel + Context Parallel (PP + CP)[#](#pipeline-parallel-context-parallel-pp-cp "Link to this heading")

This mode combines Pipeline Parallelism (PP) and Context Parallelism (CP) to scale across multiple nodes, which can achieve better throughput and Time To First Token (TTFT). Note that this method has only been tested on H20 96G.

#### Standard Usage[#](#standard-usage "Link to this heading")

To launch with PP=2 and CP (via `round-robin-split` mode) on 2 nodes. This configuration uses the fused MoE kernel by default, which generally provides better performance.

For related development details, please refer to:

- Fused MoE + CP support: [PR #13959](https://github.com/sgl-project/sglang/pull/13959)
- PP + CP support: [Issue #15358](https://github.com/sgl-project/sglang/issues/15358) and [PR #16380](https://github.com/sgl-project/sglang/pull/16380)

Node 0:

```
exportSGLANG_PP_LAYER_PARTITION=30,31
python3-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Exp\
--nnodes2--node-rank0\
--dist-init-addr<HEAD_NODE_IP>:62001\
--tp8--pp-size2\
--dp-size1--moe-dense-tp-size1\
--enable-nsa-prefill-context-parallel\
--nsa-prefill-cp-moderound-robin-split\
--trust-remote-code\
--disable-radix-cache\
--mem-fraction-static0.8\
--max-running-requests128\
--chunked-prefill-size16384\
--cuda-graph-max-bs8\
--page-size64\
--watchdog-timeout3600\
--host0.0.0.0--port8000\
--tool-call-parserdeepseekv32
```

Node 1:

```
exportSGLANG_PP_LAYER_PARTITION=30,31
python3-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Exp\
--nnodes2--node-rank1\
--dist-init-addr<HEAD_NODE_IP>:62001\
--tp8--pp-size2\
--dp-size1--moe-dense-tp-size1\
--enable-nsa-prefill-context-parallel\
--nsa-prefill-cp-moderound-robin-split\
--trust-remote-code\
--disable-radix-cache\
--mem-fraction-static0.8\
--max-running-requests128\
--chunked-prefill-size16384\
--cuda-graph-max-bs8\
--page-size64\
--watchdog-timeout3600\
--host0.0.0.0--port8000\
--tool-call-parserdeepseekv32
```

#### PD Disaggregation with PP + CP[#](#pd-disaggregation-with-pp-cp "Link to this heading")

If using PD (Prefill-Decode) Disaggregation, the Prefill nodes can be configured with PP + CP as follows.

Prefill Node 0:

```
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Exp\
--served-model-namedeepseek-v32\
--nnodes2--node-rank0\
--dist-init-addr<PREFILL_HEAD_IP>:20102\
--tp8--pp-size2\
--dp-size1--moe-dense-tp-size1\
--enable-nsa-prefill-context-parallel\
--nsa-prefill-cp-moderound-robin-split\
--disaggregation-ib-devicemlx5_bond_0,mlx5_bond_1,mlx5_bond_2,mlx5_bond_3\
--trust-remote-code\
--disable-radix-cache\
--max-running-requests512\
--chunked-prefill-size4096\
--context-length131072\
--mem-fraction-static0.9\
--page-size64\
--enable-metrics\
--collect-tokens-histogram\
--tokenizer-worker-num8\
--host0.0.0.0--port30000
```

Prefill Node 1:

```
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3.2-Exp\
--served-model-namedeepseek-v32-prefill\
--nnodes2--node-rank1\
--dist-init-addr<PREFILL_HEAD_IP>:20102\
--tp8--pp-size2\
--dp-size1--moe-dense-tp-size1\
--enable-nsa-prefill-context-parallel\
--nsa-prefill-cp-moderound-robin-split\
--disaggregation-ib-devicemlx5_bond_0,mlx5_bond_1,mlx5_bond_2,mlx5_bond_3\
--trust-remote-code\
--disable-radix-cache\
--max-running-requests512\
--chunked-prefill-size4096\
--context-length131072\
--mem-fraction-static0.9\
--page-size64\
--enable-metrics\
--collect-tokens-histogram\
--tokenizer-worker-num8\
--host0.0.0.0--port30000
```

For the Decode nodes, it is recommended to use the **EP mode**.