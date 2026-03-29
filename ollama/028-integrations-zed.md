---
title: Zed
url: https://docs.ollama.com/integrations/zed.md
source: llms
fetched_at: 2026-02-04T11:34:53.760029109-03:00
rendered_js: false
word_count: 162
summary: This document provides step-by-step instructions for installing the Zed editor and configuring it to work with Ollama as an LLM provider.
tags:
    - zed
    - ollama
    - llm
    - editor-integration
    - setup
    - configuration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zed

## Install

Install [Zed](https://zed.dev/download).

## Usage with Ollama

1. In Zed, click the **star icon** in the bottom-right corner, then select **Configure**.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-settings.png?fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=0a63b1359b1472dde2cdf6c37e314e22" alt="Zed star icon in bottom right corner" width="50%" data-og-width="944" data-og-height="224" data-path="images/zed-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-settings.png?w=280&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=bfc876e9fb924521ab6cdb7ce0f8f8b2 280w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-settings.png?w=560&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=c4b923c2b68da82a39d5834f71e595ec 560w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-settings.png?w=840&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=427b91b58eaff6245edb4d19cacbe13c 840w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-settings.png?w=1100&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=3c135be074ecb974ea19b4e286ec4439 1100w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-settings.png?w=1650&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=974ceda223ced89cf821c3f1899040db 1650w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-settings.png?w=2500&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=d75863b4421cc3f5229b673d673ec7eb 2500w" />
</div>

2. Under **LLM Providers**, choose **Ollama**
3. Confirm the **Host URL** is `http://localhost:11434`, then click **Connect**
4. Once connected, select a model under **Ollama**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-ollama-dropdown.png?fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=722c315dcb2563079865eccae2e0c56d" alt="Zed star icon in bottom right corner" width="50%" data-og-width="646" data-og-height="370" data-path="images/zed-ollama-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-ollama-dropdown.png?w=280&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=3f1d23fad0d96ddd6eacb1e79f2e4489 280w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-ollama-dropdown.png?w=560&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=a83649ed5beedb5fa741276d3f0de691 560w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-ollama-dropdown.png?w=840&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=5338e29259c73686c55ccc42a1ac1e11 840w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-ollama-dropdown.png?w=1100&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=63cca84dff4a209986daaadd2f1a1fd4 1100w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-ollama-dropdown.png?w=1650&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=51f3d300d365ffc31661b83985fa2008 1650w, https://mintcdn.com/ollama-9269c548/qP80N64oeC4tOgE5/images/zed-ollama-dropdown.png?w=2500&fit=max&auto=format&n=qP80N64oeC4tOgE5&q=85&s=d82841949d806094684e5e28c6c0a064 2500w" />
</div>

## Connecting to ollama.com

1. Create an [API key](https://ollama.com/settings/keys) on **ollama.com**
2. In Zed, open the **star icon** → **Configure**
3. Under **LLM Providers**, select **Ollama**
4. Set the **API URL** to `https://ollama.com`