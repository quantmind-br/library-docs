---
title: "Terminal Context Capture in ForgeCode"
url: https://forgecode.dev/docs/forge-term/
source: sitemap
fetched_at: 2026-04-30T14:09:09.5536454-03:00
rendered_js: false
word_count: 132
summary: "Use `FORGE_TERM` to automatically provide terminal command history and execution status to ForgeCode."
tags:
  - zsh-plugin
  - terminal-integration
  - context-capture
  - command-history
  - forgecode-configuration
category: configuration
optimized: true
---
# Terminal Context Capture in ForgeCode

> **TL;DR**
> `FORGE_TERM` tracks command history (success/failure) and passes it to ForgeCode.

## How It Works
- **Default**: Enabled.
- **Context**: ForgeCode sees your last commands and their exit codes.

## Example

| Without Context | With Context |
|----------------|---------------|
| `: fix this` → "What failed?" | `: fix this` → "The `cargo build` failed with exit code 1." |

## Configuration

### Disable
- **Session**: `unset FORGE_TERM`
- **Permanent**: Add to `~/.env` or `~/.zshrc`:
  ```bash
  unset FORGE_TERM
  ```
  > **Reload**: `source ~/.zshrc`

### Re-enable
```bash
export FORGE_TERM=1
```

## Buffer Size
- **Default**: 5 commands (`FORGE_TERM_MAX_COMMANDS=5`).
- **Adjust**: Increase for long pipelines, decrease for context limits.

## Verification
1. Check variable:
   ```bash
echo $FORGE_TERM
   ```
2. Run a command (e.g., `false`).
3. Ask ForgeCode: `: what was the last command?`

## Related
- [ZSH Support](https://forgecode.dev/docs/zsh-support/)