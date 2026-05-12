---
title: Session sharing | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/session-sharing
source: sitemap
fetched_at: 2026-04-29T15:03:58.983221893-03:00
rendered_js: false
word_count: 609
summary: This document explains how to share Warp terminal agent sessions to enable real-time collaboration, remote monitoring, and multi-user interaction across devices.
tags:
    - warp-terminal
    - agent-collaboration
    - session-sharing
    - remote-access
    - real-time-collaboration
    - developer-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Agent Session Sharing extends Warp's regular [[146-knowledge-and-collaboration-session-sharing|Session Sharing]] to include full visibility and control over Agent activity. Share any agent session — Oz or third-party — so collaborators can watch progress, review output, and steer the agent from the Warp desktop app, a web browser, or mobile device.

## Key capabilities

| Capability | Description |
|------------|-------------|
| **Full Agent visibility** | Viewers see Agent prompts, responses, thinking states, tool use, planning steps, and [[https://docs.warp.dev/support-and-community/plans-and-billing/credits|credit]] consumption in real time |
| **Cross-device access** | Open shared sessions from Warp desktop app, any web browser, or mobile device. No install required for web viewers |
| **Collaborative editing** | Grant edit access so collaborators can send their own Agent queries, execute commands, and start new conversations |
| **Multi-viewer support** | Multiple participants observe and interact with the same session simultaneously, each with their own cursor and avatar |
| **Remote Control** | Publish third-party agent sessions to the cloud for persistent, asynchronous monitoring and steering. See [[065-agent-platform-third-party-agents-remote-control|Remote Control]] |

## How it works

When you share an agent session, Warp publishes it to the cloud and generates a shareable link. The session stays in sync — any new agent output or terminal activity appears for all viewers in real time. The sharer controls who can view and who can interact.

## Sharing a session

1. Start or open an agent session in Warp (Oz agent, third-party coding agent, or any interactive agent)
2. Open the share action from any entry point:
   - **Command Palette** — Search for "Share session"
   - **Pane header** — Click the overflow menu in the pane header
   - **Right-click context menu** — Right-click inside the session pane
   - **`/remote-control` chip** — For third-party agent sessions, click the chip in the agent view footer or CLI footer
3. Choose starting point (full scrollback, no scrollback, or a specific block)
4. Confirm the share. Warp uploads the session and generates a shareable link
5. Copy the link and share it with teammates, or open it on another device

![Starting a shared agent session from the right-click context menu](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F769506432-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FAULCelT4yIUOcSwWWvPk%252Fuploads%252Fgit-blob-f6498d5fe7a37a067dc00f33f213506183509395%252Fagent-session-sharing-right-click-menu.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a888469b&sv=2)

![Starting a shared agent session from the Command Palette](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F769506432-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FAULCelT4yIUOcSwWWvPk%252Fuploads%252Fgit-blob-8343825979e5d6cd5018ceb9285a92931c1044f5%252Fagent-session-sharing-command-palette.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2014cf2a&sv=2)

## Viewing shared sessions

Shared sessions are accessible from:

| Platform | Description |
|----------|-------------|
| **Warp desktop app** | Paste the link into Warp on a different machine for full desktop experience |
| **Web browser** | Open the shared link in any browser. No app install required |
| **Mobile** | Open the link on a phone or tablet browser to check on progress |

The web experience mirrors the desktop view, showing complete Agent activity including thinking steps, tool use, and terminal output.

## Collaboration and steering

### Watching Agent activity

Viewers see Agent actions unfold live:

- **Thinking animations** — Real-time indicators of Agent reasoning
- **Tool use and planning** — Visible tool calls and planning steps
- **Credit consumption** — Live credit usage for the session
- **Final responses** — Completed Agent output

### Edit access

If a viewer requests edit access, the sharer can approve it. Once approved, collaborators can:

- Send new Agent queries
- Type directly into the prompt
- Execute commands
- Start and switch Agent conversations
- Run terminal commands alongside Agent queries

### Multi-viewer sessions

Multiple participants can join the same session from different machines, browsers, or environments. All participants:

- See each other's avatars and cursors
- Watch Agent activity in sync
- Edit together when granted access
- Run terminal or Agent commands concurrently

## Related pages

- [[146-knowledge-and-collaboration-session-sharing|Session Sharing]] — Warp's regular session sharing feature
- [[065-agent-platform-third-party-agents-remote-control|Remote Control]] — Publishing third-party agent sessions to the cloud