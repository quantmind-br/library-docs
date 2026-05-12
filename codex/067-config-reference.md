---
number: 67
category: reference
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/config-reference.md
word_count: 2714
---
# Configuration Reference

> **BLUF:** Searchable reference for `~/.codex/config.toml` and admin-enforced `requirements.toml`. Project-scoped `.codex/config.toml` overrides apply only to trusted projects. Use `#:schema https://developers.openai.com/codex/config-schema.json` with Even Better TOML for VS Code autocompletion.

## `config.toml`

### Model & Provider

| Key | Type | Description |
|-----|------|-------------|
| `model` | string | Model to use (e.g., `gpt-5.5`) |
| `review_model` | string | Model for `/review` (defaults to session model) |
| `model_provider` | string | Provider ID from `model_providers` (default: `openai`) |
| `openai_base_url` | string | Base URL override for built-in `openai` provider |
| `model_context_window` | number | Context window tokens |
| `model_auto_compact_token_limit` | number | Auto-compaction threshold |
| `model_catalog_json` | string (path) | JSON model catalog path |
| `oss_provider` | `lmstudio` \| `ollama` | Default local provider for `--oss` |

### Approval & Sandbox

| Key | Type | Description |
|-----|------|-------------|
| `approval_policy` | enum / granular | `untrusted`, `on-request`, `never`, or `{ granular = { ... } }` |
| `approval_policy.granular.sandbox_approval` | boolean | Allow sandbox escalation prompts |
| `approval_policy.granular.rules` | boolean | Allow execpolicy `prompt` rule approvals |
| `approval_policy.granular.mcp_elicitations` | boolean | Allow MCP elicitation prompts |
| `approval_policy.granular.request_permissions` | boolean | Allow `request_permissions` prompts |
| `approval_policy.granular.skill_approval` | boolean | Allow skill-script approval prompts |
| `approvals_reviewer` | `user` \| `auto_review` | Who reviews approval prompts |
| `auto_review.policy` | string | Local Markdown policy for automatic review |
| `sandbox_mode` | enum | `read-only`, `workspace-write`, `danger-full-access` |
| `sandbox_workspace_write.writable_roots` | string[] | Additional writable paths |
| `sandbox_workspace_write.network_access` | boolean | Allow outbound network in workspace-write |
| `sandbox_workspace_write.exclude_tmpdir_env_var` | boolean | Exclude `$TMPDIR` from writable roots |
| `sandbox_workspace_write.exclude_slash_tmp` | boolean | Exclude `/tmp` from writable roots |
| `windows.sandbox` | `unelevated` \| `elevated` | Windows native sandbox mode |
| `windows.sandbox_private_desktop` | boolean | Run sandbox on private desktop |

### Features

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `features.unified_exec` | boolean | true | PTY-backed exec tool |
| `features.shell_snapshot` | boolean | true | Snapshot shell environment |
| `features.undo` | boolean | false | Undo support |
| `features.multi_agent` | boolean | true | Multi-agent collaboration tools |
| `features.personality` | boolean | true | Personality selection |
| `features.fast_mode` | boolean | true | Fast mode selection |
| `features.prevent_idle_sleep` | boolean | false | Prevent sleep during turns (experimental) |
| `features.apps` | boolean | — | ChatGPT Apps/connectors (experimental) |
| `features.codex_hooks` | boolean | — | Lifecycle hooks |
| `features.memories` | boolean | — | Memories feature |
| `features.shell_tool` | boolean | true | Default `shell` tool |
| `features.enable_request_compression` | boolean | true | zstd request compression |
| `features.skill_mcp_dependency_install` | boolean | true | Install missing MCP deps for skills |
| `features.web_search*` | boolean | — | **Deprecated** — use top-level `web_search` |
| `features.web_search_cached*` | boolean | — | **Deprecated** |
| `features.web_search_request*` | boolean | — | **Deprecated** |

### MCP Servers

