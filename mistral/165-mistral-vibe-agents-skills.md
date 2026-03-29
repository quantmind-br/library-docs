---
title: Agents & Skills | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/agents-skills
source: crawler
fetched_at: 2026-01-29T07:33:14.371306743-03:00
rendered_js: false
word_count: 462
summary: A comprehensive guide on creating and managing AI agents and their associated skills within the Mistral AI ecosystem.
tags:
    - Mistral AI
    - Agents
    - Skills
    - Documentation
category: guide
---

Build custom Agents for your specific use cases and leverage Skills to extend their capabilities.

Agents are the core actors in Vibe. They are autonomous entities capable of performing tasks, making decisions, and interacting with the environment. Agents can be customized for specific use cases and extended with Skills to enhance their capabilities.

Vibe also has [AGENTS.md](https://agents.md/) support. This feature is currently only functional when an AGENTS.md file is in the root of the workspace.

Agents can be selected using the `--agent` flag when starting vibe:

Or with `Shift+Tab` in the Interactive mode.

We provide a set of **built-in** agents you can leverage out of the box:

- Agents:
  
  - `default`: Requires approval for tool executions.
  - `plan`: Read-only agent for exploration and planning (auto-approve).
  - `accept-edits`: Auto-approves file edits only.
  - `auto-approve`: Auto-approves all tool executions.
- Subagents:
  
  - `explore`: Read-only subagent for codebase exploration.

Create custom agent profiles in `~/.vibe/agents/` by creating a `.toml` file, learn more about Vibe configuration [here](https://docs.mistral.ai/mistral-vibe/introduction/configuration):

The `safety` field changes the user input border color to indicate the agent's safety level and currently has 4 choices. Their only purpose is to visually inform the user of the safety level of the agent, but **does not implement safety measures**.  
We recommend using this field together with appropriate tool permissions, such as Agents capable of editing/deleting files being classified as `destructive`, or Agents restricted to read-only tool calls being classified as `safe`.

Vibe supports subagents for delegating tasks. Subagents run independently and can perform specialized work without user interaction.  
The `task` tool allows you to delegate work to subagents:

- The agent uses the `task` tool to delegate work to a subagent.
- Subagents run independently and return results as text to the agent.

Subagents are useful for:

- **Parallel work**: Run exploration or research tasks in the background
- **Specialized tasks**: Use different agent profiles for specific work
- **Safety**: Subagents run in-memory without saving session logs

Custom subagents can be created in `~/.vibe/agents/`:

Subagents possess a few limitations:

- Subagents cannot ask questions.
- Results are returned as text only.

Agents can ask questions interactively using the `ask_user_question` tool:

- Supports multiple-choice or free-text input.
- Displays questions as tabs for multi-question scenarios.
- Automatically used when the agent needs clarification or validation.

Vibe's skills system allows you to extend functionality through reusable components. Skills can add new tools, slash commands, and specialized behaviors.

Vibe follows the [Agent Skills specification](https://agentskills.io/specification) for skill format and structure.

Skills are defined in directories with a `SKILL.md` file containing metadata in YAML frontmatter. For example, `~/.vibe/skills/code-review/SKILL.md`:

Vibe discovers skills from multiple locations:

1. **Global skills directory**: `~/.vibe/skills/`
2. **Local project skills**: `.vibe/skills/` in your project
3. **Custom paths**: Configured in `config.toml`

Enable or disable skills using patterns in your configuration:

Skills support the same pattern matching as tools (exact names, glob patterns, and regex when using the `re:` prefix).