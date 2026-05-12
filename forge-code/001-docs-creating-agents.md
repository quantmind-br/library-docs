---
title: "Creating Custom Agents in ForgeCode"
url: https://forgecode.dev/docs/creating-agents/
source: sitemap
fetched_at: 2026-04-30T14:09:04.332547064-03:00
rendered_js: false
word_count: 309
summary: "Learn how to define, configure, and manage custom AI agents in ForgeCode using YAML frontmatter and system prompts."
tags:
  - custom-agents
  - forgecode
  - yaml-configuration
  - system-prompt
  - agent-orchestration
  - mcp-integration
category: guide
optimized: true
---
# Creating Custom Agents in ForgeCode

> **TL;DR**
> A custom agent is a `.md` file with YAML frontmatter. Define its `id`, tools, model, and system prompt, then restart ForgeCode.

## Agent Definition Basics

### File Structure
- **Frontmatter**: Controls tools, model, and sampling behavior.
- **System Prompt**: Defines the agent's role and response style.

### Locations
| Location | Scope | Use Case |
|----------|-------|----------|
| `~/forge/agents/` | Global | Reusable across all projects |
| `.forge/agents/` | Project | Specific to a single codebase |

> **Priority**: Project agents override global agents with the same `id`.

## Creating Your First Agent

1. **Create the directory** (if it doesn't exist):
   ```bash
   mkdir -p ~/.forge/agents/  # Global
   mkdir -p .forge/agents/    # Project
   ```

2. **Define the agent** (example: `security-auditor.md`):
   ```yaml
   ---
   id: security-auditor
   tools: [read, search]
   model: gpt-4
   temperature: 0.1
   ---
   
   You are a security auditor. Analyze code for vulnerabilities, misconfigurations, and compliance risks. Be thorough and precise.
   ```

3. **Restart ForgeCode** and run `:agent` to see your new agent.

## Key Frontmatter Fields

| Field | Purpose | Example |
|-------|---------|---------|
| `id` | Unique identifier | `security-auditor` |
| `tools` | Tools the agent can use | `[read, search, shell]` |
| `model` | LLM model | `gpt-4` |
| `temperature` | Creativity level | `0.1` (low for code) |
| `description` | Required for tool invocation | `Audits code for security issues` |

> **Tool Access**: Restrict to only what the agent needs. Use `*` sparingly (consumes context).

## Advanced Features

### User Prompt Templates
- Wrap user input with structured context using Handlebars:
  ```yaml
  user_prompt: |
    Timestamp: {{current_date}}
    Event: {{event.name}}
    Input: {{event.value}}
  ```

### Overriding Built-in Agents
- Replace `forge`, `muse`, or `sage` by matching their `id` in `.forge/agents/`.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent not in `:agent` list | Check `.md` extension, valid YAML, unique `id`, and restart ForgeCode |
| YAML parse errors | Quote special characters or use `|` for multiline strings |
| Agent not callable as a tool | Add a `description` field |

## Related Guides
- [Built-in Agents](https://forgecode.dev/docs/operating-agents/)
- [SKILL.md](https://forgecode.dev/docs/skills/)
- [MCP Integration](https://forgecode.dev/docs/mcp-integration/)
- [AGENTS.md Guide](https://forgecode.dev/docs/custom-rules-guide/)