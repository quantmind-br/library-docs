---
title: Overview - DSPy
url: https://dspy.ai/tutorials/gepa_ai_program/
source: sitemap
fetched_at: 2026-01-23T08:03:55.087997591-03:00
rendered_js: false
word_count: 296
summary: This document introduces GEPA, a reflective prompt optimizer for DSPy that leverages model reflections and textual feedback to evolve prompt candidates. It provides a directory of tutorials demonstrating GEPA's application in areas such as mathematical reasoning, information extraction, and code safety.
tags:
    - dspy
    - gepa
    - prompt-optimization
    - reflective-evolution
    - llm-feedback
    - prompt-engineering
category: tutorial
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/tutorials/gepa_ai_program/index.md "Edit this page")

## Reflective Prompt Evolution with GEPA[¶](#reflective-prompt-evolution-with-gepa "Permanent link")

This section introduces GEPA, a reflective prompt optimizer for DSPy. GEPA works by leveraging LM's ability to reflect on the DSPy program's trajectory, identifying what went well, what didn't, and what can be improved. Based on this reflection, GEPA proposes new prompts, building a tree of evolved prompt candidates, accumulating improvements as the optimization progresses. Since GEPA can leverage domain-specific text feedback (as opposed to only the scalar metric), GEPA can often propose high performing prompts in very few rollouts. GEPA was introduced in the paper [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) and available as `dspy.GEPA` which internally uses the GEPA implementation provided in [gepa-ai/gepa](https://github.com/gepa-ai/gepa).

## `dspy.GEPA` Tutorials[¶](#dspygepa-tutorials "Permanent link")

### [GEPA for AIME (Math)](https://dspy.ai/tutorials/gepa_aime/)[¶](#gepa-for-aime-math "Permanent link")

This tutorial explores how GEPA can optimize a single `dspy.ChainOfThought` based program to achieve 10% gains on AIME 2025 with GPT-4.1 Mini!

This tutorial explores how GEPA leverages predictor-level feedback to improve GPT-4.1 Nano's performance on a three-part task for structured information extraction and classification in an enterprise setting.

### [GEPA for Privacy-Conscious Delegation](https://dspy.ai/tutorials/gepa_papillon/)[¶](#gepa-for-privacy-conscious-delegation "Permanent link")

This tutorial explores how GEPA can improve rapidly in as few as 1 iteration, while leveraging a simple feedback provided by a LLM-as-a-judge metric. The tutorial also explores how GEPA benefits from the textual feedback showing a breakdown of aggregate metrics into sub-components, allowing the reflection LM to identify what aspects of the task need improvement.

### [GEPA for Code Backdoor Classification (AI control)](https://dspy.ai/tutorials/gepa_trusted_monitor/)[¶](#gepa-for-code-backdoor-classification-ai-control "Permanent link")

This tutorial explores how GEPA can optimize a GPT-4.1 Nano classifier to identify backdoors in code written by a larger LM, using `dspy.GEPA` and a comparative metric! The comparative metric allows the prompt optimizer to create a prompt that identifies the signals in the code that are indicative of a backdoor, teasing apart positive samples from negative samples.