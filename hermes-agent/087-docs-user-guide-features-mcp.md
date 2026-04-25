---
title: MCP (Model Context Protocol) | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
source: crawler
fetched_at: 2026-04-24T17:00:03.185545494-03:00
rendered_js: false
word_count: 1464
summary: This document explains the Model Context Protocol (MCP), detailing how Hermes Agent connects to external tool servers and providing configuration guides on setting up both local stdio and remote HTTP MCP servers.
tags:
    - mcp-protocol
    - hermes-agent
    - tool-integration
    - config-guide
    - stdio-servers
    - http-server
category: reference
---

MCP lets Hermes Agent connect to external tool servers so the agent can use tools that live outside Hermes itself — GitHub, databases, file systems, browser stacks, internal APIs, and more.

If you have ever wanted Hermes to use a tool that already exists somewhere else, MCP is usually the cleanest way to do it.

## What MCP gives you[​](#what-mcp-gives-you "Direct link to What MCP gives you")

- Access to external tool ecosystems without writing a native Hermes tool first
- Local stdio servers and remote HTTP MCP servers in the same config
- Automatic tool discovery and registration at startup
- Utility wrappers for MCP resources and prompts when supported by the server
- Per-server filtering so you can expose only the MCP tools you actually want Hermes to see

## Quick start[​](#quick-start "Direct link to Quick start")

1. Install MCP support (already included if you used the standard install script):

```bash
cd ~/.hermes/hermes-agent
uv pip install-e".[mcp]"
```

2. Add an MCP server to `~/.hermes/config.yaml`:

```yaml
mcp_servers:
filesystem:
command:"npx"
args:["-y","@modelcontextprotocol/server-filesystem","/home/user/projects"]
```

3. Start Hermes:

<!--THE END-->

4. Ask Hermes to use the MCP-backed capability.

For example:

```text
List the files in /home/user/projects and summarize the repo structure.
```

Hermes will discover the MCP server's tools and use them like any other tool.

## Two kinds of MCP servers[​](#two-kinds-of-mcp-servers "Direct link to Two kinds of MCP servers")

### Stdio servers[​](#stdio-servers "Direct link to Stdio servers")

Stdio servers run as local subprocesses and talk over stdin/stdout.

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
```

Use stdio servers when:

- the server is installed locally
- you want low-latency access to local resources
- you are following MCP server docs that show `command`, `args`, and `env`

### HTTP servers[​](#http-servers "Direct link to HTTP servers")

HTTP MCP servers are remote endpoints Hermes connects to directly.

```yaml
mcp_servers:
remote_api:
url:"https://mcp.example.com/mcp"
headers:
Authorization:"Bearer ***"
```

Use HTTP servers when:

- the MCP server is hosted elsewhere
- your organization exposes internal MCP endpoints
- you do not want Hermes spawning a local subprocess for that integration

## Basic configuration reference[​](#basic-configuration-reference "Direct link to Basic configuration reference")

Hermes reads MCP config from `~/.hermes/config.yaml` under `mcp_servers`.

### Common keys[​](#common-keys "Direct link to Common keys")

KeyTypeMeaning`command`stringExecutable for a stdio MCP server`args`listArguments for the stdio server`env`mappingEnvironment variables passed to the stdio server`url`stringHTTP MCP endpoint`headers`mappingHTTP headers for remote servers`timeout`numberTool call timeout`connect_timeout`numberInitial connection timeout`enabled`boolIf `false`, Hermes skips the server entirely`tools`mappingPer-server tool filtering and utility policy

### Minimal stdio example[​](#minimal-stdio-example "Direct link to Minimal stdio example")

```yaml
mcp_servers:
filesystem:
command:"npx"
args:["-y","@modelcontextprotocol/server-filesystem","/tmp"]
```

### Minimal HTTP example[​](#minimal-http-example "Direct link to Minimal HTTP example")

```yaml
mcp_servers:
company_api:
url:"https://mcp.internal.example.com"
headers:
Authorization:"Bearer ***"
```

Hermes prefixes MCP tools so they do not collide with built-in names:

```text
mcp_<server_name>_<tool_name>
```

Examples:

ServerMCP toolRegistered name`filesystem``read_file``mcp_filesystem_read_file``github``create-issue``mcp_github_create_issue``my-api``query.data``mcp_my_api_query_data`

In practice, you usually do not need to call the prefixed name manually — Hermes sees the tool and chooses it during normal reasoning.

When supported, Hermes also registers utility tools around MCP resources and prompts:

- `list_resources`
- `read_resource`
- `list_prompts`
- `get_prompt`

These are registered per server with the same prefix pattern, for example:

- `mcp_github_list_resources`
- `mcp_github_get_prompt`

### Important[​](#important "Direct link to Important")

These utility tools are now capability-aware:

- Hermes only registers resource utilities if the MCP session actually supports resource operations
- Hermes only registers prompt utilities if the MCP session actually supports prompt operations

So a server that exposes callable tools but no resources/prompts will not get those extra wrappers.

## Per-server filtering[​](#per-server-filtering "Direct link to Per-server filtering")

You can control which tools each MCP server contributes to Hermes, allowing fine-grained management of your tool namespace.

### Disable a server entirely[​](#disable-a-server-entirely "Direct link to Disable a server entirely")

```yaml
mcp_servers:
legacy:
url:"https://mcp.legacy.internal"
enabled:false
```

If `enabled: false`, Hermes skips the server completely and does not even attempt a connection.

### Whitelist server tools[​](#whitelist-server-tools "Direct link to Whitelist server tools")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[create_issue, list_issues]
```

