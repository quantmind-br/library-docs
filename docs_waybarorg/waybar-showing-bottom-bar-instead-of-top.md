---
title: Waybar Showing Bottom Bar Instead of Top After Update (Fix Guide) - Waybar
url: https://waybar.org/waybar-showing-bottom-bar-instead-of-top/
source: crawler
fetched_at: 2026-05-11T21:37:22.528149792-03:00
rendered_js: false
word_count: 816
summary: This guide provides troubleshooting steps to fix Waybar positioning issues on Hyprland and other compositors that occur after software updates due to configuration precedence changes.
tags:
    - waybar
    - hyprland
    - linux-desktop
    - window-manager
    - config-management
    - troubleshooting
    - wayland
category: guide
---

After a recent update, many Waybar users especially those running Hyprland have encountered a confusing issue where Waybar suddenly appears at the bottom of the screen instead of the top, even though no configuration changes were made. This behavior often happens without any error messages, making it difficult to understand what went wrong.

As a result, users frequently turn to Reddit and forums but find only partial answers or guesses. This guide breaks down the real causes behind this issue, explains why it’s poorly documented, and provides clear, step-by-step solutions to fix Waybar’s position properly and prevent it from happening again.

## Why This Issue Happens After an Update

This problem usually appears after updating one of the following:

- [Waybar](https://waybar.org/)
- Hyprland
- A Waybar config framework (HyDE, dotfiles, custom scripts)

The key reason is configuration precedence changes introduced by updates.

### What Changed?

**Waybar now:**

- May load a different config file than before
- May default to a bar definition without position: top
- May apply layer-shell rules differently under Hyprland

Because of this, Waybar silently falls back to a bottom-positioned bar, without showing any error.

### Common Symptoms Users Report

If you’re affected, you’ll usually see one or more of these:

- Waybar appears at the bottom after reboot
- You see two bars (top + bottom)
- Your top bar config exists, but Waybar ignores it
- No error logs, no warnings
- Worked perfectly before the update

## Step 1: Confirm Which Config Waybar Is Actually Using

**Run this in a terminal:**

```
waybar -l debug
```

**Look for lines like:**

```
Loading config file: /home/user/.config/waybar/config
```

**Many users discover that:**

- Waybar is not using the config they edited
- A framework or theme is overriding it

### Common Locations to Check

- `~/.config/waybar/config`
- `~/.config/waybar/config.jsonc`
- `~/.config/waybar/conf.d/`
- Framework paths (HyDE, custom dotfiles)

## Step 2: Explicitly Set the Bar Position

Open the active config file and force the position:

```
{
  "position": "top",
  "layer": "top",
  "height": 30
}
```

**Why this matters:**

- Older configs relied on defaults
- Newer Waybar versions no longer assume `top`

If `position` is missing, Waybar may place the bar at the bottom.

### Step 3: Check for Multiple Bar Definitions

Waybar supports multiple bars, but after updates this often causes confusion.

**Search your config directory:**

```
grep -R '"position"' ~/.config/waybar
```

**If you find something like:**

```
"bar-bottom": {
  "position": "bottom"
}
```

Waybar may be loading that bar instead of your top bar.

**Fix**

- Remove unused bar definitions
- Or explicitly start Waybar with the correct config:

```
waybar -c ~/.config/waybar/config
```

### Step 4: Hyprland Layer-Shell Interaction (Important)

On Hyprland, Waybar depends on layer-shell rules.

**Make sure your config includes:**

```
"layer": "top",
"exclusive": true
```

**Without this:**

- Waybar may be pushed to the bottom
- Windows may overlap the bar
- Position may appear inconsistent

### Step 5: Restart Waybar Properly

**Don’t just log out. Use:**

```
pkill waybar
waybar &
```

**Or on Hyprland:**

```
hyprctl dispatch exec waybar
```

This ensures the new config is actually reloaded.

### Quick Checklist (TL;DR)

✔ Confirm which config Waybar loads  
✔ Explicitly set “position”: “top”  
✔ Remove extra bar definitions  
✔ Set “layer”: “top” on Hyprland  
✔ Restart Waybar manually

## Frequently Asked Questions

#### Why did Waybar move to the bottom after an update?

Waybar updates can change how configuration files are loaded or how default values are handled. If your config does not explicitly define `"position": "top"`, Waybar may fall back to a bottom bar without showing any error.

#### Does this issue happen only on Hyprland?

It happens most often on Hyprland, but it can also occur on Sway or other Wayland compositors if Waybar loads a different config or if layer-shell behavior changes after an update.

#### Why does Waybar show no errors when this happens?

Waybar silently ignores missing or deprecated config options. If a bar position is not explicitly set, it does not log a warning, which makes the issue hard to debug.

#### Can multiple Waybar configs cause the bar to appear at the bottom?

Yes. If you have multiple config files or bar definitions (for example from dotfiles or frameworks like HyDE), Waybar may load a bottom bar config instead of your intended top bar.

#### Is `"layer": "top"` required to fix this issue?

On Hyprland, yes. Setting `"layer": "top"`ensures Waybar stays above windows and prevents it from being pushed to the bottom by layer-shell changes.

#### Why does restarting Waybar sometimes not apply the fix?

Logging out or restarting the compositor may not reload the correct config. You must fully kill Waybar `(pkill waybar)` and start it again to ensure the updated configuration is applied.

#### Will future Waybar updates break my bar position again?

Possibly. Waybar occasionally introduces silent breaking changes. To avoid this, always define critical options like `"position"`, `"layer"`, and `"exclusive"` explicitly in your config.

## Conclusion

If Waybar starts showing at the bottom instead of the top after an update, the issue is almost never random. In most cases, it’s caused by configuration precedence changes, missing explicit position settings, or multiple bar definitions being loaded silently. Because Waybar does not clearly log these changes, the problem often confuses users and leads to unanswered Reddit threads. The fix is straightforward once you know what to check: confirm the active config file, explicitly set `"position": "top"`, define the correct layer behavior, and remove conflicting bar configs.