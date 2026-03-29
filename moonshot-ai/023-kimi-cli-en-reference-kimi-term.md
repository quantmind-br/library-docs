---
title: ""
url: https://moonshotai.github.io/kimi-cli/en/reference/kimi-term.md
source: github_pages
fetched_at: 2026-01-28T07:56:09.939186059-03:00
rendered_js: false
word_count: 190
summary: This document provides a reference for the `kimi term` subcommand, which launches the Toad graphical terminal interface for the Kimi Code CLI. It explains how the interface connects to the ACP backend and details its configuration options and system requirements.
tags:
    - kimi-cli
    - terminal-ui
    - toad-interface
    - command-line-interface
    - acp-protocol
    - textual-ui
category: reference
---

--- url: /kimi-cli/en/reference/kimi-term.md --- # \`kimi term\` Subcommand The \`kimi term\` command launches the \[Toad](https://github.com/batrachianai/toad) terminal UI, a modern terminal interface built with \[Textual](https://textual.textualize.io/). \`\`\`sh kimi term \[OPTIONS] \`\`\` ## Description \[Toad](https://github.com/batrachianai/toad) is a graphical terminal interface for Kimi Code CLI that communicates with the Kimi Code CLI backend via the ACP protocol. It provides a richer interactive experience with better output rendering and layout. When you run \`kimi term\`, it automatically starts a \`kimi acp\` server in the background, and Toad connects to it as an ACP client. ## Options All extra options are passed through to the internal \`kimi acp\` command. For example: \`\`\`sh kimi term --work-dir /path/to/project --model kimi-k2 \`\`\` Common options: | Option | Description | |--------|-------------| | \`--work-dir PATH\` | Specify working directory | | \`--model NAME\` | Specify model | | \`--yolo\` | Auto-approve all operations | For the full list of options, see \[\`kimi\` command](./kimi-command.md). ## System requirements ::: warning Note \`kimi term\` requires Python 3.14+. If you installed Kimi Code CLI with an older Python version, you need to reinstall with Python 3.14: \`\`\`sh uv tool install --python 3.14 kimi-cli \`\`\` :::