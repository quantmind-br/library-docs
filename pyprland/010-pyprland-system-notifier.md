---
title: system_notifier | Pyprland web
url: https://hyprland-community.github.io/pyprland/system/notifier
source: github_pages
fetched_at: 2026-01-31T16:03:42.530265536-03:00
rendered_js: true
word_count: 144
summary: This document provides configuration details for a system notification plugin that handles long-running commands and text stream parsing with customizable patterns and sources.
tags:
    - configuration
    - notifications
    - system-monitoring
    - regex-patterns
    - command-execution
category: configuration
---

No commands are provided by this plugin.

## Configuration [​](#configuration)

Basic (4)

OptionDescription`command`dictrecommendedThis is the long-running command (eg: `tail -f <filename>`) returning the stream of text that will be updated. A common option is the system journal output (eg: `journalctl -u nginx`)`parser`dictSets the list of rules / parser to be used to extract lines of interest Must match a list of rules defined as `system_notifier.parsers.<parser_name>`.[`sources`i](#config-sources "More details below")listrecommendedSource definitions with command and parser`pattern`strrecommendedThe pattern is any regular expression that should trigger a match.

Behavior (1)

OptionDescription[`use_notify_send`i](#config-use-notify-send "More details below")bool

=`false`

Use notify-send instead of Hyprland notifications

Appearance (1)

OptionDescription`default_color`str

=`"#5555AA"`

Default notification color

Parsers (1)

OptionDescription[`parsers`i](#config-parsers "More details below")dictrecommendedCustom parser definitions (name -&gt; list of rules). Each rule has: pattern (required), filter, color (defaults to default\_color), duration (defaults to 3 seconds)

### `sources` listrecommended [​](#config-sources)

### `parsers` dictrecommended [​](#config-parsers)

### `use_notify_send` bool=`false` [​](#config-use-notify-send)

When enabled, forces use of `notify-send` command instead of the compositor's native notification system.