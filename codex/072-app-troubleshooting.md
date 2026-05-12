---
number: 72
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/app/troubleshooting.md
word_count: 445
---
# Troubleshooting

> **BLUF:** Common Codex app issues and resolutions. Covers Git state confusion, sidebar/thread management, worktree setup, local environment sharing, terminal issues, and log locations.

## FAQ

### Files appear in review panel that Codex didn't edit

The review panel shows all Git working tree changes, not just Codex edits.

| View | What it shows |
|------|---------------|
| Staged changes | `git diff --cached` |
| Unstaged changes | `git diff` |
| **Last turn changes** | Only changes from most recent Codex turn |

Switch to **"Last turn changes"** to see Codex-only edits.

### Remove a project from sidebar

Hover project name → three dots → **Remove**. To restore: **Add new project** button or `Cmd+O`.

### Find archived threads

Go to **Settings** (`codex://settings`). Unarchive to restore to original sidebar location.

### Missing threads in sidebar

1. Click filter icon next to **Threads** → switch to **Chronological**
2. Check **Settings → Archived chats/threads**

### Code doesn't run on worktree

Worktrees only inherit Git-tracked files. Untracked dependencies may need setup.

**Solutions:**
- Run setup scripts via [local environment](https://developers.openai.com/codex/app/local-environments)
- Check out changes in regular project directory
- See [[050-app-worktrees|Worktrees]]

### Teammate's local environment not visible

Local environment config must be in `.codex/` at project root. In monorepos, open the directory containing `.codex/`.

### Codex asks for Apple Music access

macOS privacy prompts for Music, Downloads, Desktop when Codex reads home directory. Approve as needed.

### Too many worktrees from automations

- Archive old automation runs
- Avoid pinning runs unless keeping worktrees

### Recover prompt after wrong target

Cancel run → press **up arrow** in composer to recover previous prompt.

### CLI feature works but app doesn't

App and CLI may run different agent versions. Check versions:

```bash
# CLI version
codex --version

# App bundled version
/Applications/Codex.app/Contents/Resources/codex --version
```

## Feedback & Logs

| Type | Location |
|------|----------|
| App logs (macOS) | `~/Library/Logs/com.openai.codex/YYYY/MM/DD` |
| Session transcripts | `$CODEX_HOME/sessions` (default: `~/.codex/sessions`) |
| Archived sessions | `$CODEX_HOME/archived_sessions` |

### Submitting Issues

1. Search [existing issues](https://github.com/openai/codex/issues)
2. [Open new issue](https://github.com/openai/codex/issues/new?template=2-bug-report.yml) with session ID from `/feedback`
3. Review logs for sensitive data before sharing

## Stuck States

1. Check for pending approvals
2. Run `git status` in terminal
3. Start new thread with smaller, focused prompt

## Terminal Issues

| Symptom | Fix |
|---------|-----|
| Terminal stuck | Close panel → `Cmd+J` → run `pwd` or `git status` |
| Commands behave differently | Validate current directory and branch first |
| Persistent stuck state | Wait for active threads to complete → restart app |
| Fonts not rendering | Change **Code font** in Settings |

> **Note:** `Cmd+K` opens command palette, not terminal clear. Use `Ctrl+L` to clear terminal.

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/app/troubleshooting.md)*
