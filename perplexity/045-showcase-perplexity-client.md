---
title: Perplexity Client | Desktop AI Chat Interface with API Controls
url: https://docs.perplexity.ai/docs/cookbook/showcase/perplexity-client.md
source: llms
fetched_at: 2026-02-04T07:22:27.076118251-03:00
rendered_js: false
word_count: 473
summary: This document introduces and provides setup instructions for the Perplexity Client, an Electron-based desktop application designed for advanced interaction with Perplexity's Sonar API.
tags:
    - electron-app
    - perplexity-api
    - sonar-api
    - desktop-client
    - api-debugging
    - node-js
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Perplexity Client | Desktop AI Chat Interface with API Controls

> An Electron-based desktop client for Perplexity API with advanced features like model selection, custom system prompts, and API debugging mode

**Perplexity Client** is an Electron-based desktop application that provides a polished interface for interacting with Perplexity's Sonar API. It exposes advanced API parameters like max tokens, making it ideal for developers who want fine-grained control over their AI interactions while enjoying a beautiful, macOS-inspired UI.

<img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-main.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=a7733850ea803dbaf807b54fcc84b918" alt="Perplexity Client Interface" data-og-width="1344" width="1344" data-og-height="750" height="750" data-path="docs/cookbook/static/img/perplexity-client-main.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-main.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=e764724110e132913627b67a16a572e4 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-main.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=56d847b6ea4ace24eef279db77dde906 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-main.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=59163c2d7b92a98b64977d0603aa5273 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-main.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=d8b89c18cb62b6dbb81c8cda458b97cd 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-main.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=04b6404187207f0af58efb14f3f89d65 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-main.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=090ff72a2193e7eb0d650dcdd46713a5 2500w" />

## Features

* **Multiple Sonar Models** with support for Sonar, Sonar Pro, and Sonar Reasoning Pro
* **Custom Spaces** with save/load functionality for different use cases
* **API Parameter Controls** including max tokens adjustments
* **API Debugging Mode** showing full request/response payloads for troubleshooting
* **Token Usage Tracking** to monitor API consumption and costs
* **Focus Modes** for specialized tasks like coding, writing, and research

## Prerequisites

* Node.js v16 or higher
* npm or yarn
* Perplexity API key

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/straight-heart/Perplexity-client-.git
cd Perplexity-client-

# Install dependencies
npm install

npm run dev
```

## Build

Build the application for your platform:

```bash  theme={null}
npm run build:win    # Windows
npm run build:mac    # macOS
npm run build:linux  # Linux
```

## Configuration

API keys are managed directly within the application:

1. Launch the app and open Settings (gear icon)
2. In the **API Keys** section, click **Add Key**
3. Enter your Perplexity API key
4. The key is stored securely and persists across sessions

For custom system prompts, use the **Spaces** feature to save and switch between different instruction sets.

## Usage

1. **Launch**: Run `npm run dev` or use the built application
2. **Add API Key**: Open Settings and add your Perplexity API key
3. **Select Model**: Use the dropdown to choose between Sonar variants
4. **Create Spaces**: Set up custom system prompts for different tasks
5. **Chat**: Start conversing with real-time streaming responses
6. **Debug**: Enable API debugging to see full request/response details
7. **Track Usage**: Monitor token consumption in the Settings panel

## Screenshots

| Feature                      | Preview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Spaces (Custom Instructions) | <img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-spaces.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=f95967a6f2d8e6240b6b4710e20564fd" alt="Spaces" data-og-width="313" width="313" data-og-height="103" height="103" data-path="docs/cookbook/static/img/perplexity-client-spaces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-spaces.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=fa4922fa54286ae04fa738f8bd338f6f 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-spaces.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=62cf1baa87ca10bdf64da978f0c70f4a 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-spaces.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=64366083c7bdc0946ea8173bf6f931cc 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-spaces.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=de02bc75ba418ce05a9be4b7e582fe76 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-spaces.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=0a0c0f6a81d650dd73c8a6cc21fd30a3 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-spaces.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=3b95da1d775d0392d7e6b9d1d0ac17a2 2500w" />                                     |
| Model & Parameter Controls   | <img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-parameters.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=32b22baf3867a515f1865fbca64fb334" alt="Parameters" data-og-width="313" width="313" data-og-height="278" height="278" data-path="docs/cookbook/static/img/perplexity-client-parameters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-parameters.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=424691c05069fc6d31b87f839a4ab55c 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-parameters.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=f127adf4d62c7e5d9e1a3255d3fd30e6 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-parameters.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=1e9e1a87cd41364f7ed0da19ee3f81d7 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-parameters.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=b1909af1e2f411bab9f8c310e5000062 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-parameters.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=0ccaea89cd481806ee8b1577af1fa2cc 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-parameters.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=1b368dc3c7fba3c918a65409ec465dcb 2500w" /> |
| API Debugging Mode           | <img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-debug.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=005dc054f0145c5cf1a0888587fc4edd" alt="Debug" data-og-width="828" width="828" data-og-height="555" height="555" data-path="docs/cookbook/static/img/perplexity-client-debug.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-debug.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=17697a41b81b797552601609900f68a9 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-debug.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=8b58e641f367903db61173e319648230 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-debug.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=78f342a84a68ef9d7ce3fc9d2d26bbdd 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-debug.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=3ca875db39f3554d1b9ce9ea29da01d0 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-debug.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=857d25f1e42657b2b8f871864220597a 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-debug.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=1f507357c69c6d0c945d7097a4f5351b 2500w" />                                              |
| Theme Selection              | <img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-themes.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=3b9f3bf0966bd73023ad56ca1ff826ca" alt="Themes" data-og-width="473" width="473" data-og-height="216" height="216" data-path="docs/cookbook/static/img/perplexity-client-themes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-themes.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=09ef657bac2d6cb00b4df4ad4bd3c10b 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-themes.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=edb6831e1f7100b8fc4126ab427fa739 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-themes.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=c1f93a699fa14d90d7009844d9e241d1 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-themes.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=3bb2b7f5f815ae1b9c8e23722160d42f 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-themes.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=58c20a401df105a216d412e63737b546 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/perplexity-client-themes.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=31984db63646929f663c410292f43001 2500w" />                                     |

## Limitations

* Desktop only (Windows, macOS, Linux) — no mobile or web version
* Requires internet connection for API calls
* API key required for functionality

## Links

* [GitHub Repository](https://github.com/straight-heart/Perplexity-client-)