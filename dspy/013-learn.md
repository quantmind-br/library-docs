---
title: Learning DSPy - DSPy
url: https://dspy.ai/learn/
source: sitemap
fetched_at: 2026-01-23T08:03:12.746214689-03:00
rendered_js: false
word_count: 167
summary: This document outlines the iterative three-stage process for building AI systems with DSPy, covering programming, evaluation, and optimization.
tags:
    - dspy
    - ai-development
    - pipeline-design
    - evaluation-metrics
    - prompt-optimization
    - workflow
category: concept
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/learn/index.md "Edit this page")

## Learning DSPy: An Overview[¶](#learning-dspy-an-overview "Permanent link")

DSPy exposes a very small API that you can learn quickly. However, building a new AI system is a more open-ended journey of iterative development, in which you compose the tools and design patterns of DSPy to optimize for *your* objectives. The three stages of building AI systems in DSPy are:

1\) **DSPy Programming.** This is about defining your task, its constraints, exploring a few examples, and using that to inform your initial pipeline design.

2\) **DSPy Evaluation.** Once your system starts working, this is the stage where you collect an initial development set, define your DSPy metric, and use these to iterate on your system more systematically.

3\) **DSPy Optimization.** Once you have a way to evaluate your system, you use DSPy optimizers to tune the prompts or weights in your program.

We suggest learning and applying DSPy in this order. For example, it's unproductive to launch optimization runs using a poorly designed program or a bad metric.