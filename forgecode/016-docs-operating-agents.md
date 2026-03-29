---
title: ForgeCode
url: https://forgecode.dev/docs/operating-agents/
source: sitemap
fetched_at: 2026-03-29T14:52:08.304449675-03:00
rendered_js: false
word_count: 508
summary: This document explains how to select and use different AI agents in ForgeCode, detailing their capabilities and appropriate use cases for development workflows.
tags:
    - agent-selection
    - ai-development
    - workflow
    - code-assistance
    - development-tools
category: guide
---

ForgeCode provides three specialized agents, each designed for different stages of development work. They differ in capabilities and access levels, allowing you to choose the right approach for your task.

AgentAccessPurposeBest For`muse`read + writePlanning & analysisReviewing impact, planning changes, critical systems`forge`read + writeImplementationMaking changes, fixing bugs, creating features`sage`readResearch & investigationUnderstanding codebases, tracing bugs, analyzing architecture

**Typical workflow**: Use **`muse`** to plan → Switch to **`forge`** to implement

Both agents can use **`sage`** internally to research and understand your codebase when needed.

From the [Agent Selection Guide](https://forgecode.dev/docs/agent-selection-guide/), here are the key points to remember:

### How to switch quickly[​](#how-to-switch-quickly "Direct link to How to switch quickly")

1. Type `:agent` in your ForgeCode session
2. Browse the available agents list
3. Use ↑/↓ to choose an agent
4. Press Enter to confirm

### Why selection matters[​](#why-selection-matters "Direct link to Why selection matters")

Models control raw intelligence, while agents control behavior and execution style. Picking the right agent gives you help that matches your current stage of work.

### When to switch[​](#when-to-switch "Direct link to When to switch")

- Use **`sage`** for deep research and system understanding
- Use **`muse`** for planning and change analysis
- Use **`forge`** for direct implementation and code changes
- Use **custom agents** for team- or domain-specific workflows

### Pro tips[​](#pro-tips "Direct link to Pro tips")

- Your conversation and project context are preserved when switching agents
- Combine `:agent` with `:model` to tune both behavior and intelligence

* * *

`muse` analyzes your codebase and creates detailed implementation plans. It proposes solutions and explains the impact of changes without executing them.

**Switch to `muse`** : `/muse`

**Ideal for:**

- Planning complex refactoring
- Understanding scope before implementation
- Working with critical or production code
- Learning how to implement specific features
- Changes requiring team review

**Example prompts:**

- "How would you redesign this API for better scalability?"
- "Create a plan to add user authentication"
- "What's needed to implement pagination?"

* * *

`forge` implements solutions directly. It modifies files, creates code, and executes commands to complete tasks immediately.

**Switch to `forge`** : `/forge` (active by default)

**Ideal for:**

- Quick fixes and routine tasks
- Refactoring with immediate results
- Implementing approved plans
- Tasks where you want hands-off execution
- Creating new features

**Example prompts:**

- "Fix the null pointer exception in UserService"
- "Create a React component for the user profile"
- "Add unit tests for the payment processor"

* * *

`sage` is not a user-facing agent, but it's an internal tool that both **`muse`** and **`forge`** can use automatically to research and understand your codebase. When either agent needs to investigate code, trace functionality, or analyze architecture, it leverages `sage` behind the scenes.

You don't need to manually switch to `sage`; it works transparently when the agents need deeper codebase insights.

* * *

You can switch between agents at any time during your session:

- Use `:muse` to switch to `muse` Agent
- Use `:forge` to switch to `forge` Agent
- Use `:agent` to see all available agents and choose from a dropdown

**Common patterns:**

- Use **`muse`** before making significant changes to critical systems
- Switch to **`forge`** when you're ready to implement
- Both agents will automatically use **`sage`** for research when needed

**Best practice**: Use version control and commit your work before using `forge` for significant changes.

* * *

- [Plan and Act Guide: Strategic AI Development Workflow with ForgeCode](https://forgecode.dev/docs/plan-and-act-guide/)
- [AI Model Selection Guide: Optimize ForgeCode for Your Workflow](https://forgecode.dev/docs/model-selection-guide/)