---
title: Run offline
url: https://github.com/kholia/OSX-KVM/blob/master/run_offline.md
source: git
fetched_at: 2026-02-04T11:39:11.966399334-03:00
rendered_js: false
word_count: 121
summary: This document provides step-by-step instructions for performing an offline installation of macOS Ventura without a macOS host by using OpenCore and a custom ISO image.
tags:
    - macos-installation
    - opencore
    - offline-install
    - ventura
    - virtualization
    - iso-creation
category: guide
---

### How to run the Installation offline without macOS

* Download the Ventura installer (`InstallAssistant.pkg`) from [https://mrmacintosh.com/macos-ventura-13-full-installer-database-download-directly-from-apple/](https://mrmacintosh.com/macos-ventura-13-full-installer-database-download-directly-from-apple/)

* Create an ISO file `InstallAssistant.iso` with the `InstallAssistant.pkg` and
  `scripts/run_offline.sh` files.

  ```
  mkisofs -allow-limited-size -l -J -r -iso-level 3 -V InstallAssistant -o InstallAssistant.iso path/to/InstallAssistant.pkg scripts/run_offline.sh
  ```

* Add the following to your `OpenCore-Boot.sh`

  ```
  -drive id=MacDVD,if=none,file="$REPO_PATH/InstallAssistant.iso",format=raw
  -device ide-hd,bus=sata.5,drive=MacDVD
  ```

* Run `./OpenCore-Boot.sh` from the terminal

* Use the `Disk Utility` tool within the macOS installer to partition, and
  format the virtual disk attached with name **macOS**

* When completed, close `Disk Utility`

* Go to the Terminal in your virtual machine, Click `Utilities`, select `Terminal`

* Run the `sh /Volumes/InstallAssistant/run_offline.sh` command

* Wait for a few minutes for the installation window to appear