| Key | Type | Description |
|-----|------|-------------|
| `mcp_servers.<id>.command` | string | Launcher command (stdio) |
| `mcp_servers.<id>.args` | string[] | Arguments |
| `mcp_servers.<id>.env` | map | Environment variables |
| `mcp_servers.<id>.env_vars` | array | Whitelisted env vars with `source: local/remote` |
| `mcp_servers.<id>.cwd` | string | Working directory |
| `mcp_servers.<id>.url` | string | HTTP endpoint (streamable HTTP) |
| `mcp_servers.<id>.bearer_token_env_var` | string | Bearer token env var |
| `mcp_servers.<id>.http_headers` | map | Static HTTP headers |
| `mcp_servers.<id>.env_http_headers` | map | Headers from env vars |
| `mcp_servers.<id>.enabled` | boolean | Disable without removing config |
| `mcp_servers.<id>.required` | boolean | Fail startup if init fails |
| `mcp_servers.<id>.startup_timeout_sec` | number | Startup timeout (default: 10s) |
| `mcp_servers.<id>.tool_timeout_sec` | number | Per-tool timeout (default: 60s) |
| `mcp_servers.<id>.enabled_tools` | string[] | Allow list |
| `mcp_servers.<id>.disabled_tools` | string[] | Deny list (applied after allow) |
| `mcp_servers.<id>.scopes` | string[] | OAuth scopes |
| `mcp_servers.<id>.oauth_resource` | string | RFC 8707 resource parameter |
| `mcp_servers.<id>.experimental_environment` | `local` \| `remote` | Server placement |

