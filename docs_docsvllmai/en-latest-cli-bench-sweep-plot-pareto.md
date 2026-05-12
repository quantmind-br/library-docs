---
title: vllm bench sweep plot_pareto - vLLM
url: https://docs.vllm.ai/en/latest/cli/bench/sweep/plot_pareto/
source: sitemap
fetched_at: 2026-05-07T21:11:04.029643199-03:00
rendered_js: false
word_count: 107
summary: This document describes the command-line interface arguments for a benchmarking tool, including how to structure JSON input and configure specific parameters like user count and GPU variables.
tags:
    - cli-arguments
    - benchmarking
    - json-parsing
    - configuration-reference
    - vllm
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/cli/bench/sweep/plot_pareto.md "Edit this page")

## JSON CLI Arguments[¶](#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

- `--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`
- `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

- `--json-arg '{"key4": ["value3", "value4", "value5"]}'`
- `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments[¶](#arguments "Permanent link")

#### `--user-count-var`[¶](#-user-count-var "Permanent link")

Result key that stores concurrent user count. Falls back to max\_concurrent\_requests if missing.

Default: `max_concurrency`

#### `--gpu-count-var`[¶](#-gpu-count-var "Permanent link")

Result key that stores GPU count. If not provided, falls back to num\_gpus/gpu\_count or tensor\_parallel\_size * pipeline\_parallel\_size.

#### `--label-by`[¶](#-label-by "Permanent link")

Comma-separated list of fields to annotate on Pareto frontier points.

Default: `max_concurrency,gpu_count`

#### `--dry-run`[¶](#-dry-run "Permanent link")

If set, prints the figures to plot without drawing them.

Default: `False`