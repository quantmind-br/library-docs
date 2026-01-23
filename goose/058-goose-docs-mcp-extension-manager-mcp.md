---
title: Extension Manager | goose
url: https://block.github.io/goose/docs/mcp/extension-manager-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:08.17079055-03:00
rendered_js: true
word_count: 340
summary: This document explains how the Extension Manager for goose enables dynamic discovery and management of extensions to optimize tool selection and performance during active sessions.
tags:
    - extension-manager
    - goose-ai
    - tool-selection
    - performance-optimization
    - dynamic-extensions
    - resource-management
category: guide
---

You don't always need to manually manage extensions. The Extension Manager extension enables goose to dynamically discover, enable, and disable extensions during active sessions. Based on the task you give it, goose recognizes when it needs a specific extension, enables it when required, and suggests disabling unused extensions if the bloat is eating up your context window.

Simply describe your task, and goose will handle the extension management automatically.

## Configuration[​](#configuration "Direct link to Configuration")

Platform Extension

This is a [built-in platform extension](https://block.github.io/goose/docs/getting-started/using-extensions#built-in-platform-extensions) that's enabled by default. Platform extensions provide core functionality and are used within goose just like MCP server extensions.

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Extensions` in the sidebar
3. Toggle `Extension Manager` on

## Why Use Extension Manager?[​](#why-use-extension-manager "Direct link to Why Use Extension Manager?")

goose can work with many extensions, but having too many enabled at once can:

- Overwhelm the LLM with too many tool choices
- Reduce the quality of tool selection
- Slow down response times
- Exceed recommended limits (5 extensions or 50 tools)

The Extension Manager solves this by letting goose:

- **Discover** what extensions are available
- **Enable** extensions only when needed for specific tasks
- **Disable** extensions when they're no longer required

This creates a more focused, efficient experience where goose has access to exactly the tools it needs, when it needs them.

Recommended Limits

For optimal performance, aim for **5 or fewer active extensions** with a total of **50 or fewer tools**. The Extension Manager helps you stay within these limits by enabling task-specific extensions only when needed.

The Extension Manager provides these tools:

ToolDescriptionUse Case`search_available_extensions`Discover extensions that can be enabled or disabledFinding the right extension for a task`manage_extensions`Enable or disable an extension by nameLoading/unloading extensions dynamically`list_resources`List resources from extensions (if supported)Discovering available data sources`read_resource`Read specific resource content (if supported)Accessing extension-provided data

tip

The resource tools (`list_resources` and `read_resource`) are only available when at least one enabled extension supports resources.

## Example Usage[​](#example-usage "Direct link to Example Usage")

Let's enable an extension when we need it. In this example, we'll enable the GitHub extension to work with repositories.

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
List all my GitHub repositories
```

### goose Output[​](#goose-output "Direct link to goose Output")

Desktop

```
I'll enable the GitHub extension for you so we can work with repositories.

MANAGE_EXTENSIONS
action: enable
extension_name: github

✅ The extension 'github' has been installed successfully

The GitHub extension is now active.

I'll list your GitHub repositories using the GitHub extension.

LIST_REPOSITORIES

Here are your repositories:

...

Would you like to work with any of these repositories?
```