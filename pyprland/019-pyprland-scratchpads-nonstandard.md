---
title: Troubleshooting scratchpads | Pyprland web
url: https://hyprland-community.github.io/pyprland/scratchpads/nonstandard
source: github_pages
fetched_at: 2026-01-31T16:01:19.767725203-03:00
rendered_js: true
word_count: 45
summary: Configures window matching and process tracking settings for a scratchpad functionality, including various match methods and window rule skipping options.
tags:
    - window-management
    - process-tracking
    - configuration
    - scratchpad
    - match-methods
    - window-rules
category: configuration
---

OptionDescription[`[scratchpad].match_by`i](#config-match-by "More details below")str

=`"pid"`

Match method: pid, class, initialClass, title, initialTitle`[scratchpad].initialClass`strMatch value when match\_by='initialClass'`[scratchpad].initialTitle`strMatch value when match\_by='initialTitle'`[scratchpad].title`strMatch value when match\_by='title'[`[scratchpad].process_tracking`i](#config-process-tracking "More details below")bool

=`true`

Enable process management[`[scratchpad].skip_windowrules`i](#config-skip-windowrules "More details below")listRules to skip: aspect, float, workspace

### `match_by` str=`"pid"` [​](#config-match-by)

### `process_tracking` bool=`true` [​](#config-process-tracking)

### `skip_windowrules` list [​](#config-skip-windowrules)