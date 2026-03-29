---
title: ForgeCode
url: https://forgecode.dev/docs/model-selection-guide/
source: sitemap
fetched_at: 2026-03-29T14:52:04.135480614-03:00
rendered_js: false
word_count: 322
summary: This document explains how to switch between AI models in ForgeCode, including the model selection process, trade-offs between different model types, and best practices for choosing the right model for development tasks.
tags:
    - model-switching
    - ai-development
    - code-editing
    - model-selection
    - forgecode
    - development-workflow
category: guide
---

Switching models is quick and intuitive:

1. **Open the model selector** by typing `:model` in your ForgeCode session
2. **Browse available models** using the dropdown that appears (across all logged-in providers)
3. **Search by name** - just start typing the model name to filter
4. **Navigate with keyboard** - use up/down arrow keys to select
5. **Press Enter** to confirm your selection

To log in to a new provider, use `:provider-login` or `:login`.

The interface shows you model capabilities and pricing so you can make informed decisions.

The model you choose dramatically impacts your development experience. Different models excel at different tasks - some are fast for simple edits, others provide deep reasoning for complex problems. ForgeCode makes switching between models effortless, so you can always use the right tool for the job.

### Speed vs. Reasoning Trade-offs[​](#speed-vs-reasoning-trade-offs "Direct link to Speed vs. Reasoning Trade-offs")

**Fast Models (Sonnet, Grok-4, Gpt-4.1):**

- Excellent for routine code edits and simple tasks
- Sub-second response times
- Perfect for refactoring, formatting, and quick fixes
- Cost-effective for high-volume usage

**Reasoning Models (Opus 4, O3, Deepseek-r1-0528):**

- Superior for complex problem-solving and architecture decisions
- Better understanding of large codebases
- More accurate with nuanced requirements
- Worth the extra time for critical implementations

**Model Memory:** Conversation context is preserved when switching models so you can continue where you left off.

**Experiment Freely:** Model switching is instant and free - try different models to see what works best for your style.

**Save Preferences:** ForgeCode remembers your last model choice for quick access and next time it will start with the last used model.

Remember: The best model is the one that gets your job done efficiently. Start with what feels right, and don't hesitate to switch when you need different capabilities. ForgeCode makes it effortless to find the perfect AI partner for every task.

* * *

### Getting Help[​](#getting-help "Direct link to Getting Help")

If you're experiencing issues with ForgeCode:

- [Agent Selection Guide: Choose the Right Agent for Your Task](https://forgecode.dev/docs/agent-selection-guide/)
- [Custom Rules Guide: Extending ForgeCode's Capabilities](https://forgecode.dev/docs/custom-rules-guide/)
- [Plan and Act Guide: Automating Complex Workflows with ForgeCode](https://forgecode.dev/docs/plan-and-act-guide/)