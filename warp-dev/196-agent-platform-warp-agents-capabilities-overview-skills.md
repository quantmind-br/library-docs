---
title: Skills | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/skills
source: sitemap
fetched_at: 2026-04-29T15:03:48.852992922-03:00
rendered_js: false
word_count: 1205
summary: This document explains how to create and manage reusable agent skills using markdown files, detailing their discovery, invocation methods, and support for parameterized arguments.
tags:
    - ai-agents
    - workflow-automation
    - markdown-configuration
    - developer-tools
    - task-automation
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Skills create reusable, shareable instructions that agents invoke when performing tasks. Encapsulate common workflows, coding patterns, or domain expertise into skill files that agents automatically discover and use.

## Key features

- **Reusable instructions** — define a task once, agents use it when relevant
- **Project and global scopes** — create skills specific to a project or available across all projects
- **Automatic discovery** — agents are aware of all available skills and invoke them when appropriate
- **Simple markdown format** — skills are markdown files with minimal metadata
- **Supporting files** — include scripts, templates, or other resources alongside instructions
- **Slash command invocation** — invoke any skill directly with `/{skill-name}`
- **Parameterized skills** — use argument placeholders for dynamic, reusable templates

## How Skills work

When you start an [Agent conversation](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents), the Agent receives a list of all available skills with their names and descriptions. When the Agent determines a skill would help, it loads the full instructions and follows them to complete the task.

> [!note]
> Skill discovery is based on your current working directory. For Git repositories, Warp includes all skills from your current directory up through the repository root. Skills from other projects are not included.

> [!tip]
> Skills complement Rules, which provide persistent guidelines that Agents always follow. Use Rules for constraints and preferences; use Skills for specific task workflows.

### Skill name conflicts

If you have skills with the same name in multiple directories:

| Invocation method | Behavior |
|---|---|
| **Natural language** | Agent receives all in-scope skills with names, descriptions, and file paths; chooses the appropriate skill |
| **Slash commands** | Warp displays all matching skills in the menu for you to select |
| **Background resolution** | Warp prioritizes home directory (global) skills first, then skills from higher directories |

### Invoking skills

**Using natural language:**
- "Use the deploy skill to push to staging"
- "Check the docs for broken links"
- "Create a DOCX file with my project's README content"

**Using slash commands:**
- `/deploy` — invokes the deploy skill
- `/add-feature-flag` — invokes the add-feature-flag skill

---

## Skill file format

Skills are markdown files with YAML frontmatter. Each skill requires:

- **name** — unique identifier (typically kebab-case)
- **description** — brief explanation of what the skill does and when to use it

```markdown
---
name: deploy
description: Deploy the application to the specified environment
---

# Deploy Skill

Instructions for deploying...
```

---

## Skill arguments

Skills can include argument placeholders that are substituted with values you provide when invoking the skill.

### Argument syntax

| Format | Description |
|--------|-------------|
| `$ARGUMENTS` | Full raw argument string (everything after the skill name) |
| `$ARGUMENTS[N]` | Nth whitespace-separated argument (0-indexed) |
| `$N` | Shorthand for `$ARGUMENTS[N]` |

### How argument substitution works

When you invoke a skill, any text after the skill name is treated as the argument string and split on whitespace.

- If the skill **contains argument placeholders**, they are replaced with corresponding argument values before instructions are sent to the agent.
- If the skill **does not contain placeholders**, your extra text is passed as a separate user message alongside the skill instructions.
- If a placeholder references an undefined argument index (e.g., `$2` when only two arguments were given), the placeholder is left as-is.

### Example: Skill with arguments

```markdown
---
name: explain-topic
description: Explain a technical topic for a specific audience
---

Explain the following topic for a $1 audience:

$ARGUMENTS
```

Invoking with `/explain-topic 5-year-olds quantum computing` produces:

```
Explain the following topic for a 5-year-olds audience:

quantum computing
```

### Example: Skill without arguments

```markdown
---
name: greeting
description: A friendly greeting
---

Say hello in a friendly way.
```

Invoking with `/greeting say it in french` sends skill instructions first, then "say it in french" as a follow-up user message.

---

## Skill locations

Skills can be stored at two levels: project-level (accessible only within that project) and user-level (accessible from any project).

### Project skills

Store in any of these directories in your repository root:

```
.agents/skills/      (recommended)
.warp/skills/
.claude/skills/
.codex/skills/
.cursor/skills/
.gemini/skills/
.copilot/skills/
.factory/skills/
.github/skills/
.opencode/skills/
```

