---
title: Benchmark Suites - vLLM
url: https://docs.vllm.ai/en/latest/benchmarking/
source: sitemap
fetched_at: 2026-05-07T21:10:54.553864497-03:00
rendered_js: false
word_count: 52
summary: This document provides an overview of the benchmarking tools available in vLLM, including command-line utilities, automated parameter sweeping, and performance monitoring dashboards.
tags:
    - vllm
    - benchmarking
    - performance-testing
    - cli-tools
    - optimization
    - model-evaluation
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/benchmarking/README.md "Edit this page")

vLLM provides comprehensive benchmarking tools for performance testing and evaluation:

- [**Benchmark CLI**](https://docs.vllm.ai/en/latest/benchmarking/cli/): `vllm bench` CLI tools and specialized benchmark scripts for interactive performance testing.
- [**Parameter Sweeps**](https://docs.vllm.ai/en/latest/benchmarking/sweeps/): Automate `vllm bench` runs for multiple configurations, useful for [optimization and tuning](https://docs.vllm.ai/en/latest/configuration/optimization/).
- [**Performance Dashboard**](https://docs.vllm.ai/en/latest/benchmarking/dashboard/): Automated CI that publishes benchmarks on each commit.