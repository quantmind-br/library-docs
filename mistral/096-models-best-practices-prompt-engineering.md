---
title: Prompting | Mistral Docs
url: https://docs.mistral.ai/models/best-practices/prompt-engineering
source: sitemap
fetched_at: 2026-04-26T04:08:40.825986099-03:00
rendered_js: false
word_count: 1100
summary: This document provides a comprehensive guide on engineering effective prompts for LLMs, covering structural best practices, role definition, formatting techniques, and strategies to improve response consistency and reliability.
tags:
    - prompt-engineering
    - llm-optimization
    - structured-output
    - system-prompts
    - few-shot-prompting
    - best-practices
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Effective prompting is essential for generating high-quality responses from Mistral models.

## System vs User Prompts

- **`system` prompt**: Sets general context and instructions at conversation start (managed by developer)
- **`user` prompt**: Provides specific context for the current interaction

If you cannot control the `system` prompt, concatenate context and instructions in the `user` prompt.

## Role-Separated Prompting

Define a clear purpose: *"You are a `<role>`, your task is to `<task>`."* This steers the model toward a specific vertical and task.

## Prompt Structure

- **Organize hierarchically** with clear sections and subsections
- **Be complete** — write for someone with no prior context
- **Use Markdown and/or XML tags**: readable, parsable, and familiar to models

## Few-Shot Prompting

Provide task examples to improve model accuracy and output format. In contrast, **zero-shot prompting** uses no examples.

**Standard structure:**
```
System: <role and task>
User: <example input>
Assistant: <example output>
User: <actual query>
Assistant:
```

## Structured Outputs

Enforce a specific JSON output format for consistent, programmatically parseable responses. See [[131-studio-api-document-processing-basic-ocr|Structured Outputs]].

## What to Avoid

- **Blurry quantitative adjectives**: "too long", "too short", "many", "few"
  - Use objective measures instead
- **Blurry words**: "things", "stuff", "interesting", "better"
  - State exactly what you mean
- **Contradictions** in long system prompts:
  - Bad: "If record is too long, split it" (no threshold)
  - Good: "If record > 100 chars, split it"
- **Asking for unnecessary content** in structured outputs:
  - Bad: Generating full record content for `NO_OP` operation
  - Generate only what is strictly necessary

## Rating Scales

Use worded scales for better performance:
- **Bad**: "Rate 1-5"
- **Good**: "Rate as: needs improvement / acceptable / good / excellent"

Convert to numeric afterward if needed.

## Example Capabilities

Mistral models excel at **classification**, **summarization**, **personalization**, and **evaluation**.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/prompting/prompting_capabilities.ipynb)

### Classification

Provide predetermined categories in the prompt. Two strategies:
1. **Direct label**: Single word/string response (fastest, cheapest)
2. **JSON output**: Structured object for downstream processing (more flexible)

### Summarization, Personalization, Evaluation

Apply role-separated prompting, structured format, and few-shot examples as appropriate.

> [!tip]
> Iterate on prompts like you iterate on code. Different models or updates can change behavior — revisit and re-evaluate. #prompt-engineering #llm-optimization #structured-output #few-shot-prompting