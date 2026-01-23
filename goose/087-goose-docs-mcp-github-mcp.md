---
title: GitHub Extension | goose
url: https://block.github.io/goose/docs/mcp/github-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:15.725535134-03:00
rendered_js: true
word_count: 136
summary: This document provides instructions for integrating and configuring the GitHub MCP Server extension within goose to enable automated repository management and file operations.
tags:
    - github-integration
    - mcp-server
    - goose-extension
    - repository-management
    - configuration-guide
    - automation
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [GitHub MCP Server](https://github.com/github/github-mcp-server) as a goose extension to enable file operations, repository management, search functionality, and more.

TLDR

- goose Desktop
- goose CLI

**Custom Request Header**

```
Authorization: Bearer <YOUR_GITHUB_PERSONAL_ACCESS_TOKEN>
```

## Configuration[​](#configuration "Direct link to Configuration")

These steps configure the Remote MCP Server. For other deployment options, see the [official GitHub MCP Server documentation](https://github.com/github/github-mcp-server).

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?type=streamable_http&url=https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F&id=github&name=GitHub&description=GitHub%20repository%20management%20and%20operations&header=Authorization%3DBearer%20YOUR_GITHUB_PERSONAL_ACCESS_TOKEN)
2. Click `Yes` to confirm the installation
3. Get your [GitHub Personal Access Token](https://github.com/settings/personal-access-tokens) and paste it in
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

When creating my [GitHub Personal Access Token](https://github.com/settings/personal-access-tokens), I gave it the following access:

- Repository: [goose-demo](https://github.com/angiejones/goose-demo)
- Read access to metadata
- Read and Write access to code, commit status, issues, and pull requests

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
create a new branch called hello-world in my angiejones/goose-demo repository. Update the README.md file to say "this was written by goose" and commit it. Open a pull request with your changes.
```

### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you create a new branch, update the README, and open a pull request. Let me break this down into steps:

1. First, let's create the new branch called "hello-world" in your repository
2. Then update the README.md file
3. Finally, create a pull request

Let me execute these steps:

1. Creating the new branch:

─── create_branch | github ──────────────────────────
branch: hello-world
owner: angiejones
repo: goose-demo

2. Now, updating the README.md file in the new branch:

─── create_or_update_file | github ──────────────────────────
branch: hello-world
content: this was written by goose
message: Update README.md with goose message
owner: angiejones
path: README.md
repo: goose-demo


3. Finally, creating the pull request:

─── create_pull_request | github ──────────────────────────
base: main
body: ...
head: hello-world
owner: angiejones
repo: goose-demo
title: Update README.md


Great! I've completed all the requested tasks:
1. Created a new branch called "hello-world"
2. Updated the README.md file with the text "this was written by goose"
3. Created a pull request to merge these changes into the main branch

You can view the pull request at: https://github.com/angiejones/goose-demo/pull/1

The pull request is now ready for your review. Would you like me to do anything else with it?
```