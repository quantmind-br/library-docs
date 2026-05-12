---
title: Sessions
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/sessions.md
source: git
fetched_at: 2026-05-03T09:31:21.588458942-03:00
optimized: true
word_count: 533
summary: Manage, navigate, and branch conversation sessions including persistence, tree-based history, branching commands, and file organization.
tags:
    - session-management
    - cli-commands
    - data-persistence
    - conversation-history
    - tree-navigation
category: guide
---
# Sessions

Sessions auto-save to `~/.pi/agent/sessions/`, organized by working directory as JSONL files with tree structure.

## CLI Flags

| Flag | Description |
|------|-------------|
| `pi -c` | Continue most recent session |
| `pi -r` | Browse and select past sessions |
| `pi --no-session` | Ephemeral mode, no save |
| `pi --session <path\|id>` | Use specific session file or partial ID |
| `pi --fork <path\|id>` | Fork session into new session |

> [!TIP]
> Use `/session` in interactive mode to see current session file, ID, message count, tokens, and cost.

## Session Commands

| Command | Description |
|---------|-------------|
| `/resume` | Browse and select previous sessions |
| `/new` | Start new session |
| `/name <name>` | Set session display name |
| `/session` | Show session info |
| `/tree` | Navigate current session tree |
| `/fork` | Create new session from previous user message |
| `/clone` | Duplicate current active branch into new session |
| `/compact [prompt]` | Summarize older context |
| `/export [file]` | Export session to HTML |
| `/share` | Upload as private GitHub gist |

## Resume & Delete

`/resume` and `pi -r` open interactive session picker with:
- **Search** by typing
- **Ctrl+P** toggle path display
- **Ctrl+S** toggle sort mode
- **Ctrl+N** filter to named sessions
- **Ctrl+R** rename
- **Ctrl+D** delete (uses `trash` CLI when available)

## Session Tree

Sessions are stored as trees. Every entry has `id` and `parentId`, current position is active leaf.

```
Example shape:
├─ user: "Hello, can you help..."
│  └─ assistant: "Of course! I can..."
│     ├─ user: "Let's try approach A..."
│     │  └─ assistant: "For approach A..."
│     │     └─ user: "That worked..."  ← active
│     └─ user: "Actually, approach B..."
│        └─ assistant: "For approach B..."
```

### Tree Controls

| Key | Action |
|-----|--------|
| ↑/↓ | Navigate visible entries |
| ←/→ | Page up/down |
| Ctrl+←/Ctrl+→ or Alt+←/Alt+→ | Fold/unfold or jump between branches |
| Shift+L | Set or clear label |
| Shift+T | Toggle label timestamps |
| Enter | Select entry |
| Escape/Ctrl+C | Cancel |
| Ctrl+O | Cycle filter mode |

**Filter modes**: default, no-tools, user-only, labeled-only, all

Configure default via `treeFilterMode` in [[103-packages-coding-agent-docs-settings|Settings]].

### Selection Behavior

**Selecting user/custom message**:
1. Moves leaf to selected message's parent
2. Places selected text in editor
3. Edit and resubmit creates new branch

**Selecting assistant/tool/compaction**:
1. Moves leaf to that entry
2. Leaves editor empty
3. Continue from that point

**Selecting root user message**: Resets to empty conversation with original prompt in editor.

## Branching Comparison

| Feature | `/tree` | `/fork` | `/clone` |
|---------|---------|---------|----------|
| Output | Same session | New session file | New session file |
| View | Full tree | User-message selector | Current active branch |
| Typical use | Explore alternatives in place | Start new from earlier prompt | Duplicate current work |
| Summary | Optional | None | None |

## Branch Summaries

When switching away from a branch, pi can summarize the abandoned path and attach it at the new position.

Choose:
1. No summary
2. Summarize with default prompt
3. Summarize with custom focus instructions

> [!NOTE]
> See [[037-packages-coding-agent-docs-compaction|Compaction]] for branch summarization internals and extension hooks.

## Session Format

JSONL containing: messages, model changes, thinking-level changes, labels, compactions, branch summaries, extension entries.

See [[102-packages-coding-agent-docs-session-format|Session Format]] for parsers, SDK usage, SessionManager API.
