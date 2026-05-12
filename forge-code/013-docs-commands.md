---
title: "Custom Commands in ForgeCode"
url: https://forgecode.dev/docs/commands/
source: sitemap
fetched_at: 2026-04-30T14:09:04.328457862-03:00
rendered_js: false
word_count: 175
summary: "Automate repeatable workflows with custom slash commands in ForgeCode using Markdown files."
tags:
  - workflow-automation
  - developer-tools
  - cli-commands
  - custom-scripts
  - forgecode
  - productivity
category: configuration
optimized: true
---
# Custom Commands in ForgeCode

> **TL;DR**
> Turn repeatable workflows into slash commands with `.forge/commands/<name>.md`.

## How It Works

| Part | Purpose |
|------|---------|
| **Filename** | Command name (e.g., `check.md` → `/check`) |
| **Frontmatter** | Metadata (`name`, `description`) |
| **Body** | Instructions (Markdown + XML-style tags) |

## File Structure

### Frontmatter (Required)
```yaml
---
name: check
description: Run linter and tests
---
```

### Body (Markdown)
- **Prose**: Context/decision logic.
- **Lists**: Sequential steps.
- **XML tags**: Literal shell commands (e.g., `<lint>eslint src</lint>`).
- **Code blocks**: Multi-line scripts.

## Example: Lint & Test
```markdown
---
name: check
description: Run linter and tests
---

1. Lint the codebase:
   <lint>npm run lint</lint>

2. Run tests:
   <test>npm test</test>

3. If any test fails, analyze the failure and suggest fixes.
```

## Command Locations

| Location | Scope | Path |
|----------|-------|------|
| Project | Team | `.forge/commands/` |
| User | Global | `~/.forge/commands/` |
| Built-in | System | (Preloaded) |

> **Precedence**: Project > User > Built-in.

## Usage

1. **Invoke**: Type `:check` in ForgeCode chat.
2. **List**: `:help` → Shows all commands.

## Best Practices
- **Rule of 3**: If you’ve typed it 3 times, make a command.
- **Team sharing**: Use project commands for shared workflows.
- **Error handling**: ForgeCode auto-fixes failed steps.