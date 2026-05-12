---
title: Make a Quake like quick access terminal
title: Quick access terminal
word_count: 198
summary: This document explains how to set up and configure a Quake-style quick access terminal window using the kitty terminal emulator's kitten utility.
category: guide
word_count: 198
optimized: true
optimized_at: 2026-05-04T20:44:49Z
---
optimized: true
optimized_at: 2026-05-04T18:00:00Z
# Make a Quake like quick access terminal

This kitten can be used to make a quick access terminal, that appears and
disappears at a key press. To do so use the following command:

```sh
kitten quick-access-terminal
```

Run this command in a terminal, and a quick access kitty window will show up at
the top of your screen. Run it again, and the window will be hidden.

To make the terminal appear and disappear at a key press:

## Configuration

You can configure the appearance and behavior of the quick access window
by creating a quick-access-terminal.conf file in your
kitty config folder <confloc>. In particular, you can use the
kitty_conf <kitten-quick_access_terminal.kitty_conf> option to change
various kitty settings, just for the quick access window.

> [!NOTE]
> This kitten uses the panel kitten </kittens/panel> under the
> hood. You can use the techniques described there <remote_control_panel>
> for remote controlling the quick access window, remember to add
> `kitty_override allow_remote_control=socket-only` and ``kitty_override
> listen_on=unix:/tmp/whatever`` to
> quick-access-terminal.conf.

See below for the supported configuration directives:

## Sample quick-access-terminal.conf

You can download a sample quick-access-terminal.conf file with all default settings and
comments describing each setting by clicking: :download:`sample quick-access-terminal.conf
</generated/conf/quick_access_terminal.conf>`.
