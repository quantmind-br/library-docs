---
title: Integrations and Settings - Zencoder Docs
url: https://docs.zencoder.ai/zenflow/integrations-and-settings
source: crawler
fetched_at: 2026-01-23T09:28:04.154110504-03:00
rendered_js: false
word_count: 505
summary: This document provides a guide for configuring Zenflow workspace preferences, project-level automation, and specific AI agent settings.
tags:
    - workspace-configuration
    - project-setup
    - ai-agent-settings
    - github-integration
    - mcp-servers
    - workflow-automation
category: configuration
---

## General Settings

The top section covers personal preferences, project automation, and your profile—everything you need before wiring up integrations or agents.

### Preferences

- Set global options like theme, default task view, and notification toggles to keep the workspace consistent across devices.
- Choose which model selector presets appear in chat by default.

![Zenflow Preferences panel showing theme, defaults, and notification toggles](https://mintcdn.com/forgoodaiinc/_mV-YGL7yCjbniwJ/images/zenflow/zenflow-preferences-pane.png?fit=max&auto=format&n=_mV-YGL7yCjbniwJ&q=85&s=cfebe76c40d85c59822e5d8ab313c193)

### Projects

Every project gets its own configuration page (labeled **Project config for …**) with a Save button. Key sections:

- **Project Name** – Display label for the project picker.
- **Git Repository Path** – Absolute path to the repo Zenflow should clone into task worktrees. Use the folder picker to browse.
- **Scripts & Automation** – Configure Setup, Dev Server, and Cleanup scripts so Zenflow can prep, run, and finalize work automatically.
- **Copy Files** – List local-only files (e.g., `.env`, `config.local.json`) to copy into each worktree.
- **AI Rules** – Point to rule folders (e.g., `.ai/rules`, `.cursor/rules`) and always-include rule files so agents stay aligned.

![Zenflow projects configuration screen showing repo paths, scripts, and AI rules](https://mintcdn.com/forgoodaiinc/_mV-YGL7yCjbniwJ/images/zenflow/zenflow-profile-pane.png?fit=max&auto=format&n=_mV-YGL7yCjbniwJ&q=85&s=57f4a517b8939afe76fed4daf17769ae)

### Profile

- Update your name, email, and authentication methods.
- Review workspace membership and access levels.

![Zenflow profile settings page showing personal details and authentication options](https://mintcdn.com/forgoodaiinc/_mV-YGL7yCjbniwJ/images/zenflow/zenflow-profile-details.png?fit=max&auto=format&n=_mV-YGL7yCjbniwJ&q=85&s=4eb1773f893882b61faca086f91d0c39)

### GitHub

Two authentication options keep access flexible:

1. **Connect with OAuth (recommended)** – Launches GitHub’s device authorization flow. Zenflow guides you through linking at `github.com/login/device`, copying the one-time code, and approving the app. Once confirmed, the UI flips to “Connected as username” with a **Disconnect** button.
2. **Personal Access Token** – Paste a PAT if OAuth can’t reach certain private repos. Use tokens with `repo` permissions so Zenflow can read and push branches.

OAuth is easiest to manage—you can revoke it anytime in GitHub or Zenflow. PATs are useful for fine-grained org policies.

### MCP Servers

Each agent gets its own MCP configuration:

- Pick the agent (Claude Code, Codex, Copilot, Gemini, Qwen Code) from the dropdown.
- Edit the JSON config inline. Fresh installs start with:
- Use the **Available servers** gallery to add prebuilt integrations. Hovering Context7, for example, injects the correct HTTP stanza with API key headers.
- Save changes with the top-right **Save** button—Zenflow confirms with a toast.

## Agents

Each agent supports multiple **Configurations** (e.g., APPROVALS, DEFAULT, PLAN). From the configuration dropdown you can switch presets, create new ones, clone existing ones, or delete unused profiles. These presets appear in the Advanced section of the task creation modal.

### Claude Code

- **Append Prompt** – Append repo- or org-level instructions to every prompt.
- **Model** – Override the Claude model ID if you need a specific variant.
- **Dangerously Skip Permissions** – Decide whether Claude can run commands without explicit approval.

### Codex

- **Append Prompt** – Adds persistent instructions to every Codex prompt.
- **Sandbox** – Control escalation policies with modes like `None`, `Always ask`, `Workspace write`, or `Danger full access`.
- **Model** – Free-text override for the Codex model ID.
- **Model reasoning effort** – Tune how much time Codex spends reasoning (`none`, `low`, `medium`, `high`, `null`).

### Gemini

- **Append Prompt** – Add clarifying instructions to every Gemini run.
- **Model** – Choose between `default` and `flash` to balance quality vs. speed.