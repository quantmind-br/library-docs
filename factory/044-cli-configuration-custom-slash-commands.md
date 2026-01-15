---
title: Custom Slash Commands - Factory Documentation
url: https://docs.factory.ai/cli/configuration/custom-slash-commands
source: sitemap
fetched_at: 2026-01-13T19:03:56.307115088-03:00
rendered_js: false
word_count: 606
summary: This document explains how to create, manage, and use custom slash commands to turn repeatable prompts or terminal scripts into executable shortcuts.
tags:
    - custom-commands
    - cli-configuration
    - markdown-templates
    - executable-scripts
    - productivity-shortcuts
category: guide
---

Custom slash commands turn repeatable prompts or setup steps into `/shortcuts`. Droid scans a pair of `.factory/commands` folders, turns each file into a command, and pipes the result straight into the conversation or your terminal session.

* * *

## 1 · Discovery & naming

ScopeLocationPurpose**Workspace**`<repo>/.factory/commands`Project-specific commands shared with teammates. Overrides any personal command with the same slug.**Personal**`~/.factory/commands`Always scanned. Stores private or cross-project shortcuts.

- Only Markdown (`*.md`) files and files with a leading shebang (`#!`) are registered.
- Filenames are slugged (lowercase, spaces → `-`, non URL-safe characters dropped). `Code Review.mdx` becomes `/code-review`.
- Invoke commands from chat with `/command-name optional arguments`. Slash suggestions use the description pulled from the file.
- Run `/commands` to open the **Custom Commands** manager UI for browsing, reloading (`R`), or importing commands.
- Commands must live at the top level of the `commands` directory. Nested folders are ignored today.

* * *

## 2 · Markdown commands

Markdown files render into a system notification that seeds droid’s next turn. Optional YAML frontmatter controls autocomplete metadata.

```
---
description: Send a code review checklist
argument-hint: <branch-name>
---

Please review `$ARGUMENTS` and summarize any merge blockers, test gaps, and risky areas.

- Highlight security or performance concerns
- Suggest follow-up tasks with owners
- List files that need attention
```

Frontmatter keyPurpose`description`Overrides the generated summary shown in slash suggestions.`argument-hint`Appends inline usage hints (e.g., `/code-review <branch-name>`).`allowed-tools`Reserved for future use. Safe to omit.

`$ARGUMENTS` expands to everything typed after the command name. If you do not reference `$ARGUMENTS`, the body is sent unchanged.

* * *

## 3 · Executable commands

Executable files must start with a valid shebang so the CLI can call the interpreter.

```
#!/usr/bin/env bash
set -euo pipefail

echo "Preparing $1"
npm install
npm run lint
echo "Ready to deploy $1"
```

- The executable receives the command arguments (`/deploy feature/login` → `$1=feature/login`).
- Scripts run from the current working directory and inherit your environment, so they have the same permissions you do.
- Stdout and stderr (up to 64 KB) plus the script contents are posted back to the chat transcript for transparency. Failures still surface their logs.

* * *

## 4 · Managing commands

- **Edit or add** files directly in `.factory/commands`. The CLI rescans on launch; press `R` inside `/commands` to reload without restarting.
- **Import** existing `.agents` or `.claude` commands: open `/commands`, press `I`, select entries, and they copy into your Factory directory.
- **Remove** a command by deleting its file. Since workspace commands win precedence, deleting the repo version reveals the personal fallback if one exists.

* * *

## 5 · Usage patterns

- Keep project workflows under version control inside the repo’s `.factory/commands` so teammates share the same shortcuts.
- Build idempotent scripts that are safe to rerun; document any cleanup steps in the file itself.
- Use Markdown templates for checklists, code review rubrics, onboarding instructions, or context packets you frequently provide to droid.
- Review executable commands like any other source code—treat secrets carefully and prefer referencing environment variables already loaded in your shell.

* * *

## 6 · Examples

### Code review rubric (Markdown)

```
---
description: Ask droid for a structured code review
argument-hint: <branch-or-PR>
---

Review `$ARGUMENTS` and respond with:

1. **Summary** – What changed and why it matters.
2. **Correctness** – Tests, edge cases, and regressions to check.
3. **Risks** – Security, performance, or migration concerns.
4. **Follow-up** – Concrete TODOs for the author.

Include file paths alongside any specific feedback.
```

Invoke with `/review feature/login-flow` to seed droid with a consistent checklist before it inspects the diff.

### Daily standup helper (Markdown)

```
---
description: Summarize progress for standup
---

Draft a standup update using:

- **Yesterday:** Key wins, merged PRs, or blockers cleared.
- **Today:** Planned work items and their goals.
- **Risks:** Anything at risk of slipping, support needed, or cross-team dependencies.

Keep it to three short bullet sections.
```

Use `/standup` after droid reviews your git history or TODO list to generate a polished update.

### Regression smoke test (Executable)

```
#!/usr/bin/env bash
set -euo pipefail

target=${1:-"src"}

echo "Running lint + unit tests for $target"
npm run lint -- "$target"
npm test -- --runTestsByPath "$target"

echo "Collecting git status"
git status --short

echo "Done"
```

Saved as `smoke.sh`, this shows up as `/smoke`. Pass a path (`/smoke src/widgets/__tests__/widget.test.tsx`) to constrain the checks and share the aggregated output with everyone on the thread. Once set up, custom slash commands compress multi-step prompts or environment setup into a single keystroke, keeping your focus on guiding droid instead of repeating boilerplate.