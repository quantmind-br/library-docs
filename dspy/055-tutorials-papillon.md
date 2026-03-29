---
title: Privacy-Conscious Delegation - DSPy
url: https://dspy.ai/tutorials/papillon/
source: sitemap
fetched_at: 2026-01-23T08:04:16.175344108-03:00
rendered_js: false
word_count: 79
summary: This document introduces an advanced tutorial on building multi-stage DSPy modules that integrate local language models, external tools, and custom evaluation judges for model optimization.
tags:
    - dspy
    - papillon
    - local-lm
    - multi-stage-modules
    - evaluation-metrics
    - optimization
    - teacher-student-model
category: tutorial
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/tutorials/papillon/index.md "Edit this page")

Please refer to [this tutorial from the PAPILLON authors](https://colab.research.google.com/github/Columbia-NLP-Lab/PAPILLON/blob/main/papillon_tutorial.ipynb) using DSPy.

This tutorial demonstrates a few aspects of using DSPy in a more advanced context:

1. It builds a multi-stage `dspy.Module` that involves a small local LM using an external tool.
2. It builds a multi-stage *judge* in DSPy, and uses it as a metric for evaluation.
3. It uses this judge for optimizing the `dspy.Module`, using a large model as a teacher for a small local LM.