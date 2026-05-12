---
title: Shell integration
title: Shell integration
word_count: 2137
summary: This document explains how to configure and use kitty's shell integration to enable advanced features like prompt navigation, command output browsing, and terminal state synchronization.
category: configuration
optimized: true
optimized_at: 2026-05-04T20:46:25Z
---
optimized: true
optimized_at: 2026-05-04T18:00:00Z
# Shell integration

kitty has the ability to integrate closely within common shells, such as `zsh
<https://www.zsh.org/>`__, [fish](https://fishshell.com) and `bash
<https://www.gnu.org/software/bash/>`__ to enable features such as jumping to
previous prompts in the scrollback, viewing the output of the last command in
less, using the mouse to move the cursor while editing prompts, etc.

# Features

- Open the output of the last command in a pager such as less
  (show_last_command_output)

- Jump to the previous/next prompt in the scrollback
  (scroll_to_previous_prompt /  scroll_to_next_prompt)

- Click with the mouse anywhere in the current command to move the cursor there

- Hold Ctrl+Shift and right-click on any command output in the scrollback
  to view it in a pager

- The current working directory or the command being executed are automatically
  displayed in the kitty window titlebar/tab title

- The text cursor is changed to a bar when editing commands at the shell prompt

- clone_shell with all environment variables and the working directory
  copied

- Edit files in new kitty windows <edit_file> even over SSH

- Glitch free window resizing even with complex prompts. Achieved by erasing
  the prompt on resize and allowing the shell to redraw it cleanly.

- Sophisticated completion for the kitty command in the shell.

- When confirming a quit command if a window is sitting at a shell prompt,
  it is not counted (for details, see confirm_os_window_close)

# Configuration

Shell integration is controlled by the shell_integration option. By
default, all integration features are enabled. Individual features can be turned
off or it can be disabled entirely as well. The shell_integration option
takes a space separated list of keywords:

disabled
    Turn off all shell integration. The shell's launch environment is not
    modified and KITTY_SHELL_INTEGRATION is not set. Useful for
    manual integration <manual_shell_integration>.

no-rc
    Do not modify the shell's launch environment to enable integration. Useful
    if you prefer to load the kitty shell integration code yourself, either as
    part of manual integration <manual_shell_integration> or because
    you have some other software that sets up shell integration.
    This will still set the KITTY_SHELL_INTEGRATION environment
    variable when kitty runs the shell.

no-cursor
    Turn off changing of the text cursor to a bar when editing shell command
    line.

no-title
    Turn off setting the kitty window/tab title based on shell state.
    Note that for the fish shell kitty relies on fish's native title setting
    functionality instead.

no-cwd
    Turn off reporting the current working directory. This is used to allow
    new_window_with_cwd and similar to open windows logged into remote
    machines using the ssh kitten <kittens/ssh> automatically with the
    same working directory as the current window.
    Note that for the fish shell this will not disable its built-in current
    working directory reporting.

no-prompt-mark
    Turn off marking of prompts. This disables jumping to prompt, browsing
    output of last command and click to move cursor functionality.
    Note that for the fish shell this does not take effect, since fish always
    marks prompts.

no-complete
    Turn off completion for the kitty command.
    Note that for the fish shell this does not take effect, since fish already
    comes with a kitty completion script.

no-sudo
    Do not alias sudo to ensure the kitty terminfo files are
    available in the sudo environment. This is needed if you have sudo
    configured to disable setting of environment variables on the command line.
    By default, if sudo is configured to allow all commands for the current
    user, setting of environment variables at the command line is also allowed.
    Only if commands are restricted is this needed.

## More ways to browse command output

You can add further key and mouse bindings to browse the output of commands
easily. For example to select the output of a command by right clicking the
mouse on the output, define the following in kitty.conf:

```conf
mouse_map right press ungrabbed mouse_select_command_output
```

Now, when you right click on the output, the entire output is selected, ready
to be copied.

The feature to jump to previous prompts (
scroll_to_previous_prompt and scroll_to_next_prompt) and mouse
actions (mouse_select_command_output and mouse_show_command_output)
can be integrated with browsing command output as well. For example, define the
following mapping in kitty.conf:

```conf
map f1 show_last_visited_command_output
```

Now, pressing F1 will cause the output of the last jumped to command or
the last mouse clicked command output to be opened in a pager for easy browsing.

In addition, You can define shortcut to get the first command output on screen.
For example, define the following in kitty.conf:

```conf
map f1 show_first_command_output_on_screen
```

Now, pressing F1 will cause the output of the first command output on
screen to be opened in a pager.

You can also add shortcut to scroll to the last jumped position. For example,
define the following in kitty.conf:

```conf
map f1 scroll_to_prompt 0
```

# How it works

At startup, kitty detects if the shell you have configured (either system wide
or the shell option in kitty.conf) is a supported shell. If so,
kitty injects some shell specific code into the shell, to enable shell
integration. How it does so varies for different shells.

Then, when launching the shell, kitty sets the environment variable
KITTY_SHELL_INTEGRATION to the value of the shell_integration
option. The shell integration code reads the environment variable, turns on the
specified integration functionality and then unsets the variable so as to not
pollute the system.

The actual shell integration code uses hooks provided by each shell to send
special escape codes to kitty, to perform the various tasks. You can see the
code used for each shell below:

# Shell integration over SSH

The easiest way to have shell integration work when SSHing into remote systems
is to use the ssh kitten <kittens/ssh>. Simply run:

```
kitten ssh hostname
```

And, by magic, you will be logged into the remote system with fully functional
shell integration. Alternately, you can :ref:`setup shell integration manually
<manual_shell_integration>`, by copying the kitty shell integration scripts to
the remote server and editing the shell rc files there, as described below.

# Shell integration in a container

Install the kitten `standalone binary
<https://github.com/kovidgoyal/kitty/releases/latest/download/kitten-linux-amd64>`__ in the container
somewhere in the PATH, then you can log into the container with:

```sh
docker exec -ti container-id kitten run-shell --shell=/path/to/your/shell/in/the/container
```

The kitten will even take care of making the kitty terminfo database available
in the container automatically.

# Clone the current shell into a new window

You can clone the current shell into a new kitty window by simply running the
clone-in-kitty command, for example:

```sh
clone-in-kitty
clone-in-kitty --type=tab
clone-in-kitty --title "I am a clone"
```

This will open a new window running a new shell instance but with all
environment variables and the current working directory copied. This even works
over SSH when using kittens/ssh.

The clone-in-kitty command takes almost all the same arguments as the
launch <launch> command, so you can open a new tab instead or a new OS
window, etc. Arguments of launch that that don't
make sense when cloning are ignored. Most prominently, the following options are
ignored: --allow-remote-control <launch --allow-remote-control>,
--copy-cmdline <launch --copy-cmdline>, :option:`--copy-env <launch
--copy-env>`, --stdin-source <launch --stdin-source>,
--marker <launch --marker> and --watcher <launch --watcher>.

clone-in-kitty can be configured to source arbitrary code in the
cloned window using environment variables. It will automatically clone virtual
environments created by the :link:`Python venv module
<https://docs.python.org/3/library/venv.html>` or :link:`Conda
<https://conda.io/>`. In addition, setting the
env var KITTY_CLONE_SOURCE_CODE to some shell code will cause that
code to be run in the cloned window with eval. Similarly, setting
KITTY_CLONE_SOURCE_PATH to the path of a file will cause that file to
be sourced in the cloned window. This can be controlled by
clone_source_strategies.

clone-in-kitty works by asking the shell to serialize its internal
state (mainly CWD and env vars) and this state is transmitted to kitty and
restored by the shell integration scripts in the cloned window.

# Edit files in new kitty windows even over SSH

```sh
edit-in-kitty myfile.txt
edit-in-kitty --type tab --title "Editing My File" myfile.txt
# open myfile.txt at line 75 (works with vim, neovim, emacs, nano, micro)
edit-in-kitty +75 myfile.txt
```

The edit-in-kitty command allows you to seamlessly edit files
in your default editor in new kitty windows. This works even over
SSH (if you use the ssh kitten <kittens/ssh>), allowing you
to easily edit remote files in your local editor with all its bells and
whistles.

The edit-in-kitty command takes almost all the same arguments as the
launch <launch> command, so you can open a new tab instead or a new OS
window, etc. Not all arguments are supported, see the discussion in the
clone_shell section above.

In order to avoid remote code execution, kitty will only execute the configured
editor and pass the file path to edit to it and it will strip all environment
variables from the edit-in-kitty command line. Additionally, parsing
of colors is more limited, reading colors from config files is not allowed.

> [!NOTE]
> To edit files using sudo the best method is to set the
>
> then edit the file using the `sudoedit` or `sudo -e` commands.

# Using shell integration in sub-shells, containers, etc.

To start a sub-shell with shell integration automatically setup, simply run:

```
kitten run-shell
```

This will start a sub-shell using the same binary as the currently running
shell, with shell-integration enabled. To start a particular shell use:

```
kitten run-shell --shell=/bin/bash
```

To run a command before starting the shell use:

```
kitten run-shell ls .
```

This will run `ls .` before starting the shell.

This will even work on remote systems where kitty itself is not installed,
provided you use the SSH kitten <kittens/ssh> to connect to the system.
Use `kitten run-shell --help` to learn more.

# Manual shell integration

The automatic shell integration is designed to be minimally intrusive, as such
it won't work for sub-shells, terminal multiplexers, containers, etc.
For such systems, you should either use the run-shell <run_shell> command described above or
setup manual shell integration by adding some code to your shells startup files to load the shell integration script.

First, in kitty.conf set:

```conf
shell_integration disabled
```

Then in your shell's rc file, add the lines:

The value of KITTY_SHELL_INTEGRATION is the same as that for
shell_integration, except if you want to disable shell integration
completely, in which case simply do not set the
KITTY_SHELL_INTEGRATION variable at all.

In a container, you will need to install the kitty shell integration scripts
and make sure the KITTY_INSTALLATION_DIR environment variable is set
to point to the location of the scripts.

# Integration with other shells

There exist third-party integrations to use these features for various other
shells:

- Jupyter console and IPython via a patch (4475)
- [xonsh](https://github.com/xonsh/xonsh/issues/4623)
- [Nushell](https://github.com/nushell/nushell/discussions/12065): Set `$env.config.shell_integration = true` in your `config.nu` to enable it.

# Notes for shell developers

The protocol used for marking the prompt is very simple. You should consider
adding it to your shell as a builtin. Many modern terminals make use of it, for
example: kitty, iTerm2, WezTerm, DomTerm

Just before starting to draw the PS1 prompt send the escape code:

```none
<OSC>133;A<ST>
```

Just before starting to draw the PS2 prompt send the escape code:

```none
<OSC>133;A;k=s<ST>
```

Just before running a command/program, send the escape code:

```none
<OSC>133;C<ST>
```

Optionally, when a command is finished its "exit status" can be reported as:

```none
<OSC>133;D;exit status as base 10 integer<ST>
```

Here `<OSC>` is the bytes `0x1b 0x5d` and `<ST>` is the bytes ``0x1b
0x5c``. This is exactly what is needed for shell integration in kitty. For the
full protocol, that also marks the command region, see `the iTerm2 docs
<https://iterm2.com/documentation-escape-codes.html>`_.

kitty additionally supports several extra fields for the `<OSC>133;A` command
to control its behavior, separated by semi-colons. They are:

`redraw=0`
    this tells kitty that the shell will not redraw the prompt on
    resize so it should not erase it

`special_key=1`
    this tells kitty to use a special key instead of arrow keys
    to move the cursor on mouse click. Useful if arrow keys have side-effects
    like triggering auto complete. The shell integration script then binds the
    special key, as needed.

`k=s`
    this tells kitty that the secondary (PS2) prompt is starting at the
    current line.

`click_events=1|2`
    this tells kitty that the shell is capable of handling
    mouse click events. kitty will thus send a click event to the shell when
    the user clicks somewhere in the prompt. The shell can then move the cursor
    to that position or perform some other appropriate action. Without this,
    kitty will instead generate a number of fake key events to move the cursor
    to the clicked location, which is not fully robust. A value of `1` will
    cause the click events to have absolute y co-ordinates, a value of `2`
    will cause them to have y-coordinates relative to the top line of the
    current prompt. In relative mode, y is zero for cells on the top line of
    the current prompt. The current prompt here is either the secondary (PS2) or
    primary prompt. If the secondary prompt is on the same line or above the
    mouse position, then the reported y will be with respect to that, otherwise
    with respect to the primary prompt. The click event is encoded in the SGR
    encoding from xterm.

kitty also optionally supports sending the cmdline going to be executed with `<OSC>133;C` as:

```none
<OSC>133;C;cmdline=cmdline encoded by %q<ST>
or
<OSC>133;C;cmdline_url=cmdline as UTF-8 URL %-escaped text<ST>
```

Here, *encoded by %q* means the encoding produced by the %q format to printf in
bash and similar shells. Which is basically shell escaping with the addition of
using `ANSI C quoting
<https://www.gnu.org/software/bash/manual/html_node/ANSI_002dC-Quoting.html#ANSI_002dC-Quoting>`__
for control characters (`$''` quoting).
