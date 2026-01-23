---
title: Quickstart | goose
url: https://block.github.io/goose/docs/quickstart
source: github_pages
fetched_at: 2026-01-22T22:16:02.701343844-03:00
rendered_js: true
word_count: 542
summary: This tutorial provides a quickstart guide for goose, an open-source AI agent, covering installation, LLM provider configuration, and the creation of a web-based application.
tags:
    - ai-agent
    - software-automation
    - goose-cli
    - goose-desktop
    - llm-configuration
    - mcp-extensions
category: tutorial
---

goose is an extensible open source AI agent that enhances your software development by automating coding tasks.

This quick tutorial will guide you through:

- ✅ Installing goose
- ✅ Configuring your LLM
- ✅ Building a small app
- ✅ Adding an MCP server

Let's begin 🚀

## Install goose[​](#install-goose "Direct link to Install goose")

- macOS
- Linux
- Windows

Choose to install the Desktop and/or CLI version of goose:

- goose Desktop
- goose CLI

<!--THE END-->

1. Unzip the downloaded zip file.
2. Run the executable file to launch the goose Desktop application.

## Configure Provider[​](#configure-provider "Direct link to Configure Provider")

goose works with [supported LLM providers](https://block.github.io/goose/docs/getting-started/providers) that give goose the AI intelligence it needs to understand your requests. On first use, you'll be prompted to configure your preferred provider.

- goose Desktop
- goose CLI

On the welcome screen, you have three options:

- **Automatic setup with [Tetrate Agent Router](https://tetrate.io/products/tetrate-agent-router-service)**
- **Automatic Setup with [OpenRouter](https://openrouter.ai/)**
- **Other Providers**

For this quickstart, choose `Automatic setup with Tetrate Agent Router`. Tetrate provides access to multiple AI models with built-in rate limiting and automatic failover. For more information about OpenRouter or other providers, see [Configure LLM Provider](https://block.github.io/goose/docs/getting-started/providers).

goose will open a browser for you to authenticate with Tetrate, or create a new account if you don't have one already. When you return to the goose desktop app, you're ready to begin your first session.

Free Credits Offer

You'll receive $10 in free credits the first time you automatically authenticate with Tetrate through goose. This offer is available to both new and existing Tetrate users.

## Start Session[​](#start-session "Direct link to Start Session")

Sessions are single, continuous conversations between you and goose. Let's start one.

- goose Desktop
- goose CLI

After choosing an LLM provider, click the `Home` button in the sidebar.

Type your questions, tasks, or instructions directly into the input field, and goose will immediately get to work.

## Write Prompt[​](#write-prompt "Direct link to Write Prompt")

From the prompt, you can interact with goose by typing your instructions exactly as you would speak to a developer.

Let's ask goose to make a tic-tac-toe game!

```
create an interactive browser-based tic-tac-toe game in javascript where a player competes against a bot
```

goose will create a plan and then get right to work on implementing it. Once done, your directory should contain a JavaScript file as well as an HTML page for playing.

## Enable an Extension[​](#enable-an-extension "Direct link to Enable an Extension")

While you're able to manually navigate to your working directory and open the HTML file in a browser, wouldn't it be better if goose did that for you? Let's give goose the ability to open a web browser by enabling the [`Computer Controller` extension](https://block.github.io/goose/docs/mcp/computer-controller-mcp).

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar.
2. Click `Extensions` in the sidebar menu.
3. Toggle the `Computer Controller` extension to enable it. This extension enables webscraping, file caching, and automations.
4. Return to your session to continue.
5. Now that goose has browser capabilities, let's ask it to launch your game in a browser:

```
open the tic-tac-toe game in a browser
```

Go ahead and play your game, I know you want to 😂 ... good luck!

## Next Steps[​](#next-steps "Direct link to Next Steps")

Congrats, you've successfully used goose to develop a web app! 🎉

Here are some ideas for next steps:

- Continue your session with goose and improve your game (styling, functionality, etc).
- Browse other available [extensions](https://block.github.io/goose/extensions) and install more to enhance goose's functionality even further.
- Provide goose with a [set of hints](https://block.github.io/goose/docs/guides/context-engineering/using-goosehints) to use within your sessions.
- See how you can set up [access controls](https://block.github.io/goose/docs/mcp/developer-mcp#configuring-access-controls) if you don't want goose to work autonomously.