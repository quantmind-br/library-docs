---
title: Benchmarks Don't Matter — Until They Do (Part 2)
url: https://forgecode.dev/blog/gpt-5-4-agent-improvements/
source: sitemap
fetched_at: 2026-03-29T14:48:16.231411924-03:00
rendered_js: false
word_count: 1250
summary: This document explains how ForgeCode improved their agent runtime to achieve 81.8% on TermBench 2.0 by addressing model-specific failure modes and implementing schema optimizations, field ordering changes, and verification enforcement.
tags:
    - agent-runtime
    - model-failure-modes
    - schema-optimization
    - benchmarking
    - verification-enforcement
    - field-ordering
    - truncation-handling
category: guide
---

ForgeCode went from 78.4% to **81.8% on TermBench 2.0**. With two different models. At the same time.

If you read [Part 1](https://forgecode.dev/blog/benchmarks-dont-matter/), you know the backstory: we fixed seven failure modes in the agent runtime and climbed from 25% to 78.4% with `gemini-3.1-pro-preview`. That post was about the first layer — non-interactive mode, tool-call naming, planning enforcement, skill routing, reasoning-budget control.

This post is about the second layer. The fixes are smaller, weirder, and in some ways more interesting.

**We now hold the #1 and #2 positions on the [Terminal Bench 2.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0) — both at 81.8%, one with GPT 5.4 and one with Opus 4.6.**

The two models do not behave the same way. They fail differently. The reason they land on the same score is that we learned how to stop triggering each model's specific failure modes.

That distinction matters more than the number.

## The failures that remained[​](#the-failures-that-remained "Direct link to The failures that remained")

After the Part 1 fixes, the easy wins were gone. What remained was narrower and more mechanical:

- tool-call argument mistakes — small typos in JSON shape that caused hard failures
- nested schema confusion — the model mixing up which `required` belonged to which object
- truncation blindness — the model acting as if it had read an entire file when it had only seen the first 2000 lines
- premature completion — the model stopping after implementation without checking whether the task was actually done

None of these show up on a model capabilities chart. All of them show up in your pass rate.

This one sounds absurd. It is not.

We think about schemas in semantic terms: good names, clear descriptions, correct types. GPT 5.4 forced us to care about something dumber: **where fields appear in the JSON.**

In our [internal evals](https://github.com/antinomyhq/forge/tree/main/benchmarks/evals), tool-call error rates dropped when we moved `required` before `properties` in the schema. Same meaning. Different position. Fewer broken calls.

Here is the concrete change. A simplified `todo_write` tool:

**Before** — `required` after `properties`:

**After** — `required` before `properties`:

The semantics are identical. The reliability is not.

When GPT 5.4 emits arguments under pressure — deep in a long trajectory, juggling multiple tool calls — it anchors on what it sees first. Putting `required` early tells the model which fields matter before it starts generating the `properties` block. That reduced malformed calls enough that we adopted it as a schema-wide default.

**The lesson: field ordering is a reliability variable, not a cosmetic choice.** It sounds silly until you run enough evals. Then it stops sounding silly very quickly.

Nesting creates confusion. Not conceptual confusion — structural confusion.

GPT 5.4 understood nested tools at a high level. But when it came time to emit the exact JSON, nesting gave it more ways to get the shape slightly wrong. The common failure: mixing up which `required` array belonged to which object.

A nested schema like this:

Two `required` arrays. Two object layers. More surface area for mistakes.

The flat version:

One `required` array. One object layer. Fewer broken calls.

**If a schema can be flat, make it flat.** You lose some semantic grouping. You gain reliability. That trade is worth it every time.

This one exposed a real behavioral difference between models.

ForgeCode truncates large files for context management — typically returning the first 2000 lines. Opus 4.6 handled this gracefully. We included `total_lines` in the tool result metadata, and Opus inferred the rest: more content exists, adjust the next read accordingly.

GPT 5.4 missed that inference more often. It would proceed as if it had seen the whole file.

The fix was embarrassingly simple. Instead of relying on metadata alone:

We added a plain-text reminder directly in the result body:

That was enough. GPT 5.4 stopped behaving as if it had seen everything.

**Opus reads between the lines. GPT reads the lines.** Neither is wrong — but if your runtime assumes models will infer context from metadata, you are assuming Opus-like behavior. Not every model does that. Make the important information loud enough that no model can miss it.

This was the biggest single improvement.

The problem: GPT 5.4 would implement a solution, sound confident, and stop. The code changed. A command ran. The trace looked fine. But the task was not actually complete — edge cases missed, files not saved, tests not run.

Partial completions that look convincing are worse than obvious failures. At least obvious failures get retried.

We built a verification skill. It takes the original task and asks a different question: **what evidence would prove this objective is actually complete?**

The model switches from builder mode to reviewer mode. It generates a checklist:

- what was requested
- what was actually done
- what evidence exists that it worked
- what is still missing

The critical part: **we enforced it programmatically.** If the model had not called the verification skill before finishing, the runtime injected a reminder and required the pass. No opt-out.

The result: instead of stopping after the first plausible solution, GPT 5.4 caught its own gaps, generated follow-up tasks, and completed them before exiting.

Normal prompting — "please verify your work" — did not produce this effect. Enforcement did.

This is the part worth paying attention to if you build agents.

Opus 4.6 tolerated messier schemas. It inferred truncation from metadata. It naturally did one more verification pass without being forced. It was, in a word, more forgiving.

GPT 5.4 reached the same benchmark result, but it needed:

- cleaner field ordering
- flatter schemas
- explicit truncation reminders
- enforced reviewer-mode verification

That is not a capability gap. It is a behavioral difference. The models fail in different places, and the agent has to compensate in different ways.

**Drop both models into the same harness and Opus looks easier to work with. Adapt the harness to GPT 5.4's actual failure modes and the gap disappears.**

That is the real takeaway.

The easy narrative is "model X beat model Y."

The more accurate narrative: "runtime version N learned how to stop triggering model X's failure modes."

GPT 5.4 was already a strong model before we changed anything. What changed is that we found where it was brittle inside an agent loop and removed those sources of brittleness one at a time.

This is also why the most useful eval work is not headline benchmarking. It is the boring internal eval that tells you:

- which schema shape produces fewer call errors for this specific model
- which tool output wording changes follow-up behavior
- which skills need enforcement versus suggestion
- which failure patterns deserve runtime correction instead of more prompt text

Those details are where benchmark gains actually come from.

A few months ago, Anthropic was the default choice for serious agent work. GPT needed more babysitting.

That is no longer true.

After these changes, GPT 5.4 matches Opus 4.6 at **81.8% on TermBench 2.0**. It got there with some additional runtime tuning. That is not a weakness, that is how agent engineering works.

Models are not evaluated in a vacuum. They are evaluated inside tools, schemas, repair loops, truncation policies, and verification systems. Once you accept that, the model comparison discourse starts making a lot more sense.

The next layer of work is less glamorous and probably more valuable:

- per-tool reliability tracking by model
- schema-shape evals before new tools ship
- verification-skill precision, when to enforce, when to skip
- trajectory-level analysis of when a model should keep going versus stop
- provider-specific runtime defaults where failure modes clearly differ

Not better models. Better harnesses for the models we already have.

That is the frontier now.