### Agents

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agents.max_threads` | number | 6 | Max concurrent agent threads |
| `agents.max_depth` | number | 1 | Max nesting depth |
| `agents.job_max_runtime_seconds` | number | 1800 | Per-worker timeout for CSV jobs |
| `agents.<name>.description` | string | — | Role guidance |
| `agents.<name>.config_file` | string (path) | — | TOML config layer |
| `agents.<name>.nickname_candidates` | string[] | — | Display nickname pool |

### Memories

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `memories.generate_memories` | boolean | true | Store new threads as memory inputs |
| `memories.use_memories` | boolean | true | Inject existing memories into sessions |
| `memories.disable_on_external_context` | boolean | false | Exclude MCP/web search threads |
| `memories.max_raw_memories_for_consolidation` | number | 256 | Max recent raw memories (cap: 4096) |
| `memories.max_unused_days` | number | 30 | Eligibility cutoff (clamp: 0-365) |
| `memories.max_rollout_age_days` | number | 30 | Thread age cutoff (clamp: 0-90) |
| `memories.max_rollouts_per_startup` | number | 16 | Candidates per startup (cap: 128) |
| `memories.min_rollout_idle_hours` | number | 6 | Min idle time (clamp: 1-48) |
| `memories.min_rate_limit_remaining_percent` | number | 25 | Rate limit threshold (clamp: 0-100) |
| `memories.extract_model` | string | — | Model override for extraction |
| `memories.consolidation_model` | string | — | Model override for consolidation |

### Custom Providers

| Key | Type | Description |
|-----|------|-------------|
| `model_providers.<id>.name` | string | Display name |
| `model_providers.<id>.base_url` | string | API base URL |
| `model_providers.<id>.env_key` | string | API key env var |
| `model_providers.<id>.env_key_instructions` | string | Setup guidance |
| `model_providers.<id>.experimental_bearer_token` | string | Direct token (discouraged) |
| `model_providers.<id>.requires_openai_auth` | boolean | Uses OpenAI auth |
| `model_providers.<id>.wire_api` | `responses` | Protocol (default: responses) |
| `model_providers.<id>.query_params` | map | Extra query params |
| `model_providers.<id>.http_headers` | map | Static headers |
| `model_providers.<id>.env_http_headers` | map | Headers from env vars |
| `model_providers.<id>.request_max_retries` | number | HTTP retries (default: 4) |
| `model_providers.<id>.stream_max_retries` | number | SSE retries (default: 5) |
| `model_providers.<id>.stream_idle_timeout_ms` | number | SSE idle timeout (default: 300000) |
| `model_providers.<id>.supports_websockets` | boolean | Supports WebSocket transport |
| `model_providers.<id>.auth.command` | string | Token command |
| `model_providers.<id>.auth.args` | string[] | Token command args |
| `model_providers.<id>.auth.timeout_ms` | number | Token command timeout (default: 5000) |
| `model_providers.<id>.auth.refresh_interval_ms` | number | Proactive refresh (default: 300000; 0 = on-retry only) |
| `model_providers.<id>.auth.cwd` | string (path) | Token command working directory |

### Model Behavior

| Key | Type | Description |
|-----|------|-------------|
| `model_reasoning_effort` | `minimal` \| `low` \| `medium` \| `high` \| `xhigh` | Reasoning depth (Responses API) |
| `plan_mode_reasoning_effort` | `none` \| `minimal` \| `low` \| `medium` \| `high` \| `xhigh` | Plan-mode override |
| `model_reasoning_summary` | `auto` \| `concise` \| `detailed` \| `none` | Summary detail |
| `model_verbosity` | `low` \| `medium` \| `high` | GPT-5 verbosity override |
| `model_supports_reasoning_summaries` | boolean | Force reasoning metadata |

### Shell Environment

| Key | Type | Description |
|-----|------|-------------|
| `shell_environment_policy.inherit` | `all` \| `core` \| `none` | Baseline env inheritance |
| `shell_environment_policy.ignore_default_excludes` | boolean | Keep KEY/SECRET/TOKEN vars |
| `shell_environment_policy.exclude` | string[] | Glob patterns to remove |
| `shell_environment_policy.include_only` | string[] | Whitelist patterns |
| `shell_environment_policy.set` | map | Explicit overrides |
| `shell_environment_policy.experimental_use_profile` | boolean | Use shell profile |

### Project Detection

| Key | Type | Description |
|-----|------|-------------|
| `project_root_markers` | string[] | Filenames for root detection |
| `project_doc_max_bytes` | number | Max bytes read from `AGENTS.md` |
| `project_doc_fallback_filenames` | string[] | Alternatives if `AGENTS.md` missing |

### Profiles

| Key | Type | Description |
|-----|------|-------------|
| `profile` | string | Default profile at startup |
| `profiles.<name>.*` | various | Profile-scoped overrides |
| `profiles.<name>.service_tier` | `flex` \| `fast` | Service tier |
| `profiles.<name>.plan_mode_reasoning_effort` | enum | Plan-mode reasoning |
| `profiles.<name>.web_search` | `disabled` \| `cached` \| `live` | Web search mode |
| `profiles.<name>.personality` | `none` \| `friendly` \| `pragmatic` | Communication style |
| `profiles.<name>.model_catalog_json` | string (path) | Model catalog override |
| `profiles.<name>.model_instructions_file` | string (path) | Instruction file replacement |
| `profiles.<name>.oss_provider` | `lmstudio` \| `ollama` | OSS provider |
| `profiles.<name>.tools_view_image` | boolean | Enable `view_image` tool |
| `profiles.<name>.analytics.enabled` | boolean | Analytics override |
| `profiles.<name>.windows.sandbox` | `unelevated` \| `elevated` | Windows sandbox |

### History & Persistence

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `history.persistence` | `save-all` \| `none` | — | Save transcripts to `history.jsonl` |
| `tool_output_token_limit` | number | — | Token budget for tool outputs |
| `background_terminal_max_timeout` | number | 300000 | Empty `write_stdin` poll window (ms) |
| `history.max_bytes` | number | — | Cap history file size |

### Tools & Web Search

| Key | Type | Description |
|-----|------|-------------|
| `tools.web_search` | boolean \| object | Enable/config web search |
| `tools.view_image` | boolean | Enable `view_image` tool |
| `web_search` | `disabled` \| `cached` \| `live` | Web search mode (default: `cached`; `live` with full-access sandbox) |

### Permissions

| Key | Type | Description |
|-----|------|-------------|
| `default_permissions` | string | Default permissions profile name |
| `permissions.<name>.filesystem.<path>` | `read` \| `write` \| `none` \| table | Filesystem access |
| `permissions.<name>.filesystem.glob_scan_max_depth` | number | Glob expansion depth |
| `permissions.<name>.network.enabled` | boolean | Network access |
| `permissions.<name>.network.proxy_url` | string | HTTP proxy endpoint |
| `permissions.<name>.network.enable_socks5` | boolean | SOCKS5 listener |
| `permissions.<name>.network.socks_url` | string | SOCKS5 endpoint |
| `permissions.<name>.network.enable_socks5_udp` | boolean | UDP over SOCKS5 |
| `permissions.<name>.network.allow_upstream_proxy` | boolean | Chain to upstream proxy |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | boolean | Non-loopback bind addresses |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets` | boolean | Arbitrary Unix sockets |
| `permissions.<name>.network.mode` | `limited` \| `full` | Proxy mode |
| `permissions.<name>.network.domains` | map | Domain allow/deny rules |
| `permissions.<name>.network.unix_sockets` | map | Unix socket rules |
| `permissions.<name>.network.allow_local_binding` | boolean | Local bind/listen |

