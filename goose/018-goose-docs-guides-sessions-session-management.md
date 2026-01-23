---
title: Session Management | goose
url: https://block.github.io/goose/docs/guides/sessions/session-management
source: github_pages
fetched_at: 2026-01-22T22:14:28.589695022-03:00
rendered_js: true
word_count: 1241
summary: This document provides instructions for managing the full session lifecycle in goose, covering how to start, name, search, resume, and delete sessions across desktop and CLI interfaces.
tags:
    - session-management
    - goose-desktop
    - goose-cli
    - workflow-automation
    - search-functionality
    - keyboard-shortcuts
category: guide
---

A session is a single, continuous interaction between you and goose, providing a space to ask questions and prompt action. This guide covers how to manage the session lifecycle.

## Start Session[​](#start-session "Direct link to Start Session")

- goose Desktop
- goose CLI

When you open goose, you'll see the session interface ready for use. Just type—[or speak](https://block.github.io/goose/docs/guides/sessions/in-session-actions#voice-dictation "Learn how to enable voice dictation")—your questions, requests, or instructions directly into the input field, and goose will immediately get to work.

When you're ready to work on a new task, you can start a new session in the same directory or a different one. This directory is where goose reads and writes files by default.

- Same Directory
- Different Directory

To start a session in the same goose window:

1. Click the button in the top-left to open the sidebar
2. Click `Home` in the sidebar
3. Send your first prompt from the chat box

To start a session in a new goose window:

1. Click the button in the top-left
2. In the new goose window, send your first prompt from the chat box

tip

On macOS, you can use the goose dock icon to quickly start sessions:

- **Drag and drop** a folder onto the goose icon to open a new session in that directory
- **Right-click** the goose icon and select `New Window` to open a new session in your most recent directory

You can also use keyboard shortcuts to start a new session or manage goose windows.

