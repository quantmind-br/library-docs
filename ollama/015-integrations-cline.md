---
title: Cline
url: https://docs.ollama.com/integrations/cline.md
source: llms
fetched_at: 2026-02-04T11:34:22.051240666-03:00
rendered_js: false
word_count: 164
summary: This document provides instructions for installing and configuring the Cline coding tool to work with Ollama, including setting up API providers and optimizing context window size.
tags:
    - cline
    - ollama
    - ide-setup
    - configuration-guide
    - context-window
    - coding-assistant
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cline

## Install

Install [Cline](https://docs.cline.bot/getting-started/installing-cline) in your IDE.

## Usage with Ollama

1. Open Cline settings > `API Configuration` and set `API Provider` to `Ollama`
2. Select a model under `Model` or type one (e.g. `qwen3`)
3. Update the context window to at least 32K tokens under `Context Window`

<Note>Coding tools require a larger context window. It is recommended to use a context window of at least 32K tokens. See [Context length](/context-length) for more information.</Note>

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/DILXUjvsEb6UDNxN/images/cline-settings.png?fit=max&auto=format&n=DILXUjvsEb6UDNxN&q=85&s=2d2755de6b2e06cd513119abf389acd0" alt="Cline settings configuration showing API Provider set to Ollama" width="50%" data-og-width="596" data-og-height="826" data-path="images/cline-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/DILXUjvsEb6UDNxN/images/cline-settings.png?w=280&fit=max&auto=format&n=DILXUjvsEb6UDNxN&q=85&s=526c814bcfce0e2d812a6bfeb708ec74 280w, https://mintcdn.com/ollama-9269c548/DILXUjvsEb6UDNxN/images/cline-settings.png?w=560&fit=max&auto=format&n=DILXUjvsEb6UDNxN&q=85&s=03865bcf135e8ac371c526a18fc4ba8b 560w, https://mintcdn.com/ollama-9269c548/DILXUjvsEb6UDNxN/images/cline-settings.png?w=840&fit=max&auto=format&n=DILXUjvsEb6UDNxN&q=85&s=40a0ed4a094e6c3f753ef6ae8820b949 840w, https://mintcdn.com/ollama-9269c548/DILXUjvsEb6UDNxN/images/cline-settings.png?w=1100&fit=max&auto=format&n=DILXUjvsEb6UDNxN&q=85&s=f13028b0f2d177f7b3cb9eb3d6332416 1100w, https://mintcdn.com/ollama-9269c548/DILXUjvsEb6UDNxN/images/cline-settings.png?w=1650&fit=max&auto=format&n=DILXUjvsEb6UDNxN&q=85&s=00ab8386e21b6aa32e4dc4d3bbd02817 1650w, https://mintcdn.com/ollama-9269c548/DILXUjvsEb6UDNxN/images/cline-settings.png?w=2500&fit=max&auto=format&n=DILXUjvsEb6UDNxN&q=85&s=27a89d86786164ff499d03feab00d375 2500w" />
</div>

## Connecting to ollama.com

1. Create an [API key](https://ollama.com/settings/keys) from ollama.com
2. Click on `Use custom base URL` and set it to `https://ollama.com`
3. Enter your **Ollama API Key**
4. Select a model from the list

### Recommended Models

* `qwen3-coder:480b`
* `deepseek-v3.1:671b`