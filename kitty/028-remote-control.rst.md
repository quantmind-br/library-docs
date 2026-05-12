---
title: Control kitty from scripts
url: https://github.com/kovidgoyal/kitty/blob/master/docs/remote-control.rst
source: git
fetched_at: 2026-05-04T15:58:27.442591183-03:00
rendered_js: false
word_count: 421
summary: Control kitty programmatically via the kitten @ messaging system — remote control via sockets, password-based authentication, fine-grained permissions, and key mappings.
tags:
    - kitty
    - terminal-emulator
    - remote-control
    - automation
    - scripting
    - cli-tools
category: guide
optimized: true
optimized_at: 2026-05-04T20:30:00Z
---
# Control kitty from scripts

kitty can be controlled from scripts or the shell. Open windows, send text to any window, change titles, and more via the `kitten @` messaging system.

## Tutorial

Start kitty with remote control enabled:

```bash
kitty -o allow_remote_control=yes -o enabled_layouts=tall
```

> [!NOTE]
> `allow_remote_control` or `remote_control_password` must be enabled in `kitty.conf`.

Launch a new window running `cat`:

```bash
kitten @ launch --title Output --keep-focus cat
```

Send text to that window:

```bash
kitten @ send-text --match cmdline:cat Hello, World
```

Pipe command output to a window:

```bash
ls | kitten @ send-text --match 'title:^Output' --stdin
```

Type into a different window (Ctrl+D to finish):

```bash
kitten @ send-text --match 'title:^Output' --stdin
```

Open a new tab:

```bash
kitten @ launch --type=tab --tab-title "My Tab" --keep-focus bash
```

Manage tabs and windows:

```bash
kitten @ set-tab-title --match 'title:^My' "New Title"  # change tab title
kitten @ set-tab-title "Master Tab"                      # current tab
kitten @ focus-tab --match 'title:^New'                 # switch tab
kitten @ focus-window --match 'title:^Output'           # focus window
```

List all tabs and windows:

```bash
kitten @ ls
```

Returns JSON: OS windows → tabs → windows. Each window has `id`, `title`, `cwd`, `pid`, and `cmdline`. Use with `--match` to target specific windows.

> [!NOTE]
> `kitten @` works over SSH when run inside a kitty window. For programs/scripts outside kitty, use socket-based remote control.

> [!tip]
> For a single kitty daemon with subsequent invocations as new top-level windows, use `kitty --single-instance`.

## Remote control via socket

Control kitty from outside the terminal:

```bash
# Start kitty listening on a socket
kitty -o allow_remote_control=yes --listen-on unix:/tmp/mykitty

# Control it from anywhere
kitten @ --to unix:/tmp/mykitty ls
```

## Builtin kitty shell

Run `kitten @` with no arguments to enter an interactive shell with completion. Map to a shortcut with `kitty_shell` (default).

## Allowing only some windows to control kitty

Restrict remote control to specific windows via shortcut:

```conf
map ctrl+k launch --allow-remote-control some_program
```

Programs in windows created this way can use `kitten @`. Further restrict with:

```bash
kitten @ launch --remote-control-password
```

## Fine-grained permissions with passwords

Grant different access levels to different sources via `remote_control_password` in `kitty.conf`. Set `allow_remote_control to password` to enable.

```conf
remote_control_password "control colors" get-colors set-colors
```

```bash
kitten @ --password="control colors" set-colors background=red
```

Password via environment or file:

```bash
KITTY_RC_PASSWORD="control colors"     # env var
~/.config/kitty/rc-pass                 # file
```

Use glob patterns for action matching:

```conf
remote_control_password "control colors" *-colors
```

> [!NOTE]
> For SSH password auth, pass `KITTY_PUBLIC_KEY` to the remote host — the ssh kitten does this automatically. Uses `rc_crypto` for security. Clock sync required. Slow for large data (e.g., `set-background-image`).

### Custom authorization script

```conf
remote_control_password "testing custom auth" my_rc_auth.py
```

```py
def is_cmd_allowed(pcmd, window, from_socket, extra_data):
    cmd_name = pcmd['cmd']
    cmd_payload = pcmd['payload']
    # Return True/False to allow/disallow, None for no effect
    if cmd_name != 'launch':
        return None
    if cmd_payload.get('args') or cmd_payload.get('env'):
        return False
    return True
```

> [!NOTE]
> Command payloads are documented in the [[058-rc-protocol.rst|The kitty remote control protocol]].

## Mapping key presses to remote control commands

```conf
map f1 remote_control set-spacing margin=30
```

Prefix with `!` to ignore errors:

```conf
map f1 remote_control !focus-window --match XXXXXX
```

Run a script:

```conf
map f1 remote_control_script /path/to/myscript
```

Scripts run `kitten @` commands with `launch --type=background --allow-remote-control`. Relative paths resolved from the kitty config directory.

> [!NOTE]
> `allow_remote_control` is not required for these mappings — they use the remote control infrastructure directly.

## Broadcasting to all windows

Send what you type to all open kitty windows:

```conf
map f1 launch --allow-remote-control kitty +kitten broadcast
```

Press F1 and start typing — input is live-broadcast to all windows.

## Remote control protocol

Develop your own client using the [[058-rc-protocol.rst|remote control protocol]]. A standalone `kitten` binary is also available from the kitty releases page:

```bash
kitten @ --help
```

## Matching windows and tabs

The `--match` option selects targets using `field:query` expressions:

```
title:"My special window" or id:43
title:bash and env:USER=kovid
not id:1
(id:2 or id:3) and title:something
```

#kitty #terminal-emulator #remote-control #automation #scripting
