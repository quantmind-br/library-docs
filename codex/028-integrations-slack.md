---
title: Use Codex in Slack
url: https://developers.openai.com/codex/integrations/slack.md
source: llms
fetched_at: 2026-04-30T10:15:47.694940534-03:00
rendered_js: false
word_count: 446
summary: This document provides instructions for integrating and using the Codex Slack application to initiate coding tasks directly from Slack channels and threads.
tags:
    - codex
    - slack-integration
    - cloud-tasks
    - developer-tools
    - collaboration
    - workflow-automation
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Use Codex in Slack

Kick off coding tasks from Slack channels and threads. Mention `@Codex` with a prompt, and Codex creates a cloud task and replies with results.

## Set up

1. Set up [[016-cloud|Codex cloud tasks]] — need Plus, Pro, Business, Enterprise, or Edu plan, connected GitHub account, and at least one [[052-cloud-environments|environment]].
2. Go to [Codex settings](https://chatgpt.com/codex/settings/connectors) and install the Slack app for your workspace. Depending on Slack workspace policies, an admin may need to approve.
3. Add `@Codex` to a channel. Slack prompts you when you mention it if not added yet.

## Start a task

1. In a channel or thread, mention `@Codex` and include your prompt. Codex can reference earlier messages in the thread, so you often don't need to restate context.
2. (Optional) Specify environment or repository: `@Codex fix the above in openai/codex`.
3. Wait for Codex to react (👀) and reply with a task link. When finished, Codex posts the result and, depending on settings, an answer in the thread.

### How Codex chooses an environment and repo

- Reviews accessible environments and selects the best match. If ambiguous, falls back to most recently used.
- Task runs against default branch of first repository in the environment's repo map. Update repo map in Codex if you need a different default or more repositories.
- If no suitable environment or repository available, Codex replies in Slack with instructions on how to fix before retrying.

### Enterprise data controls

By default, Codex replies in thread with an answer, which may include information from the environment it ran in.

To prevent this, an Enterprise admin can clear **Allow Codex Slack app to post answers on task completion** in [ChatGPT workspace settings](https://chatgpt.com/admin/settings). When turned off, Codex replies only with a link to the task.

### Data usage, privacy, and security

When you mention `@Codex`, Codex receives your message and thread history to understand the request and create a task. Data handling follows OpenAI's [Privacy Policy](https://openai.com/privacy), [Terms of Use](https://openai.com/terms/), and applicable [policies](https://openai.com/policies).

For security, see [[041-agent-approvals-security|Codex security documentation]].

> [!warning]
> Codex uses large language models that can make mistakes. Always review answers and diffs.

### Tips and troubleshooting

| Issue | Fix |
|-------|-----|
| Missing connections | Codex replies with a link to reconnect Slack or GitHub |
| Unexpected environment choice | Reply in thread with desired environment, then mention `@Codex` again |
| Long or complex threads | Summarize key details in your latest message so Codex doesn't miss buried context |
| Workspace posting restrictions | Open the task link to view progress and results |
| More help | [OpenAI Help Center](https://help.openai.com/) |

#slack #integration #collaboration #codex