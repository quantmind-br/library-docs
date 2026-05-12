---
title: Cloud-synced conversations | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/cloud-conversations
source: sitemap
fetched_at: 2026-04-29T15:03:58.037320922-03:00
rendered_js: false
word_count: 579
summary: This document explains how to enable, manage, and share cloud-synced conversations within the Warp platform to ensure persistence across devices and facilitate collaboration.
tags:
    - warp-terminal
    - cloud-sync
    - agent-platform
    - conversation-management
    - data-persistence
    - collaboration-tools
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
Warp syncs [agent conversations](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents) to the cloud for cross-device access, teammate sharing, and persistence after logout.

## Key capabilities

- **Persistence across devices** — conversations available after logout or on different machines
- **Access past cloud agent conversations** — view and restore after completion
- **Link sharing with access controls** — share with teammates or specific people
- **Web viewing** — view shared conversations in a browser without Warp
- **Local continuation** — restore any cloud conversation locally

## Enabling cloud conversations

1. Open **Settings** → **Privacy**
2. Enable **Store AI conversations in the cloud**

When enabled, conversations sync automatically after each Agent interaction. When disabled, conversations stored locally only.

> [!warning]
> If disabled: data lost on logout, cannot be shared. Cloud agent conversations are always stored in the cloud regardless of this setting.

## How it works

### Conversation syncing

Warp syncs conversation state as snapshots after each interaction. If you open the same conversation on two machines, each continues independently—changes don't sync in real time.

### Continuing vs. forking

| Action | Behavior |
|--------|----------|
| **Continue own conversation** | Updates sync back to cloud |
| **Continue shared conversation** | Creates a fork—a new conversation with shared context, original unchanged |

This mirrors [Conversation Forking](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/conversation-forking).

## Managing conversations

Cloud-synced conversations appear alongside local conversations. Operations:

| Action | Description |
|--------|-------------|
| **Browse** | View all local and cloud-synced conversations in one place |
| **Search** | Find by title or content |
| **Restore** | Click to load into current session and continue |
| **Delete** | Permanent, immediate removal |

See [Interacting with Agents](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents) and [Terminal and Agent modes](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/terminal-and-agent-modes) for keyboard shortcuts and navigation.

## Sharing conversations

Share any cloud conversation via link.

**To share:**
1. Open the conversation
2. Access share options through the conversation menu
3. Configure permissions:

| Permission | Access Level |
|------------|--------------|
| **Anyone on your team** (default) | All team members can view |
| **Specific people** | Email addresses granted access |
| **Anyone with the link** | No authentication required |

### Viewing shared conversations

- **On the web** — open link in browser to view transcript without Warp
- **In Warp** — click "Open in Warp" to load in desktop app

Continuing a shared conversation creates a fork—build on context without modifying the original.

> [!info]
> For real-time collaboration on a live session, use [Agent Session Sharing](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/session-sharing).

## Cloud agent conversations

[Cloud agents](https://docs.warp.dev/agent-platform/cloud-agents/overview) run in the cloud; their conversations are automatically stored regardless of the local cloud conversations setting.

### Accessing cloud agent conversations

- **View transcripts** — access full conversation history of any past run
- **Restore locally** — load into local session to review or continue work

## Privacy and data

### Enterprise controls

Enterprise admins can disable cloud conversation storage via the [Admin Panel](https://docs.warp.dev/knowledge-and-collaboration/admin-panel).

When disabled:
- Conversations stored locally only
- Cannot share or access across devices
- Cloud agent conversations still accessible through Warp dashboard

### Storage limits

Limits vary by plan. Free users: oldest cloud conversations auto-removed when limit reached. Local copies always preserved—only cloud-synced copies removed.

See [pricing page](https://www.warp.dev/pricing) for current limits.

### Deleting conversations

> [!danger]
> Deletion is permanent and immediate. Ensure you no longer need a conversation before deleting.

## Related pages

- [Interacting with Agents](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents) — conversation mechanics, follow-ups, context windows
- [Session Sharing](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/session-sharing) — real-time collaboration on live sessions
- [Cloud Agents Overview](https://docs.warp.dev/agent-platform/cloud-agents/overview) — run agents from triggers, schedules, or integrations