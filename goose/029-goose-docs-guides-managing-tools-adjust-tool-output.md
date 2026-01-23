---
title: Adjusting Tool Output Verbosity | goose
url: https://block.github.io/goose/docs/guides/managing-tools/adjust-tool-output
source: github_pages
fetched_at: 2026-01-22T22:14:05.315981656-03:00
rendered_js: true
word_count: 123
summary: This document explains how to configure the display style of tool interactions in the goose Desktop chat window, allowing users to choose between detailed and concise views.
tags:
    - goose-desktop
    - chat-settings
    - response-styles
    - tool-calls
    - ui-preferences
category: configuration
---

Response Styles customize how tool interactions are displayed in the goose Desktop chat window.

To change this setting:

1. Click the button on the top-left to open the sidebar.
2. Click the `Settings` button on the sidebar.
3. Click `Chat`.
4. Under `Response Styles`, select either `Detailed` or `Concise`.

<!--THE END-->

- **Concise** (Default)
  
  - Tool calls are collapsed by default
  - Shows only which tool goose used
  - Best for users focusing on results rather than technical details
- **Detailed**
  
  - Tool calls are expanded by default
  - Shows the details of tool calls and their responses
  - Best for debugging or learning how goose works

This setting only affects the default state of tool calls in the conversation. You can always manually expand or collapse any tool call regardless of your chosen style.