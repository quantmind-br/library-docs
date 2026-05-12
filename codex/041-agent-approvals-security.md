---
number: 41
category: concept
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/agent-approvals-security.md
word_count: 647
---
# Agent Approvals & Security

> **BLUF:** Two-layer security — sandbox mode (what Codex can technically do) + approval policy (when it must ask). Default: network off, workspace write, on-request approvals. Configure via `config.toml`, CLI flags, or profiles.

## Security Layers

| Layer | What It Controls | CLI Flags |
|-------|-----------------|-----------|
| **Sandbox mode** | Where Codex can read/write; network access | `--sandbox` |
| **Approval policy** | When Codex must ask before acting | `--ask-for-approval` |

## Sandbox Modes

| Mode | File Access | Network | Use Case |
|------|-------------|---------|----------|
| `read-only` | Read workspace only | Off | Consultative browsing |
| `workspace-write` | Read/write workspace + `/tmp` | Off by default | Auto (default) |
| `danger-full-access` | Full filesystem + network | Full | Isolated environments only |

### Platform Implementation

| OS | Mechanism |
|----|-----------|
| macOS | Seatbelt (`sandbox-exec`) + platform policy |
| Linux | `bwrap` + `seccomp` |
| Windows (native) | ACL-based, elevated/unelevated modes |
| Windows (WSL2) | Linux sandbox (WSL1 deprecated since 0.115) |

### Protected Paths

Even in `workspace-write`:
- `.git/` protected as read-only
- `.git` pointer files resolve to protected gitdir
- `.agents/` and `.codex/` protected as read-only when directories exist

### Network Control

```toml
[sandbox_workspace_write]
network_access = true  # Default: false
```

Web search defaults to cached (OpenAI-maintained index). Set `web_search = "live"` for live browsing.

> ⚠️ Prompt injection can cause agent to fetch/follow untrusted instructions. Keep network access off unless needed.

## Approval Policies

| Mode | Behavior |
|------|----------|
| `untrusted` | Ask before every action |
| `on-request` | Ask only when Codex requests |
| `never` | Execute without asking |

### Granular Policy

```toml
approval_policy = { granular = {
  sandbox_approval = true,
  rules = true,
  mcp_elicitations = true,
  request_permissions = false,
  skill_approval = false
} }
```

### Common Combinations

| Intent | Flags | Effect |
|--------|-------|--------|
| **Auto (preset)** | `--full-auto` or none | Read/write workspace; approval for outside-workspace edits + network |
| **Safe read-only** | `--sandbox read-only --ask-for-approval on-request` | Read files; approval for edits, commands, network |
| **Read-only quiet** | `--sandbox read-only --ask-for-approval never` | Read only; never prompts |
| **Edit auto, untrusted command approval** | `--sandbox workspace-write --ask-for-approval untrusted` | Auto edits; approval for untrusted commands |
| **Full access (dangerous)** | `--dangerously-bypass-approvals-and-sandbox` or `--yolo` | No sandbox; no approvals |

## Automatic Approval Reviews

Route approval requests through reviewer agent instead of user:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
```

Reviewer evaluates sandbox escalations, network requests, `request_permissions`, side-effecting app/MCP tool calls.

**Reviewer policy:** checks for data exfiltration, credential probing, persistent security weakening, destructive actions.

| Risk Level | Outcome |
|-----------|---------|
| Low/Medium | Proceeds if policy allows |
| High | Requires user authorization + no deny rule |
| Critical | Denied |
| Timeout/parse error/failure | Fails closed (denied) |

Default reviewer policy: [open-source Codex repo](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md). Enterprise override via `guardian_policy_config` in managed requirements.

## Profiles

Save presets as named profiles:

```toml
[profiles.full_auto]
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[profiles.readonly_quiet]
approval_policy = "never"
sandbox_mode    = "read-only"
```

Use: `codex --profile full_auto`

## Sandbox Testing

```bash
# macOS
codex sandbox macos [--full-auto] [--log-denials] [COMMAND]...

# Linux
codex sandbox linux [--full-auto] [COMMAND]...

# Alias
codex debug
codex sandbox seatbelt   # macOS
codex sandbox landlock  # Linux
```

## Filesystem Permission Profiles

Deny reads for specific paths/globs:

```toml
default_permissions = "workspace"

[permissions.workspace.filesystem]
":project_roots" = { "." = "write", "**/*.env" = "none" }
glob_scan_max_depth = 3
```

Use `"none"` for paths Codex shouldn't read. `glob_scan_max_depth` limits unbounded `**` patterns.

## Dev Containers

Use [Codex secure devcontainer](https://github.com/openai/codex/tree/main/.devcontainer) as reference for Docker isolation with `bwrap` + firewall-based outbound controls.

Inside container:
- Keep Codex sandbox if container grants `bwrap` capabilities
- Use `--sandbox danger-full-access` if container is your security boundary

> ⚠️ Running `--sandbox danger-full-access` inside container: malicious project can exfiltrate Codex credentials. Use only with trusted repos.

## OTel Telemetry (Opt-in)

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"         # none | otlp-http | otlp-grpc
log_user_prompt = false    # redact prompts unless policy allows
```

Event types: `codex.conversation_starts`, `codex.api_request`, `codex.sse_event`, `codex.websocket_request`, `codex.user_prompt`, `codex.tool_decision`, `codex.tool_result`.

Metrics: counter + duration histogram pairs for API requests, SSE events, WebSocket activity, tool calls.

## Version Control Best Practices

- Work on feature branch; keep `git status` clean before delegating
- Prefer patch-based workflows (`git diff`/`git apply`) for easier isolation/revert
- Treat Codex suggestions like PRs: run verification, review diffs, document decisions

## Enterprise: Managed Configuration

Admins configure via [Managed Configuration](https://developers.openai.com/codex/enterprise/managed-configuration). Constrain with:
- `allowed_approval_policies`
- `allowed_approvals_reviewers`
- `allowed_sandbox_modes`
- `guardian_policy_config`

## Related

- [[037-concepts-sandboxing|Sandboxing Concepts]]
- [[018-enterprise-managed-configuration|Managed Configuration]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/agent-approvals-security.md)*