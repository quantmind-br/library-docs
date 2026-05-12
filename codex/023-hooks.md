---
number: 23
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/hooks.md
word_count: 595
---
# Hooks

> **BLUF:** Extensibility framework for injecting custom scripts into the Codex agentic loop. Covers event types, matchers, handler configuration, managed hooks, input/output schemas, and hook-specific behaviors.

## Enable Hooks

```toml
[features]
codex_hooks = true
```

## Hook Locations

Codex discovers hooks next to active config layers. Locations (highest to lowest precedence):

1. `~/.codex/config.toml` (inline `[hooks]`)
2. `~/.codex/hooks.json`
3. `<repo>/.codex/config.toml` (inline `[hooks]`) — only when project is trusted
4. `<repo>/.codex/hooks.json` — only when project is trusted

> If more than one hook source exists, Codex loads all matching hooks. Higher-precedence layers do not replace lower-precedence hooks.

## Config Shape

```json
{
  "hooks": {
    "<EventName>": [
      {
        "matcher": "<regex>",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/script",
            "timeout": 30,
            "statusMessage": "Status text shown during run"
          }
        ]
      }
    ]
  }
}
```

Equivalent inline TOML:
```toml
[[hooks.<EventName>]]
matcher = "<regex>"

[[hooks.<EventName>.hooks]]
type = "command"
command = "/path/to/script"
timeout = 30
statusMessage = "Status text"
```

## Event Types

| Event | When It Fires | Matcher Supported |
|-------|--------------|-------------------|
| `SessionStart` | Session opens | ✅ (matches `source`: `startup`\|`resume`\|`clear`) |
| `PreToolUse` | Before tool call | ✅ (tool name) |
| `PermissionRequest` | Before approval prompt | ✅ (tool name) |
| `PostToolUse` | After tool completes | ✅ (tool name) |
| `UserPromptSubmit` | Before prompt sent | ❌ (matcher ignored) |
| `Stop` | At turn end | ❌ (matcher ignored) |

Tool matchers support: `Bash`, `apply_patch` (alias: `Edit`, `Write`), MCP tool names (`mcp__filesystem__read_file`, `mcp__filesystem__.*`).

## Common Input Fields (stdin JSON)

| Field | Type | Meaning |
|-------|------|---------|
| `session_id` | `string` | Current session/thread ID |
| `transcript_path` | `string\|null` | Session transcript file path |
| `cwd` | `string` | Working directory |
| `hook_event_name` | `string` | Current event name |
| `model` | `string` | Active model slug |
| `turn_id` | `string` | (Turn-scoped hooks) Active turn ID |

## Common Output Fields (stdout JSON)

Supported by `SessionStart`, `UserPromptSubmit`, `Stop`:

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}
```

Exit `0` with no output = success (Codex continues).

## Event-Specific Behavior

### SessionStart

**Input extras:** `source` (`startup`\|`resume`\|`clear`)

**Output:** Plain text on `stdout` → extra developer context. JSON supports common output fields +:

```json
{ "hookSpecificOutput": { "additionalContext": "Load workspace conventions." } }
```

### PreToolUse

**Input extras:** `turn_id`, `tool_name`, `tool_use_id`, `tool_input` (for Bash/apply_patch: `command`; for MCP: all args)

**Output:** JSON with `systemMessage` or block:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked."
  }
}
```

Alternative: exit code `2` + reason to `stderr`.

> `continue: false`, `stopReason`, `suppressOutput` are parsed but not yet supported for PreToolUse (fail open).

### PermissionRequest

**Input extras:** `turn_id`, `tool_name`, `tool_input`, `tool_input.description`

**Output — Allow:**
```json
{ "hookSpecificOutput": { "decision": { "behavior": "allow" } } }
```

**Output — Deny:**
```json
{ "hookSpecificOutput": { "decision": { "behavior": "deny", "message": "Blocked." } } }
```

Multiple matching hooks: any `deny` wins; `allow` from all → no prompt; no decision → normal approval flow.

> `updatedInput`, `updatedPermissions`, `interrupt` are reserved (fail closed).

### PostToolUse

**Input extras:** `turn_id`, `tool_name`, `tool_use_id`, `tool_input`, `tool_response` (MCP call result)

**Output:** `systemMessage`, `continue: false`, `stopReason`, `decision: block` (replaces tool result with feedback):

```json
{
  "decision": "block",
  "reason": "Output needs review.",
  "hookSpecificOutput": { "additionalContext": "Command updated generated files." }
}
```

> `continue: false` replaces tool result with your text and continues.

### UserPromptSubmit

**Input extras:** `turn_id`, `prompt`

**Output:** Plain text → extra developer context. JSON supports common output fields + `additionalContext`.

**Block prompt:**
```json
{ "decision": "block", "reason": "Ask for confirmation." }
```
Or exit code `2` + reason to `stderr`.

### Stop

**Input extras:** `turn_id`, `stop_hook_active`, `last_assistant_message`

**Output:** JSON only (plain text invalid). Supports common output fields.

**Continue (skip the stop):**
```json
{ "decision": "block", "reason": "Run one more pass over tests." }
```

Exit code `2` + reason to `stderr` also works.

> `continue: false` from any matching hook takes precedence over continuation from other hooks.

## Managed Hooks (Enterprise)

Admins deploy `requirements.toml` with inline hook config. Scripts delivered via MDM/device management.

```toml
[features]
codex_hooks = true

[hooks]
managed_dir = "/enterprise/hooks"       # macOS/Linux
windows_managed_dir = 'C:\enterprise\hooks'  # Windows

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
timeout = 30
```

> Codex doesn't distribute scripts — enterprise tooling must install and update them separately. Use absolute paths under the configured directory.

## Matcher Examples

- `Bash` — match Bash tool
- `^apply_patch$` — exact apply_patch
- `Edit|Write` — alias matchers
- `mcp__filesystem__read_file` — specific MCP tool
- `mcp__filesystem__.*` — all filesystem MCP tools
- `startup|resume|clear` — SessionStart sources

## Timeout

Default: `600` seconds. Override per hook with `timeout` field (seconds).

## Related

- [[013-config-basic|Config Basics]]
- [[009-enterprise-admin-setup|Admin Setup]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/hooks.md)*