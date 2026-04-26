---
title: Install Mistral Vibe and send your first prompt | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/vibe/install-and-first-prompt
source: sitemap
fetched_at: 2026-04-26T04:07:31.008161315-03:00
rendered_js: false
word_count: 337
summary: This document provides a step-by-step guide for installing, configuring, and performing initial interactions with the Mistral Vibe command-line interface.
tags:
    - cli-tool
    - installation-guide
    - mistral-vibe
    - terminal-application
    - api-configuration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Install [Mistral Vibe](https://docs.mistral.ai/mistral-vibe/overview), configure your theme and API key, and send your first prompt directly from the terminal.

**What you get:**
- **One-line install**: get Mistral Vibe running in seconds on macOS or Linux
- **Theme selection**: choose an interface style for the interactive CLI
- **API key configuration**: connect Mistral Vibe to your Mistral account on first launch

**Time to complete:** ~5 minutes

**Prerequisites:**
- macOS or Linux (Windows: follow manual install below)
- Python 3.12 or later
- [Mistral account with Studio API key](https://console.mistral.ai/codestral/cli)

## One-liner Install (macOS/Linux)

```bash
curl -sL https://setup.mistral.tech | bash
```

## Manual Install (macOS/Linux/Windows)

1. Confirm Python 3.12+: `python3 --version`.
2. Install via your preferred package manager.

## First Launch

1. Open a terminal and navigate to any project directory.
2. Run `vibe`.

On first launch, Mistral Vibe prompts you to configure:

3. **Pick a theme** — select your preferred interface style. Change later with `/theme` command.

![Select your preferred theme](https://docs.mistral.ai/assets/quickstarts/vibe/theme.png)

4. **Enter your API key** — generate a key from [Studio Codestral API keys](https://console.mistral.ai/codestral/cli) and paste it into the terminal.

![Entering the API key on first launch](https://docs.mistral.ai/assets/quickstarts/vibe/api-key.png)

Mistral Vibe stores the key locally. You do not need to enter it again.

## Send a Prompt

Type a request directly into the Mistral Vibe prompt:

> List the files in this directory and explain what each one does.

Mistral Vibe reads your project context and responds with relevant information. It can also generate code, edit files, and run shell commands.

![Sending a query to Mistral Vibe](https://docs.mistral.ai/assets/quickstarts/vibe/query.png)

To run a shell command directly, prefix it with `!`. Example: `!ls` or `!git status`.

## Outcome

1. Mistral Vibe is installed and available in your terminal (`vibe --version` confirms it)
2. Your theme and API key are configured
3. Mistral Vibe responds to prompts with context-aware answers

#cli-tool #installation-guide #mistral-vibe