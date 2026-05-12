---
title: "Customizing ForgeCode Config Location"
url: https://forgecode.dev/docs/forge-config/
source: sitemap
fetched_at: 2026-04-30T14:09:07.640682395-03:00
rendered_js: false
word_count: 95
summary: "Use the `FORGE_CONFIG` environment variable to relocate the ForgeCode configuration directory."
tags:
  - forgecode
  - configuration-file
  - environment-variables
  - dotfiles
  - directory-management
category: configuration
optimized: true
---
# Customizing ForgeCode Config Location

> **TL;DR**
> Set `FORGE_CONFIG` to move the config directory (default: `~/forge/`).

## Default Location
- **macOS/Linux**: `~/forge/`
- **Windows**: `%USERPROFILE%\forge`

## Use Cases

| Scenario | Example |
|----------|---------|
| **Dotfiles repo** | `export FORGE_CONFIG="~/.config/forgecode"` |
| **Multiple environments** | `export FORGE_CONFIG="~/forge-work"` |
| **Different volume** | `export FORGE_CONFIG="/mnt/fast/forge"` |

## Configuration

### Persistent (`~/.env` or `~/.zshrc`)
```bash
export FORGE_CONFIG="/path/to/config"
```
> **Reload**: `source ~/.zshrc`

### Temporary (Current Session)
```bash
export FORGE_CONFIG="/path/to/config"
```

## Verification
```bash
echo $FORGE_CONFIG
```

## Management
- **Edit config**: `:config-edit` in ForgeCode.
- **Reset**: `unset FORGE_CONFIG` or remove from shell profile.

## Related
- [`.forge.toml` Reference](https://forgecode.dev/docs/forgecode-config/)