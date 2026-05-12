---
title: SpecBundle Usage - SGLang Documentation
url: https://docs.sglang.io/cookbook/specbundle/specbundle_usage
source: sitemap
fetched_at: 2026-05-11T05:49:43.345421031-03:00
rendered_js: false
word_count: 557
summary: SpecBundle is an open initiative that provides production-grade EAGLE3 draft models to improve speculative decoding efficiency for open-source large language models. The document explains how to deploy these models using SGLang and evaluate their performance through benchmark scripts.
tags:
    - speculative-decoding
    - eagle3
    - llm-inference
    - sglang
    - model-optimization
    - performance-benchmarking
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

![specbundle logo](https://mintcdn.com/lmsysorg/iZdDMbLWP1BLEIzC/logo/logo.png?fit=max&auto=format&n=iZdDMbLWP1BLEIzC&q=85&s=b27d467947ee2167744cb07b69badf00)

## About SpecBundle

Speculative decoding, especially EAGLE3, offer strong theoretical guarantees alongside consistent empirical improvements in token acceptance rate and end-to-end inference speed. However, despite these advances, adoption of speculative decoding—especially EAGLE3—remains limited in the open-source ecosystem, due primarily to three key factors.

1. Lack of production-ready training infrastructure: Existing speculative decoding toolchains are largely research prototypes, offering limited system-level optimization and inadequate support for diverse architectures and large-scale models.
2. Scarcity of high-quality draft models: Effective speculative decoding depends on strong draft models, yet publicly available EAGLE3-compatible checkpoints are extremely limited, primarily originating from the original authors.
3. Insufficient training scale of existing drafts: Most available draft models are trained on small or curated datasets and fail to generalize to the large, diverse corpora used in modern LLM training, resulting in low token acceptance rates and diminished practical speedups.

**SpecBundle** is a direct response to these limitations. Jointly driven by the open-source community and industry partners including **Ant Group**, **Meituan**, **Nex-AGI** and **EigenAI**, **SpecBundle** represents the **first open initiative** aimed at democratizing speculative decoding by providing high-performance, production-grade EAGLE3 draft model weights for mainstream open-source LLMs. This initiative also serves to verify the robustness of the [**SpecForge**](https://github.com/sgl-project/SpecForge) framework through multiple scales and architectures.

## Installation

```
git clone https://github.com/sgl-project/SpecForge.git
```

### Launch SGLang Server with SpecBundle models

You can use the following command to launch the SGLang server with SpecBundle models. Please add `--tp`, `--ep` and `--mem-fraction-static` arguments when you encounter memory issues.

```
python3 -m sglang.launch_server \
    --model <target-model-path> \
    --speculative-algorithm EAGLE3 \
    --speculative-draft-model-path <draft-model-path> \
    --speculative-num-steps 3 \
    --speculative-eagle-topk 1 \
    --speculative-num-draft-tokens 4
```

For example:

```
SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 python3 -m sglang.launch_server \
    --model Qwen/Qwen3-30B-A3B-Instruct-2507 \
    --speculative-algorithm EAGLE3 \
    --speculative-draft-model-path lmsys/SGLang-EAGLE3-Qwen3-30B-A3B-Instruct-2507-SpecForge-Nex \
    --speculative-num-steps 3 \
    --speculative-eagle-topk 1 \
    --speculative-num-draft-tokens 4 \
    --tp 4
```

### Use SpecBundle to compare the performance of Speculative Decoding draft models

We provide a benchmark suite to evaluate the performance of SpecBundle draft models [here](https://github.com/sgl-project/SpecForge/tree/main/benchmarks).

#### Example:

1. Launch a SGLang Server

```
SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 python3 -m sglang.launch_server \
    --model Qwen/Qwen3-30B-A3B-Instruct-2507 \
    --speculative-algorithm EAGLE3 \
    --speculative-draft-model-path lmsys/SGLang-EAGLE3-Qwen3-30B-A3B-Instruct-2507-SpecForge-Nex \
    --speculative-num-steps 3 \
    --speculative-eagle-topk 1 \
    --speculative-num-draft-tokens 4 \
    --tp 4
```

2. Use the benchmark suite to evaluate the performance of SpecBundle draft models

`bench_eagle3.py` can help you launch a SGLang server process and a Benchmarking process concurrently. In this way, you don’t have to launch the SGLang server manually, this script will manually handle the SGLang launch under different speculative decoding configurations. Some important arguments are:

- `--model-path`: the path to the target model.
- `--speculative-draft-model-path`: the path to the draft model.
- `--port`: the port to launch the SGLang server.
- `--trust-remote-code`: trust the remote code.
- `--mem-fraction-static`: the memory fraction for the static memory.
- `--tp-size`: the tensor parallelism size.
- `--attention-backend`: the attention backend.
- `--config-list`: the list of speculative decoding configuration to test, the format is `<batch-size>,<num-steps>,<topk>,<num-draft-tokens>`.
- `--benchmark-list`: the list of benchmarks to test, the format is `<benchmark-name>:<num-prompts>:<subset>`.

```
cd SpecForge/benchmarks
python bench_eagle3.py \
    --model-path Qwen/Qwen3-30B-A3B-Instruct-2507 \
    --port 30000 \
    --config-list 1,3,1,4 \
    --benchmark-list mtbench:5 gsm8k:100 \
    --skip-launch-server
```

**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate test command for your model and benchmark.

Launch Mode

With ServerLaunch SGLang server & Benchmark concurrentlyWithout ServerConnect to an existing server (--skip-launch-server)

Model Path

Path to the target model.

Port

Port to launch/connect the SGLang server.

Config List

Format: &lt;batch-size&gt;,&lt;num-steps&gt;,&lt;topk&gt;,&lt;num-draft-tokens&gt;

Benchmark List

Format: &lt;benchmark-name&gt;:&lt;num-prompts&gt;:&lt;subset&gt;. Supported: aime, ceval, financeqa, gpqa, gsm8k, humaneval, livecodebench, math500, mmlu, mmstar, mtbench, simpleqa

Draft Model Path

Path to the speculative draft model.

TP Size

Number of GPUs for Tensor Parallelism.

Memory Fraction Static

The memory fraction for the static memory.

Attention Backend

The attention backend used in sglang

Trust Remote Code

EnabledWhether to trust remote code.

Generated Command

```
python bench_eagle3.py \
  --model-path meta-llama/Llama-3.1-8B-Instruct \
  --port 30000 \
  --config-list 1,3,1,4 \
  --benchmark-list mtbench:5 ceval:5:accountant \
  --tp-size 1 \
  --mem-fraction-static 0.9 \
  --trust-remote-code
```

It will generate a json file, content is listed below:

```
{
  "mtbench": [
    {
      "batch_size": 1,
      "steps": null,
      "topk": null,
      "num_draft_tokens": null,
      "metrics": [
        {
          "latency": 12.232808108034078,
          "output_throughput": 319.71399906382845,
          "accept_length": 2.170366259711432,
          "accuracy": null,
          "num_questions": 5,
          "num_valid_predictions": 0,
          "categorical_performance": null
        }
      ],
      "num_samples": 5
    }
  ],
  "gsm8k": [
    {
      "batch_size": 1,
      "steps": null,
      "topk": null,
      "num_draft_tokens": null,
      "metrics": [
        {
          "latency": 37.42077191895805,
          "output_throughput": 373.6160234823207,
          "accept_length": 2.643410852713178,
          "accuracy": 0.96,
          "num_questions": 100,
          "num_valid_predictions": 100,
          "categorical_performance": null
        }
      ],
      "num_samples": 100
    }
  ]
}
```

## Performance Scores

We evaluate the performance of SpecBundle draft models on various benchmarks, please visit the [Performance Dashboard](https://docs.sglang.io/SpecForge/SpecBundle/index.html) for more details.