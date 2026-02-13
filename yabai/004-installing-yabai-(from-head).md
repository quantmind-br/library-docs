---
title: Installing Yabai (from HEAD)
url: https://github.com/asmvik/yabai/wiki/Installing-yabai-(from-HEAD)
source: wiki
fetched_at: 2026-02-11T07:33:46.28565-03:00
rendered_js: false
word_count: 597
summary: This document provides instructions for installing and updating the development version of yabai on macOS, including details on codesigning, accessibility permissions, and scripting addition setup.
tags:
    - yabai
    - macos-setup
    - codesigning
    - homebrew
    - window-management
    - scripting-addition
category: guide
---

If you want to run the latest and greatest version of yabai, you can install off of `HEAD`. Note that this will require codesigning with a self-signed certificate, so you'll have to create one first (and only once).

First, open `Keychain Access.app`. In its menu, navigate to `Keychain Access`, then `Certificate Assistance`, then click `Create a Certificate...`. This will open the `Certificate Assistant`. Choose these options:

- Name: `yabai-cert`,
- Identity Type: `Self-Signed Root`
- Certificate Type: `Code Signing`

Click `Create`, then `Continue` to create the certificate.

If you already have a release version installed, you need to uninstall that first due to how brew works:

```sh
brew uninstall asmvik/formulae/yabai
```

Now onto installing yabai:

```sh
brew install asmvik/formulae/yabai --HEAD
codesign -fs 'yabai-cert' $(brew --prefix yabai)/bin/yabai
```

**macOS Big Sur:**

Open `System Preferences.app` and navigate to `Security & Privacy`, then `Privacy`, then `Accessibility`.
Click the lock icon at the bottom and enter your password to allow changes to the list.

**macOS Ventura and above:**

Open `System Settings.app` and navigate to `Privacy & Security`, then `Accessibility`.
Click the + button at the bottom left of the list view and enter your password to allow changes to the list.

Starting with `yabai --start-service` will prompt the user to allow `yabai` accessibility permissions.
Check the box next to `yabai` to allow accessibility permissions.

If you disabled System Integrity Protection; [configure the scripting addition](https://github.com/asmvik/yabai/wiki/Installing-yabai-(from-HEAD)#configure-scripting-addition). Afterwards simply start yabai. 

```sh
# start yabai
yabai --start-service
```

### Updating to latest HEAD

To upgrade yabai to the latest version from HEAD, simply reinstall it with Homebrew, codesign it, and [reconfigure the scripting addition](https://github.com/asmvik/yabai/wiki/Installing-yabai-(from-HEAD)#configure-scripting-addition) again:

```sh
# set codesigning certificate name here (default: yabai-cert)
export YABAI_CERT=

# stop yabai
yabai --stop-service

# reinstall yabai (remove old service file because homebrew changes binary path)
yabai --uninstall-service
brew reinstall asmvik/formulae/yabai
codesign -fs "${YABAI_CERT:-yabai-cert}" "$(brew --prefix yabai)/bin/yabai"

# finally, start yabai
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