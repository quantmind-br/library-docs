---
title: Skills
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md
source: git
fetched_at: 2026-04-26T05:48:30.536602205-03:00
rendered_js: false
word_count: 865
summary: This document explains how to create, structure, and manage modular skill packages that extend agent capabilities in Pi, including discovery rules and frontmatter requirements.
tags:
    - agent-skills
    - automation
    - cli-tools
    - configuration
    - developer-workflow
    - extensibility
category: concept
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

> [!tip] pi can create skills. Ask it to build one for your use case.

# Skills

Skills are self-contained capability packages loaded on-demand, providing specialized workflows, setup instructions, scripts, and reference docs. Pi implements the [Agent Skills standard](https://agentskills.io/specification), warning about violations but remaining lenient.

## Locations

> [!warning] Skills can instruct the model to perform any action and may include executable code. Review skill content before use.

| Source | Path |
|--------|------|
| Global | `~/.pi/agent/skills/`, `~/.agents/skills/` |
| Project | `.pi/skills/`, `.agents/skills/` in `cwd` and ancestors (up to git root or filesystem root) |
| Packages | `skills/` directories or `pi.skills` entries in `package.json` |
| Settings | `skills` array with files or directories |
| CLI | `--skill <path>` (repeatable, additive even with `--no-skills`) |

**Discovery rules:**
- `~/.pi/agent/skills/` and `.pi/skills/`: direct root `.md` files discovered as individual skills
- All locations: directories containing `SKILL.md` discovered recursively
- `~/.agents/skills/` and project `.agents/skills/`: root `.md` files ignored

Disable discovery with `--no-skills` (explicit `--skill` paths still load).

### Using Skills from Other Harnesses

Add directories to settings to use Claude Code or OpenAI Codex skills:

```json
{
  "skills": [
    "~/.claude/skills",
    "~/.codex/skills"
  ]
}
```

For project-level Claude Code skills, add to `.pi/settings.json`:

```json
{
  "skills": ["../.claude/skills"]
}
```

## How Skills Work

1. At startup, pi scans locations and extracts names/descriptions
2. System prompt includes available skills in XML format per the [specification](https://agentskills.io/integrate-skills)
3. On task match, agent uses `read` to load full SKILL.md (models don't always do this; use prompting or `/skill:name` to force)
4. Agent follows instructions, using relative paths for scripts/assets

Progressive disclosure: only descriptions are always in context; full instructions load on-demand.

## Skill Commands

Skills register as `/skill:name` commands:

```bash
/skill:brave-search           # Load and execute the skill
/skill:pdf-tools extract      # Load skill with arguments
```

Arguments after the command are appended to skill content as `User: <args>`. Toggle via `/settings` or `settings.json`:

```json
{
  "enableSkillCommands": true
}
```

## Skill Structure

A skill is a directory with a `SKILL.md` file. Everything else is freeform.

```
my-skill/
├── SKILL.md              # Required: frontmatter + instructions
├── scripts/              # Helper scripts
│   └── process.sh
├── references/           # Detailed docs loaded on-demand
│   └── api-reference.md
└── assets/
    └── template.json
```

### SKILL.md Format

````markdown
---
name: my-skill
description: What this skill does and when to use it. Be specific.
---

# My Skill

## Setup

Run once before first use:
```bash
cd /path/to/skill && npm install
```

## Usage

```bash
./scripts/process.sh <input>
```
````

Use relative paths from the skill directory:

```markdown
See [the reference guide](references/REFERENCE.md) for details.
```

## Frontmatter

Per the [Agent Skills specification](https://agentskills.io/specification#frontmatter-required):

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Max 64 chars. Lowercase a-z, 0-9, hyphens. Must match parent directory. |
| `description` | Yes | Max 1024 chars. What the skill does and when to use it. |
| `license` | No | License name or reference to bundled file. |
| `compatibility` | No | Max 500 chars. Environment requirements. |
| `metadata` | No | Arbitrary key-value mapping. |
| `allowed-tools` | No | Space-delimited list of pre-approved tools (experimental). |
| `disable-model-invocation` | No | When `true`, skill is hidden from system prompt. Users must use `/skill:name`. |

### Name Rules

- 1-64 characters, lowercase letters, numbers, hyphens only
- No leading/trailing hyphens, no consecutive hyphens
- Must match parent directory name
- Valid: `pdf-processing`, `data-analysis`, `code-review`
- Invalid: `PDF-Processing`, `-pdf`, `pdf--processing`

### Description Best Practices

The description determines when the agent loads the skill. Be specific.

Good:
```yaml
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents.
```

Poor:
```yaml
description: Helps with PDFs.
```

## Validation

Pi validates skills against the Agent Skills standard. Most issues produce warnings but still load the skill:

- Name doesn't match parent directory
- Name exceeds 64 characters or contains invalid characters
- Name starts/ends with hyphen or has consecutive hyphens
- Description exceeds 1024 characters

Unknown frontmatter fields are ignored.

> [!danger] Skills with missing description are **not loaded**.

Name collisions (same name from different locations) warn and keep the first skill found.

## Example

```
brave-search/
├── SKILL.md
├── search.js
└── content.js
```

**SKILL.md:**
````markdown
---
name: brave-search
description: Web search and content extraction via Brave Search API. Use for searching documentation, facts, or any web content.
---

# Brave Search

## Setup

```bash
cd /path/to/brave-search && npm install
```

## Search

```bash
./search.js "query"              # Basic search
./search.js "query" --content    # Include page content
```

## Extract Page Content

```bash
./content.js https://example.com
```
````

## Skill Repositories

- [Anthropic Skills](https://github.com/anthropics/skills) - Document processing (docx, pdf, pptx, xlsx), web development
- [Pi Skills](https://github.com/badlogic/pi-skills) - Web search, browser automation, Google APIs, transcription

#agent-skills #extensibility #cli-tools
