---
title: Computer use | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/computer-use
source: sitemap
fetched_at: 2026-04-29T15:03:53.302504509-03:00
rendered_js: false
word_count: 755
summary: This document explains the Computer Use experimental feature, which allows Warp agents to interact with desktop environments to perform UI testing and web automation within secure, sandboxed cloud environments.
tags:
    - warp-agents
    - computer-use
    - ui-testing
    - browser-automation
    - sandboxed-environments
    - experimental-feature
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Computer Use is an experimental feature enabling Warp agents to interact with desktop environments—screenshot capture, click/drag, text input, keyboard shortcuts, and GUI interactions—within a secure, isolated sandbox.

Primary use case: **UI change testing** with a self-contained feedback loop where the agent verifies code changes produce expected visual and behavioral results without manual testing.

## Overview

Agents can:
- **Take screenshots** — capture and analyze the current display
- **Interact with applications** — click buttons, fill forms, navigate interfaces
- **Type and control keyboard** — enter text and use keyboard shortcuts
- **Automate testing workflows** — test UI changes end-to-end without manual intervention
- **Work with browser-based interfaces** — test web apps and navigate the web

> [!warning]
> Computer Use is only available in Warp's sandboxed cloud environments, not in local interactive terminal sessions.

---

## Enabling Computer Use

Computer Use is **opt-in** and disabled by default.

### Warp app settings

Navigate to **Settings** > **Agents** > **Warp Agent** > **Experimental** > **Computer use in Cloud Agents** and toggle to enable.

### CLI

Use flags to control Computer Use per run when running agents in the cloud via the [CLI](https://docs.warp.dev/reference/cli).

### API

Include the `computer_use_enabled` field in your request when calling the Warp API to create agent runs. See the [Oz API & SDK](https://docs.warp.dev/reference/api-and-sdk/) reference for full documentation.

### Web App

In the Warp web app, enable or disable Computer Use for:
- **New agent runs** — configure when starting a new agent run
- **Scheduled agent runs** — enable for scheduled agents managed from the web app
- **Integrations** — configure for Slack, Linear, and other integration-triggered agents

---

## How Computer Use works

### Setup and requirements

Computer Use runs in a containerized sandbox, allowing headless cloud environments to render and interact with graphical applications. The sandbox is fully isolated—it does not have access to your local machine, credentials, or sensitive data outside the sandbox environment.

Your cloud environment must include any applications you want the agent to control (e.g., Chrome or Firefox for web app testing). See [environment configuration](https://docs.warp.dev/agent-platform/cloud-agents/environments).

### Model selection

Computer Use supports multiple Anthropic Claude models: Claude 4.5 Sonnet, Claude 4.5 Opus, Claude 4.5 Haiku, Claude 4.6 Sonnet, and Claude 4.6 Opus. Warp uses an auto model selector to choose the best-suited model for each task.

---

## Security considerations

> [!danger]
> Computer Use is experimental with heightened security risks, especially when interacting with the internet.

Minimize risks by:
1. **Avoid sensitive data** — do not pass API keys, authentication tokens, or personal information to agents using Computer Use
2. **Limit internet access** — if your environment has internet access, restrict to an allowlist of known-safe domains
3. **Require human confirmation** — for tasks with real-world consequences (e.g., financial transactions, accepting legal terms)
4. **Review agent actions** — regularly review what agents are doing on your behalf

---

## Example workflows

### Testing UI changes

- **Build from mockups** — receive a Figma design, build the UI, and test it matches
- **Visual regression testing** — after code changes, verify UI renders correctly
- **Form and interaction testing** — test form submissions, validation, error handling
- **Responsive design validation** — test layout on different screen sizes

**Example: Testing a React component**

1. Ask the agent: "Build a React button component that matches this design, then test it"
2. Agent takes a screenshot to see the current state
3. Agent opens your dev server in a browser
4. Agent navigates to the component, verifies it renders correctly
5. Agent tests interactions (hover, click) and reports back

**Example: Testing a web form**

1. Provide a form design and ask the agent to build and test it
2. Agent renders your form in the browser
3. Agent fills fields with valid and invalid data
4. Agent verifies validation messages and submission behavior
5. Agent reports which fields worked correctly and which need adjustment

**Example: Verifying UI responsiveness**

1. Ask the agent to test your app on different screen sizes
2. Agent resizes the browser window to mobile, tablet, and desktop widths
3. Agent takes screenshots at each size and verifies layout
4. Agent reports any responsive design issues

### Browsing and web interaction

Computer Use can also help with:
- Browsing websites and interacting with web interfaces
- Filling out and submitting web forms
- Navigating multi-step workflows in web applications

---

- [[196-agent-platform-warp-agents-capabilities-overview-skills|Skills]] — reusable, scoped instructions for specific tasks
- [[197-agent-platform-warp-agents-capabilities-overview-task-lists|Task Lists]] — track complex workflows with real-time progress updates
- [[198-agent-platform-warp-agents-capabilities-overview|Capabilities]] — all agent capabilities and configuration options
