---
title: Use MCP with Hermes | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes
source: crawler
fetched_at: 2026-04-24T17:00:03.516875915-03:00
rendered_js: false
word_count: 859
summary: This guide details how to practically utilize the Model Context Protocol (MCP) with Hermes Agent in daily workflows. It explains when and why to use MCP, provides setup instructions, and offers various patterns for configuring server connections with granular filtering controls.
tags:
    - mcp-guide
    - hermes-agent
    - tooling-integration
    - adapter-layer
    - server-configuration
    - workflow-tutorial
category: tutorial
---

This guide shows how to actually use MCP with Hermes Agent in day-to-day workflows.

If the feature page explains what MCP is, this guide is about how to get value from it quickly and safely.

## When should you use MCP?[​](#when-should-you-use-mcp "Direct link to When should you use MCP?")

Use MCP when:

- a tool already exists in MCP form and you do not want to build a native Hermes tool
- you want Hermes to operate against a local or remote system through a clean RPC layer
- you want fine-grained per-server exposure control
- you want to connect Hermes to internal APIs, databases, or company systems without modifying Hermes core

Do not use MCP when:

- a built-in Hermes tool already solves the job well
- the server exposes a huge dangerous tool surface and you are not prepared to filter it
- you only need one very narrow integration and a native tool would be simpler and safer

## Mental model[​](#mental-model "Direct link to Mental model")

Think of MCP as an adapter layer:

- Hermes remains the agent
- MCP servers contribute tools
- Hermes discovers those tools at startup or reload time
- the model can use them like normal tools
- you control how much of each server is visible

That last part matters. Good MCP usage is not just “connect everything.” It is “connect the right thing, with the smallest useful surface.”

## Step 1: install MCP support[​](#step-1-install-mcp-support "Direct link to Step 1: install MCP support")

If you installed Hermes with the standard install script, MCP support is already included (the installer runs `uv pip install -e ".[all]"`).

If you installed without extras and need to add MCP separately:

```bash
cd ~/.hermes/hermes-agent
uv pip install-e".[mcp]"
```

For npm-based servers, make sure Node.js and `npx` are available.

For many Python MCP servers, `uvx` is a nice default.

## Step 2: add one server first[​](#step-2-add-one-server-first "Direct link to Step 2: add one server first")

Start with a single, safe server.

Example: filesystem access to one project directory only.

```yaml
mcp_servers:
project_fs:
command:"npx"
args:["-y","@modelcontextprotocol/server-filesystem","/home/user/my-project"]
```

Then start Hermes:

Now ask something concrete:

```text
Inspect this project and summarize the repo layout.
```

## Step 3: verify MCP loaded[​](#step-3-verify-mcp-loaded "Direct link to Step 3: verify MCP loaded")

You can verify MCP in a few ways:

- Hermes banner/status should show MCP integration when configured
- ask Hermes what tools it has available
- use `/reload-mcp` after config changes
- check logs if the server failed to connect

A practical test prompt:

```text
Tell me which MCP-backed tools are available right now.
```

Do not wait until later if the server exposes a lot of tools.

### Example: whitelist only what you want[​](#example-whitelist-only-what-you-want "Direct link to Example: whitelist only what you want")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[list_issues, create_issue, search_code]
```

This is usually the best default for sensitive systems.

### Example: blacklist dangerous actions[​](#example-blacklist-dangerous-actions "Direct link to Example: blacklist dangerous actions")

```yaml
mcp_servers:
stripe:
url:"https://mcp.stripe.com"
headers:
Authorization:"Bearer ***"
tools:
exclude:[delete_customer, refund_payment]
```

### Example: disable utility wrappers too[​](#example-disable-utility-wrappers-too "Direct link to Example: disable utility wrappers too")

```yaml
mcp_servers:
docs:
url:"https://mcp.docs.example.com"
tools:
prompts:false
resources:false
```

## What does filtering actually affect?[​](#what-does-filtering-actually-affect "Direct link to What does filtering actually affect?")

There are two categories of MCP-exposed functionality in Hermes:

1. Server-native MCP tools

<!--THE END-->

- filtered with:
  
  - `tools.include`
  - `tools.exclude`

<!--THE END-->

2. Hermes-added utility wrappers

<!--THE END-->

- filtered with:
  
  - `tools.resources`
  - `tools.prompts`

### Utility wrappers you may see[​](#utility-wrappers-you-may-see "Direct link to Utility wrappers you may see")

Resources:

- `list_resources`
- `read_resource`

Prompts:

- `list_prompts`
- `get_prompt`

These wrappers only appear if:

- your config allows them, and
- the MCP server session actually supports those capabilities

So Hermes will not pretend a server has resources/prompts if it does not.

## Common patterns[​](#common-patterns "Direct link to Common patterns")

### Pattern 1: local project assistant[​](#pattern-1-local-project-assistant "Direct link to Pattern 1: local project assistant")

Use MCP for a repo-local filesystem or git server when you want Hermes to reason over a bounded workspace.

```yaml
mcp_servers:
fs:
command:"npx"
args:["-y","@modelcontextprotocol/server-filesystem","/home/user/project"]

git:
command:"uvx"
args:["mcp-server-git","--repository","/home/user/project"]
```

Good prompts:

```text
Review the project structure and identify where configuration lives.
```

```text
Check the local git state and summarize what changed recently.
```

### Pattern 2: GitHub triage assistant[​](#pattern-2-github-triage-assistant "Direct link to Pattern 2: GitHub triage assistant")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[list_issues, create_issue, update_issue, search_code]
prompts:false
resources:false
```

