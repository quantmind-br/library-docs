---
title: Vercel Extension | goose
url: https://block.github.io/goose/docs/mcp/vercel-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:58.398072305-03:00
rendered_js: true
word_count: 133
summary: This document provides instructions for integrating the Vercel MCP server into goose to manage Vercel projects and monitor deployment status through an AI agent.
tags:
    - vercel
    - mcp-server
    - goose-extension
    - project-management
    - deployment-tracking
    - ai-integration
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [Vercel MCP Server](https://vercel.com/docs/mcp/vercel-mcp) as a goose extension to manage your Vercel projects and deployment status directly from goose.

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run installation commands, which use `npx`.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?type=streamable_http&url=https%3A%2F%2Fmcp.vercel.com&id=Vercel&name=Vercel&description=Access%20Vercel%20deployments%20and%20manage%20projects)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
Get a list of my Vercel projects via the Vercel MCP server, and build me a table showing when I last deployed the project and other details I should know about their status.
```

The first time you use the Vercel MCP server, you will be prompted to authenticate with Vercel via OAuth.

### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you get your Vercel projects and create a table with deployment details. Let me first get your teams to identify which team to use for listing projects.

> List Teams

> teamId: team_p3hPvXImXmdkbZ36FoqhoyYo


Now let me get the deployment information for each project to see the last deployment dates and status:

> projectId, teamId

> projectId, teamId

> projectId, teamId

Now let me get more details about each project to provide a comprehensive table:

> projectId, teamId

> projectId, teamId

> projectId, teamId

Based on the data from your Vercel projects, here's a comprehensive table showing your project status and deployment information:

Vercel Projects Overview
```

Project NameFrameworkStatusLast DeploymentCustom DomainGitHub RepoNotesproject1Next.js🟡 BuildingSep 8, 2025 (Today)Noneabout-meCurrently building - newest projectproject2Next.js✅ ReadyMay 12, 2025example.comstarter-blogNotes for site 2project3Static✅ ReadyOct 25, 2024Nonesample.comNotes for Site 3

```
Key Details & Status Summary

🟡 project1 (Currently Building)
Created: Today (Sep 8, 2025)
Status: Currently building (deployment in progress)
Last Commit: "first" (Sep 8, 2025)
Node Version: 22.x
Issue: This is your newest project and the deployment is still in progress

✅ project2 (Production Ready)
Created: Aug 21, 2024
Status: Production ready and live
Custom Domain: example.com (with www redirect)
Last Update: "grammar fix" (May 12, 2025)
Node Version: 20.x
Activity: Most active project with 12 deployments
Note: One failed deployment on Mar 12 but recovered successfully

✅ project3 (Production Ready)
Created: Oct 25, 2024
Status: Production ready
Last Update: "updated public to remove localhost" (Oct 25, 2024)
Node Version: 20.x
Activity: Single successful deployment

Recommendations
- Monitor the building project: Check on project1 as it's currently building
- Portfolio maintenance: Your project2 is well-maintained and actively used
- Domain setup: Consider adding a custom domain to your other projects if needed
- Node versions: You have mixed Node versions (20.x and 22.x) - consider standardizing
- All projects are connected to GitHub repositories and have automatic deployments configured.
```