### Apps & Skills

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `apps.<id>.enabled` | boolean | true | Enable/disable app |
| `apps._default.enabled` | boolean | — | Default app state |
| `apps._default.destructive_enabled` | boolean | — | Default for `destructive_hint = true` tools |
| `apps._default.open_world_enabled` | boolean | — | Default for `open_world_hint = true` tools |
| `apps.<id>.destructive_enabled` | boolean | — | Per-app destructive tools |
| `apps.<id>.open_world_enabled` | boolean | — | Per-app open-world tools |
| `apps.<id>.default_tools_enabled` | boolean | — | Default tool state |
| `apps.<id>.default_tools_approval_mode` | `auto` \| `prompt` \| `approve` | Default approval |
| `apps.<id>.tools.<tool>.enabled` | boolean | — | Per-tool enable |
| `apps.<id>.tools.<tool>.approval_mode` | enum | — | Per-tool approval |
| `skills.config` | object[] | — | Per-skill enablement |
| `skills.config.<index>.path` | string (path) | — | Skill folder with `SKILL.md` |
| `skills.config.<index>.enabled` | boolean | — | Enable/disable skill |
| `tool_suggest.discoverables` | table[] | — | Additional discoverable connectors/plugins |

### TUI

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `tui.notifications` | boolean \| string[] | — | Enable/ restrict notifications |
| `tui.notification_method` | `auto` \| `osc9` \| `bel` | `auto` | Notification method |
| `tui.notification_condition` | `unfocused` \| `always` | `unfocused` | When to notify |
| `tui.animations` | boolean | true | Welcome screen, shimmer, spinner |
| `tui.alternate_screen` | `auto` \| `always` \| `never` | `auto` | Alternate screen (auto skips in Zellij) |
| `tui.show_tooltips` | boolean | true | Onboarding tooltips |
| `tui.status_line` | string[] \| null | — | Footer items; `null` disables |
| `tui.terminal_title` | string[] \| null | `["spinner", "project"]` | Window title items |
| `tui.theme` | string | — | Syntax theme (kebab-case) |

### Logging & Telemetry

| Key | Type | Description |
|-----|------|-------------|
| `log_dir` | string (path) | Log directory (default: `$CODEX_HOME/log`) |
| `sqlite_home` | string (path) | SQLite state DB directory |
| `compact_prompt` | string | History compaction prompt override |
| `commit_attribution` | string | Commit co-author trailer; empty = disabled |
| `otel.environment` | string | `dev` | OTel environment tag |
| `otel.exporter` | `none` \| `otlp-http` \| `otlp-grpc` | Log exporter |
| `otel.trace_exporter` | enum | Trace exporter |
| `otel.metrics_exporter` | `none` \| `statsig` \| `otlp-http` \| `otlp-grpc` | `statsig` | Metrics exporter |
| `otel.log_user_prompt` | boolean | Export raw prompts with OTel |
| `otel.exporter.<id>.endpoint` | string | Exporter endpoint |
| `otel.exporter.<id>.protocol` | `binary` \| `json` | OTLP protocol |
| `otel.exporter.<id>.headers` | map | Static headers |
| `otel.exporter.<id>.tls.*` | string | CA, client cert, private key paths |

### Misc

