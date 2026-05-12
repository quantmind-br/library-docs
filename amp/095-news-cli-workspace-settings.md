---
title: Workspace Settings
url: https://ampcode.com/news/cli-workspace-settings
source: crawler
fetched_at: 2026-02-06T02:08:22.828272666-03:00
rendered_js: false
word_count: 109
summary: This document explains how to use workspace-specific configuration files in the Amp CLI to manage project-level settings and MCP servers.
tags:
    - amp-cli
    - workspace-settings
    - mcp-servers
    - configuration
    - cli-tools
category: configuration
---

The Amp CLI now supports workspace-specific settings via `.amp/settings.json` files in your project directory.

This allows you to configure the Amp CLI differently for each project, with settings like permissions, MCP servers, and other preferences automatically picked up when you run `amp` in that workspace.

For example, here's how you can configure the Amp CLI to use a specific MCP server in a given project:

```
$ cd my-project
$ amp mcp add --workspace playwright -- npx -y @playwright/mcp@latest
```

Due to the `--workspace` flag, the setting was added in the `.amp/settings.json` file in `my-project`:

```
$ cat .amp/settings.json
{
  "amp.mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

When you then run `amp` in `my-project`, the settings in `.amp/settings.json` will be merged with your global Amp settings.

See the [manual](https://ampcode.com/manual#configuration) for details on how settings are resolved.