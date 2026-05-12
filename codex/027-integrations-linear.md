---
title: Use Codex in Linear
url: https://developers.openai.com/codex/integrations/linear.md
source: llms
fetched_at: 2026-04-30T10:15:46.843706025-03:00
rendered_js: false
word_count: 595
summary: This document provides instructions for integrating and using Codex within Linear to delegate project management tasks and automate issue resolution. It covers setup procedures, delegation methods, automation through triage rules, and configuration for local development environments.
tags:
    - codex
    - linear
    - integration
    - automation
    - task-delegation
    - triage-rules
    - mcp-server
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Use Codex in Linear

Delegate work from Linear issues. Assign an issue to Codex or mention `@Codex` in a comment, and Codex creates a cloud task and replies with progress and results.

Available on paid plans (see [[075-pricing|Pricing]]). Enterprise plans: ask your ChatGPT workspace admin to turn on Codex cloud tasks in [workspace settings](https://chatgpt.com/admin/settings) and enable **Codex for Linear** in [connector settings](https://chatgpt.com/admin/ca).

## Set up

1. Set up [[016-cloud|Codex cloud tasks]] — connect GitHub in [Codex](https://chatgpt.com/codex) and create a [[052-cloud-environments|cloud environment]] for the target repository.
2. Go to [Codex settings](https://chatgpt.com/codex/settings/connectors) and install **Codex for Linear** for your workspace.
3. Link your Linear account by mentioning `@Codex` in a comment thread on a Linear issue.

## Delegate work

### Assign an issue to Codex

After installing the integration, assign issues to Codex the same way as teammates. Codex starts work and posts updates back to the issue.

### Mention `@Codex` in comments

Mention `@Codex` in comment threads to delegate work or ask questions. After Codex replies, follow up in the thread to continue the same session.

After Codex starts working, it [chooses an environment and repo](#how-codex-chooses-an-environment-and-repo). To pin a specific repo, include it in your comment: `@Codex fix this in openai/codex`.

Track progress:
- Open **Activity** on the issue for progress updates.
- Open the task link for detailed follow-along.

When finished, Codex posts a summary and a link to the completed task so you can create a pull request.

### How Codex chooses an environment and repo

- Linear suggests a repository based on issue context. Codex selects the best-matching environment. If ambiguous, falls back to the most recently used environment.
- Task runs against the default branch of the first repository listed in that environment's repo map. Update the repo map in Codex if you need a different default or more repositories.
- If no suitable environment or repository is available, Codex replies in Linear with instructions on how to fix before retrying.

## Automatically assign issues to Codex

Use Linear triage rules:
1. In Linear, go to **Settings**.
2. Under **Your teams**, select your team.
3. In workflow settings, open **Triage** and turn it on.
4. In **Triage rules**, create a rule and choose **Delegate** > **Codex** (and any other properties).

Linear assigns new issues entering triage to Codex automatically. When using triage rules, Codex runs tasks using the account of the issue creator.

## Data usage, privacy, and security

When you mention `@Codex` or assign an issue, Codex receives issue content to understand your request and create a task. Data handling follows OpenAI's [Privacy Policy](https://openai.com/privacy), [Terms of Use](https://openai.com/terms/), and applicable [policies](https://openai.com/policies).

For security, see [[041-agent-approvals-security|Codex security documentation]].

> [!warning]
> Codex uses large language models that can make mistakes. Always review answers and diffs.

## Tips and troubleshooting

| Issue | Fix |
|-------|-----|
| Missing connections | Codex replies with a link to connect your account |
| Unexpected environment choice | Reply with the environment you want (e.g., `@Codex please run this in openai/codex`) |
| Wrong part of the code | Add more context in the issue, or give explicit instructions in your `@Codex` comment |
| More help | [OpenAI Help Center](https://help.openai.com/) |

## Connect Linear for local tasks (MCP)

For Codex app, CLI, or IDE Extension, configure the Linear MCP server:

```bash
codex mcp add linear --url https://mcp.linear.app/mcp
```

This prompts you to sign in with Linear and connect it to Codex.

Or manually add to `~/.codex/config.toml`:
```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"
```

Then run `codex mcp login linear`.

Setup steps are the same for IDE extension and CLI since both share the same configuration.

#linear #integration #automation #codex #mcp