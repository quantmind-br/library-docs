---
title: Warp Drive overview | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive
source: sitemap
fetched_at: 2026-04-29T15:03:29.008780334-03:00
rendered_js: false
word_count: 619
summary: This document provides an overview of Warp Drive, explaining how to manage, sync, share, and organize collaborative objects like workflows, notebooks, and prompts.
tags:
    - warp-drive
    - collaboration
    - cloud-sync
    - team-management
    - file-sharing
    - keyboard-shortcuts
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What is Warp Drive?

All objects stored in Warp Drive sync immediately as updated, so you and your team always have the latest versions.

Access Warp Drive from the status bar or toggle the side panel with `CMD-\`.

## Workspaces

When you open Warp Drive, you'll find:

- **Personal workspace** — store Workflows, Notebooks, Prompts, and Environment Variables, organized into folders.
- **Team workspace** — available if you're a member of a team.

## Organizing Objects with Your Team

- Objects and folders can be sorted alphabetically or by last updated.
- Moving objects from your personal workspace into a team workspace shares them with all team members.
- Items cannot be moved back from a team workspace to personal. If shared inadvertently, copy the contents, recreate in your personal workspace, then delete from the team workspace.
- Folders cannot be dragged as a group into a team workspace — move objects one at a time.

## Offline Mode

In offline mode, some files are read-only. You can create and edit files in your personal space, but they save locally and don't sync. They cannot be moved into a team or deleted until back online.

## Keyboard Navigation

Use keyboard to navigate Warp Drive once opened or focused (`CMD-\` or click blank area).

| Key | Action |
|---|---|
| `UP`/`DOWN` or `j`/`k` | Navigate to object |
| `Enter` | Execute object, open/collapse workspace or folder, open trash |
| `CMD-ENTER` | Open object's context menu |
| `CMD-SHIFT-(` / `CMD-SHIFT-)` | Switch focus between terminal and Warp Drive |
| `LEFT-ARROW` | Collapse workspace or folder |
| `RIGHT-ARROW` | Open workspace or folder |
| `Esc` | Return to Warp Drive from trash |

To switch panels via keyboard, use "Switch Focus to Left Panel" / "Switch Focus to Right Panel" in the [Command Palette](https://docs.warp.dev/terminal/command-palette).

## Import and Export

| Object | Import | Export |
|---|---|---|
| [Workflows](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows) | YAML (.yaml, .yml) | YAML (.yaml, .yml) |
| [Prompts](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/prompts) | Not supported | YAML (.yaml, .yml) |
| [Notebooks](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/notebooks) | Markdown (.md) | Markdown (.md) |
| [Environment Variables](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/environment-variables) | Not supported | DOTENV (.env) |

**Import:** `RIGHT-CLICK` a folder or click **+** on a workspace → "Import." Directories import with matching folder structure.

**Export:** `RIGHT-CLICK` an object → "Export." To export all objects: open Command Palette → "Export all Warp Drive objects."

## Sharing Objects

Every Warp Drive object can be shared three ways:
- **Teams** — all team members have full access.
- **Direct Sharing** — share with individuals by email.
- **Link Sharing** — make public to anyone with the link, including non-Warp users.

### Link Sharing

Navigate to the object's overflow menu → "Copy link." Share with teammates or reference in codebase, docs, or Slack.

> [!info]
> Link-followers must have permission (direct invite, team membership, or public access). Without permission, they can request access from the object owner or team admin.

### Managing Permissions

Navigate to the object's overflow menu → "Share," or use Command Palette → "Share pane," or click the share button in the pane header.

From this dialog you can:
- Invite users directly via email input.
- Change or remove public link-based access level.
- Update or remove individual user access.

Permissions inherit from parent folders (e.g., edit on a folder grants edit to all contents). Owners and teammates always have full access. When sharing, choose **view** or **edit**.

## Troubleshooting

- If you previously used Warp individually and were later invited to a team, exit, update, and restart Warp to access the team's shared drive and commands.
- Navigating to **Settings > Teams** also forces a metadata update, ensuring access to the latest Workflows.
