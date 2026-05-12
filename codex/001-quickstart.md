---
number: 1
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/quickstart.md
word_count: 340
---
# Quickstart

> **BLUF:** Get started with Codex via app (recommended), IDE extension, CLI, or cloud. App/IDE use ChatGPT auth; CLI supports both ChatGPT and API key. All plans include Codex.

## Setup Options

| Method | Platform | Auth | Recommended For |
|--------|----------|------|-----------------|
| **App** | macOS, Windows | ChatGPT or API key | Most users |
| **IDE Extension** | VS Code, Cursor, Windsurf | ChatGPT or API key | In-editor coding |
| **CLI** | macOS, Windows, Linux | ChatGPT or API key | Terminal workflows |
| **Cloud** | Browser | ChatGPT | GitHub PR delegation |

## App Setup (Recommended)

1. **Download** from [openai.com/codex/app](https://openai.com/codex/app) (macOS/Windows)
2. **Sign in** with ChatGPT account or OpenAI API key
3. **Select a project** folder for Codex to work in
4. **Send your first message** — select **Local** mode for on-machine execution

> ⚠️ API key sign-in may limit cloud threads and some features.

## IDE Extension Setup

1. Install from your editor's marketplace:
   - [VS Code](vscode:extension/openai.chatgpt)
   - [Cursor](cursor:extension/openai.chatgpt)
   - [Windsurf](windsurf:extension/openai.chatgpt)
   - [VS Code Insiders](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
2. Open the Codex panel in the sidebar
3. Sign in and start your first task — defaults to Agent mode (reads files, runs commands, writes changes)
4. Use Git checkpoints before and after tasks to easily revert changes

## CLI Setup

### Install

```bash
npm install -g @openai/codex
# or
brew install codex
```

### Authenticate

```bash
codex login  # Opens browser for ChatGPT OAuth (default)
echo $OPENAI_API_KEY | codex login --with-api-key  # CI/CD, SSH, containers
```

### Use

```bash
codex  # Interactive TUI in current directory
codex -m gpt-5.5  # Use specific model
```

For full CLI reference, see [[015-cli|Codex CLI]].

## Cloud Setup

1. Go to [chatgpt.com/codex](https://chatgpt.com/codex)
2. Configure environment: [Settings → Environments](https://chatgpt.com/codex/settings/environments) → connect a GitHub repository
3. Launch tasks from the Codex interface — monitor progress or run in background
4. Review diffs and create PRs directly in GitHub

### GitHub PR Delegation

Tag `@codex` in a PR comment to delegate a task to Codex (requires ChatGPT sign-in).

## Next Steps

- [[005-app-features|Codex App Features]] — worktrees, automations, Git tools, terminal
- [[021-ide-features|IDE Extension Features]] — context, slash commands, inline chat
- [[015-cli|Codex CLI]] — full CLI reference
- [[016-cloud|Codex Cloud]] — cloud environments and execution
- [[047-best-practices|Best Practices]] — effective Codex usage

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/quickstart.md)*