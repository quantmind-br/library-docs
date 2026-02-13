---
title: Uninstalling Yabai
url: https://github.com/asmvik/yabai/wiki/Uninstalling-yabai
source: wiki
fetched_at: 2026-02-11T07:34:00.184571-03:00
rendered_js: false
word_count: 89
summary: This document provides a comprehensive set of commands and steps to completely uninstall the yabai window manager and remove all associated configuration, service, and temporary files from a macOS system.
tags:
    - yabai
    - macos
    - uninstallation
    - tiling-window-manager
    - homebrew
    - cleanup
category: guide
---

The following steps will help you remove all traces of yabai from your system.

```sh
# stop yabai
yabai --stop-service

# remove service file
yabai --uninstall-service

# uninstall the scripting addition
sudo yabai --uninstall-sa

# uninstall yabai
brew uninstall yabai

# these are logfiles that may be created when running yabai as a service.
rm -rf /tmp/yabai_$USER.out.log
rm -rf /tmp/yabai_$USER.err.log

# remove config and various temporary files
rm ~/.yabairc
rm /tmp/yabai_$USER.lock
rm /tmp/yabai_$USER.socket
rm /tmp/yabai-sa_$USER.socket

# unload the scripting addition by forcing a restart of Dock.app
killall Dock
```

