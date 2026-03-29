---
title: Evaluating New Models with SGLang — SGLang
url: https://docs.sglang.io/developer_guide/evaluating_new_models.html
source: crawler
fetched_at: 2026-02-04T08:47:16.136702509-03:00
rendered_js: false
word_count: 259
summary: This document provides instructions and command-line examples for benchmarking the accuracy and performance of LLMs and VLMs using SGLang. It covers standard evaluation metrics, latency and throughput testing, and reporting requirements for model verification.
tags:
    - model-evaluation
    - sglang
    - benchmarking
    - llm-performance
    - vlm-accuracy
    - inference-testing
category: guide
---

## Contents

## Evaluating New Models with SGLang[#](#evaluating-new-models-with-sglang "Link to this heading")

This document provides commands for evaluating models’ accuracy and performance. Before open-sourcing new models, we strongly suggest running these commands to verify whether the score matches your internal benchmark results.

**For cross verification, please submit commands for installation, server launching, and benchmark running with all the scores and hardware requirements when open-sourcing your models.**

[Reference: MiniMax M2](https://github.com/sgl-project/sglang/pull/12129)

## Accuracy[#](#accuracy "Link to this heading")

### LLMs[#](#llms "Link to this heading")

SGLang provides built-in scripts to evaluate common benchmarks.

**MMLU**

```
python-msglang.test.run_eval\
--eval-namemmlu\
--port30000\
--num-examples1000\
--max-tokens8192
```

**GSM8K**

```
python-msglang.test.few_shot_gsm8k\
--hosthttp://127.0.0.1\
--port30000\
--num-questions200\
--num-shots5
```

**HellaSwag**

```
pythonbenchmark/hellaswag/bench_sglang.py\
--hosthttp://127.0.0.1\
--port30000\
--num-questions200\
--num-shots20
```

**GPQA**

```
python-msglang.test.run_eval\
--eval-namegpqa\
--port30000\
--num-examples198\
--max-tokens120000\
--repeat8
```

Tip

For reasoning models, add `--thinking-mode <mode>` (e.g., `qwen3`, `deepseek-r1`, `deepseek-v3`). You may skip it if the model has forced thinking enabled.

**HumanEval**

```
pipinstallhuman_eval

python-msglang.test.run_eval\
--eval-namehumaneval\
--num-examples10\
--port30000
```

### VLMs[#](#vlms "Link to this heading")

**MMMU**

```
pythonbenchmark/mmmu/bench_sglang.py\
--port30000\
--concurrency64
```

Tip

You can set max tokens by passing `--extra-request-body '{"max_tokens": 4096}'`.

For models capable of processing video, we recommend extending the evaluation to include `VideoMME`, `MVBench`, and other relevant benchmarks.

## Performance[#](#performance "Link to this heading")

Performance benchmarks measure **Latency** (Time To First Token - TTFT) and **Throughput** (tokens/second).

### LLMs[#](#id1 "Link to this heading")

**Latency-Sensitive Benchmark**

This simulates a scenario with low concurrency (e.g., single user) to measure latency.

```
python-msglang.bench_serving\
--backendsglang\
--host0.0.0.0\
--port30000\
--dataset-namerandom\
--num-prompts10\
--max-concurrency1
```

**Throughput-Sensitive Benchmark**

This simulates a high-traffic scenario to measure maximum system throughput.

```
python-msglang.bench_serving\
--backendsglang\
--host0.0.0.0\
--port30000\
--dataset-namerandom\
--num-prompts1000\
--max-concurrency100
```

**Single Batch Performance**

You can also benchmark the performance of processing a single batch offline.

```
python-msglang.bench_one_batch_server\
--model<model-path>\
--batch-size8\
--input-len1024\
--output-len1024
```

You can run more granular benchmarks:

- **Low Concurrency**: `--num-prompts 10 --max-concurrency 1`
- **Medium Concurrency**: `--num-prompts 80 --max-concurrency 16`
- **High Concurrency**: `--num-prompts 500 --max-concurrency 100`

## Reporting Results[#](#reporting-results "Link to this heading")

For each evaluation, please report:

1. **Metric Score**: Accuracy % (LLMs and VLMs); Latency (ms) and Throughput (tok/s) (LLMs only).
2. **Environment settings**: GPU type/count, SGLang commit hash.
3. **Launch configuration**: Model path, TP size, and any special flags.
4. **Evaluation parameters**: Number of shots, examples, max tokens.