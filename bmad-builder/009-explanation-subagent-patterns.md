---
title: Subagent Orchestration Patterns
url: https://bmad-builder-docs.bmad-method.org/explanation/subagent-patterns/
source: sitemap
fetched_at: 2026-04-08T11:33:06.489339549-03:00
rendered_js: false
word_count: 1197
summary: This document details advanced patterns for orchestrating LLM work using isolated 'subagents' that communicate via a shared filesystem blackboard, emphasizing techniques to prevent the parent context from bloating and maintain efficiency.
tags:
    - llm-orchestration
    - subagent-patterns
    - filesystem-blackboard
    - context-management
    - ai-architecture
category: guide
---

Subagents are isolated LLM instances that a parent skill spawns to handle specific tasks. Each gets its own context window, receives instructions, and returns results. Used well, they keep the parent context small while enabling parallel work at scale.

All patterns share one principle: **the filesystem is the single source of truth**. Parent context stays tiny (file pointers + high-level plan). Subagents are stateless black boxes: instructions in, response out, isolated context.

## Foundation: The Filesystem Blackboard

[Section titled “Foundation: The Filesystem Blackboard”](#foundation-the-filesystem-blackboard)

Every pattern below builds on this infrastructure. The filesystem acts as a shared database so the parent never bloats its context.

```plaintext

/output/
├── status.json        ← task states, completion flags
├── knowledge.md       ← accumulated findings (append-only)
└── task-queue.json    ← pending work items
/tasks/{id}/
├── input.md           ← instructions for this subagent
└── output/
├── result.json    ← structured output (strict schema)
└── summary.md     ← compact summary (≤200 tokens)
/artifacts/            ← final deliverables
```

One technique is to have every subagent prompt ends the same way: *“You are stateless. Read ONLY the files listed. Write ONLY result.json + summary.md. Do not echo data back.”*

## Pattern 1: Delegated Data Access

[Section titled “Pattern 1: Delegated Data Access”](#pattern-1-delegated-data-access)

The simplest pattern. Subagents read sources and return only distilled summaries. The parent never touches raw data.

AspectDetail**How it works**Parent spawns readers in parallel; each reads a source and returns a compact summary; parent synthesizes from summaries only**Critical rule**Parent must delegate *before* touching any source material. If it reads first, the tokens are already spent**When to use**5+ documents, web research, large codebase exploration**Not worth it for**1-2 files where the overhead exceeds the savings**Token savings**~99%. Five docs at 15K tokens each = 75K raw vs ~350 tokens in summaries

## Pattern 2: Temp File Assembly

[Section titled “Pattern 2: Temp File Assembly”](#pattern-2-temp-file-assembly)

For large-scale operations with potentially a lot of relevant data across multiple sources. Subagents write results to temp files. A separate assembler subagent combines them into a cohesive deliverable.

AspectDetail**How it works**Parent spawns N worker subagents writing to `tmp/{n}.md`; after all complete, spawns an assembler subagent that reads all temp files and creates the final artifact**When to use**When summaries are still too large to return inline, or when assembly needs a dedicated agent with fresh context**Example**The BMad quality optimizer uses this: 5 parallel scanner subagents write temp JSON, then a report-creator subagent synthesizes them

Multiple subagents communicate through shared files, building on each other’s work. The parent controls turn order.

AspectDetail**How it works**Agent A writes to `shared.md`; Agent B reads it and adds; Agent A can be resumed to continue; the shared file grows incrementally**Variants**Shared file (multiple agents read/write a common file) or session resumption (reawaken a previous subagent to continue with its full context)**When to use**Pipeline stages where later work depends on earlier work, but each agent’s context stays small

## Pattern 4: Hierarchical Lead-Worker

[Section titled “Pattern 4: Hierarchical Lead-Worker”](#pattern-4-hierarchical-lead-worker)

A lead subagent analyzes the task once and writes a breakdown. The parent spawns workers from that plan. Mid-level sub-orchestrators can handle complex subtasks.

AspectDetail**How it works**Lead agent writes `plan.json` with task breakdown; parent reads plan and spawns workers in parallel; complex subtasks get their own sub-orchestrator**When to use**Tasks that need analysis before decomposition, or where the parent cannot predict the work structure upfront**Variant**Master-clone: spawn near-identical agents with slight persona tweaks exploring different branches of the same problem

## Pattern 5: Persona-Driven Parallel Reasoning

[Section titled “Pattern 5: Persona-Driven Parallel Reasoning”](#pattern-5-persona-driven-parallel-reasoning)

The most powerful pattern for quality. Spawn diverse specialists in parallel, producing genuinely independent thinking from isolated contexts.

AspectDetail**How it works**Parent spawns 3-6 agents with distinct personas (Architect, Red Teamer, Pragmatist, Innovator); each writes findings independently; an evaluator subagent scores and merges the best elements**When to use**Design decisions, code review, strategy, any task where diverse perspectives improve quality**Key**Heavy persona injection gives genuinely different outputs, not just paraphrases of the same analysis

**Useful diversity packs:**

PersonaPerspective**Architect**Scale and elegance above all**Red Teamer**Break this. What fails?**Pragmatist**Ship it Friday. What is the minimum?**Innovator**What if we approached this entirely differently?**User Advocate**How does the end user actually experience this?**Future-Self**With 5 years of hindsight, what would you change?

**Sub-patterns:**

Sub-PatternHow It Works**Multi-Path Exploration**Same task, different personas. Each writes to `/explorations/path_N/`. Parent prunes or merges best paths**Debate & Critique**Round 1: parallel proposals. Round 2: critics attack proposals. Round 3: refinement**Ensemble Voting**Same subtask K times with persona variations. Evaluator scores. Weighted merge of winners

## Pattern 6: Evolutionary & Emergent Systems

[Section titled “Pattern 6: Evolutionary & Emergent Systems”](#pattern-6-evolutionary--emergent-systems)

These turn stateless subagents into something that feels alive. All build on the filesystem blackboard.

VariantHow It WorksBest For**Evolutionary Optimization**Spawn 8-20 agents as a “generation”; evaluator scores; “breeder” creates next-gen instructions from winners; run 5-10 generationsOptimizing algorithms, UI designs, strategies**Stakeholder Simulation**Agents are characters (customer, competitor, regulator) acting on shared “world state” files in turnsProduct strategy, risk analysis**Swarm Intelligence**Dozens of lightweight agents explore solution space, depositing “pheromone” scores; later agents bias toward high-scoring pathsBroad coverage with minimal planning**Recursive Meta-Improvement**”Evolver” agents analyze past logs and propose improved system prompts, new roles, or better orchestration heuristicsSystem self-improvement across sessions

## The Most Common Mistake: Parent Reads First

[Section titled “The Most Common Mistake: Parent Reads First”](#the-most-common-mistake-parent-reads-first)

The single most important thing to get right with subagent patterns is **preventing the parent from reading the data it is delegating**. If the parent reads all the files before spawning subagents, the entire pattern is defeated. You have already spent the tokens, bloated the context, and lost the isolation benefit.

This happens often. You write a skill that should spawn subagents to each read a document and return findings. You run it. The parent agent helpfully reads every document first, then passes them to subagents, then collects distilled summaries. The subagents still provide fresh perspectives, but the context savings (the primary reason for the pattern) are gone.

**The fix is defensive language in your skill.** Explicitly tell the parent agent what it should and should not do. Be specific without being verbose.

**Practical tips for getting this right:**

TipExample Language**Tell the parent what to discover, not read**”List all files in `resources/` by name to determine how many subagents to spawn. Do not read their contents”**Tell subagents what to return**”Return only findings relevant to \[topic]. Output as JSON to `{output-path}`. Do not echo raw content”**Use pre-pass scripts**Run a lightweight script that extracts metadata (file names, sizes, structure) so the parent can plan without reading**Be explicit about the boundary**”Your role is ORCHESTRATION. Scripts and subagents do all analysis”

**Test and watch what actually happens.** If the parent reads files it should be delegating, tighten the language. This is normal iteration. The builders are tuned with these patterns, but different models and tools may need more explicit guidance. Review the BMad quality optimizer prompts (`prompts/quality-optimizer.md`) and scanner agents (`agents/quality-scan-*.md`) for working examples of this defensive language.

## Choosing a Pattern

[Section titled “Choosing a Pattern”](#choosing-a-pattern)

NeedPatternRead multiple sources without bloating context1: Delegated Data AccessCombine many outputs into one deliverable2: Temp File AssemblyPipeline where stages depend on each other3: Shared-File OrchestrationTask needs analysis before work can be decomposed4: Hierarchical Lead-WorkerQuality through diverse perspectives5: Persona-Driven Parallel ReasoningIterative optimization or simulation6: Evolutionary & Emergent

## Implementation Notes

[Section titled “Implementation Notes”](#implementation-notes)

- Force **strict JSON schemas** on every subagent output for reliable parent parsing
- Use **git worktrees** or per-agent directories to prevent crosstalk
- Start small: one orchestrator that reads `plan.md` and spawns the first wave
- Patterns compose: use Delegated Access for data gathering, Persona-Driven for analysis, Temp File Assembly for the final report
- Always include **graceful degradation**. If subagents are unavailable, the main agent performs the work sequentially