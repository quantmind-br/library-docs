---
title: Custom instructions with AGENTS.md
url: https://developers.openai.com/codex/guides/agents-md.md
source: llms
fetched_at: 2026-04-30T10:15:37.774644435-03:00
rendered_js: false
word_count: 486
summary: This document explains how to configure and structure AGENTS.md files to provide Codex with global and project-specific instructions. It details the discovery, precedence, and inheritance rules used to manage persistent behavioral guidance.
tags:
    - codex
    - instruction-files
    - configuration
    - project-management
    - agent-behavior
    - file-discovery
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Custom instructions with AGENTS.md

Codex reads `AGENTS.md` files before doing any work. Layer global guidance with project-specific overrides for consistent expectations across repositories.

## How Codex discovers guidance

Builds an instruction chain once per run (once per TUI session). Precedence:

1. **Global scope** — Codex home directory (`~/.codex` or `$CODEX_HOME`):
   - Reads `AGENTS.override.md` if it exists
   - Otherwise reads `AGENTS.md`
   - Only the first non-empty file at this level is used
2. **Project scope** — starting at project root (typically Git root), walks down to current working directory. In each directory:
   - Checks `AGENTS.override.md`, then `AGENTS.md`, then fallback names in `project_doc_fallback_filenames`
   - Includes at most one file per directory
3. **Merge order** — concatenates files from root down, joined with blank lines. Files closer to current directory override earlier guidance because they appear later in the combined prompt.

Codex skips empty files and stops adding once combined size reaches `project_doc_max_bytes` (32 KiB default). See [Project instructions discovery](https://developers.openai.com/codex/config-advanced#project-instructions-discovery). Raise the limit or split across nested directories when you hit the cap.

## Create global guidance

```bash
mkdir -p ~/.codex
```

Create `~/.codex/AGENTS.md`:
```md
# ~/.codex/AGENTS.md

## Working agreements
- Always run `npm test` after modifying JavaScript files.
- Prefer `pnpm` when installing dependencies.
- Ask for confirmation before adding new production dependencies.
```

Verify:
```bash
codex --ask-for-approval never "Summarize the current instructions."
```
Expected: Codex quotes items from `~/.codex/AGENTS.md` before proposing work.

Use `~/.codex/AGENTS.override.md` for temporary global overrides without deleting the base file.

## Layer project instructions

Repository-level files keep Codex aware of project norms while inheriting global defaults.

Repo root `AGENTS.md`:
```md
# AGENTS.md

## Repository expectations
- Run `npm run lint` before opening a pull request.
- Document public utilities in `docs/` when you change behavior.
```

Nested override example (`services/payments/AGENTS.override.md`):
```md
# services/payments/AGENTS.override.md

## Payments service rules
- Use `make test-payments` instead of `npm test`.
- Never rotate API keys without notifying the security channel.
```

Verify from payments directory:
```bash
codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."
```
Expected: global file first, repo root `AGENTS.md` second, payments override last.

## Customize fallback filenames

If your repository uses a different filename (e.g. `TEAM_GUIDE.md`), add it to the fallback list:

```toml
# ~/.codex/config.toml
project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
project_doc_max_bytes = 65536
```

Restart Codex so updated configuration loads. Codex checks each directory in this order: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`.

Use a custom `CODEX_HOME` for project-specific automation users:
```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"
```

## Verify your setup

- `codex --ask-for-approval never "Summarize the current instructions."` — echo guidance from global and project files in precedence order
- `codex --cd subdir --ask-for-approval never "Show which instruction files are active."` — confirm nested overrides replace broader rules
- Check `~/.codex/log/codex-tui.log` (or recent `session-*.jsonl` if session logging enabled) to audit loaded files
- Restart Codex in target directory if instructions look stale — Codex rebuilds the instruction chain on every run / TUI session start

## Troubleshoot discovery issues

| Issue | Fix |
|-------|-----|
| Nothing loads | Verify you're in the intended repository; `codex status` should report expected workspace root. Ensure files contain content — empty files are ignored. |
| Wrong guidance appears | Look for `AGENTS.override.md` higher in the tree or under `$CODEX_HOME`. Rename or remove to fall back. |
| Fallback names ignored | Confirm names in `project_doc_fallback_filenames` without typos; restart Codex. |
| Instructions truncated | Raise `project_doc_max_bytes` or split large files across nested directories. |
| Profile confusion | Run `echo $CODEX_HOME` before launching. Non-default value points at a different home directory. |

## Next steps

- [AGENTS.md website](https://agents.md)
- [[047-prompting|Prompting Codex]] — conversational patterns that pair well with persistent guidance

#agents-md #instructions #configuration #codex