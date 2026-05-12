---
title: !!binary MiDvv72AkCBQZXJtaXNzaW9ucw==
url: https://github.com/dj95/zjstatus/wiki/2-‐-Permissions
source: wiki
fetched_at: 2026-04-30T12:58:26.424411883-03:00
rendered_js: false
word_count: 210
summary: This document explains the permission requirements for the zjstatus plugin in Zellij, detailing how to grant, revoke, and manage specific access rights for plugin functionality.
tags:
    - zellij
    - zjstatus
    - plugin-permissions
    - terminal-emulator
    - access-control
    - configuration
category: configuration
---

Zellij requires plugins to request permissions for different actions and information. These permissions must be granted by you before you start zjstatus. Permissions can be granted by navigating to the zjstatus pane either by keyboard shortcuts or clicking on the pane. Then simply type the letter `y` to approve permissions. This process must be repeated on zjstatus updates, since the file changes.


https://github.com/dj95/zjstatus/assets/4348959/b2d5e939-52fd-4e4e-8b1b-91f8a92df8c6

> [!TIP]
> This little weird circular icon with the arrow pointing to the top left is the escape key under macOS.

If you want to revoke permissions, simply clear the cache of zellij (`$HOME/.cache/zellij/` for Linux, `$HOME/Library/Caches/org.Zellij-Contributors.Zellij/ on macOS`).

zjstatus requires the following permissions.

| Permissions | Description |
|-------------|-------------|
| `ReadApplicationState` | This permission is required to read certain information out of zellij. E.g. the current mode, session name or tabs. |
| `ChangeApplicationState` | This permission is required for actions performed by zjstatus. E.g. the tab widget allows to switch tabs by clicking on their name. Without the permissions, this feature won't work. |
| `RunCommands` | This permission is only required and used by the `command` widget. Otherwise zjstatus will not be able to execute the command through zellij. Please make sure you know which commands are run within a layout file. |