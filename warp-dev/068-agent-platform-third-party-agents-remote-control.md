---
title: Remote Control | Agents | Warp
url: https://docs.warp.dev/agent-platform/third-party-agents/remote-control
source: sitemap
fetched_at: 2026-04-29T15:04:17.338908423-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T18:15:00.000Z
tags:
    - remote-control
    - agent-platform
    - session-sharing
    - cloud-monitoring
    - terminal-automation
    - collaboration
category: guide
word_count: 376
---
Remote Control publishes a running third-party agent session (Claude Code, Codex, OpenCode) to the cloud with one click. Once published, monitor progress, review output, and steer the agent from any device.

> [!info]
> Built on top of [[042-agent-platform-warp-agents-capabilities-overview-session-sharing|Agent Session Sharing]] — uses the same infrastructure to publish sessions and generate shareable links.

## Key capabilities

- **One-click publish** — click `/remote-control` in the agent utility bar; shareable link copied to clipboard
- **Monitor from anywhere** — phone, tablet, or another computer; no install required for web viewers
- **Steer remotely** — send input, approve commands, or redirect the agent remotely
- **Team access** — share the link with teammates for observation or collaboration
- **Persistent cloud access** — session stays in sync while active; stops when you close or stop publishing

## How it works

Warp uploads the session state to the cloud and generates a shareable link. Any new agent output, tool use, or terminal activity appears for all viewers in real time.

Remote Control differs from standard Agent Session Sharing in intent: Session Sharing targets live collaborative work (pair-programming, interactive debugging), while Remote Control targets async monitoring and steering when away from your machine.

## Publishing a session

1. Start or resume a third-party agent session in Warp.
2. Click `/remote-control` in the agent utility bar. Warp publishes the session and copies the link.
3. A toast confirms the link; the status icon changes to a red broadcast indicator.
4. Open the link on another device, or share with a teammate.

To stop publishing, click **Stop sharing** in the agent utility bar.

## Accessing a remote session

- **Web browser** — open the shared link in any browser
- **Warp desktop app** — paste the link into Warp on a different machine
- **Mobile** — open the link in your phone or tablet browser

The web experience mirrors the desktop view, showing thinking steps, tool use, and terminal output.

## Permissions

- **View access** — anyone with the link can watch the session and see agent output
- **Edit access** — grant viewers permission to send input, approve commands, or redirect the agent

Only the publisher can revoke access or stop publishing.

## Related pages

- [[033-agent-platform-third-party-agents-overview|Third-Party CLI Agents]]
- [[042-agent-platform-warp-agents-capabilities-overview-session-sharing|Agent Session Sharing]]
