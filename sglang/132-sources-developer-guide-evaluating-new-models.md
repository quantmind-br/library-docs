---
title: Evaluating New Models with SGLang
url: https://docs.sglang.io/_sources/developer_guide/evaluating_new_models.md
source: crawler
fetched_at: 2026-02-04T08:48:49.428724882-03:00
rendered_js: false
word_count: 281
summary: This document provides instructions and command-line examples for evaluating the accuracy and performance of LLMs and VLMs using SGLang benchmarking scripts.
tags:
    - sglang
    - model-evaluation
    - benchmarking
    - llm-performance
    - vlm-accuracy
    - latency-testing
    - throughput-measurement
category: guide
---

# Evaluating New Models with SGLang

This document provides commands for evaluating models' accuracy and performance. Before open-sourcing new models, we strongly suggest running these commands to verify whether the score matches your internal benchmark results.

**For cross verification, please submit commands for installation, server launching, and benchmark running with all the scores and hardware requirements when open-sourcing your models.**

[Reference: MiniMax M2](https://github.com/sgl-project/sglang/pull/12129)

## Accuracy

### LLMs

SGLang provides built-in scripts to evaluate common benchmarks.

**MMLU**

```bash
python -m sglang.test.run_eval \
  --eval-name mmlu \
  --port 30000 \
  --num-examples 1000 \
  --max-tokens 8192
```

**GSM8K**

```bash
python -m sglang.test.few_shot_gsm8k \
  --host http://127.0.0.1 \
  --port 30000 \
  --num-questions 200 \
  --num-shots 5
```

**HellaSwag**

```bash
python benchmark/hellaswag/bench_sglang.py \
  --host http://127.0.0.1 \
  --port 30000 \
  --num-questions 200 \
  --num-shots 20
```

**GPQA**

```bash
python -m sglang.test.run_eval \
  --eval-name gpqa \
  --port 30000 \
  --num-examples 198 \
  --max-tokens 120000 \
  --repeat 8
```

```{tip}
For reasoning models, add `--thinking-mode <mode>` (e.g., `qwen3`, `deepseek-r1`, `deepseek-v3`). You may skip it if the model has forced thinking enabled.
```

**HumanEval**

```bash
pip install human_eval

python -m sglang.test.run_eval \
  --eval-name humaneval \
  --num-examples 10 \
  --port 30000
```

### VLMs

**MMMU**

```bash
python benchmark/mmmu/bench_sglang.py \
  --port 30000 \
  --concurrency 64
```

```{tip}
You can set max tokens by passing `--extra-request-body '{"max_tokens": 4096}'`.
```

For models capable of processing video, we recommend extending the evaluation to include `VideoMME`, `MVBench`, and other relevant benchmarks.

## Performance

Performance benchmarks measure **Latency** (Time To First Token - TTFT) and **Throughput** (tokens/second).

### LLMs

**Latency-Sensitive Benchmark**

This simulates a scenario with low concurrency (e.g., single user) to measure latency.

```bash
python -m sglang.bench_serving \
  --backend sglang \
  --host 0.0.0.0 \
  --port 30000 \
  --dataset-name random \
  --num-prompts 10 \
  --max-concurrency 1
```

**Throughput-Sensitive Benchmark**

This simulates a high-traffic scenario to measure maximum system throughput.

```bash
python -m sglang.bench_serving \
  --backend sglang \
  --host 0.0.0.0 \
  --port 30000 \
  --dataset-name random \
  --num-prompts 1000 \
  --max-concurrency 100
```

**Single Batch Performance**

You can also benchmark the performance of processing a single batch offline.

```bash
python -m sglang.bench_one_batch_server \
  --model <model-path> \
  --batch-size 8 \
  --input-len 1024 \
  --output-len 1024
```

You can run more granular benchmarks:

- **Low Concurrency**: `--num-prompts 10 --max-concurrency 1`
- **Medium Concurrency**: `--num-prompts 80 --max-concurrency 16`
- **High Concurrency**: `--num-prompts 500 --max-concurrency 100`

## Reporting Results

For each evaluation, please report:

1.  **Metric Score**: Accuracy % (LLMs and VLMs); Latency (ms) and Throughput (tok/s) (LLMs only).
2.  **Environment settings**: GPU type/count, SGLang commit hash.
3.  **Launch configuration**: Model path, TP size, and any special flags.
4.  **Evaluation parameters**: Number of shots, examples, max tokens.