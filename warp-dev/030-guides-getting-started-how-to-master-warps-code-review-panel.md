---
title: Master Warp's Code Review Panel | Guides | Warp
url: https://docs.warp.dev/guides/getting-started/how-to-master-warps-code-review-panel
source: sitemap
fetched_at: 2026-04-29T15:06:19.520560844-03:00
rendered_js: false
word_count: 186
summary: Use the Warp Code Review Panel to view, edit, and commit Git diffs directly within the workspace.
tags:
    - code-review
    - git-integration
    - warp-terminal
    - version-control
    - diff-view
    - developer-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp's Code Review Panel shows all active file diffs, additions, and deletions — without leaving your workspace.

## 1. Opening the Code Review Panel

Click **View Changes** (top-left) or the **Dirty Chip** in your input bar. The panel is available only inside a Git repo.

The panel shows:

- Changed files
- Lines added/deleted
- File-by-file diff summaries

## 2. Editing and Reviewing Code

Open any file directly from the panel in Warp's built-in editor:

- Syntax highlighting
- Find & replace
- Inline editing

Save changes and they reflect instantly in the diff view.

## 3. Componentizing Changes

To apply a fix across the app (e.g., fix an unreadable hover style):

1. Prompt Warp to componentize the hover style
2. Attach the recent diff as context so Warp can generalize it
3. The agent creates a `Tooltip` component that reuses your schema everywhere

## 4. Reviewing and Committing

Once the fix looks correct:

- Review in the code panel
- Commit directly from Warp
- Watch the panel reset to its "no changes" state

You can also click to compare your branch against `main` instantly.
