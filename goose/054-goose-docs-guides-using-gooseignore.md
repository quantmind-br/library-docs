---
title: Prevent goose from Accessing Files | goose
url: https://block.github.io/goose/docs/guides/using-gooseignore
source: github_pages
fetched_at: 2026-01-22T22:14:36.95310531-03:00
rendered_js: true
word_count: 334
summary: This document explains how to use .gooseignore files to restrict the goose Developer extension from accessing, modifying, or executing commands on specific files and directories.
tags:
    - gooseignore
    - file-exclusion
    - configuration
    - developer-extension
    - access-control
category: guide
---

`.gooseignore` is a text file that defines patterns for files and directories that goose will not access. This means goose cannot read, modify, delete, or run shell commands on these files when using the Developer extension's tools.

Developer extension only

The .gooseignore feature currently only affects tools in the [Developer](https://block.github.io/goose/docs/mcp/developer-mcp) extension. Other extensions are not restricted by these rules.

This guide will show you how to use `.gooseignore` files to prevent goose from changing specific files and directories.

## Creating your `.gooseignore` file[​](#creating-your-gooseignore-file "Direct link to creating-your-gooseignore-file")

goose supports two types of `.gooseignore` files:

- **Global ignore file** - Create a `.gooseignore` file in `~/.config/goose`. These restrictions will apply to all your sessions with goose, regardless of directory.
- **Local ignore file** - Create a `.gooseignore` file at the root of the directory you'd like it applied to. These restrictions will only apply when working in a specific directory.

tip

You can use both global and local `.gooseignore` files simultaneously. When both exist, goose will combine the restrictions from both files to determine which paths are restricted.

## Example `.gooseignore` file[​](#example-gooseignore-file "Direct link to example-gooseignore-file")

In your `.gooseignore` file, you can write patterns to match files you want goose to ignore. Here are some common patterns:

```
# Ignore specific files by name
settings.json         # Ignore only the file named "settings.json"

# Ignore files by extension
*.pdf                # Ignore all PDF files
*.config             # Ignore all files ending in .config

# Ignore directories and their contents
backup/              # Ignore everything in the "backup" directory
downloads/           # Ignore everything in the "downloads" directory

# Ignore all files with this name in any directory
**/credentials.json  # Ignore all files named "credentials.json" in any directory

# Complex patterns
*.log                # Ignore all .log files
!error.log           # Except for error.log file
```

## Ignore File Types and Priority[​](#ignore-file-types-and-priority "Direct link to Ignore File Types and Priority")

goose respects ignore rules from global `.gooseignore` and local `.gooseignore` files. It uses a priority system to determine which files should be ignored.

### 1. Global `.gooseignore`[​](#1-global-gooseignore "Direct link to 1-global-gooseignore")

- Highest priority and always applied first
- Located at `~/.config/goose/.gooseignore`
- Affects all projects on your machine

```
~/.config/goose/
└── .gooseignore      ← Applied to all projects
```

### 2. Local `.gooseignore`[​](#2-local-gooseignore "Direct link to 2-local-gooseignore")

- Project-specific rules
- Located in your project root directory

```
~/.config/goose/
└── .gooseignore      ← Global rules applied first

Project/
├── .gooseignore      ← Local rules applied second
└── src/
```

### 3. Default Patterns[​](#3-default-patterns "Direct link to 3. Default Patterns")

By default, if you haven't created any .gooseignore files, goose will not modify files matching these patterns:

```
**/.env
**/.env.*
**/secrets.*
```

## Common use cases[​](#common-use-cases "Direct link to Common use cases")

Here are some typical scenarios where `.gooseignore` is helpful:

- **Generated Files**: Prevent goose from modifying auto-generated code or build outputs
- **Third-Party Code**: Keep goose from changing external libraries or dependencies
- **Important Configurations**: Protect critical configuration files from accidental modifications
- **Version Control**: Prevent changes to version control files like `.git` directory
- **Custom Restrictions**: Create `.gooseignore` files to define which files goose should not access