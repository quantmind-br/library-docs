---
title: ACP Editor Integration | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/acp
source: crawler
fetched_at: 2026-04-24T17:00:10.493647733-03:00
rendered_js: false
word_count: 442
summary: This document details how the Hermes Agent operates in ACP (Agent Client Protocol) server mode, enabling seamless integration with editor environments by exposing various capabilities like chat messages, file operations, and terminal commands.
tags:
    - hermes-agent
    - acp-protocol
    - editor-integration
    - coding-assistant
    - server-mode
    - toolset
category: guide
---

Hermes Agent can run as an ACP server, letting ACP-compatible editors talk to Hermes over stdio and render:

- chat messages
- tool activity
- file diffs
- terminal commands
- approval prompts
- streamed thinking / response chunks

ACP is a good fit when you want Hermes to behave like an editor-native coding agent instead of a standalone CLI or messaging bot.

## What Hermes exposes in ACP mode[​](#what-hermes-exposes-in-acp-mode "Direct link to What Hermes exposes in ACP mode")

Hermes runs with a curated `hermes-acp` toolset designed for editor workflows. It includes:

- file tools: `read_file`, `write_file`, `patch`, `search_files`
- terminal tools: `terminal`, `process`
- web/browser tools
- memory, todo, session search
- skills
- execute\_code and delegate\_task
- vision

It intentionally excludes things that do not fit typical editor UX, such as messaging delivery and cronjob management.

## Installation[​](#installation "Direct link to Installation")

Install Hermes normally, then add the ACP extra:

This installs the `agent-client-protocol` dependency and enables:

- `hermes acp`
- `hermes-acp`
- `python -m acp_adapter`

## Launching the ACP server[​](#launching-the-acp-server "Direct link to Launching the ACP server")

Any of the following starts Hermes in ACP mode:

Hermes logs to stderr so stdout remains reserved for ACP JSON-RPC traffic.

## Editor setup[​](#editor-setup "Direct link to Editor setup")

### VS Code[​](#vs-code "Direct link to VS Code")

Install an ACP client extension, then point it at the repo's `acp_registry/` directory.

Example settings snippet:

```json
{
"acpClient.agents":[
{
"name":"hermes-agent",
"registryDir":"/path/to/hermes-agent/acp_registry"
}
]
}
```

### Zed[​](#zed "Direct link to Zed")

Example settings snippet:

```json
{
"agent_servers":{
"hermes-agent":{
"type":"custom",
"command":"hermes",
"args":["acp"],
},
},
}
```

### JetBrains[​](#jetbrains "Direct link to JetBrains")

Use an ACP-compatible plugin and point it at:

```text
/path/to/hermes-agent/acp_registry
```

## Registry manifest[​](#registry-manifest "Direct link to Registry manifest")

The ACP registry manifest lives at:

It advertises a command-based agent whose launch command is:

## Configuration and credentials[​](#configuration-and-credentials "Direct link to Configuration and credentials")

ACP mode uses the same Hermes configuration as the CLI:

- `~/.hermes/.env`
- `~/.hermes/config.yaml`
- `~/.hermes/skills/`
- `~/.hermes/state.db`

Provider resolution uses Hermes' normal runtime resolver, so ACP inherits the currently configured provider and credentials.

## Session behavior[​](#session-behavior "Direct link to Session behavior")

ACP sessions are tracked by the ACP adapter's in-memory session manager while the server is running.

Each session stores:

- session ID
- working directory
- selected model
- current conversation history
- cancel event

The underlying `AIAgent` still uses Hermes' normal persistence/logging paths, but ACP `list/load/resume/fork` are scoped to the currently running ACP server process.

## Working directory behavior[​](#working-directory-behavior "Direct link to Working directory behavior")

ACP sessions bind the editor's cwd to the Hermes task ID so file and terminal tools run relative to the editor workspace, not the server process cwd.

## Approvals[​](#approvals "Direct link to Approvals")

Dangerous terminal commands can be routed back to the editor as approval prompts. ACP approval options are simpler than the CLI flow:

- allow once
- allow always
- deny

On timeout or error, the approval bridge denies the request.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### ACP agent does not appear in the editor[​](#acp-agent-does-not-appear-in-the-editor "Direct link to ACP agent does not appear in the editor")

Check:

- the editor is pointed at the correct `acp_registry/` path
- Hermes is installed and on your PATH
- the ACP extra is installed (`pip install -e '.[acp]'`)

### ACP starts but immediately errors[​](#acp-starts-but-immediately-errors "Direct link to ACP starts but immediately errors")

Try these checks:

```bash
hermes doctor
hermes status
hermes acp
```

### Missing credentials[​](#missing-credentials "Direct link to Missing credentials")

ACP mode does not have its own login flow. It uses Hermes' existing provider setup. Configure credentials with:

or by editing `~/.hermes/.env`.

## See also[​](#see-also "Direct link to See also")

- [ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
- [Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
- [Tools Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)