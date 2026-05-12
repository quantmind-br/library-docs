---
title: post_cleanup - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/utility/post_cleanup/
source: sitemap
fetched_at: 2026-05-07T21:16:44.84108945-03:00
rendered_js: false
word_count: 45
summary: This document describes the PostCleanupPass class, which performs post-processing on a graph by ensuring topological order and removing redundant nodes.
tags:
    - graph-optimization
    - vllm-compiler
    - node-pruning
    - topological-sort
    - fx-graph
    - code-cleanup
category: reference
---

Bases: `VllmInductorPass`

This pass performs cleanup after custom passes. It topologically sorts the graph and removes unused nodes. This is needed because the pattern matcher does not guarantee producing a topologically sorted graph, and there may be unused nodes left around.

Source code in `vllm/compilation/passes/utility/post_cleanup.py`

```
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21

classPostCleanupPass(VllmInductorPass):
"""
    This pass performs cleanup after custom passes.
    It topologically sorts the graph and removes unused nodes.
    This is needed because the pattern matcher does not guarantee producing
    a topologically sorted graph, and there may be unused nodes left around.
    """

    @VllmInductorPass.time_and_log
    def__call__(self, graph: fx.Graph) -> None:
        fromtorch._inductor.pattern_matcherimport stable_topological_sort

        stable_topological_sort(graph)
        graph.eliminate_dead_code()
```