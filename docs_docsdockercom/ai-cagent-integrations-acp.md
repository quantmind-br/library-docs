---
title: ACP
url: https://docs.docker.com/ai/cagent/integrations/acp/
source: llms
fetched_at: 2026-01-24T14:13:28.312882679-03:00
rendered_js: false
word_count: 647
summary: This guide explains how to integrate cagent agents into code editors like Zed and Neovim using the Agent Client Protocol (ACP) for direct file access and AI-assisted development.
tags:
    - cagent
    - acp
    - editor-integration
    - neovim
    - zed
    - codecompanion
    - ai-agents
category: guide
---

## ACP integration

Run cagent agents directly in your editor using the Agent Client Protocol (ACP). Your agent gets access to your editor's filesystem context and can read and modify files as you work. The editor handles file operations while cagent provides the AI capabilities.

This guide shows you how to configure Neovim, or Zed to run cagent agents. If you're looking to expose cagent agents as tools to MCP clients like Claude Desktop or Claude Code, see [MCP integration](https://docs.docker.com/ai/cagent/integrations/mcp/) instead.

When you run cagent with ACP, it becomes part of your editor's environment. You select code, highlight a function, or reference a file - the agent sees what you see. No copying file paths or switching to a terminal.

Ask "explain this function" and the agent reads the file you're viewing. Ask it to "add error handling" and it edits the code right in your editor. The agent works with your editor's view of the project, not some external file system it has to navigate.

The difference from running cagent in a terminal: file operations go through your editor instead of the agent directly accessing your filesystem. When the agent needs to read or write a file, it requests it from your editor. This keeps the agent's view of your code synchronized with yours - same working directory, same files, same state.

Before configuring your editor, you need:

- **cagent installed** - See the [installation guide](https://docs.docker.com/ai/cagent/#installation)
- **Agent configuration** - A YAML file defining your agent. See the [tutorial](https://docs.docker.com/ai/cagent/tutorial/) or [example configurations](https://github.com/docker/cagent/tree/main/examples)
- **Editor with ACP support** - Neovim, Intellij, Zed, etc.

Your agents will use model provider API keys from your shell environment (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.). Make sure these are set before launching your editor.

### [Zed](#zed)

Zed has built-in ACP support.

1. Add cagent to your agent servers in `settings.json`:
   
   Replace:
   
   - `my-cagent-team` with the name you want to use for the agent
   - `agent.yml` with the path to your agent configuration file.
   
   If you have multiple agent files that you like to run separately, you can create multiple entries under `agent_servers` for each agent.
2. Start a new external agent thread. Select your agent in the drop-down list.
   
   ![New external thread with cagent in Zed](https://docs.docker.com/ai/cagent/images/cagent-acp-zed.avif)
   
   ![New external thread with cagent in Zed](https://docs.docker.com/ai/cagent/images/cagent-acp-zed.avif)

### [Neovim](#neovim)

Use the [CodeCompanion](https://github.com/olimorris/codecompanion.nvim) plugin, which has native support for cagent through a built-in adapter:

1. [Install CodeCompanion](https://codecompanion.olimorris.dev/installation) through your plugin manager.
2. Extend the `cagent` adapter in your CodeCompanion config:
   
   Replace `agent.yml` with the path to your agent configuration file. If you have multiple agent files that you like to run separately, you can create multiple commands for each agent.
3. Restart Neovim and launch CodeCompanion:
4. Switch to the cagent adapter (keymap `ga` in the CodeCompanion buffer, by default).

See the [CodeCompanion ACP documentation](https://codecompanion.olimorris.dev/usage/acp-protocol) for more information about ACP support in CodeCompanion. Note that terminal operations are not supported, so [toolsets](https://docs.docker.com/ai/cagent/reference/toolsets/) like `shell` or `script_shell` are not usable through CodeCompanion.

You can specify your agent configuration as a local file path or OCI registry reference:

Use the same syntax in your editor configuration:

Registry references enable team sharing, version management, and clean configuration without local file paths. See [Sharing agents](https://docs.docker.com/ai/cagent/sharing-agents/) for details on using OCI registries.

Verify your configuration works:

1. Start the cagent ACP server using your editor's configured method
2. Send a test prompt through your editor's interface
3. Check that the agent responds
4. Verify filesystem operations work by asking the agent to read a file

If the agent starts but can't access files or perform other actions, check:

- Working directory in your editor is set correctly to your project root
- Agent configuration file path is absolute or relative to working directory
- Your editor or plugin properly implements ACP protocol features

<!--THE END-->

- Review the [configuration reference](https://docs.docker.com/ai/cagent/reference/config/) for advanced agent setup
- Explore the [toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/) to learn what tools are available
- Add [RAG for codebase search](https://docs.docker.com/ai/cagent/rag/) to your agent
- Check the [CLI reference](https://docs.docker.com/ai/cagent/reference/cli/) for all `cagent acp` options
- Browse [example configurations](https://github.com/docker/cagent/tree/main/examples) for inspiration