ActionmacOSWindows/LinuxNew Session with [Quick Launcher](#quick-launcher)`Cmd+Option+Shift+G``Ctrl+Alt+Shift+G`New Session in Current Directory`Cmd+N``Ctrl+N`New Session in Current Directory (Same Window)`Cmd+T``Ctrl+T`New Session in Different Directory`Cmd+O``Ctrl+O`Toggle Sidebar`Cmd+B``Ctrl+B`Open Settings`Cmd+,``Ctrl+,`Keep goose Window Always on Top`Cmd+Shift+T``Ctrl+Shift+T`

#### Quick Launcher[​](#quick-launcher "Direct link to Quick Launcher")

Start a new session by typing your prompt into a popup:

1. Press `Cmd+Option+Shift+G` (macOS) or `Ctrl+Alt+Shift+G` (Windows/Linux) to open the popup
2. Type your prompt and press `Enter`

The session opens to your most recently opened directory in a new goose window.

## Name Session[​](#name-session "Direct link to Name Session")

- goose Desktop
- goose CLI

In the Desktop app, session tiles display auto-generated descriptions based on the context of your initial prompt.

You can edit session descriptions after they're created:

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Hover over the session you'd like to rename
4. Click the button that appears on the session card
5. In the "Edit Session Description" modal that opens:
   
   - Enter your new session description (up to 200 characters)
   - Press `Enter` to save or `Escape` to cancel
   - Or click the `Save` or `Cancel` buttons
6. A success toast notification will confirm the change

tip

Session descriptions help you manage multiple goose windows. When you're in the goose chat interface, session descriptions appear in the `Window` menu and in the Dock (macOS) or taskbar (Windows) menu, making it easy to identify and switch between different goose sessions.

## Exit Session[​](#exit-session "Direct link to Exit Session")

Note that sessions are automatically saved when you exit.

- goose Desktop
- goose CLI

To exit a session, simply close the application.

## Search Sessions[​](#search-sessions "Direct link to Search Sessions")

Search allows you to find specific content within sessions or find specific sessions.

- goose Desktop
- goose CLI

You can use keyboard shortcuts and search bar buttons to search sessions in goose Desktop.

ActionmacOSWindows/LinuxOpen Search`Cmd+F``Ctrl+F`Next Match`Cmd+G` or `↓``Ctrl+G` or `↓`Previous Match`Shift+Cmd+G` or `↑``Shift+Ctrl+G` or `↑`Use Selection for Find`Cmd+E`n/aToggle Case-Sensitivity`Aa``Aa`Close Search`Esc` or `X``Esc` or `X`

The following scenarios are supported:

#### Search Within Current Session[​](#search-within-current-session "Direct link to Search Within Current Session")

To find specific content within your current session:

1. Use `Cmd+F` to open the search bar
2. Enter your search term
3. Use shortcuts and search bar buttons to navigate the results

#### Search For Session By Name or Path[​](#search-for-session-by-name-or-path "Direct link to Search For Session By Name or Path")

To search all your sessions by name or working directory path:

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Use `Cmd+F` to open the search bar
4. Enter your search term
5. Use keyboard shortcuts and search bar buttons to navigate the results (`Cmd+E` not supported)

This is a metadata-only search. It doesn't search conversation content. Note that searching by session ID (e.g. `20251108_1`) is supported, but this property isn't displayed in the UI.

tip

You can [rename sessions](#name-session) to give them descriptive names that you'll remember later.

#### Search Across All Session Content[​](#search-across-all-session-content "Direct link to Search Across All Session Content")

To search conversation content across all your sessions, ask goose directly in any chat session. For example:

- "Find my earlier conversation about React hooks from last week"
- "Show me sessions where I worked on database migrations"

goose will search your session history and show relevant conversations with context from matching sessions.

#### Search Within Historical Session[​](#search-within-historical-session "Direct link to Search Within Historical Session")

To find specific content within a historical session:

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Click a specific session tile from the list to view its content
4. Use `Cmd+F` to open the search bar
5. Enter your search term
6. Use keyboard shortcuts and search bar buttons to navigate the results

No Regex or operator support

Using regular expressions or search operators in search text isn't supported.

## Resume Session[​](#resume-session "Direct link to Resume Session")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Click the session you'd like to resume. goose provides [search features](#search-sessions) to help you find the session.
4. Choose how to resume:
   
   - Click `Resume` to continue in the current window
   - Click `New Window` to open in a new window

tip

You can also quickly resume one of your three most recent sessions by clicking it in the `Recent chats` section on the `Home` page.

### Resume Session Across Interfaces[​](#resume-session-across-interfaces "Direct link to Resume Session Across Interfaces")

You can resume a CLI session in Desktop.

- goose Desktop
- goose CLI

All saved sessions are listed in the Desktop app, even CLI sessions. To resume a CLI session within the Desktop:

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Click the session you'd like to resume
4. Choose how to resume:
   
   - Click `Resume` to continue in the current window
   - Click `New Window` to open in a new window

### Resume Project-Based Sessions[​](#resume-project-based-sessions "Direct link to Resume Project-Based Sessions")

- goose Desktop
- goose CLI

Project-based sessions are only available through the CLI.

## Delete Sessions[​](#delete-sessions "Direct link to Delete Sessions")

- goose Desktop
- goose CLI

You can delete sessions directly from the Desktop app:

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Find the session you want to delete
4. Hover over the session card to reveal the action buttons
5. Click the button that appears
6. Confirm the deletion in the modal that appears

Permanent deletion

Deleting a session from goose Desktop will also delete it from the CLI. This action cannot be undone.

The session will be immediately removed from your session history and the underlying session record will be deleted from local storage.

## Import Sessions[​](#import-sessions "Direct link to Import Sessions")

- goose Desktop
- goose CLI

Import complete sessions from JSON files to restore, share, or migrate sessions between goose instances. Importing creates a new session with a new ID rather than overwriting existing sessions.

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Click the `Import Session` button in the top-right corner
4. Select a `.json` session file that was previously exported from goose
5. The session will be imported with a new session ID
6. A success notification will confirm the import

## Export Sessions[​](#export-sessions "Direct link to Export Sessions")

- goose Desktop
- goose CLI

Export complete sessions as JSON files for backup, sharing, migration, or archival. Exported files preserve all session data including conversation history, metadata, and settings.

1. Click the button in the top-left to open the sidebar
2. Click `History` in the sidebar
3. Find the session you want to export
4. Hover over the session card to reveal the action buttons
5. Click the button that appears
6. The session will be downloaded as a `.json` file named after the session description