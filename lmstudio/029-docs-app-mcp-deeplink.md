---
title: '`Add to LM Studio` Button'
url: https://lmstudio.ai/docs/app/mcp/deeplink
source: sitemap
fetched_at: 2026-04-07T21:29:15.706023665-03:00
rendered_js: false
word_count: 135
summary: This document explains how users can generate a deeplink to one-click install custom Model Control Panel (MCP) servers directly into LM Studio, detailing the required JSON format and URL parameters.
tags:
    - mcp-server
    - lm-studio
    - deeplink
    - installation
    - json-format
    - hosting
category: guide
---

You can install MCP servers in LM Studio with one click using a deeplink.

Starting with version 0.3.17 (10), LM Studio can act as an MCP host. Learn more about it [here](https://lmstudio.ai/docs/app/mcp).

* * *

## Generate your own MCP install link[](#generate-your-own-mcp-install-link)

Enter your MCP JSON entry to generate a deeplink for the `Add to LM Studio` button.

No MCP Server Detected

Click on the button to copy the Markdown to clipboard.

## Try an example[](#try-an-example "Link to 'Try an example'")

Try to copy and paste the following into the link generator above.

```

{
  "hf-mcp-server": {
    "url": "https://huggingface.co/mcp",
    "headers": {
      "Authorization": "Bearer <YOUR_HF_TOKEN>"
    }
  }
}
```

### Deeplink format[](#deeplink-format)

```

lmstudio://add_mcp?name=hf-mcp-server&config=eyJ1cmwiOiJodHRwczovL2h1Z2dpbmdmYWNlLmNvL21jcCIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciA8WU9VUl9IRl9UT0tFTj4ifX0%3D
```

#### Parameters

lmstudio:// : protocol

The protocol scheme to open LM Studio

add\_mcp : path

The action to install an MCP server

name : query parameter

The name of the MCP server to install

config : query parameter

Base64 encoded JSON configuration for the MCP server