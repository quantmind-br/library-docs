---
title: The Zellij Filepicker
url: https://zellij.dev/tutorials/filepicker/
source: sitemap
fetched_at: 2026-01-24T15:53:04.363100334-03:00
rendered_js: false
word_count: 630
summary: This tutorial provides instructions for using and configuring the Zellij filepicker, also known as Strider, to navigate filesystems and integrate with other terminal commands. It covers setup via keybindings, CLI usage, and creating IDE-like layouts.
tags:
    - zellij
    - file-navigation
    - strider-plugin
    - terminal-productivity
    - keybindings
    - cli-tools
    - workflow
category: tutorial
---

This tutorial shows how to use the Zellij filepicker, also known as Strider.

*The video screencast and the tutorial contain the same content, with the video screencast also containing some concrete examples of the subject material for inspiration.*

## Why use the Zellij filepicker?

The Zellij filepicker is a built-in plugin that will allow you to dynamically traverse your filesystem, optionally using fuzzy finding to look for files or folders in a deterministic way. It’s much faster than doing the usual cycle of “cd”, “ls”, look for folder, “cd” and “ls” again.

It’s also versatile: you can launch the filepicker directly and close it once you’ve chosen a file, you can keep it open to open multiple files and you can even insert it into traditional shell pipelines to pipe your chosen path into a different command.

## What we’ll cover

- [Basic usage of the filepicker](#basic-usage-of-the-filepicker)
- [How to launch the filepicker through a keybinding](#how-to-launch-the-filepicker-through-a-keybinding)
- [How to launch the filepicker from the command line](#how-to-launch-the-filepicker-from-the-command-line)
- [How to get an IDE-like experience with the filepicker](#how-to-get-an-ide-like-experience-with-the-filepicker)
- [How to pipe the filepicker’s output to another command](#how-to-pipe-the-filepickers-output-to-another-command)
- [Do you like Zellij?](#do-you-like-zellij-)

## Basic usage of the filepicker

![An image of Zellij filepicker.](https://zellij.dev/img/tutorial-4-preview.png)

When launching the filepicker, it will start in the working directory of the focused pane. We are presented with a list of the files and folders, allowing us to traverse through them with the arrow keys, backspace and tab.

When we select a file or folder (either with the right arrow or with `<TAB>`), it will be added to our `PATH:`. When we press `<ENTER>`, the filepicker will open whatever is in the `PATH:` either in our default editor if it’s a file or open a terminal to this location if it’s a folder.

We can toggle hidden files on and off with `Ctrl e`.

## How to launch the filepicker through a keybinding

To launch the filepicker through a keyboard shortcut, we’ll need to add the following lines (starting from `bind`) to the `shared_except "locked"` section of our `keybindings` in the [configuration file](https://zellij.dev/documentation/configuration.html).

For more info, please see [configuring keybindings](https://zellij.dev/documentation/keybindings.html).

```
shared_except "locked" {
// ...
    bind "Alt f" {
        LaunchPlugin "filepicker" {
            // floating true // uncomment this to have the filepicker opened in a floating window
            close_on_selection true // comment this out to have the filepicker remain open even after selecting a file
        };
    }
}
```

## How to launch the filepicker from the command line

To launch the filepicker from the command line:

```
zellij plugin -- filepicker
```

## How to get an IDE-like experience with the filepicker

![An image of Zellij filepicker opened on the side, similar to an IDE.](https://zellij.dev/img/tutorial-4-ide-like.png)

We can get an “IDE-like” experience of having the filepicker always open on the side by using the “strider” built in layout.

We can either start a session with it from the command line:

Start a session with it through the [welcome screen](https://zellij.dev/tutorials/session-management).

Or, we could open a new tab with it in an existing session:

```
zellij action new-tab -l strider
```

## How to pipe the filepicker’s output to another command

We can also pipe the output of the filepicker - our chosen file or folder - into another command with a traditional CLI pipeline.

To do this, we launch the filepicker through the `zpipe` alias (or using `zellij pipe`):

```
zpipe filepicker
zellij pipe -p filepicker
```

This will open the filepicker, allowing us to choose a file or folder. Once we press `<ENTER>`, the filepicker will close and print our chosen path to `STDOUT`. This means that we can use it to select paths dynamically and send them to other commands, for example:

```
zpipe filepicker | xargs -i cp {} my-chosen-file
```

This will open the filepicker so that we can select a file and then copy this file to `my-chosen-file` in our local directory.

## Do you like Zellij? ❤️

Me too. So much so that I spend 100% of my time developing and maintaining it and have no other income.

Zellij will always be free and open-source. Zellij will never contain ads or collect your data.

If the tool gives you value and you are able, please consider [a recurring monthly donation](https://github.com/sponsors/imsnif) of 5-10$ to help me pay my bills. There are Zellij stickers in it for you!