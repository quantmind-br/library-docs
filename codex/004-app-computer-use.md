---
title: Computer Use
url: https://developers.openai.com/codex/app/computer-use.md
source: llms
fetched_at: 2026-04-30T10:15:06.351538375-03:00
rendered_js: false
word_count: 702
summary: This document explains how to set up, authorize, and safely utilize the computer use feature in the Codex app to interact with graphical user interfaces on macOS.
tags:
    - macos-automation
    - desktop-ui
    - computer-use
    - software-setup
    - security-permissions
    - interface-interaction
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Computer Use

> [!info]
> Currently available on macOS only. Excluded in the European Economic Area, United Kingdom, and Switzerland at launch.

Codex can see and operate graphical user interfaces on macOS. Use it when command-line tools or structured integrations aren't enough: checking a desktop app, using a browser, changing app settings, working with a data source unavailable as a plugin, or reproducing a GUI-only bug.

Because computer use can affect app and system state outside your project workspace, use it for scoped tasks and review permission prompts before continuing.

## Setup

In Codex settings, open **Computer Use** and click **Install** to install the plugin. When macOS prompts, grant:
- **Screen Recording** — so Codex can see the target app
- **Accessibility** — so Codex can click, type, and navigate

## When to use

Choose computer use when the task depends on a GUI that's hard to verify through files or command output alone.

| Good fit | Example |
|----------|---------|
| Testing a macOS app, iOS simulator, or desktop app Codex is building | Reproduce onboarding bug, fix smallest code path |
| Task requiring your web browser | Verify checkout page after changes |
| Bug only appears in a GUI | Screenshot and reproduce visually |
| Changing app settings through a UI | Navigate preferences |
| Data source unavailable through a plugin | Inspect information in an app |
| Scoped background task | Run while you keep working elsewhere |
| Workflow spanning multiple apps | Cross-app automation |

For web apps you're building locally, use the [[003-app-browser|in-app browser]] first.

## Start a task

Mention `@Computer Use` or `@AppName` in your prompt, or ask Codex to use computer use. Describe the exact app, window, or flow.

```text
Open the app with computer use, reproduce the onboarding bug, and fix the smallest code path that causes it. After each change, run the same UI flow again.
```
```text
Open @Chrome and verify the checkout page still works after the latest changes.
```

If the target app has a dedicated plugin or MCP server, prefer that for data access and repeatable operations. Choose computer use when visual inspection or operation is needed.

## Permissions and approvals

macOS system permissions (Screen Recording, Accessibility) are separate from Codex app approvals.

- macOS permissions let Codex see and operate apps.
- App approvals determine which apps you allow Codex to use.
- File reads, edits, and shell commands still follow the thread's sandbox and approval settings.

Codex asks for permission before using an app. Choose **Always allow** to skip future prompts for that app. Remove apps from the **Always allow** list in **Computer Use** settings to reset.

If Codex can't see or control an app, check **System Settings > Privacy & Security > Screen Recording / Accessibility** for the Codex app.

## Safety guidance

Codex can view screen content, take screenshots, and interact with windows, menus, keyboard input, and clipboard state in the target app. Treat visible content, screenshots, and files opened in the target app as context Codex may process.

Keep tasks narrow and stay present for sensitive flows:
- Give Codex one clear target app or flow at a time.
- You can stop the task or take over at any time.
- Keep sensitive apps closed unless required.
- Avoid tasks requiring secrets unless you're present and can approve each step.
- Review app permission prompts before allowing.
- Use **Always allow** only for apps you trust Codex to use automatically.
- Stay present for account, security, privacy, network, payment, or credential-related settings.
- Cancel if Codex starts interacting with the wrong window.

If Codex uses your browser, it can interact with pages where you're already signed in. Review website actions as if you were taking them yourself — web pages can contain malicious or misleading content, and sites may treat approved clicks, form submissions, and signed-in actions as coming from your account. To keep using your browser while Codex works, ask Codex to use a different browser.

Limitations:
- Can't automate terminal apps or Codex itself (would bypass security policies).
- Can't authenticate as an administrator or approve system permission prompts.
- File edits and shell commands follow Codex approval and sandbox settings.
- Changes through desktop apps may not appear in the review pane until saved to disk and tracked by the project.
- ChatGPT data controls apply to content processed through Codex, including screenshots.

#macos #computer-use #gui #automation #security