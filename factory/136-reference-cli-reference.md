---
title: CLI Reference - Factory Documentation
url: https://docs.factory.ai/reference/cli-reference
source: sitemap
fetched_at: 2026-01-13T19:03:35.249967605-03:00
rendered_js: false
word_count: 793
summary: A comprehensive reference guide for the Droid CLI, covering installation, command syntax, operational modes (interactive and non-interactive), configuration flags, autonomy levels, and authentication.
tags:
    - cli-reference
    - command-line-interface
    - automation
    - authentication
    - configuration
category: reference
---

## Installation

The CLI operates in two modes:

- **Interactive (`droid`)** - Chat-first REPL with slash commands
- **Non-interactive (`droid exec`)** - Single-shot execution for automation and scripting

## CLI commands

CommandDescriptionExample`droid`Start interactive REPL`droid``droid "query"`Start REPL with initial prompt`droid "explain this project"``droid exec "query"`Execute task without interactive mode`droid exec "summarize src/auth"``droid exec -f prompt.md`Load prompt from file`droid exec -f .factory/prompts/review.md``cat file | droid exec`Process piped content`git diff | droid exec "draft release notes"``droid exec -s <id> "query"`Resume existing session in exec mode`droid exec -s session-123 "continue"``droid exec --list-tools`List available tools, then exit`droid exec --list-tools`

## CLI flags

Customize droid’s behavior with command-line flags:

