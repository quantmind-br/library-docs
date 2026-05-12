---
title: Prompting
url: https://developers.openai.com/codex/prompting.md
source: llms
fetched_at: 2026-04-30T10:15:58.536312955-03:00
rendered_js: false
word_count: 419
summary: This document explains the core concepts of interacting with Codex, including how to structure effective prompts, manage interaction threads, and provide relevant context for tasks.
tags:
    - codex
    - prompt-engineering
    - workflow-management
    - ai-agents
    - context-management
category: concept
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Prompting

## Prompts

Interact with Codex by sending prompts describing what you want it to do.

Examples:
```text
Explain how the transform module works and how other modules use it.
```
```text
Add a new command-line option `--json` that outputs JSON.
```

Codex works in a loop: calls the model, performs actions indicated by model output (file reads, edits, tool calls), repeating until the task is complete or you cancel it.

Tips for effective prompting:
- Codex produces higher-quality outputs when it can verify its work. Include steps to reproduce an issue, validate a feature, and run linting and pre-commit checks.
- Break complex work into smaller, focused steps. Smaller tasks are easier to test and review. If unsure how to split, ask Codex to propose a plan.

For more ideas, see [[039-workflows|workflows]].

## Threads

A thread = single session: your prompt + model outputs and tool calls that follow. Can include multiple prompts (e.g., first prompt implements a feature, follow-up adds tests).

A thread is "running" when Codex is actively working on it. You can run multiple threads at once, but avoid having two threads modify the same files. Resume a thread later by continuing with another prompt.

| Thread type | Behavior |
|-------------|----------|
| **Local** | Runs on your machine. Reads/edits files and runs commands. Uses a [[044-concepts-sandboxing|sandbox]] to reduce risk of unwanted changes outside workspace. |
| **Cloud** | Runs in an isolated [[052-cloud-environments|environment]]. Clones your repo and checks out the branch. Useful for parallel work or delegating from another device. Push code to GitHub first. You can also [[024-ide-features#cloud-delegation|delegate from your local machine]], which includes current working state. |

In the Codex app, you can also start a **chat** without choosing a project — not tied to a saved repository or project folder. Use for research, planning, connected-tool workflows, or other work where Codex shouldn't start from a codebase. Chats use a Codex-managed `threads` directory under your Codex home (default `~/.codex/threads`). Change the base location by setting `CODEX_HOME`. See [Config and state locations](https://developers.openai.com/codex/config-advanced#config-and-state-locations).

## Context

Include references to relevant files and images when submitting prompts. The Codex IDE extension automatically includes open files and selected text range as context.

As the agent works, it gathers context from file contents, tool output, and an ongoing record of what it has done and still needs to do.

All information must fit within the model's **context window**, which varies by model. Codex monitors and reports remaining space. For longer tasks, it may automatically **compact** context by summarizing relevant information and discarding less relevant details. With repeated compaction, Codex can continue working on complex tasks over many steps.

#prompting #threads #context #codex