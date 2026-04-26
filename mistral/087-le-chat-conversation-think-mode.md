---
title: Think mode | Mistral Docs
url: https://docs.mistral.ai/le-chat/conversation/think-mode
source: sitemap
fetched_at: 2026-04-26T04:07:45.599441048-03:00
rendered_js: false
word_count: 358
summary: This document explains how to utilize the Think mode in Le Chat, which leverages chain-of-thought prompting to solve complex, multi-step problems through explicit reasoning.
tags:
    - ai-reasoning
    - le-chat
    - chain-of-thought
    - problem-solving
    - user-guide
    - logic-processing
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Think mode lets Le Chat **reason through complex problems**.

Powered by [Magistral models](https://mistral.ai/news/magistral/), it breaks your question into smaller steps, works through each one, and gives you a clear answer along with the **full reasoning path**.

This approach is known as *chain-of-thought* prompting — the model reasons explicitly before answering. For the research behind it, see the [original paper](https://arxiv.org/abs/2201.11903).

## How to Use

1. Select the `Think` mode at the right of the chat window (`Fast` is the default).
2. Enter your prompt and send it as usual.
3. Le Chat begins reasoning and displays its thought process in real time.
4. Once complete, Le Chat provides the final answer.

Think mode stays active until you switch to another mode. You can toggle it at any point in an existing chat.

## When to Use Think Mode

Think mode is ideal for tasks requiring **multi-step logic** or **structured analysis**:

- **Planning and strategy**: break down a product launch, prioritize a roadmap, evaluate hiring plans
- **Debugging production issues**: trace through error chains, compare possible root causes, narrow down fixes
- **Multi-factor decisions**: weigh options with competing constraints (vendor selection, architecture trade-offs)
- **Math and quantitative reasoning**: work through financial models, statistical calculations, proofs
- **Complex code review**: reason about logic flows, edge cases, potential regressions across a codebase

For simple factual lookups, quick text generation, or straightforward tasks, standard chat is faster and equally accurate.

## Tips

- **Be specific in your prompt** — more context gives better reasoning. Instead of *"What pricing model should we use?"*, try *"Compare freemium vs. usage-based pricing for a B2B SaaS product, considering churn and expansion revenue."*
- **Use the reasoning as documentation** — the chain-of-thought output makes a useful artifact for team discussions. Copy it into [Canvas](https://docs.mistral.ai/le-chat/content-creation/canvas) or share the conversation.
- **Combine with other tools** — Think mode works alongside [web search](https://docs.mistral.ai/le-chat/research-analysis/web-search), [file uploads](https://docs.mistral.ai/le-chat/research-analysis/files-upload), and [Libraries](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries) for reasoning based on your own data.

## Related Features

- [**Deep Research**](https://docs.mistral.ai/le-chat/research-analysis/deep-research): for questions that need multi-source web research and a structured report
- [**Canvas**](https://docs.mistral.ai/le-chat/content-creation/canvas): refine and iterate on outputs in an editor
- [**Code Interpreter**](https://docs.mistral.ai/le-chat/content-creation/code-interpreter): run code and validate quantitative reasoning

#ai-reasoning #chain-of-thought #problem-solving