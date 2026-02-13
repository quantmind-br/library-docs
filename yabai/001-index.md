---
title: Home
url: https://github.com/asmvik/yabai/wiki
source: wiki
fetched_at: 2026-02-11T07:34:16.684044-03:00
rendered_js: false
word_count: 812
summary: This document introduces yabai, a tiling window manager for macOS, outlining its features, system requirements, installation caveats, and a quickstart guide for new users.
tags:
    - macos
    - window-management
    - tiling-window-manager
    - yabai
    - automation
    - system-configuration
category: guide
---

<h1 align="center">yabai</h1>
<p align="center">Tiling window management native to the Mac.</p>
<p align="center">
    <a href="https://github.com/asmvik/yabai/blob/master/LICENSE.txt"><img src="https://img.shields.io/github/license/asmvik/yabai.svg?color=green" alt="license"></a>
    <a href="https://github.com/asmvik/yabai/blob/master/doc/yabai.asciidoc"><img src="https://img.shields.io/badge/view-documentation-green.svg" alt="documentation"></a>
    <a href="https://github.com/asmvik/yabai/blob/master/CHANGELOG.md"><img src="https://img.shields.io/badge/view-changelog-green.svg" alt="changelog"></a>
    <a href="https://github.com/asmvik/yabai/releases"><img src="https://img.shields.io/github/commits-since/asmvik/yabai/latest.svg?color=green" alt="version"></a>
</p>

### What is yabai?

yabai is a tiling window manager for macOS Big Sur 11.0.0+, Monterey 12.0.0+, Ventura 13.0.0+, Sonoma 14.0.0+, and Sequoia 15.0+.  
  
It automatically modifies your window layout using a binary space partitioning algorithm to allow you to focus on the content of your windows without distractions.

A flexible and easy-to-grok command line interface allows you to control and query windows, spaces and displays to enable powerful integration with tools like [&nearr;&nbsp;skhd][gh-skhd] to allow you to work more efficiently with macOS. Create custom keybindings to control windows, spaces and displays in practically no time and get your hands off the mouse and trackpad and back onto the keyboard where actual work gets done.

### Installation requirements

Please read the below requirements and recommendations carefully. Make sure you fulfill all requirements before filing an issue.

|Requirement|Note|
|-:|:-|
|Operating&nbsp;System&nbsp;Intel x86-64|Big Sur 11.0.0+, Monterey 12.0.0+, Ventura 13.0.0+, Sonoma 14.0.0+, and Sequoia 15.0+ is supported.|
|Operating&nbsp;System&nbsp;Apple Silicon|Monterey 12.0.0+, Ventura 13.0.0+, Sonoma 14.0.0+, and Sequoia 15.0+ is supported.|
|Accessibility&nbsp;API|yabai must be given permission to utilize the Accessibility API and will request access upon launch. The application must be restarted after access has been granted.|
|Screen Recording|yabai must be given Screen Recording permission if and only if you want to enable window animations, and will request access when necessary. The application must be restarted after access has been granted.|
|System&nbsp;Preferences&nbsp;(macOS 11.x, 12.x)|In the Mission Control pane, the setting "Displays have separate Spaces" must be enabled.|
|System&nbsp;Settings&nbsp;(macOS 13.x, 14.x, 15.x)|In the Desktop & Dock tab, inside the Mission Control pane, the setting "Displays have separate Spaces" must be enabled.|


Please also take note of the following caveats.

|Caveat|Note|
|-:|:-|
|System&nbsp;Integrity&nbsp;Protection (Optional)|System Integrity Protection can be (partially) disabled for yabai to inject a scripting addition into Dock.app for controlling windows with functions that require elevated privileges. This enables control of the window server, which is the sole owner of all window connections, and enables additional features of yabai.|
|Code&nbsp;Signing|When building from source (or installing from HEAD), it is necessary to codesign the binary so it retains its accessibility and automation privileges when updated or rebuilt.|
|Finder&nbsp;Desktop|Some people disable the Finder Desktop window using an undocumented defaults write command. This breaks focusing of empty spaces and should be avoided when using yabai. To re-activate the Finder Desktop, run: defaults write com.apple.finder CreateDesktop -bool true|
|NSDocument-based&nbsp;Applications|Windows that utilize native macOS tabs such as Terminal and Finder, [do not behave correctly when creating tabs](https://github.com/asmvik/yabai/issues/68). Avoid creating tabs in these applications, consider alternatives that do not use NSDocument's tab system, or make these windows float using rules.|
|System&nbsp;Preferences&nbsp;(macOS 11.x, 12.x)|In the Mission Control pane, the setting "Automatically rearrange Spaces based on most recent use" should be disabled for commands that rely on the ordering of spaces to work reliably.|
|System&nbsp;Settings&nbsp;(macOS 13.x, 14.x, 15.x)|In the Desktop & Dock tab, inside the Mission Control pane, the setting "Automatically rearrange Spaces based on most recent use" should be disabled for commands that rely on the ordering of spaces to work reliably.|
|System&nbsp;Settings&nbsp;(macOS 14.x, 15.x)|In the Desktop & Dock tab, inside the Desktop & Stage Manager pane, the setting "Show Items On Desktop" should be enabled for display and space focus commands to work reliably in multi-display configurations.|
|System&nbsp;Settings&nbsp;(macOS 14.x, 15.x)|In the Desktop & Dock tab, inside the Desktop & Stage Manager pane, the setting "Click wallpaper to reveal Desktop" should be set to "Only in Stage Manager" for display and space focus commands to work reliably.|


### Quickstart guide

yabai can be installed via Homebrew from a custom tap. It does, however, require you to partially disable System Integrity Protection ("rootless"), because it controls windows by acting through Dock.app&thinsp;—&thinsp;which is the sole owner of the main connection to the window server.

1. Optional: Partially disable System Integrity Protection (required for many advanced features)
2. Install yabai and configure macOS to allow it to run
3. Configure yabai to your liking
4. Optional: Integrate yabai with other software like [&nearr;&nbsp;skhd][gh-skhd] for keyboard shortcuts or [&nearr;&nbsp;Übersicht][gh-uebersicht] for desktop widgets

You can find detailed instructions on every step of the quickstart guide in this wiki. The sidebar to the right (bottom for mobile devices) has a sorted list of pages with links to individual chapters. 


### Comparison with other window managers

**NOTE:** This feature comparison table is far from complete. Please contribute. It's mostly a placeholder in its current state.

<!-- 
Useful HTML entities for this table:
- Check mark symbol: &#10003;
- Ballot X symbol:   &#10007;
--->

||yabai|[&nearr;&nbsp;Amethyst][gh-amethyst]|
|-:|:-:|:-:|
|**General**|
|Supported macOS versions|11.0–15.0|10.15–15.0|
|Works with SIP enabled|&#10003;*|&#10003;|
|Integrate with 3rd party tools|Signals, Rules and Commands|&#10007;|
|**Windows**|
|Modify window properties|&#10003;|&#10007;|
|**Spaces**|
|Create and destroy spaces|&#10003;|&#10007;|
|Move spaces|&#10003;|&#10007;|
|**Displays**|
|Support multiple displays|&#10003;|&#10003;*|


\* partially  

[gh-skhd]: https://github.com/asmvik/skhd
[gh-uebersicht]: https://github.com/felixhageloh/uebersicht
[gh-amethyst]: https://github.com/ianyh/Amethyst