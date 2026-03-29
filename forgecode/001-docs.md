---
title: ForgeCode
url: https://forgecode.dev/docs/
source: sitemap
fetched_at: 2026-03-29T16:30:30.616933-03:00
rendered_js: false
word_count: 354
summary: This document provides a step-by-step guide for installing, configuring, and authenticating the ForgeCode CLI tool to enable AI-powered coding directly within a Zsh terminal environment.
tags:
    - cli-tool
    - ai-coding-assistant
    - zsh-integration
    - terminal-productivity
    - model-configuration
    - developer-tools
category: guide
---

ForgeCode is a CLI-based coding harness — think Claude Code, but with first-class support for many AI providers. It works equally well with cloud models, open-weight models, and models running locally.

- A [Nerd Font](https://www.nerdfonts.com/) installed and enabled in your terminal (for example, [FiraCode Nerd Font](https://www.nerdfonts.com/font-downloads))
- [Zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH) installed and configured

### Step 1. Install the ForgeCode binary[​](#step-1-install-the-forgecode-binary "Direct link to Step 1. Install the ForgeCode binary")

This works on macOS, Linux, Android, and Windows via WSL or Git Bash.

Verify the installation:

### Step 2. Configure the Zsh plugin[​](#step-2-configure-the-zsh-plugin "Direct link to Step 2. Configure the Zsh plugin")

ForgeCode integrates with Zsh to let you send prompts directly from your shell prompt. Run the setup wizard:

Follow the interactive prompts. Once complete, **you must restart your terminal** for the plugin to take effect. Open a new terminal window, or reload the current session:

important

The Zsh plugin will not be active until you restart your terminal. If the `:` prompt trigger isn't working, this is the most common cause.

If you're still having trouble, run the diagnostics command:

This checks your environment and reports any configuration issues with the Zsh plugin.

### Step 3. Log in to an AI provider[​](#step-3-log-in-to-an-ai-provider "Direct link to Step 3. Log in to an AI provider")

ForgeCode needs access to at least one AI model. Run:

This walks you through selecting a provider and entering your API key.

**If you already have a [ChatGPT Plus](https://chatgpt.com/pricing) or [Claude](https://claude.com/pricing) subscription**, select the corresponding provider (OpenAI or Anthropic) and use that subscription's API access instead of buying a separate key.

Recommended providers

- [OpenRouter](https://openrouter.ai/) — one key, 300+ models from every major vendor
- [OpenAI](https://platform.openai.com/) — GPT Codex series
- [Anthropic](https://console.anthropic.com/) — Claude Sonnet and Opus series

Recommended models

- **Proprietary:** Claude Sonnet & Opus series, GPT Codex series
- **Open-source:** GLM, Kimi, Minimax

After logging in, pick a model:

Browse the list, type to filter, and press Enter. ForgeCode remembers your choice across sessions. You can change it anytime.

### Step 4. Send your first prompt[​](#step-4-send-your-first-prompt "Direct link to Step 4. Send your first prompt")

With the Zsh plugin active and the LLM provider set up, type `:` followed by a **space** and your prompt:

ForgeCode takes it from there.

### Step 5. Explore available commands[​](#step-5-explore-available-commands "Direct link to Step 5. Explore available commands")

To see all available ForgeCode commands, type `:` and press `Tab` (without space):

This lists every command you can run directly from your shell.