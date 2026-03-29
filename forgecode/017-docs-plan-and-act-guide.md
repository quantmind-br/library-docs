---
title: ForgeCode
url: https://forgecode.dev/docs/plan-and-act-guide/
source: sitemap
fetched_at: 2026-03-29T14:52:11.743629286-03:00
rendered_js: false
word_count: 431
summary: This document explains how to use the Muse and ForgeCode AI agents together in a planning-first workflow for safer and more effective AI-assisted development.
tags:
    - ai-coding-tools
    - development-workflow
    - muse-agent
    - forgecode-agent
    - planning-first
    - code-implementation
category: guide
---

One of the biggest mistakes developers make with AI coding tools is jumping straight into implementation. After analyzing thousands of successful AI-assisted development sessions, we've learned that the most productive workflow follows a simple pattern: **Plan first, then act**.

ForgeCode makes this workflow smooth with two specialized agents designed to work together.

### Muse Agent: Your Strategic Planner[​](#muse-agent-your-strategic-planner "Direct link to Muse Agent: Your Strategic Planner")

Muse operates in **read-only mode**, making it perfect for analysis and planning without touching your code:

- Analyzes your codebase and identifies potential issues
- Creates detailed implementation plans
- Explores different solution approaches
- Reviews code for security, performance, and architecture concerns

**When to use Muse:**

- Before making significant changes to critical systems
- When you need to understand the scope and impact of a task
- For architecture planning.
- When working in unfamiliar codebases

### ForgeCode Agent: Your Implementation Partner[​](#forgecode-agent-your-implementation-partner "Direct link to ForgeCode Agent: Your Implementation Partner")

ForgeCode has **full read-write access** and handles the actual implementation:

- Modifies files and creates new code
- Executes commands and runs tests
- Implements the solutions from your plan
- Provides real-time feedback as changes are made

**When to use ForgeCode:**

- After reviewing and approving a plan from Muse
- For routine tasks you're confident about
- When you want hands-off implementation
- For quick fixes with proper version control

Here's how successful developers use both agents together:

### 1. Start with Muse for Planning[​](#1-start-with-muse-for-planning "Direct link to 1. Start with Muse for Planning")

Switch to Muse from your ZSH shell:

Ask Muse to create a detailed plan:

### 2. Review and Refine the Plan[​](#2-review-and-refine-the-plan "Direct link to 2. Review and Refine the Plan")

Muse will provide a structured plan and then critique it for gaps. Review this carefully - a good plan eliminates most of implementation confusion later.

### 3. Switch to ForgeCode for Implementation[​](#3-switch-to-forgecode-for-implementation "Direct link to 3. Switch to ForgeCode for Implementation")

Switch back to ForgeCode:

Reference the plan and start implementation:

### 4. Iterate as Needed[​](#4-iterate-as-needed "Direct link to 4. Iterate as Needed")

Switch back to Muse if you encounter complex decisions, then return to ForgeCode for continued implementation.

**Planning prevents confusion:** When AI understands the full scope upfront, it makes better implementation decisions and avoids getting lost halfway through.

**Separation of concerns:** Muse focuses purely on analysis without the pressure to implement, leading to better strategic thinking.

**Safety first:** Critical systems get proper review before any changes are made.

**Faster iteration:** Once you have a solid plan, ForgeCode can implement quickly without constant back-and-forth.

- **Be specific in your planning requests** - include edge cases, error handling, and integration points
- **Commit frequently** - clean git state makes it easier to track AI changes
- **Review everything** - treat AI output like a junior developer's code
- **Avoid frequent agent switching** - it causes context thrashing, hurts cache performance, and creates confusing context handoffs

Remember: You're the architect, `Muse` is your strategic advisor, and `Forge` is your implementation partner. Use each for what they do best.