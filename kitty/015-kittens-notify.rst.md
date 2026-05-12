---
title: notify
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/notify.rst
source: git
fetched_at: 2026-05-04T15:58:01.434630989-03:00
rendered_js: false
word_count: 60
summary: Show pop-up system notifications from the shell with icons, buttons, and wait-for-completion support. Works over SSH.
tags:
    - system-notifications
    - shell-utilities
    - desktop-notifications
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# notify

*Pop-up system notifications from the shell*

```bash
# Basic notification
kitten notify "Good morning" Hello world, it is a nice day!

# With icon (file path or named icon)
kitten notify --icon-path /path/to/image.png "Title" Body
kitten notify --icon firefox "Title" Body
```

## Wait for Completion

```bash
kitten notify --wait-for-completion "Title" Body
```

Blocks until the notification is closed or activated:
- Activated → prints `0` to stdout
- `Esc` or `Ctrl+C` → aborts, closes notification

## Buttons

```bash
kitten notify --wait-for-completion --button One --button Two "Title" Body
```

Each button press prints `0` to stdout.

> [!tip]
> See [[047-desktop-notifications|desktop notifications escape code protocol]] for the underlying protocol.

#system-notifications #shell-utilities #desktop-notifications
