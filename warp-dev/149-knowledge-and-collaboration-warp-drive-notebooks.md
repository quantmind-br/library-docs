---
title: Warp Drive Notebooks | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/notebooks
source: sitemap
fetched_at: 2026-04-29T15:03:29.325421589-03:00
rendered_js: false
word_count: 380
summary: This document explains how to create, manage, and execute interactive terminal-integrated notebooks, including command blocks, workflows, and team collaboration features.
tags:
    - warp-terminal
    - notebooks
    - shell-scripts
    - command-palette
    - team-collaboration
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Notebooks are runnable markdown documentation with executable shell snippets, searchable and accessible via the [Command Palette](https://docs.warp.dev/terminal/command-palette).

## Save and edit notebooks

Create a new notebook from:
- Warp Drive: `+` → New notebook
- [Command Palette](https://docs.warp.dev/terminal/command-palette): create a team or personal notebook

The notebook editor lets you title the notebook and add text and code elements. The notebook is not saved until a title or body text is added.

## Working with notebooks

### Adding elements

Add text, code, or list items by:
- Markdown shortcuts (e.g., `###` for Heading 3)
- Typing `/` to open the element selection menu
- Pressing `+` when hovering over a line

### Styling elements

Style existing elements by:
- Selecting and choosing text decorations (bold, italics, inline code) from the hover menu
- Markdown syntax (`**bold**`, `*italic*`)
- Changing the element type via the dropdown menu

### Command and code blocks

Insert a code or command block by:
- Selecting **Command** or **Code** from the new element menu
- Typing ` ``` ` (triple backticks)

Select the language at the bottom of the block for syntax highlighting. All code/command blocks provide a quick copy button.

### Command blocks

Command blocks (Shell language) provide extra terminal functionality.

**Executing:** Use the insert button at the bottom of the block, or press `CMD-ENTER` with the block selected (blue highlight). The command is inserted into the active terminal session.

**Arguments:** Use `{{double_curly_brackets}}` to specify arguments, same format as [Workflows](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows).

**Keyboard navigation:**
- Enter navigation mode by clicking a shell block or pressing `CMD-UP` / `CMD-DOWN`
- Press `CMD-ENTER` to insert the command into the terminal
- `UP`, `DOWN`, `CMD-UP`, `CMD-DOWN` navigate between command blocks
- `CMD-L` switches focus back to the terminal without inserting

### Embedding workflows

Select **Embedded Workflow** from the new element menu to insert an existing workflow. The embedded workflow is executable like a regular command block. To edit, search for the workflow title in the [Command Palette](https://docs.warp.dev/terminal/command-palette).

## Team collaboration

Shared notebooks sync immediately for all team members. Only one editor is allowed at a time — opening a notebook with an active editor opens it in Viewing mode. Toggle between view and edit above the title.

## Import and export

See [Warp Drive Import and Export](https://docs.warp.dev/knowledge-and-collaboration/warp-drive#import-and-export).

#warp-terminal #notebooks #shell-scripts #command-palette #team-collaboration #developer-productivity
