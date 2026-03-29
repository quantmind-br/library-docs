---
title: ForgeCode
url: https://forgecode.dev/docs/agent-delegation/
source: sitemap
fetched_at: 2026-03-29T16:30:32.093775-03:00
rendered_js: false
word_count: 207
summary: This document explains how to implement agent delegation, allowing orchestrator agents to utilize specialist agents as tools to perform specific tasks.
tags:
    - agent-delegation
    - orchestrator-agents
    - specialist-agents
    - workflow-automation
    - agent-configuration
category: concept
---

Agent delegation enables agents to use other agents as tools, creating specialized workflows where orchestrator agents delegate tasks to specialist agents.

### How It Works[​](#how-it-works "Direct link to How It Works")

1. **Agent Discovery**: The system automatically discovers agents from your agent files
2. **Tool Conversion**: Each agent becomes a callable tool with its ID as the tool name
3. **Execution**: The system routes agent tool calls to the appropriate specialist

### Required Configuration[​](#required-configuration "Direct link to Required Configuration")

For an agent to be used as a tool, it needs:

**Critical Requirements:**

- `id`: Unique identifier that becomes the tool name
- `description`: A comprehensive description of the tool's purpose, capabilities, and use cases. This is crucial as the agent relies on it to decide when to invoke the tool - better descriptions lead to more accurate tool selection.

### Agent Tool Usage[​](#agent-tool-usage "Direct link to Agent Tool Usage")

When calling another agent as a tool, use this format:

### Code Review Orchestrator[​](#code-review-orchestrator "Direct link to Code Review Orchestrator")

Create an orchestrator agent that delegates to specialist agents:

**1. Security Specialist** (`~/.forge/agents/security-specialist.md`):

**2. Code Review Orchestrator** (`./.forge/agents/code-review-orchestrator.md`):

The system loads agents from three sources with precedence:

1. **CWD Agents**: `./.forge/agents/*.md` (highest priority)
2. **Global Agents**: `~/.forge/agents/*.md` (Unix/macOS) or `%USERPROFILE%\.forge\agents\*.md` (Windows)
3. **Built-in Agents**: Embedded in application (lowest priority)

CWD agents override global agents with the same ID.

- [Creating Custom Agents](https://forgecode.dev/docs/agent-definition-guide/) - Basic agent configuration and creation
- [Agent Configuration](https://forgecode.dev/docs/agent-configuration/) - Detailed configuration options and troubleshooting