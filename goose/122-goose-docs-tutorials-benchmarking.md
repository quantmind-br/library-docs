---
title: Benchmarking with goose | goose
url: https://block.github.io/goose/docs/tutorials/benchmarking
source: github_pages
fetched_at: 2026-01-22T22:16:08.454844647-03:00
rendered_js: true
word_count: 114
summary: This document provides instructions on using the goose benchmarking system to evaluate performance through the goose bench command and JSON configurations. It details how to set up models, manage environment inclusions, and utilize tool shimming for non-tool-capable models.
tags:
    - goose-bench
    - benchmarking
    - performance-evaluation
    - configuration-management
    - tool-shimming
    - system-evaluation
category: guide
---

The goose benchmarking system allows you to evaluate goose performance on complex tasks with one or more system configurations.  
This guide covers how to use the `goose bench` command to run benchmarks and analyze results.

The benchmark configuration is specified in a JSON file with the following structure:

```
{
"models":[
{
"provider":"databricks",
"name":"goose",
"parallel_safe":true,
"tool_shim":{
"use_tool_shim":false,
"tool_shim_model":null
}
}
],
"evals":[
{
"selector":"core",
"post_process_cmd":null,
"parallel_safe":true
}
],
"include_dirs":[],
"repeat":2,
"run_id":null,
"eval_result_filename":"eval-results.json",
"run_summary_filename":"run-results-summary.json",
"env_file":null
}
```

The `include_dirs` config parameter makes the items at all paths listed within the option, available to all evaluations.  
It accomplishes this by:

The benchmark generates two main output files within a file-hierarchy similar to the following.  
Results from running ach model/provider pair are stored within their own directory:

Tool shimming allows you to use a non-tool-capable models with goose, provided Ollama is installed on the system.