Only those MCP server tools are registered.

### Blacklist server tools[​](#blacklist-server-tools "Direct link to Blacklist server tools")

```yaml
mcp_servers:
stripe:
url:"https://mcp.stripe.com"
tools:
exclude:[delete_customer]
```

All server tools are registered except the excluded ones.

### Precedence rule[​](#precedence-rule "Direct link to Precedence rule")

If both are present:

```yaml
tools:
include:[create_issue]
exclude:[create_issue, delete_issue]
```

`include` wins.

### Filter utility tools too[​](#filter-utility-tools-too "Direct link to Filter utility tools too")

You can also separately disable Hermes-added utility wrappers:

```yaml
mcp_servers:
docs:
url:"https://mcp.docs.example.com"
tools:
prompts:false
resources:false
```

That means:

- `tools.resources: false` disables `list_resources` and `read_resource`
- `tools.prompts: false` disables `list_prompts` and `get_prompt`

### Full example[​](#full-example "Direct link to Full example")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[create_issue, list_issues, search_code]
prompts:false

stripe:
url:"https://mcp.stripe.com"
headers:
Authorization:"Bearer ***"
tools:
exclude:[delete_customer]
resources:false

legacy:
url:"https://mcp.legacy.internal"
enabled:false
```

## What happens if everything is filtered out?[​](#what-happens-if-everything-is-filtered-out "Direct link to What happens if everything is filtered out?")

If your config filters out all callable tools and disables or omits all supported utilities, Hermes does not create an empty runtime MCP toolset for that server.

That keeps the tool list clean.

## Runtime behavior[​](#runtime-behavior "Direct link to Runtime behavior")

### Discovery time[​](#discovery-time "Direct link to Discovery time")

Hermes discovers MCP servers at startup and registers their tools into the normal tool registry.

### Dynamic Tool Discovery[​](#dynamic-tool-discovery "Direct link to Dynamic Tool Discovery")

MCP servers can notify Hermes when their available tools change at runtime by sending a `notifications/tools/list_changed` notification. When Hermes receives this notification, it automatically re-fetches the server's tool list and updates the registry — no manual `/reload-mcp` required.

This is useful for MCP servers whose capabilities change dynamically (e.g. a server that adds tools when a new database schema is loaded, or removes tools when a service goes offline).

The refresh is lock-protected so rapid-fire notifications from the same server don't cause overlapping refreshes. Prompt and resource change notifications (`prompts/list_changed`, `resources/list_changed`) are received but not yet acted on.

### Reloading[​](#reloading "Direct link to Reloading")

If you change MCP config, use:

This reloads MCP servers from config and refreshes the available tool list. For runtime tool changes pushed by the server itself, see [Dynamic Tool Discovery](#dynamic-tool-discovery) above.

### Toolsets[​](#toolsets "Direct link to Toolsets")

Each configured MCP server also creates a runtime toolset when it contributes at least one registered tool:

That makes MCP servers easier to reason about at the toolset level.

## Security model[​](#security-model "Direct link to Security model")

### Stdio env filtering[​](#stdio-env-filtering "Direct link to Stdio env filtering")

For stdio servers, Hermes does not blindly pass your full shell environment.

Only explicitly configured `env` plus a safe baseline are passed through. This reduces accidental secret leakage.

### Config-level exposure control[​](#config-level-exposure-control "Direct link to Config-level exposure control")

The new filtering support is also a security control:

- disable dangerous tools you do not want the model to see
- expose only a minimal whitelist for a sensitive server
- disable resource/prompt wrappers when you do not want that surface exposed

## Example use cases[​](#example-use-cases "Direct link to Example use cases")

### GitHub server with a minimal issue-management surface[​](#github-server-with-a-minimal-issue-management-surface "Direct link to GitHub server with a minimal issue-management surface")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[list_issues, create_issue, update_issue]
prompts:false
resources:false
```

