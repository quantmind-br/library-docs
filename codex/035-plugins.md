---
title: Plugins
url: https://developers.openai.com/codex/plugins.md
source: llms
fetched_at: 2026-04-30T10:15:55.586382186-03:00
rendered_js: false
word_count: 383
summary: This document explains how to discover, install, and manage plugins in Codex to extend functionality through skills, app integrations, and MCP servers.
tags:
    - codex
    - plugins
    - mcp-servers
    - app-integration
    - workflow-automation
    - plugin-management
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Plugins

Plugins bundle skills, app integrations, and MCP servers into reusable workflows.

Examples:
- **Gmail plugin** — read and manage Gmail
- **Google Drive plugin** — work across Drive, Docs, Sheets, Slides
- **Slack plugin** — summarize channels or draft replies

A plugin contains:
- **Skills** — reusable instructions for specific work. Codex loads them when needed.
- **Apps** — connections to tools like GitHub, Slack, Google Drive for reading information and taking actions.
- **MCP servers** — services giving Codex access to additional tools or shared information, often from systems outside the local project.

## Use and install

### Codex app

Open **Plugins** to browse and install curated plugins.

### CLI

```text
codex
/plugins
```

Browse by marketplace, inspect details, press `Space` on an installed plugin to toggle enabled state.

### Install and use

1. Search or browse for a plugin, open its details.
2. Select install (app: plus button / **Add to Codex**; CLI: **Install plugin**).
3. If the plugin needs an external app, connect when prompted. Some authenticate during install; others wait until first use.
4. Start a new thread and ask Codex to use the plugin.

After installation, use directly in the prompt window:
- **Describe the task directly** — ask for the outcome (e.g., "Summarize unread Gmail threads from today"). Codex chooses the right installed tools.
- **Choose a specific plugin** — type `@` to invoke the plugin or one of its bundled skills explicitly.

## Permissions and data sharing

Installing a plugin makes its workflows available, but your existing [[041-agent-approvals-security|approval settings]] still apply. Connected external services remain subject to their own authentication, privacy, and data-sharing policies.

- Bundled skills are available immediately after install.
- Apps may prompt you to install or sign in to those apps in ChatGPT during setup or first use.
- MCP servers may require additional setup or authentication.
- When Codex sends data through a bundled app, that app's terms and privacy policy apply.

## Remove or turn off

To remove: reopen from plugin browser and select **Uninstall plugin**. Removes the plugin bundle from Codex, but bundled apps stay installed until managed in ChatGPT.

To disable without removing:
```toml
[plugins."gmail@openai-curated"]
enabled = false
```
Restart Codex after changing `~/.codex/config.toml`.

## Build your own plugin

See [[034-plugins-build|Build plugins]] for local scaffolding, manual marketplace setup, manifests, and packaging.

#plugins #skills #mcp #apps #codex