Good prompts:

```text
List open issues about MCP, cluster them by theme, and draft a high-quality issue for the most common bug.
```

```text
Search the repo for uses of _discover_and_register_server and explain how MCP tools are registered.
```

### Pattern 3: internal API assistant[​](#pattern-3-internal-api-assistant "Direct link to Pattern 3: internal API assistant")

```yaml
mcp_servers:
internal_api:
url:"https://mcp.internal.example.com"
headers:
Authorization:"Bearer ***"
tools:
include:[list_customers, get_customer, list_invoices]
resources:false
prompts:false
```

Good prompts:

```text
Look up customer ACME Corp and summarize recent invoice activity.
```

This is the sort of place where a strict whitelist is far better than an exclude list.

### Pattern 4: documentation / knowledge servers[​](#pattern-4-documentation--knowledge-servers "Direct link to Pattern 4: documentation / knowledge servers")

Some MCP servers expose prompts or resources that are more like shared knowledge assets than direct actions.

```yaml
mcp_servers:
docs:
url:"https://mcp.docs.example.com"
tools:
prompts:true
resources:true
```

Good prompts:

```text
List available MCP resources from the docs server, then read the onboarding guide and summarize it.
```

```text
List prompts exposed by the docs server and tell me which ones would help with incident response.
```

## Tutorial: end-to-end setup with filtering[​](#tutorial-end-to-end-setup-with-filtering "Direct link to Tutorial: end-to-end setup with filtering")

Here is a practical progression.

### Phase 1: add GitHub MCP with a tight whitelist[​](#phase-1-add-github-mcp-with-a-tight-whitelist "Direct link to Phase 1: add GitHub MCP with a tight whitelist")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[list_issues, create_issue, search_code]
prompts:false
resources:false
```

Start Hermes and ask:

```text
Search the codebase for references to MCP and summarize the main integration points.
```

### Phase 2: expand only when needed[​](#phase-2-expand-only-when-needed "Direct link to Phase 2: expand only when needed")

If you later need issue updates too:

```yaml
tools:
include:[list_issues, create_issue, update_issue, search_code]
```

Then reload:

### Phase 3: add a second server with different policy[​](#phase-3-add-a-second-server-with-different-policy "Direct link to Phase 3: add a second server with different policy")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[list_issues, create_issue, update_issue, search_code]
prompts:false
resources:false

filesystem:
command:"npx"
args:["-y","@modelcontextprotocol/server-filesystem","/home/user/project"]
```

Now Hermes can combine them:

```text
Inspect the local project files, then create a GitHub issue summarizing the bug you find.
```

That is where MCP gets powerful: multi-system workflows without changing Hermes core.

## Safe usage recommendations[​](#safe-usage-recommendations "Direct link to Safe usage recommendations")

### Prefer allowlists for dangerous systems[​](#prefer-allowlists-for-dangerous-systems "Direct link to Prefer allowlists for dangerous systems")

For anything financial, customer-facing, or destructive:

- use `tools.include`
- start with the smallest set possible

### Disable unused utilities[​](#disable-unused-utilities "Direct link to Disable unused utilities")

If you do not want the model browsing server-provided resources/prompts, turn them off:

```yaml
tools:
resources:false
prompts:false
```

### Keep servers scoped narrowly[​](#keep-servers-scoped-narrowly "Direct link to Keep servers scoped narrowly")

Examples:

- filesystem server rooted to one project dir, not your whole home directory
- git server pointed at one repo
- internal API server with read-heavy tool exposure by default

### Reload after config changes[​](#reload-after-config-changes "Direct link to Reload after config changes")

Do this after changing:

- include/exclude lists
- enabled flags
- resources/prompts toggles
- auth headers / env

## Troubleshooting by symptom[​](#troubleshooting-by-symptom "Direct link to Troubleshooting by symptom")

### "The server connects but the tools I expected are missing"[​](#the-server-connects-but-the-tools-i-expected-are-missing 'Direct link to "The server connects but the tools I expected are missing"')

Possible causes:

- filtered by `tools.include`
- excluded by `tools.exclude`
- utility wrappers disabled via `resources: false` or `prompts: false`
- server does not actually support resources/prompts

### "The server is configured but nothing loads"[​](#the-server-is-configured-but-nothing-loads 'Direct link to "The server is configured but nothing loads"')

Check:

- `enabled: false` was not left in config
- command/runtime exists (`npx`, `uvx`, etc.)
- HTTP endpoint is reachable
- auth env or headers are correct

### "Why do I see fewer tools than the MCP server advertises?"[​](#why-do-i-see-fewer-tools-than-the-mcp-server-advertises 'Direct link to "Why do I see fewer tools than the MCP server advertises?"')

Because Hermes now respects your per-server policy and capability-aware registration. That is expected, and usually desirable.

### "How do I remove an MCP server without deleting the config?"[​](#how-do-i-remove-an-mcp-server-without-deleting-the-config 'Direct link to "How do I remove an MCP server without deleting the config?"')

Use:

That keeps the config around but prevents connection and registration.

## Recommended first MCP setups[​](#recommended-first-mcp-setups "Direct link to Recommended first MCP setups")

Good first servers for most users:

- filesystem
- git
- GitHub
- fetch / documentation MCP servers
- one narrow internal API

Not-great first servers:

- giant business systems with lots of destructive actions and no filtering
- anything you do not understand well enough to constrain

<!--THE END-->

- [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [FAQ](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [Slash Commands](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)