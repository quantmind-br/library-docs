---
title: "Model Selection Guide for ForgeCode"
url: https://forgecode.dev/docs/model-selection-guide/
source: sitemap
fetched_at: 2026-04-30T14:09:12.688182615-03:00
rendered_js: false
word_count: 188
summary: "Switch between AI models in ForgeCode based on task requirements: speed for edits, reasoning for complex problems."
tags:
  - model-switching
  - forgecode
  - ai-development
  - model-selection
  - workflow-optimization
  - productivity
category: guide
optimized: true
---
# Model Selection Guide for ForgeCode

> **TL;DR**
> Switch models with `:model`. Use fast models for edits, reasoning models for complex tasks.

## How to Switch Models

1. Open selector: `:model`
2. Browse/search models (across all providers)
3. Select with keyboard (↑/↓ + Enter)

> **Tip**: Log in to new providers with `:provider-login`.

## Model Trade-offs

| Type | Use Case | Examples |
|------|---------|----------|
| **Fast** | Routine edits, quick fixes | Sonnet, Grok-4, Gpt-4.1 |
| **Reasoning** | Complex problems, architecture | Opus 4, O3, Deepseek-r1-0528 |

### Fast Models
- **Pros**: Sub-second response, cost-effective
- **Best for**: Refactoring, formatting, simple tasks

### Reasoning Models
- **Pros**: Deep understanding, nuanced accuracy
- **Best for**: Architecture, large codebases, critical logic

## Key Features
- **Context preserved**: Switch models without losing conversation history.
- **Experiment freely**: Instant, no-cost switching.
- **Preferences saved**: ForgeCode remembers your last model.

## Recommendations
- Start with a fast model for routine work.
- Switch to reasoning models for complex tasks.
- Try different models to find your best fit.

## Related Guides
- [Custom Rules Guide](https://forgecode.dev/docs/custom-rules-guide/)
- [Plan and Act Guide](https://forgecode.dev/docs/plan-and-act-guide/)