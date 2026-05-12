---
title: Sample Configuration
url: https://developers.openai.com/codex/config-sample.md
source: llms
fetched_at: 2026-04-30T10:15:29.770029606-03:00
rendered_js: false
word_count: 49
summary: This document provides a template and reference guide for the Codex configuration file, outlining the available keys, default behaviors, and recommended settings for user environments.
tags:
    - configuration
    - codex
    - toml
    - setup
    - reference
    - environment-variables
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Sample Configuration

Starting point for `config.toml`. Includes most keys Codex reads, with defaults, recommended values, and short notes.

For explanations: [[055-config-basic|Config basics]], [[054-config-advanced|Advanced Config]], [[067-config-reference|Configuration Reference]], [[041-agent-approvals-security#sandbox-and-approvals|Sandbox and approvals]], [[018-enterprise-managed-configuration|Managed configuration]].

Copy only the keys you need into `~/.codex/config.toml` (or project-scoped `.codex/config.toml`), then adjust.

```toml
# Core Model Selection
model = "gpt-5.5"
# personality = "pragmatic"           # none | friendly | pragmatic
# review_model = "gpt-5.5"            # Override for /review
model_provider = "openai"
# oss_provider = "ollama"             # Default for --oss
# service_tier = "flex"               # fast | flex
# model_context_window = 128000
# model_auto_compact_token_limit = 64000
# tool_output_token_limit = 12000
# model_catalog_json = "/absolute/path/to/models.json"
# background_terminal_max_timeout = 300000  # ms; default 5m
# log_dir = "/absolute/path/to/codex-logs"
# sqlite_home = "/absolute/path/to/codex-state"

# Reasoning & Verbosity (Responses API capable models)
# model_reasoning_effort = "medium"   # minimal | low | medium | high | xhigh
# plan_mode_reasoning_effort = "high"
# model_reasoning_summary = "auto"    # auto | concise | detailed | none
# model_verbosity = "medium"          # low | medium | high
# model_supports_reasoning_summaries = true

# Instruction Overrides
# developer_instructions = ""           # Injected before AGENTS.md
# compact_prompt = ""                   # Inline override for history compaction prompt
# commit_attribution = "Jane Doe <jane@example.com>"
# model_instructions_file = "/path/to/instructions.txt"
# experimental_compact_prompt_file = "/path/to/compact_prompt.txt"

# Notifications
# notify = ["notify-send", "Codex"]   # External notifier program

# Approval & Sandbox
approval_policy = "on-request"        # untrusted | on-request | never | granular
# approvals_reviewer = "user"         # user | auto_review
# allow_login_shell = true
sandbox_mode = "read-only"            # read-only | workspace-write | danger-full-access
# default_permissions = "workspace"

# Example granular policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

# Example filesystem profile:
# [permissions.workspace.filesystem]
# glob_scan_max_depth = 3
# ":project_roots" = { "." = "write", "**/*.env" = "none" }
# "/absolute/path/to/secrets" = "none"

# Authentication & Login
cli_auth_credentials_store = "file"   # file | keyring | auto
chatgpt_base_url = "https://chatgpt.com/backend-api/"
# openai_base_url = "https://us.api.openai.com/v1"
# forced_chatgpt_workspace_id = "..."
# forced_login_method = "chatgpt"     # chatgpt | api
mcp_oauth_credentials_store = "auto"  # auto | file | keyring
# mcp_oauth_callback_port = 4321
# mcp_oauth_callback_url = "https://devbox.example.internal/callback"

# Project Documentation Controls
project_doc_max_bytes = 32768
project_doc_fallback_filenames = []
# project_root_markers = [".git"]

# History & File Opener
file_opener = "vscode"                # vscode | vscode-insiders | windsurf | cursor | none

# UI, Notifications, Misc
hide_agent_reasoning = false
show_raw_agent_reasoning = false
disable_paste_burst = false
windows_wsl_setup_acknowledged = false
check_for_update_on_startup = true

# Web Search
web_search = "cached"                 # disabled | cached | live
# profile = "default"
# suppress_unstable_features_warning = true

# Agents (multi-agent roles and limits)
[agents]
# max_threads = 6
# max_depth = 1
# job_max_runtime_seconds = 1800
# [agents.reviewer]
# description = "Find correctness, security, and test risks."
# config_file = "./agents/reviewer.toml"
# nickname_candidates = ["Athena", "Ada"]

# Skills (per-skill overrides)
# [[skills.config]]
# path = "/path/to/skill/SKILL.md"
# enabled = false

# Sandbox settings (tables)
[sandbox_workspace_write]
writable_roots = []
network_access = false
exclude_tmpdir_env_var = false
exclude_slash_tmp = false

# Shell Environment Policy
[shell_environment_policy]
inherit = "all"                       # all | core | none
ignore_default_excludes = false
exclude = []
set = {}
include_only = []
# experimental_use_profile = false

# Managed network proxy settings
# [permissions.workspace.network]
# enabled = true
# proxy_url = "http://127.0.0.1:43128"
# admin_url = "http://127.0.0.1:43129"
# enable_socks5 = false
# socks_url = "http://127.0.0.1:43130"
# mode = "limited"                    # limited | full
# [permissions.workspace.network.domains]
# "api.openai.com" = "allow"
# "example.com" = "deny"
# [permissions.workspace.network.unix_sockets]
# "/var/run/docker.sock" = "allow"

# History
[history]
persistence = "save-all"              # save-all | none
# max_bytes = 5242880

# UI, Notifications, Misc (tables)
[tui]
notifications = false                 # boolean or filtered list
# notification_method = "auto"        # auto | osc9 | bel
# notification_condition = "unfocused" # unfocused | always
animations = true
show_tooltips = true
# alternate_screen = "auto"
# status_line = ["model-with-reasoning", "context-remaining", "current-dir"]
# terminal_title = ["spinner", "project"]
# theme = "catppuccin-mocha"

[analytics]
enabled = true

[feedback]
enabled = true

# Feature flags
[features]
# shell_tool = true
# apps = false
# codex_hooks = false
# unified_exec = true
# shell_snapshot = true
# multi_agent = true
# personality = true
# fast_mode = true

# Memories
# [memories]
# generate_memories = true
# use_memories = true
# disable_on_external_context = false

# Lifecycle hooks (inline or sibling hooks.json)
# [[hooks.PreToolUse]]
# matcher = "^Bash$"
# [[hooks.PreToolUse.hooks]]
# type = "command"
# command = 'python3 "/absolute/path/to/pre_tool_use_policy.py"'
# timeout = 30
# statusMessage = "Checking Bash command"

# MCP servers
[mcp_servers]
# [mcp_servers.docs]
# enabled = true
# required = true
# command = "docs-server"
# args = ["--port", "4000"]
# env = { "API_KEY" = "value" }
# env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]
# cwd = "/path/to/server"
# startup_timeout_sec = 10.0
# tool_timeout_sec = 60.0
# enabled_tools = ["search", "summarize"]
# disabled_tools = ["slow-tool"]
# scopes = ["read:docs"]
# oauth_resource = "https://docs.example.com/"

# [mcp_servers.github]
# enabled = true
# required = true
# url = "https://github-mcp.example.com/mcp"
# bearer_token_env_var = "GITHUB_TOKEN"
# http_headers = { "X-Example" = "value" }
# env_http_headers = { "X-Auth" = "AUTH_ENV" }
# startup_timeout_sec = 10.0
# tool_timeout_sec = 60.0

# Model Providers
[model_providers]
# [model_providers.openaidr]
# name = "OpenAI Data Residency"
# base_url = "https://us.api.openai.com/v1"
# wire_api = "responses"
# requires_openai_auth = true
# request_max_retries = 4
# stream_max_retries = 5
# stream_idle_timeout_ms = 300000
# supports_websockets = true
# http_headers = { "X-Example" = "value" }
# env_http_headers = { "OpenAI-Organization" = "OPENAI_ORGANIZATION" }

# [model_providers.azure]
# name = "Azure"
# base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
# wire_api = "responses"
# query_params = { api-version = "2025-04-01-preview" }
# env_key = "AZURE_OPENAI_API_KEY"
# supports_websockets = false

# [model_providers.proxy]
# name = "OpenAI using LLM proxy"
# base_url = "https://proxy.example.com/v1"
# wire_api = "responses"
# [model_providers.proxy.auth]
# command = "/usr/local/bin/fetch-codex-token"
# args = ["--audience", "codex"]
# timeout_ms = 5000
# refresh_interval_ms = 300000

# [model_providers.local_ollama]
# name = "Ollama"
# base_url = "http://localhost:11434/v1"
# wire_api = "responses"

# Apps / Connectors
[apps]
# [apps._default]
# enabled = true
# destructive_enabled = true
# open_world_enabled = true
# [apps.google_drive]
# enabled = false
# destructive_enabled = false
# default_tools_enabled = true
# default_tools_approval_mode = "prompt"  # auto | prompt | approve
# [apps.google_drive.tools."files/delete"]
# enabled = false
# approval_mode = "approve"

# [tool_suggest]
# discoverables = [
#   { type = "connector", id = "gmail" },
#   { type = "plugin", id = "figma@openai-curated" },
# ]

# Profiles
[profiles]
# [profiles.default]
# model = "gpt-5.4"
# approval_policy = "on-request"
# sandbox_mode = "read-only"
# personality = "pragmatic"
# model_catalog_json = "./models.json"

# Projects (trust levels)
[projects]
# [projects."/absolute/path/to/project"]
# trust_level = "trusted"  # trusted | untrusted

# Tools
[tools]
# view_image = true

# OpenTelemetry
[otel]
log_user_prompt = false
environment = "dev"
exporter = "none"
trace_exporter = "none"
metrics_exporter = "statsig"
# [otel.exporter."otlp-http"]
# endpoint = "https://otel.example.com/v1/logs"
# protocol = "binary"
# [otel.exporter."otlp-http".headers]
# "x-otlp-api-key" = "${OTLP_TOKEN}"
# [otel.exporter."otlp-http".tls]
# ca-certificate = "certs/otel-ca.pem"
# [otel.trace_exporter."otlp-grpc"]
# endpoint = "https://otel.example.com:4317"
# headers = { "x-otlp-meta" = "abc123" }

# Windows
[windows]
sandbox = "unelevated"                # unelevated | elevated
```

#configuration #reference #toml #codex