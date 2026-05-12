---
title: Prompt templates
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/prompt-templates.md
source: git
fetched_at: 2026-05-03T09:31:15.552398976-03:00
rendered_js: false
word_count: 235
summary: Create, configure, and use Markdown-based prompt templates in Pi to streamline repetitive AI tasks through command-based invocation.
tags:
    - prompt-templates
    - automation
    - workflow-optimization
    - cli-tools
    - markdown-configuration
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Prompt Templates

Prompt templates are Markdown snippets that expand into full prompts. Type `/name` in the editor to invoke, where `name` is the filename without `.md`.

> pi can create prompt templates. Ask it to build one for your workflow.

## Locations

Pi loads templates from:

- Global: `~/.pi/agent/prompts/*.md`
- Project: `.pi/prompts/*.md`
- Packages: `prompts/` directories or `pi.prompts` in `package.json`
- Settings: `prompts` array with files or directories
- CLI: `--prompt-template <path>` (repeatable)

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

- Filename becomes the command name. `review.md` becomes `/review`.
- `description` is optional. If missing, the first non-empty line is used.
- `argument-hint` is optional. Displayed in autocomplete before the description.

### Argument Hints

Use `argument-hint` in frontmatter for expected arguments in autocomplete. `<angle brackets>` = required, `[square brackets]` = optional:

```markdown
---
description: Review PRs from URLs with structured issue and code analysis
argument-hint: "<PR-URL>"
---
```

Autocomplete renders as:

```
→ pr   <PR-URL>       — Review PRs from URLs with structured issue and code analysis
  is   <issue>        — Analyze GitHub issues (bugs or feature requests)
  wr   [instructions] — Finish the current task end-to-end
  cl   — Audit changelog entries before release
```

## Usage

Type `/` followed by the template name in the editor. Autocomplete shows available templates with descriptions.

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
| `$@`, `$ARGUMENTS` | All args joined |
| `${@:N}` | Args from Nth position (1-indexed) |
| `${@:N:L}` | L args starting at N |

Example:

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

#prompt-templates #automation #cli-tools
