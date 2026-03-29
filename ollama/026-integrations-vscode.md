---
title: VS Code
url: https://docs.ollama.com/integrations/vscode.md
source: llms
fetched_at: 2026-02-04T11:34:49.500895198-03:00
rendered_js: false
word_count: 82
summary: This document provides step-by-step instructions for integrating and using Ollama models within VS Code via the Copilot sidebar.
tags:
    - vscode
    - ollama
    - copilot
    - llm-integration
    - local-llms
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VS Code

## Install

Install [VS Code](https://code.visualstudio.com/download).

## Usage with Ollama

1. Open Copilot side bar found in top right window
   <div style={{ display: "flex", justifyContent: "center" }}>
     <img src="https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-sidebar.png?fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=8d841164c3a8c2e6cb502f9dece6079c" alt="VS Code chat Sidebar" width="75%" data-og-width="838" data-og-height="304" data-path="images/vscode-sidebar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-sidebar.png?w=280&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=8baa6af2c2f307707730aff500625719 280w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-sidebar.png?w=560&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=790f257751bb80213223c2d897988793 560w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-sidebar.png?w=840&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=4c1d2ba0a7e7f4c32fc7818a213eaa85 840w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-sidebar.png?w=1100&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=5470dddd3a1a42d8c599968e8a4613b1 1100w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-sidebar.png?w=1650&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=cf1e7e5ec1aa98136b76e93db93f6116 1650w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-sidebar.png?w=2500&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=6a995df960d939abd4c3ee29f3e58fac 2500w" />
   </div>
2. Select the model dropdown > **Manage models**
   <div style={{ display: "flex", justifyContent: "center" }}>
     <img src="https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-models.png?fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=9a1715817d228c9c103708da3c5ecd37" alt="VS Code model picker" width="75%" data-og-width="1064" data-og-height="462" data-path="images/vscode-models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-models.png?w=280&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=bcb1de0c96fde6b44d95a816dd81a99a 280w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-models.png?w=560&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=4941a05a32b420adabcd827ebf635097 560w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-models.png?w=840&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=1ef98e50f14c73d9027d38c2f4f28e06 840w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-models.png?w=1100&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=546c696a9857ab6721f7c084836b5921 1100w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-models.png?w=1650&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=98bf91da4065a79774c7b199a99b730f 1650w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-models.png?w=2500&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=6cbd0767ca3440fac141c2e5657f55e7 2500w" />
   </div>
3. Enter **Ollama** under **Provider Dropdown** and select desired models (e.g `qwen3, qwen3-coder:480b-cloud`)
   <div style={{ display: "flex", justifyContent: "center" }}>
     <img src="https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-model-options.png?fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=1b08a9ccc2f275e6eb039de37cceaf31" alt="VS Code model options dropdown" width="75%" data-og-width="1202" data-og-height="552" data-path="images/vscode-model-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-model-options.png?w=280&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=bdb15602e971a34695cadc7f6d90d64d 280w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-model-options.png?w=560&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=cb22702c3f6c295ae8822e8ca5f163cf 560w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-model-options.png?w=840&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=bdf5eb8776e9163afe8437f5413c67cc 840w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-model-options.png?w=1100&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=a46fc6100e91907298d223c52f306a5b 1100w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-model-options.png?w=1650&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=c134ec18e18bcdfe471fd5eb329acd9a 1650w, https://mintcdn.com/ollama-9269c548/Q0hzAGiFk9hDuXaH/images/vscode-model-options.png?w=2500&fit=max&auto=format&n=Q0hzAGiFk9hDuXaH&q=85&s=f1be99a8b9069d8d213b6a10debe73a9 2500w" />
   </div>