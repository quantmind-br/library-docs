---
title: utility - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/utility/
source: sitemap
fetched_at: 2026-05-07T21:16:42.100671907-03:00
rendered_js: false
word_count: 25
summary: This document lists and briefly describes optimization modules used for graph transformation and node replacement in a computational framework.
tags:
    - graph-optimization
    - node-replacement
    - code-transformation
    - compiler-passes
    - module-definitions
category: reference
---

Modules:

Name Description `fix_functionalization` `noop_elimination` `post_cleanup` `scatter_split_replace`

Replace `slice_scatter` and `split_with_sizes` nodes with a single

`split_coalescing`

Coalesce duplicate `split_with_sizes` nodes that operate on the same