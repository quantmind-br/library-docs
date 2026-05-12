---
title: Viewing cloud agent runs | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/viewing-cloud-agent-runs
source: sitemap
fetched_at: 2026-04-29T15:04:40.094144929-03:00
rendered_js: false
word_count: 423
summary: This document explains how to use cloud agent session sharing to inspect, collaborate on, and continue tasks performed by remote virtual machine agents.
tags:
    - cloud-agents
    - session-sharing
    - remote-debugging
    - collaboration
    - developer-tools
    - warp-agent
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Cloud agent session sharing lets you open, inspect, and continue interacting with agent tasks running on remote virtual machines. View full sessions, follow along in real time, ask follow-up questions, and fork work into your local Warp environment.

**What you can do:**

- See every command the agent executed
- Inspect context, logs, and outputs directly in Warp or the web viewer
- Ask follow-up questions after the task completes
- Bring the conversation into your local session with **Fork to local**
- Share links so teammates can view or collaborate on the session

Works whether or not Warp is installed on the viewer's machine.

## How it works

### 1. Open a remote cloud agent run

When a cloud agent starts (Slack mention, Linear issue, or CLI trigger), Warp attaches a shareable link:

- From [Slack](https://docs.warp.dev/agent-platform/cloud-agents/integrations/slack) — click **View Agent** in the agent response
- From [Linear](https://docs.warp.dev/agent-platform/cloud-agents/integrations/linear) — click the ↗ **Warp** button on the ticket

You can also open the session directly in your browser to see the complete agent session on a cloud VM.

### 2. Inspect the session

Once loaded, scroll through the agent's actions, see the prompt and plan, review code/config changes, and understand the execution environment. The UI behaves like a local Warp session.

### 3. Keep chatting with the remote agent

Even after the task completes, ask follow-up questions. Warp sends your message back to the remote VM and continues the conversation. Works as long as the remote environment is still active.

Examples:
- "Can you explain which flag you changed?"
- "Give me a summary of what you modified."
- "Show me the reasoning behind your last step."

### 4. Handle inactive or shut-down sessions

Cloud agent environments automatically shut down after a period of inactivity. Click **Fork to local** to continue the conversation or work on the code.

### 5. Fork the session to your local Warp

Forking brings the cloud agent conversation into your local machine:

- Session appears as a normal conversation in local Warp
- Continue prompting using all local tools
- Agent responds using your local environment instead of the remote VM

> [!note]
> If the cloud agent created a new git branch or repository in the remote VM, clone that branch locally first so the agent can continue working on the same code.

## Viewing sessions across devices

Sessions can be viewed from:

- The Warp desktop app
- A browser via the web viewer
- Remote teammates using the shared link
- Local Warp sessions after forking