FlagDescriptionExample`-f, --file <path>`Read prompt from a file`droid exec -f plan.md``-m, --model <id>`Select a specific model (see [model IDs](#available-models))`droid exec -m claude-opus-4-5-20251101``-s, --session-id <id>`Continue an existing session`droid exec -s session-abc123``--auto <level>`Set [autonomy level](#autonomy-levels) (`low`, `medium`, `high`)`droid exec --auto medium "run tests"``--enabled-tools <ids>`Force-enable specific tools (comma or space separated)`droid exec --enabled-tools ApplyPatch,Bash``--disabled-tools <ids>`Disable specific tools for this run`droid exec --disabled-tools execute-cli``--list-tools`Print available tools and exit`droid exec --list-tools``-o, --output-format <format>`Output format (`text`, `json`, `stream-json`, `stream-jsonrpc`)`droid exec -o json "document API"``--input-format <format>`Input format (`stream-json`, `stream-jsonrpc` for multi-turn)`droid exec --input-format stream-jsonrpc -o stream-jsonrpc``-r, --reasoning-effort <level>`Override reasoning effort (`off`, `none`, `low`, `medium`, `high`)`droid exec -r high "debug flaky test"``--spec-model <id>`Use a different model for specification planning`droid exec --spec-model claude-sonnet-4-5-20250929``--spec-reasoning-effort <level>`Override reasoning effort for spec mode`droid exec --use-spec --spec-reasoning-effort high``--use-spec`Start in specification mode (plan before executing)`droid exec --use-spec "add user profiles"``--skip-permissions-unsafe`Skip all permission prompts (⚠️ use with extreme caution)`droid exec --skip-permissions-unsafe``--cwd <path>`Execute from a specific working directory`droid exec --cwd ../service "run tests"``--delegation-url <url>`URL for delegated sessions (Slack thread or Linear issue)`droid exec --delegation-url <slack-or-linear-url>``-v, --version`Display CLI version`droid -v``-h, --help`Show help information`droid --help`

## Autonomy levels

`droid exec` uses tiered autonomy to control what operations the agent can perform. Only raise access when the environment is safe.

LevelIntended forNotable allowances*(default)*Read-only reconnaissanceFile reads, git diffs, environment inspection`--auto low`Safe editsCreate/edit files, run formatters, non-destructive commands`--auto medium`Local developmentInstall dependencies, build/test, local git commits`--auto high`CI/CD & orchestrationGit push, deploy scripts, long-running operations`--skip-permissions-unsafe`Isolated sandboxes onlyRemoves all guardrails (⚠️ use only in disposable containers)

**Examples:**

```
# Default (read-only)
droid exec "Analyze the auth system and create a plan"

# Low autonomy - safe edits
droid exec --auto low "Add JSDoc comments to all functions"

# Medium autonomy - development work
droid exec --auto medium "Install deps, run tests, fix issues"

# High autonomy - deployment
droid exec --auto high "Run tests, commit, and push changes"
```

## Available models

Model IDNameReasoning supportDefault reasoning`claude-opus-4-5-20251101`Claude Opus 4.5 (default)Yes (Off/Low/Medium/High)off`gpt-5.1-codex-max`GPT-5.1-Codex-MaxYes (Low/Medium/High/Extra High)medium`gpt-5.1-codex`GPT-5.1-CodexYes (Low/Medium/High)medium`gpt-5.1`GPT-5.1Yes (None/Low/Medium/High)none`gpt-5.2`GPT-5.2Yes (Low/Medium/High)low`claude-sonnet-4-5-20250929`Claude Sonnet 4.5Yes (Off/Low/Medium/High)off`claude-haiku-4-5-20251001`Claude Haiku 4.5Yes (Off/Low/Medium/High)off`gemini-3-pro-preview`Gemini 3 ProYes (Low/High)high`gemini-3-flash-preview`Gemini 3 FlashYes (Minimal/Low/Medium/High)high`glm-4.6`Droid Core (GLM-4.6)None onlynone

Custom models configured via [BYOK](https://docs.factory.ai/cli/configuration/byok) use the format: `custom:<alias>` See [Choosing Your Model](https://docs.factory.ai/cli/user-guides/choosing-your-model) for detailed guidance on which model to use for different tasks.

## Interactive mode features

### Bash mode

Press `!` when the input is empty to toggle bash mode. In bash mode, commands execute directly in your shell without AI interpretation—useful for quick operations like checking `git status` or running `npm test`.

- **Toggle on:** Press `!` (when input is empty)
- **Execute commands:** Type any shell command and press Enter
- **Toggle off:** Press `Esc` to return to normal AI chat mode

The prompt changes from `>` to `$` when bash mode is active.

### Slash commands

Available when running `droid` in interactive mode. Type the command at the prompt:

CommandDescription`/account`Open Factory account settings in browser`/billing`View and manage billing settings`/bug [title]`Create a bug report with session data and logs`/clear`Start a new session (alias for `/new`)`/commands`Manage custom slash commands`/compress [prompt]`Compress session and move to new one with summary`/cost`Show token usage statistics`/droids`Manage custom droids`/favorite`Mark current session as a favorite`/help`Show available slash commands`/hooks`Manage lifecycle hooks`/ide`Configure IDE integrations`/login`Sign in to Factory`/logout`Sign out of Factory`/mcp`Manage Model Context Protocol servers`/model`Switch AI model mid-session`/new`Start a new session`/quit`Exit droid (alias: `exit`, or press Ctrl+C)`/readiness-report`Generate readiness report`/review`Start AI-powered code review workflow`/rewind-conversation`Undo recent changes in the session`/sessions`List and select previous sessions`/settings`Configure application settings`/skills`Manage and invoke skills`/status`Show current droid status and configuration`/terminal-setup`Configure terminal keybindings for Shift+Enter

For detailed information on slash commands, see the [interactive mode documentation](https://docs.factory.ai/cli/getting-started/quickstart#useful-slash-commands).

### MCP command reference

The `/mcp` slash command opens an interactive manager UI for browsing and managing MCP servers. **Quick start:** Type `/mcp` and select **“Add from Registry”** to browse 40+ pre-configured servers (Linear, Sentry, Notion, Stripe, Vercel, and more). Select a server, authenticate if required, and you’re ready to go. **CLI commands** for scripting and automation:

```
droid mcp add <name> <url> --type http    # Add HTTP server
droid mcp add <name> "<command>"          # Add stdio server
droid mcp remove <name>                   # Remove a server
```

See [MCP Configuration](https://docs.factory.ai/cli/configuration/mcp) for the full registry list, CLI options (`--env`, `--header`), configuration files, and how user vs project config layering works.

## Authentication

1. Generate an API key at [app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys)
2. Set the environment variable:

**Persist the variable** in your shell profile (`~/.bashrc`, `~/.zshrc`, or PowerShell `$PROFILE`) for long-term use.

## Exit codes

CodeMeaning`0`Success`1`General runtime error`2`Invalid CLI arguments/options

## Common workflows

### Code review

```
# Interactive review workflow
> /review

# Analysis via exec (non-interactive)
droid exec "Review this PR for security issues"

# With modifications
droid exec --auto low "Review code and add missing type hints"
```

See the [Code Review documentation](https://docs.factory.ai/cli/features/code-review) for detailed guidance on review types, workflows, and best practices.

### Testing and debugging

```
# Investigation
droid exec "Analyze failing tests and explain root cause"

# Fix and verify
droid exec --auto medium "Fix failing tests and run test suite"
```

### Refactoring

```
# Planning
droid exec "Create refactoring plan for auth module"

# Execution
droid exec --auto low --use-spec "Refactor auth module"
```

### CI/CD integration

```
# GitHub Actions example
- name: Run Droid Analysis
  env:
    FACTORY_API_KEY: ${{ secrets.FACTORY_API_KEY }}
  run: |
    droid exec --auto medium -f .github/prompts/deploy.md
```

## See also

- [Quickstart guide](https://docs.factory.ai/cli/getting-started/quickstart) - Getting started with Factory CLI
- [Interactive mode](https://docs.factory.ai/cli/getting-started/quickstart) - Shortcuts, input modes, and features
- [Choosing your model](https://docs.factory.ai/cli/user-guides/choosing-your-model) - Model selection guidance
- [Settings](https://docs.factory.ai/cli/configuration/settings) - Configuration options
- [Custom commands](https://docs.factory.ai/cli/configuration/custom-slash-commands) - Create your own shortcuts
- [Custom droids](https://docs.factory.ai/cli/configuration/custom-droids) - Build specialized agents
- [Droid Exec overview](https://docs.factory.ai/cli/droid-exec/overview) - Detailed automation guide
- [MCP configuration](https://docs.factory.ai/cli/configuration/mcp) - External tool integration