---
title: X-cmd - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-x-cmd-readme
source: crawler
fetched_at: 2026-01-29T07:33:56.361595591-03:00
rendered_js: false
word_count: 182
summary: A guide and collection of examples for using X-cmd to interact with Mistral AI models via the command line.
tags:
    - x-cmd
    - mistral-ai
    - cli
    - ai
    - tutorial
category: guide
---

## The Mistral AI Command Line Client with x-cmd

The **mistral module** is a command-line client tool built by the x-cmd team using the Mistral AI API. Written in posix shell and awk, it uses `curl` to send API requests.

## Getting started

### Installing x-cmd

- x-cmd is compatible with **Windows**, **Linux**, and **macOS**, making installation easy and straightforward
- For more installation methods and instructions, please refer to the [official documentation](https://docs.mistral.ai/cookbooks/third_party-x-cmd-readme).

### Configuring `x mistral`

Obtaining a **Mistral AI API Key**: [https://console.mistral.ai/api-keys/](https://docs.mistral.ai/cookbooks/third_party-x-cmd-readme)

![x mistral init](https://docs.mistral.ai/cookbooks/third_party/x-cmd/static/mistral.init.png)

### Use Mistral AI

- `x mistral` allows you to **send messages or files to Mistral AI**. And to make things easier for users, x-cmd also provides the `@mistral` command as an alias for the `x mistral` command.
  
  ![@mistral file](https://docs.mistral.ai/cookbooks/third_party/x-cmd/static/mistral.chat.1.png)
- `x mistral` can help analyze command results and supports **opening a dialogue in interactive mode**.
  
  **[`x jina r`](https://docs.mistral.ai/cookbooks/third_party-x-cmd-readme):** Uses **Jina.ai** to extract content from web pages.
  
  ![mistral repl](https://docs.mistral.ai/cookbooks/third_party/x-cmd/static/x.mistral.png)

## Command Line Options

We offer the `x mistral` and `@mistral` commands, where `x mistral` focuses on model configuration and download management, while `@mistral` emphasizes model applications. Their command-line options are as follows:

1. `x mistral`:
2. `@mistral`: