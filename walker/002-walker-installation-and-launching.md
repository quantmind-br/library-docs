---
title: Installation and Launching | Walker
url: https://benz.gitbook.io/walker/installation-and-launching
source: sitemap
fetched_at: 2026-02-01T13:48:37.208383263-03:00
rendered_js: false
word_count: 182
summary: This document provides instructions for installing and configuring the Walker and Elephant desktop applications, including package manager installation methods, manual compilation steps, and optimization techniques for faster startup times.
tags:
    - walker
    - elephant
    - installation
    - desktop-applications
    - gtk4
    - optimization
    - systemd
    - package-manager
category: guide
---

```
yay -S walker
// for example
yay -S elephant elephant-desktopapplications
```

Will install a basic OOTB Walker+Elephant setup.

```
sudo dnf copr enable errornointernet/walker
sudo dnf install walker
sudo dnf install elephant
```

```
# Dependencies
sudo zypper install git cargo gtk4-devel gtk4-layer-shell-devel libpoppler-glib-devel protobuf-devel cairo-devel go make
# Walker
git clone https://github.com/abenz1267/walker.git ~/Downloads/walker
cd ~/Downloads/walker
sudo make install
# Elephant
git clone https://github.com/abenz1267/elephant ~/Downloads/elephant
cd ~/Downloads/elephant
sudo make install
# Provider desktopapplications
cd ~/Downloads/elephant/internal/providers/desktopapplications
sudo make install
# Provider menus
cd ~/Downloads/elephant/internal/providers/menus
sudo make install
# Provider files
cd ~/Downloads/elephant/internal/providers/files
sudo make install
```

Elephant has to be running in order for Walker to function.

Starting Elephant is best done as a user-service: you can use `elephant service enable` to generate a systemd user-level service. It will install and enable it, but won't start it. `systemctl --user start elephant.service` in order to start it without rebooting. When Elephant is running, you can simply launch Walker with `walker`! Done.

Since Walker is based on GTK4, it is by nature slow to startup. A lot of things have to be done each time you open it ⇒ slow. This can be optimized, by keeping a Walker instance running with `walker --gapplication-service` This way everything required in order to launch Walker (parsing config, setting up UI etc) is only done once. Furthermore, you can make Walker popup via a socket call, f.e. `nc -U /run/user/1000/walker/walker.sock` . This is further improve the time till Walker appears on your screen, by avoiding any GTK4 cmdline parsing. So this can be used as a faster alternative to simply calling `walker`.

Last updated 3 months ago