Use it like:

```text
Show me open issues labeled bug, then draft a new issue for the flaky MCP reconnection behavior.
```

### Stripe server with dangerous actions removed[​](#stripe-server-with-dangerous-actions-removed "Direct link to Stripe server with dangerous actions removed")

```yaml
mcp_servers:
stripe:
url:"https://mcp.stripe.com"
headers:
Authorization:"Bearer ***"
tools:
exclude:[delete_customer, refund_payment]
```

Use it like:

```text
Look up the last 10 failed payments and summarize common failure reasons.
```

### Filesystem server for a single project root[​](#filesystem-server-for-a-single-project-root "Direct link to Filesystem server for a single project root")

```yaml
mcp_servers:
project_fs:
command:"npx"
args:["-y","@modelcontextprotocol/server-filesystem","/home/user/my-project"]
```

Use it like:

```text
Inspect the project root and explain the directory layout.
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### MCP server not connecting[​](#mcp-server-not-connecting "Direct link to MCP server not connecting")

Check:

```bash
# Verify MCP deps are installed (already included in standard install)
cd ~/.hermes/hermes-agent && uv pip install-e".[mcp]"

node--version
npx --version
```

Then verify your config and restart Hermes.

### Tools not appearing[​](#tools-not-appearing "Direct link to Tools not appearing")

Possible causes:

- the server failed to connect
- discovery failed
- your filter config excluded the tools
- the utility capability does not exist on that server
- the server is disabled with `enabled: false`

If you are intentionally filtering, this is expected.

### Why didn't resource or prompt utilities appear?[​](#why-didnt-resource-or-prompt-utilities-appear "Direct link to Why didn't resource or prompt utilities appear?")

Because Hermes now only registers those wrappers when both are true:

1. your config allows them
2. the server session actually supports the capability

This is intentional and keeps the tool list honest.

## MCP Sampling Support[​](#mcp-sampling-support "Direct link to MCP Sampling Support")

MCP servers can request LLM inference from Hermes via the `sampling/createMessage` protocol. This allows an MCP server to ask Hermes to generate text on its behalf — useful for servers that need LLM capabilities but don't have their own model access.

Sampling is **enabled by default** for all MCP servers (when the MCP SDK supports it). Configure it per-server under the `sampling` key:

```yaml
mcp_servers:
my_server:
command:"my-mcp-server"
sampling:
enabled:true# Enable sampling (default: true)
model:"openai/gpt-4o"# Override model for sampling requests (optional)
max_tokens_cap:4096# Max tokens per sampling response (default: 4096)
timeout:30# Timeout in seconds per request (default: 30)
max_rpm:10# Rate limit: max requests per minute (default: 10)
max_tool_rounds:5# Max tool-use rounds in sampling loops (default: 5)
allowed_models:[]# Allowlist of model names the server may request (empty = any)
log_level:"info"# Audit log level: debug, info, or warning (default: info)
```

The sampling handler includes a sliding-window rate limiter, per-request timeouts, and tool-loop depth limits to prevent runaway usage. Metrics (request count, errors, tokens used) are tracked per server instance.

To disable sampling for a specific server:

```yaml
mcp_servers:
untrusted_server:
url:"https://mcp.example.com"
sampling:
enabled:false
```

## Running Hermes as an MCP server[​](#running-hermes-as-an-mcp-server "Direct link to Running Hermes as an MCP server")

In addition to connecting **to** MCP servers, Hermes can also **be** an MCP server. This lets other MCP-capable agents (Claude Code, Cursor, Codex, or any MCP client) use Hermes's messaging capabilities — list conversations, read message history, and send messages across all your connected platforms.

### When to use this[​](#when-to-use-this "Direct link to When to use this")

- You want Claude Code, Cursor, or another coding agent to send and read Telegram/Discord/Slack messages through Hermes
- You want a single MCP server that bridges to all of Hermes's connected messaging platforms at once
- You already have a running Hermes gateway with connected platforms

### Quick start[​](#quick-start-1 "Direct link to Quick start")

This starts a stdio MCP server. The MCP client (not you) manages the process lifecycle.

### MCP client configuration[​](#mcp-client-configuration "Direct link to MCP client configuration")

Add Hermes to your MCP client config. For example, in Claude Code's `~/.claude/claude_desktop_config.json`:

```json
{
"mcpServers":{
"hermes":{
"command":"hermes",
"args":["mcp","serve"]
}
}
}
```

Or if you installed Hermes in a specific location:

```json
{
"mcpServers":{
"hermes":{
"command":"/home/user/.hermes/hermes-agent/venv/bin/hermes",
"args":["mcp","serve"]
}
}
}
```

### Available tools[​](#available-tools "Direct link to Available tools")

The MCP server exposes 10 tools, matching OpenClaw's channel bridge surface plus a Hermes-specific channel browser:

ToolDescription`conversations_list`List active messaging conversations. Filter by platform or search by name.`conversation_get`Get detailed info about one conversation by session key.`messages_read`Read recent message history for a conversation.`attachments_fetch`Extract non-text attachments (images, media) from a specific message.`events_poll`Poll for new conversation events since a cursor position.`events_wait`Long-poll / block until the next event arrives (near-real-time).`messages_send`Send a message through a platform (e.g. `telegram:123456`, `discord:#general`).`channels_list`List available messaging targets across all platforms.`permissions_list_open`List pending approval requests observed during this bridge session.`permissions_respond`Allow or deny a pending approval request.

