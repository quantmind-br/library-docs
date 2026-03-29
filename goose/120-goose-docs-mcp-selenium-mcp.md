---
title: Selenium Extension | goose
url: https://block.github.io/goose/docs/mcp/selenium-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:48.932290853-03:00
rendered_js: true
word_count: 178
summary: This document explains how to integrate the Selenium MCP Server with goose to automate web browser interactions and generate test automation scripts.
tags:
    - selenium
    - mcp-server
    - goose-extension
    - browser-automation
    - test-automation
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [Selenium MCP Server](https://github.com/angiejones/mcp-selenium) as a goose extension to automate browser interactions such as navigating web pages and completing forms.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=%40angiejones%2Fmcp-selenium&id=selenium-mcp&name=Selenium%20MCP&description=automates%20browser%20interactions)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

Let's use goose to build a test automation project from scratch! We'll use the Selenium MCP to automate filling out a web form, then have goose generate a Selenium project with the code so that we can run these tests again when needed.

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> Use selenium to go to the heroku formy site and fill out the form page with generic data. then can you turn what you've done into an automation script for me? I would like it in Java. Also use the Page Object Model pattern.

### goose Output[​](#goose-output "Direct link to goose Output")