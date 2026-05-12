---
title: Extend with kittens
title: Kittens intro
word_count: 333
summary: This document provides an overview of 'kittens', a framework within the kitty terminal emulator for creating and using specialized programs to enhance terminal functionality.
category: concept
word_count: 333
optimized: true
optimized_at: 2026-05-04T20:44:49Z
---
optimized: true
optimized_at: 2026-05-04T18:00:00Z
# Extend with kittens

|kitty| has a framework for easily creating terminal programs that make use of
its advanced features. These programs are called kittens. They are used both to
add features to |kitty| itself and to create useful standalone programs.
Some prominent kittens:

icat <kittens/icat>
    Display images in the terminal.

diff <kittens/diff>
    A fast, side-by-side diff for the terminal with syntax highlighting and
    images.

Unicode input <kittens/unicode_input>
    Easily input arbitrary Unicode characters in |kitty| by name or hex code.

Themes <kittens/themes>
    Preview and quick switch between over three hundred color themes.

Fonts <kittens/choose-fonts>
    Preview, fine-tune and quick switch the fonts used by kitty.

Hints <kittens/hints>
    Select and open/paste/insert arbitrary text snippets such as URLs,
    filenames, words, lines, etc. from the terminal screen.

Command palette <kittens/command-palette>
    Browse, search and trigger all keyboard shortcuts and actions from a
    single searchable overlay.

Quick access terminal <kittens/quick-access-terminal>
    Get access to a quick access floating, semi-transparent kitty window
    with a single keypress.

Panel <kittens/panel>
    Draw the desktop wallpaper or docks and panels using arbitrary
    terminal programs.

Choose files <kittens/choose-files>
    Preview and select files at the speed of thought

Remote file <kittens/remote_file>
    Edit, open, or download remote files over SSH easily, by simply clicking on
    the filename.

Transfer files <kittens/transfer>
    Transfer files and directories seamlessly and easily from remote machines
    over your existing SSH sessions with a simple command.

Hyperlinked grep <kittens/hyperlinked_grep>
    Search your files using [ripgrep](https://github.com/BurntSushi/ripgrep)
    and open the results directly in your favorite editor in the terminal,
    at the line containing the search result, simply by clicking on the result
    you want.

Broadcast <kittens/broadcast>
    Type in one kitty window <window> and have it broadcast to all (or a
    subset) of other kitty windows <window>.

SSH <kittens/ssh>
    SSH with automatic shell integration <shell_integration>, connection
    re-use for low latency and easy cloning of local shell and editor
    configuration to the remote host.

Clipboard <kittens/clipboard>
    Copy/paste to the clipboard from shell scripts, even over SSH.

You can also Learn to create your own kittens <kittens/custom>.
