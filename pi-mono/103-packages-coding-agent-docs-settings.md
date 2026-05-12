---
title: Settings
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/settings.md
source: git
fetched_at: 2026-05-03T09:31:22.545457604-03:00
rendered_js: false
word_count: 941
summary: This document provides a comprehensive reference for the Pi configuration system, detailing how to manage global and project-level settings for models, UI, telemetry, retries, and environmental preferences.
tags:
    - configuration
    - json-settings
    - pi-agent
    - environment-variables
    - system-settings
    - llm-configuration
category: reference
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Settings

JSON settings files with project settings overriding global settings.

| Location | Scope |
|----------|-------|
| `~/.pi/agent/settings.json` | Global (all projects) |
| `.pi/settings.json` | Project (current directory) |

Edit directly or use `/settings` for common options.

## Model & Thinking

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `defaultProvider` | string | - | Default provider (e.g., `"anthropic"`) |
| `defaultModel` | string | - | Default model ID |
| `defaultThinkingLevel` | string | - | `"off"`, `"minimal"`, `"low"`, `"medium"`, `"high"`, `"xhigh"` |
| `hideThinkingBlock` | boolean | `false` | Hide thinking blocks in output |
| `thinkingBudgets` | object | - | Custom token budgets per level |

### thinkingBudgets

```json
{ "thinkingBudgets": { "minimal": 1024, "low": 4096, "medium": 10240, "high": 32768 } }
```

## UI & Display

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `theme` | string | `"dark"` | Theme name (`"dark"`, `"light"`, or custom) |
| `quietStartup` | boolean | `false` | Hide startup header |
| `collapseChangelog` | boolean | `false` | Show condensed changelog after updates |
| `enableInstallTelemetry` | boolean | `true` | Send anonymous install/version ping |
| `doubleEscapeAction` | string | `"tree"` | Double-escape action: `"tree"`, `"fork"`, `"none"` |
| `treeFilterMode` | string | `"default"` | Default `/tree` filter |
| `editorPaddingX` | number | `0` | Horizontal editor padding (0-3) |
| `autocompleteMaxVisible` | number | `5` | Max autocomplete items (3-20) |
| `showHardwareCursor` | boolean | `false` | Show terminal cursor |

### Telemetry & Updates

`enableInstallTelemetry` only controls the ping to `https://pi.dev/api/report-install`. Opting out does not disable update checks.

| Setting | Description |
|---------|-------------|
| `PI_SKIP_VERSION_CHECK=1` | Disable version update check |
| `--offline` / `PI_OFFLINE=1` | Disable all startup network operations |

## Warnings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `warnings.anthropicExtraUsage` | boolean | `true` | Warn when Anthropic subscription may use paid extra usage |

```json
{ "warnings": { "anthropicExtraUsage": false } }
```

## Compaction

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `compaction.enabled` | boolean | `true` | Enable auto-compaction |
| `compaction.reserveTokens` | number | `16384` | Tokens reserved for LLM response |
| `compaction.keepRecentTokens` | number | `20000` | Recent tokens to keep (not summarized) |

## Branch Summary

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `branchSummary.reserveTokens` | number | `16384` | Tokens reserved for summarization |
| `branchSummary.skipPrompt` | boolean | `false` | Skip "Summarize branch?" prompt on `/tree` |

## Retry

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `retry.enabled` | boolean | `true` | Enable automatic retry on transient errors |
| `retry.maxRetries` | number | `3` | Maximum retry attempts |
| `retry.baseDelayMs` | number | `2000` | Base delay (2s, 4s, 8s exponential backoff) |
| `retry.provider.timeoutMs` | number | SDK default | Provider request timeout (ms) |
| `retry.provider.maxRetries` | number | SDK default | Provider retry attempts |
| `retry.provider.maxRetryDelayMs` | number | `60000` | Max server-requested delay (60s) |

```json
{
  "retry": {
    "enabled": true,
    "maxRetries": 3,
    "baseDelayMs": 2000,
    "provider": { "timeoutMs": 3600000, "maxRetries": 0, "maxRetryDelayMs": 60000 }
  }
}
```