| Key | Type | Description |
|-----|------|-------------|
| `notify` | string[] | Notification command (receives JSON) |
| `check_for_update_on_startup` | boolean | Update check (default: true) |
| `feedback.enabled` | boolean | `/feedback` submission (default: true) |
| `analytics.enabled` | boolean | Analytics enablement |
| `instructions` | string | **Reserved** — use `model_instructions_file` or `AGENTS.md` |
| `developer_instructions` | string | Additional dev instructions |
| `model_instructions_file` | string (path) | Replace built-in instructions |
| `personality` | `none` \| `friendly` \| `pragmatic` | Communication style |
| `service_tier` | `flex` \| `fast` | Preferred service tier |
| `experimental_compact_prompt_file` | string (path) | Compaction prompt file (experimental) |
| `file_opener` | `vscode` \| `vscode-insiders` \| `windsurf` \| `cursor` \| `none` | `vscode` | URI scheme for citations |
| `hide_agent_reasoning` | boolean | Suppress reasoning events |
| `show_raw_agent_reasoning` | boolean | Show raw reasoning content |
| `disable_paste_burst` | boolean | Disable burst-paste detection |
| `cli_auth_credentials_store` | `file` \| `keyring` \| `auto` | Credential storage |
| `mcp_oauth_credentials_store` | `auto` \| `file` \| `keyring` | MCP OAuth store |
| `mcp_oauth_callback_port` | integer | Fixed OAuth callback port |
| `mcp_oauth_callback_url` | string | Redirect URI override |
| `projects.<path>.trust_level` | `trusted` \| `untrusted` | Project trust status |
| `notice.*` | boolean | Acknowledgement tracking flags |
| `forced_login_method` | `chatgpt` \| `api` | Restrict auth method |
| `forced_chatgpt_workspace_id` | uuid | Limit to specific workspace |

> ⚠️ Rename `experimental_instructions_file` → `model_instructions_file`. The old key is deprecated.

## `requirements.toml`

Admin-enforced constraints. Users cannot override these. See [[036-security-threat-model|Security Threat Model]] for precedence details.

| Key | Type | Description |
|-----|------|-------------|
| `allowed_approval_policies` | string[] | Permitted `approval_policy` values |
| `allowed_approvals_reviewers` | string[] | Permitted `approvals_reviewer` values |
| `guardian_policy_config` | string | Managed auto-review policy (precedence over local) |
| `allowed_sandbox_modes` | string[] | Permitted `sandbox_mode` values |
| `remote_sandbox_config` | table[] | Host-specific sandbox requirements |
| `remote_sandbox_config[].hostname_patterns` | string[] | Case-insensitive patterns (`*`, `?`) |
| `remote_sandbox_config[].allowed_sandbox_modes` | string[] | Allowed modes for matched hosts |
| `allowed_web_search_modes` | string[] | Permitted `web_search` values |
| `features.<name>` | boolean | Pin feature flags |
| `features.in_app_browser` | boolean | Disable in-app browser pane |
| `features.browser_use` | boolean | Disable Browser Use / Browser Agent |
| `features.computer_use` | boolean | Disable Computer Use |
| `hooks` | table | Admin-enforced lifecycle hooks |
| `hooks.managed_dir` | string (abs path) | Hook scripts directory (macOS/Linux) |
| `hooks.windows_managed_dir` | string (abs path) | Hook scripts directory (Windows) |
| `hooks.<Event>` | table[] | Matcher groups for events |
| `hooks.<Event>[].hooks` | table[] | Command hook handlers |
| `permissions.filesystem.deny_read` | string[] | Admin read denials (paths/globs) |
| `mcp_servers` | table | Allowlist of MCP servers |
| `mcp_servers.<id>.identity.command` | string | Allowed stdio command |
| `mcp_servers.<id>.identity.url` | string | Allowed HTTP URL |
| `rules` | table | Admin command rules (merged with `.rules` files) |
| `rules.prefix_rules` | table[] | Prefix rules with `pattern` + `decision` |
| `rules.prefix_rules[].pattern` | table[] | Tokens: `token` or `any_of` |
| `rules.prefix_rules[].decision` | `prompt` \| `forbidden` | Only `prompt` or `forbidden` allowed |
| `rules.prefix_rules[].justification` | string | Rationale for prompt/rejection |

## Related

- [[066-cli-reference|CLI Reference]]
- [[015-cli|Codex CLI Overview]]
- [[016-cloud|Codex Cloud]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/config-reference.md)*
