---
title: Expanding functionality
url: https://wiki.hypr.land/Configuring/Expanding-functionality/
source: sitemap
fetched_at: 2026-04-26T09:49:20.457677244-03:00
rendered_js: false
word_count: 75
summary: IPC sockets for Hyprland — socket1 for commands via hyprctl, socket2 for event-driven automation.
tags:
    - hyprland
    - ipc
    - socket-communication
    - bash-scripting
    - linux-desktop
    - automation
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Hyprland exposes two IPC sockets:

- **socket1** — controlled via `hyprctl`. See [[066-configuring-using-hyprctl|Using hyprctl]].
- **socket2** — sends events for changes/actions. See [[077-ipc|IPC]].

## Example Script

Changes outer gaps to 20 on monitor DP-1, 30 otherwise:

```bash
#!/usr/bin/env bash
function handle {
  if [[ ${1:0:10} == "focusedmon" ]]; then
    if [[ ${1:12:4} == "DP-1" ]]; then
      hyprctl keyword general:gaps_out 20
    else
      hyprctl keyword general:gaps_out 30
    fi
  fi
}
socat - "UNIX-CONNECT:$XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock" | while read -r line; do handle "$line"; done
```

> [!info] Last updated: April 20, 2026

[[066-configuring-using-hyprctl|Using hyprctl]] [[050-configuring-xwayland|XWayland]]

#ipc #automation #hyprland
