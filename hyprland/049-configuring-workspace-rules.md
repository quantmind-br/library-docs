---
title: Workspace Rules
url: https://wiki.hypr.land/Configuring/Workspace-Rules/
source: sitemap
fetched_at: 2026-04-26T09:48:26.286679647-03:00
rendered_js: false
word_count: 402
summary: This document explains how to configure workspace-specific behaviors in Hyprland by applying custom rules and utilizing specialized workspace selectors.
tags:
    - hyprland
    - workspace-rules
    - window-management
    - configuration
    - compositor-settings
    - desktop-customization
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Workspace rules define workspace-specific behaviors (e.g., windows without borders or gaps). For layout-specific rules, see the layout page (e.g., [[063-configuring-master-layout|Master Layout → Workspace Rules]]).

## Workspace Selectors

Target existing workspaces with selectors like `r[2-4] w[t1]`. Props are space-separated with no spaces inside props.

| Selector | Meaning |
|---|---|
| `r[A-B]` | ID range from A to B inclusive |
| `s[bool]` | Whether workspace is special |
| `n[bool]` | Whether workspace is a named workspace |
| `n[s:string]` | Named workspace starting with string |
| `n[e:string]` | Named workspace ending with string |
| `m[monitor]` | Monitor selector |
| `w[(flags)A-B]` | Window count range, flags can be `t` (tiled), `f` (floating), `g` (groups), `v` (visible), `p` (pinned) |
| `w[(flags)X]` | Specific window count X with flags |
| `f[-1]` / `f[0]` / `f[1]` / `f[2]` | Fullscreen state: `-1`=none, `0`=fullscreen, `1`=maximized, `2`=fullscreen without state sent |

## Syntax

```ini
workspace = WORKSPACE, RULES
```

- `WORKSPACE` is a valid workspace identifier (see [[061-configuring-dispatchers|Dispatchers → Workspaces]]). Can be a workspace selector but selectors only match *existing* workspaces.
- `RULES` is one or more rules from the table below.

## Examples

```ini
workspace = name:myworkspace, gapsin:0, gapsout:0
workspace = 3, rounding:false, bordersize:0
workspace = w[tg1-4], shadow:false
```

### Smart Gaps

To replicate "smart gaps" / "no gaps when only" from other WMs:

```ini
workspace = w[tv1], gapsout:0, gapsin:0
workspace = f[1], gapsout:0, gapsin:0
windowrule = border_size 0, match:float 0, match:workspace w[tv1]
windowrule = rounding 0, match:float 0, match:workspace w[tv1]
windowrule = border_size 0, match:float 0, match:workspace f[1]
windowrule = rounding 0, match:float 0, match:workspace f[1]
```

### Smart Gaps (Ignoring Special Workspaces)

Combine workspace selectors for fine-grained control:

```ini
workspace = w[tv1]s[false], gapsout:0, gapsin:0
workspace = f[1]s[false], gapsout:0, gapsin:0
windowrule = border_size 0, match:float 0, match:workspace w[tv1]s[false]
windowrule = rounding 0, match:float 0, match:workspace w[tv1]s[false]
windowrule = border_size 0, match:float 0, match:workspace f[1]s[false]
windowrule = rounding 0, match:float 0, match:workspace f[1]s[false]
```

## Rules

| Rule | Type | Description |
|---|---|---|
| `monitor:[m]` | string | Binds workspace to a monitor. See [[043-configuring-monitors|Monitors]] |
| `default:[b]` | bool | Whether this workspace is the default for the given monitor |
| `gapsin:[x]` | int | Gaps between windows (like [[067-configuring-variables|General → gaps_in]]) |
| `gapsout:[x]` | int | Gaps between windows and monitor edges (like [[067-configuring-variables|General → gaps_out]]) |
| `bordersize:[x]` | int | Border size around windows (like [[067-configuring-variables|General → border_size]]) |
| `border:[b]` | bool | Whether to draw borders |
| `shadow:[b]` | bool | Whether to draw shadows |
| `rounding:[b]` | bool | Whether to draw rounded windows |
| `decorate:[b]` | bool | Whether to draw window decorations |
| `persistent:[b]` | bool | Keep workspace alive even if empty and inactive |
| `on-created-empty:[c]` | string | Command executed when workspace is created empty. See [[061-configuring-dispatchers|command syntax]] |
| `defaultName:[s]` | string | Default name for the workspace |
| `layout:[s]` | string | Layout to use for this workspace |
| `animations:[s]` | string | Animation style to use |

### Example Rules

```ini
workspace = 3, rounding:false, decorate:false
workspace = name:coding, rounding:false, decorate:false, gapsin:0, gapsout:0, border:false, monitor:DP-1
workspace = 8,bordersize:8
workspace = name:Hello, monitor:DP-1, default:true
workspace = name:gaming, monitor:desc:Chimei Innolux Corporation 0x150C, default:true
workspace = 5, on-created-empty:[float] firefox
workspace = special:scratchpad, on-created-empty:foot
workspace = 15, animation:slidevert, defaultName:slider
```

Last updated on April 20, 2026

[[048-configuring-window-rules|Window Rules]] [[039-configuring-animations|Animations]]