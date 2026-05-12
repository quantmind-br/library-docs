---
title: !!binary NSDvv72AkCBQaXBlcw==
url: https://github.com/dj95/zjstatus/wiki/5-‐-Pipes
source: wiki
fetched_at: 2026-04-30T12:58:29.949472374-03:00
rendered_js: false
word_count: 218
summary: This document outlines the protocol for using Zellij plugin pipes to remotely control the zjstatus plugin by sending structured command messages.
tags:
    - zellij
    - zjstatus
    - plugin-pipes
    - remote-control
    - command-line
    - terminal-tools
category: api
---

With version 0.40.0, zellij introduces [pipes for plugins](https://github.com/zellij-org/zellij/pull/3066), which allow to pipe arbitrary data to plugins. This allows us to implement a handler, that processes arbitrary commands from outside of zjstatus. As a result we gain some remote control features.

> [!IMPORTANT]
> Make sure you are using zellij 0.40.0 or newer!


Here's an example of how to send a command to zjstatus. Run the following command **within** the same zellij session:

```bash
zellij pipe "zjstatus::notify::Hello, World!"
```

## Commands

The following commands are currently supported.

### Notify

**Command** `notify`  
**Arguments** `message`  
**Example** `zjstatus::notify::Hello, World!`

Displays a notification with the given body in the notification widget.

### Rerun

**Command** `rerun`  
**Arguments** `command_name`  
**Example** `zjstatus::rerun::command_pwd`

Force to run the command with the given name again.

## Protocol description

As the name indicate, the protocol sends messages via lines. This means, that each line will try to be interpreted as one command. Each line has the following structure:

```plaintext
{{prefix}}::{{command}}::{{args}}
```

`{{prefix}}` is always `zjstatus`, such that zjstatus will be able to distinguish between messages for other plugins and itself. `{{command}}` is the command you want to transmit to zjstatus. The third part is variadic and can provide arguments to the command to run. In case of rerun it is the command name as written in the layouts (e.g. `command_date`).
