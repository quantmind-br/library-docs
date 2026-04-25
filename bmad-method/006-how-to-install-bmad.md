---
title: How to Install BMad
url: https://docs.bmad-method.org/how-to/install-bmad/
source: sitemap
fetched_at: 2026-04-08T11:31:13.239232477-03:00
rendered_js: false
word_count: 306
summary: This document provides a step-by-step guide on how to install and set up BMad in a project, covering running the initial installer, selecting tools and modules, and verifying a successful setup.
tags:
    - bmad
    - installation-guide
    - project-setup
    - ai-tools
    - module-selection
category: tutorial
---

Use the `npx bmad-method install` command to set up BMad in your project with your choice of modules and AI tools.

If you want to use a non interactive installer and provide all install options on the command line, see [this guide](https://docs.bmad-method.org/how-to/non-interactive-installation/).

- Starting a new project with BMad
- Adding BMad to an existing codebase
- Update the existing BMad Installation

### 1. Run the Installer

[Section titled “1. Run the Installer”](#1-run-the-installer)

### 2. Choose Installation Location

[Section titled “2. Choose Installation Location”](#2-choose-installation-location)

The installer will ask where to install BMad files:

- Current directory (recommended for new projects if you created the directory yourself and ran from within the directory)
- Custom path

### 3. Select Your AI Tools

[Section titled “3. Select Your AI Tools”](#3-select-your-ai-tools)

Pick which AI tools you use:

- Claude Code
- Cursor
- Others

Each tool has its own way of integrating skills. The installer creates tiny prompt files to activate workflows and agents — it just puts them where your tool expects to find them.

### 4. Choose Modules

[Section titled “4. Choose Modules”](#4-choose-modules)

The installer shows available modules. Select whichever ones you need — most users just want **BMad Method** (the software development module).

### 5. Follow the Prompts

[Section titled “5. Follow the Prompts”](#5-follow-the-prompts)

The installer guides you through the rest — settings, tool integrations, etc.

```text

your-project/
├── _bmad/
│   ├── bmm/            # Your selected modules
│   │   └── config.yaml # Module settings (if you ever need to change them)
│   ├── core/           # Required core module
│   └── ...
├── _bmad-output/       # Generated artifacts
├── .claude/            # Claude Code skills (if using Claude Code)
│   └── skills/
│       ├── bmad-help/
│       ├── bmad-persona/
│       └── ...
└── .cursor/            # Cursor skills (if using Cursor)
└── skills/
└── ...
```

## Verify Installation

[Section titled “Verify Installation”](#verify-installation)

Run `bmad-help` to verify everything works and see what to do next.

**BMad-Help is your intelligent guide** that will:

- Confirm your installation is working
- Show what’s available based on your installed modules
- Recommend your first step

You can also ask it questions:

```plaintext

bmad-help I just installed, what should I do first?
bmad-help What are my options for a SaaS project?
```

**Installer throws an error** — Copy-paste the output into your AI assistant and let it figure it out.

**Installer worked but something doesn’t work later** — Your AI needs BMad context to help. See [How to Get Answers About BMad](https://docs.bmad-method.org/how-to/get-answers-about-bmad/) for how to point your AI at the right sources.