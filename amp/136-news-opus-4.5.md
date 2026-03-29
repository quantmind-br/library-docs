---
title: 'Opus 4.5: Better, Faster, Often Cheaper'
url: https://ampcode.com/news/opus-4.5
source: crawler
fetched_at: 2026-02-06T02:08:21.824285974-03:00
rendered_js: false
word_count: 409
summary: This document announces and explains the transition of Amp's 'smart' mode to the Claude Opus 4.5 model, providing a comparative analysis of its performance, reliability, and cost-efficiency against other models like Gemini 3 and Sonnet 4.5.
tags:
    - claude-opus
    - model-benchmarks
    - ai-integration
    - cost-efficiency
    - llm-comparison
    - smart-mode
category: other
---

Claude Opus 4.5 is the new main model in Amp's `smart` mode, two days after we shipped [it](https://ampcode.com/news/try-opus) for you to try out.

Only a week ago, we changed Amp's main model to Gemini 3 — [a historic change](https://ampcode.com/news/gemini-3), we said. It was the first time since Amp's creation that we switched away from Claude. Now we're switching again and you may ask: why? Why follow a historic change with another one, in a historically short amount of time?

We love Gemini 3, but, once rolled out, its impressive highs came with lows. What we internally experienced as [rough](https://ampcode.com/news/gemini-3#not-perfect) [edges](https://x.com/sqs/status/1991563112290607422) turned into some very frustrating behaviors for our users. Frustrating and costly.

Then, not even a week later, Opus 4.5 comes out. Opus 4.5, on the other hand, seems as capable as Gemini 3. Its highs might not be as brilliant as Gemini 3's, but it also seems to do away with the lows. It seems more polished. It's faster, even.

We're also pleasantly surprised by Opus's cost-efficiency. Yes, Opus tokens are more expensive, but it needs fewer tokens to do the job, makes fewer token-wasting mistakes, and needs less human intervention (which results in a higher cache hit rate, which means lower costs and latency).

Sonnet 4.5 Gemini 3 Pro Opus 4.5 **Internal Evals** 37.1% 53.7% 57.3% **Avg. Thread Cost** $2.75 $2.04 $2.05    0-200k Tokens Only[1]() $1.48 $1.19 $2.05 **Off-the-Rails Cost**[2]() 8.4% 17.8% 2.4% **Speed (p50, preliminary)** 2.4 min 4.3 min 3.5 min

In words:

- *If you use long threads (200k+ tokens):* Opus will be a lot cheaper. It’s currently limited to 200k tokens of context, which forces you to use [small threads](https://ampcode.com/guides/context-management)—our strong recommendation anyway, for both quality and cost. If you need long context, use [`large` mode](https://ampcode.com/news/large-mode).
- *If Sonnet or Gemini frequently struggles for you or has hit a capability ceiling:* Opus will be far more capable and accurate, and often cheaper too (by avoiding wasted tokens).
- *If you loved Gemini 3 Pro:* Opus will be ~40% more expensive but faster and more tolerant of ambiguous prompts. (This describes most of the Amp team, and we still find Opus worth it.)
- *If you were perfectly satisfied with Sonnet 4.5:* Opus will be ~35% more expensive for the same task. The real win comes from getting outside your comfort zone and giving it harder tasks where Sonnet would struggle.

Staying on the frontier means sometimes shipping despite [issues](https://x.com/sqs/status/1991563112290607422) — and sometimes shipping something better a week later.