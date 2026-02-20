---
title: Autohotkey
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/autohotkey.md
source: git
fetched_at: 2026-02-20T08:51:01.370467-03:00
rendered_js: false
word_count: 129
summary: This document provides instructions on how to set up and use AutoHotkey v2 as an alternative configuration and hotkey management tool for the komorebi window manager.
tags:
    - autohotkey
    - komorebi
    - window-manager
    - hotkeys
    - configuration
    - windows-automation
category: guide
---

# AutoHotkey

If you would like to use Autohotkey, please make sure you have AutoHotKey v2
installed.

Generally, users who opt for AHK will have specific needs that can only be
addressed by the advanced functionality of AHK, and so they are assumed to be
able to craft their own configuration files.

If you would like to try out AHK, here is a simple sample configuration which
largely matches the `whkdrc` sample configuration.

```autohotkey
{% include "./komorebi.ahk.txt" %}
```

By default, the `komorebi.ahk` file should be located in the `$Env:USERPROFILE`
directory, however, if `$Env:KOMOREBI_CONFIG_HOME` is set, it should be located
there.

Once the file is in place, you can stop komorebi and whkd by running `komorebic stop --whkd`,
and then start komorebi with Autohotkey by running `komorebic start --ahk`.
