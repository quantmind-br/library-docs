---
title: Waybar Not Showing Icons – Easy Fixes for Beginners - Waybar
url: https://waybar.org/waybar-not-showing-icons/
source: crawler
fetched_at: 2026-05-11T21:38:46.991295915-03:00
rendered_js: false
word_count: 615
summary: This guide provides troubleshooting steps to resolve missing or broken icons in the Waybar status bar by addressing font dependencies and configuration settings.
tags:
    - waybar
    - linux-customization
    - wayland
    - nerd-fonts
    - troubleshooting
    - hyprland
    - sway
category: guide
---

Waybar is a powerful and flexible status bar for Wayland compositors, but many beginners face a common problem: icons not showing correctly or missing completely. This issue can be confusing, especially after a fresh install or when switching to Hyprland or Sway. In most cases, the problem is not serious and can be fixed easily with a few simple steps.

This beginner-friendly guide explains why Waybar icons disappear and provides easy, step-by-step solutions to fix the issue without breaking your configuration. No advanced Linux knowledge is required just follow along and get your Waybar looking perfect again.

## Common Reasons Why Waybar Icons Are Not Showing

Before fixing the issue, it helps to understand why it happens. The most common causes are:

- Missing icon fonts (like Nerd Fonts)
- Incorrect font settings in [Waybar config](https://waybar.org/waybar-config-for-hyprland-beginners/)
- Waybar not reloaded after changes
- Broken or outdated configuration
- System tray or module misconfiguration

The good news? All of these are easy to fix.

### Fix 1: Install Nerd Fonts (Most Common Solution)

Waybar uses icons from Nerd Fonts. If they are not installed, icons will not appear.

**Install Nerd Fonts on Arch Linux:**

```
sudo pacman -S ttf-nerd-fonts-symbols
```

**You can also install a full Nerd Font like:**

```
sudo pacman -S ttf-jetbrains-mono-nerd
```

After installation, restart Waybar.

### Fix 2: Set the Correct Font in Waybar Config

Open your Waybar style file (usually `~/.config/waybar/style.css`) and add:

```
* {
  font-family: "JetBrainsMono Nerd Font", sans-serif;
}
```

Make sure the font name exactly matches the installed font.

### Fix 3: Restart Waybar Properly

Waybar does not always auto-reload changes.

**Restart it manually:**

```
pkill waybar
waybar &
```

Or reload your compositor (Hyprland/Sway).

### Fix 4: Check Module Configuration

Sometimes icons don’t show because the module is disabled or misconfigured.

```
~/.config/waybar/config
```

**Make sure the module exists, for example:**

```
"battery": {
  "format": "{icon} {capacity}%"
}
```

If `{icon}` is missing, icons will not show.

### Fix 5: Icons Showing as Squares or Boxes

**This usually means:**

- Font is installed
- But Waybar is not using it

**Double-check:**

- Font spelling
- Font installed system-wide
- No conflicting font settings

Log out and log back in if needed.

### Fix 6: System Tray Icons Missing

Tray icons need proper support.

**Ensure this module exists:**

```
"tray": {
  "spacing": 10
}
```

Also make sure your apps support Wayland tray icons.

### Fix 7: Update Waybar Safely

An outdated Waybar version may cause icon issues.

**Update on Arch:**

```
sudo pacman -Syu waybar
```

If an update breaks icons, restart Waybar and recheck fonts.

## Frequently Asked Questions

#### Why are Waybar icons not showing after installation?

This usually happens because Nerd Fonts are not installed or Waybar is not using the correct font in its configuration.

#### Which font is best for Waybar icons?

Nerd Fonts like JetBrains Mono Nerd Font or Symbols Nerd Font work best and support most Waybar icons.

#### Do I need to restart Waybar after fixing icons?

Yes. Waybar must be restarted manually for font and configuration changes to take effect.

#### Why do Waybar icons appear as squares or empty boxes?

This means the required icon font is missing or not correctly set in the Waybar style file.

#### Are Waybar icon issues common on Hyprland?

Yes. Many beginners using Hyprland face this issue due to missing fonts or tray configuration problems.

#### Can a Waybar update cause icons to disappear?

Yes. Updates can reset or break font settings, which may cause icons to stop displaying correctly.

#### Do I need to reinstall Waybar to fix missing icons?

No. Reinstalling Waybar is usually unnecessary. Installing fonts and restarting Waybar is enough.

## Conclusion

If Waybar icons are not showing, the issue is usually caused by missing fonts or small configuration mistakes. Most beginners face this problem after a fresh install or system update, but the fix is simple. By installing Nerd Fonts, setting the correct font in the Waybar style file, and restarting Waybar properly, you can restore all icons in just a few minutes. There is no need to reinstall Waybar or change complex settings.