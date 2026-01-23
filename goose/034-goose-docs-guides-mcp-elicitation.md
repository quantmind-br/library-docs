---
title: MCP Elicitation | goose
url: https://block.github.io/goose/docs/guides/mcp-elicitation
source: github_pages
fetched_at: 2026-01-22T22:14:08.438122575-03:00
rendered_js: true
word_count: 198
summary: This document explains the MCP Elicitation feature in goose, which enables extensions to request specific information from users through interactive forms instead of making assumptions.
tags:
    - mcp-elicitation
    - goose
    - model-context-protocol
    - user-input
    - extension-development
category: concept
---

MCP Elicitation allows goose to pause and ask you for specific information when an extension needs it. Instead of guessing or making assumptions, goose presents a form requesting exactly what's needed to continue.

This feature is automatically enabled in goose. When an extension that supports elicitation needs information from you, a form will appear in your session.

info

[MCP Elicitation](https://modelcontextprotocol.io/specification/draft/client/elicitation) is a feature in the Model Context Protocol. goose supports form mode requests.

## How MCP Elicitation Works[​](#how-mcp-elicitation-works "Direct link to How MCP Elicitation Works")

When an extension needs information, goose pauses and presents a form for you to fill out. You can submit your response or cancel the request.

- goose Desktop
- goose CLI

A form appears inline in the chat with:

- Fields for the requested data
- Required fields marked with an asterisk (\*)
- Default values you can accept or change
- A **Submit** button to send your response

After submitting, you'll see a confirmation message.

Timeout

Elicitation requests timeout after 5 minutes. If you don't respond in time, the request is cancelled and goose will continue without the information.

## For Extension Developers[​](#for-extension-developers "Direct link to For Extension Developers")

Want to add elicitation to your own extensions? See the [MCP Elicitation specification](https://modelcontextprotocol.io/specification/draft/client/elicitation) to learn how MCP servers can request structured input from users.