---
title: ""
url: https://moonshotai.github.io/kimi-cli/en/guides/integrations.md
source: github_pages
fetched_at: 2026-01-28T07:56:33.299142572-03:00
rendered_js: false
word_count: 126
summary: This document explains how to integrate Kimi Code CLI with other tools, focusing specifically on the installation and usage of the Zsh plugin for quick terminal access.
tags:
    - kimi-cli
    - zsh
    - shell-integration
    - oh-my-zsh
    - plugin-installation
category: guide
---

--- url: /kimi-cli/en/guides/integrations.md --- # Integrations with Tools Besides using in the terminal and IDEs, Kimi Code CLI can also be integrated with other tools. ## Zsh plugin \[zsh-kimi-cli](https://github.com/MoonshotAI/zsh-kimi-cli) is a Zsh plugin that lets you quickly switch to Kimi Code CLI in Zsh. \*\*Installation\** If you use Oh My Zsh, you can install it like this: \`\`\`sh git clone https://github.com/MoonshotAI/zsh-kimi-cli.git \\ ${ZSH\_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli \`\`\` Then add the plugin in \`~/.zshrc\`: \`\`\`sh plugins=(... kimi-cli) \`\`\` Reload the Zsh configuration: \`\`\`sh source ~/.zshrc \`\`\` \*\*Usage\** After installation, press \`Ctrl-X\` in Zsh to quickly switch to Kimi Code CLI without manually typing the \`kimi\` command. ::: tip If you use other Zsh plugin managers (like zinit, zplug, etc.), please refer to the \[zsh-kimi-cli repository](https://github.com/MoonshotAI/zsh-kimi-cli) README for installation instructions. :::