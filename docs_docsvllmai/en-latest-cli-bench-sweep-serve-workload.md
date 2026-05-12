---
title: vllm bench sweep serve_workload - vLLM
url: https://docs.vllm.ai/en/latest/cli/bench/sweep/serve_workload/
source: sitemap
fetched_at: 2026-05-07T21:11:05.65304429-03:00
rendered_js: false
word_count: 338
summary: This document describes the command-line interface arguments and configuration options for the vLLM benchmark sweep tool, which automates serving and performance testing workloads.
tags:
    - vllm
    - benchmarking
    - cli-arguments
    - workload-testing
    - performance-evaluation
    - automation
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/cli/bench/sweep/serve_workload.md "Edit this page")

## JSON CLI Arguments[¶](#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

- `--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`
- `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

- `--json-arg '{"key4": ["value3", "value4", "value5"]}'`
- `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments[¶](#arguments "Permanent link")

#### `--serve-cmd`[¶](#-serve-cmd "Permanent link")

The command used to run the server: `vllm serve ...`

#### `--bench-cmd`[¶](#-bench-cmd "Permanent link")

The command used to run the benchmark: `vllm bench serve ...`

#### `--after-bench-cmd`[¶](#-after-bench-cmd "Permanent link")

After a benchmark run is complete, invoke this command instead of the default `ServerWrapper.clear_cache()`.

#### `--show-stdout`[¶](#-show-stdout "Permanent link")

If set, logs the standard output of subcommands. Useful for debugging but can be quite spammy.

Default: `False`

#### `--server-ready-timeout`[¶](#-server-ready-timeout "Permanent link")

Timeout in seconds to wait for the server to become ready.

Default: `300`

#### `--serve-params`[¶](#-serve-params "Permanent link")

Path to JSON file containing parameter combinations for the `vllm serve` command. Can be either a list of dicts or a dict where keys are benchmark names. If both `serve_params` and `bench_params` are given, this script will iterate over their Cartesian product.

#### `--link-vars`[¶](#-link-vars "Permanent link")

Comma-separated list of linked variables between serve and bench, e.g. max\_num\_seqs=max\_concurrency,max\_model\_len=random\_input\_len

Default: `""`

#### `--bench-params`[¶](#-bench-params "Permanent link")

Path to JSON file containing parameter combinations for the `vllm bench serve` command. Can be either a list of dicts or a dict where keys are benchmark names. If both `serve_params` and `bench_params` are given, this script will iterate over their Cartesian product.

#### `-o`, `--output-dir`[¶](#-o-output-dir "Permanent link")

The main directory to which results are written.

Default: `results`

#### `-e`, `--experiment-name`[¶](#-e-experiment-name "Permanent link")

The name of this experiment (defaults to current timestamp). Results will be stored under `output_dir/experiment_name`.

#### `--num-runs`[¶](#-num-runs "Permanent link")

Number of runs per parameter combination.

Default: `3`

#### `--dry-run`[¶](#-dry-run "Permanent link")

If set, prints the commands to run, then exits without executing them.

Default: `False`

#### `--resume`[¶](#-resume "Permanent link")

Resume a previous execution of this script, i.e., only run parameter combinations for which there are still no output files under `output_dir/experiment_name`.

Default: `False`

### workload options[¶](#workload-options "Permanent link")

#### `--workload-var`[¶](#-workload-var "Permanent link")

Possible choices: `request_rate`, `max_concurrency`

The variable to adjust in each iteration.

Default: `request_rate`

#### `--workload-iters`[¶](#-workload-iters "Permanent link")

Number of workload levels to explore. This includes the first two iterations used to interpolate the value of `workload_var` for remaining iterations.

Default: `10`