---
title: Pwsh app specific configuration
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/pwsh-app-specific-configuration.md
source: git
fetched_at: 2026-02-20T08:49:20.533455-03:00
rendered_js: false
word_count: 48
summary: This document provides usage instructions for a command that generates PowerShell scripts to apply application-specific configurations and fixes from YAML files.
tags:
    - komorebi
    - powershell
    - cli-reference
    - configuration-management
    - yaml
category: reference
---

# pwsh-app-specific-configuration

```
Generate common app-specific configurations and fixes in a PowerShell script

Usage: komorebic.exe pwsh-app-specific-configuration <PATH> [OVERRIDE_PATH]

Arguments:
  <PATH>
          YAML file from which the application-specific configurations should be loaded

  [OVERRIDE_PATH]
          Optional YAML file of overrides to apply over the first file

Options:
  -h, --help
          Print help

```