> [!info]
> Warp scans all supported skill directory names, allowing you to maintain skills compatible with multiple AI coding tools in the same repository.

Each skill must be in its own subdirectory with a `SKILL.md` file. Supporting files (scripts, templates, configs) should be referenced using relative paths.

### Root directory skills (global)

Store global skills in your home folder:

```
~/.agents/skills/      (recommended)
~/.warp/skills/
~/.claude/skills/
~/.codex/skills/
~/.cursor/skills/
~/.gemini/skills/
~/.copilot/skills/
~/.factory/skills/
~/.github/skills/
~/.opencode/skills/
```

### Project vs. root directory skills

| Use case | Project skills | Root directory skills |
|----------|---------------|----------------------|
| Project-specific workflows | ✓ | |
| Team-shared procedures | ✓ | |
| Personal coding patterns | | ✓ |
| Cross-project automation | | ✓ |
| Repository-specific tooling | ✓ | |

---

## Creating skills

### Step 1: Choose a location

- **Project-specific** — place in one of your project's skill directories
- **Global** — place in one of your home directory's skill folders

### Step 2: Create the directory structure

```bash
mkdir -p .agents/skills/my-skill/
```

### Step 3: Write the skill file

Create `SKILL.md` in your skill directory.

### Step 4: Add content

Write clear instructions including exact file paths, command syntax, and expected formats.

---

## Skills with supporting files

Place supporting files (scripts, templates, configuration) in the same directory as your `SKILL.md`:

```bash
.agents/skills/deploy/
├── SKILL.md        # Main instructions
├── deploy.sh       # Deployment script
└── config.yaml     # Default configuration
```

Reference supporting files using relative paths in your `SKILL.md`.

**Use cases:**
- **Automation scripts** — Python, shell, or Node scripts for complex tasks
- **Templates** — boilerplate files the Agent can copy and customize
- **Configuration** — default settings or schemas the skill references

---

## Managing skills

### Viewing available skills

Ask the Agent: "What skills are available?" The Agent lists all discovered skills with their names and descriptions.

### Editing skills

Use the [`/open-skill`](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/slash-commands) slash command to open an interactive menu to browse, select, and edit skills.

---

## Best practices

- **Write clear descriptions** — the description is how Agents decide whether to use your skill
- **Be specific in instructions** — include exact file paths, command syntax, and expected formats
- **Include examples** — show concrete use cases to help Agents understand intent
- **Keep skills focused** — each skill should do one thing well
- **Use consistent naming** — follow `verb-noun` convention (e.g., `add-feature-flag`, `run-migrations`)
- **Version control your skills** — commit project skills to your repo so the team benefits

---

## Pre-built skills

Warp maintains a public collection of ready-to-use skills in the [warpdotdev/oz-skills](https://github.com/warpdotdev/oz-skills) repository. Browse for inspiration, copy directly into your project's `.agents/skills/` directory, or adapt to fit your workflows.

These skills also appear as suggested agents in the [Oz web app](https://docs.warp.dev/agent-platform/cloud-agents/oz-web-app) where you can run them directly in the cloud.

---

## Invoking skills with a prompt

Pass additional context when invoking with a slash command:

- `/deploy push the latest changes to staging` — invokes deploy skill with instructions to target staging
- `/code-review focus on error handling and edge cases` — invokes code-review skill with prioritization guidance

---

## Running agents from skills

Skills work with both local and [cloud agents](https://docs.warp.dev/agent-platform/cloud-agents/overview) to create reusable, automated workflows. When running an agent via CLI, web app, or API, specify a skill to provide base instructions.

For a complete guide to running skill-based agents, see [Skills as Agents](https://docs.warp.dev/agent-platform/cloud-agents/skills-as-agents).

---

- [[195-agent-platform-warp-agents-capabilities-overview-computer-use|Computer Use]] — let agents interact with desktop environments
- [[198-agent-platform-warp-agents-capabilities-overview|Capabilities]] — all agent capabilities and configuration options
- [[197-agent-platform-warp-agents-capabilities-overview-task-lists|Task Lists]] — track complex workflows with real-time progress
- [Rules](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/rules) — set persistent guidelines for agent behavior
- [MCP Servers](https://docs.warp.dev/agent-platform/warp-agents/agent-context/mcp) — expose external data sources and tools to Agents
- [Cloud Agents](https://docs.warp.dev/agent-platform/cloud-agents/overview) — run agents in the cloud on schedules or triggers
