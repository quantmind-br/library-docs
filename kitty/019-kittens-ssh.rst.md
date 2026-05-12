---
title: Truly convenient SSH
title: Truly convenient SSH
word_count: 349
summary: Describes how to use the kitty ssh kitten to automate remote host configuration, synchronization of shell environments, and terminal feature integration.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:24Z
---
# Truly convenient SSH

The ssh kitten automates remote host configuration, shell environment sync, and terminal feature integration. Run `kitten ssh user@host` as a drop-in replacement for `ssh`.

## Features

- Automatic shell_integration on remote hosts
- Clone local shell/editor config on remote hosts
- Re-use existing SSH connections to avoid setup latency (`share_connections`)
- Make kitten binary available on remote hosts on demand (`remote_kitty`)
- Change terminal colors when connecting to specific hosts (`color_scheme`)
- Forward kitty remote control socket to configured hosts (`forward_remote_control`)

## Quick Start

```bash
kitten ssh some-hostname-to-connect-to
```

For convenience, add an alias:

```bash
alias s="kitten ssh"
```

Then connect with `s hostname`.

Kitty keyboard shortcuts work too:

```conf
map f1 new_window_with_cwd
```

Pressing F1 opens a new window logged into the same host at the same directory.

## Configuration

Configure via `~/.config/kitty/ssh.conf`:

```conf
# Copy files/dirs to remote
copy .zshrc .vimrc .vim

# Environment variables on remote
env SOME_VAR=x
env COPIED_VAR=_kitty_copy_env_var_

# Per-hostname settings
hostname someserver-*
copy env-files
env SOMETHING=else

hostname someuser@somehost
copy --dest=foo/bar some-file
copy --glob some/files.*
```

Override config on command line:

```bash
kitten ssh --kitten interpreter=python servername
```

> [!WARNING]
> Due to SSH design limitations, typing before the shell prompt appears may be lost. Wait for the shell prompt before typing.

## Real-World Example

Setup zsh and vim configs on a production server without affecting other users:

```conf
hostname myserver-*

# zsh reads from custom dir
env ZDOTDIR=$HOME/my-conf/zsh
copy --dest my-conf/zsh/.zshrc .zshrc
copy --dest my-conf/zsh/.zshenv .zshenv

# vim reads from custom dir
env VIMINIT=$HOME/my-conf/vim/vimrc
env VIMRUNTIME=$HOME/my-conf/vim
copy --dest my-conf/vim .vim
copy --dest my-conf/vim/vimrc .vimrc
```

## How It Works

1. SSH transmits a bootstrap script (POSIX sh or Python via `interpreter`)
2. Script reads a Base64-encoded compressed tarball over the TTY
3. Extracts files (`copy`) and sets env vars (`env`)
4. Launches login shell with shell_integration enabled
5. Data is requested with a random one-time password; kitty validates it
6. OpenSSH >= 8.4: transmission is instant (no roundtrip delay)

> [!NOTE]
> BSD hosts may have crippled shells. Install Python on the remote, use POSIX sh, and set `interpreter=python` in ssh.conf.

> [!NOTE]
> Terminal multiplexers may interfere if escape codes aren't passed through or if `KITTY_PID`/`KITTY_WINDOW_ID` env vars are incorrect.

## Manual Terminfo Copy

If the ssh kitten fails or you prefer not to use it:

```bash
infocmp -a xterm-kitty | ssh myserver tic -x -o ~/.terminfo /dev/stdin
```

For macOS or proxy environments that block this:

```bash
# On local machine
infocmp -a xterm-kitty > /tmp/terminfo

# Copy to server, then run
tic -x -o ~/.terminfo /tmp/terminfo
```

On embedded/Android systems without `tic`, copy the file to `~/.terminfo/x/xterm-kitty`.

Modern Linux distros: install the `kitty-terminfo` package instead.

For FreeBSD or termcap-based systems, convert the terminfo to termcap format:

```bash
# On local machine
infocmp -CrT0 xterm-kitty

# Append output to /usr/share/misc/termcap on server
cap_mkdb /usr/share/misc/termcap
```

> [!NOTE]
> The correct long-term fix is convincing OpenSSH maintainers to handle this automatically for all terminals.

#ssh #terminal-emulator #remote-access #shell-integration
