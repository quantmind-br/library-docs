---
title: "ZSH Support for ForgeCode"
url: https://forgecode.dev/docs/zsh-support/
source: sitemap
fetched_at: 2026-04-30T14:09:20.619412117-03:00
rendered_js: false
word_count: 287
summary: "Use ForgeCode directly from your ZSH shell with sentinel commands, file tagging, and multiline prompts."
tags:
  - forgecode
  - terminal-integration
  - shell-workflow
  - ai-assistance
  - cli-commands
  - productivity-tools
category: guide
optimized: true
---
# ZSH Support for ForgeCode

> **TL;DR**
> Use `:` sentinel commands to interact with ForgeCode from your native ZSH shell.

## Why Use ZSH Integration?
- **No environment switch**: Use aliases, functions, and shell tools alongside ForgeCode.
- **Context continuity**: Shell and AI prompts share the same workflow.

## Core Features

### Sentinel Commands
Prefix commands with `:` to send prompts to ForgeCode.

| Command | Action |
|---------|--------|
| `:` | Send prompt to last-used agent |
| `:agent` | Switch agents |
| `:new` | Start fresh conversation |
| `:conversation` | Switch conversations |
| `:retry` | Resend last prompt |
| `:config` | Edit config file |

> **Tip**: Press `TAB` after `:` for command completion.

### Agent Selection
- **Switch**: `:muse`, `:forge`, `:sage`
- **List**: `:agent` → Pick from dropdown.
- **Inline**: `:forge Fix the bug in UserService`

> **Note**: Agent name appears in RPROMPT after switch.

### Conversation Management
- **New**: `:new [prompt]`
- **Switch**: `:conversation` → Select from list.
- **Last**: `:conversation -`

### File Tagging
- **Tag files**: `@` + `TAB` → Fuzzy picker.
- **Example**: `@src/utils TAB` → Select file.

> **Note**: `.gitignore` rules apply.

### Multiline Prompts
- **Line breaks**: `Shift+Enter` (Win/Linux), `Option+Enter` (macOS).
- **Long prompts**: Use `:edit` → Opens `$FORGE_EDITOR`/`$EDITOR`.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Commands not working | Run `:doctor` and `:version` |
| File tagging fails | Install `fd` and `fzf` |
| Prompt not sent | Check editor saved/closed (`:edit`) |

## Best Practices
- **Start small**: Test with simple prompts.
- **Use tags**: Reference files directly for context.
- **Commit often**: Clean git state helps ForgeCode track changes.

## Related Guides
- [File Tagging](https://forgecode.dev/docs/file-tagging/)
- [Configuration](https://forgecode.dev/docs/forgecode-config/)