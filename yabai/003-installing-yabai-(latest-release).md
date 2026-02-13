---
title: Installing Yabai (latest Release)
url: https://github.com/asmvik/yabai/wiki/Installing-yabai-(latest-release)
source: wiki
fetched_at: 2026-02-11T07:33:50.898272-03:00
rendered_js: false
word_count: 559
summary: This document provides comprehensive instructions for installing, updating, and configuring yabai on macOS, including specific steps for permissions and scripting additions.
tags:
    - yabai
    - macos-setup
    - installation
    - window-management
    - homebrew
    - scripting-addition
    - automation
category: guide
---

A codesigned binary release can be installed using the yabai [installer script](https://github.com/asmvik/yabai/blob/master/scripts/install.sh); it will always point at the latest release version.

```sh
# install yabai binary into /usr/local/bin and man page yabai.1 into /usr/local/man/man1
curl -L https://raw.githubusercontent.com/asmvik/yabai/master/scripts/install.sh | sh /dev/stdin

# install yabai binary into ~/.local/bin and man page yabai.1 into ~/.local/man
curl -L https://raw.githubusercontent.com/asmvik/yabai/master/scripts/install.sh | sh /dev/stdin ~/.local/bin ~/.local/man
```

Alternatively, Homebrew can also be used from the tap `asmvik/formulae`.

```sh
brew install asmvik/formulae/yabai
```

**macOS Big Sur:**

Open `System Preferences.app` and navigate to `Security & Privacy`, then `Privacy`, then `Accessibility`.
Click the lock icon at the bottom and enter your password to allow changes to the list.

**macOS Ventura and above:**

Open `System Settings.app` and navigate to `Privacy & Security`, then `Accessibility`.
Click the + button at the bottom left of the list view and enter your password to allow changes to the list.

Starting with `yabai --start-service` will prompt the user to allow `yabai` accessibility permissions.
Check the box next to `yabai` to allow accessibility permissions.

If you disabled System Integrity Protection; [configure the scripting addition](https://github.com/asmvik/yabai/wiki/Installing-yabai-(latest-release)#configure-scripting-addition). Afterwards simply start yabai. 

```sh
# start yabai
yabai --start-service
```

### Updating to the latest release

To update yabai to the latest version, simply upgrade it with the yabai installer script or Homebrew (depending on the original installation method) and [reconfigure the scripting addition](https://github.com/asmvik/yabai/wiki/Installing-yabai-(latest-release)#configure-scripting-addition) again:

```sh
# stop yabai
yabai --stop-service

# upgrade yabai with installer script -- (with or without directory override)
curl -L https://raw.githubusercontent.com/asmvik/yabai/master/scripts/install.sh | sh /dev/stdin

# or

# upgrade yabai with homebrew (remove old service file because homebrew changes binary path)
yabai --uninstall-service
brew upgrade yabai

# start yabai
yabai --start-service
```

### Configure scripting addition

**yabai** uses the macOS Mach APIs to inject code into Dock.app; this requires elevated (root) privileges.
You can configure your user to execute *yabai --load-sa* as the root user without having to enter a password. 
To do this, we add a new configuration entry that is loaded by */etc/sudoers*.

```
# create a new file for writing - visudo uses the vim editor by default.
# go read about this if you have no idea what is going on.

sudo visudo -f /private/etc/sudoers.d/yabai

# input the line below into the file you are editing.
#  replace <yabai> with the path to the yabai binary (output of: which yabai).
#  replace <user> with your username (output of: whoami). 
#  replace <hash> with the sha256 hash of the yabai binary (output of: shasum -a 256 $(which yabai)).
#   this hash must be updated manually after upgrading yabai.

<user> ALL=(root) NOPASSWD: sha256:<hash> <yabai> --load-sa
```

If you know what you are doing, the following one-liner can be used to update the sudoers file correctly:
```
echo "$(whoami) ALL=(root) NOPASSWD: sha256:$(shasum -a 256 $(which yabai) | cut -d " " -f 1) $(which yabai) --load-sa" | sudo tee /private/etc/sudoers.d/yabai
```

After the above edit has been made, add the command to load the scripting addition at the top of your yabairc config file.  
This file may not yet exist, and you can read about how to create it and configure yabai [here](https://github.com/asmvik/yabai/wiki/Configuration#configuration-file)

```
# for this to work you must configure sudo such that
# it will be able to run the command without password

yabai -m signal --add event=dock_did_restart action="sudo yabai --load-sa"
sudo yabai --load-sa

# .. more yabai startup stuff
```