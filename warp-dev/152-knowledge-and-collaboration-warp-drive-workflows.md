---
title: Warp Drive Workflows | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows
source: sitemap
fetched_at: 2026-04-29T15:03:30.848752678-03:00
rendered_js: false
word_count: 352
summary: This document explains how to create, manage, and execute parameterized workflows in Warp, including configuring arguments, enums, and team-based editing.
tags:
    - warp-terminal
    - workflow-automation
    - command-palette
    - shell-scripting
    - productivity-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Workflows are parameterized, named commands saved in Warp with descriptions and arguments, searchable via the [Command Palette](https://docs.warp.dev/terminal/command-palette).

## Save and edit workflows

Create from:
- Warp Drive: `+` → New workflow
- Block Actions: Save as Workflow
- Oz agent results: Save as Workflow

Editor fields:
- Name
- Command with arguments (`{{argument}}`)
- Description (optional, indexed for search)
- Arguments with descriptions and default values (optional)

## Working with arguments

Add arguments manually via **New argument** or by typing `{{argument}}` in the command field. Selecting text and clicking **New argument** wraps it in curly braces.

**Rules:**
- Valid characters: `A-Za-z0-9`, hyphens `-`, underscores `_`
- First character cannot be a number

Arguments are **text** type by default.

### Enum type arguments

Enums specify expected inputs, showing suggestions via `SHIFT-TAB` when the workflow is inserted.

To create an enum argument:
1. Navigate to the **default value** field of an argument.
2. Select **Enum** type.
3. Click **New** to create a new enum, or select an existing one.
4. Choose **Static** (manual values) or **Dynamic** (shell command output parsed for valid values).

### Aliases

Workflow aliases are personal shortcuts/configurations, synced across devices if settings sync is enabled. They can set default values for arguments and include [Environment Variables](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/environment-variables).

> [!warning]
> Aliases are not compatible with [YAML Workflows](https://docs.warp.dev/terminal/entry/yaml-workflows).

### AI Autofill

Create or edit a workflow and click **AutoFill** to have an Oz agent generate a title, descriptions, or parameters.

## Team editing

Shared workflows sync immediately for all team members. Simultaneous edits require checking out the latest version.

## Execute workflows

Execute via:
- Warp Drive: click the workflow
- [Command Palette](https://docs.warp.dev/terminal/command-palette): search and click/enter
- [Command Search](https://docs.warp.dev/terminal/entry/command-search): search and click/enter
- `SHIFT-TAB` to cycle through arguments

> [!info]
> Duplicate argument names auto-sync with multiple cursors. Toggle off **Show Global Workflows** in **Settings** → **Features** to exclude YAML workflows from search.

## YAML Workflows

[YAML Workflows](https://docs.warp.dev/terminal/entry/yaml-workflows) (personal and community workflows) remain accessible via Command Search or the Command Palette, but are not available in Warp Drive.

## Import and export

See [Warp Drive Import and Export](https://docs.warp.dev/knowledge-and-collaboration/warp-drive#import-and-export).

#warp-terminal #workflow-automation #command-palette #shell-scripting #productivity-tools
