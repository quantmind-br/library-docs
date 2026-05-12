---
title: "ForgeCode CLI Setup Guide"
url: https://forgecode.dev/docs/
source: sitemap
fetched_at: 2026-04-30T14:09:04.331123435-03:00
rendered_js: false
word_count: 116
summary: "Step-by-step guide to install, configure, and authenticate the ForgeCode CLI for AI-powered coding in Zsh."
tags:
  - cli-tool
  - zsh-integration
  - ai-coding-assistant
  - shell-configuration
  - llm-setup
category: guide
optimized: true
---
# ForgeCode CLI Setup Guide

> **TL;DR**
> Install binary → Configure Zsh plugin → Log in to AI provider → Send prompts with `:`.

## Prerequisites
- [Nerd Font](https://www.nerdfonts.com/) (e.g., FiraCode)
- [Zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)

## Installation Steps

### 1. Install Binary
```bash
curl -sSL https://forgecode.dev/install | sh
```
Verify:
```bash
forge --version
```

### 2. Configure Zsh Plugin
```bash
forge zsh setup
```
> **Restart terminal** for changes to take effect.

**Debugging**:
```bash
forge zsh doctor
```

### 3. Log In to AI Provider
```bash
forge login
```
**Recommended Providers**:
- [OpenRouter](https://openrouter.ai/) (300+ models)
- [OpenAI](https://platform.openai.com/)
- [Anthropic](https://console.anthropic.com/)

**Recommended Models**:
- Proprietary: Claude Sonnet/Opus, GPT Codex
- Open-source: GLM, Kimi, Minimax

### 4. Send First Prompt
```bash
: Explain how to refactor this function
```

### 5. Explore Commands
Press `:` + `Tab` to list all commands.

## Next Steps
- Enable [ForgeCode Services](https://forgecode.dev/docs/forge-services/) for semantic search and tool-call guardrails.