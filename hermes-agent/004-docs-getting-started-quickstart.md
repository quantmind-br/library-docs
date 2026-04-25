---
title: Quickstart | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
source: crawler
fetched_at: 2026-04-24T16:59:59.914169466-03:00
rendered_js: false
word_count: 1108
summary: This guide provides a comprehensive step-by-step tutorial on setting up Hermes Agent from scratch, covering installation, provider selection, running initial chats, verifying sessions, exploring key features, and adding advanced integrations like bots and external tools.
tags:
    - hermes-agent
    - setup-guide
    - ai-assistant
    - cli-tutorial
    - provider-selection
    - configuration
category: guide
---

This guide gets you from zero to a working Hermes setup that survives real use. Install, choose a provider, verify a working chat, and know exactly what to do when something breaks.

## Who this is for[​](#who-this-is-for "Direct link to Who this is for")

- Brand new and want the shortest path to a working setup
- Switching providers and don't want to lose time to config mistakes
- Setting up Hermes for a team, bot, or always-on workflow
- Tired of "it installed, but it still does nothing"

## The fastest path[​](#the-fastest-path "Direct link to The fastest path")

Pick the row that matches your goal:

GoalDo this firstThen do thisI just want Hermes working on my machine`hermes setup`Run a real chat and verify it respondsI already know my provider`hermes model`Save the config, then start chattingI want a bot or always-on setup`hermes gateway setup` after CLI worksConnect Telegram, Discord, Slack, or another platformI want a local or self-hosted model`hermes model` → custom endpointVerify the endpoint, model name, and context lengthI want multi-provider fallback`hermes model` firstAdd routing and fallback only after the base chat works

**Rule of thumb:** if Hermes cannot complete a normal chat, do not add more features yet. Get one clean conversation working first, then layer on gateway, cron, skills, voice, or routing.

* * *

## 1. Install Hermes Agent[​](#1-install-hermes-agent "Direct link to 1. Install Hermes Agent")

Run the one-line installer:

```bash
# Linux / macOS / WSL2 / Android (Termux)
curl-fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh |bash
```

Android / Termux

If you're installing on a phone, see the dedicated [Termux guide](https://hermes-agent.nousresearch.com/docs/getting-started/termux) for the tested manual path, supported extras, and current Android-specific limitations.

Windows Users

Install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) first, then run the command above inside your WSL2 terminal.

After it finishes, reload your shell:

```bash
source ~/.bashrc   # or source ~/.zshrc
```

