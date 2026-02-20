---
title: ahk-app-specific-configuration - Komorebi
url: https://lgug2z.github.io/komorebi/cli/ahk-app-specific-configuration.html
source: github_pages
fetched_at: 2026-02-20T08:45:24.715724-03:00
rendered_js: true
word_count: 9
summary: Explains how to use the komorebic command-line tool to generate application-specific AutoHotkey configurations and fixes from YAML files.
tags:
    - komorebi
    - cli-reference
    - autohotkey
    - yaml-configuration
    - window-management
    - app-fixes
category: reference
---

[](https://github.com/LGUG2Z/komorebi/edit/master/docs/cli/ahk-app-specific-configuration.md "Edit this page")[](https://github.com/LGUG2Z/komorebi/raw/master/docs/cli/ahk-app-specific-configuration.md "View source of this page")

```
Generate common app-specific configurations and fixes to use in komorebi.ahk

Usage: komorebic.exe ahk-app-specific-configuration <PATH> [OVERRIDE_PATH]

Arguments:
  <PATH>
          YAML file from which the application-specific configurations should be loaded

  [OVERRIDE_PATH]
          Optional YAML file of overrides to apply over the first file

Options:
  -h, --help
          Print help
```