---
title: 'Figma Remote MCP: Create a Website from a Figma File | Guides | Warp'
url: https://docs.warp.dev/guides/external-tools-and-integrations/figma-remote-mcp-create-a-website-from-a-figma-file-from-scratch
source: sitemap
fetched_at: 2026-04-29T15:06:47.730182178-03:00
rendered_js: false
word_count: 331
summary: This guide explains how to connect Warp to the Figma remote MCP server to enable AI-powered code generation directly from design files.
tags:
    - warp-terminal
    - figma
    - mcp-server
    - code-generation
    - ui-development
    - ai-workflow
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Connect Warp to the Figma remote MCP server to generate front-end code directly from Figma designs, complete with screenshots, metadata, and design system context.

## What is a Remote MCP Server?

A remote MCP server runs outside your local machine. Warp connects to it via secure network call — no manual process, port, or token management.

## Connect Figma MCP to Warp

1. Copy the Figma MCP configuration:

```json
{
  "Figma": {
    "url": "https://mcp.figma.com/mcp"
  }
}
```

2. In Warp, paste the JSON — Warp opens an OAuth login window automatically.
3. Log in once with your Figma account credentials.

> [!info]
> A Figma Dev account is required.

## What the Figma MCP Server Provides

| Tool | Function |
|---|---|
| `get_figma_file_screenshot` | Helps AI visualize layout and element relationships |
| `create_design_system_rules` | Components, variables, and styles for consistent code |
| `extract_code_from_design` | Extract code from Figma designs for direct use |
| `generate_mock_data` | Text, images, and layer names for realistic mock data |

## Generate a Website from a Figma File

1. Copy your Figma file link: right-click → *Copy / Paste As → Copy Link to Selection*
2. Paste a prompt in Warp:

```
Create a website from this Figma file: <LINK HERE>
Follow the design layout and use these guidelines:
- Match spacing and typography from the design
- Use Tailwind CSS and TypeScript
- Make components reusable
```

Warp pulls all necessary context from the Figma MCP server and begins generating code diffs.

## Iterating on Output

- Warp generates a working site structure in under five minutes.
- Missing assets are automatically referenced in an `assets/` folder.
- Warp prompts you to add missing files before continuing.

## Persistent Input

Warp's **persistent input** allows mid-process updates. If you forget an asset:

```
I've uploaded the Misho logo to the assets folder.
```

Warp detects and uses it automatically within the same generation session.

> [!tip]
> You can go from Figma design to a functioning website in under 20 minutes — all powered by Warp's AI coding environment.

## Recap

- Warp supports remote MCP servers (Figma, GitHub, Sentry, Linear, and more).
- OAuth login removes manual token handling.
- Figma MCP enables rapid, context-aware code generation.
- Persistent input and real-time iteration make design-to-code workflows seamless.

#figma
