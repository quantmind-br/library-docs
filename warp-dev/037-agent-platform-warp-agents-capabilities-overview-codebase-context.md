---
title: Codebase Context | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/codebase-context
source: sitemap
fetched_at: 2026-04-29T15:03:54.466093788-03:00
rendered_js: false
word_count: 732
summary: This document explains how to use Codebase Context in Warp to index local Git repositories, enabling AI agents to provide more accurate, context-aware assistance based on your specific project files.
tags:
    - codebase-indexing
    - ai-agents
    - warp-terminal
    - development-tools
    - context-aware-coding
    - repository-management
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Codebase Context indexes your local Git repository so Agents can answer questions and generate code grounded in your actual project structure.

## Get started

Index a project and see the difference in agent responses in a few minutes.

> [!note]
> Don't have a project to try? Clone a popular open-source repo:
> ```bash
> git clone https://github.com/vercel/next.js.git && cd next.js
> ```

1. **Open a project folder in Warp.** Navigate to a Git repository via `cd` or the file tree. Warp auto-detects and begins indexing.
2. **Verify indexing status.** Go to **Settings** > **Code** > **Indexing and projects** — status shows **Synced** when ready.
3. **Ask the Agent a question about your code.** Start an agent conversation (`⌘+Enter` macOS, `Ctrl+Shift+Enter` Windows/Linux) and try:
   - "Explain the architecture of this project"
   - "What are the main entry points?"
   - "Walk me through the most important modules"
4. **See the difference.** The Agent grounds responses in actual files, functions, and line numbers.

## Indexing your codebase

When you open a directory in Warp, Warp checks if it is part of a Git repository and begins indexing source code. Warp also detects [[214-code-git-worktrees|Git worktrees]] — each worktree is indexed as its own repository.

> [!note]
> Code indexed with Codebase Context is never stored on our servers. Codebase Context works with both local agent sessions and [[194-agent-platform-cloud-agents-overview|cloud agent runs]]. Without it, agents can still use terminal commands (e.g., `grep`, `sed`) to navigate code.

**Codebase indexing triggers:**

- Initially when Codebase Context is enabled
- Periodically, automatically
- When a new Agent conversation begins
- When you click the sync 🔄 button in **Settings** > **Code** > **Indexing and projects**

**The embeddings index helps Agents:**

- Understand project structure and reference relevant code
- Generate completions matching your style and patterns
- Suggest edits in correct locations based on real context

> [!note]
> For large projects, indexing may take a few minutes. Agentic coding features remain fully available in the meantime.

View and manage indexed codebases in **Settings** > **Code** > **Indexing and projects** under "Initialized / indexed folders". Toggle auto-indexing for new folders.

### Codebase indexing states

| Status | Description |
|--------|-------------|
| **Synced** | Indexing complete; codebase ready for context |
| **Discovering files** | Warp scanning and indexing |
| **Failed** | Indexing failed (unreadable `.git` dir, corrupted repo). Try re-cloning and re-syncing |
| **Codebase too large** | Files exceed plan limit. Use `.warpindexingignore` to reduce, or [[https://warp.dev/contact-sales|contact sales]] |

### When does codebase syncing happen?

Warp auto-triggers syncs initially, periodically, on conversation start, or when you click sync. In large projects (e.g., after a branch switch), there may be a short delay where the Agent references stale or outdated files.

### File and codebase limits

All plans support indexing **at least 5,000 files per codebase**. Higher tiers include more files and additional codebases. See [[https://www.warp.dev/pricing|pricing page]] for full details.

### Ignore files

Warp respects the following ignore files to control what gets indexed:

- `.gitignore`
- `.warpindexingignore`
- `.cursorignore`
- `.cursorindexingignore`
- `.codeiumignore`

Use these to skip indexing of folders, generated files, or content you don't want agents to reference. Excluded files **do not** count toward your file limit.

## Codebase Context in cloud agent runs

Codebase Context is available in all Oz cloud agent runs — CLI, API/SDK, integrations (Slack, Linear, GitHub Actions), and schedules — as long as Codebase Context is enabled for your account. No additional configuration needed.

## Multi-repo context

Warp supports referencing context across multiple indexed repositories. You don't need to be inside a specific repo for agents to use its context.

**This is especially useful when:**

- Implementing a feature across multiple repos (e.g., full-stack work across client and server)
- Using one repo as reference while building in another

Agents will only reference other repositories if they are already indexed. During cross-repo tasks, Warp's Agents have access to file paths of all indexed repos. Mentioning the exact repo name in your prompt increases the likelihood of cross-repo context usage.

## Demo: Explain my codebase with Warp

Example from [[https://docs.warp.dev/guides|Warp Guides]], where Zach demonstrates Warp using Codebase Context to search for and use relevant files:

* * *

## Next steps

With your codebase indexed:

- [[178-code-code-editor-file-tree|File Tree]] — Browse project structure and open files directly
- [[181-code-code-editor|Code editor]] — Edit files with syntax highlighting, LSP support, and find-and-replace without leaving Warp