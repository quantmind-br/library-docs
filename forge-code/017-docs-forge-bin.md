---
title: "Overriding ForgeCode Binary Path"
url: https://forgecode.dev/docs/forge-bin/
source: sitemap
fetched_at: 2026-04-30T14:09:06.666464803-03:00
rendered_js: false
word_count: 90
summary: "Use the `FORGE_BIN` environment variable to point the ForgeCode ZSH plugin at a custom binary."
tags:
  - zsh-plugin
  - binary-path
  - environment-variables
  - forgecode-configuration
  - shell-integration
category: configuration
optimized: true
---
# Overriding ForgeCode Binary Path

> **TL;DR**
> Set `FORGE_BIN` to use a local build, custom path, or multiple versions.

## How It Works
- **Default**: `forge` (resolved via `$PATH`).
- **Override**: `FORGE_BIN` specifies the binary to use.

## Use Cases

| Scenario | Example |
|----------|---------|
| **Local build** | `export FORGE_BIN="/path/to/local/forge"` |
| **Custom path** | `export FORGE_BIN="/opt/forge/nightly"` |
| **Multiple versions** | `export FORGE_BIN="/usr/local/forge-beta"` |

## Configuration

### Persistent (`~/.zshrc`)
```bash
export FORGE_BIN="/path/to/forge"
```
> **Reload**: `source ~/.zshrc`

### Temporary (Current Session)
```bash
export FORGE_BIN="/path/to/forge"
```

## Verification
```bash
$FORGE_BIN --version
```

## Reset
```bash
unset FORGE_BIN
```

## Related
- [ZSH Support](https://forgecode.dev/docs/zsh-support/)