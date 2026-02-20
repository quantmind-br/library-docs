---
title: Design - Komorebi
url: https://lgug2z.github.io/komorebi/design.html
source: github_pages
fetched_at: 2026-02-20T08:45:00.277724-03:00
rendered_js: true
word_count: 183
summary: This document outlines the architectural design and hierarchical data model of the komorebi window manager, explaining how it interacts with external tools and organizes monitors, workspaces, and containers.
tags:
    - komorebi
    - window-management
    - architecture
    - data-model
    - windows-os
    - process-communication
category: concept
---

[](https://github.com/LGUG2Z/komorebi/edit/master/docs/design.md "Edit this page")[](https://github.com/LGUG2Z/komorebi/raw/master/docs/design.md "View source of this page")

## Description

*komorebi* only responds to [WinEvents](https://docs.microsoft.com/en-us/windows/win32/winauto/event-constants) and the messages it receives on a dedicated socket.

*komorebic* is a CLI that writes messages on *komorebi*'s socket.

*komorebi* doesn't handle any keyboard or mouse inputs; a third party program (e.g. [whkd](https://github.com/LGUG2Z/whkd)) is needed in order to translate keyboard and mouse events to *komorebic* commands.

This architecture, popularised by [*bspwm*](https://github.com/baskerville/bspwm) on Linux and [*yabai*](https://github.com/koekeishiya/yabai) on macOS, is outlined as follows:

```
          PROCESS                SOCKET
whkd/ahk  -------->  komorebic  <------>  komorebi
```

## Data Model

*komorebi* holds a list of physical monitors.

A monitor is just a rectangle of the available work area which contains one or more virtual workspaces.

A workspace holds a list of containers.

A container is just a rectangle where one or more application windows can be displayed.

This means that:

- Every monitor has its own collection of virtual workspaces
- Workspaces only know about containers and their dimensions, not about individual application windows
- Every application window must belong to a container, even if that container only contains one application window
- Many application windows can be stacked and cycled through in the same container within a workspace