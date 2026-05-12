---
title: Subagents
url: https://developers.openai.com/codex/concepts/subagents.md
source: llms
fetched_at: 2026-04-30T10:15:25.860830695-03:00
rendered_js: false
word_count: 565
summary: This document outlines the architectural benefits and implementation strategies for using subagent workflows to delegate parallel tasks and minimize context pollution in Codex. It covers core terminology, best practices for triggering parallel workflows, and guidelines for selecting appropriate models and reasoning efforts.
tags:
    - subagents
    - agent-workflows
    - context-management
    - parallel-processing
    - model-selection
    - reasoning-effort
category: concept
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Subagents

Spawn specialized agents in parallel to explore, tackle, or analyze work concurrently. For setup, agent configuration, and examples, see [[049-subagents|Subagents]].

## Why subagent workflows help

Even with large context windows, models have limits. Flooding the main conversation with noisy intermediate output (exploration notes, test logs, stack traces, command output) degrades reliability over time.

| Problem | Solution |
|---------|----------|
| **Context pollution** | Useful information buried under noisy intermediate output |
| **Context rot** | Performance degrades as conversation fills with less relevant details |

Subagent workflows move noisy work off the main thread:
- **Main agent** stays focused on requirements, decisions, final outputs
- **Subagents** run in parallel for exploration, tests, log analysis
- **Summaries** return from subagents instead of raw intermediate output

They also save time when work can run independently in parallel, and make larger tasks more tractable by breaking them into bounded pieces (e.g., splitting multi-million-token document analysis into smaller problems).

As a starting point, use parallel agents for **read-heavy** tasks: exploration, tests, triage, summarization. Be more careful with **write-heavy** workflows — agents editing code simultaneously can create conflicts and increase coordination overhead.

## Core terms

| Term | Definition |
|------|------------|
| **Subagent workflow** | Workflow where Codex runs parallel agents and combines results |
| **Subagent** | Delegated agent started to handle a specific task |
| **Agent thread** | CLI thread for an agent; inspect and switch between with `/agent` |

## Triggering subagent workflows

Codex doesn't spawn subagents automatically — only when you explicitly ask for subagents or parallel agent work.

Manual triggering: direct instructions such as "spawn two agents," "delegate this work in parallel," or "use one agent per point." Subagent workflows consume more tokens than single-agent runs because each subagent does its own model and tool work.

A good subagent prompt explains how to divide work, whether Codex should wait for all agents before continuing, and what summary or output to return.

Example:
```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.
```

## Choosing models and reasoning

Codex can choose a setup balancing intelligence, speed, and price when you don't pin `model` or `model_reasoning_effort`. It may favor `gpt-5.4-mini` for fast scans or higher-effort `gpt-5.5` for demanding reasoning.

For most tasks, start with `gpt-5.5` when available. Continue using `gpt-5.4` during rollout if `gpt-5.5` isn't yet available. Use `gpt-5.4-mini` for faster, lower-cost lighter subagent work. ChatGPT Pro subscribers can use `gpt-5.3-codex-spark` for near-instant text-only iteration (research preview).

### Model choice

| Model | Use case |
|-------|----------|
| **gpt-5.5** | Demanding agents — ambiguous, multi-step work needing planning, tool use, validation, follow-through across larger context |
| **gpt-5.4** | When gpt-5.5 unavailable, or workflow pinned to GPT-5.4. Strong coding, reasoning, tool use, broader workflows |
| **gpt-5.4-mini** | Speed and efficiency over depth — exploration, read-heavy scans, large-file review, processing supporting documents. Good for parallel workers returning distilled results |
| **gpt-5.3-codex-spark** | Near-instant, text-only iteration when latency matters more than broader capability (ChatGPT Pro, research preview) |

### Reasoning effort (`model_reasoning_effort`)

| Level | Use case |
|-------|----------|
| **high** | Trace complex logic, check assumptions, work through edge cases (reviewer, security-focused agents) |
| **medium** | Balanced default for most agents |
| **low** | Straightforward tasks where speed matters most |

Higher reasoning effort increases response time and token usage but can improve quality for complex work.

See [[070-models|Models]], [[055-config-basic|Config basics]], and [[067-config-reference|Configuration Reference]] for details.

#subagents #parallel-processing #context-management #model-selection #codex