> [!warning]
> When a provider requests a retry delay longer than `retry.provider.maxRetryDelayMs`, the request fails immediately with an informative error. Set to `0` to disable the cap.

## Message Delivery

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `steeringMode` | string | `"one-at-a-time"` | Steering message delivery: `"all"` or `"one-at-a-time"` |
| `followUpMode` | string | `"one-at-a-time"` | Follow-up message delivery: `"all"` or `"one-at-a-time"` |
| `transport` | string | `"sse"` | Preferred transport: `"sse"`, `"websocket"`, `"auto"` |

## Terminal & Images

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `terminal.showImages` | boolean | `true` | Show images in terminal |
| `terminal.imageWidthCells` | number | `60` | Inline image width (cells) |
| `terminal.clearOnShrink` | boolean | `false` | Clear empty rows when content shrinks |
| `images.autoResize` | boolean | `true` | Resize to 2000x2000 max |
| `images.blockImages` | boolean | `false` | Block all images from LLM |

## Shell

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `shellPath` | string | - | Custom shell path |
| `shellCommandPrefix` | string | - | Prefix for every bash command |
| `npmCommand` | string[] | - | Command argv for npm operations |

```json
{ "npmCommand": ["mise", "exec", "node@20", "--", "npm"] }
```

> [!note]
> When `npmCommand` first element is `"bun"`, modules location is queried with `pm bin -g`.

## Sessions

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `sessionDir` | string | - | Session storage directory (absolute, relative, or `~`) |

```json
{ "sessionDir": ".pi/sessions" }
```

Precedence: `--session-dir` > `PI_CODING_AGENT_SESSION_DIR` > `sessionDir` in settings.json.

## Model Cycling

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabledModels` | string[] | - | Model patterns for Ctrl+P cycling |

```json
{ "enabledModels": ["claude-*", "gpt-4o", "gemini-2*"] }
```

## Markdown

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `markdown.codeBlockIndent` | string | `"  "` | Indentation for code blocks |

## Resources

Paths resolve relative to `~/.pi/agent` (global) or `.pi` (project). Absolute paths and `~` supported.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `packages` | array | `[]` | npm/git packages to load resources from |
| `extensions` | string[] | `[]` | Local extension paths |
| `skills` | string[] | `[]` | Local skill paths |
| `prompts` | string[] | `[]` | Local prompt template paths |
| `themes` | string[] | `[]` | Local theme paths |
| `enableSkillCommands` | boolean | `true` | Register skills as `/skill:name` commands |

Arrays support glob patterns. Use `!pattern` to exclude, `+path` to force-include.

### packages

String form loads all resources:

```json
{ "packages": ["pi-skills", "@org/my-extension"] }
```

Object form filters resources:

```json
{
  "packages": [{ "source": "pi-skills", "skills": ["brave-search"], "extensions": [] }]
}
```

## Project Overrides

Nested objects are merged. Project settings override global:

```json
// ~/.pi/agent/settings.json (global)
{ "theme": "dark", "compaction": { "enabled": true, "reserveTokens": 16384 } }

// .pi/settings.json (project)
{ "compaction": { "reserveTokens": 8192 } }

// Result
{ "theme": "dark", "compaction": { "enabled": true, "reserveTokens": 8192 } }
```

## Full Example

```json
{
  "defaultProvider": "anthropic",
  "defaultModel": "claude-sonnet-4-20250514",
  "defaultThinkingLevel": "medium",
  "theme": "dark",
  "compaction": { "enabled": true, "reserveTokens": 16384, "keepRecentTokens": 20000 },
  "retry": { "enabled": true, "maxRetries": 3 },
  "enabledModels": ["claude-*", "gpt-4o"],
  "warnings": { "anthropicExtraUsage": true },
  "packages": ["pi-skills"]
}
```

#configuration #json-settings #pi-agent #environment-variables #system-settings #llm-configuration