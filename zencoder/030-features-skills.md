---
title: Skills - Zencoder Docs
url: https://docs.zencoder.ai/features/skills
source: crawler
fetched_at: 2026-01-23T09:28:12.60946391-03:00
rendered_js: false
word_count: 195
summary: This document explains how to use and create Skills in Zencoder to provide agents with specialized procedural knowledge, scripts, and organizational context.
tags:
    - agent-skills
    - zencoder
    - automation-workflows
    - procedural-knowledge
    - workspace-configuration
category: guide
---

Skills are folders of instructions, scripts, and resources that agents can discover and use to perform tasks more accurately and efficiently. They provide procedural knowledge and context that agents can load on demand.

## Why Skills?

Agents are increasingly capable, but often lack the context needed to do real work reliably. Skills solve this by giving agents access to:

- **Domain expertise**: Specialized knowledge packaged into reusable instructions
- **New capabilities**: Extended functionality like creating presentations, building MCP servers, or analyzing datasets
- **Repeatable workflows**: Consistent, auditable multi-step task execution
- **Organizational knowledge**: Team and company-specific context in portable, version-controlled packages

## How Skills Work in Zencoder

Zencoder automatically discovers and loads skills from these locations:

LocationScope`<workspace>/.zencoder/skills/`Project-specific skills`<user-home>/.zencoder/skills/`User-level skills`<workspace>/.claude/skills/`Claude-compatible skills

The agent decides which skill to use based on the skill’s description and the current task context. Skills are available in both **Zenflow** and **Zencoder IDE plugins**.

## Skill Structure

A skill is a folder containing a `SKILL.md` file with metadata and instructions:

```
.zencoder/skills/
└── my-skill/
    ├── SKILL.md          # Required: skill definition
    ├── scripts/          # Optional: automation scripts
    └── resources/        # Optional: templates, examples
```

## Creating a Skill

Create a `SKILL.md` file in your skills folder:

```
---
name: Code Review Assistant
description: Helps perform thorough code reviews following team standards
---

# Code Review Assistant

## Instructions
When reviewing code, follow these steps:
1. Check for security vulnerabilities
2. Verify error handling patterns
3. Ensure test coverage requirements are met
...
```

## Learn More

Skills follow an open standard developed by Anthropic and adopted by leading AI development tools. For the complete specification and examples, see the [Agent Skills documentation](https://agentskills.io).