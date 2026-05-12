---
title: Task lists | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/task-lists
source: sitemap
fetched_at: 2026-04-29T15:03:48.2969696-03:00
rendered_js: false
word_count: 236
summary: This document explains how the Agent automatically decomposes complex user requests into sequential, trackable tasks with real-time status updates and completion reporting.
tags:
    - agent-automation
    - task-management
    - workflow-tracking
    - task-lists
    - ai-productivity
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The Agent automatically breaks down complex requests into clear, trackable steps. For sufficiently complex requests, the Agent creates a list of tasks, executes them in order, and tracks progress from start to finish. No settings adjustment or special mode required.

![Task list in progress](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F769506432-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FAULCelT4yIUOcSwWWvPk%252Fuploads%252Fgit-blob-8fc56bb8b1cad994773fea9568368a864a80e973%252Fin-progress-tasklist.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c44e6256&sv=2)

## How task lists work

1. **Automatic task creation** — for complex requests, the Agent generates a structured list of tasks
2. **Step-by-step execution** — the Agent works through each task in sequence, updating statuses in real time
3. **Summary** — once all tasks complete, the Agent provides a concise summary including outputs, results, and relevant context; if any tasks were skipped, it explains why

After each step completes, a completion marker appears in the Agent conversation.

![Completion markers](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F769506432-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FAULCelT4yIUOcSwWWvPk%252Fuploads%252Fgit-blob-d2650352ed9c6ddd1e6dbadceaffaab3d577c228%252Fcompletion-markers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dfa0b8eb&sv=2)

## Task statuses

| Status | Icon | Meaning |
|--------|------|---------|
| In progress | 🔄 | Agent is actively working on this task |
| Completed | ✅ | Task finished successfully |
| Pending | ⏳ | Task is queued but work hasn't begun |
| Stopped | ⛔ | Task was stopped before completion |

![Task list overview](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F769506432-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FAULCelT4yIUOcSwWWvPk%252Fuploads%252Fgit-blob-6846a8fa439fad543fc7510cce200d0476bdf7c1%252Ftasklist-small.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a07acaa5&sv=2)

## Task list access

During any Agent conversation, a task list chip appears at the bottom-right of the screen (when input is pinned to the bottom). Click the chip to open the current task list. You can collapse or expand the view at any time without interrupting the Agent.

![Task list popup](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F769506432-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FAULCelT4yIUOcSwWWvPk%252Fuploads%252Fgit-blob-9180348ecd737faea5b77d00a5d133a4fe8bd78c%252Ftasklist-popup.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dc50c0b9&sv=2)
