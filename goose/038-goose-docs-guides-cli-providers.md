---
title: CLI Providers | goose
url: https://block.github.io/goose/docs/guides/cli-providers
source: github_pages
fetched_at: 2026-01-22T22:13:35.083510518-03:00
rendered_js: true
word_count: 1261
summary: This document explains how to integrate and configure pass-through CLI providers like Claude Code, OpenAI Codex, and Gemini CLI within the goose interface to enable session management and unified workflows.
tags:
    - goose-ai
    - cli-providers
    - session-management
    - configuration
    - integration
    - claude-code
    - openai-codex
    - gemini-cli
category: guide
---

goose can make use of pass-through providers that integrate with existing CLI tools from Anthropic, OpenAI, Cursor, and Google. These providers allow you to use your existing Claude Code, Codex, Cursor Agent, and Google Gemini CLI subscriptions through goose's interface, adding session management, persistence, and workflow integration capabilities to these tools.

Limitations

These providers don’t fully support all goose features, may have platform or capability limitations, and can sometimes require advanced debugging if issues arise. They’re included here purely as a convenience.

## Why Use CLI Providers?[​](#why-use-cli-providers "Direct link to Why Use CLI Providers?")

CLI providers are useful if you:

- already have a Claude Code, Codex, Cursor, or Google Gemini CLI subscription and want to use it through goose instead of paying per token
- need session persistence to save, resume, and export conversation history
- want to use goose recipes and scheduled tasks to create repeatable workflows
- prefer unified commands across different AI providers
- want to [use multiple models together](#combining-with-other-models) in your tasks

### Benefits[​](#benefits "Direct link to Benefits")

#### Session Management[​](#session-management "Direct link to Session Management")

- **Persistent conversations**: Save and resume sessions across restarts
- **Export capabilities**: Export conversation history and artifacts
- **Session organization**: Manage multiple conversation threads

#### Workflow Integration[​](#workflow-integration "Direct link to Workflow Integration")

- **Recipe compatibility**: Use CLI providers in automated goose recipes
- **Scheduling support**: Include in scheduled tasks and workflows
- **Hybrid configurations**: Combine with LLM providers using lead/worker patterns

#### Interface Consistency[​](#interface-consistency "Direct link to Interface Consistency")

- **Unified commands**: Use the same `goose session` interface across all providers
- **Consistent configuration**: Manage all providers through goose's configuration system

Extensions

CLI providers do **not** give you access to goose's extension ecosystem (MCP servers, third-party integrations, etc.). They use their own built-in tools to prevent conflicts. If you need goose's extensions, use standard [API providers](https://block.github.io/goose/docs/getting-started/providers#available-providers) instead.

## Available CLI Providers[​](#available-cli-providers "Direct link to Available CLI Providers")

### Claude Code[​](#claude-code "Direct link to Claude Code")

The Claude Code provider integrates with Anthropic's [Claude CLI tool](https://claude.ai/cli), allowing you to use Claude models through your existing Claude Code subscription.

**Features:**

- Uses Claude's latest models
- 200,000 token context limit
- Automatic filtering of goose extensions from system prompts (since Claude Code has its own tool ecosystem)
- JSON output parsing for structured responses

**Requirements:**

- Claude CLI tool installed and configured
- Active Claude Code subscription
- CLI tool authenticated with your Anthropic account

### OpenAI Codex[​](#openai-codex "Direct link to OpenAI Codex")

The Codex provider integrates with OpenAI's [Codex CLI tool](https://developers.openai.com/codex/cli), allowing you to use OpenAI models through your existing ChatGPT Plus/Pro subscription or API credits.

**Features:**

- Uses OpenAI's GPT-5 series models (gpt-5.2-codex, gpt-5.2, gpt-5.1-codex-max, gpt-5.1-codex-mini)
- Configurable reasoning effort levels (low, medium, high)
- Optional skills support for enhanced capabilities
- JSON output parsing for structured responses
- Automatic filtering of goose extensions from system prompts

**Requirements:**

- Codex CLI tool installed (`npm i -g @openai/codex` or `brew install --cask codex`)
- Active ChatGPT Plus/Pro subscription or OpenAI API credits
- CLI tool authenticated with your OpenAI account
- By default, Codex requires running from a git repository. Set `CODEX_SKIP_GIT_CHECK=true` to bypass this requirement

### Cursor Agent[​](#cursor-agent "Direct link to Cursor Agent")

The Cursor provider integrates with Cursor's [CLI agent](https://docs.cursor.com/en/cli/installation), providing access to through your existing subscription.

**Features:**

- integrates with Cursor Agent CLI coding tasks.
- ideal for code-related workflows and file interactions.

**Requirements:**

- cursor-agent tool installed and configured.
- CLI tool authenticated.

### Gemini CLI[​](#gemini-cli "Direct link to Gemini CLI")

The Gemini CLI provider integrates with Google's [Gemini CLI tool](https://ai.google.dev/gemini-api/docs), providing access to Gemini models through your Google AI subscription.

**Features:**

- 1,000,000 token context limit

**Requirements:**

- Gemini CLI tool installed and configured
- CLI tool authenticated with your Google account

## Setup Instructions[​](#setup-instructions "Direct link to Setup Instructions")

### Claude Code[​](#claude-code-1 "Direct link to Claude Code")

1. **Install Claude CLI Tool**
   
   Follow the [installation instructions for Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) to install and configure the Claude CLI tool.
2. **Authenticate with Claude**
   
   Ensure your Claude CLI is authenticated and working
3. **Configure goose**
   
   Set the provider environment variable:
   
   ```
   export GOOSE_PROVIDER=claude-code
   ```
   
   Or configure through the goose CLI using `goose configure`:
   
   ```
   ┌   goose-configure 
   │
   ◇  What would you like to configure?
   │  Configure Providers 
   │
   ◇  Which model provider should we use?
   │  Claude Code 
   │
   ◇  Model fetch complete
   │
   ◇  Enter a model from that provider:
   │  default
   ```

### OpenAI Codex[​](#openai-codex-1 "Direct link to OpenAI Codex")

1. **Install Codex CLI Tool**
   
   Install the Codex CLI using npm or Homebrew:
   
   ```
   npm i -g @openai/codex
   # or
   brew install --cask codex
   ```
2. **Authenticate with OpenAI**
   
   Run `codex` and follow the authentication prompts. You can use your ChatGPT account or API key.
3. **Configure goose**
   
   Set the provider environment variable:
   
   ```
   export GOOSE_PROVIDER=codex
   ```
   
   Or configure through the goose CLI using `goose configure`:
   
   ```
   ┌   goose-configure
   │
   ◇  What would you like to configure?
   │  Configure Providers
   │
   ◇  Which model provider should we use?
   │  OpenAI Codex CLI
   │
   ◇  Model fetch complete
   │
   ◇  Enter a model from that provider:
   │  gpt-5.2-codex
   ```

### Cursor Agent[​](#cursor-agent-1 "Direct link to Cursor Agent")

1. **Install Cursor agent Tool**
   
   Follow the [installation instructions for Cursor Agent](https://docs.cursor.com/en/cli/installation) to install and configure the cursor agent tool.
2. **Authenticate with Cursor**
   
   Ensure your Cursor Agent is authenticated and working
3. **Configure goose**
   
   Set the provider environment variable:
   
   ```
   export GOOSE_PROVIDER=cursor-agent
   ```
   
   Or configure through the goose CLI using `goose configure`:
   
   ```
   ┌   goose-configure
   │
   ◇  What would you like to configure?
   │  Configure Providers
   │
   ◇  Which model provider should we use?
   │  Cursor Agent
   │
   ◇  Model fetch complete
   │
   ◇  Enter a model from that provider:
   │  default
   ```

### Gemini CLI[​](#gemini-cli-1 "Direct link to Gemini CLI")

1. **Install Gemini CLI Tool**
   
   Follow the [installation instructions for Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/) to install and configure the Gemini CLI tool.
2. **Authenticate with Google**
   
   Ensure your Gemini CLI is authenticated and working.
3. **Configure goose**
   
   Set the provider environment variable:
   
   ```
   export GOOSE_PROVIDER=gemini-cli
   ```
   
   Or configure through the goose CLI using `goose configure`:
   
   ```
   ┌   goose-configure 
   │
   ◇  What would you like to configure?
   │  Configure Providers 
   │
   ◇  Which model provider should we use?
   │  Gemini CLI 
   │
   ◇  Model fetch complete
   │
   ◇  Enter a model from that provider:
   │  default
   ```

## Usage Examples[​](#usage-examples "Direct link to Usage Examples")

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

Once configured, you can start a goose session using these providers just like any others:

### Combining with Other Models[​](#combining-with-other-models "Direct link to Combining with Other Models")

CLI providers work well in combination with other models using goose's [lead/worker pattern](https://block.github.io/goose/docs/tutorials/lead-worker):

```
# Use Claude Code as lead model, GPT-4o as worker
export GOOSE_LEAD_PROVIDER=claude-code
export GOOSE_PROVIDER=openai
export GOOSE_MODEL=gpt-4o
export GOOSE_LEAD_MODEL=default

goose session
```

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

### Claude Code Configuration[​](#claude-code-configuration "Direct link to Claude Code Configuration")

Environment VariableDescriptionDefault`GOOSE_PROVIDER`Set to `claude-code` to use this providerNone`GOOSE_MODEL`Model to use (only `sonnet` or `opus` are passed to CLI)`claude-sonnet-4-20250514``CLAUDE_CODE_COMMAND`Path to the Claude CLI command`claude`

**Known Models:**

The following models are recognized and passed to the Claude CLI via the `--model` flag. If `GOOSE_MODEL` is set to a value not in this list, no model flag is passed and Claude Code uses its default:

- `sonnet`
- `opus`

**Permission Modes (`GOOSE_MODE`):**

ModeClaude Code FlagBehavior`auto``--dangerously-skip-permissions`Bypasses all permission prompts`smart-approve``--permission-mode acceptEdits`Auto-accepts edits, prompts for other actions`approve`Not supportedReturns an error`chat`(none)Default Claude Code behavior

### Cursor Agent Configuration[​](#cursor-agent-configuration "Direct link to Cursor Agent Configuration")

Environment VariableDescriptionDefault`GOOSE_PROVIDER`Set to `cursor-agent` to use this providerNone`CURSOR_AGENT_COMMAND`Path to the Cursor Agent command`cursor-agent`

### OpenAI Codex Configuration[​](#openai-codex-configuration "Direct link to OpenAI Codex Configuration")

Environment VariableDescriptionDefault`GOOSE_PROVIDER`Set to `codex` to use this providerNone`GOOSE_MODEL`Model to use (only known models are passed to CLI)`gpt-5.2-codex``CODEX_COMMAND`Path to the Codex CLI command`codex``CODEX_REASONING_EFFORT`Reasoning effort level: `low`, `medium`, or `high``high``CODEX_ENABLE_SKILLS`Enable Codex skills: `true` or `false``true``CODEX_SKIP_GIT_CHECK`Skip git repository requirement: `true` or `false``false`

**Known Models:**

The following models are recognized and passed to the Codex CLI via the `-m` flag. If `GOOSE_MODEL` is set to a value not in this list, no model flag is passed and Codex uses its default:

- `gpt-5.2-codex` (400K context, auto-compacting)
- `gpt-5.2` (400K context, auto-compacting)
- `gpt-5.1-codex-max` (256K context)
- `gpt-5.1-codex-mini` (256K context)

Legacy Models

These are the default models supported by Codex CLI v0.77.0. To access older or legacy models, you can run `codex -m <model_name>` directly or configure them in Codex's `config.toml`. See the [Codex CLI documentation](https://developers.openai.com/codex/cli) for details.

**Permission Modes (`GOOSE_MODE`):**

ModeCodex FlagBehavior`auto``--yolo`Bypasses all approvals and sandbox restrictions`smart-approve``--full-auto`Workspace-write sandbox, approvals only on failure`approve`(none)Interactive approvals (Codex default behavior)`chat``--sandbox read-only`Read-only sandbox mode

### Gemini CLI Configuration[​](#gemini-cli-configuration "Direct link to Gemini CLI Configuration")

Environment VariableDescriptionDefault`GOOSE_PROVIDER`Set to `gemini-cli` to use this providerNone`GEMINI_CLI_COMMAND`Path to the Gemini CLI command`gemini`

## How It Works[​](#how-it-works "Direct link to How It Works")

### System Prompt Filtering[​](#system-prompt-filtering "Direct link to System Prompt Filtering")

The CLI providers automatically filter out goose's extension information from system prompts since these CLI tools have their own tool ecosystems. This prevents conflicts and ensures clean interaction with the underlying CLI tools.

### Message Translation[​](#message-translation "Direct link to Message Translation")

- **Claude Code**: Converts goose messages to Claude's JSON message format, handling tool calls and responses appropriately
- **Codex**: Converts messages to simple text prompts with role prefixes (Human:/Assistant:), similar to Gemini CLI
- **Cursor Agent**: Converts goose messages to Cursor's JSON message format, handling tool calls and responses appropriately
- **Gemini CLI**: Converts messages to simple text prompts with role prefixes (Human:/Assistant:)

### Response Processing[​](#response-processing "Direct link to Response Processing")

- **Claude Code**: Parses JSON responses to extract text content and usage information
- **Codex**: Parses newline-delimited JSON events to extract text content and usage information
- **Cursor Agent**: Parses JSON responses to extract text content and usage information
- **Gemini CLI**: Processes plain text responses from the CLI tool

## Error Handling[​](#error-handling "Direct link to Error Handling")

CLI providers depend on external tools, so ensure:

- CLI tools are properly installed and in your PATH
- Authentication is maintained and valid
- Subscription limits are not exceeded
- For Codex: you're in a git repository, or set `CODEX_SKIP_GIT_CHECK=true`

* * *

CLI providers offer a way to use existing AI tool subscriptions through goose's interface, adding session management and workflow integration capabilities. They're particularly valuable for users with existing CLI subscriptions who want unified session management and recipe integration.