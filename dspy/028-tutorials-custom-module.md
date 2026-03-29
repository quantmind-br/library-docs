---
title: Building AI Applications by Customizing DSPy Modules - DSPy
url: https://dspy.ai/tutorials/custom_module/
source: sitemap
fetched_at: 2026-01-23T08:03:47.832200024-03:00
rendered_js: false
word_count: 132
summary: This document explains the rationale for customizing modules in DSPy, focusing on the transition from string-based prompting to structured AI programming using custom python logic.
tags:
    - dspy
    - module-customization
    - ai-programming
    - forward-method
    - llm-framework
category: concept
---

## Why Customizing Module?[¶](#why-customizing-module)

DSPy is a lightweight authoring and optimization framework, and our focus is to resolve the mess of prompt engineering by transforming prompting (string in, string out) LLM into programming LLM (structured inputs in, structured outputs out) for robust AI system.

While we provide pre-built modules which have custom prompting logic like `dspy.ChainOfThought` for reasoning, `dspy.ReAct` for tool calling agent to facilitate building your AI applications, we don't aim at standardizing how you build agents.

In DSPy, your application logic simply goes to the `forward` method of your custom Module, which doesn't have any constraint as long as you are writing python code. With this layout, DSPy is easy to migrate to from other frameworks or vanilla SDK usage, and easy to migrate off because essentially it's just python code.