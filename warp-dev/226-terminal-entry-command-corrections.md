---
title: Command corrections | Warp
url: https://docs.warp.dev/terminal/entry/command-corrections
source: sitemap
fetched_at: 2026-04-29T15:02:26.19565187-03:00
rendered_js: false
word_count: 129
summary: This document explains the Command Corrections feature, which automatically suggests fixes for misspelled terminal commands or missing flags.
tags:
    - command-corrections
    - terminal-productivity
    - auto-suggest
    - command-line-tools
    - warp-terminal
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What is it

Command Corrections is built on [nvdn/thefuck](https://github.com/nvbn/thefuck). Examples where it helps:

| Type | Before | After |
|---|---|---|
| Misspelled command | `gti checkout myBranchName` | `git checkout myBranchName` |
| Misspelled command | `cd ap/sorce/executtor` | `cd app/source/executor` |
| Missing flag | `git push` | `git push --set-upstream myBranchName` |
| Missing permissions | `./script` | `chmod +x ./script && ./script` |

## How to access it

- Enabled by default. Disable via **Settings** > **Features** > **Terminal Input** > toggle "Suggest corrected commands".
- After an incorrect command, a suggestion panel appears above the Input Editor. `CLICK` or press `→` to insert it.

## How it works

Command Corrections Demo

### Command correction rules

generic — command agnostic (e.g., misspelled executable name)