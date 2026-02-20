---
title: Komorebi config home
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/komorebi-config-home.md
source: git
fetched_at: 2026-02-20T08:51:11.418852-03:00
rendered_js: false
word_count: 171
summary: This document explains how to use the KOMOREBI_CONFIG_HOME environment variable to relocate configuration files to a custom directory. It provides steps for updating the PowerShell profile and the main komorebi settings file.
tags:
    - komorebi
    - configuration-management
    - environment-variables
    - powershell
    - windows-tiling-window-manager
category: configuration
---

# `KOMOREBI_CONFIG_HOME`

If you do not want to keep _komorebi_-related files in your `$Env:USERPROFILE`
directory, you can specify a custom directory by setting the
`$Env:KOMOREBI_CONFIG_HOME` environment variable.

For example, to use the `~/.config/komorebi` directory:

```powershell
# Run this command to make sure that the directory has been created
mkdir -p ~/.config/komorebi

# Run this command to open up your PowerShell profile configuration in Notepad
notepad $PROFILE

# Add this line (with your login user!) to the bottom of your PowerShell profile configuration
$Env:KOMOREBI_CONFIG_HOME = 'C:\Users\LGUG2Z\.config\komorebi'

# Save the changes and then reload the PowerShell profile
. $PROFILE
```

If you already have configuration files that you wish to keep, move them to the
`~/.config/komorebi` directory.

The next time you run `komorebic start`, any files created by or loaded by
_komorebi_ will be placed or expected to exist in this folder.

After setting `$Env:KOMOREBI_CONFIG_HOME`, make sure to update the path in komorebi.json:

```json
{
  "app_specific_configuration_path": "$Env:KOMOREBI_CONFIG_HOME/applications.json"
}
```

This ensures that komorebi can locate all configuration files correctly.

[![Watch the tutorial
video](https://img.youtube.com/vi/C_KWUqQ6kko/hqdefault.jpg)](https://www.youtube.com/watch?v=C_KWUqQ6kko)
