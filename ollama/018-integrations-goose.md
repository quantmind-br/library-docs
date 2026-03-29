---
title: Goose
url: https://docs.ollama.com/integrations/goose.md
source: llms
fetched_at: 2026-02-04T11:34:28.38496386-03:00
rendered_js: false
word_count: 184
summary: This document explains how to configure Goose Desktop and CLI to work with Ollama as a model provider for both local and cloud environments.
tags:
    - goose
    - ollama
    - configuration
    - cli
    - desktop
    - setup-guide
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Goose

## Goose Desktop

Install [Goose](https://block.github.io/goose/docs/getting-started/installation/) Desktop.

### Usage with Ollama

1. In Goose, open **Settings** → **Configure Provider**.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-settings.png?fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=ba9aaea6b535f03456dbafb0ba48018b" alt="Goose settings Panel" width="75%" data-og-width="1300" data-og-height="732" data-path="images/goose-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-settings.png?w=280&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=63e0cc6d307d8a6c1b7ba8bb7b1b2532 280w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-settings.png?w=560&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=bf90aaf22a8f6307d99597964433603c 560w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-settings.png?w=840&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=4fd50ee906a26ecde5f49575bcad1700 840w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-settings.png?w=1100&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=01abb63a474ea8a2e47fe1b4ee7bd752 1100w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-settings.png?w=1650&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=7188a96a903d03fe68004faeb743156c 1650w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-settings.png?w=2500&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=92e96516a86f243a182939145d5536eb 2500w" />
</div>

2. Find **Ollama**, click **Configure**
3. Confirm **API Host** is `http://localhost:11434` and click Submit

### Connecting to ollama.com

1. Create an [API key](https://ollama.com/settings/keys) on ollama.com and save it in your `.env`
2. In Goose, set **API Host** to `https://ollama.com`

## Goose CLI

Install [Goose](https://block.github.io/goose/docs/getting-started/installation/) CLI

### Usage with Ollama

1. Run `goose configure`
2. Select **Configure Providers** and select **Ollama**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-cli.png?fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=3f34e0d16cbdf89858115b8c64d6dc08" alt="Goose CLI" width="50%" data-og-width="650" data-og-height="546" data-path="images/goose-cli.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-cli.png?w=280&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=d869883c3d68749aa534907cab2fcd5a 280w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-cli.png?w=560&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=b6e2eb41567eb401582c42b2289e2a98 560w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-cli.png?w=840&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=35c249c4cf90b3697d44e756d728d47c 840w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-cli.png?w=1100&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=957ef7e49a7b852a8995a4a7a04aea2d 1100w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-cli.png?w=1650&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=ebfa2bca9b17e3183d79c9534b24f3bf 1650w, https://mintcdn.com/ollama-9269c548/Qrfd4TFdx51mx0J_/images/goose-cli.png?w=2500&fit=max&auto=format&n=Qrfd4TFdx51mx0J_&q=85&s=b6ce0d3e1b9d07f3e28935767b0cf5e1 2500w" />
</div>

3. Enter model name (e.g `qwen3`)

### Connecting to ollama.com

1. Create an [API key](https://ollama.com/settings/keys) on ollama.com and save it in your `.env`
2. Run `goose configure`
3. Select **Configure Providers** and select **Ollama**
4. Update **OLLAMA\_HOST** to `https://ollama.com`