For detailed installation options, prerequisites, and troubleshooting, see the [Installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

## 2. Choose a Provider[​](#2-choose-a-provider "Direct link to 2. Choose a Provider")

The single most important setup step. Use `hermes model` to walk through the choice interactively:

Good defaults:

SituationRecommended pathLeast frictionNous Portal or OpenRouterYou already have Claude or Codex authAnthropic or OpenAI CodexYou want local/private inferenceOllama or any custom OpenAI-compatible endpointYou want multi-provider routingOpenRouterYou have a custom GPU servervLLM, SGLang, LiteLLM, or any OpenAI-compatible endpoint

For most first-time users: choose a provider, accept the defaults unless you know why you're changing them. The full provider catalog with env vars and setup steps lives on the [Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers) page.

Minimum context: 64K tokens

Hermes Agent requires a model with at least **64,000 tokens** of context. Models with smaller windows cannot maintain enough working memory for multi-step tool-calling workflows and will be rejected at startup. Most hosted models (Claude, GPT, Gemini, Qwen, DeepSeek) meet this easily. If you're running a local model, set its context size to at least 64K (e.g. `--ctx-size 65536` for llama.cpp or `-c 65536` for Ollama).

tip

You can switch providers at any time with `hermes model` — no lock-in. For a full list of all supported providers and setup details, see [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers).

### How settings are stored[​](#how-settings-are-stored "Direct link to How settings are stored")

Hermes separates secrets from normal config:

- **Secrets and tokens** → `~/.hermes/.env`
- **Non-secret settings** → `~/.hermes/config.yaml`

The easiest way to set values correctly is through the CLI:

```bash
hermes config set model anthropic/claude-opus-4.6
hermes config set terminal.backend docker
hermes config set OPENROUTER_API_KEY sk-or-...
```

The right value goes to the right file automatically.

## 3. Run Your First Chat[​](#3-run-your-first-chat "Direct link to 3. Run Your First Chat")

```bash
hermes            # classic CLI
hermes --tui# modern TUI (recommended)
```

You'll see a welcome banner with your model, available tools, and skills. Use a prompt that's specific and easy to verify:

Pick your interface

Hermes ships with two terminal interfaces: the classic `prompt_toolkit` CLI and a newer [TUI](https://hermes-agent.nousresearch.com/docs/user-guide/tui) with modal overlays, mouse selection, and non-blocking input. Both share the same sessions, slash commands, and config — try each with `hermes` vs `hermes --tui`.

```text
Summarize this repo in 5 bullets and tell me what the main entrypoint is.
```

```text
Check my current directory and tell me what looks like the main project file.
```

```text
Help me set up a clean GitHub PR workflow for this codebase.
```

**What success looks like:**

- The banner shows your chosen model/provider
- Hermes replies without error
- It can use a tool if needed (terminal, file read, web search)
- The conversation continues normally for more than one turn

If that works, you're past the hardest part.

## 4. Verify Sessions Work[​](#4-verify-sessions-work "Direct link to 4. Verify Sessions Work")

Before moving on, make sure resume works:

```bash
hermes --continue# Resume the most recent session
hermes -c# Short form
```

That should bring you back to the session you just had. If it doesn't, check whether you're in the same profile and whether the session actually saved. This matters later when you're juggling multiple setups or machines.

## 5. Try Key Features[​](#5-try-key-features "Direct link to 5. Try Key Features")

### Use the terminal[​](#use-the-terminal "Direct link to Use the terminal")

```text
❯ What's my disk usage? Show the top 5 largest directories.
```

The agent runs terminal commands on your behalf and shows results.

### Slash commands[​](#slash-commands "Direct link to Slash commands")

Type `/` to see an autocomplete dropdown of all commands:

CommandWhat it does`/help`Show all available commands`/tools`List available tools`/model`Switch models interactively`/personality pirate`Try a fun personality`/save`Save the conversation

### Multi-line input[​](#multi-line-input "Direct link to Multi-line input")

Press `Alt+Enter` or `Ctrl+J` to add a new line. Great for pasting code or writing detailed prompts.

### Interrupt the agent[​](#interrupt-the-agent "Direct link to Interrupt the agent")

If the agent is taking too long, type a new message and press Enter — it interrupts the current task and switches to your new instructions. `Ctrl+C` also works.

## 6. Add the Next Layer[​](#6-add-the-next-layer "Direct link to 6. Add the Next Layer")

Only after the base chat works. Pick what you need:

### Bot or shared assistant[​](#bot-or-shared-assistant "Direct link to Bot or shared assistant")

```bash
hermes gateway setup    # Interactive platform configuration
```

Connect [Telegram](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram), [Discord](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord), [Slack](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack), [WhatsApp](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp), [Signal](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/signal), [Email](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/email), or [Home Assistant](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/homeassistant).

### Automation and tools[​](#automation-and-tools "Direct link to Automation and tools")

- `hermes tools` — tune tool access per platform
- `hermes skills` — browse and install reusable workflows
- Cron — only after your bot or CLI setup is stable

### Sandboxed terminal[​](#sandboxed-terminal "Direct link to Sandboxed terminal")

For safety, run the agent in a Docker container or on a remote server:

```bash
hermes config set terminal.backend docker# Docker isolation
hermes config set terminal.backend ssh# Remote server
```

### Voice mode[​](#voice-mode "Direct link to Voice mode")

```bash
pip install"hermes-agent[voice]"
# Includes faster-whisper for free local speech-to-text
```

Then in the CLI: `/voice on`. Press `Ctrl+B` to record. See [Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode).

### Skills[​](#skills "Direct link to Skills")

```bash
hermes skills search kubernetes
hermes skills install openai/skills/k8s
```

Or use `/skills` inside a chat session.

### MCP servers[​](#mcp-servers "Direct link to MCP servers")

```yaml
# Add to ~/.hermes/config.yaml
mcp_servers:
github:
command: npx
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"ghp_xxx"
```

### Editor integration (ACP)[​](#editor-integration-acp "Direct link to Editor integration (ACP)")

```bash
pip install-e'.[acp]'
hermes acp
```

See [ACP Editor Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp).

* * *

## Common Failure Modes[​](#common-failure-modes "Direct link to Common Failure Modes")

These are the problems that waste the most time:

SymptomLikely causeFixHermes opens but gives empty or broken repliesProvider auth or model selection is wrongRun `hermes model` again and confirm provider, model, and authCustom endpoint "works" but returns garbageWrong base URL, model name, or not actually OpenAI-compatibleVerify the endpoint in a separate client firstGateway starts but nobody can message itBot token, allowlist, or platform setup is incompleteRe-run `hermes gateway setup` and check `hermes gateway status``hermes --continue` can't find old sessionSwitched profiles or session never savedCheck `hermes sessions list` and confirm you're in the right profileModel unavailable or odd fallback behaviorProvider routing or fallback settings are too aggressiveKeep routing off until the base provider is stable`hermes doctor` flags config problemsConfig values are missing or staleFix the config, retest a plain chat before adding features

When something feels off, use this order:

1. `hermes doctor`
2. `hermes model`
3. `hermes setup`
4. `hermes sessions list`
5. `hermes --continue`
6. `hermes gateway status`

That sequence gets you from "broken vibes" back to a known state fast.

* * *

## Quick Reference[​](#quick-reference "Direct link to Quick Reference")

CommandDescription`hermes`Start chatting`hermes model`Choose your LLM provider and model`hermes tools`Configure which tools are enabled per platform`hermes setup`Full setup wizard (configures everything at once)`hermes doctor`Diagnose issues`hermes update`Update to latest version`hermes gateway`Start the messaging gateway`hermes --continue`Resume last session

## Next Steps[​](#next-steps "Direct link to Next Steps")

- [**CLI Guide**](https://hermes-agent.nousresearch.com/docs/user-guide/cli) — Master the terminal interface
- [**Configuration**](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) — Customize your setup
- [**Messaging Gateway**](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/) — Connect Telegram, Discord, Slack, WhatsApp, Signal, Email, or Home Assistant
- [**Tools & Toolsets**](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools) — Explore available capabilities
- [**AI Providers**](https://hermes-agent.nousresearch.com/docs/integrations/providers) — Full provider list and setup details
- [**Skills System**](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) — Reusable workflows and knowledge
- [**Tips & Best Practices**](https://hermes-agent.nousresearch.com/docs/guides/tips) — Power user tips