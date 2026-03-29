---
title: Install goose | goose
url: https://block.github.io/goose/docs/getting-started/installation
source: github_pages
fetched_at: 2026-01-22T22:13:22.808916518-03:00
rendered_js: true
word_count: 655
summary: This document provides instructions for installing the goose Desktop and CLI applications, configuring LLM providers, and managing session settings across various operating systems.
tags:
    - installation
    - goose-desktop
    - goose-cli
    - llm-configuration
    - macos
    - linux
    - windows
    - setup-guide
category: guide
---

- macOS
- Linux
- Windows

Choose to install the Desktop and/or CLI version of goose:

- goose Desktop
- goose CLI

Install goose Desktop directly from the browser or with [Homebrew](https://brew.sh/).

### Option 1: Install via Download

1. Unzip the downloaded zip file.
2. Run the executable file to launch the goose Desktop application.

### Option 2: Install via Homebrew

Homebrew downloads the [same app](https://github.com/Homebrew/homebrew-cask/blob/master/Casks/b/block-goose.rb) but can take care of updates too.

```
  brew install --cask block-goose
```

* * *

Permissions

If you're on an Apple Mac M3 and the goose Desktop app shows no window on launch, check and update the following:

Ensure the `~/.config` directory has read and write access.

goose needs this access to create the log directory and file. Once permissions are granted, the app should load correctly. For steps on how to do this, refer to the [Known Issues Guide](https://block.github.io/goose/docs/troubleshooting/known-issues#macos-permission-issues)

## Set LLM Provider[​](#set-llm-provider "Direct link to Set LLM Provider")

goose works with [supported LLM providers](https://block.github.io/goose/docs/getting-started/providers) that give goose the AI intelligence it needs to understand your requests. On first use, you'll be prompted to configure your preferred provider.

- goose Desktop
- goose CLI

On the welcome screen, choose how to configure a provider:

- **Tetrate Agent Router** - One-click OAuth authentication provides instant access to multiple AI models, starting credits, and built-in rate limiting. See the [goose quickstart guide](https://block.github.io/goose/docs/quickstart#configure-provider) for a walkthrough of this setup.
  
  ##### INFO
  
  You'll receive $10 in free credits the first time you automatically authenticate with Tetrate through goose. This offer is available to both new and existing Tetrate users.
- **OpenRouter** - One-click OAuth authentication provides instant access to multiple AI models with built-in rate limiting.
- **Other Providers** - Choose from a selection of [~20 supported providers](https://block.github.io/goose/docs/getting-started/providers) including OpenAI, Anthropic, Google Gemini, and others through manual configuration. If you don't see your provider in the list, you can add a custom provider. Be ready to provide your API key, API Host address, or other optional parameters depending on provider.

tip

goose relies heavily on tool calling capabilities and currently works best with Claude 4 models.

## Update Provider[​](#update-provider "Direct link to Update Provider")

You can change your LLM provider and/or model or update your API key at any time.

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar.
2. Click the `Settings` button on the sidebar.
3. Click the `Models` tab.
4. Choose to update your provider, switch models, or click `Reset Provider and Model` to clear your settings and return to the welcome screen. See details about these [configuration options](https://block.github.io/goose/docs/getting-started/providers#configure-provider-and-model).

Billing

[Google Gemini](https://aistudio.google.com/app/apikey) offers a free tier you can get started with. Otherwise, you'll need to ensure that you have credits available in your LLM Provider account to successfully make requests.

Some providers also have rate limits on API usage, which can affect your experience. Check out our [Handling Rate Limits](https://block.github.io/goose/docs/guides/handling-llm-rate-limits-with-goose) guide to learn how to efficiently manage these limits while using goose.

## Running goose[​](#running-goose "Direct link to Running goose")

- goose Desktop
- goose CLI

Starting a session in the goose Desktop is straightforward. After choosing your provider, you'll see the session interface ready for use.

Type your questions, tasks, or instructions directly into the input field, and goose will get to work immediately.

The goose CLI and Desktop UI share all core configurations, including LLM provider settings, model selection, and extension configurations. When you install or configure extensions in either interface, the settings are stored in a central location, making them available to both the Desktop application and CLI. This makes it convenient to switch between interfaces while maintaining consistent settings. For more information, visit the [Config Files](https://block.github.io/goose/docs/guides/config-files) guide.

info

While core configurations are shared between interfaces, extensions have flexibility in how they store authentication credentials. Some extensions may use the shared config files while others implement their own storage methods.

- goose Desktop
- goose CLI

Navigate to shared configurations through:

1. Click the button in the top-left to open the sidebar.
2. Click the `Settings` button on the sidebar.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

You can also configure Extensions to extend goose's functionality, including adding new ones or toggling them on and off. For detailed instructions, visit the [Using Extensions Guide](https://block.github.io/goose/docs/getting-started/using-extensions).