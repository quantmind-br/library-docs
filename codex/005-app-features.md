---
number: 5
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/app/features.md
word_count: 835
---
# Codex App Features

> **BLUF:** Focused desktop experience for Codex threads. Key features: multi-project sidebar, built-in Git tools, worktrees, automations, integrated terminal, in-app browser, computer use, voice dictation, and artifact preview (PDF, spreadsheets, presentations).

## Multi-Project Multitask

Run tasks across multiple projects in one window. Each project is a codebase folder. Switch between projects as needed.

> 💡 Split distinct projects (e.g., separate apps/packages in a monorepo) into separate app projects so the sandbox only includes that project's files.

## Modes

Each thread runs in one mode:

| Mode | Execution | Use Case |
|------|-----------|----------|
| **Local** | On your machine | Direct work in project directory |
| **Worktree** | Isolated Git worktree | Try ideas without touching current work; parallel independent tasks |
| **Cloud** | Remote environment | Configured cloud environment |

## Built-in Git Tools

- **Diff pane** — view Git diffs, add inline comments, stage/revert chunks or entire files
- **Commit, push, PR** — create pull requests directly from the app
- **Integrated terminal** — run `git status`, `git pull --rebase`, project commands (`pnpm test`, `npm run lint`)

> ⚠️ `Cmd+K` opens the command palette, not clear terminal. Use `Ctrl+L` to clear.

## Skills & Automations

- **Skills** — same agent skills as CLI and IDE Extension; view team skills across projects via sidebar
- **Automations** — recurring tasks (evaluate telemetry errors + submit fixes, code change reports)
- **Thread automations** — heartbeat-style recurring wake-up calls that preserve thread context for ongoing work

## Worktrees

Create a new [Git worktree](https://git-scm.com/docs/git-worktree) so changes stay isolated from your regular project. Automations run in dedicated background worktrees for Git repos; directly in project directory for non-version-controlled projects.

## Integrated Terminal

Toggle with `Cmd+J`. Scoped to current project or worktree. Codex reads terminal output — it can check development server status or failed build output while working with you.

> 💡 Define **actions** in [[051-local-environments|local environments]] to add shortcut buttons to the top of the Codex window.

## Voice Dictation

Hold `Ctrl+M` while composer is visible and start talking. Voice is transcribed; edit or hit send.

## Pop-out Windows

Pop out an active thread into a separate window. Toggle "stay on top" for persistent visibility across workflows. Ideal for front-end work near browser, editor, or design preview.

## In-App Browser

Preview, review, and comment on local development servers, file-backed previews, and public pages. Use browser comments to mark specific elements, then ask Codex to address feedback.

> ⚠️ In-app browser doesn't support authentication flows, signed-in pages, browser profile, cookies, extensions, or existing tabs.

For Codex to operate the page directly, use **browser use** for local dev servers and file-backed pages.

## Computer Use

Codex operates a macOS app by seeing, clicking, and typing. Use for:

- Testing desktop apps
- Checking browser/simulator flows
- Working with data sources not available as plugins
- Changing app settings
- Reproducing GUI-only bugs

> ⚠️ Computer use affects app/system state outside project workspace. Keep tasks narrow, review permission prompts, use narrowest approval option first. Not available in EEA, UK, or Switzerland.

## Artifact Viewer

Preview non-code artifacts: PDF files, spreadsheets, documents, presentations. Give Codex source data, expected file type/structure, and review criteria. Ask where output was saved and how it was checked.

## IDE Extension Sync

If the [[021-ide-features|Codex IDE Extension]] is installed in your editor, app and IDE automatically sync when in the same project. See **IDE context** option in composer with "Auto context" tracking active file.

## MCP Support

MCP server settings are shared across app, CLI, and IDE Extension. Configure in app settings → MCP section.

## Web Search

- **Local tasks** — enabled by default with cached results
- **Full-access sandbox** — defaults to live results
- Configure in [[013-config-basic|Config basics]] to disable or switch to live.

## Image Generation

- Built-in: `gpt-image-2` (counts toward Codex usage limits)
- Trigger: natural language or `$imagegen` in prompt
- Usage: 3–5x faster than similar non-image turns (varies by quality/size)
- Larger batches: set `OPENAI_API_KEY` in env and ask Codex to use the API (API pricing applies)

## Image Input

- **Drag & drop** images into prompt composer
- **Hold Shift** while dropping to add to context
- **Ask Codex to view** system images — for verifying work (e.g., screenshot app while iterating)

## Chats (Projectless Threads)

For tasks that don't need a specific project/Git repo. Use for research, triage, planning, plugin-heavy workflows.

Working location: `~/.codex/threads` (Codex-managed).

## Memories

Where available, Codex carries context from past tasks into future threads. Useful for stable preferences, project conventions, recurring patterns, known pitfalls.

## Notifications

- Default: notify when task completes or needs approval (app in background)
- Configure: never send / always send (even when focused)
- Settings: Codex app settings

## Keep Awake

Enable "Prevent sleep while running" in app settings — useful for long-running tasks.

## Related

- [[003-app|Codex App]] — overview
- [[050-app-local-environments|Local Environments]]
- [[021-ide-features|IDE Extension Features]]
- [[004-app-automations|Automations]]
- [[009-app-browser|Browser]]
- [[010-app-computer-use|Computer Use]]
- [[050-app-worktrees|Worktrees]]
- [[011-app-settings|Settings]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/app/features.md)*