### Event system[​](#event-system "Direct link to Event system")

The MCP server includes a live event bridge that polls Hermes's session database for new messages. This gives MCP clients near-real-time awareness of incoming conversations:

```text
# Poll for new events (non-blocking)
events_poll(after_cursor=0)

# Wait for next event (blocks up to timeout)
events_wait(after_cursor=42, timeout_ms=30000)
```

Event types: `message`, `approval_requested`, `approval_resolved`

The event queue is in-memory and starts when the bridge connects. Older messages are available through `messages_read`.

### Options[​](#options "Direct link to Options")

```bash
hermes mcp serve              # Normal mode
hermes mcp serve --verbose# Debug logging on stderr
```

### How it works[​](#how-it-works "Direct link to How it works")

The MCP server reads conversation data directly from Hermes's session store (`~/.hermes/sessions/sessions.json` and the SQLite database). A background thread polls the database for new messages and maintains an in-memory event queue. For sending messages, it uses the same `send_message` infrastructure as the Hermes agent itself.

The gateway does NOT need to be running for read operations (listing conversations, reading history, polling events). It DOES need to be running for send operations, since the platform adapters need active connections.

### Current limits[​](#current-limits "Direct link to Current limits")

- Stdio transport only (no HTTP MCP transport yet)
- Event polling at ~200ms intervals via mtime-optimized DB polling (skips work when files are unchanged)
- No `claude/channel` push notification protocol yet
- Text-only sends (no media/attachment sending through `messages_send`)

<!--THE END-->

- [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)
- [CLI Commands](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [Slash Commands](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)
- [FAQ](https://hermes-agent.nousresearch.com/docs/reference/faq)