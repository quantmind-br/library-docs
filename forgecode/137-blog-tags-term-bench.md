---
title: ForgeCode
url: https://forgecode.dev/blog/tags/term-bench/
source: sitemap
fetched_at: 2026-03-29T14:50:59.8206478-03:00
rendered_js: false
word_count: 51
summary: This document explains how ForgeCode achieved 78.4% SOTA on TermBench 2.0, detailing seven failure modes, their fixes, and how the benchmark work generalized across models rather than overfitting to one run.
tags:
    - benchmarking
    - performance-optimization
    - machine-learning
    - model-evaluation
    - technical-implementation
category: reference
---

March 3, 2026

Benchmarks Don't Matter — Until They Do (Part 1)ForgeCode hit 78.4% SOTA on TermBench 2.0 with gemini-3.1-pro-preview. This is the technical account of how we got there: seven failure modes, their fixes, and why the benchmark work generalized across models rather than overfitting to one run.

![Tushar](https://avatars.githubusercontent.com/u/194482?v=4)

Tushar