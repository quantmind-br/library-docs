---
title: Mouse Capture
url: https://ratatui.rs/concepts/backends/mouse-capture/
source: crawler
fetched_at: 2026-02-01T21:13:05.757634474-03:00
rendered_js: false
word_count: 120
summary: This document explains the concept of mouse capture in terminal applications, describing how mouse events are sent to programs to enable interactive user experiences.
tags:
    - mouse-capture
    - terminal-events
    - input-handling
    - tui
    - backend-compatibility
category: concept
---

Mouse capture is a mode where the terminal captures mouse events such as clicks, scrolls, and movement, and sends them to the application as special sequences or events. This enables the application to handle and respond to mouse actions, providing a more interactive and graphical user experience within the terminal. It’s particularly useful for applications like terminal-based games, text editors, or other programs that require more direct interaction from the user.

Each backend handles mouse capture differently, with variations in the types of events that can be captured and how they are represented. As such, the behavior may vary depending on the backend being used, and developers should consult the specific backend’s documentation to understand how it implements mouse capture.