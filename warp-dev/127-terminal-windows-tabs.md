---
title: Tabs | Warp
url: https://docs.warp.dev/terminal/windows/tabs
source: sitemap
fetched_at: 2026-04-29T15:02:35.078700238-03:00
rendered_js: false
word_count: 205
summary: This document provides an overview of managing tabs in the Warp terminal, including keyboard shortcuts, configuration settings, and methods for customizing tab titles.
tags:
    - warp-terminal
    - tab-management
    - terminal-shortcuts
    - productivity
    - session-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!info]
> New tabs inherit the active tab's current [[working-directory|Working Directory]]. Tab colors derive from your [[themes|Warp Theme]].

## Keyboard shortcuts

| Action | Shortcut |
|---|---|
| Open new tab | `CMD-T` or click `+` in top bar |
| Close current tab | `CMD-W` or click `X` on hover |
| Reopen closed tab | `SHIFT-CMD-T` |
| Move tab left/right | `CTRL-SHIFT-LEFT` / `CTRL-SHIFT-RIGHT` or drag |
| Activate previous/next tab | `SHIFT-CMD-{` / `SHIFT-CMD-}` |
| Activate 1st–8th tab | `CMD-1` through `CMD-8` |
| Switch to last tab | `CMD-9` |
| Rename tab | Double-click |
| Right-click `+` | New tab, restore closed tab, or run saved [[124-terminal-windows-launch-configurations|Launch Configuration]] |

## Setting tab names via shell RC file

In `.zshrc` or `.bashrc`:

```bash
functionset_name(){
exportWARP_DISABLE_AUTO_TITLE=true
echo-ne"\033]0;MyTabName\007"
}
if[-n"$ZSH_VERSION"];then
preexec_functions+=(set_name)
elif[-n"$BASH_VERSION"];then
PROMPT_COMMAND='set_name'
fi
```

Replace `MyTabName` with a fixed string, `$PWD`, or any shell expression.

## Tab Restoration

Reopen recently closed tabs for up to 60 seconds via **Settings** > **Features** > **Session** > **Enable reopening of closed sessions**.

## CTRL-TAB behavior

`CTRL-TAB` activates previous/next tab by default. Configure it to cycle recent sessions (including [[125-terminal-windows-split-panes|split panes]]) in **Settings** > **Features** > **Keys** > **Ctrl-Tab behavior**.

## More settings

See [[tabs-behavior|Appearance > Tabs Behavior]] for additional tab-related settings.

#tabs
