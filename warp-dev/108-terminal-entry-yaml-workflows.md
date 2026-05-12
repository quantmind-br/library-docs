---
title: YAML workflows | Warp
url: https://docs.warp.dev/terminal/entry/yaml-workflows
source: sitemap
fetched_at: 2026-04-29T15:02:30.137271526-03:00
rendered_js: false
word_count: 362
summary: This document explains how to create, manage, and execute parameterized terminal workflows within the Warp terminal environment using YAML files.
tags:
    - terminal-productivity
    - workflow-automation
    - yaml-configuration
    - command-line-tools
    - warp-terminal
category: guide
optimized: true
optimized_at: 2026-04-29T19:02:00Z
---
> [!tip]
> New workflows should use [Warp Drive workflows](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows) for a better editing experience.

Workflows are parameterized, searchable terminal commands. Warp provides [community workflows](https://github.com/warpdotdev/workflows) and supports local or repository-scoped custom workflows.

## Use workflows

1. Open Command Search (`CTRL-R`) or Workflow Search (`CTRL-SHIFT-R`)
2. Type to filter workflows (e.g., `git`, `npm`)
3. Press `ENTER` to select, `SHIFT-TAB` to cycle arguments
4. Drag right edge to expand menu

Toggle "Show Global Workflows" in **Settings** → **Features** → **Workflows** to include/exclude YAML and Warp Drive workflows.

## Workflows vs aliases

| Pain point | Aliases | Workflows |
|------------|---------|-----------|
| Context switching | Leave vim, source dotfiles, reset shell | No context switch |
| Documentation | Difficult to attach | Built-in description field |
| Sharing | Manual distribution | Repository-scoped sharing |
| Parameterization | Not supported | Full parameter support |
| Searchability | Poor | Name/description/args searchable |

## Create custom workflows

### File format

Workflow files use `.yml` or `.yaml` extension. See [Workflow spec](https://github.com/warpdotdev/Workflows/tree/main/specs) for examples.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Workflow name (required) |
| `command` | string | Executed command (required) |
| `tags` | array | Categorization tags (optional) |
| `description` | string | What the workflow does (optional) |
| `source_url` | string | Original source URL (optional) |
| `author` | string | Original author (optional) |
| `author_url` | string | Author profile URL (optional) |
| `shells` | array | Valid shells: `zsh`, `bash`, `fish` (optional) |
| `arguments` | array | Parameterized input fields (optional) |

### Arguments

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Parameter identifier (required) |
| `description` | string | User-facing help text (optional) |
| `default_value` | string | Pre-filled value (optional) |

Parameters use `{{argument_name}}` syntax in commands:
```yaml
command: "echo {{variable}} && echo {{sequence}}"
```

## Where to save workflows

| Type | Location | Access |
|------|----------|--------|
| Local | `~/.warp/workflows/` | "My Workflows" tab |
| Repository | `.warp/workflows/` in git repo | "Repository Workflows" tab |
| Global | Fork [workflows repo](https://github.com/warpdotdev/workflows) → PR | All Warp users |

#workflow-automation #yaml-configuration #command-line-tools #terminal-productivity
