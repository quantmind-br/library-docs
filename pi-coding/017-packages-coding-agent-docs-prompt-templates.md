---
title: Prompt templates
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/prompt-templates.md
source: git
fetched_at: 2026-04-26T05:48:15.349873764-03:00
rendered_js: false
word_count: 372
summary: Create, configure, and use Markdown-based prompt templates to automate and streamline workflows in Pi.
tags:
    - prompt-templates
    - markdown-snippets
    - cli-tools
    - automation
    - configuration
    - template-discovery
category: guide
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

> [!tip] Pi can create prompt templates — ask it to build one for your workflow.

# Prompt Templates

Prompt templates are Markdown snippets that expand into full prompts. Type `/name` in the editor to invoke, where `name` is the filename without `.md`.

## Locations

Pi loads templates from:

| Source | Path / Method |
|--------|---------------|
| Global | `~/.pi/agent/prompts/*.md` |
| Project | `.pi/prompts/*.md` |
| Packages | `prompts/` directories or `pi.prompts` in `package.json` |
| Settings | `prompts` array with files or directories |
| CLI | `--prompt-template <path>` (repeatable) |

Disable discovery with `--no-prompt-templates`.

## Format

```markdown
---
description: Review staged git changes
---
Review the staged changes (`git diff --cached`). Focus on:
- Bugs and logic errors
- Security issues
- Error handling gaps
```

- The filename becomes the command name (`review.md` → `/review`).
- `description` is optional — if missing, the first non-empty line is used.
- `argument-hint` is optional — displayed before the description in autocomplete.

### Argument Hints

Use `argument-hint` in frontmatter to show expected arguments. `<angle brackets>` = required, `[square brackets]` = optional:

```markdown
---
description: Review PRs from URLs with structured issue and code analysis
argument-hint: "<PR-URL>"
---
```

Autocomplete rendering:

```
-> pr   <PR-URL>       -- Review PRs from URLs with structured issue and code analysis
   is   <issue>        -- Analyze GitHub issues (bugs or feature requests)
   wr   [instructions] -- Finish the current task end-to-end
   cl   -- Audit changelog entries before release
```

## Usage

Type `/` followed by the template name. Autocomplete shows available templates with descriptions.

```
/review                           # Expands review.md
/component Button                 # Expands with argument
/component Button "click handler" # Multiple arguments
```

## Arguments

Templates support positional arguments and slicing:

| Syntax | Meaning |
|--------|---------|
| `$1`, `$2`, ... | Positional args |
| `$@` or `$ARGUMENTS` | All args joined |
| `${@:N}` | Args from Nth position (1-indexed) |
| `${@:N:L}` | `L` args starting at N |

Example template:

```markdown
---
description: Create a component
---
Create a React component named $1 with features: $@
```

Usage: `/component Button "onClick handler" "disabled support"`

## Loading Rules

- Template discovery in `prompts/` is non-recursive.
- For subdirectory templates, add them explicitly via `prompts` settings or a package manifest.

#prompt-templates #automation #configuration
