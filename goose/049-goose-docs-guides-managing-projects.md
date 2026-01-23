---
title: Managing Projects | goose
url: https://block.github.io/goose/docs/guides/managing-projects
source: github_pages
fetched_at: 2026-01-22T22:14:00.594683181-03:00
rendered_js: true
word_count: 294
summary: This document explains how goose Projects track working directories and sessions to facilitate seamless context preservation and workflow resumption across multiple codebases.
tags:
    - goose-cli
    - project-management
    - context-preservation
    - session-tracking
    - developer-workflow
category: guide
---

goose Projects automatically track your working directories and associated sessions, making it easy to resume work across multiple codebases with full context preservation.

A **project** in goose is a record of a working directory where you've used goose. Every time you run goose, it automatically tracks the current directory as a project, storing:

- **Path**: The absolute path to the project directory
- **Last accessed**: When you last worked on this project
- **Last instruction**: The most recent command you gave to goose
- **Session ID**: The associated session for context continuity

Projects are stored in `~/.local/share/goose/projects.json`.

CLI Only Feature

Projects are currently available only through the goose CLI. Desktop support is planned for future releases.

## Basic Usage[​](#basic-usage "Direct link to Basic Usage")

**Resume your most recent project:**

**Browse all your projects:**

tip

When resuming a project, you can continue the previous session or start fresh in that directory.

For complete command syntax and options, see the [CLI Commands Guide](https://block.github.io/goose/docs/guides/goose-cli-commands#project).

## Workflow Example[​](#workflow-example "Direct link to Workflow Example")

Let's follow Sarah, a developer working on multiple projects throughout her day:

### Morning: API Development[​](#morning-api-development "Direct link to Morning: API Development")

```
cd ~/projects/ecommerce-api
goose session --name "api-auth-work"
```

*Sarah asks goose to help implement JWT token refresh logic*

### Mid-Morning: Mobile App Bug Fix[​](#mid-morning-mobile-app-bug-fix "Direct link to Mid-Morning: Mobile App Bug Fix")

```
cd ~/projects/mobile-app
goose session
```

*Sarah gets help debugging an iOS crash in the login screen*

### Afternoon: Admin Dashboard[​](#afternoon-admin-dashboard "Direct link to Afternoon: Admin Dashboard")

```
cd ~/projects/admin-dashboard  
goose session --name "dashboard-ui"
```

*Sarah works on creating user management interface components*

### Next Day: Quick Resume[​](#next-day-quick-resume "Direct link to Next Day: Quick Resume")

```
# From any directory, quickly resume the most recent project
goose project
```

goose shows:

```
┌ goose Project Manager
│
◆ Choose an option:
│  ○ Resume project with session: .../admin-dashboard
│    Continue with the previous session
│  ○ Resume project with fresh session: .../admin-dashboard  
│    Change to the project directory but start a new session
│  ○ Start new project in current directory: /Users/sarah
│    Stay in the current directory and start a new session
└
```

### Later: Browse All Projects[​](#later-browse-all-projects "Direct link to Later: Browse All Projects")

goose displays:

```
┌ goose Project Manager
│
◆ Select a project:
│  ○ 1  .../admin-dashboard (2025-01-07 09:15:30) [create user management interface]
│  ○ 2  .../mobile-app (2025-01-06 11:45:20) [login screen crashing on iOS]  
│  ○ 3  .../ecommerce-api (2025-01-06 09:30:15) [JWT token refresh logic]
│  ○ Cancel
└
```

Sarah can see her recent projects with timestamps and context, making it easy to choose where to continue working.

## Benefits[​](#benefits "Direct link to Benefits")

Time Savings

Projects eliminate the typical 2-5 minutes lost when switching between codebases, especially valuable for developers working on multiple projects daily.

- **Eliminate context switching friction** - Jump between projects instantly without manual navigation
- **Preserve work context** - Resume exactly where you left off with full conversation history
- **Seamless session integration** - Maintain continuity across different codebases