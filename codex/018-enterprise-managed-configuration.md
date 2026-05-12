---
title: Managed configuration
url: https://developers.openai.com/codex/enterprise/managed-configuration.md
source: llms
fetched_at: 2026-04-30T10:15:33.848588391-03:00
rendered_js: false
word_count: 811
summary: This document describes how enterprise administrators can enforce security requirements and managed defaults for Codex behavior across local and cloud environments.
tags:
    - enterprise-administration
    - configuration-management
    - security-policy
    - access-control
    - codex-config
    - feature-flags
    - admin-tools
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Managed configuration

Enterprise admins control local Codex behavior in two ways:

| Type | Behavior | User override? |
|------|----------|----------------|
| **Requirements** | Admin-enforced constraints | No |
| **Managed defaults** | Starting values at launch | Yes (reapplied next launch) |

## Admin-enforced requirements (`requirements.toml`)

Constrains security-sensitive settings: approval policy, approvals reviewer, automatic review policy, sandbox mode, web search mode, managed hooks, and optionally allowed MCP servers. If a value conflicts with an enforced rule, Codex falls back to a compatible value and notifies the user.

`mcp_servers` allowlist: Codex enables an MCP server only when both its name and identity match an approved entry; otherwise disables it.

Can also constrain [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags) via `[features]` in `requirements.toml`. Omitted keys remain unconstrained.

For exact keys, see [`requirements.toml` in Configuration Reference](https://developers.openai.com/codex/config-reference#requirementstoml).

### Locations and precedence

Layers applied in this order (earlier wins per field):

1. Cloud-managed requirements (ChatGPT Business/Enterprise)
2. macOS managed preferences (MDM) via `com.openai.codex:requirements_toml_base64`
3. System `requirements.toml` (`/etc/codex/` on Unix, `%ProgramData%\OpenAI\Codex\` on Windows)

Codex merges per field: if an earlier layer sets a field (including empty list), later layers don't override it, but can still fill unset fields.

Legacy `managed_config.toml` fields `approval_policy` and `sandbox_mode` are interpreted as requirements for backwards compatibility.

### Cloud-managed requirements

Fetched from the Codex service when signing in with ChatGPT on Business/Enterprise. Applies across CLI, App, and IDE Extension.

Configure at [Codex managed-config page](https://chatgpt.com/codex/settings/managed-configs). Same format and keys as `requirements.toml`.

Example:
```toml
enforce_residency = "us"
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entrypoints" },
]
```

#### Assign to groups

Different requirements for different user groups, with a default fallback. If a user matches multiple group rules, the first matching rule applies. Codex doesn't fill unset fields from later matching rules.

#### Local application

Codex applies cloud-managed requirements on a best-effort basis:
1. Check for valid, unexpired local cache entry. Use if available.
2. If cache is missing/expired/corrupted/identity mismatch, fetch from service (with retries) and write signed cache entry on success.
3. If fetch fails/timeout and no valid cache, continue without the managed requirements layer.

After cache resolution, enforces as part of normal requirements layering.

### Example `requirements.toml`

Blocks `--ask-for-approval never` and `--sandbox danger-full-access` (including `--yolo`):
```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
```

### Override sandbox by host

Use `[[remote_sandbox_config]]` for different sandbox requirements on different hosts:
```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
```

Matching: case-insensitive; prefers FQDN, falls back to local hostname; `*` = any sequence, `?` = one character. First matching entry wins within the same source.

You can also constrain web search:
```toml
allowed_web_search_modes = ["cached"]  # "disabled" remains implicitly allowed
```
`allowed_web_search_modes = []` allows only `"disabled"`.

### Pin feature flags

```toml
[features]
personality = true
unified_exec = false
browser_use = false
in_app_browser = false
computer_use = false
```

Use canonical keys from `config.toml`'s `[features]`. Codex normalizes and rejects conflicting writes.

- `in_app_browser = false` — disables in-app browser pane
- `browser_use = false` — disables Browser Use and Browser Agent
- `computer_use = false` — disables Computer Use and related install/enablement flows

If omitted, features are allowed by policy, subject to normal client/platform/rollout availability.

### Configure automatic review policy

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com, and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted destinations.
"""
```

`allowed_approvals_reviewers = ["auto_review"]` requires automatic review; include `"user"` when users can choose manual approval.

`guardian_policy_config` replaces the tenant-specific section of the automatic review policy. Managed config takes precedence over local `[auto_review].policy`.

### Enforce deny-read

```toml
[permissions.filesystem]
deny_read = [
  "/Users/alice/.ssh",
  "./private/**/*.txt",
]
```

When present, Codex constrains local sandbox to `read-only` or `workspace-write`. On native Windows, applies to direct file tools; shell subprocess reads don't use this rule.

### Enforce managed hooks

```toml
[features]
codex_hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
timeout = 30
statusMessage = "Checking managed Bash command"
```

Codex enforces hook config from `requirements.toml` but does not distribute scripts in `managed_dir`. Deliver separately via MDM. Managed hook commands should reference absolute paths under the configured directory.

### Enforce command rules

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]
```

Unlike `.rules`, requirements rules must specify `decision` as `"prompt"` or `"forbidden"` (not `"allow"`).

### Restrict MCP servers

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }
```

If `mcp_servers` is present but empty, Codex disables all MCP servers.

## Managed defaults (`managed_config.toml`)

Merge on top of user's `config.toml`, taking precedence over CLI `--config` overrides. Users can change settings during a session; managed defaults reapply next launch.

### Precedence

1. Managed preferences (macOS MDM; highest)
2. `managed_config.toml` (system/managed file)
3. `config.toml` (user base)

CLI `--config key=value` overrides apply to base, but managed layers override them.

### Locations

- Linux/macOS: `/etc/codex/managed_config.toml`
- Windows/non-Unix: `~/.codex/managed_config.toml`

### macOS MDM

Push device profile with base64-encoded TOML payloads at preference domain `com.openai.codex`:
- `config_toml_base64` — managed defaults (highest precedence)
- `requirements_toml_base64` — requirements (follows cloud-managed order)

Same `[features]` table works in `requirements_toml_base64`.

### MDM workflow

1. Build managed payload TOML, encode with `base64` (no wrapping).
2. Drop into MDM profile under `com.openai.codex` domain at `config_toml_base64` or `requirements_toml_base64`.
3. Push profile; ask users to restart Codex and confirm startup config summary reflects managed values.
4. Update payload when revoking/changing policy; CLI reads refreshed preference next launch.

Avoid embedding secrets or high-churn dynamic values.

### Example `managed_config.toml`

```toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false

[otel]
environment = "prod"
exporter = "otlp-http"
log_user_prompt = false
```

### Recommended guardrails

- Prefer `workspace-write` with approvals for most users; reserve full access for controlled containers.
- Keep `network_access = false` unless security review allows required domains.
- Pin OTel settings via managed config, but keep `log_user_prompt = false` unless policy explicitly allows storing prompt contents.
- Periodically audit diffs between local `config.toml` and managed policy to catch drift.

#enterprise #admin #security #configuration #codex