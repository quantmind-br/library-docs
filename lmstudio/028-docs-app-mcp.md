---
title: Use MCP Servers
url: https://lmstudio.ai/docs/app/mcp
source: sitemap
fetched_at: 2026-04-07T21:29:13.505715015-03:00
rendered_js: false
word_count: 316
summary: This document explains that LM Studio now functions as a Model Context Protocol (MCP) Host, allowing users to connect local or remote MCP servers; however, it strongly cautions users about the security risks associated with installing untrusted servers.
tags:
    - mcp-host
    - server-installation
    - security-warning
    - config-file
    - lm-studio
category: guide
---

Starting LM Studio 0.3.17, LM Studio acts as an **Model Context Protocol (MCP) Host**. This means you can connect MCP servers to the app and make them available to your models.

### Be cautious[](#be-cautious)

Never install MCPs from untrusted sources.

Some MCP servers can run arbitrary code, access your local files, and use your network connection. Always be cautious when installing and using MCP servers. If you don't trust the source, don't install it.

## Use MCP servers in LM Studio[](#use-mcp-servers-in-lm-studio)

Starting 0.3.17 (b10), LM Studio supports both local and remote MCP servers. You can add MCPs by editing the app's `mcp.json` file or via the ["Add to LM Studio" Button](https://lmstudio.ai/docs/app/mcp/deeplink), when available. LM Studio currently follows Cursor's `mcp.json` notation.

## Install new servers: `mcp.json`[](#install-new-servers-mcpjson "Link to 'Install new servers: ,[object Object]'")

Switch to the "Program" tab in the right hand sidebar. Click `Install > Edit mcp.json`.

![undefined](https://lmstudio.ai/assets/docs/install-mcp.png)

This will open the `mcp.json` file in the in-app editor. You can add MCP servers by editing this file.

![undefined](https://lmstudio.ai/assets/docs/mcp-editor.png)

Edit mcp.json using the in-app editor

### Example MCP to try: Hugging Face MCP Server[](#example-mcp-to-try-hugging-face-mcp-server)

This MCP server provides access to functions like model and dataset search.

[](https://lmstudio.ai/install-mcp?name=hf-mcp-server&config=eyJ1cmwiOiJodHRwczovL2h1Z2dpbmdmYWNlLmNvL21jcCIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciA8WU9VUl9IRl9UT0tFTj4ifX0%3D)

[![Add MCP Server hf-mcp-server to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=hf-mcp-server&config=eyJ1cmwiOiJodHRwczovL2h1Z2dpbmdmYWNlLmNvL21jcCIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciA8WU9VUl9IRl9UT0tFTj4ifX0%3D)

[![Add MCP Server hf-mcp-server to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-dark.svg)](https://lmstudio.ai/install-mcp?name=hf-mcp-server&config=eyJ1cmwiOiJodHRwczovL2h1Z2dpbmdmYWNlLmNvL21jcCIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciA8WU9VUl9IRl9UT0tFTj4ifX0%3D)

```

{
  "mcpServers": {
    "hf-mcp-server": {
      "url": "https://huggingface.co/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_HF_TOKEN>"
      }
    }
  }
}
```

###### You will need to replace `<YOUR_HF_TOKEN>` with your actual Hugging Face token. Learn more [here](https://huggingface.co/docs/hub/en/security-tokens).

Use the [deeplink button](https://lmstudio.ai/docs/app/mcp/deeplink), or copy the JSON snippet above and paste it into your `mcp.json` file.

* * *

## Gotchas and Troubleshooting[](#gotchas-and-troubleshooting "Link to 'Gotchas and Troubleshooting'")

- Never install MCP servers from untrusted sources. Some MCPs can have far reaching access to your system.
- Some MCP servers were designed to be used with Claude, ChatGPT, Gemini and might use excessive amounts of tokens.
  
  - Watch out for this. It may quickly bog down your local model and trigger frequent context overflows.
- When adding MCP servers manually, copy only the content after `"mcpServers": {` and before the closing `}`.