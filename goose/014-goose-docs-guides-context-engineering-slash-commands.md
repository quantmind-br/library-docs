---
title: Custom Slash Commands | goose
url: https://block.github.io/goose/docs/guides/context-engineering/slash-commands
source: github_pages
fetched_at: 2026-01-22T22:13:41.782665847-03:00
rendered_js: true
word_count: 119
summary: This document explains how to create and use custom slash commands as shortcuts to trigger specific recipes within chat sessions. It details how to invoke commands, pass parameters, and how the model processes recipe instructions as context.
tags:
    - goose
    - slash-commands
    - custom-shortcuts
    - recipes
    - workflow-automation
category: guide
---

Custom slash commands are personalized shortcuts to run [recipes](https://block.github.io/goose/docs/guides/recipes). If you have a recipe that runs a daily report, you can create a custom slash command to invoke that recipe from within a session:

Assign a custom command to a recipe.

In any chat session, type your custom command with a leading slash at the start of your message:

You can pass one parameter after the command (if needed). Quotation marks are optional:

```
/translator where is the library
```

When you run a recipe using a slash command, the recipe's instructions and prompt fields are sent to your model and loaded into the conversation, but not displayed in chat. The model responds using the recipe's context and instructions just as if you opened it directly.