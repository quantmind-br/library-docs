---
title: ForgeCode
url: https://forgecode.dev/docs/custom-commands/
source: sitemap
fetched_at: 2026-03-29T16:30:34.948142-03:00
rendered_js: false
word_count: 589
summary: This document explains how to define, configure, and manage custom commands in ForgeCode using Markdown files with YAML frontmatter to streamline development workflows.
tags:
    - cli-automation
    - custom-commands
    - workflow-optimization
    - forgecode-configuration
    - markdown-integration
category: guide
---

ForgeCode allows you to define and use custom commands that extend its functionality and streamline your workflow. These commands can be executed within the ForgeCode CLI using the `/command_name` syntax and are defined as individual files in the `~/forge/commands/` directory.

Custom commands are user-defined shortcuts that trigger specific actions or workflows. They enable you to:

- Create project-specific automation
- Standardize common workflows across your team
- Simplify complex operations into single commands
- Integrate ForgeCode with your development processes

Custom commands are defined as individual Markdown files in the `~/forge/commands/` directory. Each command file follows the naming convention `command-name.md`.

### Command File Structure[​](#command-file-structure "Direct link to Command File Structure")

Create a Markdown file in `~/forge/commands/` with frontmatter containing metadata and the body containing the prompt:

**`~/forge/commands/check.md`**

### File Format[​](#file-format "Direct link to File Format")

Command files use Markdown with YAML frontmatter:

- **Frontmatter**: Contains `name` and `description` fields enclosed in `---`
- **Body**: The content after frontmatter becomes the default prompt for the command

### Configuration Options[​](#configuration-options "Direct link to Configuration Options")

OptionRequiredLocationDescription`name`YesFrontmatterThe name of the command (used as `/name` in the CLI)`description`YesFrontmatterA description of what the command does (shown in help)promptNoBodyDefault prompt value used when no arguments are provided

Deprecated: Commands in forge.yaml

Defining commands in the `commands` section of `forge.yaml` is **deprecated** and no longer supported. Please migrate your commands to individual Markdown files in the `~/forge/commands/` directory.

Once configured, you can use custom commands in the ForgeCode CLI in two ways:

### Basic Command Execution[​](#basic-command-execution "Direct link to Basic Command Execution")

To execute a command with its default value (if provided):

This executes the `fmt` command with the default instructions defined in its prompt.

### Command with Arguments[​](#command-with-arguments "Direct link to Command with Arguments")

Commands can accept arguments passed after the command name:

All arguments are combined into a single text value that becomes part of your command's instruction.

Commands can use the `{{parameters}}` variable to incorporate user-provided arguments into their prompts. This makes commands flexible and reusable across different contexts.

### Static Commands[​](#static-commands "Direct link to Static Commands")

Commands without parameters have fixed prompts:

**`~/forge/commands/review.md`**

**Usage:** `/review`

### Dynamic Commands[​](#dynamic-commands "Direct link to Dynamic Commands")

Commands that accept arguments use `{{parameters}}` to insert user input:

**`~/forge/commands/explain.md`**

**Usage:** `/explain React hooks and their lifecycle`

The `{{parameters}}` placeholder will be replaced with `react hooks and their lifecycle`.

### Conditional Parameters[​](#conditional-parameters "Direct link to Conditional Parameters")

Use Handlebars conditionals for commands that work with or without arguments:

**`~/forge/commands/test.md`**

**Usage:**

- `/test` → Generates tests for current context
- `/test UserService` → Generates tests specifically for UserService

tip

Use `{{parameters}}` anywhere in your command prompt where you want to insert user-provided arguments.

### Git Workflow Commands[​](#git-workflow-commands "Direct link to Git Workflow Commands")

**`~/forge/commands/pr.md`**

**Usage:** `/pr Add OAuth2 authentication`

**`~/forge/commands/refactor.md`**

**Usage:** `/refactor authentication module in src/auth`

### Development Workflow Commands[​](#development-workflow-commands "Direct link to Development Workflow Commands")

**`~/forge/commands/document.md`**

### Project-Specific Commands[​](#project-specific-commands "Direct link to Project-Specific Commands")

**`~/forge/commands/fixme.md`**

**`~/forge/commands/deploy.md`**

1. **Descriptive Names**: Use clear, action-oriented names for commands (use lowercase with hyphens for multi-word commands)
2. **Helpful Descriptions**: Write descriptions that explain both the purpose and expected outcome
3. **Use Parameters**: Make commands flexible with `{{parameters}}` for user input
4. **Clear Instructions**: Provide detailed steps in command prompts for consistent results
5. **Specialized Agents**: Configure agents specifically for handling particular commands in `~/forge/agents/`
6. **File Organization**: Keep command files organized in `~/forge/commands/` with descriptive filenames
7. **Documentation**: Document custom commands for your team in a project README

If you have commands defined in your `forge.yaml` file, migrate them to individual Markdown files:

**Old format (deprecated):**

**New format:**

## In `~/forge/commands/fmt.md`

### Migration Steps[​](#migration-steps "Direct link to Migration Steps")

1. Create the `~/forge/commands/` directory if it doesn't exist:
2. For each command in your `forge.yaml`, create a Markdown file:
3. Add the frontmatter with `name` and `description` fields
4. Add the prompt as the body content (without `prompt:` prefix)
5. Remove the `commands` section from your `forge.yaml`
6. Restart ForgeCode to load the new command definitions

<!--THE END-->

- [ForgeCode Configuration](https://forgecode.dev/docs/forge-configuration/) - Global configuration settings
- [Agent Configuration](https://forgecode.dev/docs/agent-configuration/) - Configure agents to respond to custom commands
- [Commands](https://forgecode.dev/docs/commands/) - Learn about ForgeCode's built-in commands