---
title: CIS Configuration
url: https://cis-docs.bmad-method.org/reference/configuration/
source: sitemap
fetched_at: 2026-04-08T11:33:59.251601578-03:00
rendered_js: false
word_count: 341
summary: This document provides a comprehensive guide on configuring the Creative Intelligence Suite (CIS), detailing how to set up configuration files, understand various options like output folders and agent names, and manage environment variable overrides.
tags:
    - configuration
    - cis-setup
    - workflow-management
    - agent-preferences
    - environment-variables
    - output-settings
category: guide
---

Configure Creative Intelligence Suite workflows, output behavior, and agent preferences.

## Configuration File

[Section titled “Configuration File”](#configuration-file)

CIS configuration is stored in:

If the file doesn’t exist, CIS uses default values.

## Configuration Options

[Section titled “Configuration Options”](#configuration-options)

SettingDescriptionDefault**output\_folder**Where workflow outputs are saved`./_bmad-output/`**user\_name**Name used in workflow facilitation`User`**communication\_language**Language for agent responses`english`

**Where workflow results are saved.**

Absolute or relative path. Workflow outputs are named `{workflow-name}-{date}.md`.

**Example:**

```yaml

output_folder: "./creative-outputs"
# or
output_folder: "/Users/name/Documents/creative-work"
```

**Relative paths** are resolved from project root.

**How agents address you during facilitation.**

Used for personalized interaction. Agents weave your name into their responses.

**Example:**

```yaml

user_name: "Alex"
# Carson might say: "Alex, let's try a different angle..."
```

### communication\_language

[Section titled “communication\_language”](#communication_language)

**Language for workflow facilitation.**

Agents communicate in the specified language while maintaining their distinctive personalities.

**Supported values:**

- `english` (default)
- `spanish`
- `french`
- `german`
- `italian`
- `portuguese`

**Example:**

```yaml

communication_language: "spanish"
# Maya facilitará en español manteniendo su estilo jazzístico
```

## Default Configuration

[Section titled “Default Configuration”](#default-configuration)

If no config file exists, CIS uses:

```yaml

output_folder: "./_bmad-output/"
user_name: "User"
communication_language: "english"
```

## Creating Configuration

[Section titled “Creating Configuration”](#creating-configuration)

Create or edit `_bmad/cis/config.yaml`:

```yaml

# CIS Configuration
output_folder: "./_bmad-output/"
user_name: "Your Name"
communication_language: "english"
```

## Workflow-Specific Context

[Section titled “Workflow-Specific Context”](#workflow-specific-context)

Some workflows accept additional context via command-line flags:

### Providing Context Data

[Section titled “Providing Context Data”](#providing-context-data)

Pass context documents to workflows:

```bash

workflowdesign-thinking--data/path/to/user-research.md
workflowinnovation-strategy--data/path/to/market-analysis.md
workflowproblem-solving--data/path/to/problem-brief.md
workflowstorytelling--data/path/to/brand-guidelines.md
```

Context files should be markdown. Agents incorporate this information into facilitation.

## Agent Sidecar Configuration

[Section titled “Agent Sidecar Configuration”](#agent-sidecar-configuration)

Some agents maintain persistent data in sidecar directories:

Sophia (Storyteller) remembers your preferences and story history:

```plaintext

_bmad/_memory/storyteller-sidecar/
├── story-preferences.md    # Your storytelling preferences
└── stories-told.md          # History of stories created
```

**Critical actions** (automatically called):

1. Load preferences before storytelling
2. Update history after story creation

This enables Sophia to learn your style and build consistent narratives over time.

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

CIS respects these environment variables:

VariablePurposeExample`BMAD_OUTPUT_DIR`Override output folder`BMAD_OUTPUT_DIR=./outputs``BMAD_USER_NAME`Override user name`BMAD_USER_NAME=Jordan``BMAD_LANGUAGE`Override language`BMAD_LANGUAGE=spanish`

Environment variables take precedence over config file settings.

## Troubleshooting Configuration

[Section titled “Troubleshooting Configuration”](#troubleshooting-configuration)

### Outputs Not Appearing

[Section titled “Outputs Not Appearing”](#outputs-not-appearing)

Check output folder path is valid:

```bash

# Test path resolution
ls./_bmad-output/
```

Ensure the folder exists or CIS can create it.

### Agent Not Using Your Name

[Section titled “Agent Not Using Your Name”](#agent-not-using-your-name)

Verify `user_name` in config file. For Sophia, ensure sidecar files exist and are readable.

### Language Not Changing

[Section titled “Language Not Changing”](#language-not-changing)

Confirm `communication_language` uses supported values. Custom languages require agent prompt updates.

- [**Getting Started**](https://cis-docs.bmad-method.org/tutorials/getting-started/) — Use workflows with default configuration
- [**Workflows Reference**](https://cis-docs.bmad-method.org/reference/workflows/) — Detailed workflow mechanics